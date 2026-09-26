const existing = await eda.sch_PrimitiveComponent.getAll();
const refs = new Set(existing.map(c=>c.getState_Designator()));
if (sheet.parts.some(p=>refs.has(p.ref))) throw new Error('Refusing duplicate capture');
const evidence = [];
for (let i=0;i<sheet.notes.length;i++) {
  await eda.sch_PrimitiveText.create(50,790-18*i,sheet.notes[i],0,undefined,undefined,i===0?12:8);
}
for (const item of sheet.parts) {
  const device = devices[item.key];
  if (!device) throw new Error('Missing device '+item.key);
  let c = await eda.sch_PrimitiveComponent.create(device,item.x,item.y,'',0,false,!item.dnp,true);
  if (!c) throw new Error('Create failed '+item.ref);
  const props={designator:item.ref,name:item.value,addIntoBom:!item.dnp,
    manufacturer:device.manufacturer,manufacturerId:device.manufacturerId,
    supplier:device.supplier,supplierId:device.supplierId,
    otherProperty:{'Value':item.value,'Design status':'DRAFT_NOT_FOR_FABRICATION','Assembly':item.dnp?'DNP':'FIT',
      'Device qualification':item.generic?'SYMBOL_TEMPLATE_MPN_TBD':'PIN_AUDIT_REQUIRED'}};
  if (item.generic) Object.assign(props,{manufacturer:'UNQUALIFIED',manufacturerId:'MPN_TBD',supplier:'UNSELECTED',supplierId:'TBD'});
  c = await eda.sch_PrimitiveComponent.modify(c,props);
  if (!c) throw new Error('Properties failed '+item.ref);
  const pins=await c.getAllPins();
  if (!pins || pins.length!==Object.keys(item.nets).length) throw new Error('Pin count mismatch '+item.ref);
  for (const pin of pins) {
    const number=pin.getState_PinNumber();
    if (!(number in item.nets)) throw new Error('Unmapped pin '+item.ref+'.'+number);
    const net=item.nets[number];
    if (net===null) { pin.setState_NoConnected(true); await pin.done(); }
    else {
      const x=pin.getState_X(),y=pin.getState_Y(),angle=pin.getState_Rotation()*Math.PI/180;
      const ex=Math.round(x+80*Math.cos(angle)),ey=Math.round(y+20*Math.sin(angle));
      const wire=await eda.sch_PrimitiveWire.create([x,y,ex,ey],net);
      if (!wire) throw new Error('Wire failed '+item.ref+'.'+number);
    }
    evidence.push({ref:item.ref,pin:number,net});
  }
}
const saved=await eda.sch_Document.save();
if(!saved)throw new Error('Native save failed');
return {sheet:sheet.name,componentCount:sheet.parts.length,pins:evidence,saved};
