import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';
const root=path.resolve(process.argv[2]);
const inputs=JSON.parse(await fs.readFile(path.join(root,'hardware/prepcb/bom_inputs.json'),'utf8'));
const out=path.join(root,'hardware/bom/working/2026-10-09/prepcb');
const evidence=path.join(root,'evidence/pre_pcb_20261009/bom');
await fs.mkdir(out,{recursive:true});await fs.mkdir(evidence,{recursive:true});
const wb=Workbook.create();
const overview=wb.worksheets.add('Review');
const sheets=['Upper','Lower','Central','External'].map(n=>wb.worksheets.add(n));
overview.showGridLines=false;
overview.getRange('A2:F2').values=[['SonoField v5 pre-PCB BOM',null,null,null,null,null]];
overview.getRange('A4:B11').values=[['Release','HOLD'],['Formal ADC','AD7606BBSTZ-RL'],['TX','NU40C10T'],['RX','MPN REQUIRED'],['Temperature','3 TMP117 required'],['Central power','AX7020 headers; measured budget missing'],['Array sources','2 independent12V5A candidates'],['Manufacturing','NOT_RELEASED; native ERC NOT_RUN']];
overview.getRange('A13:D13').values=[['Board','Installed items','Candidate quantities','Procurement release']];
const headers=['ID','Part / MPN','Package','Installed qty','Suggested spare %','Procurement qty','Supply / rating','Max current A','IO domain','Measured','Package verification','Source URL','Supplier','Approval','Risk / required action','Manufacturer'];
const boardIndices=[0,1,2,4];
for(let b=0;b<sheets.length;b++){
 const s=sheets[b];s.showGridLines=false;
 s.getRange('A2').values=[[s.name+' candidate assembly']];
 s.getRange('A4:P4').values=[headers];
 const items=inputs.items.filter(a=>a.quantities[boardIndices[b]]>0);
 const manufacturer=a=>a.source.includes('ti.com')?'Texas Instruments':a.source.includes('analog.com')?'Analog Devices':a.source.includes('microchip.com')?'Microchip':a.mpn.includes('SHT45')?'Sensirion':'UNKNOWN; vendor evidence required';
 const values=items.map(a=>[a.id,a.mpn,a.package,a.quantities[boardIndices[b]],.10,null,a.supply,a.current_A,a.logic,a.measured,a.package_evidence,a.source,a.supplier,a.approval,a.risk,manufacturer(a)]);
 s.getRange(`A5:P${4+values.length}`).values=values;
 s.getRange(`F5:F${4+values.length}`).formulas=values.map((_,i)=>[`=ROUNDUP(D${5+i}*(1+E${5+i}),0)`]);
 s.getRange(`D5:D${4+values.length}`).setNumberFormat('0');s.getRange(`F5:F${4+values.length}`).setNumberFormat('0');s.getRange(`E5:E${4+values.length}`).setNumberFormat('0%');
 s.getRange(`A2:P${4+values.length}`).format.font={name:'Arial',size:10};
 s.getRange('A2').format.font={name:'Arial',size:14,bold:true};
 s.getRange('A4:P4').format={fill:'#1f4e78',font:{color:'#ffffff',bold:true},rowHeight:34,wrapText:true};
 s.getRange(`A5:P${4+values.length}`).format.rowHeight=52;
 const widths=[12,35,20,12,12,14,50,14,35,18,38,55,32,38,70,38];
 widths.forEach((w,i)=>{s.getRangeByIndexes(0,i,values.length+4,1).format.columnWidth=w;});
 s.getRange(`A5:P${4+values.length}`).format.wrapText=true;
 s.freezePanes.freezeRows(4);s.freezePanes.freezeColumns(2);
 s.tables.add(`A4:P${4+values.length}`,true,`${s.name}Assembly`);
 s.getRange(`J5:J${4+values.length}`).conditionalFormats.add('containsText',{text:'NOT_VERIFIED',format:{fill:'#fff0ce'}});
 overview.getRange(`A${14+b}:D${14+b}`).values=[[s.name,items.length,null,'HOLD']];
 overview.getRange(`C${14+b}`).formulas=[[`=SUM('${s.name}'!D5:D${4+values.length})`]];
}
overview.getRange('A20:D21').values=[['Sensitivity inputs','C_eq nF (hypothetical)','V swing','Frequency Hz'],['Ideal charging only',2,12,40000]];
overview.getRange('A23:B23').values=[['64TX ideal capacitive charging W',null]];
overview.getRange('B23').formulas=[['=64*B21*1E-9*C21^2*D21']];
overview.getRange('A25:B28').values=[['Measured C_eq','UNKNOWN'],['Driver loss / resonance','NOT_INCLUDED'],['5A source vs2A eFuse','Available current NOT_QUALIFIED'],['Central max/startup current','MEASUREMENT_REQUIRED']];
overview.getRange('A2:F28').format.font={name:'Arial',size:10};overview.getRange('A2').format.font={name:'Arial',size:14,bold:true};
overview.getRange('A1:A28').format.columnWidth=38;overview.getRange('B1:B28').format.columnWidth=60;overview.getRange('C1:F28').format.columnWidth=22;
overview.getRange('A13:D13').format={fill:'#1f4e78',font:{color:'#ffffff',bold:true},rowHeight:28};
overview.getRange('B21:D21').format.fill='#fff0ce';overview.getRange('B23').setNumberFormat('0.000');overview.getRange('A4:B11').format.rowHeight=24;
wb.recalculate();
const check=await wb.inspect({kind:'table',range:'Review!A13:D17',include:'values,formulas',maxChars:2500,tableMaxRows:5,tableMaxCols:4});
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!',options:{useRegex:true,maxResults:20},maxChars:2000});
await fs.writeFile(path.join(evidence,'inspection.ndjson'),check.ndjson+'\n'+errors.ndjson);
const original=overview.getRange('B23').values[0][0];overview.getRange('B21').values=[[4]];wb.recalculate();
const changed=overview.getRange('B23').values[0][0];if(Math.abs(changed-2*original)>1e-10)throw Error('Sensitivity formula did not recalculate');
overview.getRange('B21').values=[[2]];wb.recalculate();
for(const s of [overview,...sheets]){
 const preview=await wb.render({sheetName:s.name,range:s.name==='Review'?'A1:D28':'A1:F14',scale:1.5,format:'png'});
 await fs.writeFile(path.join(evidence,s.name+'.png'),new Uint8Array(await preview.arrayBuffer()));
 if(s.name!=='Review'){
  const detail=await wb.render({sheetName:s.name,range:'G1:P14',scale:1,format:'png'});
  await fs.writeFile(path.join(evidence,s.name+'_detail.png'),new Uint8Array(await detail.arrayBuffer()));
 }
}
await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(out,'BOM_AX7020_NU40C10T_PREPCB_WORKING.xlsx'));
console.log(JSON.stringify({status:'EXPORTED',sheets:5,original_W:original,sensitivity_W:changed,source:inputs.source}));
