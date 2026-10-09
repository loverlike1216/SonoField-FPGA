"""Independent candidate checks. No board programming or physical pass claims."""
from pathlib import Path
import argparse,csv,hashlib,itertools,json,math,random,re,subprocess,sys,zipfile,xml.etree.ElementTree as ET
HERE=Path(__file__).resolve().parent; V=HERE.parents[2]; R=V.parent
REFERENCE=V/'evidence/board_bringup/20261009/package_pin_database.csv'
checks=[]
def check(name,condition,detail):
 checks.append(dict(name=name,status='PASS' if condition else 'FAIL',detail=detail))
 if not condition:raise AssertionError(name)

class Safety:
 """Functional abstraction of READY/ARMED/TX_SEEN async-clear latch candidate.
 Analog thresholds, pulse glitches and unpowered chip behavior are outside this model.
 """
 def __init__(self):self.ready=False;self.armed=False;self.seen=False;self.prev_request=False
 def step(self,*,healthy,request=False,clear_latch=False,tx_good=False):
  if not healthy:self.ready=self.armed=self.seen=False
  else:
   if clear_latch:self.ready=True
   if not request:self.seen=False
   if self.seen and not tx_good:self.armed=False
   if request and not self.prev_request:self.armed=self.ready
   if self.armed and tx_good:self.seen=True
  self.prev_request=request
  power=bool(healthy and request and self.armed)
  output=bool(power and self.ready and tx_good)
  return power,output

def safety_checks():
 faults=['logic_power','upstream_power','watchdog_ok','estop_ok','cable_present','local_fault_clear','fpga_configured']
 n=0
 for flags in itertools.product([False,True],repeat=len(faults)):
  healthy=all(flags);m=Safety()
  for request,clear,tx in itertools.product([False,True],repeat=3):
   _,on=m.step(healthy=healthy,request=request,clear_latch=clear,tx_good=tx)
   assert not on or (healthy and request and tx and m.ready);n+=1
 check('safety_exhaustive_qualified_inputs',n==1024,{'states':n,'scope':'FUNCTIONAL_MODEL_ONLY'})
 events=[]
 for bad in faults:
  m=Safety();m.step(healthy=True,clear_latch=True);m.step(healthy=True,request=True);assert m.step(healthy=True,request=True,tx_good=True)[1]
  assert m.step(healthy=False,request=True,tx_good=True)==(False,False)
  assert m.step(healthy=True,request=True,tx_good=True)==(False,False)
  m.step(healthy=True,request=False,clear_latch=True)
  assert m.step(healthy=True,request=True,tx_good=True)[1]
  events.append({'fault':bad,'shutdown':'PASS','automatic_restart':'REJECTED','controlled_rearm':'PASS'})
 m=Safety();m.step(healthy=True,clear_latch=True);m.step(healthy=True,request=True,tx_good=True)
 assert m.step(healthy=True,request=True,tx_good=False)==(False,False)
 assert m.step(healthy=True,request=True,tx_good=True)==(False,False)
 check('tx_power_loss_requires_new_enable_edge',True,'TX_SEEN latch prevents automatic power recovery')
 up,dn=Safety(),Safety()
 for m in [up,dn]:m.step(healthy=True,clear_latch=True);assert m.step(healthy=True,request=True,tx_good=True)[1]
 assert not up.step(healthy=False,request=True,tx_good=True)[1]
 assert dn.step(healthy=True,request=True,tx_good=True)[1]
 check('independent_array_disable',True,'Functional abstraction, no actual driver board')
 (OUT/'safety_fault_matrix.json').write_text(json.dumps({'classification':'SIMULATION_ESTIMATE_FUNCTIONAL_NOT_ELECTRICAL','events':events,
  'uncovered':['individual DATA wire interruption with heartbeat intact','analog power ramp/driver below4.5V','gate hazards and synchronizer/async clear pulse widths','watchdog oscillator/timing tolerance','component short circuit','discharge and physical rearm behavior']},indent=2)+'\n',encoding='utf-8')

