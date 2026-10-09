"""Reproducible motion digital gate. Missing evidence always fails; no hardware claims."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from software.motion.trap_solver import digest


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='build/motion_gate')
    parser.add_argument('--skip-regression',action='store_true');args=parser.parse_args()
    out=(ROOT/args.output).resolve();out.mkdir(parents=True,exist_ok=True)
    summary={'status':'RUNNING','classification':'SIMULATION_VALIDATED_PENDING','commands':[],
             'limits':'PROVISIONAL_UNTIL_HARDWARE_VALIDATED','gui':'Tk 8.6; PySide6 absent in pinned environment',
             'timing':'GUI controls no field clock. RTL queue is clocked at 132 MHz, 2,640,000 cycles production cadence; full waveform demo shortens interval to 8192 cycles.',
             'not_verified':['physical particle movement','absolute force / mass support','PS transport deployment',
                             'board synthesis / pin constraints / timing closure','hardware enable and watchdog circuit'],
             'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}

    def run(label,argv,cwd=ROOT,timeout=1800):
        started=time.monotonic()
        p=subprocess.run([str(x) for x in argv],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                         text=True,errors='replace',timeout=timeout)
        (out/(label+'.log')).write_text(p.stdout,encoding='utf-8')
        summary['commands'].append({'label':label,'argv':[str(x) for x in argv],'exit_code':p.returncode,
                                    'elapsed_s':round(time.monotonic()-started,3)})
        print(label+': '+str(p.returncode),flush=True)
        if p.returncode or 'FATAL:' in p.stdout or 'Fatal:' in p.stdout:
            raise RuntimeError(label+' failed: '+p.stdout[-2000:])
        return p.stdout

    try:
        run('python_tests',[sys.executable,'-m','unittest','discover','-s','tests','-v'])
        iv=Path(os.environ.get('IVERILOG_BIN','C:/iverilog/bin'))
        vb=Path(os.environ.get('VIVADO_BIN','D:/Vivado/2025.2/2025.2/Vivado/bin'))
        faults=out/'faults';faults.mkdir(exist_ok=True)
        rtl=ROOT/'rtl/motion/motion_queue.sv';tb=ROOT/'tb/tb_motion_faults.sv'
        for cadence in (1200,2640000):
            run('compile_faults_'+str(cadence),[iv/'iverilog.exe','-g2012','-s','tb_motion_faults',
                f'-Ptb_motion_faults.INTERVAL_CYCLES={cadence}','-o',f'faults_{cadence}.vvp',rtl,tb],faults)
            text=run('icarus_faults_'+str(cadence),[iv/'vvp.exe',f'faults_{cadence}.vvp'],faults)
            if 'PASS MOTION-RTL10' not in text:raise AssertionError('Incomplete fault tests')
        run('faults_xvlog',[vb/'xvlog.bat','--sv',rtl,tb],faults)
        for cadence in (1200,2640000):
            run('faults_xelab_'+str(cadence),[vb/'xelab.bat','tb_motion_faults' if cadence==1200 else 'tb_motion_cadence',
                                             '--snapshot',f'faults_{cadence}','--debug','typical'],faults)
            text=run('faults_xsim_'+str(cadence),[vb/'xsim.bat',f'faults_{cadence}','--runall'],faults)
            if 'PASS MOTION-RTL10' not in text:raise AssertionError('Incomplete XSim fault tests')
        summary['fault_injection']='PASS: all 10 required cases plus ACK timeout; 1200 and production 2640000 cycles, both tools'
        # Separate output directories make all runs independent. GUI callbacks drive every run.
        def gui(label,simulator):
            dest=out/label
            run(label,[sys.executable,'-m','software.ui.app','--automated-demo','--simulator',simulator,'--output',dest],timeout=1800)
            result=json.loads((dest/'gui_result.json').read_text())
            if result['status']!='PASS' or result['final_status']['commanded_trap_position_mm']!=[0,0,0]:
                raise AssertionError('GUI sequence did not finish at center')
            if [r['command'] for r in result['results']]!=['APPLY_CENTER','RUN_DEMO']:
                raise AssertionError('GUI failed to drive full continuous demonstration')
            return label,result
        jobs=[('gui_icarus_'+str(i),'icarus') for i in range(3)]+[('gui_xsim','xsim')]
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures=[pool.submit(gui,*job) for job in jobs]
            results=dict(f.result() for f in futures)
        summary['gui_results']=results
        key=lambda result:[(r['trajectory_sha256'],r['map_words_sha256'],r['trap_reports_sha256'],r['ack_sha256']) for r in result['results']]
        if any(key(result)!=key(results['gui_icarus_0']) for result in results.values()):
            raise AssertionError('Path/map/trap/RTL ACK repeat or cross-simulator mismatch')
        summary['determinism']={'status':'PASS','runs':4,'independent_simulators':['Icarus','Vivado 2025.2 XSim'],
                                'comparison':'exact canonical JSON and ACK hashes; wall timestamps excluded',
                                'hashes':key(results['gui_icarus_0'])}
        canonical_run=out/'gui_icarus_0';trajectory=json.loads((canonical_run/'trajectory_01.json').read_text())
        summary['frame_count']=len(trajectory)
        if not all(r['validity']=='TRAP_VALID' for r in trajectory):raise AssertionError('Invalid trap transmitted')
        summary['trap_score_min']=min(r['trap_score'] for r in trajectory)
        (out/'phase_map_hashes.txt').write_text('\n'.join(r['phase_map_reference'] for r in trajectory)+'\n')
        with gzip.open(out/'trajectory.json.gz','wt',encoding='utf-8',newline='\n') as f:
            json.dump(trajectory,f,separators=(',',':'),allow_nan=False)
        if not args.skip_regression:
            run('regression',[sys.executable,ROOT/'scripts/validate.py','--output',out/'regression'],timeout=1800)
            summary['regression']='PASS'
        else:summary['regression']='NOT_RUN'
        run('frozen_parent',[sys.executable,ROOT/'scripts/check_migration.py'])
        summary['source_hash_policy']='CANONICAL_LF_UTF8'
        paths=[]
        for folder in ('software','rtl','tb','tests','scripts','config'):
            paths.extend(p for p in (ROOT/folder).rglob('*') if p.suffix in ('.py','.sv','.svh','.tcl','.json'))
        summary['source_sha256']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_text(encoding='utf-8').encode()).hexdigest() for p in paths}
        summary['status']='PARTIAL' if args.skip_regression else 'PASS'
        summary['classification']='SIMULATION_VALIDATED' if summary['status']=='PASS' else 'PARTIAL_DIGITAL_VALIDATION'
    except Exception as exc:
        summary['status']='FAIL';summary['error']=str(exc);raise
    finally:
        (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print('MOTION_GATE '+summary['status'],flush=True)


if __name__=='__main__':main()
