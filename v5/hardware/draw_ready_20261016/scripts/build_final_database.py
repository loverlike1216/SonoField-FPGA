"""Additive final candidate; original supplied BOM/EDA files are never written."""
from pathlib import Path
import json,csv,collections,copy
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'inputs/PREVIOUS_CONNECTION_DATABASE.json').read_text(encoding='utf-8'))
def remove(board,refs):
 for k in ['instances','pins','passives']:d[k]=[x for x in d[k]if not(x['board']==board and x['refdes']in refs)]
def pnet(board,ref,pin,net):
 a=[x for x in d['pins']if x['board']==board and x['refdes']==ref and x['pin']==str(pin)];assert len(a)==1,(board,ref,pin)
 a[0]['net']=net
 for x in d['passives']:
  if x['board']==board and x['refdes']==ref:x['pin'+str(pin)+'_net']=net
def chip(board,ref,mpn,pkg,pins,url,rating):
 assert not any(x['board']==board and x['refdes']==ref for x in d['instances']),(board,ref)
 d['instances'].append(dict(board=board,refdes=ref,mpn=mpn,package=pkg,source=url,note='',value='IC',manufacturer='Texas Instruments'if'mti'in url or'ti.com'in url else'Analog Devices',rating=rating,role=ref,source_url=url,lcsc='待采购映射',selection_status='PASS',procurement_status='HOLD_PRICE_STOCK_EDA_NOT_VERIFIED'))
 for p,(func,net,kind)in pins.items():d['pins'].append(dict(board=board,refdes=ref,mpn=mpn,pin=str(p),function=func,net=net,kind=kind,source=url,status='PASS'))
def passive(board,ref,value,a,b,mpn=None,package='0603',rating=None,url=None):
 cap=ref.startswith('C');mpn=mpn or('C0603C104K5RACTU'if cap else'RC0603FR-07'+value.replace('k','K').replace('.','R')+'L')
 rating=rating or('50V X7R ±10%'if cap else'0.1W ±1%');url=url or('https://www.yageo.com/en/Product/Index/product_category/resistor/rc'if not cap else'https://www.kemet.com/en/us/capacitors/ceramic.html')
 chip(board,ref,mpn,package,{1:('1',a,'PASSIVE'),2:('2',b,'PASSIVE')},url,rating)
 x=d['instances'][-1];x.update(value=value,manufacturer='YAGEO'if not cap else'KEMET (YAGEO)')
 d['passives'].append(dict(board=board,refdes=ref,value=value,pin1_net=a,pin2_net=b,package=package,rating=rating,mpn=mpn,manufacturer=x['manufacturer'],role=ref,source_url=url,polarity='nonpolar',status='PASS'))
def resistor_value(board,ref,value):
 for k in ['instances','passives']:
  x=next(x for x in d[k]if x['board']==board and x['refdes']==ref);x.update(value=value,mpn='RC0603FR-07'+value+'RL',rating='0.1W ±1%',manufacturer='YAGEO',source_url='https://www.yageo.com/en/Product/Index/product_category/resistor/rc')
 for x in d['pins']:
  if x['board']==board and x['refdes']==ref:x['mpn']='RC0603FR-07'+value+'RL'
def decouple(board,ref,rail='V3V3'):passive(board,'C_'+ref,'100nF',rail,'GND')
LVT='SN74LVT244BPWR';LVTURL='https://www.ti.com/lit/ds/symlink/sn74lvt244b.pdf'
AIN=[2,4,6,8,11,13,15,17];YOUT=[18,16,14,12,9,7,5,3]
def buffer(board,ref,channels):
 pins={1:('1OE_N','GND','IN'),19:('2OE_N','GND','IN'),10:('GND','GND','POWER'),20:('VCC','V3V3','POWER')}
 for i in range(8):
  a,b=channels[i]if i<len(channels)else('GND','NC');pins[AIN[i]]=(f'A{i}',a,'IN');pins[YOUT[i]]=(f'Y{i}',b,'NC'if b=='NC'else'OUT')
 chip(board,ref,LVT,'PW/TSSOP20',pins,LVTURL,'VCC2.7–3.6V; input≤5.5V; Ioff≤100uA; CL50pF tPLH1.1–3.5ns/tPHL1.3–3.3ns; −40..85°C');decouple(board,ref)
