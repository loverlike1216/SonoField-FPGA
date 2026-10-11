"""Summarize observed S3 validation; frozen archive checked as Git metadata only."""
from pathlib import Path
import datetime, hashlib, json, subprocess

R = Path(__file__).resolve().parents[1]
ROOT = R.parents[4]
E = ROOT/'v5/evidence/pcb_s3_20261011'
BASE = '23f8d4cedb44536f8c35fd132171868a80f9ded7'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True, encoding='utf-8').strip()


def load(name):
    return json.loads((E/name).read_text(encoding='utf-8'))


def main():
    tests = (E/'unit_243.log').read_text(encoding='utf-8')
    assert 'Ran 243 tests' in tests and tests.rstrip().endswith('OK')
    checks = {}
    for name in ['STRUCTURE_CHECK.json','INHERITANCE_CHECK.json','PROTECTED_HASH_CHECK.json',
                 'HARDWARE_MODEL_CHECK.json','WORKSPACE_INTEGRITY.json','SEMANTIC_REVIEW.json',
                 'WORKBOOK_VERIFICATION.json']:
        data = load(name)
        if name == 'SEMANTIC_REVIEW.json':
            assert data['failure_count'] == 0 and data['pass_count'] == 45
            assert data['single_endpoint_net_count'] == 0
            assert all(row['result'] == 'PASS' for row in data['checks'])
        else:
            assert data.get('status') == 'PASS', (name, data)
        checks[name] = 'PASS'
    core = ['v5/rtl','v5/tests','v5/config','v5/constraints','v5/firmware','v5/software','v5/tb','v5/simulation','v5/scripts']
    assert git('diff', BASE, '--name-only', '--', *core) == ''
    assert git('diff', BASE, '--name-only', '--', 'v5/hardware/pcb/reviews/20261011_s2','v5/evidence/pcb_s2_20261011') == ''
    archive = git('rev-parse', BASE+':Historical project')
    assert git('rev-parse', 'HEAD:Historical project') == archive
    assert git('diff', BASE, '--name-only', '--', 'Historical project') == ''
    p = ROOT/'AI-problem/problem/P-20261011-001__pcb-safety-and-electrical-gates.md'
    body = p.read_text(encoding='utf-8').replace('\r\n','\n').split('---\n\n',1)[1]
    assert hashlib.sha256(body.encode()).hexdigest() == 'ff10749ee46342eae17ecc5eff632b9131055199be6eb2cfb0583c16d79ec77f'
    result = dict(status='PASS_WITH_RELEASE_GATES',project_id='SONOFIELD_FPGA',active_version='v5',
        branch=git('branch','--show-current'),base_commit=BASE,recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        scope='Candidate artifacts and original digital preservation; not electrical/hardware acceptance',
        fresh_digital_tests=dict(count=243,status='PASS',command='python -m unittest discover -s v5/tests -v',
            raw_log_local_only='unit_243.log',raw_log_sha256=hashlib.sha256((E/'unit_243.log').read_bytes()).hexdigest(),
            evidence_boundary='Real local test execution; no board operation'),
        checks=checks,semantic_checks=45,safety_boolean_combinations=256,board_local_singleton_nets=0,
        workbooks=load('WORKBOOK_VERIFICATION.json'),candidate_counts=load('CANDIDATE_COUNTS.json'),
        vector_pages=len(json.loads((R/'svg/INDEX.json').read_text())),
        inherited_not_rerun=['S2 3696frames x3 Icarus +1 XSim','Prior OOC synthesis/routing; no new board timing proof'],
        unchanged=dict(digital_core_paths=core,S2_review_and_evidence=True,problem_body=True,
            historical_tree=archive,historical_body_read=False,sole_active_version=True),
        native_schematic='NOT_CREATED',native_erc='NOT_RUN',independent_review='PENDING',
        spice_ibis='NOT_RUN',hardware='NOT_VERIFIED',release_result='REVISE',
        release_gates=['G1 nativeCAD/independent review','G2 power/fault/thermal','G3 AFE/protection/power-off isolation',
                       'G4 actual digital integration/VCCO/externalSTA/BRAM','G5 mechanical/SKUs'],
        holds=['Manufacturing','Procurement','Board write','Main merge'])
    (E/'FINAL_VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('S3 observed validation recorded; REVISE release gates retained')


if __name__ == '__main__':
    main()
