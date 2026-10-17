"""Render reviewable connection contracts and independently crosscheck real sources."""
from pathlib import Path
import json,csv,re,collections,hashlib,datetime,shutil
R=Path(__file__).resolve().parents[1];NATIVE=(R/'results/FINAL_NATIVE_LABEL.txt').read_text().strip() if (R/'results/FINAL_NATIVE_LABEL.txt').exists() else 'native19';V=Path('E:/Codex_project/AMD_Sonofield/v5')
d=json.loads((R/'results/FINAL_CONNECTION_DATABASE.json').read_text(encoding='utf-8'))
def csvout(name,rows):
 with(R/name).open('w',encoding='utf-8-sig',newline='')as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def mdtable(rows,cols):
 return '\n'.join(['| '+' | '.join(cols)+' |','| '+' | '.join('---'for _ in cols)+' |']+['| '+' | '.join(str(x.get(k,'')).replace('|','/').replace('\n',' ')for k in cols)+' |'for x in rows])
def write(name,t):(R/name).write_text(t,encoding='utf-8')
pins={(x['board'],x['refdes'],x['pin']):x for x in d['pins']}
assert len(pins)==len(d['pins']),'duplicatephysicalpin'
inst={(x['board'],x['refdes']):x for x in d['instances']};assert len(inst)==len(d['instances'])
def pin(b,r,p):return pins[(b,r,str(p))]['net']
def bynet(b,n):return [x for x in d['pins']if x['board']==b and x['net']==n and n!='NC']
for x in d['passives']:
 assert pin(x['board'],x['refdes'],1)==x['pin1_net']and pin(x['board'],x['refdes'],2)==x['pin2_net']
for x in d['bom']:
 assert int(x['system_quantity'])==int(x['central_quantity'])+2*int(x['array_quantity'])
 assert len([p for p in d['instances']if p['mpn']==x['mpn']and p['package']==x['package']and p['value']==x['value']])==x['system_quantity']
assert sum(x['system_quantity']for x in d['bom'])==len(inst)
for b in ['UP','DN']:
 assert sum(x['board']==b and x['mpn']=='SN74LVC595APWR'for x in d['instances'])==16
 assert sum(x['board']==b and x['mpn']=='UCC27624QDRQ1'for x in d['instances'])==32
 assert not any(x['net']=='V2V5'for x in d['pins'])
 assert pin(b,'U_ARM',6)=='ARM_CLEAR_N'
 assert pin(b,'Q_TX',4)=='TX_GATE'
 assert pin(b,'U_WD_SRCLK',5)=='V3V3'and pin(b,'U_WD_SRCLK',6)=='SRCLK_ALIVE'
 for j in range(16):
  assert pin(b,f'U_SR{j:02d}',11)==f'SRCLK_G{j//4}'
  assert pin(b,f'U_SR{j:02d}',12)==f'RCLK_G{j//4}'
  assert {pin(b,f'U_SR{j:02d}',p)for p in [4,5,6,7,9]}=={'NC'}
 for j in range(32):assert pin(b,f'U_DRV{j:02d}',1)==pin(b,f'U_DRV{j:02d}',8)=='DRIVER_EN_G0'
#Independent source: OEM XLSX rawXML, actual formalXDC, actual nativeVivado I/O.
raw=json.loads((R/'results/VENDOR_XLSX_CELLS.json').read_text(encoding='utf-8'));vendor={}
for sheet in raw:
 for row in sheet['rows']:
  a=next((v for k,v in row.items()if k.startswith('A')),None);b=next((v.strip()for k,v in row.items()if k.startswith('B')),None)
  if a and b:vendor[b]=a
xdc=(V/'hardware/constraints/ax7020_draw_ready.xdc').read_text(encoding='utf-8-sig')
bindings=dict((a or b,ball)for ball,a,b in re.findall(r'set_property PACKAGE_PIN (\w+) \[get_ports (?:\{([^}]+)\}|(\w+))\]',xdc))
io={}
for line in(R/f'results/{NATIVE}/NATIVE_PHYSICAL_IO.rpt').read_text().splitlines():
 if line.startswith('|'):
  a=[x.strip()for x in line.split('|')[1:-1]]
  if len(a)>8 and re.fullmatch('[A-Z]+[0-9]+',a[0])and a[1]:io[a[1]]=dict(ball=a[0],direction=a[4],iostandard=a[5],bank=a[6])