def xlsx(path):
 ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
 with zipfile.ZipFile(path) as z:
  strings=[]
  if 'xl/sharedStrings.xml' in z.namelist():strings=[''.join(el.itertext()) for el in ET.fromstring(z.read('xl/sharedStrings.xml'))]
  sheets=[]
  for name in sorted(n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$',n)):
   cells={}
   for c in ET.fromstring(z.read(name)).findall('.//m:c',ns):
    val=c.find('m:v',ns);v=val.text if val is not None else None
    if c.get('t')=='s':v=strings[int(v)]
    if c.get('t')=='inlineStr':v=''.join(c.find('m:is',ns).itertext())
    f=c.find('m:f',ns);cells[c.get('r')]={'value':v,'formula':f.text if f is not None else None,'type':c.get('t')}
   sheets.append(cells)
  return sheets

def main():
 global OUT
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
 OUT=(V/args.output).resolve()
 if not OUT.is_relative_to(V/'evidence'):raise ValueError('Candidate evidence must stay in this v5 clone')
 if (OUT/'candidate_checks.json').exists():raise FileExistsError('Use new evidence directory')
 OUT.mkdir(parents=True,exist_ok=True)
 pins=list(csv.DictReader((HERE/'connector_pinmap_candidate.csv').open(encoding='utf-8-sig')))
 db={r['pin']:r for r in csv.DictReader(REFERENCE.open())}
 gpio=[p for p in pins if p['bank']]
 check('connector_all80_and_unique68',len(pins)==80 and len(gpio)==68 and len(db)==68,'Official connector candidate only; no physical continuity claimed')
 check('vivado_pin_bank_crosscheck',all(db[p['package_pin']]['bank']==p['bank'] for p in gpio),'Vivado2025.2 database; clock-capable fields retained in pin_func')
 check('gpio_assignment63',sum(p['v5_signal']!='RESERVED' for p in gpio)==63,'includes2SYNC+1ESTOP')
 addresses=[0x40,0x41,0x44,0x48,0x49,0x4b];check('i2c_addresses_no_collision',len(set(addresses))==6,'Proposed INA22640/41/44 TMP11748/49/4B; straps must be verified')
 config=json.loads((HERE/'adc_candidate.json').read_text());regs={int(k,16):v for k,v in config['registers'].items()}
 rom=[int(v,16) for v in re.findall(r"command=16'h([0-9a-f]{4})",(HERE/'ad7606c_candidate_rom.sv').read_text())][:-1]
 check('adc_bandwidth_write_and_readback_present',0x07ff in rom and 0x4700 in rom,'Official BANDWIDTH address0x07,all8bits=1; original core does not contain this')
 good={2:0x10,3:0x11,4:0x11,5:0x11,6:0x11,7:0xff}
 verified=lambda observed:all(observed.get(k)==v for k,v in good.items())
 check('adc_candidate_readback_fault_rejection',verified(regs) and all(not verified({**regs,k:regs[k]^1}) for k in good),'Each of6 register corruptions rejects READY in reference policy; production RTL not modified')
 rng=random.Random(20261009);frames=[[0,-32768,32767,-1,1,0x1234,-1234,42]]+[[rng.randint(-32768,32767) for _ in range(8)] for _ in range(255)]
 vec=[''.join(f'{v&0xffff:04x}' for v in reversed(frame)) for frame in frames]
 (OUT/'adc_vectors.mem').write_text('\n'.join(vec)+'\n',encoding='ascii')
 # Per-lane wire shifts MSB first, CH1/2 through CH7/8; channel-major decoder independent of RTL.
 for frame in frames:
  lanes=[[(frame[2*k+j]>>b)&1 for j in (0,1) for b in range(15,-1,-1)] for k in range(4)]
  decoded=[]
  for lane in lanes:
   for j in (0,1):
    raw=sum(lane[j*16+b]<<(15-b) for b in range(16));decoded.append(raw-65536 if raw&32768 else raw)
  assert decoded==frame
 check('adc_four_lane_signed_reference',True,{'frames':256,'seed':20261009,'hash':hashlib.sha256(('\n'.join(vec)+'\n').encode()).hexdigest(),'analog_synchrony':'NOT_MEASURED'})
 safety_checks()
 working=R/'v5/hardware/bom/working/2026-10-09/BOM_AX7020_NU40C10T_WORKING_2026-10-09.xlsx'
 sheets=xlsx(working);bom=sheets[1]
 for row in range(5,77):
  total=sum(float(bom.get(f'{c}{row}',{}).get('value') or 0) for c in 'HIJKL')
  assert bom[f'M{row}']['formula'].lstrip('=')==f'SUM(H{row}:L{row})'
  assert float(bom[f'M{row}']['value'])==total
  assert float(bom[f'N{row}']['value'] or 0)>=total
 check('workbook72_formulas_recalculated',True,'All72 unchanged SUM formulas/caches checked; purchase>=installed')
 check('workbook_no_formula_errors',not any(c['type']=='e' for sh in sheets for c in sh.values()),'XLSX cached error scan, including added sheet')
 additions=sheets[-1]
 for row in [2,3,6,7,8,9]:
  assert additions[f'F{row}']['formula'].lstrip('=')==f'SUM(C{row}:E{row})'
  assert float(additions[f'F{row}']['value'])==sum(float(additions[f'{c}{row}']['value'] or 0) for c in 'CDE')
 check('six_added_quantity_formulas_recalculated',True,'Extra candidate/passive allocations are not an automatic purchase release')
 source=R/'v5/hardware/bom/submissions/2026-10-08/BOM_AX7020_NU40C10T_2026-10-08.xlsx'
 check('original_bom_unchanged',hashlib.sha256(source.read_bytes()).hexdigest()=='decf6b026c0b5a48efb6800d27463246d61f62a9e2de01c75da5012d7fe69a35','User original preserved byte-identically')
 budgets=[]
 for cap_nf,v in itertools.product([1,2,3],[5,10,12,16]):
  c=cap_nf*1e-9;f=40000;n=64;current=n*c*v*f;power=n*c*v*v*f
  budgets.append(dict(channels=n,capacitance_nf_assumption=cap_nf,drive_v_assumption=v,frequency_hz=f,ideal_capacitive_average_a=current,ideal_charging_power_w=power,
   classification='CALCULATION_NOT_MEASUREMENT',excludes='resonant/motional load,driver loss/quiescent,logic,AFE,buck,inrush'))
 (OUT/'power_sweep.csv').write_text('channels,capacitance_nf,drive_v,frequency_hz,ideal_average_a,ideal_charging_w\n'+''.join(f"{r['channels']},{r['capacitance_nf_assumption']},{r['drive_v_assumption']},{r['frequency_hz']},{r['ideal_capacitive_average_a']:.6f},{r['ideal_charging_power_w']:.6f}\n" for r in budgets),encoding='utf-8')
 calculations={'efuse_nominal_ilim_a':3334/1650,'ina226_current_full_scale_a':0.08192/0.020,'shunt_loss_w_at2a':2**2*.020,
  'buck_feedback_v':.8*(1+590000/100000),'ldo_maximum_a':.2,'ldo_nominal_headroom_v':.52,'ldo_200ma_max_dropout_v':.420,
  'adc_c16_max_avcc_a_at1msps':.050,'adc_ldo_nominal_loss_w':.52*.050,'array_sweep':budgets,
  'full_board_peak_min_max':'NOT_DETERMINED_C0_MOTIONAL_PARAMETERS_AND_INRUSH_REQUIRED','copper_temperature_and_width':'NOT_DETERMINED_NO_STACKUP',
  'surge_coordination':'FAIL_UNQUALIFIED_SMBJ20A32.4V_VS_EFUSE28V_ABSMAX'}
 check('power_budget_bounds_recorded',calculations['efuse_nominal_ilim_a']<calculations['ina226_current_full_scale_a'],'Not a real thermal or surge test')
 (OUT/'candidate_checks.json').write_text(json.dumps({'status':'PASS','classification':'OFFLINE_CANDIDATE_CHECKS_ONLY','checks':checks,'calculations':calculations,
  'hardware_tests':'NOT_RUN','native_erc':'NOT_RUN','independent_review':'PENDING'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','checks':len(checks),'physical_validation':'NOT_RUN'}))
if __name__=='__main__':main()
