"""Coupled-stage transmission-line study with OEM static IV subsets.

Each corner carries actual extracted input transitions into the following stage.
This is deliberately called IBIS_DERIVED_STATIC_IV, not full IBIS simulation:
OEM multi-fixture dynamic waveform fitting, die power nets, SSO and595 IBIS absent.
"""
from pathlib import Path
import numpy as np,subprocess,json,itertools,csv,hashlib,threading,os
from concurrent.futures import ThreadPoolExecutor,as_completed
from ibis_tools import models,scalar,table,pwl_expr
R=Path(__file__).resolve().parents[1]
NG='E:/Codex_project/SonoField_v5_Fixed12V_Audit_20261015/tools/ngspice_py7zr/Spice64/bin/ngspice_con.exe'
MODEL_PATHS={'AX':('zynq.ibs','LVCMOS33_F_8_HR'),'AUC':('scem333/sn74auc244.ibs','AUC244_OUT_25'),'LVC':('scam008/sn74lvc244a.ibs','LVC244A_OUT_33'),'ALVC':('scem386/SN74ALVC244_IBIS/sn74alvc244.ibs','ALVC244_OUT_33'),'LVT':('scam013/sn74lvt244b.ibs','LVT244B_OUT_33')}
INPUT_PATHS={'AUC':('scem333/sn74auc244.ibs','AUC244_IN_25'),'LVC':('scam008/sn74lvc244a.ibs','LVC244A_IN_33'),'ALVC':('scem386/SN74ALVC244_IBIS/sn74alvc244.ibs','ALVC244_IN_33'),'LVT':('scam013/sn74lvt244b.ibs','LVT244B_IN_33')}
MODELS={k:models(R/'sources/models'/p)[n]for k,(p,n)in MODEL_PATHS.items()}
REVISION=os.environ.get('SI_REVISION','si_final_128_256_lvt_r15_c3p3')
STEP_NS=os.environ.get('SI_STEP_NS','.03')
INPUTS={k:models(R/'sources/models'/p)[n]for k,(p,n)in INPUT_PATHS.items()}
T=1000/128;U=T/2
def crossing(t,v,level):
 ix=np.flatnonzero((v[:-1]<level)&(v[1:]>=level));rise=t[ix]+(level-v[ix])*(t[ix+1]-t[ix])/(v[ix+1]-v[ix])
 ix=np.flatnonzero((v[:-1]>level)&(v[1:]<=level));fall=t[ix]+(level-v[ix])*(t[ix+1]-t[ix])/(v[ix+1]-v[ix])
 return list(rise),list(fall)
def control(events,slew=.5):
 a=[(0.,0.)];previous=0
 for time,value in events:
  if time<=a[-1][0]:raise ValueError(('non-monotonic control',time,a[-1]))
  a.extend([(time,previous),(time+slew,value)]);previous=value
 a.append((240.,previous))
 return a
def source_events(signal,pipeline=False):
 out=[]
 for f in range(2):
  start=20+12*T*f
  if signal=='data':
   for b in range(4):out.append((start+b*(6*U if pipeline else 2*T),float(b%2==0)))
  elif signal=='clock':
   for b in range(4):
    rise=start+(3+6*b)*U if pipeline else start+(1+2*b)*T
    width=3*U if pipeline else T
    out.extend([(rise,1.),(rise+width,0.)])
  else:
   rise=start+24*U if pipeline else start+9*T;out.extend([(rise,1.),(rise+(3*U if pipeline else T),0.)])
 return sorted(out)
def logic_events(t,v,vil,vih,delay):
 rise,fall=crossing(t,v,(vil+vih)/2)
 return sorted([(float(x+delay),1.)for x in rise if x>5]+[(float(x+delay),0.)for x in fall if x>5])
def input_cards(prefix,node,ground,rail,kind,corner):
 if kind=='595':return [] # OEM model unavailable; Cin interval only, never invent clamp tables.
 m=INPUTS[kind];lines=[]
 for label,arg,section,end in [('g',f'v({node},{ground})','gnd clamp',ground),('p',f'v({rail},{node})','power clamp',rail)]:
  a=table(m,section,corner)
  if len(a):
   if label=='p':a=a.copy();a[:,1]*=-1
   lines.append(f'B{prefix}{label} {node} {end} I='+pwl_expr(arg,a))
 return lines