def gate(board,ref,mpn,kind,pairs):
 #TI DCU dual gate common pinout 1A1/2B1/3Y2/4GND/5A2/6B2/7Y1/8VCC.
 pins={4:('GND','GND','POWER'),8:('VCC','V3V3','POWER')}
 for j,(a,b,y)in enumerate(pairs):
  for p,f,n,k in zip(([1,2,7]if j==0 else[5,6,3]),['A','B','Y'],[a,b,y],['IN','IN','OUT']):pins[p]=(f+str(j+1),n,'NC'if n=='NC'else k)
 chip(board,ref,mpn,'DCU/VSSOP8',pins,'https://www.ti.com/lit/ds/symlink/'+mpn.lower().replace('dcur','')+'.pdf','VCC3.3V; inputs5.5V tolerant; Ioff');decouple(board,ref)
def inverter(board,ref,mpn,a,y):
 chip(board,ref,mpn,'DBV/SOT23-5',{1:('NC','NC','NC'),2:('A',a,'IN'),3:('GND','GND','POWER'),4:('Y',y,'OUT'),5:('VCC','V3V3','POWER')},'https://www.ti.com/lit/ds/symlink/'+mpn.lower().replace('dbvr','')+'.pdf','VCC3.3V; Schmitt input; Ioff');decouple(board,ref)
#Same physical power-reference contact, named explicitly; never parallel localrail.
for k in ['pins','passives','fpga']:
 for x in d[k]:
  for f,v in list(x.items()):
   if isinstance(v,str):x[f]=v.replace('AX_VIO3V3','AX_VIO_REF3V3')
#Reference-derived buck compensation and bias-independent minimumbulkcapacitance.
for board in ['CENTRAL','UP','DN']:
 for j,rail in [(1,'V3V3'),(2,'V7V15')]+([]if board=='CENTRAL'else[(3,'VTX_PRE')]):
  if j!=3:
   ref=f'C_B{j}_BULK';passive(board,ref,'47uF',rail,'GND',mpn='25SVPF47M',package='Panasonic C6 Ø6.3mm height6mm polar',rating='25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C',url='https://industrial.panasonic.com/sa/products/pt/os-con/models/25SVPF47M');d['instances'][-1]['manufacturer']='Panasonic';d['passives'][-1]['manufacturer']='Panasonic';d['passives'][-1]['polarity']='pin1positive;pin2negative'
  passive(board,f'C_B{j}_FF','220pF',rail,f'BUCK{j}_FB',mpn='C0603C221J5GACTU',rating='50V C0G ±5%; TPS54202equation16 feedforward',url='https://www.ti.com/lit/ds/symlink/tps54202.pdf')
#Proper receiver-local RC and regenerated32 data lanes, no DC termination current.
central_channels=[]
for side in ['UP','DN']:
 for i in range(16):
  raw=f'{side}_DATA_RAW_{i:02d}';filt=f'{side}_DATA_FILT_{i:02d}';out=f'{side}_DATA_DRV_{i:02d}'
  old=f'R_PASS_D_{side}{i:02d}';remove('CENTRAL',[old])
  passive('CENTRAL',f'R_RX_{side}{i:02d}','22',raw,filt,mpn='RC0603FR-0722RL')
  passive('CENTRAL',f'C_RX_{side}{i:02d}','3.3pF',filt,'GND',mpn='CC0603JRNPO9BN3R3',rating='50V C0G ±5%',url='https://www.yageo.com/en/Product/Index/product_category/mlcc/npo')
  passive('CENTRAL',f'R_TX_{side}{i:02d}','47',out,f'{side}_DATA_{i:02d}',mpn='RC0603FR-0747RL')
  central_channels.append((filt,out))
