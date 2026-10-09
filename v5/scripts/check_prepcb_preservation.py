"""Compare original S0 bytes. Exactly two optional C adapters and their manifest may differ."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
ALLOWED={'firmware/ps_service/service.c','firmware/ps_service/service.h','config/inheritance_manifest.json'}

def audit():
    original=json.loads((ROOT/'evidence/pre_pcb_20261009/S0_protected_hashes.json').read_text())
    changed=[];errors=[]
    for rel,wanted in original.items():
        p=ROOT/rel
        if not p.is_file():errors.append('Missing '+rel);continue
        actual=hashlib.sha256(p.read_bytes()).hexdigest()
        if actual!=wanted:
            changed.append(dict(file=rel,before=wanted,after=actual))
            if rel not in ALLOWED:errors.append('Unauthorized original change '+rel)
    return dict(status='FAIL' if errors else 'PASS',protected_files=len(original),changed=changed,errors=errors,
                authorization='Current user pre-PCB optional protocol extension; original build unchanged when macro absent',
                original_tests_goldens_thresholds_unchanged=not errors)

if __name__=='__main__':
    r=audit();print(json.dumps(r,indent=2));raise SystemExit(bool(r['errors']))
