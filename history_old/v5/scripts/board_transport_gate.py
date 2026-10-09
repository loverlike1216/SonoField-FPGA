"""Run real host-C/Python tests and both independent RTL simulators, no board I/O."""
import json
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidence/board_transport';WORK=ROOT/'build/board_transport/sim'

def main():
    global OUT
    parser=argparse.ArgumentParser();parser.add_argument("--output",default="evidence/board_transport")
    OUT=(ROOT/parser.parse_args().output).resolve();OUT.mkdir(parents=True,exist_ok=True)
    WORK.mkdir(parents=True,exist_ok=True);results=[]
    def run(name,argv,cwd=WORK):
        p=subprocess.run(list(map(str,argv)),cwd=cwd,capture_output=True,text=True,errors='replace',timeout=900)
        (OUT/(name+'.log')).write_text(p.stdout+p.stderr,encoding='utf-8')
        results.append(dict(name=name,command=list(map(str,argv)),exit_code=p.returncode))
        if p.returncode or 'FATAL:' in p.stdout or 'Fatal:' in p.stdout:raise RuntimeError(name+' failed '+p.stdout[-1000:]+p.stderr[-1000:])
        print(name+' PASS',flush=True);return p.stdout
    try:
        run('generated_transport',[sys.executable,ROOT/'scripts/generate_transport.py','--check'])
        run('python_tests',[sys.executable,'-m','unittest','discover','-s','tests','-v'],ROOT)
        shutil.copyfile(ROOT/'build/board_transport/c_compile.log',OUT/'ps_service_compile.log')
        rtl=sorted((ROOT/'rtl').rglob('*.sv'))
        tbs=[ROOT/'tb/tb_axi_native_bridge.sv',ROOT/'tb/tb_axi_system.sv',ROOT/'tb/tb_board_smoke_pl.sv']
        iv=Path(os.environ.get('IVERILOG_BIN','C:/iverilog/bin'));vb=Path(os.environ.get('VIVADO_BIN','D:/Vivado/2025.2/2025.2/Vivado/bin'))
        for name in ('tb_axi_native_bridge','tb_axi_system','tb_board_smoke_pl'):
            run(name+'_compile',[iv/'iverilog.exe','-g2012','-I',ROOT/'rtl/generated','-s',name,'-o',WORK/(name+'.vvp'),*rtl,*tbs])
            text=run('icarus_'+name,[iv/'vvp.exe',WORK/(name+'.vvp')]);assert ('PASS AXI_' in text or 'PASS BOARD_SMOKE_PL' in text)
        run('xvlog',[vb/'xvlog.bat','--sv','-i',ROOT/'rtl/generated',*rtl,*tbs])
        for name in ('tb_axi_native_bridge','tb_axi_system','tb_board_smoke_pl'):
            run('xelab_'+name,[vb/'xelab.bat',name,'--snapshot',name,'--debug','typical'])
            text=run('xsim_'+name,[vb/'xsim.bat',name,'--runall']);assert ('PASS AXI_' in text or 'PASS BOARD_SMOKE_PL' in text)
        (OUT/'icarus.log').write_text('\n'.join((OUT/('icarus_'+n+'.log')).read_text() for n in ('tb_axi_native_bridge','tb_axi_system')))
        (OUT/'xsim.log').write_text('\n'.join((OUT/('xsim_'+n+'.log')).read_text() for n in ('tb_axi_native_bridge','tb_axi_system')))
        status='PASS'
    except Exception:
        status='FAIL';raise
    finally:
        (OUT/'axi_bridge_tests.json').write_text(json.dumps(dict(status=status,commands=results,
            classification='OFFLINE_SIMULATION',hardware_programmed=False),indent=2)+'\n')
        (OUT/'protocol_tests.json').write_text(json.dumps(dict(status='PASS' if any(r['name']=='python_tests' and r['exit_code']==0 for r in results) else 'FAIL',
            cross_validation='Python client and actual GCC-compiled C service; MMIO fixture only',real_uart_tested=False),indent=2)+'\n')

if __name__=='__main__':main()
