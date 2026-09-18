"""Read-only deliverable consistency and hygiene audit; no fabricated acceptance."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]


def main():
    errors=[]
    required=["README.md","AGENTS.md","shared/CURRENT_PLAN.md","shared/PROJECT_STATE.json",
              "shared/DECISIONS.md","shared/ACCEPTANCE.md","shared/BLOCKERS.md","shared/HANDOFF.md",
              "shared/CHANGELOG.md","shared/VN1_REPORT.md","docs/OPERATING_GUIDE.md"]
    for name in required:
        if not (ROOT/name).is_file(): errors.append("Missing "+name)
    for p in ROOT.glob("*"):
        if p.is_file() and p.suffix in (".log",".jou",".wdb",".vcd",".dcp",".xpr"):
            errors.append("Root build artifact "+p.name)
    for folder in ("rtl","software","scripts","tb","tests"):
        for p in (ROOT/folder).rglob("*"):
            if p.suffix in (".py",".sv",".tcl"):
                content=p.read_text(encoding="utf-8")
                # Explicit implementation markers only; skip legitimate safety and audit prose.
                for line_num,line in enumerate(content.splitlines(),1):
                    if re.search(r"\b(TODO|FIXME)\b",line) and p.name != "check_repository.py":
                        errors.append(f"Unresolved marker {p.relative_to(ROOT)}:{line_num}")
    for p in [ROOT/"README.md",*(ROOT/"docs").rglob("*.md"),*(ROOT/"shared").rglob("*.md")]:
        for link in re.findall(r"\]\(([^)]+)\)",p.read_text(encoding="utf-8")):
            if "://" not in link and not link.startswith("#") and not (p.parent/link.split("#")[0]).exists():
                errors.append(f"Broken link {p.relative_to(ROOT)} -> {link}")
    summary=json.loads((ROOT/"evidence/simulation/vn1_release/summary.json").read_text())
    if summary["status"]!="PASS":errors.append("Digital gate not PASS")
    for path,digest in summary["source_sha256"].items():
        if hashlib.sha256((ROOT/path.replace("\\","/")).read_bytes()).hexdigest()!=digest:
            errors.append("Evidence stale for "+path)
    if list((ROOT/"constraints").glob("*.xdc")):errors.append("Unexpected board XDC before hardware gate")
    state=json.loads((ROOT/"shared/PROJECT_STATE.json").read_text())
    if state.get("hardware_verified"):errors.append("Unexpected hardware PASS claim")
    result={"status":"PASS" if not errors else "FAIL","errors":errors,
            "checks":["required artifacts","root generated-file hygiene","implementation markers",
                      "Markdown local links","digital evidence source hashes","no fabricated XDC/hardware PASS"]}
    print(json.dumps(result,indent=2))
    if errors:raise SystemExit(1)


if __name__=="__main__":main()