def run_segment(directory,driver,receiver,events,z,ron,vsource,cap,corner,td,term='source',local=False,signal='data',off=False,input_multiplier=1,actual_package=False):
 directory.mkdir(parents=True,exist_ok=True)
 vdrv=vsource if driver=='AX'else ({'min':2.44,'typ':2.5,'max':2.56}[corner]if driver=='AUC'else vsource)
 vrx=2.5 if receiver=='AUC'else 3.3
 k=control(events,slew=.5 if driver=='AX'else .35)
 cards=['* OEM static IV subset + assumed package/cable; NOT full IBIS',f'VDD vdd 0 {0 if off else vdrv}',f'VRX vrx g {0 if off else vrx}','Rground g gx .05','Lground gx 0 1n', 'Vctrl ctrl 0 PWL('+ ' '.join(f'{t:.9g}n {x:.9g}'for t,x in k)+')']
 if driver=='AX_GENERIC':
  cards+=['Bvoltage internal 0 V=v(vdd)*v(ctrl)',f'Rdriver internal die {ron}']
 elif driver=='AX':
  # Baseline Ron sweep remains an independent model; OEM runs use selected
  # DRIVE8 I/V and do not double-count a fictitious extra series Ron.
  m=MODELS['AX'];cards+=[f'Bpd die 0 I=(1-v(ctrl))*'+pwl_expr('v(die)',table(m,'pulldown',corner)),f'Bpu die vdd I=v(ctrl)*'+pwl_expr('v(vdd)-v(die)',table(m,'pullup',corner)),f'Cdrv die 0 {scalar(m,"c_comp",corner,5e-12)}']
 else:
  m=MODELS[driver];cards+=[f'Bpd die 0 I=(1-v(ctrl))*'+pwl_expr('v(die)',table(m,'pulldown',corner)),f'Bpu die vdd I=v(ctrl)*'+pwl_expr('v(vdd)-v(die)',table(m,'pullup',corner)),f'Cdrv die 0 {scalar(m,"c_comp",corner,5e-12)}']
 if driver!='AX_GENERIC':
  m=MODELS[driver]
  for label,arg,section,end in [('g','v(die)','gnd clamp','0'),('p','v(vdd)-v(die)','power clamp','vdd')]:
   a=table(m,section,corner)
   if len(a):
    if label=='p':a=a.copy();a[:,1]*=-1
    cards.append(f'Bout{label} die {end} I='+pwl_expr(arg,a))
 # Generic5/20/30 source specifically retained for the common envelope.
 if driver=='AX_GENERIC':vdrv=vsource
 fanout=4 if local and signal!='data'else 1
 #3/6pF is the common single-input+parasitic envelope. For tied buffer
 # inputs, multiply the3pF device cap, not the whole board parasitic allowance.
 # Arraylocal595 fanout remains an independent3/6pF-per-device sensitivity.
 load_pf=cap*fanout if local else 3*input_multiplier+(cap-3)
 if receiver=='LVT':load_pf=max(3.,scalar(INPUTS['LVT'],'c_comp',corner,6e-12)*1e12)*input_multiplier+(cap-3)
 if local:
  #Conservative10pF per595, plus6pF watchdog input on one clock branch.
  load_pf=10*fanout+(6 if signal!='data'else 0)
 pr,pl,pc=(.05,1.2e-9,0.)
 if actual_package and driver.startswith('AX'):
  pr,pl,pc={'min':(.1309,2.71e-9,.33e-12),'typ':(.4093,8.10e-9,1.31e-12),'max':(.7305,14.76e-9,2.90e-12)}[corner]
 if driver=='LVT':
  #PW package values audited independently inLVT_COMPONENT_PACKAGE.json.
  package=json.loads((R/'results/LVT_COMPONENT_PACKAGE.json').read_text())
  pr,pl,pc=package[corner]
 cards+= [f'Rpkg die pkg {pr}',f'Lpkg pkg out {pl}']
 if pc:cards+=[f'Cpackage out 0 {pc}']
 cards += [f'Rseries out tx {33 if driver.startswith("AX")else (47 if not local or signal=="data"else 15)}',f'Tline tx 0 end g Z0={z if not local else 80} TD={td if not local else (.08 if cap==3 else .18)}n','Rpin end pin .05','Lpin pin rxi 1.2n',f'Cin rxi g {load_pf*1e-12}']
 if receiver=='LVT':
  receive_pkg=json.loads((R/'results/LVT_COMPONENT_PACKAGE.json').read_text())[corner]
  cards=[x.replace('Rpin end pin .05',f'Rpin end pin {receive_pkg[0]}').replace('Lpin pin rxi 1.2n',f'Lpin pin rxi {receive_pkg[1]}')for x in cards]
 if term=='rx_filter':
  #Receiver isolation RC:~1.5ns pole, below the~11.36ns F halfcell.
  #Absorbs firstline reflection energy without DCtermination or AXpower tap.
  #68ohm inseries immediately at receiver,22pF C0G shunt at theinput.
  rt={'min':21.78,'typ':22.,'max':22.22}[corner]
  ct={'min':3.135,'typ':3.3,'max':3.465}[corner]
  cards=[x.replace(' pin rxi ',' pin rxf ')if x.startswith('Lpin')else x for x in cards]
  cards +=[f'Rrxfilter rxf rxi {rt}',f'Crxfilter rxi g {ct}p']
 if term=='thevenin':cards+=['Rup end vterm 330','Rdn end g 150',f'Vterm vterm g {vsource}']
 elif term=='far_thevenin':cards+=['Rup end vterm 330','Rdn end g 150',f'Vterm vterm g {vdrv}']
 elif term=='ac':cards+=['Rac end ac 100','Cac ac g 100p']
 elif term=='ac_first':
  #Topology-derived AC termination:~100ohm cable, tau~4.7ns, longer than
  #2ns flight roundtrip and shorter than F's11.36ns halfcell. No DCpullup.
  rt={'min':99,'typ':100,'max':101}[corner];ct={'min':44.65,'typ':47,'max':49.35}[corner]
  cards +=[f'Rac end ac {rt}',f'Cac ac g {ct}p']
 if input_multiplier>1:
  # All tied inputs have clamp currents in parallel as well as capacitance.
  for j in range(input_multiplier):cards+=input_cards('in'+str(j),'rxi','g','vrx',receiver,corner)
 else:cards+=input_cards('in', 'rxi','g','vrx',receiver,corner)
 cards+=['.control','set wr_vecnames','set wr_singlescale','set noaskquit',f'tran {STEP_NS}n 300n','wrdata wave.txt v(rxi,g) v(die) i(VDD)','quit','.endc','.end']
 net='\n'.join(cards)+'\n';(directory/'network.cir').write_text(net,encoding='ascii')
 p=subprocess.run([NG,'-n','-b','network.cir'],cwd=directory,capture_output=True,text=True,timeout=45)
 (directory/'ngspice.log').write_text(p.stdout+p.stderr,encoding='utf-8')
 if p.returncode:raise RuntimeError(f'ngspice {directory}: '+p.stdout[-700:]+p.stderr[-700:])
 a=np.loadtxt(directory/'wave.txt',skiprows=1);t=a[:,0]*1e9;v=a[:,1]
 if not np.isfinite(a).all()or np.max(np.abs(v))>20 or t[-1]<234.999 or 'aborted'in(p.stdout+p.stderr).lower():
  # Trapezoidal instability of nonlinear static-IV/ideal lossless lines is a
  # numerical issue, never evidence of trillion-volt hardware overshoot.
  (directory/'network_trap.cir').write_text(net,encoding='ascii')
  (directory/'ngspice_trap.log').write_text(p.stdout+p.stderr,encoding='utf-8')
  np.savez_compressed(directory/'wave_trap_invalid.npz',samples=a)
  net=net.replace('.control','.options method=gear maxord=2 reltol=1e-4 abstol=1e-11\n.control')
  (directory/'network.cir').write_text(net,encoding='ascii')
  p=subprocess.run([NG,'-n','-b','network.cir'],cwd=directory,capture_output=True,text=True,timeout=45)
  (directory/'ngspice.log').write_text('NUMERICAL_RETRY_GEAR2\n'+p.stdout+p.stderr,encoding='utf-8')
  if p.returncode:raise RuntimeError('GEAR2 solver failed: '+p.stdout[-500:])
  a=np.loadtxt(directory/'wave.txt',skiprows=1);t=a[:,0]*1e9;v=a[:,1]
  if not np.isfinite(a).all()or np.max(np.abs(v))>20 or t[-1]<234.999 or 'aborted'in(p.stdout+p.stderr).lower():
   np.savez_compressed(directory/'wave_gear_incomplete.npz',samples=a)
   raise RuntimeError('MODEL_HOLD: transient incomplete/divergent after GEAR2; not physical SI evidence')
 np.savez_compressed(directory/'wave.npz',time_ns=t,receiver_v=v,driver_v=a[:,2],supply_a=a[:,3])
 (directory/'wave.txt').unlink() # generated scratch only; compressed raw samples retained
 return t,v
