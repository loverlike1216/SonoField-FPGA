from pathlib import Path
import itertools,json
from concurrent.futures import ThreadPoolExecutor,as_completed
from si_engine import R,run_case,REVISION
jobs=[]
for i,(z,ron,v,cap)in enumerate(itertools.product([80,100,120],[5,20,30],[3.,3.3,3.45],[3.,6.])):jobs.append(('F',i,z,ron,v,cap,'typ',1.,'lvt_filter',False,False))
for i,(c,td,z,cap)in enumerate(itertools.product(['min','typ','max'],[.75,1.,1.25],[80,120],[3.,6.])):jobs.append(('F',1000+i,z,20,{'min':3.135,'typ':3.3,'max':3.465}[c],cap,c,td,'lvt_filter',True,True))
rows=[];errors=[]
with ThreadPoolExecutor(max_workers=4)as p:
 fs={p.submit(run_case,*j):j for j in jobs}
 for f in as_completed(fs):
  try:rows.append(f.result())
  except Exception as e:errors.append(dict(job=fs[f],error=str(e)))
  if(len(rows)+len(errors))%15==0:print(len(rows),len(errors),flush=True)
(R/'results/SELECTED_FINAL_SI.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
(R/'results/SELECTED_FINAL_SI_ERRORS.json').write_text(json.dumps(errors,indent=2),encoding='utf-8')
#Independent data-vs-clock and rise-vs-fall manufacturer timing intervals.
#Extra relative-line skew0.5ns, native pad skew/jitter must subsequently fit0.5ns.
for x in rows:
 x['independent_setup_ns']=x['setup_ns']-4.8-.5-.5-.4 if x['setup_ns']is not None else None
 x['independent_hold_ns']=x['hold_ns']-4.8-.5-.5-.4 if x['hold_ns']is not None else None
 x['independent_pulse_ns']=x['pulse_ns']-4.4-.4 if x['pulse_ns']is not None else None
 x['independent_latch_ns']=x['srclk_rclk_ns']-4.8-.5-.5-.4 if x['srclk_rclk_ns']is not None else None
 x['independent_status']='PASS'if x['model_joint_status']=='PASS'and x['independent_setup_ns']>=3.2 and x['independent_hold_ns']>=2.2 and x['independent_pulse_ns']>=5.2 and x['independent_latch_ns']>=3.2 else'FAIL'
(R/'results/SELECTED_FINAL_SI_INDEPENDENT.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps(dict(revision=REVISION,cases=len(rows),errors=len(errors),pass_count=sum(x['independent_status']=='PASS'for x in rows),minima={k:min(x[k]for x in rows if x[k]is not None)for k in ['independent_setup_ns','independent_hold_ns','independent_pulse_ns','independent_latch_ns']})))
if errors or any(x['independent_status']!='PASS'for x in rows):raise SystemExit(1)
