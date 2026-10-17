"""Fresh bounded models; this file never claims physical or full vendor-SPICE proof."""
from pathlib import Path
import csv,json,itertools,math,subprocess,ctypes,sys
import numpy as np
R=Path(__file__).resolve().parents[1];V=Path('E:/Codex_project/AMD_Sonofield/v5')
NG='E:/Codex_project/SonoField_v5_Fixed12V_Audit_20261015/tools/ngspice_py7zr/Spice64/bin/ngspice_con.exe'
d=json.loads((R/'results/FINAL_CONNECTION_DATABASE.json').read_text(encoding='utf-8'))
def save(name,rows):
 with(R/'results'/name).open('w',encoding='utf-8-sig',newline='')as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def dump(name,x):(R/'results'/name).write_text(json.dumps(x,indent=2,ensure_ascii=False),encoding='utf-8')
checks=[]
def check(name,ok,detail):checks.append(dict(check=name,status='PASS'if ok else'FAIL',detail=detail))
#Feedback resistor .1%, 25ppm/K and55K sensitivity; line/load .6%,20mV ripple.
tol=.001+25e-6*55;rails={}
for name,lo,hi,top in [('V3V3',.581,.611,45300),('V7V15',.581,.611,110000),('VTX_PRE',.581,.611,158000),('V5A',1.228,1.252,31000)]:
 a=[ref*(1+top*(1+t)/(10000*(1+b)))*(1+e)+r for ref,t,b,e,r in itertools.product([lo,hi],[-tol,tol],[-tol,tol],[-.006,.006],[-.02,.02])]
 rails[name]=dict(min=min(a),max=max(a))
check('ADC/OPA/analog switches5Vrail',rails['V5A']['min']>=4.75 and rails['V5A']['max']<=5.25,rails['V5A'])
check('LVT/5953V3rail',rails['V3V3']['min']>=3.0 and rails['V3V3']['max']<=3.6,rails['V3V3'])
vtx=rails['VTX_PRE']['max']+.15;rmin=150*(1-.01-100e-6*55)
txbound=64*vtx*vtx/(4*rmin)+.032*vtx+.12
arrayinput=(txbound+rails['V3V3']['max']*.7+rails['V7V15']['max']*.2)/.8+.3
ilimlo=3334/(1300*1.01)*.9;ilimhi=3334/(1300*.99)*1.1
check('Passive-load upper power and eFuse/3A connector',arrayinput/11.4<ilimlo and ilimhi<3,dict(array_upper_w=arrayinput,input_at11V4_a=arrayinput/11.4,ilim_min_a=ilimlo,ilim_max_a=ilimhi))
check('150R1W resistor bounded passive power',vtx*vtx/(4*rmin)<.5,dict(upper_w=vtx*vtx/(4*rmin)))
check('TXbuck2A and1.5A reservation',txbound/rails['VTX_PRE']['min']<1.5,dict(upper_a=txbound/rails['VTX_PRE']['min']))
power=dict(rails=rails,tx_bus_transient_assumption_v=.15,tx_upper_w=txbound,array_input_upper_w=arrayinput,array_reserved_w=24,central_reserved_w=8,adapter_each='regulated12V3A36W, independently isolated SELV output',thermal=dict(ambient_design_c=[0,40],buck_loss_design_w=1.2,buck_theta_board_assumption=65.,buck_tj_estimate=40+1.2*65.,buck_theta_official_evm=57.2,ldo_reserved_a=.15,ldo_tj_estimate=40+(rails['V7V15']['max']-rails['V5A']['min'])*.15*100,scope='THERMAL_ESTIMATE; actual copper/layout not created; TPS7A26DRV requiresEPgroundcopper;TPS54202DDC hasnoEP,usepinthermalcopper/plane/vias'))
check('Thermal estimate within stated PCB thermal budget',power['thermal']['buck_tj_estimate']<125 and power['thermal']['ldo_tj_estimate']<125,dict(basis='engineering upperloss1.2W; requirePCBtheta<=65C/W, TI EVM57.2C/W is feasibility reference, noactualboardmeasurement',**power['thermal']))
dump('POWER_FINAL.json',power)
#Re-use only the mathematical function body, never old main(), reports or models.
from power_budget_model import periodic
bvd=[]
for c0,cm,q,fs,fd,rs,cb in itertools.product([2e-9,3e-9],[.02e-9,.1e-9,.5e-9],[10,50,100],[39200,40000,40800],[38500,40000,41500],[rmin,151.5],[95e-9,105e-9]):
 bvd.append(dict(c0_f=c0,cm_f=cm,q=q,fs_hz=fs,drive_hz=fd,r_ohm=rs,cb_f=cb,**periodic(vtx,c0,cm,q,fs,fd,rs,cb,256)))
