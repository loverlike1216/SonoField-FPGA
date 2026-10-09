"""Check standalone v5 copy completeness without reading old-version files."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def audit():
    manifest=json.loads((ROOT/'config/inheritance_manifest.json').read_text(encoding='utf-8'));errors=[]
    for item in manifest['files']:
        rel=Path(item['target']).relative_to('v5');p=ROOT/rel
        if not p.is_file():errors.append('Missing inherited asset: '+str(rel));continue
        actual=hashlib.sha256(p.read_text(encoding='utf-8').encode()).hexdigest() if item['hash_policy']=='CANONICAL_LF_UTF8' else hashlib.sha256(p.read_bytes()).hexdigest()
        if actual!=item['v5_expected_sha256']:errors.append('Inherited asset changed after reviewed adaptation: '+str(rel))
    return {'status':'FAIL' if errors else 'PASS','errors':errors,'coverage_files':len(manifest['files']),
            'historical_source':manifest['source_head'],'old_version_worktree_required':False,
            'scope':'Reviewed copy completeness/content; historical preservation audited separately'}

if __name__=='__main__':
    r=audit();print(json.dumps(r,indent=2));raise SystemExit(bool(r['errors']))
