"""Use EasyEDA native page-copy; rebind every part by its verified template position."""
import argparse
import json
from gateway import execute
from capture_tx import write
from tx_design import OUT


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--start',type=int,default=1);parser.add_argument('--stop',type=int,default=32)
    args=parser.parse_args()
    design=json.loads((OUT/'project/tx_design.json').read_text(encoding='utf-8'))
    mp=OUT/'project/native_sheet_map.json'
    mapping=json.loads(mp.read_text(encoding='utf-8'))
    first_copy=OUT/'log/review/first_native_copy.json'
    if first_copy.exists():mapping.setdefault('TX_UPPER_01',json.loads(first_copy.read_text(encoding='utf-8'))['id'])
    base=design['sheets'][0]
    for sheet in design['sheets'][args.start:args.stop]:
        name=sheet['name']
        if name not in mapping:
            mapping[name]=execute("return await eda.dmt_Schematic.copySchematicPage('d44f64bd1a3255a6','ac7ec8f12e696ab7');")
            if not mapping[name]:raise RuntimeError('Native copy failed')
            write(mp,mapping)
        page=mapping[name]
        execute('await eda.dmt_Schematic.modifySchematicPageName('+json.dumps(page)+','+json.dumps(name)+');return await eda.dmt_EditorControl.openDocument('+json.dumps(page)+');')
        netmap={}
        for old,new in zip(base['parts'],sheet['parts']):
            assert old['key']==new['key'] and (old['x'],old['y'])==(new['x'],new['y'])
            for pin,net in old['nets'].items():
                if net is not None:
                    assert netmap.setdefault(net,new['nets'][pin])==new['nets'][pin]
        script='const sheet='+json.dumps(sheet)+';const netmap='+json.dumps(netmap)+';const base='+json.dumps(base)+';'+r'''
const components=await eda.sch_PrimitiveComponent.getAll();
const found=new Set();
for(const c of components){
 const p=sheet.parts.find(p=>p.x===c.getState_X()&&p.y===c.getState_Y());
 if(!p){if(c.getState_X()===230&&c.getState_Y()===120){await eda.sch_PrimitiveComponent.delete(c);continue;}throw new Error('Unexpected template component');}
 if(found.has(p.ref))throw new Error('Duplicate template position');found.add(p.ref);
 const props={designator:p.ref,otherProperty:{Value:p.value,'Design status':'DRAFT_NOT_FOR_FABRICATION',Assembly:p.dnp?'DNP':'FIT','Device qualification':p.generic?'SYMBOL_TEMPLATE_MPN_TBD':'PIN_AUDIT_REQUIRED'}};
 if(p.generic)Object.assign(props,{manufacturer:'UNQUALIFIED',manufacturerId:'MPN_TBD',supplier:'UNSELECTED',supplierId:'TBD'});
 else Object.assign(props,{supplier:'LCSC',supplierId:'C20551'});
 const updated=await eda.sch_PrimitiveComponent.modify(c,props);if(!updated)throw new Error('Rename failed');
}
if(found.size!==sheet.parts.length)throw new Error('Missing template slot');
for(const w of await eda.sch_PrimitiveWire.getAll())await eda.sch_PrimitiveWire.delete(w);
if((await eda.sch_PrimitiveWire.getAll()).length)throw new Error('Old wires remain');
for(const c of await eda.sch_PrimitiveComponent.getAll()){
 const p=sheet.parts.find(p=>p.ref===c.getState_Designator());if(!p)throw new Error('Unmapped part');
 for(const pin of await c.getAllPins()){
  const number=pin.getState_PinNumber();if(!(number in p.nets))throw new Error('Unmapped pin');
  const net=p.nets[number];if(net===null)continue;
  const x=pin.getState_X(),y=pin.getState_Y(),angle=pin.getState_Rotation()*Math.PI/180;
  const ex=Math.round(x+80*Math.cos(angle)),ey=Math.round(y+20*Math.sin(angle));
  if(!await eda.sch_PrimitiveWire.create([x,y,ex,ey],net))throw new Error('Wire rebuild failed');
 }
}
for(const t of await eda.sch_PrimitiveText.getAll()){
 const i=base.notes.indexOf(t.getState_Content());if(i>=0)await eda.sch_PrimitiveText.modify(t,{content:sheet.notes[i]});
}
const saved=await eda.sch_Document.save();
const doc=await eda.dmt_SelectControl.getCurrentDocumentInfo();
const closed=await eda.dmt_EditorControl.closeDocument(doc.tabId);
const reopened=await eda.dmt_EditorControl.openDocument(doc.uuid);
return {saved,closed,reopened,name:sheet.name,components:found.size};
'''
        result=execute(script)
        write(OUT/f'log/review/{name}_clone.json',result)
        write(mp,mapping)
        print(name,result,flush=True)


if __name__=='__main__':main()
