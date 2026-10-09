"""Self-calibration acceptance: real tools, synthetic estimates, explicit failure envelope."""
import argparse,hashlib,json,os,shutil,subprocess,sys,datetime
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from software.calibration.config import load
from software.calibration.synthetic import generate,truth
from software.calibration.experiment import run as experiment
from software.calibration.database import decode_frames,canonical
from software.calibration.signal import estimate_tof,capture_quality
from software.calibration.visualize import render
from software.calibration.pipeline import phase_lut,process
from software.calibration.report import write_report


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='build/self_calibration_gate')
    parser.add_argument('--skip-xsim',action='store_true');a=parser.parse_args()
    output=(ROOT/a.output).resolve();output.mkdir(parents=True,exist_ok=True)
    work=ROOT/'build/self_calibration_sim';work.mkdir(parents=True,exist_ok=True)
    cfg=load();summary={'status':'RUNNING','classification':'SIMULATION_ESTIMATE','commands':[],
                       'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                       'tolerances':{'repeat_json_csv':'byte-identical canonical LF on same dependencies',
                                     'numeric_repeat_absolute':1e-12,'translation_mm':.1,'rotation_deg':.1,
                                     'f0_rmse_hz':80,'phase_rmse_deg':2},
                       'simulation_only_override':{'POWER_WAIT_CYCLES':32,'production':264000001,
                                                   'reset_and_setup_delays':'unshortened'},
                       'adc_model':'AD7606B Rev B Figure 73; 9ns CS data, 15ns SCLK data, 650/850ns alternating conversion'}
    def command(name,args):
        p=subprocess.run([str(x) for x in args],cwd=work,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,errors='replace',timeout=300)
        (output/(name+'.log')).write_text(p.stdout,encoding='utf-8')
        summary['commands'].append({'name':name,'argv':[str(x) for x in args],'exit_code':p.returncode,'log':name+'.log'})
        print(name+': '+str(p.returncode),flush=True)
        if p.returncode or 'Fatal:' in p.stdout or 'FATAL:' in p.stdout:raise RuntimeError(name+' failed: '+p.stdout[-2000:])
        return p.stdout
    def checks(m):return m['translation_error_mm']<.1 and m['rotation_error_deg']<.1 and m['f0_rmse_hz']<80 and m['phase_rmse_deg']<2
    try:
        command('generated_config',[sys.executable,ROOT/'scripts/generate_system.py','--check'])
        repeats=[]
        for i in range(3):
            dest=work/f'python_repeat_{i}';record,diag,metrics=experiment(dest)
            write_report(record,diag,metrics,dest)
            if not checks(metrics):raise AssertionError('Baseline estimator accuracy outside declared limits')
            hashes={n:hashlib.sha256((dest/n).read_bytes()).hexdigest() for n in ['calibration.json','phase_lut.csv','channel_health.csv','path_quality.csv','quality_summary.json']}
            repeats.append(hashes)
        if repeats[1:]!=[repeats[0]]*2:raise AssertionError('Nondeterministic calibration artifacts')
        summary['synthetic_end_to_end']=metrics;summary['repeated_artifacts']=repeats
        for name in ['calibration.json','phase_lut.csv','channel_health.csv','path_quality.csv','quality_summary.json','report.md','metrics.json']:
            shutil.copy2(dest/name,output/name)
        render(cfg,record,diag,output/'plots')
        # Exact ADC round-trip includes signed corner codes, in the bank blanked for
        # this capture. The four opposing acoustic paths remain intact for TOF reuse.
        vector=generate(cfg,truth(cfg),40000)[64]
        vector[0,4:]=[-32768,-1,0,32767]
        (work/'adc_vectors.hex').write_text('\n'.join(''.join(f'{int(v)&65535:04x}' for v in row[::-1]) for row in vector)+'\n')
        lut=phase_lut(cfg,record)
        (work/'calibration_frequency.hex').write_text(f"{int(record['f_work']):08x}\n")
        (work/'calibration_map.hex').write_text('\n'.join(f"{(x['enabled']<<16)|(x['calibration_phase']<<8)|x['requested_phase']:05x}" for x in lut)+'\n')
        rtl=sorted((ROOT/'rtl').rglob('*.sv'));tb=[ROOT/'tb/ad7606b_model.sv',ROOT/'tb/tb_calibration.sv']
        iv=Path(os.environ.get('IVERILOG_BIN','C:/iverilog/bin'))
        command('iverilog_compile',[iv/'iverilog.exe','-g2012','-I',ROOT/'rtl/generated','-s','tb_calibration','-o',work/'calibration.vvp',*rtl,*tb])
        roundtrips=[]
        def roundtrip(label):
            words=[int(v,16) for v in (work/'adc_roundtrip.hex').read_text().split()]
            raw=b''.join(x.to_bytes(4,'little') for x in words);decoded=decode_frames(raw)
            np.testing.assert_array_equal(decoded,vector)
            sha=hashlib.sha256(raw).hexdigest();roundtrips.append({'tool_run':label,'frames':len(decoded),'sha256':sha})
            # Feed decoded RTL samples into the actual TOF estimator, no injected answer.
            delays=[]
            for rx in range(4):
                p=estimate_tof(decoded[:,rx],800000,40000,16,cfg['ring_up_s'],cfg['ring_down_s'])
                q=estimate_tof(vector[:,rx],800000,40000,16,cfg['ring_up_s'],cfg['ring_down_s'])
                if abs(p['tof_s']-q['tof_s'])>1e-12:raise AssertionError('RTL-to-estimator difference')
                delays.append(p['tof_s'])
            return delays
        for i in range(3):
            out=command('icarus_'+str(i),[iv/'vvp.exe',work/'calibration.vvp'])
            if 'PASS calibration digital system' not in out:raise AssertionError('Missing RTL completion')
            summary['rtl_decoded_tof_s']=roundtrip('Icarus '+str(i))
        if not a.skip_xsim:
            vb=Path(os.environ.get('VIVADO_BIN','D:/Vivado/2025.2/2025.2/Vivado/bin'))
            command('xvlog',[vb/'xvlog.bat','--sv','-i',ROOT/'rtl/generated',*rtl,*tb])
            command('xelab',[vb/'xelab.bat','tb_calibration','--snapshot','calibration_snapshot','--debug','typical'])
            out=command('xsim',[vb/'xsim.bat','calibration_snapshot','--runall'])
            if 'PASS calibration digital system' not in out:raise AssertionError('XSim incomplete')
            roundtrip('Vivado 2025.2 XSim')
        summary['adc_roundtrips']=roundtrips
        if len(set(x['sha256'] for x in roundtrips))!=1:raise AssertionError('Simulator mismatch')
        # Noise levels report the same fixed limits, including actual failures.
        robustness=[]
        for snr in (35,25,15,5):
            try:
                _,_,m=experiment(work/f'noise_{snr}',snr=snr,save_raw=False)
                robustness.append({**m,'status':'WITHIN_BASELINE_LIMITS' if checks(m) else 'OUTSIDE_BASELINE_LIMITS'})
            except (ValueError,RuntimeError) as exc:
                robustness.append({'snr_db':snr,'status':'REJECTED','error':str(exc)})
        summary['noise_robustness']=robustness
        (output/'robustness.json').write_text(canonical(robustness))
        summary['status']='PARTIAL' if a.skip_xsim else 'PASS'
        summary['scope']='512-path raw software pipeline; exact 1024x8 ADC RTL roundtrip; 128 captures in RTL scan use 32 frames each'
        summary['not_verified']=['physical transducers/AFE/ADC/clock/board','target synthesis and timing closure','absolute pressure/force','PS AXI transport','real RX phase reference']
    except Exception as exc:
        summary.update(status='FAIL',error=str(exc));raise
    finally:
        (output/'summary.json').write_text(canonical(summary),encoding='utf-8')
    print('SELF_CALIBRATION_GATE '+summary['status'])


if __name__=='__main__':main()
