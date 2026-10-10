"""Export observable current-task messages; never read reasoning or old projects."""
from pathlib import Path
import argparse, datetime, hashlib, json, re

ROOT = Path(__file__).resolve().parents[2]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def redact(text):
    text = re.sub(r'(?i)[A-Z]:[\\/](?:Users|wechat)[\\/][^\n<>"\r]+', '[REDACTED_PRIVATE_PATH]', text)
    text = re.sub(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,})\b', '[REDACTED_SECRET]', text)
    text = re.sub(r'(?i)([?&]pwd=)[^\s&<>]+', r'\1[REDACTED_SECRET]', text)
    text = re.sub(r'(提取码\s*[:：]?\s*)[A-Za-z0-9]{4}\b', r'\1[REDACTED_SECRET]', text)
    return text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--session', type=Path, required=True)
    parser.add_argument('--start', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--record-id', default='S-20261010-nextstage-001')
    args = parser.parse_args()
    out = args.output.resolve()
    if not out.is_relative_to(ROOT/'AI-interaction-memory/codex'):
        raise ValueError('Output must be a current interaction record')
    raw = args.session.read_bytes()
    messages, events, session_id = [], [], 'UNKNOWN'
    lines = raw.splitlines()
    for number, line in enumerate(lines, 1):
        try:
            record = json.loads(line)
        except (ValueError, UnicodeDecodeError):
            continue
        payload = record.get('payload', {})
        if record.get('type') == 'session_meta':
            session_id = payload.get('id', 'UNKNOWN')
        timestamp = record.get('timestamp', '')
        if timestamp < args.start or record.get('type') != 'response_item':
            continue
        kind = payload.get('type')
        if kind == 'message' and payload.get('role') in ('user', 'assistant'):
            channel = payload.get('channel', payload.get('phase'))
            if payload.get('role') == 'assistant' and channel not in ('commentary', 'final'):
                continue
            chunks = [c.get('text', '') for c in payload.get('content', []) if isinstance(c, dict) and 'text' in c]
            body = '\n'.join(chunks)
            if body:
                public = redact(body)
                messages.append(dict(role=payload['role'], channel=channel, message_id=payload.get('id', 'UNKNOWN'), timestamp=timestamp,
                    source_line=number, raw_text_sha256=digest(body.encode()), public_text_sha256=digest(public.encode()), text=public))
        elif kind in ('function_call', 'custom_tool_call', 'function_call_output', 'custom_tool_call_output'):
            observed = payload.get('arguments', payload.get('input', payload.get('output', '')))
            if not isinstance(observed, str):
                observed = json.dumps(observed, ensure_ascii=False)
            events.append(dict(type=kind, name=payload.get('name'), call_id=payload.get('call_id'),
                timestamp=timestamp, source_line=number, observable_payload_sha256=digest(observed.encode())))
    meta = dict(project_id='SONOFIELD_FPGA', active_version='v5', current_stage='S0-S7_NEXTSTAGE',
        session_id=args.record_id, thread_id=session_id, sync_status='PARTIAL',
        scope='Actual new request and subsequent visible messages up to source snapshot; no hidden reasoning; no inaccessible history',
        source_basename=args.session.name, source_snapshot_sha256=digest(raw), source_line_cutoff=len(lines),
        timestamp_cutoff=datetime.datetime.now(datetime.timezone.utc).isoformat(), message_count=len(messages),
        tool_event_count=len(events), start=args.start, privacy='Private user paths and credential patterns redacted; tool payloads stored as hashes only')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('---\n'+json.dumps(meta, ensure_ascii=False, indent=2)+'\n---\n\n# Observable Codex conversation\n\n'+
        '\n\n'.join('## Message %04d\nRole: %s\nTime: %s\nSource line: %s\nRaw SHA256: %s\nPublic SHA256: %s\n\n%s' %
            (i, m['role'], m['timestamp'], m['source_line'], m['raw_text_sha256'], m['public_text_sha256'], m['text'])
            for i,m in enumerate(messages,1))+'\n', encoding='utf-8')
    events_path = out.with_suffix('.tools.json')
    events_path.write_text(json.dumps(dict(metadata=meta, events=events), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(status='PARTIAL', messages=len(messages), tool_events=len(events),
        transcript_sha256=digest(out.read_bytes()), events_sha256=digest(events_path.read_bytes())), indent=2))

if __name__ == '__main__':
    main()
