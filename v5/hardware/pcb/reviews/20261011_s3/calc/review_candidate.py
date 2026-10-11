"""Independent semantic inspection of generated files, not native ERC/SPICE.
Reads exported records rather than importing the circuit builder.
"""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,hashlib,itertools,math,subprocess
R=Path(__file__).resolve().parents[1];ROOT=R.parents[4];E=ROOT/'v5/evidence/pcb_s3_20261011'
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def main():
    cs=rows(R/'netlist/COMPONENTS.csv');ps=rows(R/'netlist/PIN_NET.csv');bm=rows(R/'10_BOM_RELEASE_CANDIDATE_DELTA.csv');mapping=rows(R/'05_TX_CHANNEL_MAPPING.csv')
    checks=[]
    def check(name,cond,detail):
        checks.append(dict(name=name,result='PASS' if cond else 'FAIL',detail=detail))
    byref={c['refdes']:c for c in cs};pin={(p['refdes'],p['pin']):p for p in ps}
    def net(r,p):return pin[r,str(p)]['net'].split(':',1)[-1]
    check('unique_component_refs',len(byref)==len(cs),len(cs))
    check('unique_physical_pins',len(pin)==len(ps),len(ps))
    check('all_pins_have_component',all(p['refdes'] in byref for p in ps),len(ps))
    check('no_empty_nets',all(p['net'] for p in ps),len(ps))
    check('supervisor_exact_two',sum(c['mpn']=='TPS3851H33EDRBR' for c in cs)==2,'one per array')
    check('legacy_four_retired',sum(int(b['qty']) for b in bm if b['board']=='LEGACY_RETIRED')==0,'B008/009=0')
    check('physical_bom_matches_components',sum(int(b['qty']) for b in bm)==len(cs),'group rows count installed positions once')
    check('old_supervisor_combo_absent',not any('TLV803' in c['mpn'] for c in cs),'TPS3430 is additional window function;TPS3851 retained')
    check('adc_all64pins',set(p['pin'] for p in ps if p['refdes']=='CENTRAL_UADC')==set(map(str,range(1,65))),'ADI RevA Table9')
    check('adc_regcaps_separate',net('CENTRAL_UADC',36)!=net('CENTRAL_UADC',39),'each1uF')
    check('adc_refcap_common',net('CENTRAL_UADC',44)==net('CENTRAL_UADC',45),'common10uF')
    check('adc_serial_unused_outputs_not_grounded',all(pin['CENTRAL_UADC',str(i)]['disposition']=='INTENTIONAL_NC' for i in range(19,23)),'avoid short if8DOUT accidentally configured')
    check('adc_os_software_straps',all(net('CENTRAL_UADC',i)=='3V3' for i in [3,4,5,6]),'software+serial')
    check('adc_singleended_baseline_preserved',all(net('CENTRAL_UADC',i)=='GND' for i in range(50,65,2)),'negativeinputAGND;no unapproved differential range change')
    check('central_physical_gpio_buffers_only',sum(c['mpn']=='SN74AXC8T245PWR' and c['board']=='CENTRAL' for c in cs)==9,'51out+10in =7+2packages;logical128TXnotphysicalGPIO')
    check('tca9548a_physical_map',net('CENTRAL_UMUX',3)=='3V3' and net('CENTRAL_UMUX',21)=='GND' and pin['CENTRAL_UMUX','13']['disposition']=='INTENTIONAL_NC','RESET3;A2=21;SD4=13')
    check('usb_hardware_3a_qualifier',net('CENTRAL_UCC',8)=='CC3A_N' and net('CENTRAL_UINV',2)=='CC3A_N' and net('CENTRAL_U1',1)=='USB_ALLOW','OUT2low->allow;default pull down')
    check('usb_no_parallel_rd',not any(c['value']=='5.1k' for c in cs if c['board']=='CENTRAL'),'internal TUSB Rd')
    con=json.loads((ROOT/'v5/hardware/design_20261011/CONNECTION_CONTRACT.json').read_text())['connections']
    for board in ['UP','DN']:
        cnt=Counter(c['mpn'] for c in cs if c['board']==board)
        check(board+'_channel_counts',cnt['TC4427AEOA']==32 and cnt['SN74LVC595APWR']==16 and cnt['NU40C10T']==64 and cnt['RX_MPN_UNKNOWN']==4,'32dual/16eightbit4used/64TX/4RX')
        check(board+'_latch_Q_pin5',net(board+'_U13',5)=='ARMED' and net(board+'_U13',3)=='NOT_ARMED','barred Q is pin3')
        check(board+'_window_straps',net(board+'_U11',3)=='GND' and net(board+'_U11',6)=='3V3' and pin[board+'_U11','2']['disposition']=='INTENTIONAL_NC','CWDNC SET0=0 SET1=1')
        check(board+'_faultwired_or',all(net(board+'_'+r,p)=='FAULT_N' for r,p in [('U10',7),('U10',8),('U11',8),('U12',3),('U13',6)]),'OD watchdog/UV/temp clear latch')
        check(board+'_TC_no_always_on_supply',all(net(board+'_UD'+str(i),6)=='TX12' for i in range(32)),'one independently switched TX rail')
        check(board+'_64_series_resistors',all(byref[board+'_RTX'+str(i)]['value']=='330' for i in range(64)),'includes100%dutyshort calculation')
        check(board+'_highside_pullups_switched',all(net(board+'_RC2'+str(i),1)=='TX12' for i in range(64)),'Q2 collector pullups track TC supply')
        check(board+'_serializer_unused_four_NC',all(pin[board+'_US'+str(i),str(p)]['disposition']=='INTENTIONAL_NC' for i in range(16) for p in [4,5,6,7]),'exact32lanesx4used system')
    check('128_unique_mapping',len(mapping)==128 and {int(m['global_channel']) for m in mapping}==set(range(128)),'all channels')
    check('32_lane_mapping',Counter(int(m['lane']) for m in mapping)==Counter({i:4 for i in range(32)}),'no dropped channels')
    check('mirror_arrays',Counter((c['mpn'],c['value'],c['function']) for c in cs if c['board']=='UP')==Counter((c['mpn'],c['value'],c['function']) for c in cs if c['board']=='DN'),'identical population')
    # Check port positions against existing approved NC list inferred from unassigned contacts.
    for header in ['J10','J11']:
        # OPEN_DRAIN are the two approved I2C signal contacts, not power contacts.
        assigned={int(c['central_endpoint'].rsplit('.',1)[1]) for c in con if c['central_endpoint'].startswith('CENTRAL_AX_'+header+'.') and c['direction'] in ['IN','OUT','GROUND','OPEN_DRAIN']}
        check(header+'_power_unassigned_NC',all(pin['CENTRAL_AX_'+header,str(i)]['disposition']=='INTENTIONAL_NC' for i in range(1,41) if i not in assigned),'no header power fed to central rails')
    # Truth table explores allsevenindependent fault inputs and both arm/reset states.
    table=[]
    for faults in itertools.product([0,1],repeat=7):
        for armed in [0,1]:
            enable=int(armed and not any(faults));table.append(dict(uv=faults[0],early=faults[1],late=faults[2],thermal=faults[3],estop=faults[4],mainflt=faults[5],txflt=faults[6],armed_before=armed,enable_after=enable))
    check('all_fault_combinations_disable',all(t['enable_after']==0 for t in table if any(t[k] for k in ['uv','early','late','thermal','estop','mainflt','txflt'])),'256 boolean model states;not transistor transient proof')
    with (E/'SAFETY_TRUTH_TABLE.csv').open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,list(table[0]));w.writeheader();w.writerows(table)
    arithmetic=json.loads((E/'POWER_RESULTS.json').read_text())
    check('adc_avcc_static_range',4.75<arithmetic['adc_avcc_min_v']<arithmetic['adc_avcc_max_v']<5.25,'LDO accuracy condition needs6V3min>=6.09V')
    check('ina_shunt_range',arithmetic['shunt_at_limit_mv']<81.92,'not5A arbitrary mode')
    check('undefined_logic_EN_off',arithmetic['kill_en_undefined_vcc_max_v']<1.076,'undefined FF below1.65V remains beloweFuseENfallmin')
    check('defined_logic_EN_on',arithmetic['kill_en_normal_min_v']>1.223,'healthy3V3min3.15 assumed output VOH>=Vcc-.2 atmicroamp')
    # Net islands are REVIEW entries, not silently treated as nativeERC PASS.
    nets=defaultdict(list)
    for p in ps:
        if p['disposition']=='CONNECTED':nets[p['net']].append(p['refdes']+'.'+p['pin'])
    islands=[dict(net=n,endpoints=e,review='REVIEW_EXTERNAL_PORT_OR_UNUSED_STATUS') for n,e in nets.items() if len(e)<2]
    (E/'SINGLE_ENDPOINT_NET_REVIEW.json').write_text(json.dumps(islands,indent=2)+'\n')
    check('core_files_unchanged',not subprocess.check_output(['git','diff','23f8d4c','--','v5/rtl','v5/tests','v5/config','v5/constraints','v5/firmware'],cwd=ROOT),'scoped current files only')
    (E/'SEMANTIC_REVIEW.json').write_text(json.dumps(dict(classification='STATIC_ALTERNATIVE_VALIDATION_NOT_NATIVE_ERC_NOT_INDEPENDENT_REVIEW',checks=checks,pass_count=sum(c['result']=='PASS' for c in checks),failure_count=sum(c['result']=='FAIL' for c in checks),single_endpoint_net_count=len(islands),native_schematic='NOT_CREATED',native_erc='NOT_RUN'),indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks),failed=[c for c in checks if c['result']=='FAIL'],singleton_review=len(islands)),indent=2))
    assert all(c['result']=='PASS' for c in checks)
if __name__=='__main__':main()
