"""Fresh local Git clone + isolated venv + complete tests, all within the specified workspace."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent


def main():
    p=argparse.ArgumentParser();p.add_argument("--target",default="build/repro_v1")
    p.add_argument("--output",default="build/reproduction_review")
    a=p.parse_args();target=(REPO/a.target).resolve()
    if REPO not in target.parents or target.exists():
        raise SystemExit("Reproduction target must be new and inside this workspace; nothing will be deleted")
    evidence=(ROOT/a.output).resolve()
    if ROOT not in evidence.parents or evidence.exists():
        raise SystemExit("Evidence path must be new and inside workspace to preserve historical results")
    evidence.mkdir(parents=True,exist_ok=True)
    records=[];summary={"status":"RUNNING","target":str(target),"commands":records}
    def run(name,cmd,cwd=REPO):
        result=subprocess.run([str(v) for v in cmd],cwd=cwd,capture_output=True,text=True,errors="replace",timeout=900)
        (evidence/f"{name}.log").write_text(result.stdout+result.stderr,encoding="utf-8")
        records.append({"command":[str(v) for v in cmd],"cwd":str(cwd),"exit_code":result.returncode,"log":name+".log"})
        print(f"{name}: exit {result.returncode}",flush=True)
        if result.returncode: raise RuntimeError(name+" failed: "+(result.stdout+result.stderr)[-1800:])
        return result.stdout
    try:
        summary["started_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
        dirty=run("source_status",["git","status","--porcelain","--untracked-files=no"]).strip()
        if dirty:
            raise RuntimeError("Commit the source checkpoint before attempting fresh-clone reproduction")
        summary["source_commit"]=run("source_commit",["git","rev-parse","HEAD"]).strip()
        run("clone",["git","clone","--no-hardlinks",REPO,target])
        run("venv",[sys.executable,"-m","venv",target/".venv"])
        python=target/".venv/Scripts/python.exe"
        version_target=target/"v1"
        run("install",[python,"-m","pip","install","--cache-dir",REPO/"build/pip_cache","-r","requirements-lock.txt"],version_target)
        run("dependency_check",[python,"-m","pip","check"],version_target)
        run("full_validation",[python,"scripts/validate.py","--output","build/reproduced_evidence"],version_target)
        run("model",[python,"-m","software.acoustic_model.visualize_field","--output","build/reproduced_model"],version_target)
        matching=[]
        state=json.loads((REPO/"shared/PROJECT_STATE.json").read_text(encoding="utf-8"))
        for path in sorted((REPO/state["model_evidence"]).glob("*.csv")):
            # CSV content identity is independent of Git/Windows newline conversion.
            original=hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
            repeated=hashlib.sha256((version_target/"build/reproduced_model"/path.name).read_text(encoding="utf-8").encode("utf-8")).hexdigest()
            if original!=repeated:raise AssertionError("Model reproduction mismatch: "+path.name)
            matching.append({"file":path.name,"canonical_lf_sha256":original})
        digital=json.loads((version_target/"build/reproduced_evidence/summary.json").read_text())
        if digital["status"]!="PASS":raise AssertionError("Reproduction digital gate incomplete")
        run("repository_audit",[python,"scripts/check_repository.py"],version_target)
        run("coordinates",[python,"-m","software.acoustic_model.export_geometry","--output","build/reproduced_coordinates"],version_target)
        for path in sorted((ROOT/"hardware/mechanical/geometry_10mm").glob("*.csv")):
            repeated=version_target/"build/reproduced_coordinates"/path.name
            if path.read_text(encoding="utf-8")!=repeated.read_text(encoding="utf-8"):
                raise AssertionError("Coordinate/phase export mismatch: "+path.name)
        summary["coordinate_phase_csv_count"]=len(list((ROOT/"hardware/mechanical/geometry_10mm").glob("*.csv")))
        summary.update(status="PASS",model_csv_hashes=matching,digital_trace_sha256=digital["TB15"]["hashes"][0],
                       note="Fresh local clone/new venv on same Windows host; not an independent physical board or OS")
    except Exception as exc:
        summary.update(status="FAIL",error=str(exc));raise
    finally:
        (evidence/"summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")


if __name__=="__main__":main()