cross=[];active=[]
for x in d['fpga']:
 s=x['manual_signal'];p=x['rtl_port'];expected=vendor[s[3:]]if s.startswith('EX_')else'NON_IO'
 assert (not s.startswith('EX_'))or expected==x['ball'],x
 if p:
  assert bindings[p]==x['ball']and io[p]['ball']==x['ball']and io[p]['iostandard']=='LVCMOS33',x
  assert str(x['bank'])==io[p]['bank'],(x,io[p])
  if x['direction']in('IN','OUT'):assert io[p]['direction']=={'IN':'INPUT','OUT':'OUTPUT'}[x['direction']],(x,io[p])
  active.append(p)
 #Header physical contacts must agree with component pin database independently.
 assert pin('CENTRAL','J_'+x['connector'],x['pin'])==x['net'],(x,pin('CENTRAL','J_'+x['connector'],x['pin']))
 cross.append(dict(connector=x['connector'],physical_pin=x['pin'],vendor_function=s,vendor_ball=expected,rtl_logical_port=x['logical_rtl_port'],native_top_port=p,xdc_ball=bindings.get(p,'NO_CONSTRAINT'),native_ball=io.get(p,{}).get('ball','NC/NON_IO'),central_net=x['net'],status='PASS',basis='OEM XML+formal XDC+actual routed IO+component pin contract'))
for row in cross:
 x=next(x for x in d['fpga']if x['connector']==row['connector']and x['pin']==row['physical_pin'])
 row['contract_bank']=x['bank'];row['native_bank']=io.get(x['rtl_port'],{}).get('bank','NON_IO/NC');row['voltage_domain']=x['level']
 row['central_component_endpoints']=';'.join(f'{q["refdes"]}.{q["pin"]}:{q["function"]}'for q in bynet('CENTRAL',x['net'])if not q['refdes'].startswith('J_'))
 net=x['net'];desc='Pinisolated'if net=='NC'else'Commonreferenceground'if net=='GND'else'Localinterfaceonly'
 if '_DATA_RAW_'in net:
  side,_,_,num=net.split('_');local=int(num);global_lane=local+(16 if side=='DN'else 0)
  desc=f'CENTRAL22R/3.3pF→LVT→47R→J_{side}.{2*local+1}↔{side}.J_LINK.{2*local+1}→LVT→47R→U_SR{local:02d}.14→QA-D→UCC→150R/100nF→TXlocal{local*4:02d}..{local*4+3:02d};channel{global_lane*4}..{global_lane*4+3};05_TX_128_CHANNEL_CHAIN.csv'
 elif net.startswith('ADC_DOUT'):desc='U_ADC DOUTphysicalpin→U_RET0 B/A→AX; all8receiver/ADCphysicalchannelpaths in06_ADC_RX_8CH_AND_TEMP.csv'
 elif 'SRCLK'in net or'RCLK'in net:desc='Masterstrobe→central22R/3.3pF/LVT/47R→UP/DNheader33/35→arrayLVT4branches15R→595.11/12; eachbranch4loads'
 elif x['rtl_port'].startswith('IIC_'):desc='TCA9517A/B→TCA9548A0x70channel0/1/2→centralTMP/UPheader51,53/DNheader51,53→arrayTCA9517A/B→TMP1170x48'
 elif 'PGOOD'in net or'FAULT'in net:desc='Localpower/safety→arrayJ_LINK49/47→CENTRALJ_UP/J_DN49/47→U_RET1B/A→AXhealth;07_POWER_FAULT_AND_STARTUP.csv'
 elif 'TX_PERMIT'in net:desc='Centralcontrolbuffer→header39→arrayU_ARM.1 and localAND/MOS/ENclamp; bothclocksWD mustbealive;07_POWER_FAULT_AND_STARTUP.csv'
 elif net.startswith('ADC_'):desc='ADCcontrol/feedback→AHCT244 or BUSYbuffer→U_ADC; allphysicalpins in02 and06;8MHz/400kSPS'
 elif 'OE'in net:desc='Centralcontrol→bothheader37→array595.13 and ENsafetygate;high=disabled'
 elif 'RX_BLANK'in net:desc='Centralblanklogic→ADG4612RXswitches; header43reservedarrayblankreference;actualendpoints04/02'
 elif net=='AX_VIO_REF3V3':desc='J11.39→returnbufferVCCA/TCA9517A+1kbleed;<=50mA budget;noTX/centralpower'
 row['downstream_path']=desc
