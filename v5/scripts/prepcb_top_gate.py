from pathlib import Path
import argparse,os,subprocess,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--maps',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 out=a.output.resolve();out.mkdir(parents=True,exist_ok=True)
 data=a.maps.read_bytes();iv=Path(os.environ['IVERILOG_BIN']);vb=Path(os.environ['VIVADO_BIN']);records=[]
 files=[*[ROOT/x.strip() for x in (ROOT/'config/ooc_source_list.txt').read_text().splitlines() if x.strip()],ROOT/'rtl/control/prepcb_supervisor.sv',ROOT/'rtl/motion/prepcb_frame_mailbox.sv',ROOT/'rtl/board/prepcb_pl.v',ROOT/'tb/ad7606b_model.sv',ROOT/'tb/tb_prepcb_system.sv']
 for simulator in ('icarus','xsim'):
  dest=out/simulator;dest.mkdir(exist_ok=True);(dest/'motion_maps.hex').write_bytes(data)
  (dest/'adc_vectors.hex').write_text(('0'*32+'\n')*1024)
  commands=([('compile',[iv/'iverilog.exe','-g2012','-I',ROOT/'rtl/generated','-s','tb_prepcb_system','-o','system.vvp',*files]),('run',[iv/'vvp.exe','system.vvp'])] if simulator=='icarus' else
   [('xvlog',[vb/'xvlog.bat','--sv','-i',ROOT/'rtl/generated',*files]),('xelab',[vb/'xelab.bat','tb_prepcb_system','-s','system']),('xsim',[vb/'xsim.bat','system','--runall'])])
  for label,cmd in commands:
   r=subprocess.run(list(map(str,cmd)),cwd=dest,capture_output=True,text=True,timeout=120)
   (dest/(label+'.log')).write_text(r.stdout+r.stderr,encoding='utf-8')
   if r.returncode or 'ERROR:' in r.stdout or 'FATAL:' in r.stdout or (label in ('run','xsim') and 'PASS PREPCB SYSTEM' not in r.stdout):raise RuntimeError(simulator+':'+label+' failed; '+r.stdout[-1500:]+r.stderr[-1500:])
  lines=(dest/'integrated_ack.txt').read_text().splitlines();records.append(dict(simulator=simulator,frames=len(lines),ack_sha256=hashlib.sha256('\n'.join(lines).encode()).hexdigest()))
 assert records[0]['ack_sha256']==records[1]['ack_sha256']
 (out/'summary.json').write_text(json.dumps(dict(status='PASS',classification='SIMULATED_ACTUAL_NEW_TOP_NOT_BOARD',maps_sha256=hashlib.sha256(data).hexdigest(),runs=records),indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
