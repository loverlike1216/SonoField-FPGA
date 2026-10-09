"""One reproducible offline gate. Never opens/programs hardware or reads old source."""
from pathlib import Path
import argparse,datetime,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT/'evidence') or out.exists():raise ValueError('Fresh v5/evidence output required')
    out.mkdir(parents=True);records=[];result=dict(status='RUNNING',classification='OFFLINE_NOT_PHYSICAL',commands=records,
        started_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_root=str(ROOT),python=sys.executable)
    environment=os.environ.copy();environment['PYTHONUTF8']='1';environment['PYTHONIOENCODING']='utf-8'
    scratch=ROOT/'build/prepcb_gate'/out.name;scratch.mkdir(parents=True,exist_ok=True)
    environment['TMP']=environment['TEMP']=str(scratch)
    def run(name,script,*args):
        cmd=[sys.executable,str(ROOT/'scripts'/script),*map(str,args)]
        with (out/(name+'.log')).open('w',encoding='utf-8') as log:
            proc=subprocess.run(cmd,cwd=ROOT,env=environment,stdout=log,stderr=subprocess.STDOUT,timeout=3600)
        records.append(dict(name=name,command=cmd,exit_code=proc.returncode));print(name,proc.returncode,flush=True)
        if proc.returncode:raise RuntimeError(name+' failed; preserve logs')
    try:
        run('preservation','check_prepcb_preservation.py')
        run('inherited_full','run_baseline.py','--output',out/'inherited_full')
        run('supervisor_mailbox','prepcb_rtl_gate.py','--output',out/'supervisor')
        run('temperature_sparse_gui','prepcb_system_gate.py','--output',out/'system')
        run('actual_top','prepcb_top_gate.py','--maps',out/'system/gui/case_1/icarus/motion_maps.hex','--output',out/'top')
        result['status']='PASS'
    except Exception as exc:result.update(status='FAIL',error=str(exc));raise
    finally:(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
