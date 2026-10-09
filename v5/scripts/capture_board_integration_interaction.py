"""Incrementally capture actual visible messages for this authorized v5 session.

Uses existing public redaction rules. No reasoning or tool payloads are exported.
Does not rewrite previously captured session files or truncate the master index.
"""
from pathlib import Path
import hashlib
import json
import sys

R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / 'AI-interaction-memory/tools'))
import sync_codex as sync


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


def main():
    source = Path.home() / '.codex/sessions/2026/09/18/rollout-2026-09-18T23-52-59-01a0b538-9430-7561-9ba4-623f57501f43.jsonl'
    meta, messages, calls, boundary = sync.extract(source, R)
    after = '2026-10-08T11:19:15.042Z'
    messages = [m for m in messages if m['time'] > after]
    calls = [c for c in calls if c['time'] > after]
    sid = 'S-20261009-codex-001'
    root = R / 'AI-interaction-memory'
    text = f'''# Observable Codex conversation — {sid}

PROJECT_ID: SONOFIELD_FPGA. Active version: v5. Current Stage: AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT. Provider: OpenAI. Model: GPT-6.1 Sol High (user-declared, not inferred runtime metadata). Actual source thread: {meta['id']}; source file: {source.name}. Incremental after {after}. Status PARTIAL: capture ends at {boundary['cutoff']}; the current final reply may not yet exist.

Only actual user and assistant commentary/final messages are exported with redaction. Hidden reasoning, system/developer text, compaction summaries, raw tool parameters/outputs and binary images are excluded. External ChatGPT source SonoField-FPGA is separately BLOCKED. No reconstructed transcript or independent review is invented.

'''
    for i, message in enumerate(messages, 1):
        text += f"## Message {i:04d}\n\nRole: {message['role']}\nTime: {message['time']}\nSource ID: {message['id']}\nSource line: {message['source_line']}\nSanitized content SHA256: {message['sha256']}\n\n````````text\n{message['text']}\n````````\n\n"
    text = text.rstrip() + '\n'
    assert sync.sanitize(text) == text
    flow = f'''# Observable tool-call register — {sid}

PARTIAL. Names/IDs/source-line references only. No raw payloads or hidden reasoning. Selected actual commands/results are separately curated in T-20261009-001__ax7020-board-bom.md and linked evidence.

| Time | Tool | Call ID | Source line | Output source line |
|---|---|---|---|---|
'''
    for call in calls:
        out = call['output_reference']
        flow += f"| {call['time']} | {call['name']} | {call['call_id']} | {call['source_line']} | {out['source_line'] if isinstance(out, dict) else out} |\n"
    flow = flow.rstrip() + '\n'
    files = {f'codex/{sid}.md': sync.file_digest(text), f'tool-flow/{sid}.md': sync.file_digest(flow)}
    manifest = dict(project_id='SONOFIELD_FPGA', active_version='v5', thread_id=meta['id'], session_id=sid,
        current_stage='AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT', model='GPT-6.1 Sol High', model_provenance='USER_DECLARED',
        sync_status='PARTIAL', source_file=source.name, started_at=messages[0]['time'] if messages else 'UNKNOWN', previous_cutoff=after,
        **boundary, message_count=len(messages), tool_call_count=len(calls), messages=[{k:v for k,v in m.items() if k != 'text'} for m in messages], files=files)
    target = root / 'sessions' / f'{sid}.json'
    if target.exists():
        old = json.loads(target.read_text(encoding='utf-8'))
        current = {m['id']: m['sha256'] for m in messages}
        assert all(current.get(m['id']) == m['sha256'] for m in old['messages']), 'Captured source events must not change silently'
    write(root / 'codex' / f'{sid}.md', text)
    write(root / 'tool-flow' / f'{sid}.md', flow)
    write(target, json.dumps(manifest, ensure_ascii=False, indent=2))
    attachment = Path.home() / '.codex/attachments/4b78522d-e640-448c-8788-c916d293b560/已粘贴的文本.txt'
    raw = attachment.read_text(encoding='utf-8-sig')
    published = sync.sanitize(raw)
    write(root / 'codex/instructions/ax7020_v5_board_bom_integration.md', published)
    write(root / 'codex/instructions/ax7020_v5_board_bom_integration.provenance.json', json.dumps(dict(
        source='Actual user attachment 4b78522d-e640-448c-8788-c916d293b560', source_type='USER_INSTRUCTION_NOT_CHATGPT_DECISION',
        raw_sha256_bytes=hashlib.sha256(attachment.read_bytes()).hexdigest(), published_sanitized_canonical_sha256=sync.file_digest(published.rstrip()+'\n'),
        active_version='v5', privacy_status='SANITIZED', model='GPT-6.1 Sol High'), ensure_ascii=False, indent=2))
    index = root / 'INDEX.md'
    prior = index.read_text(encoding='utf-8')
    marker = '<!-- AX7020_BOARD_BOM_20261009 -->'
    end_marker = '<!-- END_AX7020_BOARD_BOM_20261009 -->'
    if marker in prior:
        assert end_marker in prior, 'Never truncate an unknown following index section'
        start = prior.index(marker)
        end = prior.index(end_marker, start) + len(end_marker)
        following = prior[end:]
        prior = prior[:start]
    else:
        following = ''
    # This marker is owned by this script only; previous entries remain intact.
    prior += f'''

{marker}
## Current AX7020 board/BOM integration — 2026-10-09

Active v5; Stage AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT; OpenAI / GPT-6.1 Sol High (user-declared). [Session {sid}](codex/{sid}.md) · [manifest](sessions/{sid}.json) · [observable tool register](tool-flow/{sid}.md). {len(messages)} actual visible messages; cutoff {boundary['cutoff']}; PARTIAL. Canonical sanitized transcript SHA256 {files[f'codex/{sid}.md']}. Impact IMPLEMENTATION_INPUT.

[Formal user instruction](codex/instructions/ax7020_v5_board_bom_integration.md) · [curated tool flow T-20261009-001](tool-flow/T-20261009-001__ax7020-board-bom.md), VALIDATION_INPUT, PARTIAL. No external ChatGPT/Work/other-agent consultation occurred. ChatGPT source remains BLOCKED; independent review PENDING. Original device identities/photos stay private local_raw. Current state/checkpoint supersedes older recovery scope, preserving original history.
{end_marker}
'''
    write(index, prior + following)
    print(json.dumps(dict(status='PARTIAL', messages=len(messages), calls=len(calls), cutoff=boundary['cutoff'], secret_scan='PASS')))


if __name__ == '__main__':
    main()
