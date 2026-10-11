"""Save accessible observable S3 messages and tool payload hashes only.

Never save analysis/summary/system/developer content or hidden reasoning.
The canonical user-provided instruction is stored separately without alteration.
"""
from pathlib import Path
import datetime, hashlib, json, os, re

R = Path(__file__).resolve().parents[1]
ROOT = R.parents[4]
ID = 'S-20261011-pcb-s3-001'


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def redact(s):
    s = re.sub(r'(?i)[CG]:[\\/]+Users[\\/]+loverlike[^\n"<>]*?(?=\n|"|<|>|$)', '[REDACTED_PERSONAL_PATH]', s)
    return re.sub(r'(?i)(?:sk-(?:proj-)?[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})', '[REDACTED_SECRET]', s)


def main():
    thread = os.environ['CODEX_THREAD_ID']
    sources = list((Path.home()/'.codex/sessions/2026/10/11').glob('*'+thread+'.jsonl'))
    assert len(sources) == 1
    messages, events = [], []
    active = False
    for line in sources[0].read_text(encoding='utf-8').splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get('type') != 'response_item':
            continue
        p = event.get('payload', {})
        typ = p.get('type')
        channel = p.get('channel') or p.get('phase')
        if typ == 'message' and (p.get('role') == 'user' or
                (p.get('role') == 'assistant' and channel in ['commentary', 'final', 'final_answer'])):
            content = '\n'.join(c.get('text', '') for c in p.get('content', [])
                                if c.get('type') in ['text', 'input_text', 'output_text'])
            if p.get('role') == 'user' and 'PCB-S3_Codex_Engineering_Instruction_20261011.md' in content:
                active = True
            if not active or not content:
                continue
            if content.startswith('# AGENTS.md instructions'):
                saved = 'Actual user AGENTS instructions received; canonical AGENTS.md/current S3 instruction applies. Large prompt referenced by its raw observable hash, not duplicated.'
            else:
                saved = redact(content)
            messages.append(dict(role=p.get('role'), time=event.get('timestamp'),
                                 text=saved, raw_observable_sha256=digest(content), channel=channel))
        elif active and typ in ['function_call', 'function_call_output', 'custom_tool_call', 'custom_tool_call_output']:
            serialized = json.dumps(p, ensure_ascii=False, sort_keys=True)
            events.append(dict(time=event.get('timestamp'), type=typ, name=p.get('name'),
                               call_id=p.get('call_id'), payload_sha256=digest(serialized),
                               characters=len(serialized)))
    assert messages and any('按 S3 文件完整执行' in m['text'] for m in messages)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    boundary = ('PARTIAL: accessible response_item user/commentary/final from the actual S3 document message '
                'through this cutoff only. Large AGENTS prompt referenced; personal paths/credential patterns '
                'redacted. Later final/publication events are not yet included. External ChatGPT reader BLOCKED. '
                'No inaccessible history, analysis, summaries or hidden reasoning saved.')
    text = f'''---
project_id: SONOFIELD_FPGA
source: codex
thread_id: {thread}
session_id: {ID}
active_version: v5
current_stage: PCB_S3_DEVICE_CANDIDATE
sync_status: PARTIAL
last_updated_at: {now}
message_count: {len(messages)}
---

# Observable Codex conversation

{boundary}

'''
    for i, m in enumerate(messages, 1):
        text += f"## Message {i:04d}\nRole: {m['role']}\nTime: {m['time']}\nRaw observable SHA256: {m['raw_observable_sha256']}\n\n{m['text']}\n\n"
    path = ROOT/'AI-interaction-memory/codex'/f'{ID}.md'
    path.write_text(text, encoding='utf-8')
    toolpath = path.with_suffix('.tools.json')
    toolpath.write_text(json.dumps(dict(thread_id=thread, status='PARTIAL', cutoff=now,
                                      boundary='Observable tool hashes only; no payload bodies or hidden reasoning.',
                                      events=events), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    index = ROOT/'AI-interaction-memory/INDEX.md'
    old = index.read_text(encoding='utf-8')
    if ID not in old:
        old += '''
## v5 PCB-S3 authorized device candidate

| ID/source | Record | Status | Impact |
|---|---|---|---|
| S-20261011-pcb-s3-001 / Codex | [observable transcript](codex/S-20261011-pcb-s3-001.md) and [tool hashes](codex/S-20261011-pcb-s3-001.tools.json) | PARTIAL | IMPLEMENTATION_INPUT |
| Actual S3 instruction / User | [canonical document](codex/instructions/v5_pcb_s3_engineering_20261011.md) | COMPLETE_DOCUMENT_ONLY | DESIGN_INPUT |
| T-20261011-PCB-S3 | [tool flow](tool-flow/T-20261011-PCB-S3__device-candidate.md) | PARTIAL | VALIDATION_INPUT |

Actual approval: 按 S3 文件完整执行，保持 v5、制造/采购/板写/main 合并 HOLD。
Canonical instruction SHA256: b3a33a2b0541e8626ea952f2c6c8288ae0a78b8133f024c1cd05c42036475e44.
Transcript hashes are recorded in SESSION_MANIFEST.json in S3 evidence. Current accessible observable messages only; no external ChatGPT decision or independent review invented.
'''
        index.write_text(old, encoding='utf-8')
    manifest = dict(project_id='SONOFIELD_FPGA', active_version='v5', thread_id=thread, id=ID,
                    status='PARTIAL', cutoff=now, message_count=len(messages), tool_event_count=len(events),
                    boundary=boundary, records=[dict(path=p.relative_to(ROOT).as_posix(),
                    sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in [path, toolpath]])
    (ROOT/'v5/evidence/pcb_s3_20261011/SESSION_MANIFEST.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:manifest[k] for k in ['id','status','message_count','tool_event_count','cutoff']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
