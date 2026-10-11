"""Numerical independent checks + workbook/contract/candidate consistency.
This validates the audit/model, not hardware. Existing tests are untouched.
"""
from pathlib import Path
import csv,hashlib,json,math,subprocess,sys
sys.stdout.reconfigure(encoding='utf-8')
R=Path(__file__).resolve().parent.parent;V5=R.parents[3];E=V5/'evidence/pcb_s2_20261011'
def main():
    result=json.loads((R/'calc/RESULTS.json').read_text(encoding='utf-8'))
    audit=json.loads((E/'BOM_RECOUNT.json').read_text(encoding='utf-8'))
    checks=[]
    def check(name,ok,detail):
        checks.append(dict(name=name,status='PASS' if ok else 'FAIL',detail=detail))
        if not ok:raise AssertionError(name)
    # Time-domain resistor/capacitor integration independent of C*V^2*f expression.
    c=2.2e-9;v=12;r=47.;tau=r*c;dt=tau/1000;voltage=0.;energy=0.
    steps=20000
    for supply in [v,0.]:
        for _ in range(steps):
            current=(supply-voltage)/r
            energy+=r*current**2*dt
            voltage+=current/c*dt
    p=energy*40000;target=result['capacitive_power'][0]['nominal_W']
    check('RC_TIME_DOMAIN_ENERGY',abs(p/target-1)<.002,dict(numerical_W=p,closed_form_W=target,relative_error=p/target-1))
    # Integrate switched inductor voltage at duty Vo/Vin, compare pp excursion.
    worst=result['buck'][2];vo=3.3;vin=13.2;fs=390000;L=22e-6*.8
    n=12000;dt=1/fs/n;duty=vo/vin;i=0.;lo=0.;hi=0.
    for k in range(n):
        i+=(vin-vo if (k+.5)/n<duty else -vo)*dt/L;lo=min(lo,i);hi=max(hi,i)
    check('BUCK_SWITCHED_VOLTAGE_INTEGRAL',abs((hi-lo)/worst['delta_IL_A']-1)<.002,dict(numerical_delta_A=hi-lo,closed_form_delta_A=worst['delta_IL_A'],end_current_A=i))
    check('WORKBOOK_FORMULAS',audit['formula_checks']==1010 and not audit['formula_errors'],audit['formula_checks'])
    check('OLD_INSTALLED_COUNTS',audit['installed_by_sheet']==dict(Upper=551,Lower=551,Central=83,External=20),audit['installed_by_sheet'])
    wb=json.loads((E/'WORKBOOK_XML_AUDIT.json').read_text(encoding='utf-8'))
    maps={}
    for s in wb['sheets']:
        if s['name']=='Summary':continue
        maps[s['name']]={}
        for row in s['rows']:
            n=next(iter(row))[1:];id=row.get('A'+n,{}).get('value','')
            if id.startswith(('B-','PC-','NS-','H-')):maps[s['name']][id]=int(row['E'+n]['value'])
    source=json.loads((V5/'hardware/design_20261011/BOM_INPUTS.json').read_text(encoding='utf-8'))
    mismatches=[]
    for x in source['items']:
        for name,k in [('Upper',0),('Lower',1),('Central',2),('External',4)]:
            if maps[name][x['id']]!=x['quantities'][k]:mismatches.append([name,x['id']])
    check('WORKBOOK_VS_CONTRACT_EVERY_ITEM',not mismatches,mismatches)
    candidate=json.loads((R/'BOM_INPUTS_S2_CANDIDATE.json').read_text(encoding='utf-8'))
    items={x['id']:x for x in candidate['items']}
    check('SUPERVISOR_EXACT_2',items['S2-001']['mpn']=='TPS3851H33EDRBR' and items['S2-001']['quantities']==[1,1,0,0,0],items['S2-001']['quantities'])
    check('OLD_SUPERVISOR_INSTALLED_ZERO',all(sum(items[id]['quantities'])==0 for id in ['B-008','B-009']),'provenance retained')
    check('ONLY_APPROVED_BOM_CHANGE',sum(sum(x['quantities']) for x in candidate['items'])==1203,'Not final purchase count')
    rows=list(csv.DictReader((R/'06_PASSIVE_CALC_REGISTER.csv').open(encoding='utf-8-sig',newline='')))
    check('ALL_860_PASSIVE_ITEMS_BLOCKED',len(rows)==860 and all(x['status']=='S2_C_BLOCKED' and x['actual_node']=='UNKNOWN_NO_NATIVE_SCHEMATIC' for x in rows),len(rows))
    check('NO_DUPLICATE_INVENTORY_REF',len({(x['board'],x['inventory_reference']) for x in rows})==860,'does not prove functional deduplication')
    check('KNOWN_INVALID_1P65K_REJECTED',result['efuse_ILIM'][0]['status']=='INVALID_LT_3K',result['efuse_ILIM'][0])
    check('INA_RANGE_FAILURE_RECORDED',result['power_path']['shunt20mOhm_5A_V']>result['power_path']['ina226_shunt_range_V'],'100mV >81.92mV; REVISE')
    for i in range(11):
        matches=list(R.glob(f'{i:02d}_*.md'))
        check('DELIVERABLE_'+str(i),bool(matches),[x.name for x in matches])
    # Scope guard includes tracked metadata, never opens historical source bodies.
    root=V5.parent
    for scope in ['v5/rtl','v5/ps','v5/config','v5/tests','v5/scripts','v5/golden','v5/constraints']:
        run=subprocess.run(['git','diff','--quiet','HEAD','--',scope],cwd=root)
        check('PROTECTED_SCOPE_'+scope,run.returncode==0,'Git diff only; no archive read')
    out=dict(status='PASS',classification='TESTED_REVIEW_ARTIFACTS_ALTERNATIVE_VALIDATION_NO_HARDWARE',checks=checks,
      calculation_sha256=hashlib.sha256((R/'calc/RESULTS.json').read_bytes()).hexdigest(),
      unit_test_claim='Existing243 remains243; review checks are separate')
    (E/'REVIEW_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('REVIEW_VERIFICATION PASS',len(checks),'checks; no hardware certification')
if __name__=='__main__':main()
