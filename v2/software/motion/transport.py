"""Execution adapters. Register transcripts are plans; only RTL ACKs prove execution."""
import os
import subprocess
import threading
from pathlib import Path
from ..control import registers as r
from .trap_solver import digest
from ..board.serial_transport import SerialBoardTransport

ROOT=Path(__file__).resolve().parents[2]


class RegisterTranscriptTransport:
    """Validate Controller bus writes and collect full maps, without inventing read ACKs."""
    def __init__(self):
        self.frames=[]; self.pending={}; self.channel=None; self.data=None; self.write_count=0

    def read32(self,address):
        raise RuntimeError('TRANSCRIPT_HAS_NO_LIVE_ACK; execute with an RTL transport')

    def write32(self,address,value):
        self.write_count+=1
        if address==r.MAP_CHANNEL:
            if not 0<=value<128: raise ValueError('Invalid map channel')
            self.channel=value
        elif address==r.MAP_DATA:
            if not 0<=value<2**17: raise ValueError('Invalid map word')
            self.data=value
        elif address==r.MAP_WRITE:
            if value!=1 or self.channel is None or self.data is None or self.channel in self.pending:
                raise ValueError('Invalid/duplicate map write')
            self.pending[self.channel]=self.data
            self.channel=None;self.data=None
        elif address==r.MAP_COMMIT:
            if value!=1 or len(self.pending)!=128: raise ValueError('Incomplete atomic map')
            self.frames.append([self.pending[c] for c in range(128)]);self.pending={}
        else: raise ValueError('Unexpected motion register')


class SimulationTransport:
    """Real Icarus/Vivado file-driven RTL execution, faster-than-wall-time simulation.

    Logical 50 Hz sample time is preserved in metadata. The RTL regression uses a
    disclosed shortened interval; production cadence is independently tested.
    """
    def __init__(self, output, *, simulator='icarus', interval_cycles=8192):
        self.output=Path(output).resolve();self.output.mkdir(parents=True,exist_ok=True)
        self.simulator=simulator;self.interval_cycles=interval_cycles
        self.process=None;self.cancelled=threading.Event();self._lock=threading.Lock()

    def stop(self):
        self.cancelled.set()
        with self._lock:
            if self.process and self.process.poll() is None:self.process.terminate()

    def _run(self,label,args,timeout=900):
        if self.cancelled.is_set():raise RuntimeError('STOPPED')
        with self._lock:
            self.process=subprocess.Popen([str(x) for x in args],cwd=self.output,stdout=subprocess.PIPE,
                                          stderr=subprocess.STDOUT,text=True,errors='replace')
        try:output,_=self.process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            self.stop();output,_=self.process.communicate()
            (self.output/(label+'.log')).write_text(output,encoding='utf-8')
            raise TimeoutError(f'SIMULATOR_PROCESS_TIMEOUT: {label} exceeded {timeout}s wall time; RTL cycle timeout is separate')
        (self.output/(label+'.log')).write_text(output,encoding='utf-8')
        if self.cancelled.is_set():raise RuntimeError('STOPPED')
        if self.process.returncode or 'FATAL:' in output or 'Fatal:' in output:
            raise RuntimeError(label+' failed: '+output[-1500:])
        return output

    def execute(self, transcript, frequency):
        if not 1<=len(transcript.frames)<=12000 or transcript.pending:raise ValueError('Invalid bounded trajectory')
        if not 38500<=frequency<=41500:raise ValueError('Invalid working frequency')
        (self.output/'adc_vectors.hex').write_text(('0'*32+'\n')*1024)
        with (self.output/'motion_maps.hex').open('w',newline='\n') as f:
            f.write(f'{len(transcript.frames):08x}\n')
            for row in transcript.frames:
                for word in row:f.write(f'{word:08x}\n')
            f.write(f'@177001\n{int(frequency):08x}\n')  # outside bounded frame data
        rtl=[*sorted((ROOT/'rtl').rglob('*.sv')),ROOT/'tb/ad7606b_model.sv'];tb=ROOT/'tb/tb_motion.sv'
        if self.simulator=='icarus':
            iv=Path(os.environ.get('IVERILOG_BIN','C:/iverilog/bin'))
            self._run('compile',[iv/'iverilog.exe','-g2012','-I',ROOT/'rtl/generated','-s','tb_motion',
                                f'-Ptb_motion.INTERVAL_CYCLES={self.interval_cycles}','-o','motion.vvp',*rtl,tb])
            output=self._run('run',[iv/'vvp.exe','motion.vvp'])
        elif self.simulator=='xsim':
            vb=Path(os.environ.get('VIVADO_BIN','D:/Vivado/2025.2/2025.2/Vivado/bin'))
            if type(self.interval_cycles) is not int or self.interval_cycles<800:raise ValueError('Invalid cadence')
            wrapper=self.output/'tb_motion_configured.sv'
            wrapper.write_text(f'module tb_motion_configured; tb_motion #(.INTERVAL_CYCLES({self.interval_cycles})) tests(); endmodule\n')
            self._run('xvlog',[vb/'xvlog.bat','--sv','-i',ROOT/'rtl/generated',*rtl,tb,wrapper])
            self._run('xelab',[vb/'xelab.bat','tb_motion_configured',
                               '--snapshot','motion_snapshot','--debug','typical'])
            output=self._run('xsim',[vb/'xsim.bat','motion_snapshot','--runall'])
        else:raise ValueError('Unknown simulator')
        if 'PASS MOTION RTL' not in output:raise RuntimeError('RTL_INCOMPLETE')
        lines=(self.output/'motion_ack.txt').read_text().splitlines()
        if len(lines)!=len(transcript.frames):raise RuntimeError('Missing RTL ACK')
        for seq,(line,row) in enumerate(zip(lines,transcript.frames)):
            ack,cycle,effective,mask=line.split()
            expected=sum((((v&255)+((v>>8)&255))&255)<<(8*c) for c,v in enumerate(row))
            expected_mask=sum((v>>16)<<c for c,v in enumerate(row))
            if int(ack)!=seq or int(effective,16)!=expected or int(mask,16)!=expected_mask:
                raise RuntimeError('RTL_ACK_MAP_MISMATCH')
        return {'classification':'SIMULATED','simulator':self.simulator,'frames_acknowledged':len(lines),
                'map_words_sha256':digest(transcript.frames),'ack_sha256':digest(lines),
                'interval_cycles':self.interval_cycles,'production_interval_cycles':2640000,
                'clock_hz':132000000,'bus_writes':transcript.write_count}


class BoardTransport:
    def __init__(self,*args,**kwargs):
        raise RuntimeError('BOARD_TRANSPORT_BLOCKED: verified PS bus, pins, hardware profile and interlock required')