worst=max(bvd,key=lambda x:x['vpp_v']);refined=periodic(vtx,worst['c0_f'],worst['cm_f'],worst['q'],worst['fs_hz'],worst['drive_hz'],worst['r_ohm'],worst['cb_f'],2048)
save('BVD_FINAL_SCAN.csv',bvd);dump('BVD_FINAL.json',dict(cases=len(bvd),worst=worst,refined=refined,scope='UNFITTED_BVD sensitivity, motional Q/Cm are engineering assumptions, no supplier impedance fit, no SPL claim'))
check('NU continuous<20Vpp in stated BVD envelope',max(x['vpp_v']for x in bvd)<20 and refined['vpp_v']<20,refined)
#Derive safety combinational gates from exported physical pins independently.
idx={(x['refdes'],int(x['pin'])):x['net']for x in d['pins']if x['board']=='UP'and str(x['pin']).isdigit()}
parts=[x for x in d['instances']if x['board']=='UP']
def comb(s):
 s=dict(s)
 for _ in range(20):
  for x in parts:
   g=lambda p:idx[(x['refdes'],p)]
   if x['mpn']in('SN74LVC2G08DCUR','SN74LVC2G32DCUR'):
    for a,b,y in [(1,2,7),(5,6,3)]:
     if g(a)in s and g(b)in s and g(y)!='NC':s[g(y)]=(s[g(a)]and s[g(b)])if '2G08'in x['mpn']else(s[g(a)]or s[g(b)])
   elif x['mpn']in('SN74LVC1G14DBVR','SN74LVC1G17DBVR')and g(2)in s:s[g(4)]=(not s[g(2)])if'1G14'in x['mpn']else s[g(2)]
 return s
truth=[]
for bits in itertools.product([False,True],repeat=9):
 por,v5,tx,central,arm,permit,oe,sr,rc=bits
 state=dict(GND=False,V3V3=True,POR_N=por,V5_GOOD=v5,TX_PRE_GOOD=tx,CENTRAL_POWER_OK=central,ARM_SEEN=arm,TX_PERMIT=permit,OE_N=oe,SRCLK_ALIVE=sr,RCLK_ALIVE=rc)
 s=comb(state)
 #Asynchronous clear on U_ARM dominates its Q; clock resume is not a newpermit.
 if not s[idx[('U_ARM',6)]]:state['ARM_SEEN']=False;s=comb(state)
 expected=por and v5 and tx and central and arm and permit and not oe and sr and rc
 truth.append(dict(zip(['por','v5','tx_pre','central','armed_requested','permit','oe_n','sr_alive','rc_alive'],bits),enable=s['EN_PERMIT'],expected=expected,match=s['EN_PERMIT']==expected))
save('FAULT_TRUTH_FINAL.csv',truth);check('512 physical-pin-derived safety combinations',all(x['match']for x in truth),dict(cases=len(truth)))
#Input RC fault reporting: 5ns normal-arm skew rejected; latched failure reported.
tau=1000*1e-9;short=3.3*math.exp(-5e-9/tau);report_us=-tau*math.log(.7/3.3)*1e6
check('Fault-report RC does not filter localEN cutoff',short>2.1 and report_us<2,dict(v_after5ns=short,fall_below0V7_us=report_us,local_en='asynchronous unfiltered'))
#Post-cutoff capacitance is derived from actual BOM, not an assumed32x100nF.
caps=[x for x in d['passives']if x['board']=='UP'and x['pin1_net']=='VTX'and x['pin2_net']=='GND'and x['refdes'].startswith('C')]
load=sum({'100nF':.1e-6,'1uF':1e-6}[x['value']]for x in caps)
check('Switched TX capacitance7.2uF',abs(load-7.2e-6)<1e-12,dict(capacitors=len(caps),nominal_f=load))
#Finite-slope, generic PMOS equivalent: not an AO4407 vendor SPICE model.
sp=[]
for k,(vt,kp,cl,cm)in enumerate(itertools.product([-1.,-3.],[4.,12.],[load*.8,load*1.2],[9.5e-9,10.5e-9])):
 out=R/'results/power_spice'/str(k);out.mkdir(parents=True,exist_ok=True)
 net=f'''* bounded PMOS Miller softstart equivalent; not OEM device model
Vsrc source 0 10.55
Vctl collect 0 pulse(10.55 .2 50u 20n 20n 500u 1m)
Rpull source gate 100k
Rdrive gate collect 10k
Cm gate drain {cm}
Mpower drain gate source source P
.model P pmos(level=1 vto={vt} kp={kp} lambda=.001)
Cload drain 0 {cl}
Rbleed drain 0 2200
.control
set wr_vecnames
set wr_singlescale
tran .1u 800u
wrdata wave.txt v(drain) v(gate) i(Vsrc)
quit
.endc
.end
'''
 (out/'network.cir').write_text(net,encoding='ascii');q=subprocess.run([NG,'-n','-b','network.cir'],cwd=out,capture_output=True,text=True,timeout=30);(out/'ngspice.log').write_text(q.stdout+q.stderr,encoding='utf-8');assert q.returncode==0
 a=np.loadtxt(out/'wave.txt',skiprows=1);on=(a[:,0]>50e-6)&(a[:,0]<550e-6)
 row=dict(case=k,vto=vt,kp=kp,load_f=cl,miller_f=cm,peak_inrush_a=float((-a[on,3]).max()),minimum_before_on_v=float(a[a[:,0]<49e-6,1].max()),settled_at500us_v=float(a[np.argmin(abs(a[:,0]-500e-6)),1]));sp.append(row)