for i in range(4):buffer('CENTRAL',f'U_TXB{i}',central_channels[i*8:i*8+8])
clock_channels=[]
for signal in ['SRCLK','RCLK']:
 filt='MASTER_'+signal+'_FILT';passive('CENTRAL','R_RX_'+signal,'22','MASTER_'+signal,filt,mpn='RC0603FR-0722RL');passive('CENTRAL','C_RX_'+signal,'3.3pF',filt,'GND',mpn='CC0603JRNPO9BN3R3',rating='50V C0G ±5%',url='https://www.yageo.com/en/Product/Index/product_category/mlcc/npo')
 for side in ['UP','DN']:
  remove('CENTRAL',[f'R_PASS_{side}_{signal}']);clock_channels.append((filt,f'{side}_{signal}_DRV'));passive('CENTRAL',f'R_TX_{side}_{signal}','47',f'{side}_{signal}_DRV',f'{side}_{signal}',mpn='RC0603FR-0747RL')
buffer('CENTRAL','U_TXCLK',clock_channels)
for board in ['UP','DN']:
 remove(board,['U_FAST','C_FAST_IN','C_FAST_OUT'])
 #Four1uF localbank capacitors plus32x100nF remain aftercutoff (7.2uF nominal).
 remove(board,[f'C_DRV_BULK{j:02d}'for j in range(32)if j not in(0,8,16,24)])
 #Bulkenergy stays before cutoff; drain-to-gate Miller capacitor boundsinrush.
 remove(board,[f'C_TX_BANK{j}'for j in range(4)]+['C_TX_LOCAL','R_GATE_DRIVE'])
 passive(board,'C_TX_LOCAL','47uF','VTX_PRE','GND',mpn='25SVPF47M',package='Panasonic C6 Ø6.3mm height6mm polar',rating='25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C',url='https://industrial.panasonic.com/sa/products/pt/os-con/models/25SVPF47M');d['instances'][-1]['manufacturer']='Panasonic';d['passives'][-1]['manufacturer']='Panasonic';d['passives'][-1]['polarity']='pin1positive;pin2negative'
 passive(board,'R_GATE_DRIVE','10k','TX_GATE','CUT_COLLECTOR',mpn='RC0603FR-0710KL')
 passive(board,'C_TX_MILLER','10nF','TX_GATE','VTX',mpn='C1206C103J5GACTU',package='1206',rating='50V C0G ±5%; drain-to-gate softstart; notgate-to-source')
 for ref in ['U_DBUF0','U_DBUF1','U_CLK_SRCLK','U_CLK_RCLK']:
  old=[x for x in d['pins']if x['board']==board and x['refdes']==ref]
  ch=[(next(x['net']for x in old if x['pin']==str(a)),next(x['net']for x in old if x['pin']==str(y)))for a,y in zip(AIN,YOUT)]
  if ref.startswith('U_CLK_'):ch=ch[:4]
  remove(board,[ref,'C_'+ref]);buffer(board,ref,ch)
 #Retain four595 per strobe output; two clock buffers perarray, separatefanout.
 for signal in ['SRCLK','RCLK']:
  for j in range(4,8):remove(board,[f'R_CLK_{signal}{j}'])
  for j in range(4):resistor_value(board,f'R_CLK_{signal}{j}','15')
  for j in range(16):pnet(board,f'U_SR{j:02d}',11 if signal=='SRCLK'else 12,f'{signal}_G{j//4}')
 for x in list(d['passives']):
  if x['board']==board and x['pin2_net'].startswith('DATA_LOCAL_'):resistor_value(board,x['refdes'],'47')
 #Saturate default-on EN clamp even with64enable pullups at twice nominalcurrent.
 for x in list(d['passives']):
  if x['board']==board and x['pin1_net']=='VTX'and x['pin2_net']=='ENCLAMP_BASE_G0':
   ref=x['refdes'];remove(board,[ref]);passive(board,ref,'8.2k','VTX','ENCLAMP_BASE_G0',mpn='RC0603FR-078K2L')
 #Independent clocks stop detection; localpermit rearm requires a newedge.
 for signal in ['SRCLK','RCLK']:
  ref='U_WDIV_'+signal;fb=signal+'_DIV_N';q=signal+'_DIV'
  chip(board,ref,'SN74LVC1G74DCUR','DCU/VSSOP8',{1:('CLK',signal+'_G0','IN'),2:('D',fb,'IN'),3:('Q_N',fb,'OUT'),4:('GND','GND','POWER'),5:('Q',q,'OUT'),6:('CLR_N','POR_N','IN'),7:('PRE_N','V3V3','IN'),8:('VCC','V3V3','POWER')},'https://www.ti.com/lit/ds/symlink/sn74lvc1g74.pdf','Toggle divider; independentSRCLK/RCLK activity');decouple(board,ref)
  ref='U_WD_'+signal
  chip(board,ref,'LTC6993IS6-2#TRMPBF','S6/TSOT23-6',{1:('TRIG',q,'IN'),2:('GND','GND','POWER'),3:('SET',signal+'_SET','IN'),4:('DIV','GND','IN'),5:('V+','V3V3','POWER'),6:('OUT',signal+'_ALIVE','OUT')},'https://www.analog.com/media/en/technical-documentation/data-sheets/69931234fc.pdf','Retriggerablepositiveedge; RSET100k1%; NDIV1; theoretical1.8612–2.1412us with±6%');decouple(board,ref);passive(board,'R_WD_'+signal,'100k',signal+'_SET','GND',mpn='RC0603FR-07100KL')
 gate(board,'U_WDAND','SN74LVC2G08DCUR','AND',[('SRCLK_ALIVE','RCLK_ALIVE','WD_OK'),('RAIL_CENTRAL_OK','WD_OK','ARM_CLEAR_N')]);pnet(board,'U_ARM',6,'ARM_CLEAR_N')
 #Report loss persistently while permit remains high. RC rejects the normal
 #few-ns permit-to-arm propagation difference; it never delays localcutoff.
 inverter(board,'U_PERMIT_INV','SN74LVC1G14DBVR','TX_PERMIT','PERMIT_N')
 gate(board,'U_WDOR','SN74LVC2G32DCUR','OR',[('ARM_SEEN','PERMIT_N','WD_REPORT_OK'),('GND','GND','NC')])
 passive(board,'R_FAULT_FILTER','1k','WD_REPORT_OK','WD_REPORT_RC',mpn='RC0603FR-071KL');passive(board,'C_FAULT_FILTER','1nF','WD_REPORT_RC','GND',mpn='C0603C102J5GACTU',rating='50V C0G ±5%')
 inverter(board,'U_FAULT_SCHMITT','SN74LVC1G17DBVR','WD_REPORT_RC','WD_REPORT_CLEAN')
 gate(board,'U_FAULTAND','SN74LVC2G08DCUR','AND',[('LOCAL_OK','WD_REPORT_CLEAN','FAULT_OK'),('GND','GND','NC')]);pnet(board,'U_FLT',2,'FAULT_OK')
 #No2.5V rail remains. All newlyselected fastchips use local3.3V.
 for k in ['pins','passives']:
  for x in d[k]:
   if x['board']==board:
    for f,v in list(x.items()):
     if v=='V2V5':x[f]='V3V3'
