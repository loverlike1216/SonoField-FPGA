"""Full current offline gate; no serial/hardware/CAD/archived-source operations."""
from pathlib import Path
import argparse,datetime,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists() or not out.is_relative_to(ROOT/'evidence'):raise ValueError('Fresh v5/evidence path required')
 out.mkdir(parents=True);records=[];result=dict(status='RUNNING',classification='OFFLINE_ONLY',source_root=str(ROOT),python=sys.executable,started_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),commands=records)
 def run(name,script,*args):
  cmd=[sys.executable,str(ROOT/'scripts'/script),*map(str,args)]
  with (out/(name+'.log')).open('w',encoding='utf-8') as f:r=subprocess.run(cmd,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=3600)
  records.append(dict(name=name,command=cmd,exit_code=r.returncode));print(name,r.returncode,flush=True)
  if r.returncode:raise RuntimeError(name+' failed; preserved logs')
 try:
  run('prepcb_full','run_prepcb.py','--output',out/'full')
  run('adc_c16','adc7606c16_gate.py','--output',out/'adc')
  run('c16_capture_chain','c16_capture_chain_gate.py','--output',out/'capture_c16')
  run('c16_actual_top','nextstage_top_gate.py','--maps',out/'full/system/gui/case_1/icarus/motion_maps.hex','--output',out/'top_c16')
  run('software_target','nextstage_software_gate.py','--output',out/'software')
  result['status']='PASS'
 except Exception as exc:result.update(status='FAIL',error=str(exc));raise
 finally:(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
