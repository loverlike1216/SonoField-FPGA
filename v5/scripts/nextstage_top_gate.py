"""Actual C-16 production candidate, inherited assertions and identical ACK maps."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--maps',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists():raise ValueError('Fresh output required')
 out.mkdir(parents=True);data=a.maps.read_bytes();iv=Path(os.environ['IVERILOG_BIN']);vb=Path(os.environ['VIVADO_BIN']);records=[]
 files=[ROOT/x for x in (ROOT/'config/nextstage_source_list.txt').read_text().splitlines()]+[ROOT/'tb/ad7606c16_model.sv',ROOT/'tb/tb_nextstage_system.sv']
 try:
  for sim in ('icarus','xsim'):
   dest=out/sim;dest.mkdir();(dest/'motion_maps.hex').write_bytes(data)
   cmds=([('compile',[iv/'iverilog.exe','-g2012','-I',ROOT/'rtl/generated','-s','tb_nextstage_system','-o','top.vvp',*files]),('run',[iv/'vvp.exe','top.vvp'])] if sim=='icarus' else [('xvlog',[vb/'xvlog.bat','--sv','-i',ROOT/'rtl/generated',*files]),('xelab',[vb/'xelab.bat','tb_nextstage_system','-s','top_c16']),('run',[vb/'xsim.bat','top_c16','--runall'])])
   for step,cmd in cmds:
    r=subprocess.run(list(map(str,cmd)),cwd=dest,capture_output=True,text=True,timeout=180);text=r.stdout+r.stderr;(dest/(step+'.log')).write_text(text,encoding='utf-8')
    if r.returncode or 'ERROR:' in text or 'FATAL:' in text or(step=='run' and 'PASS PREPCB SYSTEM' not in text):raise RuntimeError(sim+step+text[-1000:])
   lines=(dest/'integrated_ack.txt').read_text().splitlines();records.append(dict(simulator=sim,frames=len(lines),ack_sha256=hashlib.sha256('\n'.join(lines).encode()).hexdigest()))
  assert records[0]['ack_sha256']==records[1]['ack_sha256']
  result=dict(status='PASS',classification='C16_ACTUAL_TOP_SIMULATED_NOT_BOARD',maps_sha256=hashlib.sha256(data).hexdigest(),runs=records)
 except Exception as exc:result=dict(status='FAIL',error=str(exc),runs=records);raise
 finally:(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
