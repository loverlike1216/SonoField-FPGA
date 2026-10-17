from pathlib import Path
import subprocess,json,sys
R=Path(__file__).resolve().parents[1];V=Path('E:/Codex_project/AMD_Sonofield/v5');B=Path('D:/Vivado/2025.2/2025.2/Vivado/bin');out=R/'results'/('final_digital_'+(sys.argv[1]if len(sys.argv)>1 else'initial'));out.mkdir(exist_ok=False)
jobs=[('scheduler_production','tb_scheduler_production',[V/'rtl/calibration/calibration_scheduler.sv',R/'candidate_rtl/scheduler_golden.sv',R/'candidate_rtl/tb_scheduler_production.sv'],False),('freshness','tb_freshness',[V/'rtl/control/service_freshness.sv',R/'candidate_rtl/tb_freshness.sv'],False),('tx38500','tb_final_tx38500',[V/'rtl/output/tx_pipeline44.sv',V/'rtl/output/serializer_pipeline_44.sv',V/'rtl/control/safety_controller.sv',R/'candidate_rtl/tb_final_tx38500.sv'],False),('tx40000','tb_final_tx40000',[V/'rtl/output/tx_pipeline44.sv',V/'rtl/output/serializer_pipeline_44.sv',V/'rtl/control/safety_controller.sv',R/'candidate_rtl/tb_final_tx40000.sv'],False),('tx41500','tb_final_tx41500',[V/'rtl/output/tx_pipeline44.sv',V/'rtl/output/serializer_pipeline_44.sv',V/'rtl/control/safety_controller.sv',R/'candidate_rtl/tb_final_tx41500.sv'],False),('clocks','tb_final_clocks',[V/'rtl/timing/draw_ready_clocks.v',R/'candidate_rtl/tb_final_clocks.sv'],True)]
rows=[]
for label,top,files,unisim in jobs:
 for sim in (['xsim']if unisim else['icarus','xsim']):
  dest=out/(label+'_'+sim);dest.mkdir();src=files+([B.parent/'data/verilog/src/glbl.v']if unisim else[])
  cmds=([['C:/iverilog/bin/iverilog.exe','-g2012','-s',top,'-o','sim.vvp',*src],['C:/iverilog/bin/vvp.exe','sim.vvp']]if sim=='icarus'else[[B/'xvlog.bat','--sv',*src],[B/'xelab.bat',top,*(['glbl','-L','unisims_ver']if unisim else[]),'-s','sim'],[B/'xsim.bat','sim','--runall']])
  row=dict(case=label,simulator=sim,status='RUNNING',commands=[])
  for i,cmd in enumerate(cmds):
   p=subprocess.run(list(map(str,cmd)),cwd=dest,capture_output=True,text=True,errors='replace',timeout=120);t=p.stdout+p.stderr;(dest/f'{i}.log').write_text(t,encoding='utf-8');row['commands'].append(dict(command=list(map(str,cmd)),returncode=p.returncode))
   if p.returncode or'ERROR:'in t or'FATAL:'in t:row.update(status='FAIL',error=t[-1500:]);break
  else:row['status']='PASS'if'PASS'in t else'FAIL'
  rows.append(row);print(label,sim,row['status'],row.get('error',''),flush=True);(out/'summary.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
assert all(x['status']=='PASS'for x in rows)
