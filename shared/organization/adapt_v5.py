"""Adapt only copied v5 metadata and paths; no old source mutations."""
from pathlib import Path
import json, re, hashlib
R=Path(__file__).resolve().parents[2]; V=R/'v5'
def write(p,t):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t,encoding='utf-8',newline='\n')
def put(p,d):write(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def change(rel,old,new):
    p=V/rel;t=p.read_text(encoding='utf-8');assert old in t,rel;write(p,t.replace(old,new))

if __name__=='__main__':
    for rel in ['software/ui/app.py','software/calibration/pipeline.py','software/calibration/database.py','software/acoustic_model/phase_lut_generator.py','scripts/run_motion_app.ps1']:
        p=V/rel;write(p,p.read_text(encoding='utf-8').replace('v2','v5'))
    change('scripts/pre_pcb_checks.py',"ROOT/'evidence/pre_pcb_board_ready/timing/baseline/motion_queue.sv'","ROOT/'simulation/golden/motion_queue.sv'")
    change('scripts/pre_pcb_checks.py',"ROOT/'evidence/pre_pcb_board_ready/timing/baseline/calibration_scheduler.sv'","ROOT/'simulation/golden/calibration_scheduler.sv'")
    change('scripts/timing_equivalence.py',"R/'evidence/core_timing_real_loop/baseline/burst_generator.sv'","R/'simulation/golden/burst_generator.sv'")
    c=json.loads((V/'config/system_baseline.json').read_text());c['project_version']='v5';put(V/'config/system_baseline.json',c)
    c=json.loads((V/'config/board_transport_profile.json').read_text());c.update(port=None,baudrate=None,exact_part=None,uart_route_verified=False,
        reason='AX7020 physical board revision,UART/COM route and PS/PL platform not verified; old COM4 Robei record is not inherited')
    put(V/'config/board_transport_profile.json',c)
    c=json.loads((V/'config/board_smoke_profile.json').read_text());c.update(engineering_part='xc7z020clg400-2',physical_speed_grade=None,
        classification='AX7020_DOCUMENTED_OOC_TARGET_NOT_DEPLOYABLE',part_provenance='ALINX_OFFICIAL_REFERENCE_NOT_PHYSICAL_IDENTIFICATION',
        clock_source='132MHZ_INTERNAL_DESIGN_TARGET_NOT_ACTUAL_BOARD_CLOCK',uart_route='UNVERIFIED_AX7020',uart_instance=None,uart_mio=None,
        ps_preset_tcl=None,ps_platform_xsa=None,target_bsp=None,physical_deployment='BLOCKED',board='ALINX AX7020')
    put(V/'config/board_smoke_profile.json',c)
    put(V/'config/board_facts.json',{'board':'ALINX AX7020','active_version':'v5','classification':'MANUFACTURER_DOCUMENTATION_NOT_PHYSICAL_VERIFICATION',
        'documented_part':'XC7Z020-2CLG400I','engineering_ooc_part':'xc7z020clg400-2','physical_part':None,'physical_board_revision':None,
        'documented_pl_clock_hz':50000000,'documented_pl_clock_pin':'U18','documented_ps_clock_hz':33333000,
        'documented_ddr_capacity_bytes':1073741824,'actual_ddr_capacity_bytes':None,'ps_preset_verified':False,'pins_verified':False,
        'actual_io_voltage':None,'production_xdc':None,'uart_com':None,'hardware_access_authorized_this_task':False,
        'source':'https://github.com/alinxalinx/AX7020_2023.1/tree/fcf1e4a239b0f47e8ee95dfde7c2eedc5685c327',
        'manual':'https://ax7020-20231-v101.readthedocs.io/zh-cn/latest/AX7020UserManual_CN/AX7020UserManual.html',
        'not_inherited':['Robei N18 clock','COM4/FTDI descriptors','512MiB D9PSK board candidate','J3-J6 connector assignments','old board XDC/preset']})
    for p in (V/'docs').rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        text=re.sub(r'\bv2\b','v5',text)
        text=text.replace('V2_REQUIREMENTS','V5_REQUIREMENTS')
        prefix=('> v5 inherited design/reference documentation. Original source is recorded in config/inheritance_manifest.json. '
                'Technical behavior/requirements are retained; historical numeric results are reference inputs, not v5 validation or AX7020 electrical qualification. '
                'Current board facts are config/board_facts.json; baseline results are evidence/BASELINE_VALIDATION.md.\n\n')
        write(p,prefix+text)
    # Record every copied path and which content changed; actual current hashes finalized before validation.
    p=V/'config/inheritance_manifest.json';m=json.loads(p.read_text(encoding='utf-8'))
    for item in m['files']:
        dest=R/item['target'];now=hashlib.sha256(dest.read_bytes()).hexdigest()
        item['classification']='COPY_AS_IS' if now==item['source_sha256_bytes'] else 'COPY_AND_UPDATE'
        item['initial_copy_sha256_bytes']=item['source_sha256_bytes']
    put(p,m)
    print('Adapted only v5 metadata, UI identity, golden-fixture paths and AX7020 fail-closed board profiles')
