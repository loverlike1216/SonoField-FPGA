from pathlib import Path
import subprocess,json,hashlib,sys
R=Path(__file__).resolve().parents[1];V=Path('E:/Codex_project/AMD_Sonofield/v5');B=Path('D:/Vivado/2025.2/2025.2/Vivado/bin')
out=R/'results'/('production_profile_'+(sys.argv[1]if len(sys.argv)>1 else'initial'));out.mkdir(exist_ok=False)
maps=V/'evidence/hardware_design_20261011/digital_full_retry2/full/system/gui/case_1/icarus/motion_maps.hex'
files=[V/x for x in(V/'config/nextstage_source_list.txt').read_text().splitlines()]+[V/'rtl/board/draw_ready_pl.v',R/'candidate_rtl/ad7606c16_model.sv',R/'candidate_rtl/tb_draw_ready_system.sv']
records=[]
for sim in ['icarus','xsim']:
 dest=out/sim;dest.mkdir();(dest/'motion_maps.hex').write_bytes(maps.read_bytes())
 commands=([['C:/iverilog/bin/iverilog.exe','-g2012','-I',V/'rtl/generated','-s','tb_draw_ready_system','-o','prod.vvp',*files],['C:/iverilog/bin/vvp.exe','prod.vvp']]if sim=='icarus'else[[B/'xvlog.bat','--sv','-i',V/'rtl/generated',*files],[B/'xelab.bat','tb_draw_ready_system','-s','production'],[B/'xsim.bat','production','--runall']])
 row=dict(simulator=sim,status='RUNNING',commands=[])
 for i,cmd in enumerate(commands):
  p=subprocess.run(list(map(str,cmd)),cwd=dest,capture_output=True,text=True,errors='replace',timeout=300);t=p.stdout+p.stderr;(dest/f'{i}.log').write_text(t,encoding='utf-8');row['commands'].append(dict(argv=list(map(str,cmd)),returncode=p.returncode))
  if p.returncode or'ERROR:'in t or'FATAL:'in t:row.update(status='FAIL',error=t[-1800:]);break
 else:
  row['status']='PASS'if'PASS PREPCB SYSTEM'in t else'FAIL'
  if row['status']=='PASS':
   data=(dest/'integrated_ack.txt').read_bytes();row['frames']=len(data.splitlines());row['ack_sha256']=hashlib.sha256(data.replace(b'\r\n',b'\n')).hexdigest()
 records.append(row);(out/'summary.json').write_text(json.dumps(records,indent=2),encoding='utf-8');print(sim,row['status'],row.get('error',''),flush=True)
assert all(x['status']=='PASS'for x in records)
assert records[0]['ack_sha256']==records[1]['ack_sha256']
