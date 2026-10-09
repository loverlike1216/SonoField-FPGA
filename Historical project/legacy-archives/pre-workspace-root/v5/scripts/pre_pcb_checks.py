"""Independent golden comparison and actual serializer throughput gate."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='evidence/pre_pcb_board_ready/independent_checks')
    args=parser.parse_args()
    out=(ROOT/args.output).resolve();out.mkdir(parents=True,exist_ok=True)
    work=ROOT/'build/pre_pcb/independent_checks';work.mkdir(parents=True,exist_ok=True)
    baseline=ROOT/'simulation/golden/motion_queue.sv'
    golden=work/'motion_queue_golden.sv'
    golden.write_text(baseline.read_text().replace('module motion_queue #','module motion_queue_golden #'))
    scheduler_golden=work/'scheduler_golden.sv'
    scheduler_golden.write_text((ROOT/'simulation/golden/calibration_scheduler.sv').read_text().replace('module calibration_scheduler #','module calibration_scheduler_golden #'))
    iv=Path(os.environ.get('IVERILOG_BIN','C:/iverilog/bin'))
    vb=Path(os.environ.get('VIVADO_BIN','D:/Vivado/2025.2/2025.2/Vivado/bin'))
    results=[]
    cases=[('tb_motion_queue_equivalence',[ROOT/'rtl/motion/motion_queue.sv',golden,ROOT/'tb/tb_motion_queue_equivalence.sv'],'PASS QUEUE_EQ_ALL'),
           ('tb_serializer_throughput',[ROOT/'rtl/output/serializer.sv',ROOT/'tb/tb_serializer_throughput.sv'],'PASS SERIALIZER_THROUGHPUT'),
           ('tb_array_interface',[ROOT/'rtl/output/sono_array_interface.sv',ROOT/'rtl/control/safety_controller.sv',ROOT/'tb/tb_array_interface.sv'],'PASS ARRAY_INTERFACE'),
           ('tb_scheduler_equivalence',[ROOT/'rtl/calibration/calibration_scheduler.sv',scheduler_golden,ROOT/'tb/tb_scheduler_equivalence.sv'],'PASS SCHEDULER_EQ')]
    files={p for _,paths,_ in cases for p in paths}
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    summary={'status':'RUNNING','classification':'SIMULATED','source_sha256':hashes,'commands':results,
             'hardware_programmed':False,'core_clock_design_target_hz':132000000}
    try:
        for top,paths,marker in cases:
            cmds=[[iv/'iverilog.exe','-g2012','-s',top,'-o',work/(top+'.vvp'),*paths],
                  [iv/'vvp.exe',work/(top+'.vvp')],[vb/'xvlog.bat','--sv',*paths],
                  [vb/'xelab.bat',top,'--snapshot',top,'--debug','typical'],[vb/'xsim.bat',top,'--runall']]
            for i,cmd in enumerate(cmds):
                p=subprocess.run(list(map(str,cmd)),cwd=work,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                                 text=True,errors='replace',timeout=240)
                log=f'{top}_{i}.log';(out/log).write_text(p.stdout,encoding='utf-8')
                results.append({'top':top,'step':i,'command':list(map(str,cmd)),'exit_code':p.returncode,'log':log})
                print(top,i,p.returncode,flush=True)
                if p.returncode or 'FATAL:' in p.stdout or (i in (1,4) and marker not in p.stdout):
                    raise RuntimeError(f'{top} step{i} failed; see {log}')
        assert all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p.relative_to(ROOT))] for p in files),'Sources changed during verification'
        summary['status']='PASS'
    except Exception:
        summary['status']='FAIL';raise
    finally:
        (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')

if __name__=='__main__':main()
