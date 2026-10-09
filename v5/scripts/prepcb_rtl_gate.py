from pathlib import Path
import os, subprocess, argparse, json
ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve();out.mkdir(parents=True,exist_ok=True)
    iv=Path(os.environ['IVERILOG_BIN']);vb=Path(os.environ['VIVADO_BIN'])
    files=[ROOT/'rtl/control/prepcb_supervisor.sv',ROOT/'rtl/motion/prepcb_frame_mailbox.sv',ROOT/'tb/tb_prepcb.sv']
    commands=[('compile',[iv/'iverilog.exe','-g2012','-s','tb_prepcb','-o','prepcb.vvp',*files]),
              ('icarus',[iv/'vvp.exe','prepcb.vvp']),('xvlog',[vb/'xvlog.bat','--sv',*files]),
              ('xelab',[vb/'xelab.bat','tb_prepcb','-s','prepcb']),('xsim',[vb/'xsim.bat','prepcb','--runall'])]
    records=[]
    for label,cmd in commands:
        r=subprocess.run(list(map(str,cmd)),cwd=out,capture_output=True,text=True,timeout=120)
        (out/(label+'.log')).write_text(r.stdout+r.stderr,encoding='utf-8');records.append(dict(label=label,exit_code=r.returncode))
        if r.returncode or (label in ('icarus','xsim') and 'PASS PREPCB' not in r.stdout):raise RuntimeError(label+' failed')
    (out/'summary.json').write_text(json.dumps(dict(status='PASS',classification='SIMULATED_NOT_PHYSICAL_FAILSAFE',commands=records),indent=2),encoding='utf-8')

if __name__=='__main__':main()
