"""Cross-tool exact-cycle equivalence checks for the authorized timing refactor."""
from pathlib import Path
import os,subprocess,json,sys
R=Path(__file__).resolve().parents[1];O=R/'evidence/core_timing_real_loop/timing_refactor';W=R/'build/core_timing/equivalence'
def main():
 W.mkdir(parents=True,exist_ok=True);O.mkdir(parents=True,exist_ok=True);records=[]
 golden=(R/'evidence/core_timing_real_loop/baseline/burst_generator.sv').read_text(encoding='utf-8').replace('module burst_generator #','module burst_generator_golden #')
 (W/'burst_generator_golden.sv').write_text(golden,encoding='utf-8')
 rtl=sorted((R/'rtl').rglob('*.sv'))
 iv=Path(os.environ['IVERILOG_BIN']);vb=Path(os.environ['VIVADO_BIN'])
 def run(name,args):
  p=subprocess.run(list(map(str,args)),cwd=W,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=300)
  text=p.stdout+p.stderr;(O/(name+'.log')).write_text(text,encoding='utf-8');records.append({'name':name,'argv':list(map(str,args)),'exit_code':p.returncode})
  if p.returncode or 'FATAL:' in text or 'Fatal:' in text:raise RuntimeError(name)
  return text
 try:
  for name in ['tb_phase_equivalence','tb_burst_equivalence']:
   files=rtl+[W/'burst_generator_golden.sv',R/'tb'/f'{name}.sv']
   run(name+'_compile',[iv/'iverilog.exe','-g2012','-I',R/'rtl/generated','-s',name,'-o',name+'.vvp',*files])
   assert 'PASS ' in run(name+'_icarus',[iv/'vvp.exe',name+'.vvp'])
   run(name+'_xvlog',[vb/'xvlog.bat','--sv','-i',R/'rtl/generated',*files])
   run(name+'_xelab',[vb/'xelab.bat',name,'--snapshot',name,'--debug','typical'])
   assert 'PASS ' in run(name+'_xsim',[vb/'xsim.bat',name,'--runall'])
  status='PASS'
 finally:
  (O/'equivalence.json').write_text(json.dumps({'status':locals().get('status','FAIL'),'latency_change_cycles':0,'commands':records,'scope':'valid frequency contract, main phase/boundary/tick and burst active/done/wave compared to original formula/RTL'},indent=2)+'\n')
 print('EQUIVALENCE '+status)
if __name__=='__main__':main()