def run_lvds(directory,events,z,cap,td,corner):
 directory.mkdir(parents=True,exist_ok=True)
 control_points=control(events)
 common={'min':.7,'typ':1.2,'max':1.7}[corner] # includes assumed +/-0.5V ground shift
 # Driver0.5..1.7ns, receiver1.2..2.7ns: OEM datasheet limits, not invented3.5ns.
 txdelay={'min':.5,'typ':1.05,'max':1.7}[corner]
 points=' '.join(f'{t+txdelay:.9g}n {v:.9g}'for t,v in control_points)
 amplitude={'min':.25,'typ':.35,'max':.45}[corner]
 net=f'''* G differentialclock, assumed pairedlines; ideal LVDS behavioral model
Vctrl ctrl 0 PWL({points})
Bpos sp 0 V={common}+{amplitude}*(2*v(ctrl)-1)
Bneg sn 0 V={common}-{amplitude}*(2*v(ctrl)-1)
Rp sp tp 50
Rn sn tn 50
Tpos tp 0 rp 0 Z0={z/2} TD={td}n
Tneg tn 0 rn 0 Z0={z/2} TD={td}n
Rterm rp rn 100
Cp rp 0 {cap*1e-12}
Cn rn 0 {cap*1e-12}
.control
set wr_vecnames
set wr_singlescale
tran .03n 235n
wrdata wave.txt v(rp,rn) v(rp) v(rn)
quit
.endc
.end
'''
 (directory/'network.cir').write_text(net,encoding='ascii');p=subprocess.run([NG,'-n','-b','network.cir'],cwd=directory,capture_output=True,text=True,timeout=45)
 (directory/'ngspice.log').write_text(p.stdout+p.stderr,encoding='utf-8');assert p.returncode==0,p.stdout+p.stderr
 a=np.loadtxt(directory/'wave.txt',skiprows=1);t=a[:,0]*1e9;v=a[:,1];np.savez_compressed(directory/'wave.npz',time_ns=t,differential_v=v,positive_v=a[:,2],negative_v=a[:,3]);(directory/'wave.txt').unlink()
 rr,ff=crossing(t,v,0);delay={'min':1.2,'typ':1.95,'max':2.7}[corner]
 ev=sorted([(float(x+delay),1.)for x in rr]+[(float(x+delay),0.)for x in ff])
 return ev,dict(model='IDEAL_LVDS_LINES; OEM_VOD_and_tpd_bounds; full_IBIS_NOT_AVAILABLE',differential_max=float(v.max()),differential_min=float(v.min()),common_mode_min=float(((a[:,2]+a[:,3])/2).min()),common_mode_max=float(((a[:,2]+a[:,3])/2).max()),rising_edges=len(rr),falling_edges=len(ff))
