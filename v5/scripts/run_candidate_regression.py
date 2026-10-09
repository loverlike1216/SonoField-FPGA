"""Run candidate checks and both ADC simulators in fresh evidence, no board I/O."""
from pathlib import Path
import argparse,json,os,re,subprocess,sys,time
R=Path(__file__).resolve().parents[2];V=R/'v5'
parser=argparse.ArgumentParser();parser.add_argument('--label',required=True);args=parser.parse_args()
if not re.fullmatch(r'[A-Za-z0-9_-]+',args.label):raise ValueError('Label must be a simple run name')
out=V/'evidence/migration/20261009'/args.label/'candidates';out.mkdir(parents=True,exist_ok=True)
assert not (out/'extra_summary.json').exists()
os.environ.update(PYTHONUTF8='1',PYTHONIOENCODING='utf-8')
candidate=V/'hardware/integration_candidates/20261009';commands=[]
def run(name,argv):
 started=time.monotonic()
 p=subprocess.run([str(x) for x in argv],cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8',errors='replace',timeout=300)
 (out/(name+'.log')).write_text(p.stdout,encoding='utf-8')
 commands.append({'name':name,'argv':[str(x) for x in argv],'exit_code':p.returncode,'elapsed_s':time.monotonic()-started})
 if p.returncode or 'FATAL:' in p.stdout:raise RuntimeError(name)
 return p.stdout
try:
 run('offline15',[sys.executable,candidate/'verify_candidates.py','--output',out])
 files=[V/'rtl/acquisition/adc_serial.sv',candidate/'ad7606c_candidate_rom.sv',candidate/'tb_adc_candidate.sv']
 iv=Path(os.environ['IVERILOG_BIN']);vb=Path(os.environ['VIVADO_BIN'])
 run('adc_iverilog',[iv/'iverilog.exe','-g2012','-s','tb_adc_candidate','-o',out/'adc_candidate.vvp',*files])
 assert 'ADC_CANDIDATE_SERIAL_PASS frames=256' in run('adc_icarus',[iv/'vvp.exe',out/'adc_candidate.vvp'])
 run('adc_xvlog',[vb/'xvlog.bat','--sv',*files])
 run('adc_xelab',[vb/'xelab.bat','tb_adc_candidate','--snapshot','adc_candidate','--debug','typical'])
 assert 'ADC_CANDIDATE_SERIAL_PASS frames=256' in run('adc_xsim',[vb/'xsim.bat','adc_candidate','--runall'])
 status='PASS'
finally:
 (out/'extra_summary.json').write_text(json.dumps({'status':locals().get('status','FAIL'),'classification':'OFFLINE_DIGITAL_CANDIDATE_ONLY','hardware_verified':False,'commands':commands},indent=2)+'\n',encoding='utf-8')
print('EXTRA_GATES_PASS',args.label)
