"""Generate current candidate contracts from unchanged pre-PCB provenance."""
from pathlib import Path
import copy,csv,hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'hardware/next_stage/20261010'
def save(name,data):
 p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
 source=ROOT/'hardware/prepcb/bom_inputs.json';d=copy.deepcopy(json.loads(source.read_text(encoding='utf-8')))
 d.update(source='hardware/prepcb/bom_inputs.json',source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),status='PROPOSED_WORKING_NOT_PROCUREMENT_RELEASE',formal_adc='AD7606C-16BSTZ-RL',native_cad='NOT_CREATED',erc='NOT_RUN',manufacturing='HOLD',currency='CNY',prices='UNKNOWN_NO_PURCHASE_AUTHORIZATION')
 for x in d['items']:
  x.update(unit_price=None,currency='CNY',native_footprint='UNVERIFIED',electrical_release='HOLD',pin_count=None)
  if x['id']=='B-001':x.update(mpn='NU40C10T-2_ORDER_CODE_PENDING_VENDOR',family='NU40C10T',package='THT2; body9.8+/-0.5mm; pitch5.0+/-0.5mm; lead0.7+/-0.1mm',pin_count=2,approval='FAMILY_APPROVED_SUFFIX_HOLD',source='USER_VENDOR_IMAGES_HASHES_IN_VENDOR_PARAMETERS.json')
  if x['id']=='B-002':x.update(mpn='NU40C10R-2_CANDIDATE_EXACT_RX_MPN_HOLD',package='THT2_CANDIDATE_VERIFY_RX_MECHANICAL',pin_count=2,approval='PROPOSED_RX_HOLD')
  if x['id']=='B-014':x.update(mpn='AD7606C-16BSTZ-RL',package='LQFP64 ST-64-2; Pin1/native footprint/order suffix HOLD',pin_count=64,approval='USER_APPROVED_DEVICE_DIRECTION_ELECTRICAL_HOLD',source='https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf',supply='AVCC4.75..5.25V; VDRIVE3V3 candidate; highBW220kHz +/-5VSE',current_A=.05,risk='50mA max AVCC1MSPS data-sheet envelope only; add VDRIVE/reference/AFE/startup; not measured central budget')
  if x['id']=='B-016':x.update(mpn='AD7606C16_REFERENCE_DECOUPLING_ALLOCATION',quantities=[0,0,0,0,0],package='ALLOCATION_NOTE_NOT_A_PHYSICAL_COMPONENT',risk='B047central2: REGCAP36/39 each1uF; B049one: REFCAP44+45 10uF lowESR; B046one REFIN42 100nF and four AVCC bypass; remaining aggregate caps require pin-level allocation')
  if x['id']=='B-017':x.update(approval='OPTIONAL_DIAGNOSTIC_ONLY',risk='Humidity not applied to numerical compensation')
  if x['id']=='B-023':x.update(risk='Inherited SMBJ20A clamp cannot be assumed safe for <=23V eFuse; dynamic clamp/current and buck absolute limits HOLD')
  if x['id']=='B-024':x.update(risk='2A candidate is not validated with5A source; fuse/eFuse/wire inrush/selectivity HOLD')
  if x['id']=='B-032':x.update(source='https://www.ti.com/lit/ds/symlink/tmp117.pdf',pin_count=6,risk='3 sensors required; CENTER air representative away from heat; UP0x49/DOWN0x4b/CENTER0x48; read ID/readiness and bounded bus; no temperatureCRC')
  if x['id']=='B-069':x.update(risk='One shared array PCB, opposite assembly orientation; 64TX +4outsideRX, hole/clearance not released')
  if x['id']=='B-070':x.update(risk='Central interface board ONLY AX7020 protected single source per rail; no central external12V')
 # Explicit independent hardware shutdown candidates. Exact MPN/circuit awaits electrical review.
 for ident,description,quantity in [('NS-001','Independent NC estop safety loop connector',[1,1,1,0,0]),('NS-002','Independent thermal comparator and threshold network',[1,1,0,0,0]),('NS-003','Cold-start/rearm latch and power-good AND cutoff controller',[1,1,0,0,0]),('NS-004','Driver rail discharge/bleed and reset default-off network',[1,1,0,0,0])]:
  d['items'].append(dict(id=ident,description=description,mpn='PART_SELECTION_HOLD',package='UNKNOWN',quantities=quantity,supply='LOGIC/12V_DOMAIN_REVIEW',current_A=None,logic='INDEPENDENT_OF_FPGA_PS_PL',measured='NOT_VERIFIED',package_evidence='NOT_VERIFIED',source='Current user GateC3/D1',supplier='NOT_SELECTED',approval='PROPOSED_HOLD',risk='Power-loss/cable/unpowered/clock-stop physical injection required',unit_price=None,currency='CNY',native_footprint='UNVERIFIED',pin_count=None,electrical_release='HOLD'))
 boards={};components=[]
 for board,index,prefix in [('Upper',0,'UP'),('Lower',1,'DN'),('Central',2,'CE'),('External',4,'EX')]:
  refs=[]
  for x in d['items']:
   x.setdefault('references',{})[board]=[f"{prefix}_{x['id'].replace('-','')}_{i+1:03d}" for i in range(x['quantities'][index])]
   for ref in x['references'][board]:
    refs.append(ref);components.append(dict(reference=ref,board=board,bom_id=x['id'],mpn=x['mpn'],pins_status='PENDING_NATIVE_SYMBOL_AND_ELECTRICAL_REVIEW',pin_count=x['pin_count']))
  boards[board]=dict(installed_components=len(refs),references=refs)
 save('BOM_INPUTS.json',d)
 names={1:'AVCC',2:'AGND',3:'OS0',4:'OS1',5:'OS2',6:'PAR_SER',7:'STBY',8:'RANGE',9:'CONVST',10:'WR',11:'RESET',12:'SCLK',13:'CS_N',14:'BUSY',15:'FRSTDATA',23:'VDRIVE',24:'DOUTA',25:'DOUTB',26:'AGND',27:'DOUTC',28:'DOUTD',29:'SDI',34:'REF_SELECT',35:'AGND',36:'REGCAP_A',37:'AVCC',38:'AVCC',39:'REGCAP_D',40:'AGND',41:'AGND',42:'REFIN_REFOUT',43:'REFGND',44:'REFCAPA',45:'REFCAPB',46:'REFGND',47:'AGND',48:'AVCC'}
 names.update({i:f'DB{i-16}' for i in range(16,23)});names.update({i:f'DB{i-18}' for i in range(30,34)})
 names.update({49+2*c:f'V{c+1}P' for c in range(8)});names.update({50+2*c:f'V{c+1}N' for c in range(8)})
 pins=[]
 for pin in range(1,65):
  name=names[pin]
  if name=='AVCC':net='ADC_AVCC5V_FILTERED'
  elif 19<=pin<=22:net=f'NC_UNUSED_DOUT_{chr(69+pin-19)}' # Table23 footnote2: leave unconnected in four-DOUT mode.
  elif name in ('AGND','REFGND') or name.startswith('DB'):net='AGND'
  elif name in ('OS0','OS1','OS2','PAR_SER','STBY','REF_SELECT','WR'):net='CENTRAL_3V3'
  elif name=='RANGE':net='AGND'
  elif name=='VDRIVE':net='CENTRAL_3V3'
  elif name in ('REFCAPA','REFCAPB'):net='ADC_REFCAP4V4'
  elif name.startswith('REGCAP'):net='ADC_'+name
  elif name=='REFIN_REFOUT':net='ADC_REF2V5'
  elif name.startswith('V') and name[-1] in 'PN':net=f"RX_{int(name[1:-1])-1}_{'SIGNAL' if name[-1]=='P' else 'ANALOG_RETURN'}"
  else:net='ADC_'+name
  pins.append(dict(component='CE_B014_001',pin=pin,name=name,net=net,status='DATASHEET_PIN_MAP_PROPOSED_NOT_NATIVE_CAD',source='ADI Rev.A Table9 pp15-17'))
 save('ADC64_PIN_CONTRACT.json',pins)
 connectors=[]
 signal=json.loads((ROOT/'config/SIGNAL_CONTRACT.json').read_text(encoding='utf-8'))
 for p in signal['pins']:connectors.append({k:p[k] for k in ('connector','connector_pin','package_pin','dir','net','power_domain','verification')})
 save('CONNECTOR_PIN_CONTRACT.json',connectors)
 nets=[dict(name=x,driver='INDEPENDENT_HARDWARE_CIRCUIT_REQUIRED',loads=['CUT_OFF','OE_FAIL_CLOSED'],status='PROPOSED_LOGICAL_CONTRACT_ELECTRICAL_HOLD') for x in ('NC_ESTOP_OK','LOCAL_WATCHDOG_OK','HOTSPOT_OK','PGOOD_LOCAL','COLD_START_REARM')]
 contract=dict(status='PROPOSED_MACHINE_READABLE_NETWORK_CONTRACT_NOT_NATIVE_NETLIST_NOT_ERC',native_cad='NOT_CREATED_NO_CONNECTED_EASYEDA',erc='NOT_RUN',manufacturing='HOLD',boards=boards,components=components,adc_pins=pins,ax7020_connectors=connectors,safety_nets=nets,
  power=dict(Upper='EXTERNAL12V_INDEPENDENT_PROTECTED_NOT_FROM_AX7020',Lower='EXTERNAL12V_INDEPENDENT_PROTECTED_NOT_FROM_AX7020',Central='AX7020_J10_J11_ONLY_SINGLE_PROTECTED_SOURCE_PER_RAIL_NO_BACKFEED',budget='CENTRAL_POWER_BUDGET_BLOCKED'),
  array_design='ONE_COMMON_PCB_BOM; Upper radiates-Z / Lower+Z; positions centered; RX corner+-54mm CANDIDATE',
  adc=dict(channels=8,location='CENTRAL_SINGLE_DEVICE',dout_pins=[24,25,27,28],lane_channels=[[1,2],[3,4],[5,6],[7,8]],straps='OS111 PAR_SER1 STBY1 REFSEL1 RANGE0 WR1',decoupling={'REGCAP36':'1uF separate toAGND','REGCAP39':'1uF separate toAGND','REFCAP44_45':'join and10uF lowESR toREFGND','REFIN42':'100nF toREFGND','AVCC1_37_38_48':'local100nF each plusbulk'}),
  unresolved=['All nonADC native symbol/footprint/pin-to-pin nets require verification; aggregate passives not fully allocated','Rev3 J10/J11 power current/voltage/pin qualification','AFE gain/blank/protection/noise/group-delay and alias attenuation','Independent cutoff actual netlist/MPNs/thresholds/rearm','66MHz external timing/clock fanout/min-max SI','ADC power-good/brownout and safe recovery wiring','No PCB/Gerber/purchase release'])
 save('SCHEMATIC_CONTRACT.json',contract)
 rows=[]
 for n in (1,4,16,64):
  for capacitance in (1.76,2.2,2.64):
   for voltage in (6,12):rows.append(dict(channels=n,C_nF=capacitance,V_swing=voltage,f_Hz=40000,ideal_CV2f_W=n*capacitance*1e-9*voltage**2*40000,classification='IDEAL_CHARGING_SENSITIVITY_NOT_MEASURED_NOT_UPPER_BOUND'))
 save('POWER_SENSITIVITY.json',rows)
 with (OUT/'PIN_REVIEW.csv').open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(pins[0]));w.writeheader();w.writerows(pins)
 print(json.dumps(dict(status='GENERATED_CANDIDATE',bom_types=len(d['items']),boards={k:v['installed_components'] for k,v in boards.items()},adc_pins=len(pins),native_erc='NOT_RUN'),indent=2))
if __name__=='__main__':main()