def wave_metrics(t,v,receiver,expected_rises,signal,corner='typ'):
 vil,vih=(.7,1.7)if receiver=='AUC'else(.7,2.1)
 limit=3.6 if receiver in['AUC','ALVC']else 5.5
 mid=(vil+vih)/2;rise,fall=crossing(t,v,mid);widths=[];counts=[];allrise=[];allfall=[]
 for lev in[vil,mid,vih]:
  rr,ff=crossing(t,v,lev);counts.append((len(rr),len(ff)));allrise.append(rr);allfall.append(ff)
  ee=sorted([(x,1)for x in rr]+[(x,0)for x in ff]);widths.extend(b[0]-a[0]for a,b in zip(ee,ee[1:])if a[1]!=b[1])
 # Recommended voltage and absolute negative rating are separately visible.
 clamp=None;charge=None
 if receiver!='595':
  arr=table(INPUTS[receiver],'gnd clamp',corner)
  if len(arr):
   current=np.interp(v,arr[:,0],arr[:,1]);clamp=float(np.max(np.abs(np.minimum(current,0))))
   charge=float(np.trapezoid(np.abs(np.minimum(current,0)),t*1e-9))
 # TI AUC/LVC negative-voltage exception explicitly allows exceeding-0.5V
 # when negative input clamp current stays within50mA. Keep both screens:
 # do not equate a clamped voltage to safe current, nor silently reject the
 # datasheet exception. This still does NOT qualify repeated-injection lifetime.
 neg_ok=float(v.min())>=-.5 or(clamp is not None and clamp<=.05)
 volt=float(v.max())<=limit and neg_ok
 edge_ok=all(x==(expected_rises,expected_rises)for x in counts)
 slew=[]
 if len(allrise[0])==len(allrise[-1]):slew=[b-a for a,b in zip(allrise[0],allrise[-1])]
 return dict(vmax=float(v.max()),vmin=float(v.min()),voltage_status='PASS'if volt else'FAIL',negative_voltage_screen='PASS'if float(v.min())>=-.5 else'FAIL',negative_clamp_exception_used=float(v.min())<-.5 and neg_ok,negative_clamp_peak_a=clamp,negative_injection_charge_c=charge,threshold_counts=counts,edge_status='PASS'if edge_ok else'FAIL',min_pulse_ns=float(min(widths))if widths else 0,max_vil_to_vih_ns=float(max(slew))if slew else None,rises=allrise,falls=allfall,scope='receiver voltage relative to modeled local ground;595 clamp/injection absent MODEL_HOLD')
