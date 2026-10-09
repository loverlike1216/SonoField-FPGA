"""Real v5 baseline; no hardware access, inherited tests are never skipped."""
from pathlib import Path
import argparse,subprocess,sys,json,os,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    out=(ROOT/args.output).resolve();out.mkdir(parents=True,exist_ok=True)
    if (out/'summary.json').exists():raise RuntimeError('Use a fresh evidence directory; never overwrite an earlier result')
    env=os.environ.copy();env['PYTHONUTF8']='1';env['PYTHONIOENCODING']='utf-8'
    records=[];summary={'status':'RUNNING','active_version':'v5','platform':'ALINX AX7020','commands':records,
        'classification':'DIGITAL_BASELINE_NOT_BOARD_VERIFICATION','hardware_programmed':False,
        'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    def run(label,script,*argv):
        cmd=[sys.executable,str(ROOT/'scripts'/script),*map(str,argv)]
        with (out/(label+'.log')).open('w',encoding='utf-8') as log:
            proc=subprocess.run(cmd,cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=2400)
        records.append({'label':label,'command':cmd,'exit_code':proc.returncode})
        print(label,proc.returncode,flush=True)
        if proc.returncode:raise RuntimeError(label+' failed; inspect '+str(out/(label+'.log')))
    try:
        run('structure','check_structure.py')
        run('inheritance','check_migration.py')
        run('generated_system','generate_system.py','--check')
        run('generated_transport','generate_transport.py','--check')
        run('motion_full','motion_gate.py','--output',out/'motion')
        run('axi_offline','board_transport_gate.py','--output',out/'axi')
        run('independent_safety','pre_pcb_checks.py','--output',out/'independent')
        run('timing_equivalence','timing_equivalence.py')
        motion=json.loads((out/'motion/summary.json').read_text(encoding='utf-8'))
        assert motion['status']=='PASS' and motion['frame_count']==3696
        assert motion['determinism']['status']=='PASS' and motion['determinism']['runs']==4
        text=(out/'motion/python_tests.log').read_text(encoding='utf-8')
        import re
        tests=int(re.search(r'Ran (\d+) tests',text).group(1));assert tests==115,tests
        summary.update(status='PASS',python_tests=tests,frame_count=motion['frame_count'],determinism=motion['determinism'],
            regression='PASS',axi_offline='PASS',independent_safety='PASS',timing_equivalence='PASS',
            source_sha256={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_text(encoding='utf-8').encode()).hexdigest()
              for folder in ['rtl','tb','tests','software','scripts','config','simulation'] for p in (ROOT/folder).rglob('*')
              if p.suffix in ('.py','.sv','.svh','.json','.tcl','.ps1','.c','.h')})
    except Exception as exc:summary.update(status='FAIL',error=str(exc));raise
    finally:(out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('V5_BASELINE_PASS',flush=True)

if __name__=='__main__':main()
