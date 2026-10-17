"""Re-express the sealed contract; write only under this additive guide directory."""
from pathlib import Path
import collections, csv, hashlib, json, re

O = Path(__file__).resolve().parents[1]
A = O.parent
def source_path(name):
 p=O/'source_inputs'/name
 return p if p.is_file() else A/name
D = json.loads(source_path('results/FINAL_CONNECTION_DATABASE.json').read_text(encoding='utf-8-sig'))
I = {(x['board'],x['refdes']):x for x in D['instances']}
P = collections.defaultdict(list)
for x in D['pins']: P[x['board'],x['refdes']].append(x)
PV = {(x['board'],x['refdes']):x for x in D['passives']}
pages = {
 'CENTRAL': {
  '00_POWER': ['J_PWR','F1','SW1','U_EF','D_TVS','U_BUCK1','U_BUCK2','U_LDO','U_5MON','U_POR'],
  '01_FPGA_HEADERS': ['J_J10','J_J11'],
  '02_TX_BUFFERS': ['U_TXB0','U_TXB1','U_TXB2','U_TXB3','U_TXCLK','U_CBUF1','U_CBUF2'],
  '03_ARRAY_HEADERS': ['J_UP','J_DN'],
  '04_ADC': ['U_ADC','U_ADCBUF','U_RET0','U_BUSYBUF'],
  '05_RX_INPUT': ['U_BLANKINV_UP','U_RXG_UP','U_RXSW_UP','U_BLANKINV_DN','U_RXG_DN','U_RXSW_DN'],
  '06_I2C_TEMP_SAFETY': ['U_I2C_MAIN','U_MUX','U_TEMP','U_G1','U_RET1'],
 },
 'ARRAY': {
  '00_POWER': ['J_PWR','F1','SW1','U_EF','D_TVS','U_BUCK1','U_BUCK2','U_BUCK3','U_LDO','U_5MON','U_POR','U_TXMON','Q_TX','Q_CUT'],
  '01_LINK_BUFFERS': ['J_LINK','U_DBUF0','U_DBUF1','U_CLK_SRCLK','U_CLK_RCLK'],
  '02_595': [f'U_SR{i:02d}' for i in range(16)],
  '03_UCC_TX': sum(([f'U_DRV{i:02d}',f'TX{2*i:02d}',f'TX{2*i+1:02d}'] for i in range(32)), []),
  '04_RX': ['U_BIAS','U_RX']+sum(([f'RX{i}',f'D_RX{i}'] for i in range(4)), []),
  '05_SAFETY_TEMP': ['U_OEINV','U_WDIV_SRCLK','U_WD_SRCLK','U_WDIV_RCLK','U_WD_RCLK','U_WDAND',
      'U_PERMIT_INV','U_WDOR','U_G1','U_G2','U_G3','U_ARM','Q_ENCLAMP0','Q_ENRELEASE0',
      'U_FAULT_SCHMITT','U_FAULTAND','U_PG','U_FLT','U_I2C','U_TEMP'],
 },
}
source_board = {'CENTRAL':'CENTRAL','ARRAY':'UP'}
rail_names = {'GND','DC12_RAW','DC12_FUSED','DC12_AFTER_SWITCH','V12_SW','V3V3','V7V15','V5A',
              'VTX_PRE','VTX','AX_VIO_REF3V3','VBIAS25'}
main_page = {(b,r):page for b,ps in pages.items() for page,refs in ps.items() for r in refs}
assert len(main_page)==sum(len(v) for ps in pages.values() for v in ps.values())

def natural(s):
 return [int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s)]

