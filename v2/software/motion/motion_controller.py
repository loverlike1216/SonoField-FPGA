"""PS execution reference model: GUI commands, safety state, planner, trap and transport.

This runs on the host for digital validation. No deployment to Zynq PS is claimed.
"""
import json
import threading
import time
from pathlib import Path
from typing import Protocol
from .commands import decode
from .trajectory import Planner,xyz
from .trap_solver import TrapSolver,canonical,digest
from .transport import RegisterTranscriptTransport
from ..control.host import Controller


class MeasuredPositionProvider(Protocol):
    def position_mm(self):
        """Return a timestamped measured position, or None if unavailable."""
        ...


class MotionController:
    def __init__(self, config, profile, transport, log_path):
        self.config=config;self.profile=profile;self.transport=transport
        self.planner=Planner(profile);self.state='SAFE_DISABLED';self.connected=False
        self.solver=None;self.confirmed=False;self.position=[0.0,0.0,0.0]
        self.last_sequence=-1;self.cancel=threading.Event();self.busy=False
        self.log_path=Path(log_path);self.log_path.parent.mkdir(parents=True,exist_ok=True)
        self.last_result=None;self._lock=threading.RLock();self.generation=0
        self.calibration_records={}

    def status(self):
        return dict(state=self.state,connected=self.connected,commanded_trap_position_mm=self.position[:],
                    actual_particle_position='NOT_MEASURED',calibration_id=self.solver.calibration_id if self.solver else None,
                    f_work=self.solver.record['f_work'] if self.solver else None,
                    workspace_profile=self.profile['profile_id'],mode='SIMULATION',busy=self.busy,
                    board_status='NOT_CONNECTED',hardware_enable='NOT_VERIFIED')

    def load_calibration(self,record):
        if not self.connected or self.busy:raise RuntimeError('CONNECT_FIRST_OR_BUSY')
        self.solver=TrapSolver(self.config,record,self.profile,simulation=True)
        self.state='CALIBRATION_READY';self.confirmed=False

    def stop(self):
        with self._lock:
            self.generation+=1;self.cancel.set();self.transport.stop()
            self.confirmed=False;self.state='SAFE_DISABLED';self.busy=False

    def preview(self,command,payload,*,start=None):
        p=payload;planner=self.planner;start=self.position if start is None else start
        if command=='RUN_DEMO':
            if not all(abs(x)<1e-9 for x in start):raise ValueError('DEMO_REQUIRES_CENTER')
            segments=[];current=start
            for child,options in demo_commands():
                segment=self.preview(child,options,start=current);segments.append(segment);current=xyz(segment[-1])
            return planner.join(*segments)
        if command in ('SET_TARGET','RETURN_CENTER'):
            target=[0,0,0] if command=='RETURN_CENTER' else p['target']
            return planner.point_move(start,target,p.get('speed',3),p.get('vertical_speed',2))
        if command=='RUN_VERTICAL':
            target=[*start[:2],p['z']]
            return planner.line(start,target,p.get('speed',2),vertical=True)
        if command=='RUN_LINE':
            end=p['end'];begin=p.get('start',start)
            lead=planner.point_move(start,begin,p.get('speed',3))
            return planner.join(lead,planner.line(begin,end,p.get('speed',3)))
        if command=='RUN_TRAJECTORY':
            path=planner.planar(p['kind'],p['parameters'],p.get('speed',3),p.get('z',start[2]),p.get('repeat',1),p.get('clockwise',False))
            return planner.join(planner.point_move(start,xyz(path[0]),p.get('speed',3)),path)
        if command in ('HOLD','APPLY_CENTER'):
            return planner.hold([0,0,0] if command=='APPLY_CENTER' else start,p.get('duration',.1))
        raise ValueError('Command has no trajectory')

    def prepare(self,path):
        if self.solver is None:raise RuntimeError('CALIBRATION_REQUIRED')
        transcript=RegisterTranscriptTransport();controller=Controller(transcript.read32,transcript.write32)
        reports=[];cal=None
        for row in path:
            if self.cancel.is_set():raise RuntimeError('STOPPED')
            rows,report=self.solver.solve(xyz(row))
            if report['validity']!='TRAP_VALID':raise ValueError('TRAP_INVALID_MODEL')
            signature=[x['calibration_phase'] for x in rows]
            if cal is not None and signature!=cal:raise RuntimeError('Calibration changed during motion')
            cal=signature
            controller.stream_map(rows)
            row.update(phase_map_reference=report['map_sha256'],validity=report['validity'],trap_score=report['trap_score'])
            reports.append(report)
        return transcript,reports

    def execute_path(self,path):
        token=self.generation
        transcript,reports=self.prepare(path)
        if token!=self.generation or self.cancel.is_set():raise RuntimeError('STOPPED')
        result=self.transport.execute(transcript,self.solver.record['f_work'])
        with self._lock:
            if token!=self.generation or self.cancel.is_set():raise RuntimeError('STOPPED')
            self.position=xyz(path[-1]).tolist()
            self.last_result={**result,'trajectory_sha256':digest(path),'frames':len(path),
                              'calibration_id':self.solver.calibration_id,'trap_reports_sha256':digest(reports)}
        return self.last_result,transcript,reports

    def dispatch(self,packet, *, prepared_path=None):
        seq,command,payload=decode(packet)
        with self._lock:
            if seq<=self.last_sequence:raise ValueError('COMMAND_SEQUENCE_REPLAY')
            self.last_sequence=seq
            if self.busy and command not in ('STOP','GET_STATUS'):raise RuntimeError('MOTION_BUSY')
        event={'timestamp':time.time(),'sequence':seq,'command':command,'payload':payload,
               'start_mm':self.position[:],'target_mm':payload.get('target'),
               'trajectory_type':payload.get('kind',command),
               'speed_mm_s':payload.get('speed',2 if command=='RUN_VERTICAL' else
                                       (3 if command in ('SET_TARGET','RUN_LINE','RUN_TRAJECTORY','RETURN_CENTER','RUN_DEMO') else 0)),
               'vertical_speed_mm_s':payload.get('vertical_speed',2),
               'duration_s':0,'update_rate_hz':self.profile['update_rate_hz'],'point_count':0,
               'calibration_id':self.solver.calibration_id if self.solver else None,
               'f_work':self.solver.record['f_work'] if self.solver else None,
               'workspace_profile':self.profile['profile_id'],'abort_fault_reason':None}
        try:
            if command=='STOP':self.stop()
            elif command=='CONNECT':self.connected=True
            elif command=='GET_STATUS':pass
            elif command=='LOAD_CALIBRATION':self.load_calibration(self.calibration_records[payload['calibration_id']])
            elif command=='BALL_AT_CENTER_CONFIRMED':
                if self.state!='WAIT_OPERATOR':raise RuntimeError('APPLY_CENTER_FIRST')
                self.confirmed=True;self.state='ARMED'
            else:
                if not self.connected or self.solver is None:raise RuntimeError('CONNECT_AND_CALIBRATE_FIRST')
                if command=='APPLY_CENTER':
                    if self.confirmed:raise RuntimeError('Use RETURN_CENTER after arming')
                elif not self.confirmed or self.state!='ARMED':raise RuntimeError('OPERATOR_CONFIRMATION_REQUIRED')
                self.cancel.clear();self.transport.cancelled.clear();self.busy=True
                try:
                    planned=self.preview(command,payload)
                    if prepared_path is not None:
                        # GUI preview is an exact approved plan, not a second independent generator.
                        if digest(planned)!=digest(prepared_path):raise ValueError('STALE_PREVIEW')
                        path=prepared_path
                    else:path=planned
                    event.update(target_mm=xyz(path[-1]).tolist(),duration_s=path[-1]['timestamp_target'],point_count=len(path))
                    self.execute_path(path)
                    with self._lock:
                        if self.cancel.is_set():raise RuntimeError('STOPPED')
                        self.state='WAIT_OPERATOR' if command=='APPLY_CENTER' else 'ARMED'
                finally:self.busy=False
            event['result']='PASS';return self.status()
        except Exception as exc:
            event['result']='REJECTED';event['abort_fault_reason']=str(exc)
            # Validation errors before transmission leave a valid hold; transport faults disable.
            if not isinstance(exc,ValueError):self.stop()
            raise
        finally:
            # Calibration content remains in its own database; command logs carry its identifier.
            if command=='LOAD_CALIBRATION':event['payload']={'calibration_id':self.solver.calibration_id if self.solver else None}
            with self.log_path.open('a',encoding='utf-8') as f:f.write(canonical(event)+'\n')
            with self.log_path.with_suffix('.txt').open('a',encoding='utf-8') as f:
                f.write(f"{seq} {command} {event['result']} -> {self.position} {event['abort_fault_reason'] or ''}\n")


def demo_commands():
    return [('HOLD',{'duration':.1}),('RUN_LINE',{'end':[8,0,0],'speed':3}),
            ('RETURN_CENTER',{}),('RUN_TRAJECTORY',{'kind':'CIRCLE','parameters':{'radius':5},'z':0,'speed':3}),
            ('RUN_TRAJECTORY',{'kind':'RECTANGLE','parameters':{'width':8,'height':6},'z':0,'speed':3}),
            ('RETURN_CENTER',{}),('RUN_VERTICAL',{'z':4,'speed':2}),
            ('RUN_VERTICAL',{'z':-4,'speed':2}),('RETURN_CENTER',{})]