def run_case(sol,index,z,ron,vsource,cap,corner='typ',td=1.,variant='source',oem_ax=False,actual_package=False):
 directory=R/'results'/REVISION/(f'{sol}_{variant}_{index}_{corner}_{td}_{int(oem_ax)}'+('_actualpkg'if actual_package else''))
 pipeline=sol=='F';stages={}
 first_kind='AUC'if sol in'CEF'else'LVC'
 second_kind=first_kind
 first_term='thevenin'if sol in'BEF'else'source'
 if sol=='C':first_kind='AUC';second_kind='AUC'
 if sol=='G':first_kind='AUC';second_kind='AUC';first_term='thevenin'
 if variant in['lvt','lvt_ac']:first_kind=second_kind='LVT';first_term='ac_first'if variant=='lvt_ac'else'source'
 if variant=='lvt_filter':first_kind=second_kind='LVT';first_term='rx_filter'
 if variant=='auc_filter':first_kind=second_kind='AUC';first_term='rx_filter'
 for signal in['data','clock','latch']:
  ev=source_events(signal,pipeline);n=4 if signal=='data'else 8 if signal=='clock'else 2
  # The legacyC uses a passivecentral junction, replayed separately; here C
  # adds one fast central AUC stage to study a corrected2-level alternative.
  t,v=run_segment(directory/signal/'first','AX'if oem_ax else'AX_GENERIC',first_kind,ev,z,ron,vsource,cap,corner,td,first_term,signal=signal,input_multiplier=2 if signal!='data'else 1,actual_package=actual_package)
  stats=[wave_metrics(t,v,first_kind,n,signal,corner)]
  if stats[0]['edge_status']=='FAIL':
   stages[signal]=dict(status='FAIL',reason='first input has extra/missing crossings; do not hide glitches in an inertial buffer model',stages=stats);continue
  delay1=({'min':.7,'typ':1.3,'max':1.9}[corner]if signal!='data'else {'min':.4,'typ':.95,'max':1.5}[corner])if first_kind=='AUC'else ({'min':1.1,'typ':2.3,'max':3.5}[corner]if first_kind=='LVT'else {'min':0.,'typ':3.9,'max':5.9}[corner])
  ev=logic_events(t,v,.7 if first_kind=='AUC'else .8,1.7 if first_kind=='AUC'else 2.,delay1)
  if not ev or any(b[0]-a[0]<=.5 for a,b in zip(ev,ev[1:])):
   stages[signal]=dict(status='FAIL',reason='no valid receiver transition',stages=stats);continue
  # D/E introduce a common-clock phase shift only on strobes.
  if sol in'DE'and signal!='data':ev=[(x+.5681818,y)for x,y in ev]
  second_term='far_thevenin'if sol=='B'and variant=='far'else'ac'if sol=='B'and variant=='ac'else'source'
  lvds=None
  if sol=='G'and signal!='data':ev,lvds=run_lvds(directory/signal/'lvds',ev,z,cap,td,corner)
  else:
   t,v=run_segment(directory/signal/'second',first_kind,second_kind,ev,z,ron,vsource,cap,corner,td,second_term,signal=signal,input_multiplier=4 if signal!='data'else 1)
   stats.append(wave_metrics(t,v,second_kind,n,signal,corner))
   if stats[-1]['edge_status']=='FAIL':
    stages[signal]=dict(status='FAIL',reason='second input has extra/missing crossings',stages=stats);continue
   delay2={'min':.4,'typ':.95,'max':1.5}[corner]if second_kind=='AUC'else ({'min':1.1,'typ':2.3,'max':3.5}[corner]if second_kind=='LVT'else {'min':0.,'typ':3.9,'max':5.9}[corner])
   ev=logic_events(t,v,.7 if second_kind=='AUC'else .8,1.7 if second_kind=='AUC'else 2.,delay2)
  if not ev or any(b[0]-a[0]<=.35 for a,b in zip(ev,ev[1:])):
   stages[signal]=dict(status='FAIL',reason='second input has no transitions',stages=stats);continue
  t,v=run_segment(directory/signal/'local',second_kind,'595',ev,z,ron,vsource,cap,corner,.08,local=True,signal=signal)
  end=wave_metrics(t,v,'595',n,signal,corner);stats.append(end)
  stages[signal]=dict(status='PASS'if all(x['voltage_status']=='PASS'and x['edge_status']=='PASS'for x in stats)else'FAIL',stages=stats,end=end,lvds=lvds)
 # Complete same-corner check; never combine different scenarios' best values.
 setup=hold=gap=1e6;pulse=1e6;valid=all('end'in stages[s]for s in['data','clock','latch'])
 if valid:
  data,clock,latch=[stages[s]['end']for s in['data','clock','latch']]
  for dr,df,cr,lr in itertools.product(data['rises'],data['falls'],clock['rises'],latch['rises']):
   changes=sorted(dr+df)
   for edge in cr:
    before=[x for x in changes if x<edge];after=[x for x in changes if x>=edge]
    if before:setup=min(setup,edge-before[-1])
    if after:hold=min(hold,after[0]-edge)
   for edge in lr:
    before=[x for x in cr if x<edge]
    if before:gap=min(gap,edge-before[-1])
  pulse=min(clock['min_pulse_ns'],latch['min_pulse_ns'])
 # Quantified extra0.5ns margin on setup/hold/pulse/latch, and0.2ns jitter reserve.
 ordered=True
 if valid:
  for cr,lr in itertools.product(clock['rises'],latch['rises']):
   for i,e in enumerate(lr):
    if sum(x<e for x in cr)!=(i+1)*4:ordered=False
 joint=valid and ordered and all(stages[s]['status']=='PASS'for s in stages)and setup>=3.2 and hold>=2.2 and pulse>=5.2 and gap>=3.2
 compact={s:{k:v for k,v in x.items()if k!='end'}for s,x in stages.items()}
 for x in compact.values():
  for st in x.get('stages',[]):st.pop('rises',None);st.pop('falls',None)
 out=dict(solution=sol,case=index,z0_ohm=z,ron_ohm=ron,voltage=vsource,cin_pf=cap,corner=corner,td_ns=td,variant=variant,ax_model='OEM_IV_SUBSET'if oem_ax else'RON_ENVELOPE',setup_ns=setup if valid else None,hold_ns=hold if valid else None,pulse_ns=pulse if valid else None,srclk_rclk_ns=gap if valid else None,stage_metrics=compact,model_joint_status='PASS'if joint else'FAIL',evidence_level='IBIS_DERIVED_STATIC_IV; MODEL_HOLD; not full compliant IBIS',wave_dir=str(directory.relative_to(R)),model_revision=REVISION,actual_package=actual_package)
 (directory/'metrics.json').write_text(json.dumps(out,indent=2),encoding='utf-8');return out