save('POWER_SOFTSTART_SPICE.csv',sp);check('Generic softstart inrush<1.5A, defaultoff and settled',all(x['peak_inrush_a']<1.5 and x['minimum_before_on_v']<.1 and x['settled_at500us_v']>9.5 for x in sp),dict(cases=len(sp),max_inrush_a=max(x['peak_inrush_a']for x in sp)))
#Actual C function regression, independently compared with sinusoid least squares.
out=R/'results/feature_after';out.mkdir(exist_ok=True);export=R/'results/feature_before/export.c'
cmd=['D:/DevC++/Dev-Cpp/TDM-GCC-64/bin/gcc.exe','-std=c11','-O2','-Wall','-Wextra','-Werror','-shared','-DSF_PREPCB_EXTENSION','-I'+str(V/'firmware/ps_service'),str(V/'firmware/ps_service/service.c'),str(V/'firmware/ps_service/prepcb_service.c'),str(export),'-lm','-o',str(out/'feature.dll')]
q=subprocess.run(cmd,capture_output=True,text=True);(out/'compile.log').write_text(q.stdout+q.stderr);assert q.returncode==0
f=ctypes.CDLL(str(out/'feature.dll')).feature;f.argtypes=[ctypes.POINTER(ctypes.c_int16),ctypes.c_uint,ctypes.c_uint,ctypes.c_double,ctypes.c_double,*[ctypes.POINTER(ctypes.c_double)]*3]
feature=[]
for frequency,offset,amplitude in itertools.product([38500,40000,40300,41500],[0,16384],[0,1000,5000]):
 fs=128e6/320;n=800;t=np.arange(n)/fs;wave=np.rint(offset+amplitude*np.cos(2*np.pi*frequency*t+.7)).astype(np.int16);arr=np.tile(wave[:,None],(1,8)).ravel();buf=(ctypes.c_int16*len(arr))(*arr);aa,pp,co=ctypes.c_double(),ctypes.c_double(),ctypes.c_double();ret=f(buf,n,0,fs,frequency,ctypes.byref(aa),ctypes.byref(pp),ctypes.byref(co))
 ref=np.linalg.lstsq(np.column_stack([np.ones(n),np.cos(2*np.pi*frequency*t),np.sin(2*np.pi*frequency*t)]),wave,rcond=None)[0];refa=math.hypot(ref[1],ref[2]);refp=math.atan2(-ref[2],ref[1]);err=abs(math.atan2(math.sin(pp.value-refp),math.cos(pp.value-refp)))
 ok=(ret==-3)if amplitude==0 else(ret==0 and abs(aa.value/refa-1)<.005 and err<math.radians(.5))
 feature.append(dict(frequency_hz=frequency,offset=offset,amplitude=amplitude,returncode=ret,measured_amplitude=aa.value,reference_amplitude=refa,phase_error_rad=err,status='PASS'if ok else'FAIL'))
save('C_FEATURE_BIAS_REGRESSION.csv',feature);check('Actual C biased/noncoherent feature extraction',all(x['status']=='PASS'for x in feature),dict(cases=len(feature),classification='HOST_FIXTURE_NOT_PHYSICAL_ADC'))
dump('ELECTRICAL_FINAL_CHECKS.json',checks);print(json.dumps(dict(checks=len(checks),fail=[x for x in checks if x['status']=='FAIL']),ensure_ascii=False));assert all(x['status']=='PASS'for x in checks)


