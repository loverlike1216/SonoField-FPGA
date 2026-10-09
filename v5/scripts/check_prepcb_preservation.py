"""Preserve original S0 bytes; separately pinned user-approved C16 adaptations."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
ALLOWED={'firmware/ps_service/service.c','firmware/ps_service/service.h','config/inheritance_manifest.json'}
REVIEWABLE={'rtl/sono_digital_system.sv','rtl/sono_motion_system.sv','rtl/sono_axi_system.sv','rtl/board/prepcb_pl.v','config/system_baseline.json','config/hardware_parts.json'}

def audit():
    original=json.loads((ROOT/'evidence/pre_pcb_20261009/S0_protected_hashes.json').read_text())
    changed=[];errors=[]
    review_path=ROOT/'config/nextstage_reviewed_changes.json'
    reviewed=json.loads(review_path.read_text())['files'] if review_path.exists() else {}
    if set(reviewed)-REVIEWABLE:errors.append('Review manifest cannot exempt tests/goldens/thresholds or unrelated files')
    for rel,wanted in original.items():
        p=ROOT/rel
        if not p.is_file():errors.append('Missing '+rel);continue
        actual=hashlib.sha256(p.read_bytes()).hexdigest()
        if actual!=wanted:
            changed.append(dict(file=rel,before=wanted,after=actual))
            if rel not in ALLOWED and reviewed.get(rel,{}).get('after_raw_sha256')!=actual:errors.append('Unauthorized original change '+rel)
    return dict(status='FAIL' if errors else 'PASS',protected_files=len(original),changed=changed,errors=errors,
                authorization='Original optional C adapters plus exact pinned current user-approved C16 parameter/config adaptations; tests/goldens/thresholds never exempted',
                original_tests_goldens_thresholds_unchanged=not errors)

if __name__=='__main__':
    r=audit();print(json.dumps(r,indent=2));raise SystemExit(bool(r['errors']))