#Return buffers: OE is localground, control referenceA-domain is0(GND),
#both-rail isolation guaranteed; no powered-localcontrol enters AX-side controls.
#They become electricallyqualified for theory, not procurement certification.
for x in d['instances']:
 if x['mpn']==LVT:x['role']='B-TX two-stage3.3V regenerated signal'
 if x['mpn']=='AD7606C-16BSTZ':x['rating']='AVCC4.75–5.25V; VDRIVE=AVCC;8DOUT software0x0218; SCLK8MHz nominal;8x16bit'
 if x['mpn']=='DC-050-20':x['selection_status']='PASS';x['rating']='12VDC3A supplierdrawing; usematching2.0mm center contact; 12V2.2A designbudget'
 if x['mpn']=='CC0603JRNPO9BN3R3':x['manufacturer']='YAGEO'
 if x['mpn']=='AD7606C-16BSTZ':x['rating']='AVCC4.75–5.25V; VDRIVE=AVCC;8DOUT0x0218; SCLK8MHz; sampleperiod320/128MHz =400kSPS; read-during-nextconversion'
#LVT inputleakage and clockfanout require an explicit10k default pulldown.
for x in list(d['passives']):
 if x['value']=='100k'and x['pin2_net']=='GND'and (x['refdes'].startswith('R_DATA_RAW_PD')or x['refdes'].startswith('R_DEF_')):
  board,ref,a,b=x['board'],x['refdes'],x['pin1_net'],x['pin2_net'];remove(board,[ref]);passive(board,ref,'10k',a,b,mpn='RC0603FR-0710KL')
