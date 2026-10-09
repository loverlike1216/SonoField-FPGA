// GPT-6.1 Sol High (user-declared); working candidate only.
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const {FileBlob,SpreadsheetFile}=await import(process.env.ARTIFACT_TOOL_MODULE ? pathToFileURL(process.env.ARTIFACT_TOOL_MODULE).href : '@oai/artifact-tool');
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const out=path.join(root,'v5/hardware/bom/working/2026-10-09');
await fs.mkdir(out+'/preview',{recursive:true});
const source=path.join(root,'v5/hardware/bom/submissions/2026-10-08/BOM_AX7020_NU40C10T_2026-10-08.xlsx');
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(source));
const s=wb.worksheets.getItem('新版BOM'),changes=[];
function edit(sheet,cell,value,why){const x=wb.worksheets.getItem(sheet).getRange(cell);changes.push({sheet,cell,before:x.values[0][0],after:value,reason:why});x.values=[[value]];}
const put=(cell,value,why)=>edit('新版BOM',cell,value,why);
put('G33','LFCSP-6 / CP-6-3 (EP=GND)','ADI Rev H ordering table: exact ACPZN model has six pins');
put('U33','Pin1 VOUT,2 SENSE/ADJ,3 GND,4 EN,5 SS,6 VIN; exposed pad GND. CAD pad geometry still requires library audit.','Exact LFCSP6 pin map');
put('E18','AD7606C-16BSTZ-RL (推荐候选)','P-20261008-001 recommendation; formal selection still pending user/independent review');
put('F18','8×16bit同步；软件模式0x07=0xFF，220kHz；四DOUT；保留既有采样节奏','High bandwidth requires register write and readback');
put('P18','候选；待独立Review与用户批准','Not a formal ADC substitution');
put('R18','现有AD7606B初始化不能直接沿用；需隔离适配及带宽读回/实际相位测量','Pin compatibility alone does not prove protocol compatibility');
put('T18','https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf','Primary manufacturer source');
put('U18','原件为AD7606BBSTZ-RL；数字核心未改；候选ROM/模型单独保存，不能声称实板采样通过','Preserve traceable baseline');
put('H9',4,'21 nonclock outputs plus2 returns require7 four-bit direction groups per array');
put('I9',4,'Each AXC has2 direction groups;4 devices candidate, not automatic manufacturing approval');
put('N9',12,'10 candidate installed plus2 spare');
put('P9','数量候选：4+4+2；电平/VCCO待核验','Explicit group allocation');
put('U9','每阵列6组输出+1组返回；2路时钟另走LVC244。中央ADC5出5入分四组；I2C不得走推挽AXC。','Keep32-lane architecture');
for(const row of [19,20]){for(const col of ['H','I','J','K','L','N'])put(col+row,0,'Composite design group is not a purchasable line; actual passives remain in dedicated rows');put('P'+row,'非采购设计组；见无源分配','Prevent double counting');}
put('U19','8个ADC输入各47Ω与1nF在B-053/B-058计数；不能再采购RC套件。','Explicit passive ownership');
put('U20','ADC REFIN10µF×1、REFCAPA/B共10µF×1、REGCAP1µF×2；从B-049/B-047分配，独立去耦另行核算。','Separate ADC reference/bypass nets');
for(const row of [21,42,75,50,60])put('K'+row,0,'Remote environment board optional DNP, not compulsory fourth board');
for(const row of [21,42,75])put('P'+row,'可选DNP；不纳入三块主板装机','Current formal user instruction');
put('F27','SMBJ20A候选撤销释放；32.4V钳位高于eFuse28V abs max','Surge coordination cannot be fixed by package correction');
put('P27','阻塞；保护网络待浪涌条件核算','Do not invent safe replacement TVS');
put('U27','不能仅改低VRWM就放行；要验证Ipp、源阻抗、寄生、响应及TC4427A电压限制。','Worst-case protection review');
put('F66','1.65kΩ→约2.02A标称；不是5.5A','Datasheet ILIM≈3334/RILIM');
put('U66','保持候选2A档；电阻/IC容差、启动浪涌及新增TX切断级协调待测。','No automatic current increase');
put('F26','20mΩ：INA226电流测量满量程约±4.096A','81.92mV /20mohm');
put('U67','1.37M仅为上臂；下臂/OVLO公式与容差未冻结，不能作为已闭合保护。','No guessed OVLO configuration');
put('U68','Rtop590k/Rbottom100k、VFB0.8V→5.52V；LDO最大dropout420mV@200mA，余量需含buck公差/纹波。','Document full calculation');
put('U44','上/下独立保护支路必需；另给中央AUX供电，源端星形分配；AX7020原厂5V独立。','Third branch and ground policy');
edit('使用说明','A3','2026-10-09 工作修订候选 | 原始提交保留 | 三块必需PCB | 制造/采购释放HOLD','Separate source from working revision');
edit('使用说明','B15','原始提交：submissions/2026-10-08；本文件为工作候选，不替换继承BOM_MASTER','Original preserved');
edit('板级供电','G6','候选：OE+输入偏置+独立TX电源切断+锁存重新使能；实物未测','No unsupported safety assertion');
edit('板级供电','G7','候选：同上，下板独立；失电恢复不自动重启','Independent fail-safe');
edit('板级供电','D8','同步ADC候选AD7606C-16；正式选型待批','Recommendation not release');
edit('接口与网表','A9','UP_OE_N / DN_OE_N','Align active-low naming');
edit('接口与网表','A10','UP_RESET_N / DN_RESET_N','595 clear active low');
edit('接口与网表','A11','UP_RX_BLANK / DN_RX_BLANK','Canonical net names');
edit('接口与网表','A16','MON_I2C_SCL / MON_I2C_SDA','Shared status bus, not obligatory environment board');
edit('接口与网表','F16','3×INA226+3×TMP117；环境传感器可选','Do not remove monitoring');
edit('接口与网表','C17','63 / 68候选，余5；另见80针表','Complete signal budget includesSYNC andESTOP');
edit('接口与网表','H17','V2.0官方映射，Vivado器件库核验；Rev3.0实板连通/VCCO仍未核验','Not productionXDC');
const src=wb.worksheets.getItem('数据来源');
src.getRange('A3:D3').values=[['器件/依据','原厂URL','读取依据','边界']];
const refs=[
 ['AD7606C-16','https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf','Rev A p67 BANDWIDTH=0x07','220kHz需软件模式；推荐未批准'],
 ['AD7606B','https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606b.pdf','Rev B analog LPF','采样率不能代替40kHz模拟带宽'],
 ['ADP7118','https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf','Rev H p6/p22','ACPZN5.0 CP-6-3六引脚'],
 ['TPS25947','https://www.ti.com/lit/ds/symlink/tps25947.pdf','Rev C 电气/ILIM/引脚表','28V abs；FLT不是PGOOD'],
 ['SN74AXC8T245','https://www.ti.com/lit/ds/symlink/sn74axc8t245.pdf','Rev C 两个四位DIR组','I2C另用开漏隔离；VCC≤3.6V'],
 ['SN74LVC595A','https://www.ti.com/lit/ds/symlink/sn74lvc595a.pdf','Rev A 3.3V时序','104MHz器件规格不等于66MHz外部链路通过'],
 ['ALINX AX7020','https://github.com/alinxalinx/AX7020_2023.1/tree/fcf1e4a239b0f47e8ee95dfde7c2eedc5685c327','官方手册/原理图/hello XSA','实板Rev3.0；文件V2.0；DDR预设料号有差异'],
 ['INA226','https://www.ti.com/lit/ds/symlink/ina226.pdf','±81.92mV','20mΩ→4.096A量程'],
 ['NU40C10T/RX','用户供应商原件待提供','SOURCE_MISSING','不套用16mm额定参数'],
];src.getRange('A4:D12').values=refs;
const gates=wb.worksheets.getItem('变化与质量门禁');gates.getRange('A4:G18').clear({applyTo:'contents'});
gates.getRange('A4:G4').values=[['问题','处理','证据','当前状态','解除条件','硬件状态','放行']];
const issues=[
 ['P0-01 ADC','C-16软件高带宽候选','ADC_CANDIDATE_REVIEW.md','已提出可验证方案','独立Review+用户批准+实测','NOT_RUN','HOLD'],
 ['P0-02安全','本地门禁+锁存rearm+TX切断候选','SAFETY_AND_POWER.md','已提出可验证方案','门级/掉电/热/断线示波器测试','NOT_RUN','HOLD'],
 ['P0-03浪涌','SMBJ20A未释放；核算真实surge','SAFETY_AND_POWER.md','仍然阻塞','浪涌条件/容差/响应/器件选定','NOT_RUN','HOLD'],
 ['P1-04封装','ADP7118改为LFCSP6','ADI RevH p6/p22','已解决：文本封装','EDA焊盘/Pin1/EP仍需审查','NOT_RUN','HOLD'],
 ['P1-05 T/R','保持NU40C10T；RX未知','供应商规格与样品缺失','仍然阻塞','完整型号/尺寸/C/频响/连续驱动','NOT_RUN','HOLD'],
 ['P1-06链路','维持32lane；分开内外时序','TIMING_BUDGET.md','已提出可验证方案','外部min/max及线束实测','NOT_RUN','HOLD'],
 ['P1-07 IO','63/68；AXC4+4+2候选','connector_pinmap_candidate.csv','已提出可验证方案','Rev3/VCCO/开漏隔离/连接器核验','NOT_RUN','HOLD'],
 ['P1-08功耗','2A/4.096A/200mA及动态参数扫描','candidate_checks.json','已提出可验证方案','1–4路负载/热/电容测量','NOT_RUN','HOLD'],
 ['P2-09 BOM','保留原件、补源、复合行去重复','changes.json','已提出可验证方案','精确料号/位号/原生网表对账','NOT_RUN','HOLD'],
];gates.getRange('A5:G13').values=issues;
const additions=wb.worksheets.add('新增候选与无源分配');
additions.getRange('A1:G1').values=[['类别','候选器件/网络','每上板','每下板','中央','总量','审批/验证边界']];
additions.getRange('A2:G9').values=[
 ['TX电源切断','第二级TPS259470LRPWR',1,1,0,2,'新增候选；原输入eFuse保持，避免本地逻辑供电自锁死；协调未冻结'],
 ['锁存重新使能','SN74LVC1G74DCTR',3,3,0,6,'READY/ARMED/TX_SEEN功能候选；门级/脉冲/时序待独立审核'],
 ['硬件门逻辑','SN74LVC1G08/1G32/1G04/1G11',null,null,0,null,'需由完整原生门级网络导出数量，不虚填'],
 ['电源监控','TPS3808G01DBVR/TPS3700DDCR',null,null,null,null,'本地3.3V/5V/VDRV窗口阈值与延时未冻结'],
 ['开漏总线隔离','TCA4307DGKR',0,0,3,3,'AX→中央、中央→UP/DN三个独立域；原厂时序/掉电资格待验证'],
 ['driver输入下拉','10kΩ 1% 每驱动输入一颗',64,64,0,128,'候选新增：替代原100k相应分配，不能与旧模糊总数相加采购'],
 ['ADC REGCAP','1µF×2',0,0,2,2,'分配自B-047；每个REGCAP单独到AGND'],
 ['ADC参考旁路','REFIN10µF、REFCAPA/B共10µF',0,0,2,2,'分配自B-049；不能用RX_REF2V5代替ADC内参考'],
];
for(const row of [2,3,6,7,8,9])additions.getRange('F'+row).formulas=[[`=SUM(C${row}:E${row})`]];
for(const sh of [src,additions]){const used=sh.getUsedRange();used.format.font={name:'Arial',size:11};used.format.verticalAlignment='center';used.format.wrapText=true;used.format.rowHeight=48;sh.getRange('A:A').format.columnWidth=22;sh.getRange('B:B').format.columnWidth=68;}
src.getRange('C:D').format.columnWidth=45;src.getRange('A3:D3').format={fill:'#17365D',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:28};
additions.getRange('C:F').format.columnWidth=13;additions.getRange('G:G').format.columnWidth=75;additions.getRange('A1:G1').format={fill:'#17365D',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:28};
wb.recalculate();
for(const [sheet,range,name] of [['新版BOM','D31:G34','package'],['变化与质量门禁','A4:G13','gates'],['数据来源','A3:D12','sources'],['新增候选与无源分配','A1:G9','additions']]){const p=await wb.render({sheetName:sheet,range,scale:1,format:'png'});await fs.writeFile(out+'/preview/'+name+'.png',new Uint8Array(await p.arrayBuffer()));}
const inspection=await wb.inspect({kind:'region',sheetId:'新版BOM',range:'H5:N76',maxChars:1800,tableMaxRows:4});
await fs.writeFile(out+'/artifact_inspection.ndjson',inspection.ndjson+'\n');
const x=await SpreadsheetFile.exportXlsx(wb);await x.save(out+'/BOM_AX7020_NU40C10T_WORKING_2026-10-09.xlsx');
await fs.writeFile(out+'/changes.json',JSON.stringify({classification:'WORKING_CANDIDATE_NOT_PROCUREMENT_RELEASE',original_sha256:crypto.createHash('sha256').update(await fs.readFile(source)).digest('hex'),changes,added_sheets:['新增候选与无源分配'],sources:refs,issues},null,2)+'\n');
console.log(JSON.stringify({status:'EXPORTED',edits:changes.length,output:out}));