def owner_for(b,r):
 sb=source_board[b]
 if (b,r) in main_page:return r
 dec = r[2:] if r.startswith('C_U_') else None
 if dec:
  for candidate in [dec,re.sub(r'_[AB]$','',dec)]:
   if (b,candidate) in main_page:return candidate
 if r in ['R_UV_TOP','R_UV_BOT','R_OV_TOP','R_OV_BOT','R_ILM','C_DVDT','R_EF_FLT','C_EF_OUT']:return 'U_EF'
 if r=='C_ENTRY_HF':return 'SW1'
 m=re.match(r'^[CR]_B([123])_',r)
 if m:return 'U_BUCK'+m[1]
 if re.fullmatch(r'L[123]',r):return 'U_BUCK'+r[1:]
 if r.startswith(('C_LDO_','R_LDO_')) or r=='R_V5_BLEED':return 'U_LDO'
 if r.startswith(('R_5M_','C_5M_')) or r=='R_5GOOD':return 'U_5MON'
 m=re.match(r'^[RC]_U_(POR|TXMON)_',r)
 if m:return 'U_'+m[1]
 if r in ['C_U_POR','C_U_TXMON']:return r[2:]
 if b=='CENTRAL':
  if r=='R_AXVIO_BLEED':return 'J_J11'
  m=re.match(r'^[RC]_(?:RX|TX)_(UP|DN)(\d\d)$',r)
  if not m:m=re.match(r'^R_DATA_RAW_PD_(UP|DN)(\d\d)$',r)
  if m:return 'U_TXB'+str((int(m[2])+(16 if m[1]=='DN' else 0))//8)
  if r in ['R_RX_SRCLK','C_RX_SRCLK','R_RX_RCLK','C_RX_RCLK','R_DEF_MASTER_SRCLK','R_DEF_MASTER_RCLK'] or re.fullmatch(r'R_TX_(UP|DN)_(SRCLK|RCLK)',r):return 'U_TXCLK'
  m=re.match(r'^[RC]_ADC_(?:IN|BLEED)(\d)$',r)
  if m:return 'U_RXSW_'+('UP' if int(m[1])<4 else 'DN')
  if re.match(r'^C_(?:ADC_|REG\d)',r):return 'U_ADC'
  m=re.match(r'^R_RETURN_PD_(U_RET[01])_',r)
  if m:return m[1]
  if r.startswith('R_ADC_RETURN_PD_'):return 'U_RET1' if r.endswith('BUSY') else 'U_RET0'
  if r.startswith('R_ADC_'):return 'U_ADCBUF'
  if r.startswith(('R_FPGA_I2C_','R_MUX_I2C_')):return 'U_I2C_MAIN'
  if r.startswith(('R_TEMP_C_','R_UP_SC','R_UP_SD','R_DN_SC','R_DN_SD')):return 'U_MUX'
  if r.startswith(('R_PG_','R_FAULT_')):return 'U_RET1'
  if r=='R_U_TEMP_ALERT':return 'U_TEMP'
 else:
  m=re.match(r'^R_DATA_PD(\d\d)$',r)
  if m:return 'U_DBUF'+str(int(m[1])//8)
  m=re.match(r'^R_CLK_(SRCLK|RCLK)[0-3]$',r)
  if m:return 'U_CLK_'+m[1]
  if r in ['R_DEF_SRCLK','R_DEF_RCLK']:return 'U_CLK_'+r[6:]
  if r.startswith('R_DEF_'):return 'J_LINK'
  m=re.match(r'^R_TX_PD(\d\d)$',r)
  if m:return f'U_SR{int(m[1])//4:02d}'
  m=re.match(r'^C_DRV_BULK(\d\d)$',r)
  if m:return 'U_DRV'+m[1]
  m=re.match(r'^[RC]_TX(?:_AC|_BLEED)?(\d\d)$',r)
  if m:return 'TX'+m[1]
  if r in ['R_GATE_OFF','R_GATE_DRIVE','C_TX_MILLER','C_TX_LOCAL','R_TX_BLEED']:return 'Q_TX'
  if r in ['R_CUT_BASE','R_CUT_PD']:return 'Q_CUT'
  if r in ['R_ENCLAMP0','R_EN_PU0','R_EN_PD0']:return 'Q_ENCLAMP0'
  if r in ['R_ENRELEASE0','R_ENRELEASE_PD0']:return 'Q_ENRELEASE0'
  if r.startswith('C_BIAS_'):return 'U_BIAS'
  if r=='C_RX_BULK':return 'U_RX'
  m=re.match(r'^[RC]_RX_(?:IN|AC|BIAS|GAIN|FB|BLEED)(\d)$',r)
  if m:return 'RX'+m[1]
  m=re.match(r'^R_WD_(SRCLK|RCLK)$',r)
  if m:return 'U_WD_'+m[1]
  if r in ['R_FAULT_FILTER','C_FAULT_FILTER']:return 'U_FAULT_SCHMITT'
  if r.startswith('R_TEMP_'):return 'U_I2C'
  if r=='R_U_TEMP_ALERT':return 'U_TEMP'
 #Find an actual connected active device; no guess based on voltage rail alone.
 candidates=[]
 for pin in P[sb,r]:
  if pin['net'] in rail_names or pin['net']=='NC':continue
  for (bb,ref),pins in P.items():
   if bb==sb and (b,ref) in main_page and any(q['net']==pin['net'] for q in pins):
    candidates.append(ref)
 if candidates:return sorted(set(candidates),key=lambda x:(not x.startswith('U_'),natural(x)))[0]
 raise ValueError(f'No explicit page/placement owner: {b}.{r}')

plans=[]
for b,ps in pages.items():
 sb=source_board[b]; owners={}
 for (bb,r) in I:
  if bb==sb:
   owner=owner_for(b,r)
   assert (b,owner) in main_page,(b,r,owner)
   owners[r]=owner
 for page,roots in ps.items():
  order=[]
  for root in roots:
   children=sorted([r for r,o in owners.items() if o==root and r!=root],key=natural)
   # Put local supply bypass first, then the remaining explicitly connected parts.
   children.sort(key=lambda r:(not r.startswith('C_U_'),natural(r)))
   if b=='ARRAY' and page=='03_UCC_TX' and re.fullmatch(r'TX\d\d',root):
    number=root[2:];before=['R_TX'+number,'C_TX_AC'+number]
    assert all(x in children for x in before),(root,children)
    order.extend(before);order.append(root);order.extend(x for x in children if x not in before)
   else:
    order.append(root);order.extend(children)
  for n,r in enumerate(order,1):
   plans.append({'board':b,'source_board':sb,'page':page,'step':n,'refdes':r,'owner':owners[r]})
assert len(plans)==982 and len({(x['board'],x['refdes']) for x in plans})==982
plan={(x['board'],x['refdes']):x for x in plans}

def esc(x):return str(x).replace('|','&#124;').replace('\n',' ')
def table(rows):
 return '\n'.join('| '+' | '.join(esc(x) for x in row)+' |' for row in rows)+'\n'
def anchor(b,r):return (b+'-'+r).lower().replace('_','-')
def endpoint(b,q):
 page=plan[b,q['refdes']]['page']
 return f"{page}/{q['refdes']}.{q['pin']}（{q['function']}）"

nets=collections.defaultdict(list)
for b,sb in source_board.items():
 for pin in D['pins']:
  if pin['board']==sb and pin['net']!='NC':nets[b,pin['net']].append(pin)
netids={key:f'N{i:04d}' for i,key in enumerate(sorted(nets),1)}

rail_source={
 'GND':'本板连续公共地；不要串磁珠分割数字/模拟/驱动回流',
 'DC12_RAW':'本板J_PWR.1输入正极，仅到本板保险丝输入',
 'DC12_FUSED':'本板F1.2保险丝后，到SW1.3',
 'DC12_AFTER_SWITCH':'本板SW1.2公共端输出，到eFuse输入',
 'V12_SW':'本板U_EF.6保护输出，给本板各降压输入',
 'V3V3':'本板U_BUCK1经L1输出的3.3V数字电源',
 'V7V15':'本板U_BUCK2经L2输出的约7.15V电源，给LDO输入',
 'V5A':'本板U_LDO.1输出的约5.084V模拟电源',
 'VTX_PRE':'本板U_BUCK3经L3输出的约10V，位于Q_TX之前',
 'VTX':'本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动',
 'AX_VIO_REF3V3':'CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA',
 'VBIAS25':'本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联',
}
fpga={(x['connector'],str(x['pin'])):x for x in D['fpga']}
array={str(x['pin']):x for x in D['array']}

def mate_text(b,r,pin):
 if b=='CENTRAL' and r in ['J_J10','J_J11']:
  row=fpga[r[2:],pin]
  return f"外部排线1对1接AX7020 {r[2:]}.{pin}；AX功能={row['manual_signal']}，球位={row['ball']}"
 if b=='CENTRAL' and r in ['J_UP','J_DN']:
  row=array[pin]
  return f"外部排线1对1接{'UP' if r=='J_UP' else 'DN'}阵列J_LINK.{pin}（该板网名{row['array_net']}）"
 if b=='ARRAY' and r=='J_LINK':
  row=array[pin]
  return f"装成上板时接CENTRAL.J_UP.{pin}（{row['central_up']}）；装成下板时接CENTRAL.J_DN.{pin}（{row['central_dn']}）"
 return ''

def connect_text(b,r,p):
 n=p['net'];mate=mate_text(b,r,p['pin'])
 if n=='NC':return '此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。'+('接口触点即使随1对1排线存在，也不从此脚取电或补接其他电路。 '+mate if mate else '')
 nid=netids[b,n];link=f'[完整端点{nid}](#net-{nid.lower()})'
 peers=[q for q in nets[b,n] if (q['refdes'],q['pin'])!=(r,p['pin'])]
 if n=='GND':action='直接接本板GND符号；所有本板GND同网。'
 elif n in rail_source:action=f'接本板`{n}`电源/参考标签；来源：{rail_source[n]}。'
 else:action=f'从此脚引线，标注精确网名`{n}`；跨页使用同名板内标签。'
 if len(peers)<=8:
  action+='同网还接：'+('；'.join(endpoint(b,q) for q in peers) if peers else '无其他板内端点，保留本表所示单端网络，不补接地或电源')+'。'
 else:
  action+=f'同网另有{len(peers)}个物理端点，逐个见{link}；例如'+ '；'.join(endpoint(b,q) for q in peers[:3])+'。'
 if len(peers)<=8:action+=f' {link}。'
 return action+(' '+mate if mate else '')

special={
 'J_PWR':'本页最左侧放DC入口。两处同编号1焊盘均属于同一CENTER正极；2接GND，3独立NC。匹配2.0mm中心针插头，中心正。',
 'SW1':'放在保险丝之后。物理2是公共端，3是ON端，1为OFF端NC；图形旋转不改变物理脚号。开关状态由2与3接通定义。',
 'U_EF':'放在开关右侧。按精确TPS259470L变体连接限流、欠压、过压和DVDT；AUXOFF/ITIMER按原表NC。它的供电启动与TX_PERMIT是不同功能。',
 'U_LDO':'放在7.15V与V5A之间；EP接本板GND。反馈电阻一端接OUT、另一端接FB，不能把反馈全部接地。',
 'Q_TX':'00_POWER右侧放TX高侧MOS。S=1/2/3接VTX_PRE，D=5/6/7/8接VTX，G=4接TX_GATE。C_TX_MILLER必须G到D，不是G到S。',
 'Q_CUT':'紧邻Q_TX放门极控制NPN；B1/E2/C3按表。其控制来自05_SAFETY_TEMP的EN_PERMIT，跨页用精确网名。',
 'Q_ENCLAMP0':'本地UCC使能默认夹低晶体管，放在05_SAFETY_TEMP许可链右侧。DRIVER_EN_G0同时连接32颗UCC的64个EN脚，完整端点必须全接。',
 'Q_ENRELEASE0':'紧邻Q_ENCLAMP0，只有EN_PERMIT合格才解除夹低；不要将内部上拉或100k电阻当作主动关断。',
 'U_ADC':'04_ADC中部放64脚ADC。AVCC/VDRIVE用V5A；所有AGND/REFGND接本地连续GND。REGCAP、REFIN/REFOUT、REFCAP电容按各自网络，不能混接。',
 'U_ADCBUF':'放在ADC控制输入左侧；AHCT供电使用V5A，将3.3V控制送入ADC。不要把输出端直接回接AX引脚。',
 'U_RET0':'放在ADC八路输出与FPGA接口之间；VCCA使用AX_VIO_REF3V3，VCCB使用V5A，DIR与OE_N按表。未用输入和输出也逐脚处理。',
 'U_RET1':'放在中央健康/故障返回信号旁；VCCA使用AX_VIO_REF3V3，VCCB使用本地V3V3。ADC_BUSY也经过本芯片返回AX。',
 'U_BUSYBUF':'放在ADC BUSY与返回翻译器之间，V5A侧输入、本地3.3V输出网络按表。',
 'U_BIAS':'在ARRAY/04_RX左侧放REF3025，给本阵列产生VBIAS25；输入/输出各自退耦，不能跨阵列并联偏置源。',
 'U_RX':'在ARRAY/04_RX中部放四运放；四路IN+/IN−/OUT逐脚对应四个RX通道。反馈电阻跨OUT与IN−，不是串到GND；V+接V5A，V−接GND。',
 'U_TEMP':'放在本页I2C支路末端；三个板上的TMP117均为0x48，ADD0接GND；EP接GND。ALERT及其上拉按原表保留。',
 'U_MUX':'放在中央I2C主侧与三支路之间；TCA9548A为0x70，通道0中央、1上阵列、2下阵列。一次只选一路。',
 'U_I2C_MAIN':'放在AX侧I2C与中央MUX之间，A侧供电AX_VIO_REF3V3、B侧本地V3V3；分域退耦及上拉不混接。',
 'U_I2C':'放在ARRAY排线I2C与本地传感器之间；A侧是排线侧、B侧是本地侧，禁止B侧直接连另一TCA9517的B侧。',
}

def component_note(b,r):
 if r in special:return special[r]
 if r.startswith('U_BUCK'):
  return '本页对应电压区左放芯片，中间SW→电感，右放输出电容和负载标签；BOOT电容跨BOOT/SW，前馈220pF跨反馈上臂。5脚EN按原表独立NC，不因通用接线习惯擅自补接电源。'
 if r.startswith(('U_TXB','U_TXCLK','U_DBUF','U_CLK_')):
  return '按信号从接口到输出的顺序摆放LVT缓冲，供电本地V3V3、地GND；PW20无EP。每个通道A/Y和两个OE_N按实际脚号，未用输入接表定网络、未用输出独立NC。'
 if r.startswith('U_SR'):
  return '在四组595中的对应组摆放，时钟只接本组SRCLK_G/RCLK_G。SER14接本lane数据；QA15/QB1/QC2/QD3使用，QE4/QF5/QG6/QH7/QH′9独立NC。'
 if r.startswith('U_DRV'):
  return '放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。'
 if re.fullmatch(r'TX\d\d',r):return '放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。'
 if re.fullmatch(r'RX[0-3]',r):return '放在对应接收通道最左侧；两脚按表，后接输入限流、交流耦合、偏置和运放；不要与发射驱动输出网络连接。'
 if re.fullmatch(r'D_RX[0-3]',r):return '放在对应RX输入钳位节点旁。BAS70-04为双二极管：1脚A1接GND，2脚K2接V5A，3脚K1/A2接本通道钳位节点；不能按两脚TVS接法处理。'
 if r.startswith('U_WD_'):return '放在对应时钟二分频器右侧；LTC6993IS6-2的1TRIG/2GND/3SET/4DIV/5V+/6OUT逐脚照表，RSET=100k，DIV接GND。'
 if r.startswith('U_WDIV_'):return '放在对应SRCLK/RCLK监测线上；74LVC1G74的D与反相输出构成二分频，PRE/CLR按表，不能用HB取代两路时钟监测。'
 return '按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。'

page_intro={
 ('CENTRAL','00_POWER'):'从左到右：J_PWR→F1→SW1→U_EF→V12_SW。下方分出3.3V与7.15V降压，再由7.15V经LDO得到V5A；监测输出送安全页。这里仅给中央板供电。',
 ('CENTRAL','01_FPGA_HEADERS'):'左上放J_J10，左下放J_J11，均2.54mm 2×20排母。按物理脚号放标签；J11.39仅作AX接口参考，其他原定NC电源脚不连接。',
 ('CENTRAL','02_TX_BUFFERS'):'左侧放DATA输入串阻/滤波，中央放4颗数据LVT和1颗时钟LVT，右侧放UP/DN输出串阻。控制信号使用原LVC缓冲。原AX7020板载33Ω不再新增进本板BOM。',
 ('CENTRAL','03_ARRAY_HEADERS'):'上方放J_UP，下方放J_DN，均2.54mm 2×32排母。左侧接本板缓冲/采集网，右侧标出对应阵列J_LINK的同号针；所有偶数针为GND。',
 ('CENTRAL','04_ADC'):'中央放ADC，左侧放控制AHCT，右侧放DOUT返回翻译器。ADC参考电容就近围绕相应脚，不能把REFCAP当2.5V偏置。',
 ('CENTRAL','05_RX_INPUT'):'按UP四路在上、DN四路在下摆放掉电隔离开关、空白控制和499Ω/1nF ADC输入RC。每路终点是对应ADC正输入；负输入接GND。',
 ('CENTRAL','06_I2C_TEMP_SAFETY'):'从左到右：AX I2C域转换→MUX→三条温度支路。下方放本板健康逻辑和返回AX的故障/PG翻译器。电源监测器本体在00_POWER。',
 ('ARRAY','00_POWER'):'入口同样J_PWR→F1→SW1→U_EF。分出3.3V、7.15V与10V；7.15V→LDO→V5A。10V为VTX_PRE，经Q_TX才成为VTX；安全许可来自05页，电源地均为本板GND。',
 ('ARRAY','01_LINK_BUFFERS'):'左侧放2×32 J_LINK，中央放两颗DATA LVT，下方放SRCLK/RCLK各一颗LVT；每个时钟分四个独立15Ω支路，不能将四组输出互并。',
 ('ARRAY','02_595'):'依次放U_SR00–15，按00–03、04–07、08–11、12–15分四组。每组SRCLK_Gn/RCLK_Gn只驱动四颗595；QA–QD各自对应唯一TXLOG。',
 ('ARRAY','03_UCC_TX'):'按U_DRV00→TX00/TX01，U_DRV01→TX02/TX03，直至U_DRV31→TX62/TX63排列。驱动后依次串150Ω、100nF、换能器；泄放并到换能器两端。',
 ('ARRAY','04_RX'):'先生成本板VBIAS25，再放四运放及RX0–3四路。每路从接收器进入限流/隔直/钳位/偏置/反馈网络，输出到J_LINK对应RX针。',
 ('ARRAY','05_SAFETY_TEMP'):'先放两路时钟二分频与独立单稳，再放许可/ARM逻辑和默认EN夹低晶体管，最后放故障上报和I2C温度。故障RC只滤报告，不串进本地EN关断。',
}

lines=['# SonoField-FPGA v5｜按板卡、图页、放置顺序的逐引脚连接指南\n',
 '2026-10-17。本文只转换2026-10-16终版02指南的表述。原器件型号、数量、物理脚、网络、接口、无源值及工程限制不变；新增加的是图页归属、纸面摆放顺序和同网器件定位。原指南保持原样。\n',
 '工程状态沿用原FINAL_REVIEW与10_DRAW_READY_ACCEPTANCE：理论候选ACCEPT WITH LIMITATIONS、独立Review待完成。本轮核对PASS只表示新旧指南一致，不新增实物验证、ERC或制造放行。\n',
 '## 先明确画在哪块板\n',
 '`CENTRAL`是中央板工程，画1套。`ARRAY`是通用阵列板工程，画1套、制作实例为UP和DN；已核对两者全部629个器件/1964个物理脚完全一致。CENTRAL有353个器件/1277脚。画图阶段不能把两块ARRAY的本地电源互并。本文不执行任何绘图操作。\n',
 '在嘉立创EDA专业版分别建立原指南指定的`SonoField_v5_CENTRAL_20261016`和`SonoField_v5_ARRAY_20261016`工程，再按目录建7页/6页。下文的“摆放”仅指原理图纸面位置，不是PCB布局。元件库按精确MPN及封装选择，逐个设置位号、值和物理脚号；立创号待映射与原资格HOLD保持不变。\n',
 '每一步先放该器件，按表把全部电源/GND和其他引脚接完，再做下一步。已放器件直接拉线；尚未放或在另一页的器件，先放精确同名板内标签，再到该器件步骤连接。接线对象写成`图页/位号.物理脚（功能）`。不同网络之间必须通过表中器件连接，不能将串阻、隔直电容、滤波节点两侧短接。\n',
 '`GND`在同一块板内是一个连续公共参考；每个GND脚都接本板GND符号。`V3V3`、`V5A`、`VTX_PRE`、`VTX`等必须用各自精确标签；同名网不跨两个独立工程自动合并。`NC`不是网络名：每个NC脚单独放不连接标记，互不连线。EP仅按本表已有的EP行接入，UCC SOIC8和LVT PW20不得添加虚构EP。原表IN/OUT/POWER/PASSIVE等是核对输入，不得为消ERC提示把所有库脚改成无源。\n',
 '表中电源/GND与高扇出网不重复抄写数百个端点；链接的“完整端点Nxxxx”逐个列出所有相连器件脚，未删减任何连接。页末核对与最终检查均从最终Markdown重新解析后执行，详见14_GUIDE_CONSISTENCY_REPORT.md。\n',
 '## 图页与执行顺序\n']
toc=[['板卡','图页','器件数','本页先做什么'],['---']*4]
for b,ps in pages.items():
 for page in ps:
  count=sum(x['board']==b and x['page']==page for x in plans)
  toc.append([b,f'[{page}](#page-{b.lower()}-{page.lower().replace("_","-")})',count,page_intro[b,page]])
lines.append(table(toc))

for b,ps in pages.items():
 for page in ps:
  lines += [f'<a id="page-{b.lower()}-{page.lower().replace("_","-")}"></a>\n',f'## {b}板／{page}图页\n',page_intro[b,page]+'\n']
  parts=[x for x in plans if x['board']==b and x['page']==page]
  for item in parts:
   r=item['refdes'];sb=item['source_board'];inst=I[sb,r];passive=PV.get((sb,r))
   lines += [f'<a id="{anchor(b,r)}"></a>\n',f'### 第{item["step"]:03d}步：在{b}／{page}放置 {r}\n',
       f'在 **{b}板的{page}图页**，'+('先' if item['step']==1 else '接着')+f'放置 **{r}**，精确型号 **{inst["mpn"]}**，封装 **{inst["package"]}**。'+
       (f'其值为 **{inst["value"]}**。' if passive else '')+'\n']
   if passive:
    owner=item['owner'];where='本页输入/输出位置' if owner==r else f'紧邻本页{owner}的相应引脚区域'
    if b=='ARRAY':
     m=re.fullmatch(r'R_TX(\d\d)',r)
     if m:where=f'本通道U_DRV{int(m[1])//2:02d}输出与C_TX_AC{m[1]}之间'
     m=re.fullmatch(r'C_TX_AC(\d\d)',r)
     if m:where=f'R_TX{m[1]}之后、TX{m[1]}之前，作为串联隔直元件'
     m=re.fullmatch(r'R_TX_BLEED(\d\d)',r)
     if m:where=f'跨TX{m[1]}.1与TX{m[1]}.2的并联位置'
    polarity=passive['polarity'];pol='有极性：物理1为正端、2为负端，不能对调。' if 'positive' in polarity else '无极性/双向；本文仍固定物理1/2，便于逐脚核对。'
    lines += [f'纸面位置：{where}。额定条件：{passive["rating"]}。{pol}\n']
    if r.startswith('C_') and passive['pin2_net']!='GND':
     lines += ['此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。\n']
   else:
    lines += [component_note(b,r)+'\n']
   rows=[['板卡','图页','位号','型号','物理脚','功能','网络','原表类型','具体接法／同网器件'],['---']*9]
   for pin in sorted(P[sb,r],key=lambda q:natural(q['pin'])):
    rows.append([b,page,r,inst['mpn'],pin['pin'],pin['function'],pin['net'],pin['kind'],connect_text(b,r,pin)])
   lines.append(table(rows))
   if passive:
    lines += [f'接完确认：{r}.1=`{passive["pin1_net"]}`，{r}.2=`{passive["pin2_net"]}`；不可旁路该器件把两个网名短在一起。\n']
   else:
    pp=P[sb,r];sup=[f'{r}.{q["pin"]}→{q["net"]}' for q in pp if q['net'] in rail_names]
    nc=[q['pin'] for q in pp if q['net']=='NC']
    lines += ['接完确认：'+('电源/地/参考为'+'；'.join(sup)+'。' if sup else '本器件没有另列的电源引脚，仍须按上表连接所有信号/无源端。')+
        (' NC脚'+','.join(nc)+'逐个单独标记。' if nc else '')+'\n']
  lines += [f'本页完成核对：**{len(parts)}个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。\n']

lines += ['## 两套FPGA接口：逐针接到AX7020的哪里\n',
 '下表是CENTRAL.J_J10/J_J11到AX自带J10/J11的1对1物理连接，连接器均按原指南配合面物理编号，不能按符号屏幕左右猜针号。\n']
rows=[['中央排母','物理脚','AX连接器/物理脚','AX原功能','FPGA球位','板内网络','RTL端口'],['---']*7]
for x in D['fpga']:
 rows.append(['J_'+x['connector'],x['pin'],x['connector']+'.'+str(x['pin']),x['manual_signal'],x['ball'],x['net'],x['rtl_port']])
lines.append(table(rows))
lines += ['## 两套阵列接口：中央上板/下板与通用ARRAY的同号针\n',
 '两条64芯排线均1对1。通用ARRAY.J_LINK只使用本地网名；装成UP时接J_UP，装成DN时接J_DN。所有偶数针都是GND，63独立NC，不输送12V或TX功率。\n']
rows=[['物理脚','CENTRAL上接口','上接口板内网','CENTRAL下接口','下接口板内网','ARRAY接口','ARRAY本地网','方向','安全默认'],['---']*9]
for x in D['array']:
 p=str(x['pin']);rows.append([p,'J_UP.'+p,x['central_up'],'J_DN.'+p,x['central_dn'],'J_LINK.'+p,x['array_net'],x['direction'],x['safe_default']])
lines.append(table(rows))

lines += ['## 全部网络的完整端点索引\n',
 '本节逐网列出全部同网物理脚，包含电源、GND及高扇出。仅同一板卡同一网名才属于同网；表里没有的端点不能自行补接。同一器件两个不同脚也必须分别连接。NC不形成公共网络，因此不进入本节。\n']
for (b,n),pins in sorted(nets.items()):
 nid=netids[b,n]
 lines += [f'<a id="net-{nid.lower()}"></a>\n',f'### {nid}｜{b}／{n}\n']
 rows=[['板卡','图页','位号','物理脚','功能','网络'],['---']*6]
 for pin in sorted(pins,key=lambda q:(plan[b,q['refdes']]['page'],natural(q['refdes']),natural(q['pin']))):
  rows.append([b,plan[b,pin['refdes']]['page'],pin['refdes'],pin['pin'],pin['function'],n])
 lines.append(table(rows))

original=source_path('02_JLCEDA_PRO_COMPLETE_SCHEMATIC_GUIDE.md').read_text(encoding='utf-8-sig')
technical=original.split('## 1. 冻结架构与唯一选型',1)[1].split('## 8. 全部物理针与无源连接附录',1)[0]
technical='## 1. 冻结架构与唯一选型'+technical
lines += ['## 原指南技术条件保留正文\n',
 '下面保留原指南第1–7节正文，作为本轮表述转换的约束，避免遗漏电气、时序、安装和后续验证条件。标题仅增加一级，正文不改写，文件末尾空行统一；这些绘图操作是供用户日后执行的说明，不表示本轮已执行。\n',
 re.sub(r'^(#{1,5}) ',r'\1# ',technical,flags=re.M)]

out='\n'.join(lines).rstrip('\n')+'\n'
with (O/'13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md').open('w',encoding='utf-8',newline='\n') as f:f.write(out)
#Readable per-page copies: identical instructions, links back to the full net index.
(O/'pages').mkdir(exist_ok=True)
page_keys=[(b,p) for b,ps in pages.items() for p in ps]
index=['# 按板卡、图页逐步连接指南入口\n',
 '本目录是原02指南的追加表述转换包，原文件与电路不改。完整指南包含全部步骤、接口和完整同网端点；下方13份分册便于一页一页照着连接，内容来自同一份已核对全文。\n',
 '- [完整步骤指南](13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)\n- [独立一致性报告](14_GUIDE_CONSISTENCY_REPORT.md)\n- [机器可读核对结果](results/CONSISTENCY.json)\n',
 '| 板卡 | 图页分册 |\n| --- | --- |']
for k,(b,p) in enumerate(page_keys):
 marker=f'<a id="page-{b.lower()}-{p.lower().replace("_","-")}"></a>'
 start=out.index(marker)
 if k+1<len(page_keys):
  nb,np=page_keys[k+1];end=out.index(f'<a id="page-{nb.lower()}-{np.lower().replace("_","-")}"></a>')
 else:end=out.index('## 两套FPGA接口：逐针接到AX7020的哪里')
 body=out[start:end].replace('](#net-','](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-')
 pre=f'# {b}／{p}逐步连接分册\n\n本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。\n\n'
 name=f'{b}_{p}.md'
 with (O/'pages'/name).open('w',encoding='utf-8',newline='\n') as f:f.write((pre+body).rstrip('\n')+'\n')
 index.append(f'| {b} | [{p}](pages/{name}) |')
index += ['\n先完成CENTRAL的00_POWER→01_FPGA_HEADERS→02_TX_BUFFERS→03_ARRAY_HEADERS→04_ADC→05_RX_INPUT→06_I2C_TEMP_SAFETY；再完成ARRAY的00_POWER→01_LINK_BUFFERS→02_595→03_UCC_TX→04_RX→05_SAFETY_TEMP。ARRAY仅画一套，UP/DN分别实例化，电源不互并。\n',
 '复核命令：PowerShell7执行`./CHECK_GUIDE.ps1`；可用`-Python`指定任意可用Python3.10+解释器。检查器只用标准库，不安装工具，不执行EDA操作。实际命令、输出与错误注入结果保存在logs和results。\n']
with (O/'README.md').open('w',encoding='utf-8',newline='\n') as f:f.write('\n'.join(index))
inputs=['02_JLCEDA_PRO_COMPLETE_SCHEMATIC_GUIDE.md','ALL_INSTANCES.csv','ALL_DEVICE_PINS.csv',
 'ALL_PASSIVE_CONNECTIONS.csv','01_COMPLETE_BOM.csv','03_AX7020_J10_J11_PINMAP.csv',
 '04_CENTRAL_TO_ARRAY_2x32_PINMAP.csv','results/FINAL_CONNECTION_DATABASE.json']
hashes={n:hashlib.sha256(source_path(n).read_bytes()).hexdigest() for n in inputs}
for name,obj in [('STEP_COMPONENT_MANIFEST.json',plans),('GUIDE_INPUT_HASHES.json',hashes)]:
 with (O/'results'/name).open('w',encoding='utf-8',newline='\n') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'status':'GENERATED_NOT_YET_INDEPENDENTLY_CHECKED','template_devices':len(plans),
 'template_pins':sum(len(P[source_board[x['board']],x['refdes']]) for x in plans),
 'template_networks':len(nets),'pages':sum(len(x)for x in pages.values()),'lines':len(out.splitlines()),
 'bytes':(O/'13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md').stat().st_size}))
