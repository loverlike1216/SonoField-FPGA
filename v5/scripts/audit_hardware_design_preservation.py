"""Audit this stage's original active files; never load frozen source bodies."""
from pathlib import Path
import argparse,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2]
ALLOWED={'.gitattributes','.gitignore','README.md','AGENTS.md','CHANGELOG.md',
         'AI-interaction-memory/INDEX.md','AI-chat-memory/INDEX.md',
         'v5/config/SIGNAL_CONTRACT.json','v5/config/board_facts.json',
         'v5/scripts/check_nextstage_preservation.py','v5/scripts/check_prepcb_preservation.py'}
ALLOWED.update('shared/'+name for name in ('PROJECT_STATE.md','PROJECT_STATE.json','VERSION_STATE.json',
    'CURRENT_PLAN.md','DECISIONS.md','ACCEPTANCE.md','BLOCKERS.md','CONTEXT_CHECKPOINT.md',
    'CONTEXT_CHECKPOINT.json','HANDOFF.md'))


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    output=a.output.resolve()
    if not output.is_relative_to(ROOT/'v5') or output.exists():raise ValueError('Fresh v5 output required')
    before=json.loads((ROOT/'v5/evidence/hardware_design_20261011/BEFORE_CHANGE_HASHES.json').read_text())
    errors=[];changes=[];protected=0
    for rel,wanted in before.items():
        if rel.split('/')[0] in {'Historical project','history_old'}:raise ValueError('Forbidden archive body')
        path=ROOT/rel
        if not path.is_file():errors.append('Missing '+rel);continue
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        immutable=rel.startswith(('v5/rtl/','v5/firmware/','v5/tests/','v5/tb/','v5/simulation/','v5/evidence/','v5/hardware/bom/'))
        protected+=immutable
        if actual!=wanted:
            changes.append(dict(path=rel,before=wanted,after=actual,allowed=rel in ALLOWED))
            if immutable or rel not in ALLOWED:errors.append('Protected/unreviewed change '+rel)
    base='618b6f1ffe3dae9b98c59bf1c981349e48644662'
    def tree(ref):return subprocess.check_output(['git','ls-tree','-rz',ref,'--','Historical project'],cwd=ROOT)
    frozen=tree(base)
    if frozen!=tree('HEAD'):errors.append('Frozen Git metadata changed')
    result=dict(status='FAIL' if errors else 'PASS',original_files=len(before),immutable_files=protected,
                changes=changes,errors=errors,frozen_metadata_files=len(frozen.split(b'\0'))-1,
                frozen_body_read=False,old_workspace_accessed=False)
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));return bool(errors)


if __name__=='__main__':raise SystemExit(main())
