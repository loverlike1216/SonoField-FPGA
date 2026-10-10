"""Real native C execution + real ARM object compilation, never board evidence."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from software.prepcb.c_session import Session,build
import numpy as np

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists():raise ValueError('Fresh output required')
 out.mkdir(parents=True);scratch=ROOT/'build/nextstage_software'/out.name;scratch.mkdir(parents=True,exist_ok=True);commands=[]
 def run(name,cmd,env=None):
  r=subprocess.run(list(map(str,cmd)),capture_output=True,text=True,timeout=120,cwd=ROOT,env=env);t=r.stdout+r.stderr;(out/(name+'.log')).write_text(t,encoding='utf-8');commands.append(dict(name=name,command=list(map(str,cmd)),exit_code=r.returncode))
  if r.returncode or 'error:' in t:raise RuntimeError(name+' failed '+t[-1000:])
  return t
 try:
  files=[ROOT/'firmware/ps_service/adc7606c16.c',ROOT/'tests/nextstage_driver_fixture.c']
  run('host_compile',[os.environ['CC'],'-std=c11','-O2','-Wall','-Wextra','-Werror','-I',ROOT/'firmware/ps_service',*files,'-o',scratch/'driver.exe'])
  text=run('host_execute',[scratch/'driver.exe']);assert 'PASS HOST_FIXTURE' in text
  lib=build(scratch/'service');s=Session(lib);lat=[]
  for i in range(1000):
   data=i.to_bytes(4,'little')+b'outputs_disabled';start=time.perf_counter_ns();assert s.request(1,data)==data;lat.append((time.perf_counter_ns()-start)/1000)
  (out/'ping_latency_us.json').write_text(json.dumps(lat)+'\n');(out/'protocol_trace.json').write_text(json.dumps(s.trace,indent=2)+'\n')
  vb=Path(os.environ['VIVADO_BIN']);install=vb.parents[1];clang=install/'win64/tools/clang-16/bin/clang.exe';readelf=clang.with_name('llvm-readelf.exe')
  env=os.environ.copy();env['PATH']=str(install/'Vivado/lib/win64.o')+';'+str(install/'Vitis/lib/win64.o')+';'+env['PATH']
  run('arm_compiler_version',[clang,'--version'],env)
  obj=scratch/'adc7606c16_arm.o';run('arm_compile',[clang,'-target','armv7a-none-eabi','-mcpu=cortex-a9','-mfloat-abi=soft','-ffreestanding','-Wall','-Wextra','-Werror','-O2','-c',files[0],'-o',obj],env)
  elf=run('arm_readelf',[readelf,'-h','-s',obj],env);assert 'ARM' in elf and 'sf_c16_configure' in elf
  result=dict(status='PASS',classification='HOST_FIXTURE_AND_ARM_OBJECT_ONLY',register_masks=256,ping=dict(count=1000,success=1000,classification='IN_PROCESS_COMPILED_C_NOT_UART_PS_AXI',min_us=min(lat),p50_us=float(np.percentile(lat,50)),p95_us=float(np.percentile(lat,95)),p99_us=float(np.percentile(lat,99)),max_us=max(lat)),arm_object_sha256=hashlib.sha256(obj.read_bytes()).hexdigest(),target_application='BLOCKED_NO_QUALIFIED_XSA_BSP',commands=commands)
 except Exception as exc:result=dict(status='FAIL',error=str(exc),commands=commands);raise
 finally:(out/'summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
