import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const root=path.resolve(process.argv[2]);
const data=JSON.parse(await fs.readFile(path.join(root,'hardware/design_20261011/BOM_INPUTS.json'),'utf8'));
const output=path.resolve(process.argv[3]);
await fs.mkdir(output,{recursive:true});
const wb=Workbook.create();
const names=['Summary','Central','Upper','Lower','External'];
for(const name of names)wb.worksheets.add(name);
const headers=['ID','器件名称','完整MPN / 待定标记','原厂','装机数','备件率','计划数量','位号','封装 / Pin1 / EP','主要额定 / 用途','电流 A','供电域','原厂资料链接','国内供应商 / 替代','Datasheet版本','检索日期','器件筛选状态','批准来源','未知及证明路径','单价 CNY','装配侧','采购状态'];
const qtyIndex={Central:2,Upper:0,Lower:1,External:4};
for(const name of names.slice(1)){
  const s=wb.worksheets.getItem(name),idx=qtyIndex[name],end=4+data.items.length;
  s.getRange('A2').values=[[`${name} v5 四源供电工作 BOM`]];
  s.getRange('A3').values=[['采购 HOLD；DNP 行装机数为0；聚合无源件需分解定料']];
  s.getRange('A4:V4').values=[headers];
  s.getRange(`A5:V${end}`).values=data.items.map(x=>[x.id,x.description,x.mpn,x.manufacturer,x.quantities[idx],.1,null,
    x.references[name].join(', '),`${x.package}; Pin1/EP原生库待核`,x.supply??'见电源/连接合同',x.current_A??'UNKNOWN',
    name==='Central'?'CENTRAL_USB5V / 3V3':name==='External'?'外部独立电源 / 线束':'LOCAL12V / 5V / 3V3',
    x.source,'授权渠道待选；不默认替代',x.datasheet_revision,x.access_date,x.qualification,x.approval_source,
    x.risk,'UNKNOWN',name==='External'?'外部配件':'背面电子件 / 正面TX RX',x.procurement]);
  s.getRange(`G5:G${end}`).formulas=data.items.map((_,i)=>[`=ROUNDUP(E${i+5}*(1+F${i+5}),0)`]);
  s.getRange(`F5:F${end}`).setNumberFormat('0%');
  s.getRange(`E5:G${end}`).format.horizontalAlignment='right';
  s.getRange(`A4:V${end}`).format.wrapText=true;
  s.getRange(`A5:V${end}`).format.rowHeight=64;
  data.items.forEach((x,i)=>{
    const text=x.references[name].join(', ');
    s.getRange(`A${i+5}:V${i+5}`).format.rowHeight=Math.max(64,Math.ceil(text.length/48)*12);
  });
  const widths=[12,36,46,23,10,10,11,62,50,58,16,32,76,34,28,16,53,65,105,16,32,20];
  widths.forEach((v,i)=>s.getRangeByIndexes(0,i,end+2,1).format.columnWidth=v);
  s.getRange('A4:V4').format={fill:'#244662',font:{color:'#ffffff',bold:true},rowHeight:32,wrapText:true};
  s.getRange(`A${end+2}:D${end+2}`).values=[['装机数量合计',null,null,null]];
  s.getRange(`E${end+2}`).formulas=[[`=SUM(E5:E${end})`]];
  s.freezePanes.freezeRows(4);s.freezePanes.freezeColumns(3);
  s.tables.add(`A4:V${end}`,true,`${name}Parts`);
}
const s=wb.worksheets.getItem('Summary'),end=4+data.items.length;
s.getRange('A2').values=[['SonoField v5 三 PCB 采购审核候选']];
s.getRange('A3').values=[['128 TX / 8 RX / 1 C16 / 3 TMP117；四路独立供电；全部采购 HOLD']];
s.getRange('A4:H4').values=[['ID','完整MPN / 待定标记','上阵列','下阵列','中央','外部','总装机数量','含备件计划']];
s.getRange(`A5:B${end}`).values=data.items.map(x=>[x.id,x.mpn]);
for(let i=0;i<data.items.length;i++){
 const r=i+5;
 s.getRange(`C${r}:H${r}`).formulas=[[`='Upper'!E${r}`,`='Lower'!E${r}`,`='Central'!E${r}`,`='External'!E${r}`,`=SUM(C${r}:F${r})`,`=SUM('Upper'!G${r},'Lower'!G${r},'Central'!G${r},'External'!G${r})`]];
}
s.getRange(`A${end+2}`).values=[['合计']];s.getRange(`C${end+2}:H${end+2}`).formulas=[['C','D','E','F','G','H'].map(c=>`=SUM(${c}5:${c}${end})`)];
[12,59,14,14,14,14,18,20].forEach((v,i)=>s.getRangeByIndexes(0,i,end+2,1).format.columnWidth=v);
s.getRange(`A4:H${end}`).format.wrapText=true;s.getRange(`A5:H${end}`).format.rowHeight=34;
s.getRange('A4:H4').format={fill:'#244662',font:{color:'#ffffff',bold:true},rowHeight:32,wrapText:true};
s.freezePanes.freezeRows(4);s.freezePanes.freezeColumns(2);s.tables.add(`A4:H${end}`,true,'SystemParts');
for(const sheet of wb.worksheets.items){sheet.showGridLines=false;sheet.getRange(`A1:V${end+2}`).format.font={name:'Arial',size:10};sheet.getRange('A2').format.font={name:'Arial',size:14,bold:true};}
wb.recalculate();
const counts=['Upper','Lower','Central','External'].map(n=>data.items.reduce((total,x)=>total+x.quantities[qtyIndex[n]],0));
const cached=s.getRange(`C${end+2}:F${end+2}`).values[0];
if(cached.some((v,i)=>v!==counts[i]))throw Error('Independent numeric counts disagree');
const check=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!',options:{useRegex:true,maxResults:20},maxChars:2000});
await fs.writeFile(path.join(output,'formula_inspection.ndjson'),check.ndjson);
for(const name of names){
 const preview=await wb.render({sheetName:name,range:name==='Summary'?'A1:H12':'A1:G12',scale:1.25,format:'png'});
 await fs.writeFile(path.join(output,`${name}.png`),new Uint8Array(await preview.arrayBuffer()));
}
const file=path.join(output,'BOM_V5_FOUR_SOURCE_20261011.xlsx');
await(await SpreadsheetFile.exportXlsx(wb)).save(file);
await fs.writeFile(path.join(output,'BOM_QUANTITY_VERIFICATION.json'),JSON.stringify({status:'PASS',part_types:data.items.length,installed:counts,sheet_order:names,source:'Artifact formulas vs separate JS quantity reduction',prices:'UNKNOWN',procurement:'HOLD'},null,2)+'\n');
console.log(JSON.stringify({status:'EXPORTED',file,counts,part_types:data.items.length}));
