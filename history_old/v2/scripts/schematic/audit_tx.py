"""Compare EasyEDA's exported netlist against intended per-pin connectivity."""
import argparse
import hashlib
import json
from pathlib import Path
from tx_design import OUT


def audit(netlist_path, sheet_count, extra_designs=()):
    wrapper = json.loads(netlist_path.read_text(encoding='utf-8'))
    netlist = json.loads(wrapper['text'])
    design = json.loads((OUT/'project/tx_design.json').read_text(encoding='utf-8'))
    expected = {p['ref']:p for s in design['sheets'][:sheet_count] for p in s['parts']}
    for filename in extra_designs:
        extra = json.loads((OUT/'project'/filename).read_text(encoding='utf-8'))
        for s in extra['sheets']:
            for p in s['parts']:
                if p['ref'] in expected: raise ValueError('Duplicate intended reference '+p['ref'])
                expected[p['ref']] = p
        sheet_count += len(extra['sheets'])
    components = [c for c in netlist['components'].values() if c['props'].get('Designator')]
    actual = {c['props']['Designator']:c for c in components}
    errors=[]
    if len(actual)!=len(components): errors.append('Duplicate designators')
    if actual.keys()!=expected.keys(): errors.append({'missing':sorted(expected.keys()-actual.keys()),'unexpected':sorted(actual.keys()-expected.keys())})
    pins=0
    for ref,item in expected.items():
        if ref not in actual: continue
        part=actual[ref]
        if set(part['pinInfoMap'])!=set(item['nets']): errors.append({'pin_count':ref})
        for number,net in item['nets'].items():
            pins+=1
            found=part['pinInfoMap'].get(number,{}).get('net')
            if found!=(net or ''): errors.append({'ref':ref,'pin':number,'expected':net,'actual':found})
        if item['generic'] and part['props'].get('Manufacturer Part')!='MPN_TBD':
            errors.append({'stale_template_mpn':ref})
        if part['props'].get('Assembly')!=('DNP' if item['dnp'] else 'FIT'): errors.append({'assembly':ref})
    return {'status':'PASS' if not errors else 'FAIL','scope':'Native per-pin connectivity against design manifests and template metadata; not independent circuit validation or ERC',
            'logical_modules':sheet_count,'components':len(actual),'pins_checked':pins,'errors':errors,
            'netlist_sha256':hashlib.sha256(netlist_path.read_bytes()).hexdigest()}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--sheets',type=int,default=1)
    p.add_argument('--extra',action='append',default=[])
    p.add_argument('--netlist',default='tx_native_netlist.json');p.add_argument('--output',default='tx_connectivity_audit.json');a=p.parse_args()
    result=audit(OUT/'log/review'/a.netlist,a.sheets,a.extra)
    (OUT/'log/review'/a.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2));raise SystemExit(0 if result['status']=='PASS' else 1)
