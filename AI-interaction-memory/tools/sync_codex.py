"""Export only observable user/assistant messages from an explicitly selected local rollout.

Never exports reasoning, compaction summaries, system/developer instructions or raw runtime objects.
Outputs are public-safe snapshots; repeat exports merge by source event identity, not inferred text.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

REPO = Path(__file__).resolve().parents[2]
SECRET_PATTERNS = [
    r"-----BEGIN (?:[A-Z ]+)?PRIVATE KEY-----[\s\S]*?-----END (?:[A-Z ]+)?PRIVATE KEY-----",
    r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{25,})\b",
    r"(?i)\bBearer\s+[A-Za-z0-9._~+/-]{12,}=*",
    r'''(?i)(?:api[_-]?key|access[_-]?token|password|cookie|secret|otp)\s*[=:]\s*["']?[^\s"'<>;,]{6,}''',
]


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def file_digest(text):
    return digest(text.replace("\r\n", "\n").replace("\r", "\n"))


def sanitize(text):
    for pattern in SECRET_PATTERNS:
        text = re.sub(pattern, "[REDACTED_SECRET]", text)
    text = re.sub(r"(?i)[A-Z]:[\\/]Users[\\/][^\\/\s\"']+", "[USER_HOME]", text)
    text = re.sub(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b", "[REDACTED_EMAIL]", text)
    text = re.sub(r"data:[^\s\"']+;base64,[A-Za-z0-9+/=]+", "[OMITTED_BINARY]", text)
    return text


def text_content(parts):
    return "\n".join(p.get("text", "") for p in parts
                     if p.get("type") in ("input_text", "output_text", "text"))


def extract(source, expected_workspace):
    messages, calls, outputs = [], [], {}
    meta, cutoff, compacted, partial_line = None, "UNKNOWN", False, False
    lines = source.read_bytes().splitlines(keepends=True)
    for n, raw in enumerate(lines, 1):
        try:
            row = json.loads(raw)
        except (ValueError, UnicodeDecodeError):
            if n == len(lines) and not raw.endswith(b"\n"):
                partial_line = True
                break
            raise ValueError(f"Malformed source JSONL at line {n}")
        kind, item = row.get("type"), row.get("payload", {})
        cutoff = row.get("timestamp", cutoff)
        if kind == "session_meta":
            meta = {k: item.get(k, "UNKNOWN") for k in ("id", "cwd", "timestamp")}
        if kind == "compacted":
            compacted = True
        if kind != "response_item":
            continue
        entry_type = item.get("type")
        role, phase, channel = item.get("role"), item.get("phase"), item.get("channel")
        visible = role == "user" or (role == "assistant" and
                  (phase in ("commentary", "final_answer") or channel in ("commentary", "final")))
        if entry_type == "message" and visible and channel not in ("analysis", "summary"):
            text = sanitize(text_content(item.get("content", [])))
            if text:
                messages.append({"id": item.get("id") or f"source-line-{n}", "role": role,
                                 "time": row.get("timestamp", "UNKNOWN"), "source_line": n,
                                 "text": text, "sha256": digest(text)})
        elif entry_type in ("function_call", "custom_tool_call"):
            # Tool-flow register stores explicit name/IDs only. Full inputs may contain echoes of
            # source log inspection; copying those would risk exporting excluded reasoning indirectly.
            calls.append({"call_id": item.get("call_id", "UNKNOWN"), "name": item.get("name", "UNKNOWN"),
                          "time": row.get("timestamp", "UNKNOWN"), "source_line": n})
        elif entry_type in ("function_call_output", "custom_tool_call_output"):
            outputs[item.get("call_id")] = {"time": row.get("timestamp", "UNKNOWN"), "source_line": n}
    workspace_match = bool(meta) and Path(meta["cwd"]).resolve() == Path(expected_workspace).resolve()
    state_path = Path(expected_workspace) / "shared/PROJECT_STATE.json"
    if meta and not workspace_match and state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        # A verified relocation is scoped to one project and session, never a global path bypass.
        workspace_match = state.get("project_id") == "SONOFIELD_FPGA" and any(
            item.get("thread_id") == meta["id"]
            and Path(item["path"]).resolve() == Path(meta["cwd"]).resolve()
            for item in state.get("verified_previous_workspaces", []))
    if not workspace_match:
        raise ValueError("Session workspace does not match this repository")
    if not re.fullmatch(r"[a-zA-Z0-9-]+", meta["id"]):
        raise ValueError("Invalid session identity")
    for c in calls:
        c["output_reference"] = outputs.get(c["call_id"], "NOT_CAPTURED_AT_CUTOFF")
    return meta, messages, calls, {"cutoff": cutoff, "compaction_present": compacted,
                                   "incomplete_tail": partial_line, "source_line_count": len(lines)}


def write_changed(path, text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8", newline="\n")


def export(source, repo=REPO):
    meta, messages, calls, boundary = extract(source, repo)
    state_path=repo / "shared/PROJECT_STATE.json"
    state=json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    active=state.get("active_version", "UNKNOWN")
    root = repo / "AI-interaction-memory"
    sid = meta["id"]
    manifest_path = root / "sessions" / f"{sid}.json"
    # Persist original public payloads and reject mutation rather than silently rewriting history.
    if manifest_path.exists():
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        new_by_id = {m["id"]: m["sha256"] for m in messages}
        for event in old["messages"]:
            if new_by_id.get(event["id"]) != event["sha256"]:
                raise ValueError("Source lost/changed a previously captured message; preserve old export and review")
    header = (f"# Codex conversation — {sid}\n\nProject: SONOFIELD_FPGA. Active version at export: {active}.\n"
              f"Source: local Codex rollout `{source.name}`; provider OpenAI. Thread/session: {sid}.\n"
              "Sync status: PARTIAL. Public-safe source transcript, not a reconstructed summary.\n"
              "Only actual user messages and visible assistant commentary/final answers are included.\n"
              "Images, system/developer prompts, reasoning, compaction summaries and tool payloads excluded.\n"
              "Old version words inside quoted instructions are historical quotations, not active versions.\n"
              f"First source time: {meta['timestamp']}. Last message time: {messages[-1]['time'] if messages else 'UNKNOWN'}.\n"
              "Current open turn and unavailable/compacted history prevent a COMPLETE claim.\n\n")
    body = []
    for i, m in enumerate(messages, 1):
        fence = "`" * max(3, 1 + max((len(v) for v in re.findall(r"`+", m["text"])), default=0))
        body.append(f"## Message {i:04d}\n\nRole: {m['role']}\nTime: {m['time']}\n"
                    f"Source ID: {m['id']}\nSource line: {m['source_line']}\n"
                    f"Sanitized content SHA256: {m['sha256']}\n\n{fence}text\n{m['text']}\n{fence}\n")
    transcript = header + "\n".join(body)
    write_changed(root / "codex" / f"{sid}.md", transcript)
    flow = (f"# Observable tool-call register — {sid}\n\nStatus: PARTIAL. Names, call IDs, source line references and output-presence only.\n"
            "No command/result payload is claimed here. Important commands/results are recorded in the curated\n"
            "tool-flow report and linked repository evidence; excluded source payloads may contain sensitive/private content.\n\n"
            "| Time (UTC) | Tool | Call ID | Input source line | Output source line |\n|---|---|---|---|---|\n")
    for c in calls:
        output = c["output_reference"]
        flow += f"| {c['time']} | {c['name']} | {c['call_id']} | {c['source_line']} | {output['source_line'] if isinstance(output, dict) else output} |\n"
    write_changed(root / "tool-flow" / f"{sid}.md", flow)
    manifest = {"project_id": "SONOFIELD_FPGA", "active_version": active, "thread_id": sid,
                "sync_status": "PARTIAL", "source_file": source.name, "started_at": meta["timestamp"],
                **boundary, "message_count": len(messages), "tool_call_count": len(calls),
                "messages": [{k: v for k, v in m.items() if k != "text"} for m in messages],
                "files": {f"codex/{sid}.md": file_digest(transcript), f"tool-flow/{sid}.md": file_digest(flow)}}
    write_changed(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    index(root)
    return manifest


def index(root):
    state_path=root.parent / "shared/PROJECT_STATE.json"
    state=json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    text = ("# AI Interaction Memory Index\n\nCanonical ChatGPT history: [SonoField-FPGA](../AI-chat-memory/SonoField-FPGA.md), BLOCKED.\n"
            "Codex records below are distinct from external ChatGPT history. Provider: OpenAI.\n"
            "Work, other AI and cross-agent consultations: none captured; no participation invented.\n"
            f"Source timestamps are UTC. Active version {state.get('active_version','UNKNOWN')}. Stage: {state.get('current_stage','UNKNOWN')}.\n\n"
            "| Thread / Session | Role / Impact | First used | Last captured | Record | Status | Content SHA256 |\n|---|---|---|---|---|---|---|\n")
    for p in sorted((root / "sessions").glob("*.json")):
        m = json.loads(p.read_text(encoding="utf-8")); sid = m["thread_id"]
        for kind, impact in (("codex", "IMPLEMENTATION_INPUT"), ("tool-flow", "VALIDATION_INPUT")):
            name = f"{kind}/{sid}.md"
            text += f"| {sid} | {kind} / {impact} | {m['started_at']} | {m['cutoff']} | [{kind}]({name}) | PARTIAL | {m['files'][name]} |\n"
    text += "\n[Capture policy and commands](README.md) · [Current tool flow](tool-flow/T-20260920-001__interaction-memory.md)\n"
    if (root/'codex/instructions/v2_formal_development.md').exists():
        text += "\n[User v2 instruction and approval](codex/instructions/v2_formal_development.md) · [v2 bootstrap flow](tool-flow/T-20260921-001__v2-bootstrap.md)\n"
    if (root/"codex/instructions/v2_self_calibration.md").exists():
        text += "\n[User software/digital instruction](codex/instructions/v2_self_calibration.md) · [Calibration stage flow](tool-flow/T-20260921-002__self-calibration.md)\n"
    write_changed(root / "INDEX.md", text)


def check(repo=REPO):
    root = repo / "AI-interaction-memory"
    records = list((root / "sessions").glob("*.json"))
    if not records:
        raise ValueError("No captured sessions")
    for p in records:
        m = json.loads(p.read_text(encoding="utf-8"))
        if m["sync_status"] != "PARTIAL" or len(m["messages"]) != m["message_count"]:
            raise ValueError("Session coverage metadata mismatch")
        for relative, sha in m["files"].items():
            path = (root / relative).resolve()
            if root.resolve() not in path.parents or file_digest(path.read_text(encoding="utf-8")) != sha:
                raise ValueError("Transcript/tool-register integrity mismatch")
            text = path.read_text(encoding="utf-8")
            if sanitize(text) != text:
                raise ValueError("INTERACTION_MEMORY_SECRET_SCAN: unredacted pattern")
    return {"status": "PASS", "sessions": len(records), "scope": "canonical hashes and public redaction rules"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        result = check()
    elif args.source:
        m = export(args.source)
        result = {k: m[k] for k in ("thread_id", "sync_status", "message_count", "tool_call_count", "cutoff")}
    else:
        parser.error("Use --source with an explicit authorized local JSONL, or --check")
    print(json.dumps(result, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
