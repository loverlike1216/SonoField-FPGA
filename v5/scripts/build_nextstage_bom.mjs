import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';
const root=path.resolve(process.argv[2]), data=JSON.parse(await fs.readFile(path.join(root,'hardware/next_stage/20261010/BOM_INPUTS.json'),'utf8'));
const out=path.join(root,'hardware/bom/working/2026-10-10'), ev=path.join(root,'evidence/next_stage/20261010/bom');
await fs.mkdir(out,{recursive:true});await fs.mkdir(ev,{recursive:true});
const wb=Workbook.create(), review=wb.worksheets.add('Review');
review.getRange('A2').values=[['SonoField v5 / AD7606C-16 working BOM']];
review.getRange('A4:B12').values=[['Release','HOLD - NOT FOR PROCUREMENT'],['ADC direction','USER APPROVED C-16; electrical HOLD'],['TX / RX','NU40C10T suffix pending / RX exact MPN HOLD'],['Temperature','3 TMP117; optional SHT45 diagnostic'],['Array power','Independent external12V per board'],['Central power','AX7020 only; capacity UNKNOWN'],['Native schematic / ERC','NOT_CREATED / NOT_RUN'],['Price currency','CNY; all prices UNKNOWN'],['Provenance','Unchanged pre-PCB baseline + current user decision']];
review.getRange('A15:D15').values=[['Assembly','Part types','Installed units','Release']];
const names=['Upper','Lower','Central','External'],indices=[0,1,2,4];
const cols=['ID','MPN / family','Description','Package / pins','Installed','Spare fraction','Planned qty','References','Supply / rating','Current A (scope in risk)','Source','Supplier','Approval','Footprint verification','Price CNY','Alternative / required evidence'];
for(let b=0;b<4;b++){
 const s=wb.worksheets.add(names[b]),items=data.items.filter(x=>x.quantities[indices[b]]>0);
 s.getRange('A2').values=[[`${names[b]} - PROPOSED WORKING; ELECTRICAL HOLD`]];
 s.getRange('A4:P4').values=[cols];
 s.getRange(`A5:P${4+items.length}`).values=items.map(x=>[x.id,x.mpn,x.description,`${x.package}; pins ${x.pin_count??'UNKNOWN'}`,x.quantities[indices[b]],.1,null,x.references[names[b]].join(', '),x.supply,x.current_A??'UNKNOWN',x.source,x.supplier,x.approval,x.native_footprint,'UNKNOWN',x.risk]);
 s.getRange(`G5:G${4+items.length}`).formulas=items.map((_,i)=>[`=ROUNDUP(E${i+5}*(1+F${i+5}),0)`]);
 s.getRange(`F5:F${4+items.length}`).setNumberFormat('0%');
 s.getRange(`A4:P${4+items.length}`).format.wrapText=true;s.getRange(`A5:P${4+items.length}`).format.rowHeight=76;
 // Preserve every instance ID and give long reference lists enough visible height.
 items.forEach((x,i)=>{const rows=Math.ceil(x.references[names[b]].join(', ').length/55);s.getRange(`A${i+5}:P${i+5}`).format.rowHeight=Math.max(76,rows*12);});
 const widths=[11,38,40,46,11,12,12,70,48,22,58,28,48,26,16,90];widths.forEach((v,i)=>s.getRangeByIndexes(0,i,items.length+4,1).format.columnWidth=v);
 s.getRange('A4:P4').format={fill:'#174967',font:{color:'#ffffff',bold:true},rowHeight:38,wrapText:true};
 s.freezePanes.freezeRows(4);s.freezePanes.freezeColumns(2);s.tables.add(`A4:P${4+items.length}`,true,`${names[b]}Parts`);
 review.getRange(`A${16+b}:D${16+b}`).values=[[names[b],items.length,null,'HOLD']];
 review.getRange(`C${16+b}`).formulas=[[`=SUM('${names[b]}'!E5:E${4+items.length})`]];
 const expected=items.reduce((n,x)=>n+x.quantities[indices[b]],0);wb.recalculate();if(review.getRange(`C${16+b}`).values[0][0]!==expected)throw Error('Board quantity mismatch');
}
review.getRange('A22:D23').values=[['Ideal CV2f sensitivity ONLY','C nF','V swing','f Hz'],['64TX, not measured / not upper bound',2.2,12,40000]];
review.getRange('A25:B25').values=[['Ideal charging power W',null]];review.getRange('B25').formulas=[['=64*B23*1E-9*C23^2*D23']];
review.getRange('A28:B30').values=[['5A source / 2A eFuse','NOT interchangeable; selectivity / wiring HOLD'],['Continuous piezo load','Resonance, driver loss, peak current UNKNOWN'],['Pin review','DOUT E-H unconnected; all ADC64 pins in JSON']];
review.getRange('A1:A30').format.columnWidth=46;review.getRange('B1:B30').format.columnWidth=64;review.getRange('C1:D30').format.columnWidth=20;review.getRange('A4:D30').format.wrapText=true;review.getRange('A4:D30').format.rowHeight=32;
for(const r of ['A15:D15','A22:D22'])review.getRange(r).format={fill:'#174967',font:{color:'#ffffff',bold:true},rowHeight:34,wrapText:true};
const sources=wb.worksheets.add('Source_References');sources.getRange('A2:D2').values=[['Source','Version / scope','URL / provenance','Release effect']];
sources.getRange('A3:D8').values=[['ADC','ADI Rev.A; Table9/23/26/38','https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf','Digital verified; physical HOLD'],['TMP117','TI Rev.D','https://www.ti.com/lit/ds/symlink/tmp117.pdf','3 addresses; ID/readiness; no CRC'],['NU40C','User supplier images; hashes in VENDOR_PARAMETERS.json','Private originals excluded from public repository','T/R suffix and continuous rating HOLD'],['AX7020','Official2023.1; Rev3 mismatch','https://github.com/alinxalinx/AX7020_2023.1','Pin/VCCO/power/DDR HOLD'],['Driver','Microchip TC4427A','https://www.microchip.com/en-us/product/TC4427A','Load/thermal/protection HOLD'],['Baseline','Canonical JSON hash in BOM_INPUTS.json','v5/hardware/prepcb/bom_inputs.json','Historical baseline preserved']];
const decisions=wb.worksheets.add('Decisions');decisions.getRange('A2:D2').values=[['Decision','Status','Rationale / risk','Approval boundary']];
decisions.getRange('A3:D8').values=[['AD7606C-16','APPROVED DEVICE DIRECTION','User explicit approval 2026-10-10; electrical HOLD','No further device approval needed'],['RX full MPN','PROPOSED HOLD','R-2 exact ordering code not confirmed','User/vendor confirmation'],['Array power','PROPOSED HOLD','Independent12V; cutoff/OE/watchdog/NC estop','Electrical review and bench'],['Central power','BLOCKED','AX7020 only; current limit unknown','Rev3 docs and measurement'],['Native CAD / manufacture','BLOCKED / HOLD','Machine contract only; ERC NOT_RUN','CAD and electrical review; manufacture separate'],['Main merge','PENDING','Stacked Draft PR; no automatic merge','User review of concrete candidate']];
for(const s of wb.worksheets.items){s.showGridLines=false;s.getRange('A1:P100').format.font={name:'Arial',size:10};s.getRange('A2').format.font={name:'Arial',size:14,bold:true};}
for(const s of [sources,decisions]){[28,38,85,60].forEach((v,i)=>s.getRangeByIndexes(0,i,10,1).format.columnWidth=v);s.getRange('A2:D8').format.wrapText=true;s.getRange('A3:D8').format.rowHeight=65;s.getRange('A2:D2').format={fill:'#174967',font:{color:'#ffffff',bold:true},rowHeight:30};}
wb.recalculate();const original=review.getRange('B25').values[0][0];review.getRange('B23').values=[[4.4]];wb.recalculate();if(Math.abs(review.getRange('B25').values[0][0]-original*2)>1e-10)throw Error('Formula recalculation failed');review.getRange('B23').values=[[2.2]];wb.recalculate();
const checks=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!',options:{useRegex:true,maxResults:20},maxChars:2000});await fs.writeFile(path.join(ev,'formula_inspection.ndjson'),checks.ndjson);
for(const s of [review,...names.map(n=>wb.worksheets.getItem(n)),sources,decisions]){const range=s.name==='Review'?'A1:D30':names.includes(s.name)?'A1:G12':'A1:D8';const preview=await wb.render({sheetName:s.name,range,scale:1.2,format:'png'});await fs.writeFile(path.join(ev,s.name+'.png'),new Uint8Array(await preview.arrayBuffer()));if(names.includes(s.name)){const detail=await wb.render({sheetName:s.name,range:'H4:P8',scale:1,format:'png'});await fs.writeFile(path.join(ev,s.name+'_detail.png'),new Uint8Array(await detail.arrayBuffer()));}}
const file=path.join(out,'BOM_AX7020_NU40C10T_AD7606C16_WORKING.xlsx');await(await SpreadsheetFile.exportXlsx(wb)).save(file);
console.log(JSON.stringify({status:'EXPORTED',sheets:7,types:data.items.length,ideal_only_W:original,file}));
