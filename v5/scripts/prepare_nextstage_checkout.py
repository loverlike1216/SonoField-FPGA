"""Recreate S0 raw LF/CRLF bytes from this clone's own unchanged Git blobs."""
from pathlib import Path
import hashlib,json,subprocess

ROOT=Path(__file__).resolve().parents[2]

def main():
    def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
    if subprocess.run(['git','diff','--quiet'],cwd=ROOT).returncode:
        raise RuntimeError('Preserve/review tracked working changes before byte materialization')
    snapshot=json.loads((ROOT/'v5/evidence/next_stage/20261010/S0_PROTECTED_HASHES.json').read_text(encoding='utf-8'))
    subprocess.run(['git','config','core.autocrlf','false'],cwd=ROOT,check=True)
    changed=[]
    for rel,old in snapshot.items():
        if rel.startswith(('Historical project/','history_old/')):raise RuntimeError('Historical body forbidden')
        path=ROOT/rel
        if not path.is_file():raise RuntimeError('Missing '+rel)
        raw=path.read_bytes()
        if hashlib.sha256(raw).hexdigest()==old['raw_sha256']:continue
        current_blob=git('rev-parse','HEAD:'+rel).decode().strip()
        if current_blob!=old['git_blob']:continue # authorized adaptations are audited separately
        blob=git('show','HEAD:'+rel)
        lf=blob.replace(b'\r\n',b'\n')
        expected=next((x for x in (blob,lf,lf.replace(b'\n',b'\r\n')) if hashlib.sha256(x).hexdigest()==old['raw_sha256']),None)
        if expected is None or raw.replace(b'\r\n',b'\n')!=lf:
            raise RuntimeError('Non-EOL difference; no rewrite allowed: '+rel)
        path.write_bytes(expected)
        changed.append(dict(path=rel,before=hashlib.sha256(raw).hexdigest(),after=old['raw_sha256'],git_blob=current_blob))
    print(json.dumps(dict(status='PASS',source='THIS_CLONE_OWN_GIT_OBJECTS',historical_body_read=False,
        root_or_original_sandbox_source_copied=False,files=changed),indent=2))

if __name__=='__main__':main()
