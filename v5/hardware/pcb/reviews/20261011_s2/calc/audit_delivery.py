"""Audit only this task's explicit current payload before public publication.
No historical body access, secret values, private reasoning, or hardware claims.
"""
from pathlib import Path
import datetime, hashlib, json, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
R = Path(__file__).resolve().parent.parent
V5 = R.parents[3]
ROOT = V5.parent
E = V5 / "evidence/pcb_s2_20261011"
EXACT = {
    ".gitattributes",
    "AI-interaction-memory/INDEX.md", "AI-problem/INDEX.md", "CHANGELOG.md",
    "shared/ACCEPTANCE.md", "shared/BLOCKERS.md", "shared/CONTEXT_CHECKPOINT.json",
    "shared/CONTEXT_CHECKPOINT.md", "shared/CURRENT_PLAN.md", "shared/DECISIONS.md",
    "shared/PROJECT_STATE.json", "shared/VERSION_STATE.json",
    "shared/context-checkpoints/CP-20261011-002__v5__pcb-s2-review.md",
    "AI-problem/problem/P-20261011-001__pcb-safety-and-electrical-gates.md",
    "AI-problem/decision/P-20261011-001__pcb-supervisor-user-direction.md",
    "AI-interaction-memory/codex/S-20261011-pcb-s2-001.md",
    "AI-interaction-memory/codex/S-20261011-pcb-s2-001.tools.json",
    "AI-interaction-memory/codex/instructions/v5_pcb_task_start_20261011.md",
    "AI-interaction-memory/codex/instructions/v5_pcb_architecture_parameter_review_20261011.md",
    "AI-interaction-memory/tool-flow/T-20261011-PCB-001__pcb-review.md",
}
PREFIXES = ("v5/hardware/pcb/", "v5/evidence/pcb_s2_20261011/")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT).decode("utf-8").splitlines()


def main():
    # Metadata-only enumeration; every body read is checked against the task allowlist.
    changed = set(git("diff", "--name-only", "8c27b5841b5494c3761ab211881a3ea2be63e8c8", "--"))
    changed.update(git("ls-files", "--others", "--exclude-standard"))
    assert all(p in EXACT or p.startswith(PREFIXES) for p in changed), sorted(changed - EXACT)
    patterns = {
        "provider_key": r"(?:sk-(?:proj-)?[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})",
        "private_key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        "bearer_token": r"(?i)Bearer\s+[A-Za-z0-9_.-]{24,}",
        "credential_url": r"https?://[^\s/@:]+:[^\s/@]+@",
    }
    findings = []
    personal = []
    files = []
    json_count = 0
    for rel in sorted(changed):
        p = ROOT / rel
        assert p.is_file(), rel
        assert not any(s in p.parts for s in ["local_raw", "digital_full", "__pycache__"]), rel
        data = p.read_bytes()
        text = data.decode("utf-8-sig")
        if p.suffix == ".json":
            json.loads(text)
            json_count += 1
        for name, pattern in patterns.items():
            if re.search(pattern, text):
                findings.append(dict(path=rel, pattern=name))
        if re.search(r"(?i)[CG]:[\\/]+Users[\\/]+loverlike", text):
            personal.append(rel)
        if p.name not in ["DELIVERY_HASHES.json", "PUBLICATION_AUDIT.json", "PUBLICATION_RECEIPT.json"]:
            files.append(dict(path=rel, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), canonical_lf_utf8_sha256=hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()))
    problem = (ROOT / "AI-problem/problem/P-20261011-001__pcb-safety-and-electrical-gates.md").read_text(encoding="utf-8")
    decision = (ROOT / "AI-problem/decision/P-20261011-001__pcb-supervisor-user-direction.md").read_text(encoding="utf-8")
    digest = hashlib.sha256(problem.split("---\n\n", 1)[1].encode("utf-8")).hexdigest()
    assert "problem_hash: " + digest in problem and "problem_hash: " + digest in decision
    assert "active_version: v5" in problem and "active_version: v5" in decision
    assert json.loads((ROOT / "shared/VERSION_STATE.json").read_text(encoding="utf-8"))["active_version"] == "v5"
    canonical = ROOT / "AI-interaction-memory/codex/instructions/v5_pcb_architecture_parameter_review_20261011.md"
    assert hashlib.sha256(canonical.read_bytes()).hexdigest() == "d14eb709d7b625158ba40af32b2b0c56166101dc6e4beeb68b485d5d2da35e2e"
    assert not findings, findings
    assert not personal, personal
    out = dict(status="PASS", scope="EXPLICIT_CURRENT_TASK_PUBLIC_PAYLOAD_ONLY", recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               files_scanned=len(changed), json_parsed=json_count, secrets=findings, unredacted_personal_user_directories=personal,
               problem_id="P-20261011-001", problem_body_sha256=digest, problem_decision_version="v5",
               historical_body_read=False, note="Pattern/privacy review is bounded; no claim of an exhaustive security certification.")
    (E / "PUBLICATION_AUDIT.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (E / "DELIVERY_HASHES.json").write_text(json.dumps(dict(scope="Local deliverable bytes plus canonical LF hashes for text checkout portability. Evidence/received instructions use -text and preserve raw bytes. Excludes this manifest/audit/publication receipt to avoid self-reference", files=files), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PUBLIC_PAYLOAD_AUDIT PASS", len(changed), "files;", json_count, "JSON; problem ID/hash/version matched")


if __name__ == "__main__":
    main()