passive('CENTRAL','R_AXVIO_BLEED','1k','AX_VIO_REF3V3','GND',mpn='RC0603FR-071KL')
#Reverse polarity must not reach a polarized input capacitor. TVS is protected
#by the eFuse OVLO; regulated12V input remains the source contract.
for board in ['CENTRAL','UP','DN']:
 remove(board,['C_ENTRY','C_ENTRY_HF'])
 passive(board,'C_ENTRY_HF','1uF','DC12_AFTER_SWITCH','GND',mpn='C1206C105K5RACTU',package='1206',rating='50V X7R ±10%; nonpolar input hotplug capacitor')
 #TVS pin1/2 mapping preserves bidirectional symmetry.
 for x in list(d['pins']):
  if x['board']==board and x['refdes']=='D_TVS'and x['net']=='DC12_AFTER_SWITCH':pnet(board,'D_TVS',x['pin'],'V12_SW')
for ref in ['U_RET0','U_RET1']:
 for x in list(d['pins']):
  if x['board']=='CENTRAL'and x['refdes']==ref and x['function'].startswith('A')and x['net']!='NC':
   passive('CENTRAL',f'R_RETURN_PD_{ref}_{x["pin"]}','10k',x['net'],'GND',mpn='RC0603FR-0710KL')
for x in d['passives']:
 if x['mpn']=='CC0603JRNPO9BN3R3':x['manufacturer']='YAGEO'
with(R/'03_AX7020_J10_J11_PINMAP.csv').open(encoding='utf-8-sig',newline='')as f:d['fpga']=list(csv.DictReader(f))
for x in d['pins']:
 x['net_key']=('NC:'+x['board']+':'+x['refdes']+':'+x['pin'])if x['net']=='NC'else x['board']+':'+x['net']
 assert x['net']!='V2V5'
for group in ['instances','passives','pins']:
 for x in d[group]:
  for f in ['source','source_url']:
   if x.get(f)=='https://assets.nexperia.com/documents/data-sheet/BAS70_1PS70SB70_SER.pdf':x[f]='https://assets.nexperia.com/documents/data-sheet/BAS70-04.pdf'
#BOM rebuilt from instances, keeping confirmedpartsource and independentboardcounts.
groups=collections.defaultdict(list)
for x in d['instances']:groups[(x['mpn'],x['package'],x['value'])].append(x)
d['bom']=[]
for i,(k,parts)in enumerate(sorted(groups.items()),1):
 x=parts[0];c=collections.Counter(p['board']for p in parts);assert c['UP']==c['DN'],(k,c)
 d['bom'].append(dict(id=f'B{i:03d}',mpn=k[0],manufacturer=x['manufacturer'],package=k[1],value=k[2],rating=x['rating'],central_quantity=c['CENTRAL'],array_quantity=c['UP'],array_board_count=2,system_quantity=len(parts),lcsc=x['lcsc'],role=x['role'],substitution='Sameexactfunction/pin/electricaldomain; fixedUCC/595 unchanged',price='待采购映射',stock='NOT_CHECKED',procurement_status='HOLD_NOT_ORDER_RELEASED',selection_status=x['selection_status'],source_url=x['source_url'],references=';'.join(p['board']+'.'+p['refdes']for p in parts)))
def csvfile(name,rows):
 with(R/name).open('w',encoding='utf-8-sig',newline='')as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
csvfile('01_COMPLETE_BOM.csv',d['bom']);csvfile('ALL_DEVICE_PINS.csv',d['pins']);csvfile('ALL_PASSIVE_CONNECTIONS.csv',d['passives']);csvfile('ALL_INSTANCES.csv',d['instances']);csvfile('04_CENTRAL_TO_ARRAY_2x32_PINMAP.csv',d['array'])
(R/'results/FINAL_CONNECTION_DATABASE.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:len(v)for k,v in d.items()}))
