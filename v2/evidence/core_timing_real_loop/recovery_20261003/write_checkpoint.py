"""Persist reconciled v2 facts; no HDL, board, clock or acceptance changes."""
from pathlib import Path
import hashlib
import json
import subprocess
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]


def main():
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
    state = json.loads((REPO / 'shared/PROJECT_STATE.json').read_text(encoding='utf-8'))
    versions = json.loads((REPO / 'shared/VERSION_STATE.json').read_text(encoding='utf-8'))
    stage = json.loads((HERE / 'summary.json').read_text())
    regression = json.loads((HERE.parent / stage['regression_evidence']).read_text())
    assert state['active_version'] == versions['active_version'] == 'v2'
    assert regression['status'] == 'PASS', 'Do not claim a completed recovery before real gate PASS'
    source = json.loads((HERE / 'continuity_baseline.json').read_text())
    preserved = source['historical_file_sha256'] | source['protected_engineering_sha256']
    justified = json.loads((HERE / 'justified_changes.json').read_text())['changes']
    for path, change in justified.items():
        assert preserved[path] == change['before_sha256'], 'Wrong change baseline'
        assert hashlib.sha256((REPO / path).read_bytes()).hexdigest() == change['after_sha256'], 'Stale fix evidence'
    changed = [p for p, digest in preserved.items()
               if p not in justified and (not (REPO / p).is_file() or hashlib.sha256((REPO / p).read_bytes()).hexdigest() != digest)]
    assert not changed, 'Protected files changed: ' + str(changed)
    protected_report = {'current_model': 'GPT-6.1 Sol High', 'status': 'PASS',
                        'protected_files': len(preserved), 'unexpected_changes': changed,
                        'evidence_justified_changes': justified,
                        'scope': 'Historical files, RTL/config unchanged; measured local GUI evidence fix recorded'}
    (HERE / 'continuity_verification.json').write_text(json.dumps(protected_report, indent=2) + '\n')
    cp = {
        'checkpoint_id': 'CP-20261003-001', 'project_id': 'SONOFIELD_FPGA',
        'project_name': 'SonoField-FPGA', 'repository': state['repository'],
        'workspace_path': state['workspace_path'], 'branch': 'main',
        'base_commit': 'b11c80ca3e7fc7745241c32f8f80d95329ca4ddf', 'head_commit': head,
        'commit_scope': 'Validated engineering source commit; later checkpoint-only commits may follow',
        'active_version': 'v2', 'version_status': 'ACTIVE', 'current_stage': state['current_stage'],
        'current_model': 'GPT-6.1 Sol High', 'model_provenance_basis': 'USER_DECLARED_MANUAL_SELECTION',
        'created_at': datetime.now(timezone.utc).isoformat(), 'created_by': 'Codex', 'source_of_truth': 'repository',
        'checkpoint_reason': 'Model continuity, user replacement policy, bounded timing RCA and recovery regression',
        'current_goal': 'Single Robei octagonal Zynq-7020 sound-field controller; measured levitation roadmap, 50 mg final target',
        'architecture_ref': 'v2/docs/architecture/SELF_CALIBRATION.md',
        'architecture': 'Host solver/commands -> PS transport (not deployed) -> AXI bridge -> deterministic common PL phase/calibration/motion -> serializer -> qualified drivers/transducers (not deployed)',
        'completed': [
            {'item': '128-channel common phase, calibration and atomic maps', 'status': 'SIMULATED'},
            {'item': 'Exact rational phase and burst timing refactors', 'status': 'SIMULATED', 'added_latency_cycles': 0},
            {'item': 'Offline protocol/host C/AXI/safe leaf', 'status': 'TESTED'},
            {'item': 'Current motion/calibration/inherited regression', 'status': 'SIMULATED'},
            {'item': 'Conservative -1 OOC core', 'status': 'SYNTHESIZED', 'post_route_timing': 'FAIL'},
            {'item': 'Historical board JTAG identity', 'status': 'HARDWARE_VERIFIED', 'scope': 'Identity only, not system function'}],
        'current_plan_position': 'Two timing rounds exhausted; recovery regression complete; next bounded timing decision pending',
        'next_actions': [
            'Read P-20260929-001 and real routed path/throughput evidence; obtain independent bounded timing decision',
            'Establish real UART-to-PS route and reviewed PS preset/XSA/BSP/ARM toolchain',
            'After Gate A plus prerequisites pass, run temporary-JTAG bare-board safe transport',
            'Qualify driver electrical timing and measured opposing-pair acoustics before array/particle scaling'],
        'active_decisions': [
            {'problem_id': 'P-20260927-001', 'decision': 'APPROVE_LIMITED_TIMING_REFACTOR_IN_V2',
             'source': 'Direct user formal attachment, preserved approval file',
             'scope': 'Two rounds at 132/66 MHz and quantified trade; exhausted, no third round',
             'problem_hash': '0bf40cdd79faaf5fd4aca4af6e1f7cf85eab8662128f4633ea1acb3b4ef61916'},
            {'decision': 'MODEL_TRANSITION', 'date': '2026-10-03', 'source': 'Direct user', 'scope': 'Provenance only'},
            {'decision': 'ACTIVE_V2_SINGLE_BOARD_ONLY', 'date': '2026-10-03', 'source': 'Direct user', 'scope': 'Recovery focus'}],
        'blockers': ['CORE_TIMING', 'UART_ROUTE', 'PS_TARGET_BUILD', 'B01', 'B03', 'B04', 'B05', 'B06', 'B07'],
        'critical_issues': [],
        'latest_validation': [
            {'type': 'Functional regression', 'result': 'PASS', 'evidence': 'v2/evidence/core_timing_real_loop/' + stage['regression_evidence'],
             'date': '2026-10-03', 'commit': head, 'python_tests': 114, 'trajectory_frames': regression['frame_count'],
             'deterministic_runs': regression['determinism']['runs']},
            {'type': 'Exact-cycle cross-tool equivalence', 'result': 'PASS', 'date': '2026-09-29',
             'phase_comparisons': 486026, 'burst_comparisons': 5066261,
             'evidence': 'v2/evidence/core_timing_real_loop/timing_refactor/equivalence.json'},
            {'type': 'Historical latest routed timing', 'result': 'FAIL', 'date': '2026-09-29',
             'wns_ns': -4.515, 'tns_ns': -6007.936, 'whs_ns': 0.070, 'ths_ns': 0,
             'evidence': 'v2/evidence/core_timing_real_loop/round2/routed/timing_summary.rpt'},
            {'type': 'Physical PS/PL transport', 'result': 'NOT_VERIFIED', 'evidence': 'v2/evidence/core_timing_real_loop/board_smoke/preflight.json'}],
        'known_limitations': ['Conservative engineering -1 target; physical speed/temperature/order UNKNOWN',
            'OOC ideal primary clock, external I/O delays missing; full-board timing not qualified',
            'No real PS firmware, UART loop, acoustic outputs, calibration or levitation',
            'Failed previous GUI retry retained; new PASS does not rewrite its history',
            'External ChatGPT history BLOCKED; local visible interaction coverage PARTIAL',
            'Fresh clone follows documented sparse v2 workflow because frozen raw-byte hashes are sensitive to CRLF conversion'],
        'do_not_change': ['Frozen v1 and historical evidence', 'PCB files and unverified board constraints',
            'Current register/packet/channel formats and motion ACK/cadence', 'Acceptance thresholds',
            'Core architecture or next-version creation without applicable decision/user authorization'],
        'invariants': ['128-channel/8-bit phase', 'Separate requested/calibration modulo256',
            'Common coherent PL timing', 'Complete-map atomic commit', 'Safe reset and disable',
            '38.5-41.5 kHz contract; production132/66MHz until valid decision',
            '10 mm body/12 mm radiating-center pitch/100 mm nominal face gap/90-115 mm range/geometric-center origin'],
        'open_ai_problems': state['open_ai_problems'],
        'state_conflicts': [{'old': 'Older narrative plan and machine evidence pointers describe previous stage',
            'current': 'Preserved routed FAIL plus current recovery PASS govern the active checkpoint',
            'resolution': 'Current plan/state/evidence references reconciled; historical content retained'},
            {'old': 'Old summary said regression RUNNING although its final GUI retry failed',
             'current': 'Failed retry remains FAIL, separate recovery PASS is current', 'resolution': 'No historical reports overwritten'}],
        'repository_delta': 'Pending phase/burst/safe-leaf implementation and tests now checkpointed; current model/event/policy/state/plan restored from actual evidence',
        'evidence_refs': ['v2/evidence/core_timing_real_loop/RESULT.md',
            'v2/evidence/core_timing_real_loop/recovery_20261003/summary.json',
            'v2/evidence/core_timing_real_loop/critical_paths.json', 'v2/evidence/core_timing_real_loop/clock_trade.json',
            'v2/evidence/core_timing_real_loop/axi/axi_bridge_tests.json',
            'v2/evidence/core_timing_real_loop/uart/uart_route_evidence.json',
            'AI-interaction-memory/codex/I-20261003-0001__model-transition.md'],
        'resume_from': 'Read this checkpoint, then current plan and P-20260929-001; remain in current v2 single-board scope',
        'status': 'VALID', 'stage_acceptance': 'REVISE', 'independent_review': 'PENDING'}
    fresh = json.loads((HERE / 'fresh_checkout.json').read_text())
    assert fresh['status'] == 'PASS' and fresh['source_commit'] == head
    cp['latest_validation'].append({'type': 'Fresh sparse checkout / 114 tests / structure / interaction integrity',
        'result': 'PASS', 'date': '2026-10-03', 'commit': head,
        'classification': fresh['classification'],
        'evidence': 'v2/evidence/core_timing_real_loop/recovery_20261003/fresh_checkout.json',
        'limitation': 'Same machine, existing pinned venv; not a second physical machine'})
    lines = [f'---\ncheckpoint_id: {cp["checkpoint_id"]}\nproject_id: SONOFIELD_FPGA\nactive_version: v2\n'
             f'current_stage: {cp["current_stage"]}\nbase_commit: {cp["base_commit"]}\nhead_commit: {head}\n'
             f'project_name: SonoField-FPGA\nrepository: {cp["repository"]}\nbranch: main\nversion_status: ACTIVE\n'
             f'created_at: {cp["created_at"]}\ncreated_by: Codex\ncheckpoint_reason: {cp["checkpoint_reason"]}\n'
             'current_model: GPT-6.1 Sol High\nsource_of_truth: repository\nstatus: VALID\n---\n',
             '# Context Checkpoint\n',
             'This is a recoverable engineering-state checkpoint, not a version change or platform acceptance. Stage result: REVISE.\n']
    sections = [('1. Current Identity', {k: cp[k] for k in ('project_id','repository','workspace_path','branch','head_commit','active_version','current_stage','current_model')}),
        ('2. Current Goal', cp['current_goal']), ('3. Architecture', cp['architecture']), ('4. Completed', cp['completed']),
        ('5. Current Plan Position', cp['current_plan_position']), ('6. Next Actions', cp['next_actions']),
        ('7. Active Decisions', cp['active_decisions']), ('8. Blockers / Critical Issues', {'blockers': cp['blockers'], 'critical_issues': []}),
        ('9. Latest Validation', cp['latest_validation']), ('10. Known Limitations', cp['known_limitations']),
        ('11. Do Not Change', cp['do_not_change']), ('12. Invariants', cp['invariants']), ('13. Open AI Problems', cp['open_ai_problems']),
        ('14. Repository Delta Since Previous Checkpoint', cp['repository_delta']), ('15. Resume Instruction', cp['resume_from']),
        ('16. Evidence References', cp['evidence_refs']), ('17. Provenance', 'Real files/decisions/tool reports and current Git HEAD; user model selection; no fabricated Chat decision'),
        ('State Conflicts', cp['state_conflicts'])]
    for title, value in sections:
        lines.append('\n## ' + title + '\n\n' + (value if isinstance(value, str) else '```json\n' + json.dumps(value, indent=2, ensure_ascii=False) + '\n```') + '\n')
    document = ''.join(lines)
    (REPO / 'shared/CONTEXT_CHECKPOINT.json').write_text(json.dumps(cp, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    (REPO / 'shared/CONTEXT_CHECKPOINT.md').write_text(document, encoding='utf-8')
    archive = REPO / 'shared/context-checkpoints/CP-20261003-001__v2__core-timing-recovery.md'
    archive.parent.mkdir(exist_ok=True)
    assert not archive.exists(), 'Never overwrite a historical checkpoint'
    archive.write_text(document, encoding='utf-8')
    print(json.dumps({'checkpoint': cp['checkpoint_id'], 'status': 'VALID', 'protected_files': len(preserved)}))


if __name__ == '__main__':
    main()
