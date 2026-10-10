"""Full signed C16 capture and buffer ACK chain in two independent tools."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists():raise ValueError('Fresh output required')
 out.mkdir(parents=True);records=[]
 files=[ROOT/x for x in ['rtl/acquisition/adc_serial.sv','rtl/acquisition/ad7606c16_if.sv','rtl/calibration/calibration_scheduler.sv','rtl/calibration/burst_generator.sv','tb/ad7606c16_model.sv','tb/tb_c16_capture_chain.sv']]
 try:
  for sim in ['icarus','xsim']:
   dest=out/sim;dest.mkdir();iv=Path(os.environ['IVERILOG_BIN']);vb=Path(os.environ['VIVADO_BIN'])
   cmds=([('compile',[iv/'iverilog.exe','-g2012','-s','tb_c16_capture_chain','-o','capture.vvp',*files]),('run',[iv/'vvp.exe','capture.vvp'])] if sim=='icarus' else [('xvlog',[vb/'xvlog.bat','--sv',*files]),('xelab',[vb/'xelab.bat','tb_c16_capture_chain','-s','capture']),('run',[vb/'xsim.bat','capture','--runall'])])
   for step,cmd in cmds:
    r=subprocess.run(list(map(str,cmd)),cwd=dest,capture_output=True,text=True,timeout=180);text=r.stdout+r.stderr;(dest/(step+'.log')).write_text(text,encoding='utf-8')
    if r.returncode or 'ERROR:' in text or 'FATAL:' in text or(step=='run' and 'PASS C16_CAPTURE_CHAIN' not in text):raise RuntimeError(sim+step+text[-1000:])
   lines=(dest/'capture_trace.txt').read_text().splitlines();assert len(lines)==2048;records.append(dict(simulator=sim,signed_frames=len(lines),trace_sha256=hashlib.sha256('\n'.join(lines).encode()).hexdigest()))
  assert records[0]['trace_sha256']==records[1]['trace_sha256'];result=dict(status='PASS',classification='SIMULATED_C16_SCHEDULER_BRAM_SIGNED_READ_ACK_NOT_HARDWARE',runs=records)
 except Exception as exc:result=dict(status='FAIL',error=str(exc),runs=records);raise
 finally:(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
