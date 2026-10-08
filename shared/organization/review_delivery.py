"""Review staged public delivery bytes in one Git batch, preserving raw evidence locally."""
from pathlib import Path
import re,json,subprocess,hashlib,sys,shutil
from archive_after_baseline import write,dump
R=Path(__file__).resolve().parents[2];V=R/'v5'

def sanitize_evidence_paths():
    records=[]
    pattern=r'(?i)[A-Z]:[\\/]Users[\\/][^\\/\s\"\']+'
    for p in (V/'evidence').rglob('*'):
        if p.suffix not in ('.log','.txt','.rpt','.md','.json') or 'local_raw' in p.parts:continue
        text=p.read_text(encoding='utf-8',errors='replace')
        sanitized=re.sub(pattern,'[USER_HOME]',text)
        if text!=sanitized:
            rel=p.relative_to(V/'evidence');raw=V/'evidence/local_raw/public_path_redaction'/rel
            assert not raw.exists(),'Do not overwrite raw original evidence'
            raw.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,raw)
            write(p,sanitized)
            records.append({'public_file':p.relative_to(R).as_posix(),'original_sha256_bytes':hashlib.sha256(raw.read_bytes()).hexdigest(),
                'public_canonical_sha256':hashlib.sha256(sanitized.encode()).hexdigest(),'policy':'Redact personal user-home prefix; tool outcome unchanged; exact original kept locally'})
    if records:dump(R/'shared/organization/EVIDENCE_PATH_REDACTION.json',{'status':'PASS','records':records})
    return records

def staged_review():
    paths=[x for x in subprocess.check_output(['git','diff','--cached','--name-only','-z'],cwd=R).decode('utf-8').split('\0') if x]
    # Git's :path is an index object spec; batch avoids one subprocess per artifact.
    blob=subprocess.run(['git','cat-file','--batch'],input=''.join(':'+p+'\n' for p in paths).encode(),cwd=R,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout
    pos=0;issues=[];total=0;largest=0
    for path in paths:
        end=blob.index(b'\n',pos);header=blob[pos:end].split();assert len(header)==3 and header[1]==b'blob',path
        size=int(header[2]);data=blob[end+1:end+1+size];pos=end+size+2;assert len(data)==size
        total+=size;largest=max(largest,size)
        if '/local_raw/' in path or '/build/' in path or path.startswith(('v1/','v2/','v3/','PCB/','BOM/','Zynq7020/','parameter_detection/','evidence/')):
            issues.append('Staged outside authorized current scope:'+path)
        if size>5*1024*1024:issues.append('Large artifact:'+path)
        if re.search(rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{25,})\b',data):issues.append('Credential pattern:'+path)
        # Require actual PEM body/newlines, not a scanner's quoted pattern literal.
        if re.search(rb'-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----\r?\n[A-Za-z0-9+/=\r\n]{40,}-----END (?:[A-Z]+ )*PRIVATE KEY-----',data):
            issues.append('Private key:'+path)
    original_delta=subprocess.check_output(['git','diff','--name-only','851d1ef747cd95da13e5eb0705b5a7885b68d83c','--',
        'v1','v2','PCB','BOM','Zynq7020','parameter_detection','evidence'],cwd=R).decode('utf-8').strip()
    if original_delta:issues.append('Historical tracked delta:'+original_delta)
    # Verify archived snapshots' staged payloads preserve original bytes, including CRLF.
    m=json.loads((R/'archive/manifests/MIGRATION_MANIFEST.json').read_text(encoding='utf-8'))
    for item in m['operations']:
        if item['operation']!='COPY_SNAPSHOT':continue
        p=R/item['target_path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256_bytes']
    result={'status':'FAIL' if issues else 'PASS','staged_files':len(paths),'total_bytes':total,'largest_file_bytes':largest,
        'credential_patterns':'PASS' if not any('Credential' in x or 'Private key' in x for x in issues) else 'FAIL',
        'historical_tracked_delta':original_delta or 'NONE','issues':issues,
        'scope':'Review staged public bytes/scope/sizes, plus exact original byte inventory and redacted visible transcripts; no claim of inaccessible chat completeness'}
    dump(R/'shared/organization/PUBLIC_DELIVERY_REVIEW.json',result)
    if issues:raise RuntimeError(repr(issues))
    return result

if __name__=='__main__':
    if '--sanitize-evidence-paths' in sys.argv:print(json.dumps({'redacted':len(sanitize_evidence_paths())}))
    else:print(json.dumps(staged_review(),indent=2))
