"""Generate S3 review text, pin-labelled vector sheets and bounded model tables."""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,html,math,cmath,re,hashlib
R=Path(__file__).resolve().parents[1];ROOT=R.parents[4];E=ROOT/'v5/evidence/pcb_s3_20261011'
def rd(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def csvout(p,rows):
    with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,list(rows[0]));w.writeheader();w.writerows(rows)
def write(name,text):(R/name).write_text(text.strip()+'\n',encoding='utf-8')
def main():
    c=rd(R/'netlist/COMPONENTS.csv');pins=rd(R/'netlist/PIN_NET.csv');p=json.loads((E/'POWER_RESULTS.json').read_text());cnt=json.loads((E/'CANDIDATE_COUNTS.json').read_text())
    sources=json.loads((E/'SOURCE_MANIFEST.json').read_text())['documents'];source={x['name']:x for x in sources}
    specs={
      'TPS259470LRPWR':('tps25947','RevC May2026;Table5-5/Table9/7-3;pp7-10,29-38','2.7..23V;TJ-40..125C','IN -15..28V;not working rating','RON<=45mOhm;IQ<=610uA;1.65k Table9 ILIM1.8..2.2A','tLIM400us/fasttrip500ns TYP only;ITIMER open does not mean zero delay'),
      'TPS54202DDCR':('tps54202','RevC Feb2026;p5 EC','VIN4.5..28V;TJ-40..125C','VIN30V stress only','VFB0.581..0.611V;f390..630k;HSlimit2.5..3.9A','IQ45uA TYP;2A is output capability;minimum currentlimit not dissipation'),
      'TPS63070RNMR':('tps63070','RevB Mar2019;pp3-7 EC','VIN2..16V;startVIN>=3V;VOUT2.5..9V','VIN20V;TJ150C stress only','forcedPWM FBaccuracy+/-1%;inputlimit3.05..4.15A at specified5V->6.5V test','2A output only under specified buck conditions;no guaranteed efficiency minimum'),
      'TPS7A2033PDBVR':('tps7a20','RevH Jul2024;pp4-7 EC','VIN1.6..6V;VOUT3.3V;TJ-40..125C','See p5 stress;not20V tolerant','accuracy+/-1.5% withVIN>=3.6V;dropout<=145mV at300mA','300mA outputcapability;bootstrap20mA allocation must be verified'),
      'ADP7118AUJZ-5.0-R7':('adp7118','RevH;Table1 p3;Table5 p6','VIN2.7..20V;5Voutput;IOUT<=200mA','SeeTable4;currentlimit250..460mA not workingcurrent','5V+/-1.8% overtemp;accuracy requiresVIN>=VOUTnom+1V;dropout<=420mV at200mA','SS TSOT unavailable;start380us TYP;headroom alone is not transient proof'),
      'AD7606C-16BSTZ-RL':('ad7606c16','RevA;Table2 pp6-9;Table9 pp15-17','AVCC4.75..5.25V;VDRIVE1.71..5.25V;1MSPS','AVCC6.5V;analog+/-21V;pin+/-10mA stress','IAVCC50mA max;IDRIVE1.9mA max at1MSPS;HBW220kHz at+/-5V','Inputrange,bandwidth,4DOUT registers require physical readback;+/-2.5V HBW150kHz'),
      'TC4427AEOA':('tc4427a','DS20001423J;pp3-4 DC;Table3-1 p8','VDD4.5..18V;TA-40..85C Egrade','VDD22V;input<=VDD+.3V','VIH>=2.4V;VIL<=.8V;inputleak+/-10uA fulltemp;IQmax1.5mA high','1.5A peak TYP at18V is output capability;RON limits at18V not12V;dynamic supply curves TYP'),
      'SN74LVC595APWR':('sn74lvc595a','RevA Oct2025;pp3-8','VCC1.65..3.6V;TA-40..125C','VCC6.5V;IO50mA stress','4 outputs used of8;input5Vtolerant/Ioff;staticICC and switchingC separate','104MHz singledevice rating not66MHz endtoend proof;unusedQ4..Q7NC'),
      'SN74LVC244APWR':('sn74lvc244a','Downloaded source exactSHA in manifest;pin/EC tables','VCC1.65..3.6V','See selecteddatasheet stress tables','Ioff inputbuffer candidate;one local powered domain','clockfanout16 loads/cable/source rise needIBIS/STA'),
      'SN74AXC8T245PWR':('sn74axc8t245','Rev/EC in manifest;Table4-1 pin map','VCCA0.65..3.6V;VCCB0.65..3.6V','Not12V tolerant','twoDIRs;DIR2ground;OE pull high;Ioff local supply loss','localIoff does not prove AX7020 powered-off safety;VCCO unknown;manualdisconnect gate'),
      'TUSB321AIRWBR':('tusb321ai','SLLSER2A May2017;pin/functions currentadvertisement','UFP PORTground;VDD2.7..5V operating table','See absolute table;not20V fault certified','OUT2 OD low for3A only;VBUS_DET900k;internalRd','2017 TypeC1.1 document;no present USB-IF certification claim'),
      'TPS3851H33EDRBR':('tps3851','SBVS300B Jun2025;pp3-7','VDD1.6..6.5V;TJ-40..125C','VDD7V stress','H33 UV3.069V+/-0.8%;CWD10k/SET1high170..230ms','RESET undefined belowPOR;WDOhighZ whileRESETlow;no earlyfeed function'),
      'TPS3430DRCR':('tps3430','SBVS366A Oct2021;Table8-3 p18','VDD1.6..6.5V;TJ-40..125C','See p4','CWDNC SET0=0 SET1=1;lower1.48..2.22ms;upper23.375..31.625ms','FALLINGedge;CRSTNC170..230ms startup ignore;not an independent progress generator'),
      'TMP302ADRLR':('tmp302','SBOS488E Dec2018;pin/EC tables','VS1.4..3.6V','See stress table','A bothTRIPSETshigh65C;+/-2C;HYSThigh10C typical;IQmax15uA','thermal placement/lag/driverjunction unqualified'),
      'INA226AIDGSR':('ina226','SBOS547C Aug2026;pin/EC','VS2.7..5.5V;bus0..36V','bus40V stress','shunt+/-81.92mV;selected20mOhm<=44.889mV','currenttelemetry is not independent powercut'),
      'TMP117AIDRVR':('tmp117','SNOSD82D Sep2022;Table5-1 p4','VS1.7..5.5V;TA-55..150C','See stress table','one telemetrysensor/board;average current depends conversionmode','Do not substitute software temperature limit forTMP302'),
      'OPA4192IPWR':('opa4192','SBOS620 family;EC andpin map','supply4.5..36V;rail-to-rail','inputclamp+/-10mA stress limit;not a working fault regime','peramp1mAtyp/1.3mAmax allocation;quad4amps;twoquad/array','poweredoff receiver injection/ESD/real source spectrum remain unqualified'),
      'REF5025AIDR':('ref50','SBOS410O Oct2025;Table3,pp3-4','VIN up to18V standardgrade;5V used','See stress table','2.5V;initial+/-0.1%;8ppm/C;IQmax1.2mA','externalADCreference;bias loads/cap stability need qualification'),
      'TMUX1574PWR':('tmux1574','SCDS391C Dec2019;PW pinmap p3','VDD1.5..5.5V;postamp terminals0..5V','See stress table;not rawbipolar sensor protector','SELhigh routesVBIAS;ENground;poweredoffprotection function','break-before-make/charge injection/settling needRXblank timing test'),
      'MMBT3904LT1G':('WEB_ONSEMI','MMBT3904LT1/D Rev15 Sep2026;pp1-2','candidate40kHz;C-E voltage13.2V;hot qualification pending','VCEO40V;IC200mA;TJ150C stress','pin1B/2E/3C;VCEsat<=.2V atIC10mA IB1mA;hFEmin70 at1mA','storage200ns bound only atspecified25C test;no alltemp phase guarantee'),
      'USB4500-03-0-A':('WEB_GCT','Manufacturer productpage captured20261011','5A collectiveVBUS;16 contacts;poweronly use','48V connector rating does not protect5V chips','aftertest contactR<=50mOhm;midmount0.8mm','exactdrawingrevision/footprint acquisition outstanding'),
      'PJ-002BH':('pj002bh','2024-09-12;pp1-2','24VDC5A;2.5mmcenter;THT','No higherfault rating implied','contactR30mOhm;jackdepth9.5mm','terminal1center mapping requires footprintvisualsignoff'),
      'SMBJ15A':('WEB_LITTELFUSE','SMBJ series electrical table','standoff15V','600W pulse capability notcontinuouspower','clamp24.4V specifiedwaveform;leakage1uA test','leadL overshoot and source/fuse coordination not guaranteed'),
      '0451003.MRL':('WEB_LITTELFUSE451','451/453 series table;3A row','3A125V;2410','Fuse rating does not establish protectedchip SOA','nominalcoldR.0227ohm;nominalI2t1.650A2s','I2t/temperaturederating/faultsource coordination HOLD')
    }
    for mp,name in [('SN74LVC1G74DCUR','sn74lvc1g74'),('SN74LVC1G17DBVR','sn74lvc1g17'),('SN74LVC1G04DBVR','sn74lvc1g04'),('SN74LVC1G32DBVR','sn74lvc1g32'),('SN74LVC1G08DBVR','sn74lvc1g08')]:
        specs[mp]=(name,'manifest revision;pin/EC tables','VCC1.65..5.5V;3.3V selected','See datasheet stress;not12V tolerant','Ioff/VOH/VOL conditions;1G74noninvertedQpin5','dynamiccurrent and poweroffinjection separately qualified')
    registry=[]
    for mp in sorted(set(x['mpn'] for x in c if x['refdes'].split('_',1)[1].startswith('U') or x['mpn'] in specs or x['function'] in ['ultrasound_transmitter','ultrasound_receiver'])):
        if mp not in specs:
            ds=next((n for n in source if n in mp.lower()),None)
            info=(ds or 'NO_GUARANTEED_VENDOR_MODEL','manifest/pin table ifavailable','S3selectedrail;completegrade table must be signed','UNKNOWN_NOT_INFERRED','No guaranteed dynamiccurrent substituted','Vendorordering/model/pin/temperature qualification required')
        else:info=specs[mp]
        name,rev,op,ab,vals,lim=info;refs=[x for x in c if x['mpn']==mp]
        registry.append(dict(device=mp,qty=len(refs),refdes=' '.join(x['refdes'] for x in refs),operating_conditions=op,absolute_max_separate=ab,guaranteed_or_tested_parameters=vals,typical_assumptions_and_limitations=lim,revision_table_pages=rev,source_URL=refs[0]['source_url'],download_sha256=source.get(name,{}).get('sha256','WEB_REFERENCE_OR_VENDOR_UNKNOWN'),qualification='CANDIDATE_NOT_RELEASED'))
    csvout(R/'01_DATASHEET_MAX_RATINGS_REGISTER.csv',registry)
    # Mating connections are explicit, separate from each board's localnet names.
    byp={(x['refdes'],x['pin']):x for x in pins};mates=[]
    for b in ['UP','DN']:
        for k in range(1,65):
            a=byp['CENTRAL_J'+b,str(k)];z=byp[b+'_JCTRL',str(k)]
            mates.append(dict(cable=b,central_ref=a['refdes'],central_pin=k,central_net=a['net'],array_ref=z['refdes'],array_pin=k,array_net=z['net'],installed='YES' if a['disposition']=='CONNECTED' else 'NC',qualification='KEYED64PIN_INTERLEAVED_GND_CABLE_MPN_HOLD'))
    csvout(R/'08_INTERBOARD_CONNECTIONS.csv',mates)
    geometry=[]
    for b,z in [('UP',50),('DN',-50)]:
        for i in range(64):geometry.append(dict(board=b,channel=i,x_mm=(i%8-3.5)*12,y_mm=(i//8-3.5)*12,radiating_face_z_mm=z,origin='SYSTEM_GEOMETRIC_CENTER',status='NOMINAL_GEOMETRY_NOT_LAYOUT'))
    csvout(R/'08_NOMINAL_TX_GEOMETRY.csv',geometry)
    # Frequency-domain nominal/corner sweeps; excludes transducer physics and ADC internalfilter.
    afe=[]
    for f in [1000,10000,40000,100000,500000]:
        for corner in [-1,0,1]:
            rr=1+.001*corner;cc=1+.02*corner;s=2j*math.pi*f
            h=100000/(9980+1/(s*100e-9)+100000)*(1+(100000*rr/(1+s*100000*rr*15e-12*cc))/(10000/rr)) /(1+s*2210*rr*680e-12*cc)/(1+s*499*rr*1e-9*cc)
            afe.append(dict(frequency_hz=f,corner=corner,gain=abs(h),phase_deg=cmath.phase(h)*180/math.pi,status='LINEAR_RC_MODEL_ONLY_NO_ADC_INTERNALFILTER_NO_RX_VENDOR_MODEL'))
    csvout(E/'AFE_FREQUENCY_SWEEP.csv',afe)
    loadnormal=64*13.2**2/1485*.5+p['array_normal_c0_only_w']+32*.0015*13.2+64*3.37**2/990/.8+64*3.37*(3.37-.65)/990/.8+.30+p['efuse_one_heat_w']*2+p['shunt_heat_w']
    conditions=[]
    for b in ['UP','DN','CENTRAL']:
        for mode in ['STANDBY','NORMAL_ALL_ACTIVE','STARTUP','FAULT_CONTINUOUS_LIMIT','FAST_FAULT']:
            conditions.append(dict(board=b,mode=mode,continuous_input_bound_W=p['central_steady_input_max_w'] if b=='CENTRAL' else p['array_steady_input_max_w'],conditional_model_W=round(loadnormal,6) if b!='CENTRAL' and mode=='NORMAL_ALL_ACTIVE' else None,peak_A=p['tx_all_edges_peak_a'] if b!='CENTRAL' and mode=='NORMAL_ALL_ACTIVE' else None,peak_time_s=330*2.64e-9 if b!='CENTRAL' and mode=='NORMAL_ALL_ACTIVE' else None,status='NO_FINITE_GUARANTEED_FAST_FAULT_ENERGY' if mode=='FAST_FAULT' else 'STEADY_INPUT_LIMIT_ONLY; NO_UNINTERRUPTED_OPERATION_GUARANTEE',formula='C0 + bias + levelshift + assumed80pct efficiency; not measured' if b!='CENTRAL' and mode=='NORMAL_ALL_ACTIVE' else 'Table9 limit; excludes pre-limit propagation/overshoot'))
    csvout(R/'02_OPERATING_CONDITIONS.csv',conditions)
    write('00_BASELINE_AND_EXECUTION_SCOPE.md',f'''
# PCB-S3 execution contract / baseline

PROJECT_ID=SONOFIELD_FPGA;repository=https://github.com/loverlike1216/SonoField-FPGA.git;workspace=E:/Codex_project/AMD_Sonofield_PCB_v5;branch=feat/v5-pcb-design;active/highest=v5;S3 base=23f8d4cedb44536f8c35fd132171868a80f9ded7.

用户实际回复：“按 S3 文件完整执行，保持 v5、制造/采购/板写/main 合并 HOLD”。正式指令完整保存在 AI-interaction-memory/codex/instructions/v5_pcb_s3_engineering_20261011.md，SHA256=b3a33a2b0541e8626ea952f2c6c8288ae0a78b8133f024c1cd05c42036475e44。附件中的批准文字没有被当作独立授权；本轮依据真实用户回复执行。

Goal/Scope: 三板器件级候选、严格连接表、最大持续输入包络、条件负载模型、保护真值表、可复算工作簿、实位号BOM和Draft PR6同步。电源选择由Codex完成。未知真实RLC不再阻止画图。

Non-goals/Do not change: RTL/firmware/XDC/接口协议/goldens/35dB门限/128TX8RX/32lanes×4used/40kHz激励/50Hz运动/12mm pitch/100mm nominal90–115mm gap/AX7020Rev3/C16。无v6。无实板串口/JTAG/SD/Flash/DDR操作、采购制造、main合并。原工作区和Historical project正文不读写。

Architecture: 每阵列独立12V；中央5V3A USB-C只供电；AX7020电源触点NC；每阵列TPS3851×1另加独立窗口监测、温度、锁存、TX独立切断。外部ChatGPT读取BLOCKED，无独立审查伪称。

Validation: 原243测试；严格pin/net数量/实际端口/ADC物理pin/上下一致性/硬件禁能逻辑/功率角落计算；工作簿缓存与Python交叉计算。S2已有3696帧×3Icarus+1XSim为继承证据，本轮未重跑且不宣称新跑。原生CAD未连接时使用明确允许的严格连接表降级；ERC NOT_RUN。

Rollback: 独立工作树新增S3路径，保留S2、失败日志和原BOM；可通过revert S3提交撤销；不reset/forcepush。DoneWhen: 候选内容可审查可复算、未完成门禁明确、PR更新并确认远端；不等同制造验收。

Reproduce from worktree: `.venv/Scripts/python.exe v5/hardware/pcb/reviews/20261011_s3/calc/power_worst_case.py`, then `build_candidate.py`, `review_candidate.py`, `build_reports.py` in同一calc目录。设置PYTHONUTF8=1；输出限S3目录；脚本不访问硬件。工作簿命令见calc/build_workbooks.mjs。
''')
    write('03_POWER_SELECTION_FINAL_RECOMMENDATION.md',f'''
# 电源选择结论：中央5V3A；每阵列12V3A36W

中央固定5V/3A USB-C，15W是标称容量。TUSB321AI UFP/PORT=GND，内部Rd，不再并联5.1k；OUT2低才通过反相器打开TPS259470L。默认/1.5A广告只允许CC启动支路。USB数据触点NC，原PC→AX7020 UART链路保持分离。

每块阵列选择 **Mean Well GST36E12，12V/3A/36W，P1L 5.5×2.5×9.5mm中心正定制插头候选**；若只有标准P1J，不能强插2.5mm插座，也不能省略适配转接额定审查。适配器文件GST36E-SPEC2026-04-03 pp2–4；230VAC、环境≤50°C、100–264VAC按降额曲线核对。更高环境温度须降额，不把36W在70°C仍可用。P1L可涉及MOQ，采购仍HOLD，不产生订单。

TPS25947 RevC Table9 RILIM=1.65kΩ：保证表格区间1.8–2.2A；传播电阻±1%后按保守逆比包络得到 {p['ilim_min_a']:.6f}–{p['ilim_max_a']:.6f}A。非表中其他阻值不做假精确插值。输入额外留2mA支路分配，实际确认手册所列Iq/分压/TVS泄漏合计不超过分配后，阵列持续输入设计上界={p['array_steady_input_max_a']:.6f}A×13.2V=**{p['array_steady_input_max_w']:.5f}W**；中央加20mA启动支路分配后={p['central_steady_input_max_a']:.6f}A×5.5V=**{p['central_steady_input_max_w']:.5f}W**。2mA/20mA为须验证分配，不是原厂对整板的承诺。

已核查GST25E12约2.08A，低于2.224A边界；GST36E12的3A覆盖边界，差额{p['adapter_current_margin_a']:.6f}A。选择36W是这两个核查系列中最低合适规格，不声称全市场绝对最低，也不预设40/60W或统一30%裕量。表格输出能力、芯片absmax和真实消耗严格分开。

线束：适配器原厂1m16AWG候选；新增线若有则≤0.5m、18AWG或更粗、温度额定≥80°C、实际插头温升/拉力检查。PJ-002BH原厂24V5A、接触电阻30mΩ；3A接口能力覆盖持续2.224A边界，故不为功率额定而改高电流接口。3A2410熔丝0451003.MRL、SMBJ15A、限流eFuse、20mΩKelvin取样构成保护；保险丝不是芯片保护的快速替代。

USB连接器VBUS设计3.8–5.5V，额外板内回路阻抗分配≤0.12Ω时，2.224A后约3.533V；TPS63070启动≥3V可覆盖这一静态条件。该0.12Ω分配须以器件/铜/插座实测校核。中央数字3.3V来自6.3V升降压后的TPS54202，避免把低VBUS直入3.3VLDO的精度条件误判；启动LDO在输入保护前，只供低功率CC。USB异常20V/ESD/热插拔的保护仍需验证。

重要限制：这些是**限流定义的持续系统设计上限**，不保证压电真实负载恒定、不保证故障前瞬时电流、不保证持续满限流时芯片温度允许、不保证欠压时仍正常采样。超过包络时允许停机。TPS25947 tLIM/fasttrip只有典型响应，故“全部故障能量已理论保证”不成立。启动47nF/10nF dVdt为明确值候选，按原厂应用公式/典型曲线评估后必须做斜率、源阻、有效C、短路SOA交叉验证。

数据来源：[TPS25947](https://www.ti.com/lit/ds/symlink/tps25947.pdf)、[GST36E](https://www.meanwell.com/Upload/PDF/GST36E/GST36E-SPEC.PDF)、[PJ-002BH](https://www.sameskydevices.com/product/resource/pj-002bh.pdf)。完整逐器件预算CSV/工作簿含UNKNOWN，不以空值冒充零功耗。
''')
    write('04_TX_POWER_ENABLE_AND_SAFETY_SCHEMATIC.md',f'''
# 阵列电源切断和安全电路候选

精确连接以netlist/PIN_NET.csv为准，UP/DN逐位一致；svg/为由同一连接表输出的带pin/net标记审图页，非嘉立创EDA原生图纸。没有运行ERC。

路径：J1中心正12V→F1 3A→D1 SMBJ15A→U1 TPS259470LRPWR全板输入保护→RS1 20mΩ→常供逻辑/AFE及U5独立TX切断→TX12→32×TC4427A。U1的UVLO用38.3k/4.99k、OVLO48.3k/4.99k，均0.1%；用比较器min/max和漏电验证上下界。U5 EN由锁存ARMED经过100k/100k分压，默认接地；所有TC输入高侧上拉都由TX12供电。U1/U5各1.65k1%限流，ITIMER NC；不能解释为零延迟。

U10 TPS3851H33EDRBR：VDD=3V3，CWD经10k至3V3，SET1高，MR高；RESET和WDO为开漏汇入FAULT_N。每阵列1颗、总2颗。H33约3.069V±0.8%欠压监测；看门狗170–230ms，非窗口。U11 TPS3430DRCR是**补足过快检测**，不是旧TLV803组合；CWD/CRST NC、SET0低、SET1高，下降沿合法保证交集2.22–23.375ms。建议合格进度每20ms下降沿，19–21ms合同；低/高各5/15ms或10/10ms实现须与下降沿合同一致，不用40ms翻转误喂。

U12 TMP302A两TRIPSET高：65°C候选，HYST高10°C典型；独立于TMP117/I2C/PS。放在TC阵列热点邻近，需热点和响应滞后实测。JESTOP常闭回路，断线后10k下拉、U15反相、QSAFE拉低FAULT_N。U1/U5 FLT也经0Ω显式汇入FAULT_N，但FLT并不报告所有UV/OV，12V保护依靠eFuse直接比较器，逻辑欠压由TPS3851独立处理。

U13 SN74LVC1G74：/CLR=FAULT_N，D=/PRE=3V3，非反相Q是**pin5**，反相Q是pin3；手动按钮、RC、Schmitt送CLK。故障清零锁存；故障消失不产生CLK上升沿，所以不自动重启。按钮持续按下不能当作持续许可；按钮弹跳/释放时序仍须实测。启动RESET保持低期间不能正常解锁，初始化必须在进度合格后人工重使能。

分压处理POR盲区：FF VCC<1.65V输出未定义，按输出≤VCC及EN漏电分配，EN最大{p['kill_en_undefined_vcc_max_v']:.4f}V<eFuse下降阈值min1.076V。健康3V3≥3.15V且小负载VOH≥VCC−.2V时，EN最小{p['kill_en_normal_min_v']:.4f}V>上升阈值max1.223V。其他引脚反灌破坏该供电边界的情形仍需电气验证，不能用布尔表证明。

U16/U17/U18把FPGA OE、NOT_ARMED、FAULT_BAD组合为595_OE_N，10k默认上拉。数据无效时强制595高阻，逐通道基极下拉使TX输入低；3V3完全掉电时TX可残留DC电压，依赖切断和680Ω泄放。总TX电容上限设计750uF时，储能≤{p['tx_stored_energy_max_j']:.5f}J、降到1V被动泄放约{p['tx_bleed_time_to_1v_s']:.3f}s；**不是瞬时归零或认证安全能量**。C/ESR/泄漏/声学单次瞬态必须在G2验证；若要求更快泄放，优先补独立主动泄放电路，当前未伪称已有。

已检256种布尔故障/锁存组合；任一UV/early/late/temp/estop/inputflt/txflt使能均为0。这只是静态ALTERNATIVE_VALIDATION。手册未给出最大fasttrip/传播/能量时，仍保留制造HOLD，不能虚构一个全故障瞬态上界。
''')
    write('05_TX_DRIVER_64CH_SCHEMA_AND_THERMAL.md',f'''
# 64TX/阵列连接与热审查

05_TX_CHANNEL_MAPPING.csv逐项列128个全局通道、row/col、32lanes中的lane、4used bit、595物理Qpin、TC物理输出pin、330Ω串阻、NU40C10T位号。每阵列16×595，每颗QA/QB/QC/QD用pin15/1/2/3；QE–QH及QH'明确NC。每阵列32×TC4427AEOA，SOIC8pin2INA/4INB/7OUTA/5OUTB/6TX12/3GND/1和8NC。

每路：595Q→1k基极→QA NPN，QA集电极经1k上拉3V3，再经1k基极→QB NPN；QB集电极经1.5k上拉TX12，10k下拉，进入TC；两次反相保持原逻辑相位。每基极10k下拉；TC输出→330Ω1%2512≥1W→TX正端，TX负端GND。该结构用器件数换取电源域关断路径可见性，未采用没有3.3V全温时序保证的CD40109B作为保证路径。MMBT3904两级全温延迟需测，不用25°C storage时间承诺系统相位。

基极驱动、最小hFE和强迫β按原厂测试条件检查；1.5k下拉电流约8.9mA、10k下拉及输入漏电均计入状态。高电平10.8V×10k/(10k+1.5k)约9.39V，高于TC2.4V；低电平目标≤.2V低于.8V，仍须全温和PCB检查。TC input max为VDD+.3V，高侧电阻只来自其自身TX12，避免常供3.3V直接高灌入掉电TC。

不把TC1.5A峰值能力乘64当功耗。C0=2.2nF±20%仅为敏感性假设，未包含谐振支路。在13.2V40kHz64路下，C0充放电模型={p['array_normal_c0_only_w']:.6f}W；64路同向边沿串阻约束峰值={p['tx_all_edges_peak_a']:.6f}A，时间尺度RC≈0.87us，电荷{p['tx_edge_charge_c']:.9f}C。470uF最小376uF只考虑电荷的跌落={p['tx_edge_bulk_droop_v']:.6f}V，**未含ESR/ESL**。

330Ω对2.64nF的极点{p['tx_c0_pole_hz']:.0f}Hz，40k增益{p['tx_c0_40k_gain']:.6f}；不是换能器真实频响。单路端口对地硬短、TC持续高时，330Ω最低326.7Ω耗散{p['tx_one_short_continuous_w']:.6f}W，故使用2512≥1W并检查热降额和脉冲曲线；绝不只按50%软件占空保护。64路同时短路未经总限流将需{p['tx_all_shorts_unlimited_w']:.6f}W，输入保护会限制/停机，不保证声场继续正常。

条件正常全通道模型（含NPN偏置、TC静态、C0、20mΩ、eFuse导通及**假设80%变换效率**等）约{loadnormal:.3f}W/阵列。不是保证总负载。低效率、线损、TC动态交越、磁件损耗均需补测/模型；真实持续输入受29.36W包络约束，但保护IC可能先因热停机。

每TC本地100nF+1uF/16V有效C需验证，TX入口470uF25V；总Cmax≤750uF为设计约束。以TC手册18V RON上限来推12V热不合法；因此未给伪精确TC结温。核查热路径、所有短路位置、TC芯片内部短路、保护FET失效短路的单故障覆盖，均在G2；输入限流不能自动证明每芯片SOA。
''')
    write('06_RX_AFE_ADC_AND_CENTRAL_USB_C.md',f'''
# 8RX/AFE/C16/中央USB-C

每阵列4RX，型号仍RX_MPN_UNKNOWN；每阵列2×OPA4192四运放，合计4颗/16个放大器，每路两级，数量无虚增。每RX经2×4.99k0805、100nF50V耦合、100k偏置到本地REF5025的2.5V。第一级非反相增益11，Rg10k/Rf100k均0.1%，Rf并15pF2% C0G；TMUX1574后放大器域blank选择2.5V，之后2.21k/680pF2%低通及第二级跟随器，100Ω输出阻尼；中央每路499Ω/1nF2%对地滤波后到ADC正端，负端接AGND，保持既有单端接口。

线性模型见evidence/AFE_FREQUENCY_SWEEP.csv，包含给定RC角落；不把它当作真实RX/OPA/线缆/ADC内部滤波模型。2.5V单电源偏置后输入有效动态范围要保留OPA输出余量；C16软件配置建议与既有RTL约定保持±5V/高带宽220kHz/4DOUT，实际转换/配置读回未运行。AFE输出中心2.5V占用单端±5V量程的部分动态范围，需要核查DC偏置处理、饱和及噪声，未擅自切换差分量程或修改RTL。35dB校准验收门限保持，线性RC匹配不能证明35dB。

传感器±30V为输入保护分析的假设故障，不是供应商保证；2×4.99k只限制电流，不能证明上电/掉电内部钳位和反灌安全。当前未加入经完整验证的外部钳位/泄放网络，G3保持REVISE；ADC±21V和OPA±10mA是stress边界，不能宣称正常工作额定或ESD能力。blank在放大器之后有意限制TMUX信号范围0..5V，不能保护第一级过载，恢复时间须测。

中央USB-C UFP3A检测见03；TPS63070强制PWM、1.5uH、Rtop68.7k/Rbottom10k0.1%产生约6.296V。含FB±1%、阻值、漏电及20mV纹波分配得到{p['central_boost_min_v']:.6f}–{p['central_boost_max_v']:.6f}V；最低大于ADP7118的6.09V完整精度条件。ADP5V全温±1.8%给AVCC4.91–5.09V，满足4.75–5.25V静态条件。中央3V3另用TPS54202，从6V3供电。阵列模拟前级则TPS54202 Rtop102k/10k，VFB0.581..0.611传播得到约6.49–6.85V后再ADP5V；不是套用0.6V假精度。两个22uH buck磁件须按实际负载与390k最小频率验证峰值及热。

UADC全部64pin在严格表：AVCC1/37/38/48每pin100nF，VDRIVE23本地100nF；36/39REGCAP分别1uF，42REFIN100nF，44/45相连10uF；AGND2/26/35/40/41/47和REFGND43/46到连续地平面。OS0..2高进入软件模式；PAR/SER高；STBY高、RANGE低、WR低；RESET activehigh默认下拉；CS默认上拉，CONVST/SCLK/SDI默认下拉。DOUTA/B/C/D是pin24/25/27/28，SDI29。其余未用串行数据输出19..22NC，DB0..2/DB12..15按手册串行模式接地。

ADC RevA Table2p9正常1MSPS IAVCCmax50mA、IDRIVEmax1.9mA，分别算，不把1MSPS能力误作软件现有采样率。USB连接器GCTUSB4500-03-0-A16pin，power-only数据触点NC；原厂网页确认5A总VBUS额定，型号不再占位，准确封装/图纸版本待核。连接器48V额定不表示CC/LDO能承受48V。开机瞬态、buckboost效率/纹波/稳定性和USB ESD为G2/G3，未声称电源完整验证。
''')
    write('08_CONNECTOR_SI_GROUND_MECHANICAL_REVIEW.md','''
# 连接器、SI、地和机械审查

候选上/下各64pin信号接口，逐signal交错地，精确配线见08_INTERBOARD_CONNECTIONS.csv；31signal+32地+1NC，不送任何电源。候选从稀疏地线接口改为带独立回流的类型；**64pin器件/键位/电缆MPN及与原机械的兼容性尚未冻结**，这是S3候选普通设计选择，不是已部署兼容性声明。

AX7020J10/J11按现有合约和AX7020_REV3_PROPOSED_PINMAP.csv；2/39/40电源触点在候选中保持NC，1/37/38地连受控信号参考地。中央主机侧9颗SN74AXC8T245按51OUT/10IN分组，2根I2C单独可断开；VCCA/VCCB暂用本地3V3，只在真实VCCO核实后成立。**这种接法没有自动检测AX7020掉电，不能证明主机断电防反灌**。JHOSTEN/JHOSTI2C出厂默认开路/无跳帽；只给离线审查，不可据此声称现场安全。需自动隔离方案或明确受控连线规范并独立批准后才关闭G3。

本地LVC244 Ioff缓冲/33ΩADC源串阻/100ΩAFE输出阻尼是候选；66MHz serializer信号不能用50Hz运动节拍替代。外部STA必须含FPGA输出、中央AXC、线缆flight/skew、阵列LVC244、16路595时钟负载、setup/hold，参考接收最坏阈值和rise/fall。132MHz内部OOC时序不是外部66MHz证明。模拟4RX信号与高速时钟不共享相邻回流瓶颈；电缆阻抗、长度、屏蔽和串扰需IBIS/测量。

三板地平面连续，分区域控制开关/驱动/AFE回流；不制造无依据的AGND/DGND裂缝。DC适配器ClassII浮地，中央USB/PC-UART/AX7020可能形成多条接地回路，必须核查线缆屏蔽/保护地和共模，不虚称不存在环路。TX电流在本地电源回流，不经中央信号地传功率。

08_NOMINAL_TX_GEOMETRY.csv记录几何中心原点、8×8、x/y±42mm、12mm pitch，辐射面z±50mm。90–115mm间距按辐射面定义。RX四角、安装孔、12V插座高度、USB中沉0.8mm、2512热隔离和接插件应力释放仍需真实尺寸/3D布局审查。没有臆造完成PCB布线或DRC；没有Gerber。EPS2–5mm是目标，不是已漂浮证据。
''')
    write('09_SCHEMATIC_NETLIST_ERC_AND_REVIEW.md',f'''
# 原理图/连接表/ERC/审图状态

SCHEMATIC=NATIVE_NOT_CREATED；ERC=NOT_RUN；NATIVE_CAD_CONNECTION=NO_PROCESS_NO_BRIDGE_CLIENT_OBSERVED。工具条件检查见PREFLIGHT.json。按S3允许降级交付严格pin/net表，而非伪装成功导入嘉立创EDA。

netlist/COMPONENTS.csv：{cnt['total_components']}个明确装机位号；PIN_NET.csv：{cnt['pins']}个pin处置；THREE_BOARD_CANDIDATE.json与GENERIC_NETLIST.xml为可解析严格连接候选，XML不是原生EDA项目。未提交无许可证第三方源码。svg/带物理pin/net标签，REVIEW.html可搜索位号/网名/浏览模块；图由规范表生成，独立核查仍以手册和外部Reviewer为准。

SEMANTIC_REVIEW.json：45项最终PASS，板内单端网络0；SAFETY_TRUTH_TABLE.csv：256种布尔状态。结果只证明所列静态关系，不证明类比电路瞬态/布局/制造。曾失败J11_NC检查：检查器把OPEN_DRAIN两根I2C误归未分配电源触点；依据已批准pinmap修正分类，不删除I2C、不放宽电源NC。SEMANTIC_REVIEW_FAILED_01.json保留原失败。前期237项连接合约中包括逻辑TX通道，现只取63实际信号GPIO建立中央缓冲器，防止虚增128条物理接口。

手工审查已覆盖：C16完整64pin及REGCAP/REFCAP、5954used/NC、TC两级非反相和12V域、TPS物理pin/OD/厂设timing、FF pin5非反相Q、TCA RESETpin3与A2pin21、USB OUT2、NC电源、三板BOM数量。所有结论来自当前连接表与原厂资料，**不是独立Reviewer签字**。

Native导入要求：创建正确符号/封装并逐pin对照；先导入电源/安全/TX一通道/AFE一通道、确认复制映射，再全板绘制；运行真实ERC，逐告警记录处理，产生导出网表与本表差异。可沿用当前位号，无需改RTL。完成前G1仍HOLD。

本轮243测试PASS；S2完整帧/综合证据继承，当前未做SPICE、IBIS、外部STA、PCB DRC、硬件验证。没有把45项脚本检查命名成ERC。
''')
    write('10_BOM_RECONCILIATION.md',f'''
# S3实位号BOM对账

旧工作簿1205装机位置（551+551+83+20）是历史候选类别展开，不是S3电路必须凑齐的数量。旧文件保持不变。新候选来自COMPONENTS.csv：UP={cnt['per_board']['UP']}，DN={cnt['per_board']['DN']}，CENTRAL={cnt['per_board']['CENTRAL']}，总{cnt['total_components']}，其中R/C/L实际位号{cnt['passives']}。B-008/B-009各旧2个位置现在0，共四个旧位置退役；TPS3851只增为2实际颗数。新增TPS3430仅窗口功能，TMP302独立过温、锁存/逻辑、NPN电源域、保护和明确去耦均按实际位号计。

温度档细化：TC4427AEOA是同一已批准驱动系列的工业温度候选（−40至85°C），S2商业C档旧BOM保持原样；并非更换驱动架构。

净增加{cnt['total_components']-1205}不能解释为产品硬性需求增加同样数量：S2混合“待分类100k/0Ω”等库存算术与功能位；S3删除无连接的库存式计数，重新展开。两级NPN每阵列128只、其基极/上拉/下拉电阻和每TX330Ω高功率电阻是主要数量差异。它们解决明确的电源域/defaultoff/能量路径问题，但不是已经完成成本/板面积优化。不能因为想回到1205而删除保护。

10_BOM_RELEASE_CANDIDATE_DELTA.csv/.xlsx每组列所有真实refs、数量、值、封装、功能和来源；Components页是每位置一行canonical源。连接器/LED/磁件/熔丝/TVS/测试点/按钮/换能器/所有电源芯片均计入；外部适配器2只和线束属于系统件，在03列明，不偷偷加到PCB装机数。采购SKU级参数、价格、供应商、精确被动器件系列尚未闭环，字段HOLD不会假造库存或价格。

保留的明确缺项：RX完整型号、64pin信号连接器/电缆、USB准确封装、无源器件具体系列及有效C/热降额、融合保护SOA。BOM是RELEASE_CANDIDATE_ONLY / PROCUREMENT_HOLD。还不能称正式BOM release。
''')
    write('HW_SW_HANDOFF.md','''
# PCB-S3给数字/PS/PL任务线的合同；本轮没有修改该实现

1. 每板独立HB，**合格任务完成后才产生下降沿**，正常下降沿19–21ms；上电/错误/未完整commit/未ACK/temperature invalid/safety fail时停止喂狗。自由运行计数器或定时器翻转不合格。高低电平建议10/10ms，不能每20ms仅翻转一次导致40ms下降沿。
2. TPS3430选CWDNC/SET0low/SET1high：保证合法窗口2.22–23.375ms；早于1.48ms必违规；1.48–2.22ms处于容差不确定区不得使用；超31.625ms最迟触发watchdog逻辑，另外叠加未保证的传播和切断/泄放时间。启动忽略170–230ms期间不允许据“未故障”判定已有进度。
3. 完整map/phase/safety/calibration状态/轨迹命令校验+atomiccommit+帧/ACK完成形成progress token；总错误状态、安全锁存、failcapture应阻断token。保留8bit请求/校准分离、35dB、签名capture/ACK、50Hz轨迹、共同timebase。RTL原prepcb_supervisor自由计时HB未改，当前不能联机使能。
4. 安全硬件FAULT独立清锁存+OE+TX功率，PS只观察。人工重使能须电源/温度/进度/配置均合法；不能自动定时重试清除故障。PGOOD只报告本地3V3存在，不等于全部12V/AFE/声学健康；ESTOP_STATUS组合两阵列FAULT_N目前建议健康高，需数字任务线核查health[0]极性。
5. 原63GPIO的RESET/SYNC/FAULT/I2C尚未完整暴露的项照旧开门禁；S3给出端口和物理pin，没有伪称有相应RTL。AXVCCO/外部STA/BRAM异步reset问题保留原问题单。
6. ADC负端保持AGND，既有单端±5V/高带宽方向不变；AFE输出带2.5V偏置须核查既有估计器对DC和饱和的处理。未经正式接口决策不得改为差分或改golden。±5V HBW220kHz不能泛化到±2.5V。读回配置/校准/blank恢复合格才允许正常采集。
''')
    write('11_FINAL_ENGINEERING_REVIEW_AND_REMAINING_GATES.md',f'''
# PCB-S3工程审查与剩余门禁

**PCB-S3结果：REVISE。** 器件连接/可复算候选交付ACCEPT WITH LIMITATIONS；整板电气、原生原理图、独立Review和制造验收未通过。不是模型自我认证。电源推荐已确定，不再要求用户选择功率档。

| 模块 | 结果 | 依据/限制 |
|---|---|---|
| 工作区/版本/保护边界 | ACCEPT WITH LIMITATIONS | v5/独立工作树/原区保留/Draft链未合并 |
| 12V/USB电源选择和静态限流 | ACCEPT WITH LIMITATIONS | 29.36W/12.35W持续设计包络；2mA/20mA分配及阻值传播待真实资格确认 |
| 安全/切断 | REVISE | 45静态检查、256布尔状态；快速故障能量/储能泄放/单故障SOA未保证 |
| 64TX映射 | ACCEPT WITH LIMITATIONS | 128逐通道、双阵列完全对称；真实RLC和全温相位/热未验证 |
| 8AFE/C16 | REVISE | 64pin/RC模型/静态AVCC可审；poweredoff钳位、量程/偏置处理、噪声和35dB未验证 |
| 跨板/AX接口 | REVISE | 电源NC/groundinterleave；自动掉电隔离及真实VCCO/66MHz STA未闭环 |
| 原生CAD/ERC/BOMrelease | REVISE | 严格表/可视审图fallback交付；native NOT_CREATED/ERC NOT_RUN/采购HOLD |

S3-0对账完成；S3-1预算及上下界分层完成候选；S3-2电源选择完成候选；S3-3全TX/安全连接完成候选；S3-4全RX/ADC完成候选但保护/配置有关键门禁；S3-5信号/机械连接完成候选但具体线束和时序未冻结；S3-6按允许fallback交付，原生/ERC未完成；S3-7实位号候选BOM和Draft同步。所有“完成”只指指定候选资产，不表示电气合格。

| Gate | Owner | 可关闭门禁的具体动作 |
|---|---|---|
| G1 原生图纸与独立审查 | PCB/CAD reviewer | 按严格表建立嘉立创EDA原生图、符号/封装逐pin复核、真实ERC+导出差异签核；当前无连接客户端 |
| G2 电源/故障/热资格 | 电源及安全工程 | 确认限流R容差传播与支路分配；源线阻/启动/UVLO/OVLO/电容有效值/热/短路SOA/fastfault最大能量/泄放；先离线模型后受控样机，另获硬件操作授权 |
| G3 AFE和接口电气 | 模拟及接口工程 | 定型RX、外部钳位/掉电隔离；修复主机/阵列I2C反灌；证明自动off或受控连接边界；噪声/blank/增益相位35dB及线束热/ESD |
| G4 真实数字集成/约束 | 主RTL/PS任务线 | 实现progressHB，补63GPIO绑定，核对ADC单端量程/偏置；VCCO/外部STA/BRAM问题闭环，S3不替其改实现 |
| G5 机械/物料最终签核 | PCB机械/物料工程 | 确认NU/RX尺寸及辐射面、64pin连接器/线缆、USB封装、所有无源/保护具体SKU/降额，净表BOM交叉审查；随后再申请制造/采购/main批准 |

当前243测试PASS；S2帧级/综合继承，不是新硬件证据。失败记录、未取到的源、原始资料hash、工作簿公式与静态检查均保留。用户授权只到候选/Draft同步，制造/采购/板写/main仍HOLD。创新性NOVELTY_NOT_CONFIRMED；未复制开源电路冒称原创，S2参考保留为背景。

复核入口：03电源结论、04安全、05TX映射、06AFE、09图纸/ERC、10BOM对账、HW_SW_HANDOFF。当前候选仍有G1–G5，不能进入制造。
''')
    # Pin-labelled electrical sheets: equal labels connect within a board; NC explicitlymarked.
    make_visuals(c,pins)
    print('S3 reports/registry/mating/geometry/AFE model/vector review generated')

def make_visuals(cs,ps):
    folder=R/'svg';folder.mkdir(exist_ok=True);index=[]
    pinmap=defaultdict(list)
    for p in ps:pinmap[p['refdes']].append(p)
    for b in ['UP','DN','CENTRAL']:
        groups=defaultdict(list)
        for c in cs:
            if c['board']!=b:continue
            tail=c['refdes'].split('_',1)[1]
            mt=re.fullmatch(r'(?:QA|QB|RIN|RB1|RC1|RB2|RBD|RC2|RTI|RTX|TX)(\d+)',tail)
            md=re.fullmatch(r'(?:UD|CD|CDX)(\d+)',tail)
            ms=re.fullmatch(r'US(\d+)(?:C)?',tail)
            if mt:group=f'TX_{int(mt[1])//8:02d}'
            elif md:group=f'TX_{int(md[1])//4:02d}'
            elif ms:group=f'TX_{int(ms[1])//2:02d}'
            elif c['function'].startswith('rx_') or c['function'] in ['receiver_amplifier','ultrasound_receiver','analog_bias_reference','rx_blanking']:group='AFE'
            elif c['function'] in ['uv_and_backup_watchdog','early_late_watchdog','independent_thermal_trip','fault_latch','safety_logic','normally_closed_estop','manual_rearm','watchdog_factory_select','heartbeat_idle','fault_pullup','fault_sink_base','kill_enable_divider','debounce','disable_default','open_cable_fault','estop_fault_sink']:group='SAFETY'
            elif c['function'] in ['serializer','control_buffer','signal_connector','array_signal_connector','ax7020_interface','ax_domain_interface','port_default','manual_host_io_enable','manual_host_i2c_isolation','adc','adc_reference','adc_input_filter','adc_digital_series','adc_default','i2c_mux','i2c_pullup','i2c_handoff']:group='IO_ADC'
            else:group='POWER_OTHER'
            groups[group].append(c)
        for group,cc in sorted(groups.items()):
            cols=3;cellw=650;cellh=max(190,max(len(pinmap[c['refdes']]) for c in cc)*16+70);height=100+math.ceil(len(cc)/cols)*cellh
            out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1950" height="{height}" viewBox="0 0 1950 {height}">','<style>text{font:12px monospace;fill:#172a3a}.title{font:bold 22px sans-serif}.net{fill:#176a47}.nc{fill:#b64d18}</style>','<rect width="100%" height="100%" fill="#fff"/>',f'<text x="22" y="35" class="title">v5 PCB-S3 {b} / {group} — PIN / NET REVIEW CANDIDATE</text>','<text x="22" y="65">Equal board-qualified labels are electrically common. NC = unconnected. Not native CAD / ERC NOT RUN.</text>']
            for i,c in enumerate(cc):
                x=20+(i%cols)*cellw;y=90+(i//cols)*cellh;pp=pinmap[c['refdes']];hh=len(pp)*16+50
                out.append(f'<rect x="{x}" y="{y}" width="620" height="{hh}" fill="#f7fafc" stroke="#8da6ba"/>')
                out.append(f'<text x="{x+10}" y="{y+18}" style="font-weight:bold">{html.escape(c["refdes"])}  {html.escape(c["value"])}</text>')
                out.append(f'<text x="{x+10}" y="{y+35}">{html.escape(c["function"])} / {html.escape(c["package"][:67])}</text>')
                for k,p in enumerate(pp):
                    yy=y+52+16*k;cl='nc' if p['disposition']=='INTENTIONAL_NC' else 'net';out.append(f'<line x1="{x+10}" y1="{yy-4}" x2="{x+55}" y2="{yy-4}" stroke="#607587"/><text x="{x+15}" y="{yy-6}">{html.escape(p["pin"])}</text><text x="{x+65}" y="{yy}" class="{cl}">{html.escape(p["net"])}</text>')
            out.append('</svg>');name=f'{b}_{group}.svg';(folder/name).write_text('\n'.join(out),encoding='utf-8');index.append(dict(board=b,module=group,file='svg/'+name,components=len(cc)))
    data=json.dumps(dict(components=cs,pins=ps,sheets=index),ensure_ascii=False).replace('</','<\/')
    page='''<!doctype html><html lang="zh"><meta charset="utf-8"><title>SonoField v5 PCB-S3 审图</title><style>body{font:16px system-ui;margin:24px;color:#17324d;background:#f4f7fb}input,select{font:inherit;padding:8px}table{border-collapse:collapse;background:white;width:100%}td,th{text-align:left;border-bottom:1px solid #ddd;padding:7px}iframe{width:100%;height:70vh;background:white;border:1px solid #bbb}.hold{color:#a53b19}button{padding:8px}</style><h1>SonoField v5 PCB-S3 严格连接候选</h1><p class="hold">REVISE · 原生图纸 NOT_CREATED · ERC NOT_RUN · 制造/采购/板写/main HOLD</p><p>这是带物理 pin/net 标记的矢量审图页。相同板前缀网标电气相连；不表示布局布线完成。每个组件来自规范连接表，不能代替独立审查。</p><select id="sheet"></select><iframe id="diagram" title="Pin net candidate"></iframe><p><input id="query" placeholder="搜索位号 / 器件 / 网名" size="50"><button id="find">检索</button></p><div id="results"></div><script>const D=DATA;const s=document.querySelector('#sheet');for(const x of D.sheets){let o=document.createElement('option');o.value=x.file;o.textContent=x.board+' / '+x.module+' ('+x.components+')';s.append(o)}s.onchange=()=>document.querySelector('#diagram').src=s.value;s.onchange();const esc=v=>String(v).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');document.querySelector('#find').onclick=()=>{const q=document.querySelector('#query').value.trim().toLowerCase();if(!q)return;const hits=D.pins.filter(p=>JSON.stringify(p).toLowerCase().includes(q));document.querySelector('#results').innerHTML='<p>'+hits.length+' matching pins; first200 shown</p><table><tr><th>Refdes</th><th>Pin</th><th>Net</th><th>Disposition</th></tr>'+hits.slice(0,200).map(p=>'<tr>'+[p.refdes,p.pin,p.net,p.disposition].map(v=>'<td>'+esc(v)+'</td>').join('')+'</tr>').join('')+'</table>'};</script></html>'''.replace('DATA',data,1)
    (R/'REVIEW.html').write_text(page,encoding='utf-8');(R/'svg/INDEX.json').write_text(json.dumps(index,indent=2)+'\n')
if __name__=='__main__':main()