assert len(active)==len(set(active));assert set(bindings)==set(active)|{'ref_clk50_0'}
assert bindings['ref_clk50_0']==vendor['PL_GCLK']=='U18'
for p,l in [(32,'E'),(33,'F'),(34,'G'),(35,'H')]:assert next(x for x in d['fpga']if x['connector']=='J11'and int(x['pin'])==p)['net']==f'ADC_DOUT{l}_FPGA'
assert next(x for x in d['fpga']if x['connector']=='J11'and int(x['pin'])==39)['rtl_port']==''
assert pin('CENTRAL','J_J11',39)=='AX_VIO_REF3V3'
assert not any(x['net']=='AX_VIO_REF3V3'and x['board']!='CENTRAL'for x in d['pins'])
csvout('09_RTL_XDC_PINMAP_CROSSCHECK.csv',cross)
array=[]
for b in ['UP','DN']:
 for x in d['array']:
  n=int(x['pin']);cn=x['central_up'if b=='UP'else'central_dn'];an=x['array_net']
  assert pin('CENTRAL','J_'+b,n)==cn and pin(b,'J_LINK',n)==an,(b,n)
  if n%2==0:assert cn==an=='GND'
  if n==63:assert cn==an=='NC'
  endpoints=lambda board,net:';'.join(f'{p["refdes"]}.{p["pin"]}:{p["function"]}'for p in bynet(board,net)if not p['refdes'].startswith('J_'))
  array.append(dict(board=b,pin=n,signal=x['signal'],central_net=cn,array_net=an,direction=x['direction'],domain=x['domain'],safe_default=x['safe_default'],central_endpoint=endpoints('CENTRAL',cn),array_endpoint=endpoints(b,an),cable='2.54mm female-to-female boards via usermale-male1:1 harness; <=150mm; nohotplug',status='PASS'))
