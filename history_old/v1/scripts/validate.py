"""Run actual tools and save per-command evidence. Nonzero/missing gates fail closed."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from check_waveform import check

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from software.acoustic_model.array_geometry import opposing_arrays
from software.acoustic_model.phase_lut_generator import phase_map


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--vivado-bin",default=os.environ.get("VIVADO_BIN",r"D:\Vivado\2025.2\2025.2\Vivado\bin"))
    parser.add_argument("--iverilog-bin",default=os.environ.get("IVERILOG_BIN",r"C:\iverilog\bin"))
    parser.add_argument("--output",default="build/verification_review")
    parser.add_argument("--config",default="config/acoustic_baseline.json")
    parser.add_argument("--skip-xsim",action="store_true",help="Marks XSim NOT_RUN; does not claim full gate")
    args=parser.parse_args()
    evidence=(ROOT/args.output).resolve(); evidence.mkdir(parents=True,exist_ok=True)
    work=ROOT/"build"/"validation"; work.mkdir(parents=True,exist_ok=True)
    results=[]
    def run(label, command, cwd=work):
        started=datetime.datetime.now(datetime.timezone.utc).isoformat()
        proc=subprocess.run([str(x) for x in command],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                            text=True,errors="replace",timeout=300)
        (evidence/f"{label}.log").write_text(proc.stdout,encoding="utf-8")
        results.append({"label":label,"command":[str(x) for x in command],"cwd":str(cwd),
                        "started_utc":started,"exit_code":proc.returncode,"log":f"{label}.log"})
        print(f"{label}: exit {proc.returncode}",flush=True)
        if proc.returncode:
            raise RuntimeError(f"{label} failed: {proc.stdout[-2500:]}")
        return proc.stdout
    summary={"python":sys.version,"platform":sys.platform,"commands":results,"status":"RUNNING"}
    config=json.loads((ROOT/args.config).read_text(encoding="utf-8"))
    map_cases=[(n,config["geometry"]["gap"],"STANDING_WAVE") for n in (2,32,72)]
    map_cases += [(128,g,mode) for g in (config["gap_range_m"][0],config["geometry"]["gap"],config["gap_range_m"][1])
                  for mode in ("STANDING_WAVE","FOCUS")]
    def prepare_map(count,gap,mode):
        geometry={**config["geometry"],"total":count,"gap":gap}
        rows=phase_map(opposing_arrays(**geometry),mode,config["target_m"],config["sound_speed_m_s"])
        (work/"phase_map.hex").write_text("\n".join(f'{(r["enabled"]<<16)|(r["calibration_phase"]<<8)|r["requested_phase"]:05x}' for r in rows)+"\n")
        expected=[]
        for cycle in range(825):
            phase=cycle*10240000//33000000
            word=sum((int(r["enabled"] and ((phase-r["effective_phase"])%256)<128)<<r["rtl_channel"]) for r in rows)
            expected.append(f"{word:032x}")
        (work/"phase_waveform.hex").write_text("\n".join(expected)+"\n")
        return f"{count}_{mode.lower()}_{gap*1000:g}mm"
    try:
        run("python_tests",[sys.executable,"-m","unittest","discover","-s","tests","-v"],ROOT)
        rtl=sorted((ROOT/"rtl").rglob("*.sv"))
        iv=Path(args.iverilog_bin)/"iverilog.exe"; vvp=Path(args.iverilog_bin)/"vvp.exe"
        run("iverilog_version",[iv,"-V"])
        oracles=[]; hashes=[]
        for channels in (1,2,7,32,72,128):
            target=work/f"core_{channels}.vvp"
            run(f"compile_core_{channels}",[iv,"-g2012","-s","tb_core",f"-Ptb_core.CHANNELS={channels}","-o",target,*rtl,ROOT/"tb/tb_core.sv"])
            repeats=3 if channels==128 else 1
            for repeat in range(repeats):
                trace=work/f"core_{channels}_{repeat}.csv"
                output=run(f"run_core_{channels}_{repeat}",[vvp,target,f"+TRACE={trace.as_posix()}"])
                if "PASS TB01" not in output: raise AssertionError("Missing core completion marker")
                report=check(trace,channels); oracles.append(report)
                if channels==128: hashes.append(report["sha256"])
        if len(set(hashes))!=1: raise AssertionError("TB15 non-deterministic Icarus traces")
        for name in ("tb_system","tb_serializer_fault"):
            run(f"compile_{name}",[iv,"-g2012","-s",name,"-o",work/f"{name}.vvp",*rtl,ROOT/f"tb/{name}.sv"])
            out=run(f"run_{name}",[vvp,work/f"{name}.vvp"])
            if "PASS " not in out: raise AssertionError(f"No completion marker: {name}")
        run("compile_model_map",[iv,"-g2012","-s","tb_phase_map","-o",work/"tb_phase_map.vvp",*rtl,ROOT/"tb/tb_phase_map.sv"])
        for count,gap,mode in map_cases:
            label=prepare_map(count,gap,mode)
            out=run(f"model_map_{label}",[vvp,work/"tb_phase_map.vvp"])
            if "PASS model phase map" not in out: raise AssertionError("Model-map integration incomplete")
        run("compile_bandwidth_guard",[iv,"-g2012","-s","tb_bad_bandwidth","-o",work/"bad_bandwidth.vvp",*rtl,ROOT/"tb/tb_bad_bandwidth.sv"])
        bad=subprocess.run([str(vvp),str(work/"bad_bandwidth.vvp")],cwd=work,capture_output=True,text=True,timeout=30)
        (evidence/"bandwidth_guard.log").write_text(bad.stdout+bad.stderr)
        if bad.returncode==0 or "Serializer bandwidth insufficient" not in bad.stdout:
            raise AssertionError("Unsafe bandwidth profile was not rejected")
        summary["bandwidth_guard"]={"status":"PASS", "expected_nonzero_exit":bad.returncode,
                                     "command":[str(vvp),str(work/"bad_bandwidth.vvp")]}
        summary["python_oracles"]=oracles
        summary["TB15"]={"status":"PASS","repetitions":3,"hashes":hashes}
        if not args.skip_xsim:
            vb=Path(args.vivado_bin)
            # XSim is part-independent; an FPGA package is not selected for behavioral simulation.
            out=run("xvlog",[vb/"xvlog.bat","--sv",*rtl,ROOT/"tb/tb_core.sv",ROOT/"tb/tb_system.sv",ROOT/"tb/tb_serializer_fault.sv",ROOT/"tb/tb_phase_map.sv"])
            for name in ("tb_core","tb_system","tb_serializer_fault","tb_phase_map"):
                run(f"xelab_{name}",[vb/"xelab.bat",name,"--snapshot",name+"_snapshot","--debug","typical"])
                if name=="tb_phase_map":
                    for count,gap,mode in map_cases:
                        if count!=128:continue
                        label=prepare_map(count,gap,mode)
                        out=run(f"xsim_model_map_{label}",[vb/"xsim.bat",name+"_snapshot","--runall"])
                        if "PASS model phase map" not in out or "Fatal:" in out:
                            raise AssertionError("XSim model-map case failed: "+label)
                    continue
                for repeat in range(3 if name=="tb_core" else 1):
                    trace=work/f"xsim_{repeat}.csv"
                    command=[vb/"xsim.bat",name+"_snapshot","--runall"]
                    out=run(f"xsim_{name}_{repeat}",command)
                    if "PASS " not in out or "Fatal:" in out: raise AssertionError(f"XSim missing pass: {name}")
                    if name=="tb_core":
                        # Windows .bat argument forwarding tokenizes an unquoted '=' in plusargs.
                        # Use the TB default filename and preserve each completed trace independently.
                        shutil.copy2(work/"trace.csv",trace)
                        report=check(trace,128)
                        if report["sha256"]!=hashes[0]: raise AssertionError("Independent simulator trace mismatch")
            summary["independent_simulator"]="Vivado 2025.2 XSim; 3 traces byte-identical to Icarus"
        else:
            summary["independent_simulator"]="NOT_RUN"
        summary["source_sha256"]={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                                    for p in [*rtl,*sorted((ROOT/"tb").glob("*.sv"))]}
        summary["model_map_cases"]=[{"channels":n,"face_gap_mm":g*1000,"mode":m} for n,g,m in map_cases]
        summary["geometry_configuration"]=config
        summary["source_text_sha256"]={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
            for p in [*sorted((ROOT/"software").rglob("*.py")),*sorted((ROOT/"tests").rglob("*.py")),
                      *sorted((ROOT/"scripts").glob("*.py")),ROOT/args.config]}
        summary["status"]="PASS" if not args.skip_xsim else "PARTIAL"
    except Exception as exc:
        summary["status"]="FAIL"; summary["error"]=str(exc)
        raise
    finally:
        (evidence/"summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps({"status":summary["status"],"evidence":str(evidence)},indent=2))


if __name__=="__main__": main()
