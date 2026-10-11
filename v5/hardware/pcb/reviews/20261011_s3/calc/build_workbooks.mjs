// Run from worktree: copy this file into v5/build/pcb_s3_artifacts/ and run node there.
// The build directory node_modules junction points to the bundled @oai/artifact-tool.
import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';
const root=process.cwd();
const r=path.join(root,'v5/hardware/pcb/reviews/20261011_s3');
const e=path.join(root,'v5/evidence/pcb_s3_20261011');
const d=JSON.parse(await fs.readFile(path.join(r,'calc/workbook_data.json'),'utf8'));
const x=JSON.parse(await fs.readFile(path.join(r,'calc/inputs.json'),'utf8'));
const model=JSON.parse(await fs.readFile(path.join(r,'netlist/THREE_BOARD_CANDIDATE.json'),'utf8'));
const col=n=>{let s='';for(n++;n;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;};
function style(sh,n,m,headerRow=4){
  sh.showGridLines=false;
  sh.getRange(`A1:${col(m-1)}${n}`).format.font={name:'Arial',size:10};
  sh.getRange(`A1:${col(m-1)}${n}`).format.verticalAlignment='center';
  sh.getRange(`A${headerRow}:${col(m-1)}${headerRow}`).format={fill:'#203D59',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},rowHeight:28,wrapText:true};
  sh.getRange(`A5:${col(m-1)}${n}`).format.rowHeight=24;
  sh.getRange(`A1:${col(m-1)}${n}`).format.columnWidth=19;
  sh.getRange('A2').format.font={name:'Arial',size:14,bold:true};
  sh.freezePanes.freezeRows(headerRow);
}
function components(wb){
 const s=wb.worksheets.add('Components');
 s.getRange('A2').values=[['Actual installed positions — candidate only']];
 s.getRange('A4:H4').values=[['Board','Refdes','MPN','Value','Package','Function','Status','Source URL']];
 s.getRange(`A5:H${model.components.length+4}`).values=model.components.map(c=>[c.board,c.refdes,c.mpn,c.value,c.package,c.function,c.procurement,c.source_url]);
 style(s,model.components.length+4,8);s.getRange('B:B').format.columnWidth=29;s.getRange('C:C').format.columnWidth=30;s.getRange('E:F').format.columnWidth=43;s.getRange('H:H').format.columnWidth=90;
 return s;
}
const wb=Workbook.create();const summary=wb.worksheets.add('Decision');const ins=wb.worksheets.add('Inputs');const loads=wb.worksheets.add('Loads');components(wb);
const entries=Object.entries(x);const addr={};
ins.getRange('A2').values=[['Inputs and evidence classes']];ins.getRange('A4:D4').values=[['Parameter','Value','Class','Source / boundary']];
ins.getRange(`A5:D${entries.length+4}`).values=entries.map(([k,v],i)=>{addr[k]=`Inputs!$B$${i+5}`;return[k,v,k.includes('c0')?'ASSUMPTION':k.includes('ilim_table9')?'DATASHEET_TABLE9':typeof v==='number'?'DESIGN_INPUT':'BOUNDARY',k.includes('ilim')?'TI TPS25947 RevC Table9; tolerance propagation in Python':k.includes('usb')?'Installation envelope, not present compliance certification':'calc/inputs.json / reports03-06'];});
style(ins,entries.length+4,4);ins.getRange('A:A').format.columnWidth=42;ins.getRange('B:B').format.columnWidth=22;ins.getRange('D:D').format.columnWidth=100;ins.getRange(`B5:B${entries.length+4}`).format.fill='#FFF2CC';
summary.getRange('A2').values=[['v5 PCB-S3 — power selection']];summary.getRange('A3').values=[['Continuous input-limit envelope; fast-fault energy NOT GUARANTEED']];
summary.getRange('A4:J4').values=[['Board','V max (V)','Limit min (A)','Limit max (A)','Input max (A)','Input max (W)','Supply (A)','Nominal (W)','Margin (A)','Decision']];
for(let i=0;i<3;i++){
 const row=i+5,b=['CENTRAL','UP','DN'][i];summary.getRange(`A${row}`).values=[[b]];
 summary.getRange(`B${row}:I${row}`).formulas=[[
  `=${addr[i===0?'usb_v_max':'array_v_max']}`,
  `=${addr.ilim_table9_min_a}/(1+${addr.rilim_tolerance})`,
  `=${addr.ilim_table9_max_a}/(1-${addr.rilim_tolerance})`,
  `=D${row}+${addr.upstream_allowance_a}${i===0?'+'+addr.central_bootstrap_allowance_a:''}`,
  `=B${row}*E${row}`,`=${addr.adapter_a}`,i===0?'=5*3':`=${addr.adapter_w}`,`=G${row}-E${row}`]];
 summary.getRange(`J${row}`).values=[[i===0?'5V/3A USB-C':'12V/3A GST36E12']];
}
summary.getRange('A10').values=[['REVISE — manufacturing / procurement / hardware writes / main HOLD']];
summary.getRange('A12:C17').values=[['Other result','Value','Boundary'],['TX64 simultaneous edge (A)',d.results.tx_all_edges_peak_a,'C0 / resistor model only'],['One short resistor heat (W)',d.results.tx_one_short_continuous_w,'100% duty,13.2V,Rmin'],['TX stored energy (J)',d.results.tx_stored_energy_max_j,'Total C<=750uF assumption'],['Bleed to1V (s)',d.results.tx_bleed_time_to_1v_s,'Passive RC;not instant off'],['ADC AVCC static (V)','4.91–5.09','LDO condition met;transients unverified']];
style(summary,17,10);summary.getRange('A:A').format.columnWidth=37;summary.getRange('B:I').format.columnWidth=16;summary.getRange('J:J').format.columnWidth=30;summary.getRange('B5:I7').setNumberFormat('0.0000');summary.getRange('A10:J10').format.font={name:'Arial',size:10,bold:true,color:'#9C3C19'};summary.tabColor='#203D59';summary.freezePanes.unfreeze();summary.getRange('C12:C17').format.columnWidth=32;
loads.getRange('A2').values=[['Device / function loads — UNKNOWN is not zero']];loads.getRange('A3').values=[['Rows allocate components once; numerical power is only the specified current mode. See Components for all refs.']];
loads.getRange('A4:K4').values=[['Board','Rail','Device / function','Qty','I typ (A)','I max (A)','V rail (V)','Allocated P (W)','Evidence class','Source URL','Qualification']];
loads.getRange(`A5:K${d.budget.length+4}`).values=d.budget.map(b=>[b.Board,b.Rail,b.Device_function,b.Qty,b.I_typ_A??null,b.I_max_continuous_A??null,b.Vrail_for_power,null,b.classification,b.source_URL,b.open_qualification]);
for(let i=0;i<d.budget.length;i++){const row=i+5;const extra=d.budget[i].Device_function.startsWith('AD7606C-16')?`+D${row}*3.42*0.0019`:'';loads.getRange(`H${row}`).formulas=[[`=IF(ISNUMBER(F${row}),D${row}*F${row}*G${row}${extra},"UNKNOWN")`]];}
style(loads,d.budget.length+4,11);loads.getRange('C:C').format.columnWidth=60;loads.getRange('I:K').format.columnWidth=70;loads.getRange('E5:H'+(d.budget.length+4)).setNumberFormat('0.000000');
wb.recalculate();
const inspect1=await wb.inspect({kind:'region',sheetId:'Decision',range:'A4:J7',maxChars:3500,tableMaxCols:10,tableMaxRows:5});
await fs.writeFile(path.join(e,'WORKBOOK_POWER_INSPECT.json'),JSON.stringify(inspect1,null,2));
await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(r,'02_THREE_BOARD_POWER_BUDGET.xlsx'));
const preview=await wb.render({sheetName:'Decision',range:'A1:J10',scale:1.3,format:'png'});await fs.writeFile(path.join(e,'POWER_PREVIEW.png'),new Uint8Array(await preview.arrayBuffer()));
const bw=Workbook.create();const bs=bw.worksheets.add('BOM Summary');const bg=bw.worksheets.add('BOM Groups');components(bw);
bs.getRange('A2').values=[['PCB-S3 BOM — release candidate only']];bs.getRange('A3').values=[['Procurement HOLD. External adapters and cables are system items in report03.']];
bs.getRange('A4:D4').values=[['Board','Installed positions','Legacy baseline','Difference']];
for(let i=0;i<3;i++){let row=i+5;bs.getRange(`A${row}`).values=[[['UP','DN','CENTRAL'][i]]];bs.getRange(`B${row}`).formulas=[[`=COUNTIF(Components!$A$5:$A$${model.components.length+4},A${row})`]];bs.getRange(`C${row}`).values=[[[551,551,83][i]]];bs.getRange(`D${row}`).formulas=[[`=B${row}-C${row}`]];}
bs.getRange('A8:D8').values=[['Legacy system items',0,20,-20]];
bs.getRange('A9').values=[['Total']];bs.getRange('B9:D9').formulas=[['=SUM(B5:B8)','=SUM(C5:C8)','=B9-C9']];
bs.getRange('A12:C16').values=[['Boundary','Value','Action'],['TPS3851 count',2,'one perarray'],['B-008 / B-009 retired',0,'oldfour installedpositions removed'],['Native/ERC','NOT_CREATED / NOT_RUN','create CAD and external review'],['Remaining MPN/thermal gates','G1–G5','see report11']];
style(bs,16,4);bs.getRange('A:A').format.columnWidth=43;bs.getRange('B:D').format.columnWidth=28;bs.getRange('C:C').format.columnWidth=48;bs.tabColor='#203D59';bs.freezePanes.unfreeze();
bg.getRange('A2').values=[['Actual component groups — all refs in Components']];bg.getRange('A4:H4').values=[['Board','MPN','Value','Package','Function','Quantity','Status','Source URL']];
bg.getRange(`A5:H${d.bom.length+4}`).values=d.bom.map(b=>[b.board,b.mpn,b.value,b.package,b.function,null,b.status,b.source_url]);
for(let i=0;i<d.bom.length;i++){let row=i+5,end=model.components.length+4;bg.getRange(`F${row}`).formulas=[[`=COUNTIFS(Components!$A$5:$A$${end},A${row},Components!$C$5:$C$${end},B${row},Components!$D$5:$D$${end},C${row},Components!$E$5:$E$${end},D${row},Components!$F$5:$F$${end},E${row})`]];}
style(bg,d.bom.length+4,8);bg.getRange('B:E').format.columnWidth=44;bg.getRange('G:H').format.columnWidth=75;
bw.recalculate();
const inspect2=await bw.inspect({kind:'region',sheetId:'BOM Summary',range:'A4:D9',maxChars:3000,tableMaxCols:4,tableMaxRows:6});await fs.writeFile(path.join(e,'WORKBOOK_BOM_INSPECT.json'),JSON.stringify(inspect2,null,2));
await (await SpreadsheetFile.exportXlsx(bw)).save(path.join(r,'10_BOM_RELEASE_CANDIDATE_DELTA.xlsx'));
const bp=await bw.render({sheetName:'BOM Summary',range:'A1:D16',scale:1.4,format:'png'});await fs.writeFile(path.join(e,'BOM_PREVIEW.png'),new Uint8Array(await bp.arrayBuffer()));
console.log(JSON.stringify({power:'02_THREE_BOARD_POWER_BUDGET.xlsx',bom:'10_BOM_RELEASE_CANDIDATE_DELTA.xlsx',components:model.components.length,bomFormulaRows:d.bom.length,loadFormulaRows:d.budget.length}));
