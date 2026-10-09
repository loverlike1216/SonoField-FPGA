"""Verify immutable parent and full inherited source coverage; usable in a sparse v2 clone."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent


def audit():
    frozen = json.loads((REPO / 'shared/versions/v1_freeze.json').read_text(encoding='utf-8'))
    inventory = json.loads((ROOT / 'docs/architecture/migration_inventory.json').read_text(encoding='utf-8'))
    errors = []
    git = lambda *args: subprocess.check_output(['git', *args], cwd=REPO, text=True).strip()
    parent_tree = git('rev-parse', frozen['source_commit'] + ':v1')
    if git('rev-parse', 'HEAD:v1') != parent_tree:
        errors.append('Frozen v1 Git tree changed')
    if (REPO / 'v1').exists():
        for name, digest in frozen['sha256'].items():
            p = REPO / name
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
                errors.append('Frozen working file changed: ' + name)
    if {i['source'] for i in inventory} != set(frozen['sha256']):
        errors.append('Migration inventory does not cover all parent files')
    classifications = []
    for item in inventory:
        p = REPO / item['target']
        if not p.is_file():
            errors.append('Missing inherited asset: ' + item['target'])
            continue
        # Git text normalization can differ from original Windows bytes.
        original = subprocess.check_output(['git', 'show', frozen['source_commit'] + ':' + item['source']], cwd=REPO)
        current = p.read_bytes()
        same = original == current or original.replace(b'\r\n', b'\n') == current.replace(b'\r\n', b'\n')
        relative = item['source'][3:]
        immutable = relative.startswith(('rtl/', 'tb/', 'software/', 'tests/', 'config/', 'evidence/')) or relative.startswith('requirements')
        permitted_metadata = False
        if relative == 'config/board_facts.json':
            expected = json.loads(original); expected['source_path_base'] = 'v2'
            permitted_metadata = json.loads(current) == expected
        elif relative == 'software/acoustic_model/phase_lut_generator.py':
            expected = original.replace(b'v1 only implements', b'v2 baseline only implements')
            permitted_metadata = expected.replace(b'\r\n', b'\n') == current.replace(b'\r\n', b'\n')
        if immutable and not same and not permitted_metadata:
            errors.append('Unexpected inherited functional/evidence change: ' + item['target'])
        classifications.append({'path': item['target'], 'classification': 'COPY_UNCHANGED' if same else 'COPY_AND_EXTEND'})
    for folder in ('rtl', 'tb', 'software', 'tests', 'config'):
        for p in (ROOT / folder).rglob('*'):
            if p.suffix in ('.py', '.sv', '.json', '.tcl'):
                text = p.read_text(encoding='utf-8').replace('\\', '/')
                if '../v1' in text or 'from v1' in text or 'import v1' in text:
                    errors.append('Runtime depends on v1: ' + str(p.relative_to(ROOT)))
    return {'status': 'FAIL' if errors else 'PASS', 'errors': errors, 'frozen_v1_tree': parent_tree,
            'frozen_files': frozen['file_count'], 'v1_worktree_present': (REPO / 'v1').exists(),
            'coverage_files': len(inventory), 'classifications': classifications}


if __name__ == '__main__':
    result = audit()
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(result['errors']))
