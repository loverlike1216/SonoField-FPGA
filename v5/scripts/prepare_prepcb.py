"""Materialize user-specified pre-PCB contracts without reading frozen history."""
from pathlib import Path
import csv, json, hashlib, subprocess, shutil, datetime
ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent

def write(path, text):
    p = ROOT/path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8', newline='\n')

def main():
    instruction = Path('G:/Users/loverlike/Desktop/26嵌入式比赛/md/SonoField_FPGA_v5_AX7020_PrePCB_Full_System_Codex61Sol_XHigh_2026-10-09.md')
    assets = [(instruction, REPO/'AI-interaction-memory/codex/instructions/v5_prepcb_full_system_20261009.md')]
    for name in ('阵列板.png', '中央板.png'):
        assets.append((Path('G:/Users/loverlike/Desktop/26嵌入式比赛/pcb')/name, ROOT/'docs/pre_pcb/references'/name))
    sources = []
    for a, b in assets:
        b.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(a, b)
        sources.append(dict(file=b.relative_to(REPO).as_posix(), sha256=hashlib.sha256(b.read_bytes()).hexdigest(),
                            source='ACTUAL_USER_ATTACHMENT', role='INSTRUCTION' if a.suffix == '.md' else 'CONCEPT_LAYOUT_NOT_PIN_AUTHORITY'))
    sources += [dict(url=url, checked='2026-10-09', type='PRIMARY_PUBLIC_NOT_REV3_MATCHED') for url in (
        'https://ax7020-20231-v101.readthedocs.io/zh-cn/latest/AX7020UserManual_CN/AX7020UserManual.html',
        'https://github.com/alinxalinx/AX7020_2023.1',
        'https://www.ti.com/lit/ds/symlink/tmp117.pdf',
        'https://sensirion.com/products/catalog/SHT45',
        'https://www.ti.com/product/SN74AXC8T245',
        'https://www.ti.com/product/TCA4307', 'https://www.ti.com/product/INA226',
        'https://www.microchip.com/en-us/product/TC4427A',
        'https://www.analog.com/en/products/ad7606b.html',
        'https://docs.amd.com/r/2025.2-English/ug903-vivado-using-constraints/About-Constraining-I/O-Delay')]
    write('docs/pre_pcb/SOURCES.json', json.dumps(sources, ensure_ascii=False, indent=2)+'\n')
    git = lambda *a: subprocess.check_output(['git', *a], cwd=REPO, text=True).strip()
    protected = {}
    for folder in ('rtl', 'firmware', 'software', 'tests', 'tb', 'simulation', 'config'):
        for f in (ROOT/folder).rglob('*'):
            if f.is_file() and git('ls-files', '--', f.relative_to(REPO).as_posix()) and '__pycache__' not in f.parts:
                protected[f.relative_to(ROOT).as_posix()] = hashlib.sha256(f.read_bytes()).hexdigest()
    if not (ROOT/'evidence/pre_pcb_20261009/S0_protected_hashes.json').exists():
        write('evidence/pre_pcb_20261009/S0_protected_hashes.json', json.dumps(protected, indent=2)+'\n')
    write('evidence/pre_pcb_20261009/REPOSITORY_RECONCILIATION.md', f'''# Repository reconciliation

Observed {datetime.datetime.now(datetime.timezone.utc).isoformat()}; project SONOFIELD_FPGA; active v5 unchanged.
Execution sandbox: independent clone `{REPO}`. Development branch `{git('branch','--show-current')}`.
Base HEAD `{git('rev-parse','HEAD')}`. Remote main `{git('rev-parse','origin/main')}`.
Migration PR#1 OPEN/DRAFT, head d7f7b60ae8ed9ed8bdee34c8738ce68aacd81743, not merged.
This branch is stacked on the migration candidate. Main merge remains user-gated.
Old sandbox and frozen archive contents were not read. Original new-sandbox working tree was clean.

Current inputs: root state/checkpoint CP-004, acceptance, decisions, blockers,
current v5 source/config, candidate connector CSV, actual new instruction and both PNGs.
S0_protected_hashes.json locks existing tracked inputs; new code is additional.
Existing canonical hashes and full 115-test/3696-frame×4 acceptance remain required.
Sources are v5/config/ooc_source_list.txt; new integration has an explicit additional list.
AX701020.3.0/XC7Z020/CLG400 are inherited read-only identification evidence, not re-measured now.
User states -2/I; full physical grade and Rev3 matched electrical details remain unverified.
Vitis drivers installed, target ARM compiler/BSP not yet qualified. No device operations.
''')
    old = list(csv.DictReader((ROOT/'hardware/integration_candidates/20261009/connector_pinmap_candidate.csv').open(encoding='utf-8-sig')))
    pins = []
    for r in old:
        net = r['v5_signal'] or r['documented_net']
        if r['connector'] == 'J11' and r['pin'] in ('32','33','34','35'):
            net = {'32':'TEMP_UP_SCL','33':'TEMP_UP_SDA','34':'TEMP_DN_SCL','35':'TEMP_DN_SDA'}[r['pin']]
            r['direction'] = 'OPEN_DRAIN'
        pins.append(dict(connector=r['connector'], connector_pin=r['pin'], package_pin=r['package_pin'],
                         bank=r['bank'], vcco=r['vcco'] or 'NOT_APPLICABLE', io_standard='LVCMOS33_CANDIDATE' if r['bank'] else 'NOT_APPLICABLE',
                         dir=r['direction'], net=net, clock_class='66MHz_CANDIDATE' if 'SRCLK' in net else '33MHz_CANDIDATE' if 'ADC_SCLK' in net else 'CONTROL_OR_DATA',
                         reset_level='OFF_OR_HIGH_Z', pull='EXTERNAL_DEFAULT_OFF_REQUIRES_REVIEW',
                         power_domain='CENTRAL_3V3_CANDIDATE', harness_pin=r['connector']+'.'+r['pin'],
                         source='ALINX_PUBLIC_MANUAL_AND_VIVADO_PACKAGE_DATABASE', verification='REV3_AND_VCCO_AND_TIMING_UNVERIFIED',
                         status='NON_DEPLOYABLE'))
    write('hardware/prepcb/AX7020_REV3_PINMAP.csv', '')
    with (ROOT/'hardware/prepcb/AX7020_REV3_PINMAP.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(pins[0])); w.writeheader(); w.writerows(pins)
    write('config/SIGNAL_CONTRACT.json', json.dumps(dict(active_version='v5', status='NON_DEPLOYABLE', pins=pins,
        geometry=dict(tx=128, rx=8, lanes=32, used_bits_per_595=4, pitch_mm=12, gap_mm=100),
        changed_candidate='Four of five spare GPIO allocated to two extra open-drain I2C segments; one spare remains. Original63 mapping retained.',
        sensors=[dict(location=k,address=a,required=True) for k,a in [('center',72),('upper',73),('lower',75)]],
        monitors=[dict(segment=k,address=64,part='INA226',status='CANDIDATE') for k in ('upper','lower')]), indent=2)+'\n')
    write('hardware/constraints/ax7020_candidate.xdc', '# NON_DEPLOYABLE. Deliberately errors on loading into a production flow.\nerror "Rev3 VCCO/pin/grade and offchip min/max timing not qualified"\n# Candidate assignments for review only:\n'+''.join(
        f'# set_property PACKAGE_PIN {p["package_pin"]} [get_ports {{{p["net"]}}}]\n' for p in pins if p['bank'] and p['net'] != 'RESERVED'))
    write('config/ax7020_power_budget.json', json.dumps(dict(status='CENTRAL_POWER_BUDGET_BLOCKED',
        central_source='AX7020_SINGLE_PROTECTED_5V_AND_SINGLE_PROTECTED_3V3_SOURCE', measured_header_capacity_A=None,
        measured_startup_A=None, measured_max_working_A=None, reverse_current_verified=False,
        array_supply_candidate=dict(voltage_V=12,rating_A=5,protection_baseline_A=2,usable_current_A=None),
        tx_equivalent_capacitance_F=None, continuous_drive_Vpp=None,
        illustrative_sweep=[dict(C_nF=c,V=v,f_Hz=f,ideal_capacitive_W_64=64*c*1e-9*v*v*f,measured=False)
          for c in (1,2,4) for v in (6,9,12) for f in (38500,40000,41500)],
        calculation_limits='Ideal charging scale only, hypothetical C values; excludes motional resonance, losses and measured NU40C10T power. Not authorization to drive.'),indent=2)+'\n')
    write('docs/pre_pcb/EXECUTION_CONTRACT.md', '''# v5 pre-PCB execution contract

Goal: S0-S7 offline software/RTL/algorithm/three-PCB preparation in existing v5.
Inputs: actual user full-system instruction and two sketches; current repository facts.
Architecture: preserve 128TX/8RX/32×4/8bit independent requested/calibration/common clock/atomic commit/50Hz.
Allowed: additive supervisory RTL, explicit PS/PL platform candidate, sensor/temperature/sparse solver,
negotiated optional protocol extensions, runtime path editor and tests, new working BOM and evidence.
Do not change: original goldens/thresholds, formal AD7606B, RX unknown, NU40C10T identity, frozen history.
Existing inherited core files remain fixed unless an explicit extension adapter is documented and reviewed.
Non-goals: version upgrade/main merge, board init/program/DDR access, physical acoustic acceptance, CAD/Gerber/orders.
Validation: original 115 tests+3696×4, new unit/fault tests, C host execution, two real simulators,
Vivado2025.2 PS7 candidate build/OOC route evidence, independent clean checkout/environment.
Evidence: actual logs/hashes/source commits/provenance, retain failures. No model self-certification.
Rollback: drop this development branch before merge; original migration candidate and physical sandbox persist.
Done: all feasible offline gates pass, physical holds recorded, S7 state/checkpoint and normal push verified.
''')

if __name__ == '__main__': main()
