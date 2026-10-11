"""SI calculations and exhaustive inherited passive inventory; candidate, not release.
Run from any cwd. No original workbook, RTL or source contract is changed.
"""
from pathlib import Path
import cmath, collections, copy, csv, hashlib, itertools, json, math, sys
sys.stdout.reconfigure(encoding='utf-8')
V5=Path(__file__).resolve().parents[5]
REVIEW=Path(__file__).resolve().parent.parent
E=V5/'evidence/pcb_s2_20261011'
def writecsv(path,rows):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def save(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
    inputs=dict(classification='ENGINEERING_ASSUMPTIONS_UNLESS_SPECIFICALLY_SOURCED',
       C0_F=2.2e-9,C0_tolerance=.2,frequency_Hz=40000,voltage_step_V=12,
       Vrail_corners_V=[10.8,12,13.2],buck_fsw_min_Hz=390000,buck_L_tolerance=.2,
       buck_load_A=.5,buck_stress_load_A=2,ambient_assumption_C=60,
       buck_Vref_bounds_V=[.581,.596,.611],feedback_R_tolerance=.001,
       charge_model='fully settled non-energy-recovering ideal capacitor; excludes motional branch and driver cross conduction',
       sources={'C0':'User S2 instruction section4 GateA, assumption only; no vendor validation',
        'buck':'TPS54202 RevC sections5.5/7.2.3; 390kHz min; 2A rated',
        'watchdog':'TPS3851 RevB sections5.5/5.6/7.1.1.2',
        'efuse':'TPS2663 RevG table6.5 and eq8 p30; 18 A*kOhm/RkOhm'})
    save(REVIEW/'calc/INPUTS.json',inputs)
    out=dict(inputs=inputs,status='ALTERNATIVE_VALIDATION_CALCULATION_ONLY')
    out['capacitive_power']=[]
    for n in [1,16,64,128]:
        out['capacitive_power'].append(dict(channels=n,nominal_W=n*2.2e-9*12**2*40000,
            C_only_min_W=n*1.76e-9*12**2*40000,C_only_max_W=n*2.64e-9*12**2*40000,
            C_and_Vmax_W=n*2.64e-9*13.2**2*40000,nominal_input_A=n*2.2e-9*12*40000))
    out['driver_edge_examples']=[dict(Rext_ohm=r,Rdriver_typ_assumed_ohm=7,
       Iinitial_typ_A=12/(7+r),rise_10_90_ns=2.2*(7+r)*2.64e-9*1e9,
       resistor_ideal_average_W=2.64e-9*13.2**2*40000*r/(7+r)) for r in [0,22,47]]
    # Buck linear inductor voltage integration, checked against manufacturer formula.
    out['buck']=[]
    for vo in [3.3,5.5]:
        for L in [6.8e-6,15e-6,22e-6,33e-6]:
            lmin=L*.8;v=13.2;fs=390000;di=vo*(v-vo)/(v*lmin*fs)
            out['buck'].append(dict(Vout_V=vo,L_nom_uH=L*1e6,L_min_uH=lmin*1e6,
               delta_IL_A=di,peak_0p5A_A=.5+di/2,peak_2A_A=2+di/2,
               Irms_2A_A=math.sqrt(4+di**2/12),ripple_Ceff22uF_ESR10mOhm_V=di/(8*fs*22e-6)+di*.01))
    out['buck_Lmin_30percent_at_2A_uH']={str(v):v*(13.2-v)/(13.2*.3*2*390000)*1e6 for v in [3.3,5.5]}
    out['feedback']=[]
    for target,rb in [(3.3,22100),(5.5,12100)]:
        values=[vf*(1+100000*(1+rt)/ (rb*(1+rbt))) for vf in [.581,.611] for rt in [-.001,.001] for rbt in [-.001,.001]]
        out['feedback'].append(dict(target_V=target,Rtop_ohm=100000,Rbottom_ohm=rb,
          ideal_Rbottom_ohm=100000/(target/.596-1),Vnom_V=.596*(1+100000/rb),Vmin_V=min(values),Vmax_V=max(values),
          FB_bias_error_bound_V=None,FB_bias_formula='I_FB*Rtop; guaranteed bound NOT_FOUND; not included'))
    out['supervisor']=dict(VIT_nom_V=3.3*.93,VIT_min_V=3.3*.93*.992,VIT_max_V=3.3*.93*1.008,
      CWD_1p8nF_nom_ms=77.4*1.8+55,CWD_1p8nF_min_ms=.905*(77.4*1.8*.95+55),
      CWD_1p8nF_max_ms=1.095*(77.4*1.8*1.05+55),fixed_10k_ms=[170,200,230],
      pullup10k_sink_A=3.3/10000,pullup10k_power_W=3.3**2/10000)
    out['efuse_ILIM']=[]
    for R in [1650,4020,4750,6040,9090]:
        i=18000/R
        out['efuse_ILIM'].append(dict(R_ohm=R,I_nom_A=i,I_lo_7percent_plus_Rtol_A=i*.93/1.01,
           I_hi_7percent_plus_Rtol_A=i*1.07/.99,status='INVALID_LT_3K' if R<3000 else 'CANDIDATE_PULSE_AND_SOURCE_HOLD'))
    out['power_path']=dict(adapter_load_max_W={str(p):{str(h):p/(1+h) for h in [.2,.3]} for p in [40,60]},
       shunt20mOhm_5A_V=.02*5,shunt20mOhm_5A_W=.02*5**2,
       ina226_shunt_range_V=.08192,shunt_max_5A_1percent_ohm=.08192/(5*1.01),
       efuse53mOhm_5A_W=.053*5**2,jack30mOhm_5A_W=.03*5**2,
       cap470uF_energy_12V_J=.5*470e-6*12**2,
       cap470uF_droop_64channels_V=64*2.64e-9*13.2/(470e-6*.8),
       driver_Ceff_for_2channels_drop0p1V_F=2*2.64e-9*13.2/.1,
       bleed12_to1V_in1s_Rmax_470uFplus20_ohm=1/(470e-6*1.2*math.log(12)),
       bleed680ohm_initial_13p2V_W=13.2**2/680,
       slew_10nF_12V_typ_s=20.8e3*12*10e-9,
       Icap470uF_slew_10nF_A=470e-6*12/(20.8e3*12*10e-9))
    out['pulldown']=dict(leak_budget_A=25e-6,VIL_V=.8,Rmax_ohm=.8/25e-6,
       R100k_off_voltage_V=100000*25e-6,R10k_off_voltage_V=10000*25e-6,
       R10k_high_load_A=3.3/10000,warning='25uA = 595 IOZ15uA + TC4427 input10uA; routing leakage extra; VOH low-load conditions must be checked')
    out['i2c']=[dict(bus_C_F=c,Rmax_1us_ohm=1e-6/(.8473*c),Rmin_3mA_ohm=(3.3-.4)/.003,
       rise4700_ns=.8473*4700*c*1e9) for c in [100e-12,200e-12,400e-12]]
    # Two buffered first-order poles. This is a deliberately explicit example,
    # NOT a claim to describe the absent production AFE nor ADC internal filter.
    hp=1/(2*math.pi*100000*10e-9);lp=1/(2*math.pi*10000*100e-12)
    def transfer(f,hp,lp):
        s=1j*f;return (s/hp)/(1+s/hp)/(1+s/lp)
    rows=[]
    for f in [100,1000,10000,25000,40000,100000,150000,220000,400000,800000,1000000]:
        h=transfer(f,hp,lp);rows.append(dict(frequency_Hz=f,magnitude_dB=20*math.log10(abs(h)),phase_deg=math.degrees(cmath.phase(h))))
    writecsv(REVIEW/'calc/AFE_EXAMPLE_AC.csv',rows)
    phases=[math.degrees(cmath.phase(transfer(40000,hp/a,lp/b))) for a in [.99*.95,1.01*1.05] for b in [.99*.95,1.01*1.05]]
    out['afe_example']=dict(highpass_Hz=hp,lowpass_Hz=lp,phase40k_deg_min=min(phases),phase40k_deg_max=max(phases),
       max_interchannel_phase_deg=max(phases)-min(phases),acceptance='NOT_A_35dB_PASS; insufficient anti-aliasing without spectral envelope')
    out['digital']=dict(T66MHz_s=1/66e6,half_T66MHz_s=.5/66e6,ADC32bits_800k_lowerbound_Hz=32*800000,
       raw_8x16x800k_byte_per_s=8*16*800000/8,UART115200_8N1_byte_per_s=115200/10)
    save(REVIEW/'calc/RESULTS.json',out)
    # Independently recount worksheet rows, cached formulas, references, no Excel editing.
    w=json.loads((E/'WORKBOOK_XML_AUDIT.json').read_text(encoding='utf-8'))
    sheets={s['name']:s for s in w['sheets']}; sums={}; rowmaps={};errors=[];formula_count=0;refs=collections.defaultdict(list)
    for name in ['Upper','Lower','Central','External']:
        rowmaps[name]={}
        for row in sheets[name]['rows']:
            n=next(iter(row))[1:];id=row.get('A'+n,{}).get('value','')
            if not re_id(id):continue
            q=int(row['E'+n]['value']);rowmaps[name][id]=q
            expected=math.ceil(round(q*(1+float(row['F'+n]['value'])),8));cached=int(row['G'+n]['value'])
            formula_count+=1
            if expected!=cached:errors.append(f'{name}:G{n}')
            for ref in row['H'+n]['value'].split(','):
                if ref.strip():refs[name,ref.strip()].append(id)
        sums[name]=sum(rowmaps[name].values())
    for row in sheets['Summary']['rows']:
        n=next(iter(row))[1:];id=row.get('A'+n,{}).get('value','')
        if not re_id(id):continue
        for col,name in [('C','Upper'),('D','Lower'),('E','Central'),('F','External')]:
            formula_count+=1
            if int(row[col+n]['value'])!=rowmaps[name][id]:errors.append('Summary:'+col+n)
        formula_count+=2
        if int(row['G'+n]['value'])!=sum(rowmaps[s][id] for s in rowmaps):errors.append('Summary:G'+n)
        purchase_total=0
        for name in rowmaps:
            r=next(r for r in sheets[name]['rows'] if r.get('A'+next(iter(r))[1:],{}).get('value')==id)
            rn=next(iter(r))[1:];purchase_total+=int(r['G'+rn]['value'])
        if int(row['H'+n]['value'])!=purchase_total:errors.append('Summary:H'+n)
    original=json.loads((V5/'hardware/design_20261011/BOM_INPUTS.json').read_text(encoding='utf-8'))
    items=original['items'];categories=collections.Counter();register=[];delta=[]
    for x in items:
        id=x['id'];q=x['quantities'];installed=sum(q);action='KEEP';why='Inherited placeholder; no electrical release'
        if id in ['B-008','B-009']:action='DELETE';why='Merged into S2-001, provenance retained, safety coverage incomplete'
        if id=='B-030':action='CHANGE';why='6.8uH cannot be universal; see buck corners; quantity4 retained only as placeholder'
        if id=='B-022':action='CHANGE';why='20mOhm at5A gives100mV > INA22681.92mV; coordinate each rail range'
        if id=='B-062':action='CHANGE';why='Array1.65k invalid for TPS26631; central chip unknown; final Rlim BLOCKED'
        if id=='H-020':action='CHANGE';why='10k candidate from leakage budget; count128 retained; not finalized'
        if id in ['B-054','B-061']:action='DUPLICATE_SUSPECT';why='No actual nets/refdes; B054 may overlap H020; B061 not proven to be TX damping'
        delta.append(dict(id=id,old_spec=x['mpn'],new_spec='0 INSTALLED; see S2-001' if action=='DELETE' else ('CONDITIONAL; see calculation register' if action=='CHANGE' else x['mpn']),
           old_upper=q[0],old_lower=q[1],old_central=q[2],old_spares_column=q[3],old_external=q[4],
           new_upper=0 if action=='DELETE' else q[0],new_lower=0 if action=='DELETE' else q[1],new_central=q[2],new_external=q[4],
           action=action,reason=why,status='PURCHASE_HOLD'))
        typ='C' if id in ['B-'+str(i).zfill(3) for i in range(46,54)] else 'L' if id=='B-030' else 'R' if id in ['B-022']+['B-'+str(i).zfill(3) for i in range(54,69)]+['H-020'] else None
        if not typ:continue
        categories[typ]+=installed
        for board,idx in [('Upper',0),('Lower',1),('Central',2),('External',4)]:
            xr=x.get('references',{}).get(board,[])
            for i in range(q[idx]):
                ref=xr[i] if i<len(xr) else f'{board}_{id}_{i+1:03d}'
                register.append(dict(board=board,inventory_reference=ref,bom_id=id,type=typ,function=x['description'],
                   actual_node='UNKNOWN_NO_NATIVE_SCHEMATIC',old_value=x['mpn'],action=action if action!='KEEP' else 'BLOCKED',
                   formula='BLOCKED: node connectivity and operating corners required; illustrative derived nodes in 06.md',
                   inputs_source='BOM_INPUTS.json + independently read workbook',theory_value='UNKNOWN',standard_value='NOT_FINALIZED',
                   tolerance_derating='NOT_QUALIFIED',package=x['package'],worst_case='UNKNOWN_LOAD_AND_NET',
                   measurement_required='Actual node allocation, effective C, loop impedance, voltage/current/thermal corners',
                   evidence='WORKBOOK_XML_AUDIT.json; calc/RESULTS.json',status='S2_C_BLOCKED'))
    candidate=copy.deepcopy(original)
    for x in candidate['items']:
        if x['id'] in ['B-008','B-009']:
            x['superseded_by']='S2-001';x['previous_quantities']=x['quantities'];x['quantities']=[0,0,0,0,0];x['approval']='SUPERSEDED_NOT_INSTALLED'
            x['previous_references']=x.pop('references',{})
    item=dict(id='S2-001',mpn='TPS3851H33EDRBR',description='Combined 3V3 UV supervisor and timeout watchdog; window/cutoff incomplete',
       quantities=[1,1,0,0,0],package='DRB 8-pin VSON 3x3mm + exposed thermal pad; native qualification HOLD',
       source='User approved S2 instruction and explicit execution reply',procurement='HOLD',qualification='DIRECTION_APPROVED_CIRCUIT_HOLD')
    candidate['items'].append(item);candidate.update(status='S2_REVIEW_CANDIDATE_NOT_FULL_RCL_FREEZE',based_on='8c27b5841b5494c3761ab211881a3ea2be63e8c8',safety='REVISE_WINDOW_HEARTBEAT_CUTOFF_HOLD')
    save(REVIEW/'BOM_INPUTS_S2_CANDIDATE.json',candidate)
    delta.append(dict(zip(delta[0].keys(),['S2-001','B008+B009 merged','TPS3851H33EDRBR',0,0,0,0,0,1,1,0,0,'ADD','User approved2 total; not full protection replacement','PURCHASE_HOLD'])))
    writecsv(REVIEW/'07_BOM_DELTA_DRAFT.csv',delta)
    writecsv(REVIEW/'06_PASSIVE_CALC_REGISTER.csv',register)
    audit=dict(workbook_sha256=w['sha256'],item_types=len(items),installed_by_sheet=sums,total_installed=sum(sums.values()),
       spare_column_order='BOM_INPUTS quantities: Upper,Lower,Central,Spare,External',
       formula_checks=formula_count,formula_errors=errors,exact_ref_duplicates={str(k):v for k,v in refs.items() if len(v)>1},
       functional_duplicates='B054 vs H020 unresolved; no actual nets, artificial unique names do not disprove overlap',
       passive_counts=dict(categories),passive_inventory_rows=len(register),new_total_with_only_supervisor_change=sum(sums.values())-2,
       approved_new_passive_additions=0,approved_passive_deletions=0,conditional_change_groups=['B-022','B-030','B-062','H-020'],
       conditional_change_inventory_quantities={'L':4,'R':134},functional_duplicate_suspect_inventory={'B-054':180,'B-061':136},
       full_RCL_status='S2_C_BLOCKED; no final procurement counts',new_total_not_final=True)
    save(E/'BOM_RECOUNT.json',audit)
    print(json.dumps(audit,ensure_ascii=False,indent=2))
def re_id(s):return s.startswith(('B-','PC-','NS-','H-'))
if __name__=='__main__':main()
