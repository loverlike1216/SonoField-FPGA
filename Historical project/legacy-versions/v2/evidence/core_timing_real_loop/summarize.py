"""Derive the bounded timing result from real Vivado reports (no hardware access)."""
from pathlib import Path
import collections
import csv
import json
import re

HERE = Path(__file__).resolve().parent


def timing(path):
    text = path.read_text(encoding='utf-8')
    match = re.search(r'WNS\(ns\).*?\n\s*-+.*?\n\s*([-\d.]+)\s+([-\d.]+)\s+(\d+)\s+(\d+)\s+([-\d.]+)\s+([-\d.]+)', text, re.S)
    if not match:
        raise ValueError(f'Missing timing summary: {path}')
    keys = ['wns_ns', 'tns_ns', 'setup_failing_endpoints', 'total_endpoints', 'whs_ns', 'ths_ns']
    return dict(zip(keys, map(float, match.groups())), report=path.relative_to(HERE).as_posix())


def write(name, obj):
    (HERE / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def main():
    reports = {name: timing(HERE / folder / 'timing_summary.rpt') for name, folder in {
        'original_synthesis': 'baseline/synthesis', 'round1_synthesis': 'round1/synthesis',
        'round1_postroute': 'round1/routed', 'round2_synthesis': 'round2/synthesis',
        'round2_postroute': 'round2/routed'}.items()}
    minimum_hz = 41500 * 256 * (2 * 4 + 3)
    profiles = []
    for mhz in [132.0, 123.75, 121.0, 118.8, 115.5, 99.0, 82.5]:
        stem = str(mhz)
        drc = (HERE / f'timing_refactor/trade/mmcm_{stem}MHz_drc.rpt').read_text()
        profiles.append(dict(core_mhz=mhz, shift_mhz=mhz / 2,
            minimum_phase_interval_cycles=int(mhz * 1e6 // (41500 * 256)),
            serializer_required_cycles=11, throughput_pass=mhz * 1e6 >= minimum_hz,
            throughput_margin_percent=100 * (mhz * 1e6 / minimum_hz - 1),
            mmcm_drc_errors=bool(re.search(r'\|\s*\S+\s*\|\s*(?:Error|Critical Warning)\s*\|', drc)),
            mmcm_scope='Synthesized primitive ratios checked; ZPS7-1 warning; NOT board clock qualification',
            fixed_route_screen=timing(HERE / f'timing_refactor/trade/screen_{stem}MHz.rpt')))
    rows = list(csv.DictReader((HERE / 'timing_refactor/trade/round2_failing_paths.tsv').open(), delimiter='\t'))
    write('critical_paths.json', dict(round2_worst_paths=rows[:20], failing_path_count=len(rows),
        endpoint_pin_classes=dict(collections.Counter(r['endpoint'].rsplit('/', 1)[-1] for r in rows)),
        original_synthesis=reports['original_synthesis'],
        critical_source='rtl/motion/motion_queue.sv: active[channel*17+:17], integer channel',
        hypothesis='Overwide variable index and selection; remaining CE fanout and internal async reset recovery paths need separate review'))
    write('clock_trade.json', dict(profiles=profiles, minimum_core_hz=minimum_hz,
        formula='41500 Hz * 256 phase states * (2*4 shift edges + LATCH + FINISH + new IDLE capture)',
        scope='Fixed-route STA diagnostic only, no fresh implementation at alternate frequencies',
        official_clock_profile_changed=False, selected_core_hz=132000000, selected_shift_hz=66000000))
    regression_path = HERE / 'final_regression/summary.json'
    regression = json.loads(regression_path.read_text()) if regression_path.exists() else {'status': 'RUNNING'}
    write('summary.json', dict(project_id='SONOFIELD_FPGA', active_version='v2',
        stage='CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST', status='CORE_TIMING_REVISE',
        gate_a='FAIL', gate_b='NOT_RUN_GATE_A_FAILED', timing=reports,
        physical_speed_grade='UNKNOWN', engineering_timing_target='xc7z020clg400-1',
        engineering_part_classification='CONSERVATIVE_ENGINEERING_ASSUMPTION',
        internal_latency_change_cycles=0, bounded_refactor_rounds=2,
        functional_regression=regression['status'], regression_evidence='final_regression/summary.json',
        equivalence=json.loads((HERE / 'timing_refactor/equivalence.json').read_text())['status'],
        axi_offline=json.loads((HERE / 'axi/axi_bridge_tests.json').read_text())['status'],
        real_uart='BLOCKED_BY_MISSING_ROUTE_EVIDENCE', real_ps_pl_loop='NOT_RUN',
        hardware_programmed=False, external_gpio_driven=False,
        implementation_scope='Routed OOC sono_axi_system internal paths; ideal primary clock; external input/output delays absent',
        starting_commit='b11c80ca3e7fc7745241c32f8f80d95329ca4ddf',
        result='REVISE', independent_acceptance='PENDING'))


if __name__ == '__main__':
    main()
