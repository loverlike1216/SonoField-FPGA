"""Real Icarus + XSim adapter test; never accesses hardware."""
from pathlib import Path
import argparse,os,json,subprocess,hashlib
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists():raise ValueError('Use a fresh evidence directory')
 out.mkdir(parents=True);records=[]
 sources=[ROOT/'rtl/acquisition/adc_serial.sv',ROOT/'rtl/acquisition/ad7606c16_if.sv',ROOT/'tb/ad7606c16_model.sv',ROOT/'tb/tb_ad7606c16.sv']
 try:
  for sim in ('icarus','xsim'):
   dest=out/sim;dest.mkdir();iv=Path(os.environ['IVERILOG_BIN']);vb=Path(os.environ['VIVADO_BIN'])
   cmds=([('compile',[iv/'iverilog.exe','-g2012','-s','tb_ad7606c16','-o','adc.vvp',*sources]),('run',[iv/'vvp.exe','adc.vvp'])] if sim=='icarus' else [('xvlog',[vb/'xvlog.bat','--sv',*sources]),('xelab',[vb/'xelab.bat','tb_ad7606c16','-s','adc_c16']),('run',[vb/'xsim.bat','adc_c16','--runall'])])
   for label,cmd in cmds:
    r=subprocess.run(list(map(str,cmd)),cwd=dest,capture_output=True,text=True,timeout=180)
    text=r.stdout+r.stderr;(dest/(label+'.log')).write_text(text,encoding='utf-8');records.append(dict(simulator=sim,step=label,exit_code=r.returncode))
    if r.returncode or 'ERROR:' in text or 'FATAL:' in text or (label=='run' and 'PASS C16' not in text):raise RuntimeError(sim+'/'+label+': '+text[-1200:])
  hashes={sim:hashlib.sha256((out/sim/'c16_trace.txt').read_bytes().replace(b'\r\n',b'\n')).hexdigest() for sim in ('icarus','xsim')}
  if len(set(hashes.values()))!=1:raise AssertionError('ADC trace differs')
  result=dict(status='PASS',classification='DIGITAL_ADAPTER_SIMULATED_ANALOG_UNVERIFIED',signed_frames=64,continuous_800ksps_frames=32,negative_readback_cases=5,hashes=hashes,commands=records,crc='DISABLED_AND_READBACK_CHECKED; unexpected-enable rejected; CRC-enabled frames unsupported')
 except Exception as e:
  result=dict(status='FAIL',error=str(e),commands=records);raise
 finally:(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
