"""Audit every current file snapshotted at S0, without opening frozen content."""
from pathlib import Path
import hashlib, json, subprocess

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT/'v5/evidence/next_stage/20261010'
ALLOWED = {'README.md', 'AGENTS.md', '.gitignore', '.gitattributes', '.github/workflows/workspace-integrity.yml',
    'CHANGELOG.md', 'AI-interaction-memory/INDEX.md', 'AI-chat-memory/INDEX.md', 'AI-problem/INDEX.md',
    'AI-problem/decision/P-20261008-001__adc-40khz-bandwidth.md',
    'v5/config/inheritance_manifest.json', 'v5/scripts/check_prepcb_preservation.py'}
ALLOWED.update('shared/'+name for name in ('PROJECT_STATE.md', 'PROJECT_STATE.json', 'VERSION_STATE.json',
    'CURRENT_PLAN.md', 'DECISIONS.md', 'BLOCKERS.md', 'ACCEPTANCE.md', 'CONTEXT_CHECKPOINT.md',
    'CONTEXT_CHECKPOINT.json', 'HANDOFF.md'))

def audit():
    snapshot = json.loads((EVIDENCE/'S0_PROTECTED_HASHES.json').read_text(encoding='utf-8'))
    reviewed = json.loads((ROOT/'v5/config/nextstage_reviewed_changes.json').read_text(encoding='utf-8'))['files']
    pinned = {'v5/'+name: value['after_raw_sha256'] for name,value in reviewed.items()}
    changed, errors = [], []
    immutable = 0
    for rel, old in snapshot.items():
        if rel.split('/',1)[0] in {'Historical project', 'history_old'}:
            errors.append('Forbidden historical body in S0 snapshot: '+rel)
            continue
        path = ROOT/rel
        if not path.is_file():
            errors.append('Missing original current file: '+rel)
            continue
        current = hashlib.sha256(path.read_bytes()).hexdigest()
        if rel.startswith(('v5/tests/', 'v5/tb/', 'v5/simulation/', 'v5/evidence/', 'v5/hardware/bom/')):
            immutable += 1
            if current != old['raw_sha256']:
                errors.append('Immutable test/golden/evidence/BOM changed: '+rel)
        if current != old['raw_sha256']:
            authorized = rel in ALLOWED or pinned.get(rel) == current
            changed.append(dict(path=rel, before=old['raw_sha256'], after=current, authorized=authorized))
            if not authorized:
                errors.append('Unreviewed S0 change: '+rel)
    base = 'b08ccf58c984ca7e6250d9e8489a24bc0789c4b0'
    def tree(ref):
        raw = subprocess.check_output(['git','ls-tree','-r','-z',ref,'--','Historical project'],cwd=ROOT)
        return sorted(raw.split(b'\0')[:-1])
    frozen_before, frozen_now = tree(base), tree('HEAD')
    if frozen_before != frozen_now or len(frozen_now) != 3918:
        errors.append('Frozen archive Git blob/mode/path metadata mismatch')
    return dict(status='FAIL' if errors else 'PASS', s0_files=len(snapshot),
        immutable_tests_goldens_evidence_bom_files=immutable, changed=changed, errors=errors,
        frozen_metadata_files=len(frozen_now), frozen_body_read=False, old_physical_workspace_accessed=False)

if __name__ == '__main__':
    result = audit()
    print(json.dumps(result,indent=2))
    raise SystemExit(bool(result['errors']))
