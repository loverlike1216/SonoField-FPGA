"""Integrity gates for the 2026-10-09 v5 read-only integration checkpoint.

No hardware access. A passing check does not accept the electrical platform.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess

V = Path(__file__).resolve().parents[1]
R = V.parent
E = V / 'evidence/board_bringup/20261009'


def main():
    checks = []
    def check(name, ok, detail):
        checks.append(dict(name=name, status='PASS' if ok else 'FAIL', detail=detail))
        if not ok:
            raise AssertionError(name)
    load = lambda rel: json.loads((R / rel).read_text(encoding='utf-8'))
    state = load('shared/PROJECT_STATE.json')
    version = load('shared/VERSION_STATE.json')
    cp = load('shared/CONTEXT_CHECKPOINT.json')
    facts = load('v5/config/board_facts.json')
    baseline = load('v5/evidence/baseline/board_integration_20261009/summary.json')
    check('version_stage_continuity', state['active_version'] == version['active_version'] == cp['active_version'] == 'v5'
          and version['highest_version'] == 'v5' and not version['upgrade_pending'] and state['current_stage'] == cp['current_stage'], 'No version upgrade or architecture change')
    check('full_baseline_pass', baseline['status'] == 'PASS' and all(item['exit_code'] == 0 for item in baseline['commands']), 'Actual archived full baseline outcomes')
    hashes = baseline.get('source_sha256', baseline.get('source_hashes', {}))
    # The baseline has many file kinds; scope this equality gate to production code/tests.
    selected = {p: sha for p, sha in hashes.items() if p.split('/')[0] in ('rtl', 'software', 'firmware', 'tb', 'tests')}
    check('production_sources_unchanged_after_baseline', bool(selected) and all(hashlib.sha256((V / p).read_text(encoding='utf-8').encode()).hexdigest() == sha for p, sha in selected.items()), {'files': len(selected), 'hash_scope': 'UTF-8 LF-normalized text, identical to run_baseline.py'})
    check('unverified_physical_fields_not_promoted', facts['physical_part'] is None and facts['actual_ddr_capacity_bytes'] is None
          and facts['actual_io_voltage'] is None and facts['production_xdc'] is None and not facts['ps_preset_verified'], 'JTAG/controller width does not prove grade, topology, capacity or VCCO')
    check('original_bom_unchanged', hashlib.sha256((V / 'hardware/bom/submissions/2026-10-08/BOM_AX7020_NU40C10T_2026-10-08.xlsx').read_bytes()).hexdigest()
          == 'decf6b026c0b5a48efb6800d27463246d61f62a9e2de01c75da5012d7fe69a35', 'Original submission byte identity')
    check('candidate_package_rows_complete', len(list(csv.DictReader((V / 'hardware/integration_candidates/20261009/package_procurement_audit.csv').open(encoding='utf-8-sig')))) == 72, 'All rows have explicit package/procurement disposition; native library check still absent')
    for name in ('adc_candidate_icarus.log', 'adc_candidate_xsim.log'):
        check(name, 'ADC_CANDIDATE_SERIAL_PASS frames=256' in (E / name).read_text(encoding='utf-8'), 'Actual self-checking simulator marker')
    candidate = json.loads((E / 'candidate_checks.json').read_text(encoding='utf-8'))
    check('candidate_checks_and_release_scope', candidate['status'] == 'PASS' and len(candidate['checks']) == 15
          and candidate['hardware_tests'] == 'NOT_RUN' and state['bom_electrical_release'] == 'HOLD', 'Offline tests do not release hardware')
    problem = (R / 'AI-problem/problem/P-20261009-001__ax7020-revision-ps-platform.md').read_text(encoding='utf-8')
    front, body = problem.split('---\n\n', 1)
    expected = re.search(r'problem_hash: ([0-9a-f]{64})', front).group(1)
    check('open_problem_hash', hashlib.sha256(body.encode()).hexdigest() == expected, 'No fabricated Decision or stale body hash')
    check('checkpoint_snapshot_matches', (R / 'shared/CONTEXT_CHECKPOINT.md').read_bytes()
          == (R / 'shared/context-checkpoints/CP-20261009-001__v5__ax7020-board-bom.md').read_bytes(), 'Latest and archived checkpoint agree at publication')
    old_paths = ['v1', 'v2', 'archive', 'PCB']
    touched = subprocess.check_output(['git', 'diff', '--name-only', cp['base_commit'], '--', *old_paths], cwd=R, text=True).strip()
    check('frozen_tracked_history_unchanged', not touched, 'No frozen tracked source/PCB change; untracked preexisting user assets excluded')
    for filename in ('ax7020_readonly.tcl', 'ax7020_ps_readonly.tcl', 'ax7020_results_gui.tcl'):
        text = (V / 'scripts' / filename).read_text(encoding='utf-8')
        check(filename + '_no_mutating_command', not re.search(r'(?m)^\s*(?:stop|rst|dow|mwr|ps7_init|program_hw_devices)\b', text), 'Read-only audit only; not a general Tcl safety verifier')
    evidence_refs = cp['evidence_refs']
    check('checkpoint_evidence_exists', all((R / rel).exists() for rel in evidence_refs), 'All explicit current evidence references resolve')
    report = dict(status='PASS', project_id='SONOFIELD_FPGA', active_version='v5', model='GPT-6.1 Sol High',
        checks=checks, scope='REPOSITORY_INTEGRITY_ONLY', hardware_acceptance='REVISE', manufacturing='HOLD',
        fake_implementation_review=dict(scope='Current rtl/software/firmware/candidate source grep', findings=[
            'No new TODO/FIXME/stub/fake implementation found in active production sources.',
            'disabled matches are safety/UI states; real serial map capability intentionally disabled until board integration, not a passed runtime feature.',
            'Candidate ROM and functional safety abstraction explicitly incomplete as electrical/production implementation; native schematic/real hardware remain NOT_RUN.']))
    (E / 'final_integrity.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(status='PASS', checks=len(checks), hardware_acceptance='REVISE')))


if __name__ == '__main__':
    main()
