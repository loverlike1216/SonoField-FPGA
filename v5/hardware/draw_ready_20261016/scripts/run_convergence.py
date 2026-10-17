from pathlib import Path
import os,json,subprocess,sys
R=Path(__file__).resolve().parents[1]
if '--one'in sys.argv:
 from si_engine import run_case
 x=json.loads(sys.argv[-1]);y=run_case(x['solution'],x['case'],x['z0_ohm'],x['ron_ohm'],x['voltage'],x['cin_pf'],x['corner'],x['td_ns'],x['variant'],x['ax_model']=='OEM_IV_SUBSET',x['actual_package'])
 (R/'results'/f"CONVERGENCE_{os.environ['SI_STEP_NS']}_{x['case']}.json").write_text(json.dumps(y,indent=2));print(y['pulse_ns']);sys.exit()
a=json.loads((R/'results/SELECTED_FINAL_SI_INDEPENDENT.json').read_text());worst={min(a,key=lambda x:x[k])['case']:min(a,key=lambda x:x[k])for k in ['independent_pulse_ns']}
out=[]
for x in worst.values():
 ys=[]
 for step in ['.01','.005']:
  e=os.environ.copy();e.update(SI_STEP_NS=step,SI_REVISION='si_convergence'+step)
  q=subprocess.run([sys.executable,__file__,'--one',json.dumps(x)],env=e,capture_output=True,text=True,timeout=90);assert q.returncode==0,q.stdout+q.stderr
  ys.append(json.loads((R/'results'/f"CONVERGENCE_{step}_{x['case']}.json").read_text()))
 diff=abs(ys[1]['pulse_ns']-ys[0]['pulse_ns']);bound=ys[1]['pulse_ns']-4.4-.4-max(.001,diff)
 out.append(dict(case=x['case'],coarse_pulse_ns=x['pulse_ns'],step10ps_pulse_ns=ys[0]['pulse_ns'],step5ps_pulse_ns=ys[1]['pulse_ns'],difference_ns=diff,conservative_pulse_ns=bound,status='PASS'if diff<.001 and bound>=5.2 else'FAIL'))
(R/'results/CONVERGENCE_FINAL.json').write_text(json.dumps(out,indent=2));print(json.dumps(out));assert all(x['status']=='PASS'for x in out)
