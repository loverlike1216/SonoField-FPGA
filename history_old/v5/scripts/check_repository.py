"""Audit v2 layout, live evidence, frozen-parent coverage and decision provenance."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
from check_migration import audit as audit_migration

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent


def verify_problem(path):
    """Verify either canonical-body SHA256 or the existing adjacent whole-file digest.

    Schematic-stage problems already use an adjacent .sha256 file. Supporting
    that format preserves their original record instead of rewriting its hash.
    """
    text=path.read_text(encoding='utf-8');_,front,body=text.split('---\n',2)
    metadata=dict(line.split(': ',1) for line in front.strip().splitlines())
    expected=metadata['problem_hash']
    if expected=='SEE_ADJACENT_SHA256_FILE':
        parts=path.with_suffix('.sha256').read_text(encoding='utf-8').strip().split()
        if len(parts)!=2 or parts[1]!=path.name or not re.fullmatch('[0-9a-f]{64}',parts[0]):
            raise ValueError('Invalid adjacent problem digest')
        valid=hashlib.sha256(text.encode('utf-8')).hexdigest()==parts[0]
    else:
        valid=bool(re.fullmatch('[0-9a-f]{64}',expected)) and hashlib.sha256(body.encode('utf-8')).hexdigest()==expected
    return metadata,valid


def main():
    from check_structure import audit as structure_audit
    migration=audit_migration();structure=structure_audit()
    errors=migration['errors']+structure['errors']
    result={'status':'FAIL' if errors else 'PASS','errors':errors,'inheritance':migration,'structure':structure,
            'scope':'Current v5 local integrity; historical management checked separately, no old source loads'}
    print(json.dumps(result,indent=2))
    if errors:raise SystemExit(1)

if __name__=='__main__':main()