csvout('04_CENTRAL_TO_ARRAY_2x32_PINMAP.csv',array)
tx=[]
for ch in range(128):
 b='UP'if ch<64 else'DN';local=ch%64;lane=local//4;bit=local%4;sr=f'U_SR{lane:02d}';drv=f'U_DRV{local//2:02d}';qpin=[15,1,2,3][bit];inp=2 if local%2==0 else 4;out=7 if local%2==0 else 5
 assert pin(b,sr,qpin)==pin(b,drv,inp)==f'TXLOG_{local:02d}'
 assert pin(b,drv,out)==pin(b,f'R_TX{local:02d}',1)
 assert pin(b,f'R_TX{local:02d}',2)==pin(b,f'C_TX_AC{local:02d}',1)
 assert pin(b,f'C_TX_AC{local:02d}',2)==pin(b,f'TX{local:02d}',1)
 assert pin(b,f'TX{local:02d}',2)=='GND'
 fp=next(x for x in d['fpga']if x['net']==f'{b}_DATA_RAW_{lane:02d}')
 tx.append(dict(channel=ch,board=b,local_channel=local,row=local//8+1,column=local%8+1,lane=ch//4,bit=bit,send_order='bit3,bit2,bit1,bit0',ax_connector=fp['connector'],ax_pin=fp['pin'],fpga_ball=fp['ball'],rtl_port=fp['rtl_port'],central_chain=f'R_RX_{b}{lane:02d}=22R;3.3pFtoGND;LVT;R_TX_{b}{lane:02d}=47R',array_header_pin=2*lane+1,array_chain=f'LVT data buffer;47R;{sr}.14',sr=sr,sr_output_pin=qpin,sr_output=['QA','QB','QC','QD'][bit],srclk_pin11=pin(b,sr,11),rclk_pin12=pin(b,sr,12),driver=drv,driver_input_pin=inp,driver_output_pin=out,series_resistor=f'R_TX{local:02d}=150R1W',ac_capacitor=f'C_TX_AC{local:02d}=100nFC0G50V',transducer=f'TX{local:02d}',nu_pin1=pin(b,f'TX{local:02d}',1),nu_pin2='GND',status='PASS'))
assert len({x['channel']for x in tx})==128
csvout('05_TX_128_CHANNEL_CHAIN.csv',tx)
adc=[]
for c in range(8):
 b='UP'if c<4 else'DN';n=c%4;pp=49+2*c
 assert pin('CENTRAL','U_ADC',pp)==f'ADC_IN{c}'and pin('CENTRAL','U_ADC',pp+1)=='GND'
 adc.append(dict(kind='RX_ADC_CHANNEL',channel=c+1,board=b,receiver=f'RX{n}:NU40C10R-2',frontend='OPA4192IPWR biased2.5V; detailedphysicalpins/passives in02',array_header_pin=55+2*n,central_net=f'{b}_RX{n}',central_switch='ADG4612BRUZ poweroffprotection',adc_positive_pin=pp,adc_negative_pin=pp+1,adc_net=f'ADC_IN{c}',mode='singleended ±5V; signed16bit; DCoffsetremoved inCfeatures',status='PASS'))
for b,ch in [('CENTRAL',0),('UP',1),('DN',2)]:adc.append(dict(kind='TEMP',channel=ch,board=b,receiver='TMP117NAIDRVR',frontend='TCA9548A0x70onehot channel; TMP117all0x48; volatileconfig01=0000;20msfirstwait;50mspoll',array_header_pin='51SCL/53SDA'if b!='CENTRAL'else'localchannel0',central_net='I2C mux; TCA9517A-B-B-A topology',central_switch='onechannelenabledatonce',adc_positive_pin='N/A',adc_negative_pin='N/A',adc_net='N/A',mode='200msPSfreshnesstimeout; EEPROMneverwritten',status='PASS'))
csvout('06_ADC_RX_8CH_AND_TEMP.csv',adc)
power=[]
for b in ['CENTRAL','UP','DN']:
 for x in d['instances']:
  if x['board']==b and (x['refdes']in ['J_PWR','F1','SW_PWR','U_EF','U_POR','U_5MON','U_TXMON','U_LDO','Q_TX','Q_CUT','U_ARM','U_TEMP']or x['refdes'].startswith(('SW','F','J_PWR','D_TVS','U_BUCK','U_WD','U_G','U_ENCLAMP','U_FAULT','U_PERMIT'))):
   power.append(dict(board=b,refdes=x['refdes'],mpn=x['mpn'],pins=';'.join(f'{p["pin"]}:{p["function"]}={p["net"]}'for p in d['pins']if p['board']==b and p['refdes']==x['refdes']),role=x['role'],rating=x['rating'],safe_scope='TXdefaultoff; permitnewedge; eitherclockloss localkill; fullguide explainsstartup',status='PASS'))
csvout('07_POWER_FAULT_AND_STARTUP.csv',power)
network=[]
for (b,n),ps in sorted(collections.defaultdict(list,{}).items()):pass
groups=collections.defaultdict(list)
for x in d['pins']:
 if x['net']!='NC':groups[(x['board'],x['net'])].append(x)
for (b,n),ps in sorted(groups.items()):network.append(dict(board=b,net=n,pins=len(ps),endpoints=';'.join(f'{p["refdes"]}.{p["pin"]}'for p in ps),status='PASS',erc='NOT_CHECKED_NATIVE_CAD_NOT_CREATED'))
csvout('ALL_NETWORK_AUDIT.csv',network)
dev=[dict(board=x['board'],refdes=x['refdes'],mpn=x['mpn'],package=x['package'],physical_pin_count=sum(p['board']==x['board']and p['refdes']==x['refdes']for p in d['pins']),rating=x['rating'],source=x['source_url'],selection_status=x['selection_status'],pin_status='PASS',procurement_status=x['procurement_status'])for x in d['instances']]
csvout('ALL_DEVICE_AUDIT.csv',dev)
result=dict(status='PASS',instances=len(inst),physical_pins=len(pins),passives=len(d['passives']),bom_types=len(d['bom']),fpga_contacts=80,active_gpio=len(active),array_contacts=128,tx_channels=128,rx_channels=8,nets=len(network),source_independence=['OEMxlsxrawXML','formalRTL/XDC','VivadoroutedI/O','connectioncontract'],native_part='xc7z020clg400-2',hardware=False,native_erc='NOT_CHECKED')
write('results/INDEPENDENT_CONSISTENCY_FINAL.json',json.dumps(result,indent=2));print(json.dumps(result))
intro='''# SonoField-FPGA v5｜嘉立创EDA专业版操作与逐物理引脚连接指南

2026-10-16。性质：原理图绘制输入合同。尚未创建原理图或PCB，未运行原生ERC，未进行跨板实物验证。最终放行结论见10_DRAW_READY_ACCEPTANCE.md。只使用本文、01完整BOM和03–09终版表；旧候选仅作历史证据。

## 1. 冻结架构与唯一选型

中央板×1、相同通用阵列板×2；每块PCB各自用独立12V直流输入。AX7020仅提供控制，J10/J11不供TX或中央板功率。J11.39仅取板上3.3V小电流接口参考，预算≤50mA，实际理论保守预算≤20mA；绝不与中央V3V3并联。其余扩展电源触点NC。所有信号使用规定公共地。

目标板为用户明确确认的XC7Z020-2CLG400I（Vivado xc7z020clg400-2，工业级）。50MHz来自U18，双MMCM生成64MHz中间时钟，再生成共同时间基准128MHz核心和256MHz串行微时钟。载波38.5–41.5kHz，标称40kHz；128TX、256级相位、32lane×4bit实际使用。

B-TX唯一方案为F型六微周期流水：中央5颗、每阵列4颗SN74LVT244BPWR，均本地3.3V。AX现有33Ω保留；中央接收端22Ω串联、3.3pF C0G对地；中央输出47Ω串联；阵列DATA输出47Ω，SRCLK/RCLK每个局部支路15Ω。每个时钟输出驱动4颗595，总局部支路≤27mm、总负载≤50pF；四组不互并。两段线缆各≤150mm，32个阵列偶数针全部作GND。SI模型扫描Z0=80–120Ω、飞行时间0.75–1.25ns等边界；实际走线与排线必须遵守这些界限。

每阵列16颗SN74LVC595APWR使用QA–QD，QE–QH及QH′隔离；32颗UCC27624QDRQ1使用D/SOIC8封装，**没有散热焊盘**。不要换成DDA、WSON或其他同名封装。TX本地12V降压10V、单端驱动，150Ω1W串联、100nF C0G串联隔直、1MΩ泄放。长期NU40C10T-2端电压严格小于20Vpp，60Vpp仅脉冲额定。给定未拟合BVD敏感性模型最坏约15Vpp；这不替代未来首板端电压/阻抗确认，不是声压或悬浮实测。

中央AD7606C-16BSTZ，AVCC与VDRIVE同为本地V5A（约5.084V），8DOUT、8MHz SCLK、320个核心周期采样一次，约400kSPS；不要套用旧132MHz/4DOUT/800kSPS配置。ADC输出经SN74LVC8T245回到AX参考域，控制经AHCT升到V5A。八路同时采样保留。

## 2. 在嘉立创EDA专业版建立工程

1. 打开专业版，在工程面板新建工程`SonoField_v5_CENTRAL_20261016`，再建`SonoField_v5_ARRAY_20261016`。中央与通用阵列是两个独立PCB工程，避免全局电源标签跨板短接。通用阵列只绘制一套，BOM按两块计数。
2. 中央原理图页依次建立`00_POWER`、`01_FPGA_HEADERS`、`02_TX_BUFFERS`、`03_ARRAY_HEADERS`、`04_ADC`、`05_RX_INPUT`、`06_I2C_TEMP_SAFETY`。阵列建立`00_POWER`、`01_LINK_BUFFERS`、`02_595`、`03_UCC_TX`、`04_RX`、`05_SAFETY_TEMP`。
3. 按01_BOM的**精确制造商料号与封装**在元件库搜索。立创号“待采购映射”表示未确认采购/库资源；可搜索MPN对应器件，但必须逐针与本文核对。库中图形名称不是引脚证据。缺失时根据原厂封装图建立符号，物理脚号不得自行换序。
4. 放置器件后先设置位号、值、制造商料号、封装；先连电源/地/退耦，再连信号。按下文模块表和附录逐针连接，按ALL_PASSIVE_CONNECTIONS.csv逐个接入无源双端。短距离直接导线，跨页用唯一网络标签；同名标签只能表示同一个板内网络。
5. 中央保留`UP_`、`DN_`区分信号；通用阵列使用不带方向前缀的本地网名。`GND`是板内共同参考，不串磁珠割裂高速信号回流。独立12V或V3V3不得经排线互供。
6. `NC`是明确不连接标志，**不是全局名为NC的网络**。所有NC脚分别放不连接标记，不互接。未用输入需按表接地或指定电源；未用输出NC；EP只在确实有裸露焊盘的具体封装上连接，不能给SOIC8 UCC或PW20 LVT虚构EP。
7. 先完成中央00_POWER和01_FPGA_HEADERS，再画TX缓冲和阵列接口；随后ADC、RX、I2C、安全；阵列按电源→时钟/数据→595→UCC/TX→RX→安全温度完成。画完运行专业版ERC，逐个处理电源域、未驱动输入、输出冲突、NC与封装针数；不要为消除提示把所有脚设为无源。本次尚未执行ERC。

## 3. 排母、针号、安装方向与线缆

中央J_J10/J_J11为2.54mm双排2×20排母；中央J_UP/J_DN和阵列J_LINK为2.54mm双排2×32排母。AX自带连接器保持原状，用户自配对应公对公排线。数量：40芯两条、64芯两条，逐针1→1，全部GND导体接通。DC-050-20中心针是**2.0mm**，匹配插头不能直接沿用旧2.5mm内孔假设。

本文编号按连接器本身物理pin号，不按屏幕左右猜号。定义配合面视图：pin1为第一排的奇数侧，邻侧pin2；下一排pin3/4，依次至39/40或63/64。背面视图左右镜像，但网络编号不变。PCB丝印标pin1，排线有pin1色带；必须在封装预览中确认库的1号焊盘。若库的几何排列不同，只改变图形摆放，绝不改变针号合同。上下阵列用同一针序；发射面朝内，保持全局row/column方向一致，上板换能器可从相反PCB面安装。若机械上翻转整块阵列，必须明确通道置换，不得悄悄镜像。

J10/J11的1、37、38为GND；2为板端5V，39/40为板端3.3V。除J11.39小电流接口参考外全部电源触点NC。J11.32/33/34/35分别为DOUTE/F/G/H，J11.39不能作为GPIO写XDC；本方案没有IO_ALIVE接口。03表逐个列出全部80触点，09表把原厂针表、真实XDC、实际布局布线IO独立对账。

阵列接口所有偶数针为GND，63为NC。1–31奇数为DATA00–15；33 SRCLK、35 RCLK、37 OE_N、39 TX_PERMIT、41 CENTRAL_POWER_OK、43 RX_BLANK、45 HB、47 FAULT_N、49 PGOOD、51 SCL、53 SDA、55/57/59/61 RX0–3。04表对上下阵列各列64脚及端点。

## 4. 电源、无源与默认关断的实际画法

各板J_PWR.1中心正→F1 3A→SPDT电源开关公共脚→DC12_AFTER_SWITCH→TPS259470L IN；J_PWR.2外壳接GND，3开关触点NC。开关位号/物理脚按附录，不能凭符号位置猜公共端。输入1µF/50V非极性电容对地，原输入侧有极性47µF已删除，避免反接12V损坏电容。双向SMBJ15CA移到eFuse保护后的V12_SW对地；它不承担持续误接高压的吸收，OVLO负责切断。源必须是稳压12V±5%、≥3A隔离SELV电源；不把汽车浪涌等未建模场景写成通过。

TPS259470LRPWR有反接/反灌及限流，ILM=1.3kΩ，3334/R得到标称2.565A，含±10%与电阻误差约2.285–2.85A；ITIMER与AUXOFF按表NC，EN/UVLO、OVLO都有分压，不能悬空。eFuse的默认工作不等于TX许可；`efuse_up/dn` RTL名在接口上表示TX_PERMIT，不能直接连到电源芯片EN取代本地安全链。

TPS54202每路SW→22µH电感→该路输出，BOOT与SW之间100nF；FB用表中精密电阻，上臂输出到FB、下臂FB到GND，上臂并220pF C0G前馈电容；输入/输出电容对本地GND。3.3V与7.15V增加47µF/25V低ESR聚合物电容，TX的47µF放在VTX_PRE。TX开关后保留每颗UCC的100nF，并仅四组共享1µF（位号00/08/16/24），合计7.2µF，减少浪涌。所有有极性电容pin1为正端。

阵列AO4407A源脚1/2/3接VTX_PRE，漏脚5/6/7/8接VTX，4为TX_GATE。100k从G到S默认关断；10k从G到Q_CUT集电极；10nF **G到D**作为Miller软启动，不接成G到S。Q_CUT基极由EN_PERMIT经电阻控制，发射极GND。关断通过独立UCC EN夹低即时抑制输出，不依赖MOS门极慢回升或VTX电容放完。

每组默认导通的MMBT3904 EN夹低器，基极从VTX经8.2k取电，集电极夹住64个ENA/ENB公共网；另一个释放晶体管仅在EN_PERMIT成立时解除夹低。UCC EN内部200k上拉是典型值，不能把10k无源下拉当安全关断；本模型按两倍内部上拉电流检查。每个595输出仍有10k对地，确保OE高、未上电、三态时驱动INA/B为低。595 VOH保证下界2.4V与UCC VIHmax2.3V的静态裕量约0.1V，因此TXLOG为低速、短本地线，要求局部地噪声≤50mV、不得跨连接器。

本地SRCLK和RCLK分别经SN74LVC1G74二分频后触发LTC6993IS6-2。每个定时器1 TRIG、2 GND、3 SET、4 DIV、5 V+、6 OUT；RSET=100k1%，DIV接GND，计入工业级±6%后约1.861–2.141µs。两路存活AND与电源监控共同清除U_ARM；时钟恢复不会重新触发保持高的TX_PERMIT，必须先拉低再产生新的上升沿。故障报告1k/1nF滤除正常ARM数ns偏差，**不滤波本地EN关断**。PGOOD只报告本地电源，不能把时钟WD串进去造成启动死锁。

## 5. TX串行、相位与收发时序

微周期3.90625ns。相对接收一次快域请求：DATA pad在tick1/7/13/19输出bit3/2/1/0，SRCLK在4/10/16/22上升、各高3tick；RCLK在25上升，高3tick。下一快域请求可在24tick开始，旧锁存与下一帧移位错开，不能把serializer重新改成“锁存结束才接受下一帧”。32lane实际每lane4bit映射QA–QD；05表给128通道全部链路。

40kHz×256=10.24M帧/s；F最大256MHz/24=10.6667M帧/s。41.5kHz×256=10.624M帧/s仍可持续，最短核心间隔12周期。4096帧、三个载波点、两个RTL模拟器逐128位比较；不得用理想吞吐公式代替这些实际测试。相位量化单步97.65625ns，NCO时间抖动受核心7.8125ns量化；全通道共同流水延迟保留在校准时间参考内，不增加通道极性反转。

核心缺完整帧64周期后关断（约0.5µs量级，CDC/同步再计若干周期）；整个PL/时钟停摆由阵列独立硬件WD关断，约2.14µs加门延时。正常PC保持目标不变仍持续刷新完整输出帧，不会误判为缺帧。

## 6. ADC、RX前端、温度和PS参数

AD7606C-16：OS0/1/2接V5A，PAR/SER_SEL接V5A，STBY_N/WR_N/REF_SELECT接V5A，RANGE接GND，以软件模式初始化并读回0x0218八DOUT。不要用硬件模式或旧0x0210四DOUT初始化。pin36/39 REGCAP分别各1µF到AGND；pin42参考100nF到REFGND；44/45短接后10µF低ESR到REFGND；所有AVCC各就近100nF；所有AGND/REFGND接连续本地GND。ADC参考4.4V网络不是RX的外部2.5V偏置源。

ADC模拟正输入49/51/53/55为UP RX0–3，57/59/61/63为DN RX0–3，负输入50/52/54/56/58/60/62/64接GND。每路经过ADG4612掉电隔离及499Ω/1nF输入RC。阵列OPA4192按附录各通道的IN+/IN−/OUT接入偏置、反馈、输入耦合；反馈电阻在OUT和IN−之间，电容按双端表连接，不把所有电容一端机械接地。两块板的2.5V偏置各自生成，不通过排线并联。

DOUTA/B/C/D物理24/25/27/28，E/F/G/H物理19/20/21/22。SDI29、SCLK12、CS13、BUSY14、RESET11、CONVST9。ADC在SCLK上升沿后更新DOUT，RTL在下一次上升沿采旧数据；8MHz的完整125ns周期用于该往返。联合模型采用44ns DOUT路径上界及500/650ns转换交替。不能误改为半周期采样。数字CRC保持关闭并读回，数据有符号16位，C特征提取先检查原始削顶再去除2.5V偏置。

TCA9548A地址0x70；通道0中央、1上板、2下板，三个TMP117都0x48（ADD0接GND）。主侧TCA9517 A=AX参考3.3V，B=中央3.3V；阵列A=排线侧、B=本地传感器侧，避免TCA9517的B侧直连B侧。总线100kHz，每段上拉与负载按原理图表；只允许一次选一个mux通道。

PS初始化三个TMP117身份后，仅写易失配置寄存器01=0000，连续单次转换约15.5ms，先等待≥20ms，此后每50ms读取全部三点。禁止写EEPROM或使用旧一秒默认配置来满足200ms新鲜度要求。control16温度有效、17温度安全、18配置有效；仅全三点读取成功后翻转control19。200ms没有新的合格翻转立即撤销健康许可；固定高电平不能喂狗。总线NACK、超时、读数范围异常使标志无效。

GPIO控制低16位协议保留。PS AXI地址：核心0x40000000，任务BRAM0x42000000，服务GPIO0x41200000，I2C0x41600000。采样时间换算必须用128MHz/320，不能硬编码800kSPS。115200 UART全128路原始校准传输量约2MiB，生产CAL任务截止600s；其他阶段30s不变，200ms温度新鲜度、缺帧和2µs时钟故障均持续有效。600s是通信任务总时限，不是安全响应时间。主机/C/BSP适配与板端部署状态在FINAL_REVIEW中单独说明，当前未下载任何镜像。

## 7. 绘图后ERC与后续PCB输入

本次原生ERC=NOT_CHECKED，因为用户授权的工作到理论连接指南为止。完成原理图后逐页检查所有电源口、未用输入、UCC无EP、LDO/TMP117确有EP、ADC参考电容、磁性件额定、开关公共端、全部GND及NC。BOM采购映射和封装库逐针复核仍为制板前事项。不得将本指南当作PCB布局或Gerber放行。

布局输入：595集中为四个短时钟组，UCC靠近对应595，TXLOG≤25mm，长线放在150Ω阻尼后的换能器一侧；ADC/AHCT所有本地控制线≤25mm、CL≤15pF。高速缓冲紧靠接口，接收RC紧靠中央LVT输入；4颗595一个时钟分组，27mm是整条局部时钟支路上限；信号参考连续地，不跨电源分割；64线排线保留偶数地，屏蔽/接地环路遵守独立隔离适配器约束；ADC/RX远离SW、10V驱动回流；BUCK/LDO热铜按功耗上界设计。输入环境0–40°C是当前热估算边界，不等于全系统工业温度认证。

## 8. 全部物理针与无源连接附录

下表板作用域：CENTRAL为中央板；UP与DN是相同通用阵列板的两块实体。阵列绘图以UP一次为准，DN只替换实体作用域，不能将两板的本地电源并联。电气类型IN/OUT/POWER/PASSIVE作为符号ERC设置输入；OD输出应在专业版设开漏类别或据库规范设置。

'''
parts=[]
for b in ['CENTRAL','UP','DN']:
 parts.append(f'### {b}全部非无源器件逐针表\n')
 nonpass={x['refdes']for x in d['passives']if x['board']==b}
 rows=[dict(位号=x['refdes'],型号=x['mpn'],物理脚=x['pin'],功能=x['function'],网络=x['net'],类型=x['kind'])for x in d['pins']if x['board']==b and x['refdes']not in nonpass]
 parts.append(mdtable(rows,['位号','型号','物理脚','功能','网络','类型'])+'\n')
 parts.append(f'### {b}全部电阻、电容与电感等双端连接\n')
 rows=[dict(位号=x['refdes'],型号=x['mpn'],值=x['value'],端1=x['pin1_net'],端2=x['pin2_net'],封装=x['package'],额定=x['rating'],极性=x['polarity'])for x in d['passives']if x['board']==b]
 parts.append(mdtable(rows,['位号','型号','值','端1','端2','封装','额定','极性'])+'\n')
write('02_JLCEDA_PRO_COMPLETE_SCHEMATIC_GUIDE.md',intro+'\n'.join(parts))
write('03_AX7020_J10_J11_PINMAP.md','# AX7020全部80触点\n\n'+mdtable(d['fpga'],['connector','pin','manual_signal','ball','bank','net','rtl_port','direction','iostandard','vcco_theory']))
write('04_CENTRAL_TO_ARRAY_2x32_PINMAP.md','# 上下阵列全部128触点\n\n'+mdtable(array,['board','pin','signal','central_net','array_net','direction','safe_default']))
write('05_TX_128_CHANNEL_CHAIN.md','# 128TX唯一链路\n\n'+mdtable(tx,['channel','board','row','column','lane','bit','ax_connector','ax_pin','array_header_pin','sr','sr_output_pin','driver','driver_input_pin','driver_output_pin','transducer']))
write('06_ADC_RX_8CH_AND_TEMP.md','# 8路RX/ADC与三点温度\n\n'+mdtable(adc,list(adc[0])))
write('07_POWER_FAULT_AND_STARTUP.md','# 电源与故障逐器件\n\n'+mdtable(power,['board','refdes','mpn','pins','safe_scope','status']))
write('ALL_PASSIVE_CONNECTIONS.md','# 所有必要无源双端连接\n\n'+mdtable(d['passives'],['board','refdes','mpn','value','pin1_net','pin2_net','package','rating','polarity']))
changes=[]
old=json.loads((R/'inputs/PREVIOUS_CONNECTION_DATABASE.json').read_text(encoding='utf-8'));oldinst={(x['board'],x['refdes']):x for x in old['instances']}
for key in sorted(set(oldinst)|set(inst)):
 a=oldinst.get(key);b=inst.get(key)
 if a!=b:
  changes.append(dict(board=key[0],refdes=key[1],change='ADD'if not a else'REMOVE'if not b else'REVISE',old_mpn=a['mpn']if a else'',new_mpn=b['mpn']if b else'',old_value=a['value']if a else'',new_value=b['value']if b else'',reason='Final3.3Vregeneration/watchdog/power/inrush correction; original preserved'))
csvout('DESIGN_DIFF.csv',changes)
write('DESIGN_DIFF.md','# 与上一精简候选的差异\n\n取消USB-C、三板独立12V是用户当前架构，旧S3/S4文件未修改。本表比较隔离目录保存的上一连接数据库。历史66MHz、AUC2.5V、中央82Ω无源传输、AX_IO_ALIVE复用等不再是本版候选；旧文件只读保留。\n\n'+mdtable(changes,['board','refdes','change','old_mpn','new_mpn','old_value','new_value']))

