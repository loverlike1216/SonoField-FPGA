"""Fresh sparse clone + fresh venv, v1 absent, full motion GUI/XSim reproduction."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parent


def main():
    p=argparse.ArgumentParser();p.add_argument('--target',default='build/motion_standalone')
    p.add_argument('--output',default='evidence/engineering/motion/standalone')
    a=p.parse_args();target=(REPO/a.target).resolve();out=(REPO/a.output).resolve()
    if REPO not in target.parents or target.exists() or REPO not in out.parents:
        raise SystemExit('Use a new in-workspace target; no existing data will be deleted')
    out.mkdir(parents=True,exist_ok=True);summary={'status':'RUNNING','commands':[]}
    def run(label,command,cwd=REPO):
        r=subprocess.run([str(x) for x in command],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                         text=True,errors='replace',timeout=1800)
        (out/(label+'.log')).write_text(r.stdout,encoding='utf-8')
        summary['commands'].append({'label':label,'command':[str(x) for x in command],'exit_code':r.returncode})
        print(label+': '+str(r.returncode),flush=True)
        if r.returncode:raise RuntimeError(label+' failed: '+r.stdout[-1800:])
        return r.stdout.strip()
    try:
        if run('source_status',['git','status','--porcelain','--untracked-files=no']):raise RuntimeError('Commit tracked source changes first')
        summary['source_commit']=run('source_commit',['git','rev-parse','HEAD'])
        run('clone',['git','clone','--no-hardlinks','--no-checkout',REPO,target])
        run('sparse_init',['git','sparse-checkout','init','--cone'],target)
        run('sparse_scope',['git','sparse-checkout','set','v2','shared','evidence','PCB','AI-chat-memory','AI-interaction-memory','AI-problem'],target)
        run('checkout',['git','checkout','main'],target)
        if (target/'v1').exists():raise AssertionError('Frozen parent must be absent in standalone clone')
        run('venv',[sys.executable,'-m','venv',target/'.venv'])
        python=target/'.venv/Scripts/python.exe';v2=target/'v2'
        run('dependencies',[python,'-m','pip','install','--cache-dir',REPO/'build/pip_cache','-r','requirements-lock.txt'],v2)
        run('dependency_check',[python,'-m','pip','check'],v2)
        run('python_tests',[python,'-m','unittest','discover','-s','tests','-v'],v2)
        run('gui_xsim',[python,'-m','software.ui.app','--automated-demo','--simulator','xsim','--output',v2/'build/motion_standalone'],v2)
        result=json.loads((v2/'build/motion_standalone/gui_result.json').read_text(encoding='utf-8'))
        baseline=json.loads((REPO/'evidence/engineering/motion/validation/summary.json').read_text(encoding='utf-8'))
        fields=('trajectory_sha256','map_words_sha256','trap_reports_sha256','ack_sha256')
        for measured,expected in zip(result['results'],baseline['gui_results']['gui_xsim']['results']):
            for key in fields:
                if measured[key]!=expected[key]:raise AssertionError('Standalone hash mismatch '+key)
        if len(result['results'])!=2 or result['status']!='PASS':raise AssertionError('Incomplete GUI demo')
        summary.update(status='PASS',v1_worktree_present=False,environment='Fresh sparse clone and fresh venv; same Windows host',
                       gui_result=result,scope='90 Python tests, complete 3696-frame GUI/XSim path and exact baseline hashes')
        import shutil
        for name in ('gui_result.json','gui_simulation.png','commands.jsonl','commands.txt','01_motion_ack.txt','01_xsim.log'):
            shutil.copy2(v2/'build/motion_standalone'/name,out/name)
        run('repository_audit',[python,'scripts/check_repository.py'],v2)
    except Exception as exc:
        summary.update(status='FAIL',error=str(exc));raise
    finally:(out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')


if __name__=='__main__':main()
