"""Capture actual visible events only; no reasoning/tool payload reconstruction."""
from pathlib import Path
import sys,json,hashlib
R=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(R/'AI-interaction-memory/tools'))
import sync_codex as sync
from archive_after_baseline import write,dump

if __name__=='__main__':
    source=Path('C:/Users/loverlike/.codex/sessions/2026/09/18/rollout-2026-09-18T23-52-59-01a0b538-9430-7561-9ba4-623f57501f43.jsonl')
    meta,messages,calls,boundary=sync.extract(source,R)
    after='2026-10-03T20:47:02.532Z'
    messages=[m for m in messages if m['time']>after]
    calls=[c for c in calls if c['time']>after]
    sid='S-20261008-codex-001';root=R/'AI-interaction-memory'
    transcript=f'''# Observable Codex conversation — {sid}

PROJECT_ID:SONOFIELD_FPGA. Current authorized version:v5 (older messages retain their real version). Model record:GPT-6.1 Sol High, user-declared; exact platform runtime model metadata unavailable. Provider:OpenAI. Source thread:{meta['id']}. Source file:{source.name}. Capture is PARTIAL and incrementally follows the previous cutoff {after}. Current turn final reply may not yet exist at capture. External ChatGPT history is a separate BLOCKED source.

Only actual observable user messages and assistant commentary/final are captured, sanitized for public GitHub. No hidden reasoning, system/developer text, compaction summary, images/binary payload or raw tool parameters/output is exported. Source message timestamps/line references below are observed, not invented.

'''
    for i,m in enumerate(messages,1):
        transcript+=f"## Message {i:04d}\n\nRole:{m['role']}\nTime:{m['time']}\nSource ID:{m['id']}\nSource line:{m['source_line']}\nSanitized content SHA256:{m['sha256']}\n\n"+'````````text\n'+m['text']+'\n````````\n\n'
    assert sync.sanitize(transcript)==transcript,'Secret/privacy sanitation did not stabilize'
    flow=f'# Observable tool-call register — {sid}\n\nPARTIAL. Names/IDs/source-line references only; no hidden reasoning or sensitive raw tool payload. Actual selected commands/results are separately curated in T-20261008-001__v5-organization.md and linked evidence.\n\n| Time | Tool | Call ID | Source line | Output source line |\n|---|---|---|---|---|\n'
    for c in calls:
        ref=c['output_reference'];flow+=f"| {c['time']} | {c['name']} | {c['call_id']} | {c['source_line']} | {ref['source_line'] if isinstance(ref,dict) else ref} |\n"
    files={f'codex/{sid}.md':sync.file_digest(transcript),f'tool-flow/{sid}.md':sync.file_digest(flow)}
    manifest={'project_id':'SONOFIELD_FPGA','active_version':'v5','thread_id':meta['id'],'session_id':sid,
      'sync_status':'PARTIAL','model':'GPT-6.1 Sol High','model_provenance':'USER_DECLARED','started_at':messages[0]['time'] if messages else 'UNKNOWN',
      'source_file':source.name,'previous_cutoff':after,**boundary,'message_count':len(messages),'tool_call_count':len(calls),
      'messages':[{k:v for k,v in m.items() if k!='text'} for m in messages],'files':files}
    target=root/'sessions'/f'{sid}.json'
    if target.exists():
        old=json.loads(target.read_text(encoding='utf-8'));current={m['id']:m['sha256'] for m in messages}
        assert all(current.get(m['id'])==m['sha256'] for m in old['messages']),'Never silently mutate captured source events'
    write(root/'codex'/f'{sid}.md',transcript);write(root/'tool-flow'/f'{sid}.md',flow);dump(target,manifest)
    attachment=Path('C:/Users/loverlike/.codex/attachments/e8213cac-ae60-4eee-bb3e-6461d16eaf66/已粘贴的文本.txt')
    raw=attachment.read_text(encoding='utf-8-sig');sanitized=sync.sanitize(raw)
    write(root/'codex/instructions/ax7020_v5_safe_organization.md',sanitized)
    dump(root/'codex/instructions/ax7020_v5_safe_organization.provenance.json',{'source':'User actual attachment e8213cac-ae60-4eee-bb3e-6461d16eaf66',
      'raw_sha256_bytes':hashlib.sha256(attachment.read_bytes()).hexdigest(),'published_sanitized_canonical_sha256':sync.file_digest(sanitized),
      'version_authorized':'v5','source_type':'USER_INSTRUCTION_NOT_CHATGPT_DECISION','privacy_status':'SANITIZED','model_record':'GPT-6.1 Sol High'})
    index=root/'INDEX.md';text=index.read_text(encoding='utf-8');marker='<!-- CURRENT_V5_CAPTURE -->'
    if marker in text:text=text[:text.index(marker)]
    text+=f'''\n\n{marker}
## Current AX7020 v5 capture — 2026-10-08

[S-20261008-codex-001](codex/{sid}.md) · [manifest](sessions/{sid}.json) · [observable tool register](tool-flow/{sid}.md): {len(messages)} actual visible messages after previous cutoff, current cutoff {boundary['cutoff']}, PARTIAL. OpenAI; GPT-6.1 Sol High user-declared; IMPLEMENTATION_INPUT. Sanitized canonical transcript SHA256 {files[f'codex/{sid}.md']}.

[User-authorized v5 instruction](codex/instructions/ax7020_v5_safe_organization.md) · [actual tool flow T-20261008-001](tool-flow/T-20261008-001__v5-organization.md): VALIDATION_INPUT. Sole active version v5, AX7020; older index entries preserve original version/model provenance. External ChatGPT source SonoField-FPGA remains BLOCKED. No Work/other-agent consultation invented. Secret/privacy scan passed for this export; private raw logs/documents/backup remain local.
'''
    write(index,text)
    print(json.dumps({'status':'PARTIAL','messages':len(messages),'calls':len(calls),'cutoff':boundary['cutoff'],'secret_scan':'PASS'}))
