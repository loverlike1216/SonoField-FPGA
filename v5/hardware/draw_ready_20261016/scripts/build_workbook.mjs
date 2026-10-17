import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';
const root=path.resolve(import.meta.dirname,'..');
const d=JSON.parse(await fs.readFile(path.join(root,'results/FINAL_CONNECTION_DATABASE.json'),'utf8'));
d.array=JSON.parse(await fs.readFile(path.join(root,'results/ARRAY_EXPANDED_FINAL.json'),'utf8'));
const wb=Workbook.create();
const specs=[
 ['BOM',d.bom,['id','mpn','manufacturer','package','value','central_quantity','array_quantity','array_board_count','system_quantity','rating','lcsc','price','stock','procurement_status','source_url','role','substitution','references'],['ID','精确MPN','制造商','封装','值','中央板×1','单阵列板','阵列板数量','全系统数量','规格/额定','立创编号','价格','库存','采购状态','原厂/用户证据','用途','替代条件','全部位号']],
 ['FPGA接口',d.fpga,['connector','pin','ball','bank','net','rtl_port','direction','level','xdc_status','cable'],['接口','针号','FPGA球号','Bank','中央端网络','RTL逻辑端口','方向','电平条件','XDC状态','线缆要求']],
 ['阵列接口',d.array,['board','pin','signal','central_net','array_net','direction','safe_default','domain','cable'],['实体板','物理针','信号','中央网络','通用阵列','方向','安全默认态','电气域','线缆要求']],
 ['器件引脚',d.pins,['board','refdes','mpn','pin','function','net','kind','status','source'],['实体板','位号','精确MPN','物理脚','功能','本地网络','电气类型','审核状态','依据']],
 ['无源连接',d.passives,['board','refdes','mpn','value','pin1_net','pin2_net','package','rating','role','polarity','source_url'],['实体板','位号','精确MPN','数值','端点1网络','端点2网络','封装','规格额定','用途','极性','证据']],
 ['外部配件',JSON.parse(await fs.readFile(path.join(root,'results/EXTERNAL_BOM.json'),'utf8')),['mpn','manufacturer','quantity','rating','role','status','source_url'],['建议型号','制造商','数量','规格','用途','审核状态','依据']]
];
specs[0][2].push('quote_source','quote_time','quote_basis');
specs[0][3].push('报价来源','报价时间UTC','阶梯/快照说明');
for(const [name,rows,keys,headers]of specs){
 const s=wb.worksheets.add(name);s.showGridLines=false;
 s.getRange('A2').values=[[name==='BOM'?'SonoField-FPGA v5 原理图前完整候选BOM':`SonoField-FPGA v5 ${name}`]];
 s.getRange('A2').format.font={name:'Arial',size:14,bold:true};
 s.getRange('A3').values=[[name==='BOM'?'中央板×1＋阵列板×2；12V→10V；128/256MHz生产配置；理论候选，实物未验证':'网络名以实体板为作用域；NC明确隔离；详见02完整指南；PASS仅表示对应记录审查范围']];
 const vals=[headers,...rows.map(r=>keys.map(k=>k==='value'&&r[k]==='IC/connector/transducer'?'—':['pin','central_quantity','array_quantity','array_board_count','system_quantity','quantity'].includes(k)&&String(r[k]).match(/^\d+$/)?Number(r[k]):r[k]??''))];
 const area=s.getRangeByIndexes(4,0,vals.length,keys.length);area.values=vals;area.format.font={name:'Arial',size:10};area.format.rowHeight=23;area.format.verticalAlignment='center';area.format.columnWidth=22;
 s.getRangeByIndexes(4,0,1,keys.length).format={fill:'#24364B',font:{name:'Arial',bold:true,color:'#FFFFFF',size:10},rowHeight:28,horizontalAlignment:'center'};
 s.freezePanes.freezeRows(5);s.freezePanes.freezeColumns(name==='BOM'?2:2);
 const widths=name==='BOM'?[9,30,36,30,15,13,13,13,14,75,15,15,15,45,78,45,78,100]:name==='器件引脚'?[12,25,30,12,25,30,18,14,70]:name==='无源连接'?[12,25,30,15,30,30,25,68,44,22,80]:name==='FPGA接口'?[12,10,14,12,30,37,20,68,55,76]:name==='阵列接口'?[12,22,30,30,25,35,60,20,75]:[36,25,12,65,75,65,90];
 if(name==='BOM')widths.push(90,65,80);
 widths.forEach((w,i)=>{s.getRangeByIndexes(4,i,vals.length,1).format.columnWidth=w;});
 if(name==='BOM'){
  s.getRange(`D6:D${rows.length+5}`).setNumberFormat('@');s.getRange(`D6:D${rows.length+5}`).format.wrapText=true;
  rows.forEach((r,i)=>{if(/^\d{4}$/.test(r.package))s.getRange(`D${i+6}`).setNumberFormat('0000');});
 for(let i=0;i<rows.length;i++)s.getRange(`I${i+6}`).formulas=[[`=F${i+6}+G${i+6}*H${i+6}`]];
  s.getRange(`F6:I${rows.length+5}`).setNumberFormat('0');
  s.getRange(`L6:L${rows.length+5}`).setNumberFormat('0.0000');
  s.getRange('L5').values=[['价格USD/件']];
  s.getRange(`F${rows.length+7}:H${rows.length+7}`).values=[['全系统安装器件数',null,null]];
  s.getRange(`I${rows.length+7}`).formulas=[[`=SUM(I6:I${rows.length+5})`]];
  s.getRange(`F${rows.length+8}:H${rows.length+8}`).values=[['含外部配件请参见独立配件页',null,null]];
 }
 // Keep wrapping bounded to long fields, with generous but fitted row heights.
 if(name==='BOM'){
  s.getRange(`J6:J${rows.length+5}`).format.wrapText=true;
  s.getRangeByIndexes(5,0,rows.length,keys.length).format.rowHeight=48;
 }
 if(name==='外部配件'){
  s.getRangeByIndexes(5,0,rows.length,keys.length).format.wrapText=true;
  s.getRangeByIndexes(5,0,rows.length,keys.length).format.rowHeight=72;
 }
 const statusCol=keys.indexOf('status');
 if(statusCol>=0)s.getRangeByIndexes(5,statusCol,rows.length,1).conditionalFormats.add('containsText',{text:'HOLD',format:{fill:'#FFF0CB',font:{color:'#7C4A00'}}});
}
const bomSheet=wb.worksheets.getItem('BOM');
const oldQty=bomSheet.getRange('F6').values[0][0];
bomSheet.getRange('F6').values=[[oldQty+1]];wb.recalculate();
const changedQty=bomSheet.getRange('I6').values[0][0];
if(changedQty!==Number(d.bom[0].system_quantity)+1)throw new Error('Quantity formula did not recalculate');
bomSheet.getRange('F6').values=[[oldQty]];
wb.recalculate();
await fs.writeFile(path.join(root,'results/WORKBOOK_RECALC_TEST.json'),JSON.stringify({test:'increment central quantity then restore',observedChangedSystemQty:changedQty,restoredCentralQty:oldQty,status:'PASS'}));
const inspections=[];
inspections.push((await wb.inspect({kind:'table',range:'BOM!A5:K12',include:'values,formulas',tableMaxRows:8,tableMaxCols:11,maxChars:6500})).ndjson);
inspections.push((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50},maxChars:2000})).ndjson);
await fs.writeFile(path.join(root,'logs/workbook_inspection.ndjson'),inspections.join('\n'));
for(const[name]of specs){
 const preview=await wb.render({sheetName:name,range:name==='BOM'?'A1:J12':'A1:F12',scale:1.3,format:'png'});await fs.writeFile(path.join(root,'results',`revision_preview_${name}.png`),new Uint8Array(await preview.arrayBuffer()));
}
const changedRow=d.bom.findIndex(x=>x.mpn==='SN74LVC8T245PWR')+6;
for (const [sheetName,range,label] of [['BOM',`A${changedRow}:K${changedRow+5}`,'changed_components'],['FPGA接口','A75:J85','J11_endpins']]){
 const preview=await wb.render({sheetName,range,scale:1.3,format:'png'});await fs.writeFile(path.join(root,'results',`revision_preview_${label}.png`),new Uint8Array(await preview.arrayBuffer()));
}
const xlsx=await SpreadsheetFile.exportXlsx(wb);await xlsx.save(path.join(root,'01_COMPLETE_BOM.xlsx'));
console.log(JSON.stringify({output:path.join(root,'01_COMPLETE_BOM.xlsx'),sheets:specs.length,bomRows:d.bom.length,installedComponents:d.instances.length}));