def main(smoke=False,resume=False):
 (R/'results'/REVISION).mkdir(exist_ok=True)
 jobs=[]
 cases=list(itertools.product([80,100,120],[5,20,30],[3.0,3.3,3.45],[3.,6.]))
 for sol in'ABCDEFG':
  for i,c in enumerate(cases):jobs.append((sol,i,*c))
 # B has3 topology-motivated alternatives, not unconstrained RC trial-and-error.
 for variant in['far','ac']:
  for i,c in enumerate(cases):jobs.append(('B',i,*c,'typ',1.,variant))
 # Same min/typ/max and0.75/1.00/1.25ns extension applied to every family.
 for sol in'ABCDEFG':
  for j,(corner,td,z,cap)in enumerate(itertools.product(['min','typ','max'],[.75,1.,1.25],[80,120],[3.,6.])):jobs.append((sol,1000+j,z,20,{'min':3.,'typ':3.3,'max':3.45}[corner],cap,corner,td,'source',True))
 if smoke:jobs=[('E',0,100,20,3.3,3.,'typ',1.,'source',True)]
 rows=[];errors=[]
 if resume:
  previous=json.loads((R/'results/SI_MATRIX.json').read_text())
  previous_errors=json.loads((R/'results/SI_ERRORS.json').read_text())
  jobs=[tuple(x['job'])for x in previous_errors]
  for x in previous:
   invalid=any(max(abs(s['vmax']),abs(s['vmin']))>20 for y in x['stage_metrics'].values()for s in y.get('stages',[]))
   if invalid:jobs.append((x['solution'],x['case'],x['z0_ohm'],x['ron_ohm'],x['voltage'],x['cin_pf'],x['corner'],x['td_ns'],x['variant'],x['ax_model']=='OEM_IV_SUBSET'))
   else:rows.append(x)
  (R/'results/SI_REPAIR_JOBS.json').write_text(json.dumps(jobs,indent=2),encoding='utf-8')
 with ThreadPoolExecutor(max_workers=4)as pool:
  futures={pool.submit(run_case,*a):a for a in jobs}
  for f in as_completed(futures):
   try:rows.append(f.result())
   except Exception as e:errors.append(dict(job=futures[f],error=str(e)))
   if(len(rows)+len(errors))%50==0:print(json.dumps(dict(completed=len(rows),errors=len(errors),total=len(jobs))),flush=True)
 (R/'results/SI_MATRIX.json').write_text(json.dumps(rows,indent=2),encoding='utf-8');(R/'results/SI_ERRORS.json').write_text(json.dumps(errors,indent=2),encoding='utf-8')
 summary={s:dict(cases=sum(x['solution']==s for x in rows),pass_count=sum(x['solution']==s and x['model_joint_status']=='PASS'for x in rows),fail_count=sum(x['solution']==s and x['model_joint_status']=='FAIL'for x in rows))for s in'ABCDEFG'}
 (R/'results/SI_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(dict(summary=summary,errors=errors[:2])))
 if errors:raise SystemExit(1)
if __name__=='__main__':
 import sys
 main('--smoke'in sys.argv,'--resume-errors'in sys.argv)
