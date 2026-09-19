"""Audit current v1 layout, live evidence and external-decision provenance."""
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent


def main():
    errors=[]
    required=["README.md","AGENTS.md","CHANGELOG.md","shared/CURRENT_PLAN.md",
              "shared/PROJECT_STATE.json","shared/PROJECT_STATE.md","shared/VERSION_STATE.json",
              "shared/DECISIONS.md","shared/ACCEPTANCE.md","shared/BLOCKERS.md","shared/HANDOFF.md",
              "shared/report_v1.md","AI-chat-memory/INDEX.md","AI-chat-memory/SonoField-FPGA.md",
              "AI-chat-memory/CHAT_MEMORY_IMPORT_REQUIRED.md","AI-problem/README.md",
              "v1/README.md","v1/VERSION_MANIFEST.md","v1/docs/OPERATING_GUIDE.md"]
    for name in required:
        if not (REPO/name).is_file():errors.append("Missing "+name)
    versions=json.loads((REPO/"shared/VERSION_STATE.json").read_text(encoding="utf-8"))
    if versions["active_version"]!="v1" or versions["highest_version"]!="v1":errors.append("Unexpected version")
    if versions["upgrade_pending"] or versions["legacy_versions"]:errors.append("Unexpected version migration state")
    actual_versions=sorted(p.name for p in REPO.iterdir() if p.is_dir() and re.fullmatch(r"v[0-9]+",p.name))
    if actual_versions!=["v1"]:errors.append("Only v1 may exist")
    for base in (ROOT,REPO):
        for p in base.glob("*"):
            if p.is_file() and p.suffix in (".log",".jou",".wdb",".vcd",".dcp",".xpr"):
                errors.append("Root build artifact "+str(p.relative_to(REPO)))
    for folder in ("rtl","software","scripts","tb","tests"):
        for p in (ROOT/folder).rglob("*"):
            if p.suffix in (".py",".sv",".tcl"):
                for n,line in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
                    if re.search(r"\b(TODO|FIXME)\b",line) and p.name!="check_repository.py":
                        errors.append(f"Unresolved marker {p.relative_to(REPO)}:{n}")
    documents=[REPO/"README.md",ROOT/"README.md"]
    for base in (ROOT/"docs",ROOT/"hardware",REPO/"shared",REPO/"AI-chat-memory",REPO/"AI-problem"):
        documents.extend(base.rglob("*.md"))
    for p in documents:
        for link in re.findall(r"\]\(([^)]+)\)",p.read_text(encoding="utf-8")):
            if "://" not in link and not link.startswith("#") and not (p.parent/link.split("#")[0]).exists():
                errors.append(f"Broken link {p.relative_to(REPO)} -> {link}")
    state=json.loads((REPO/"shared/PROJECT_STATE.json").read_text(encoding="utf-8"))
    if state["active_version"]!="v1" or state["chat_source_name"]!="SonoField-FPGA":errors.append("State identity mismatch")
    summary=json.loads((REPO/state["digital_evidence"]).read_text(encoding="utf-8"))
    if summary["status"]!="PASS":errors.append("Digital gate not PASS")
    for path,digest in summary["source_sha256"].items():
        if hashlib.sha256((ROOT/path.replace("\\","/")).read_bytes()).hexdigest()!=digest:errors.append("Stale RTL evidence "+path)
    for path,digest in summary.get("source_text_sha256",{}).items():
        if hashlib.sha256((ROOT/path).read_text(encoding="utf-8").encode("utf-8")).hexdigest()!=digest:errors.append("Stale model/control evidence "+path)
    if list((ROOT/"constraints").glob("*.xdc")):errors.append("Unexpected XDC before board gate")
    if state.get("hardware_verified"):errors.append("Unexpected hardware PASS")
    problem_ids=[]
    for p in (REPO/"AI-problem/problem").glob("P-*.md"):
        text=p.read_text(encoding="utf-8");_,front,body=text.split("---\n",2)
        metadata=dict(line.split(": ",1) for line in front.strip().splitlines())
        if hashlib.sha256(body.encode("utf-8")).hexdigest()!=metadata["problem_hash"]:errors.append("Problem hash mismatch "+p.name)
        if metadata["active_version"]!="v1":errors.append("Problem version mismatch "+p.name)
        problem_ids.append(metadata["problem_id"])
    if sorted(problem_ids)!=sorted(state["open_ai_problems"]):errors.append("Open problem index mismatch")
    for folder in (REPO/"shared",REPO/"AI-chat-memory",REPO/"AI-problem",ROOT):
        for p in folder.rglob("*"):
            if any(part in ("build","__pycache__","references") for part in p.relative_to(folder).parts):continue
            if re.search(r"(?i)vn[0-9]+",p.name):errors.append("Obsolete version-bearing path "+str(p.relative_to(REPO)))
    result={"status":"PASS" if not errors else "FAIL","errors":errors,
            "checks":["v1 layout and state","required artifacts","root hygiene","implementation markers",
                      "Markdown links","live source hashes","no fabricated board PASS","Problem ID/version/body SHA256"]}
    print(json.dumps(result,indent=2))
    if errors:raise SystemExit(1)


if __name__=="__main__":main()
