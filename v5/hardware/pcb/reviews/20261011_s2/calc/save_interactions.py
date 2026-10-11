"""Export only observable current-session user/commentary/final and tool hashes.
Analysis, summaries, developer/system text and private reasoning are never saved.
"""
from pathlib import Path
import datetime,hashlib,json,os,re,sys
sys.stdout.reconfigure(encoding='utf-8')
R=Path(__file__).resolve().parent.parent;ROOT=R.parents[4]
def h(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
def redact(s):
    s=re.sub(r'(?i)[CG]:[\\/]+Users[\\/]+loverlike[^\n"<>]*?(?=\n|"|<|>|$)','[REDACTED_PERSONAL_PATH]',s)
    s=re.sub(r'(?i)(?:sk-(?:proj-)?[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})','[REDACTED_SECRET]',s)
    return s
def main():
    thread=os.environ.get('CODEX_THREAD_ID');assert thread
    sources=list((Path.home()/'.codex/sessions/2026/10/11').glob('*'+thread+'.jsonl'));assert len(sources)==1
    messages=[];tool=[]
    for line in sources[0].read_text(encoding='utf-8').splitlines():
        try:event=json.loads(line)
        except json.JSONDecodeError:continue
        if event.get('type')!='response_item':continue
        p=event.get('payload',{});typ=p.get('type');channel=p.get('channel') or p.get('phase')
        if typ=='message' and (p.get('role')=='user' or (p.get('role')=='assistant' and channel in ['commentary','final','final_answer'])):
            content='\n'.join(c.get('text','') for c in p.get('content',[]) if c.get('type') in ['text','input_text','output_text'])
            if not content:continue
            if content.startswith('# AGENTS.md instructions'):
                messages.append(dict(role='user',time=event.get('timestamp'),text='Actual user AGENTS instructions received; canonical current AGENTS.md/project instruction applies. Full raw prompt hash only, not duplicated here.',sha256=h(content),boundary='LARGE_INSTRUCTION_REFERENCE'))
            else:messages.append(dict(role=p.get('role'),time=event.get('timestamp'),text=redact(content),sha256=h(content),channel=channel))
        elif typ in ['function_call','function_call_output','custom_tool_call','custom_tool_call_output']:
            # Explicit observable payload hashes only, no private reasoning/analysis.
            serialized=json.dumps(p,ensure_ascii=False,sort_keys=True)
            tool.append(dict(time=event.get('timestamp'),type=typ,name=p.get('name'),call_id=p.get('call_id'),payload_sha256=h(serialized),characters=len(serialized)))
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    j=dict(project_id='SONOFIELD_FPGA',source='codex',thread_id=thread,session_id=thread,active_version='v5',current_stage='PCB_S2_REVIEW',
       sync_status='PARTIAL',last_updated_at=now,message_count=len(messages),tool_event_count=len(tool),
       boundary='Only accessible response_item user/commentary/final through cutoff. Large AGENTS reference; source paths redacted; final delivery after cutoff not captured; externalChatGPTBLOCKED; no hidden reasoning.',messages=messages)
    path=ROOT/'AI-interaction-memory/codex/S-20261011-pcb-s2-001.md'
    body='---\nproject_id: SONOFIELD_FPGA\nsource: codex\nthread_id: '+thread+'\nactive_version: v5\ncurrent_stage: PCB_S2_REVIEW\nsync_status: PARTIAL\nlast_updated_at: '+now+'\nmessage_count: '+str(len(messages))+'\n---\n\n# Observable Codex conversation\n\n'+j['boundary']+'\n\n'
    for i,m in enumerate(messages,1):body+=f'## Message {i:04d}\nRole: {m["role"]}\nTime: {m["time"]}\nRaw observable payload SHA256: {m["sha256"]}\n\n{m["text"]}\n\n'
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body,encoding='utf-8')
    tp=ROOT/'AI-interaction-memory/codex/S-20261011-pcb-s2-001.tools.json';tp.write_text(json.dumps(dict(thread_id=thread,status='PARTIAL',cutoff=now,events=tool),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    index=ROOT/'AI-interaction-memory/INDEX.md';old=index.read_text(encoding='utf-8');marker='S-20261011-pcb-s2-001'
    if marker not in old:index.write_text(old+'''\n\n## v5 PCB-S2 independent workstream

| ID/source | Record | Status | Impact |
|---|---|---|---|
| S-20261011-pcb-s2-001 / Codex | [observable transcript](codex/S-20261011-pcb-s2-001.md) and [tool hashes](codex/S-20261011-pcb-s2-001.tools.json) | PARTIAL | IMPLEMENTATION_INPUT |
| Actual instructions | [S2 canonical](codex/instructions/v5_pcb_architecture_parameter_review_20261011.md) / [startup](codex/instructions/v5_pcb_task_start_20261011.md) | COMPLETE_DOCUMENT_ONLY | DESIGN_INPUT |
| T-20261011-PCB-001 | [tool flow](tool-flow/T-20261011-PCB-001__pcb-review.md) | PARTIAL | VALIDATION_INPUT |

Current observable session only through recorded cutoff. No inaccessible history, private reasoning or invented ChatGPT review. Public records redact personal paths and credentials. Canonical instruction file hashes retained.
''',encoding='utf-8')
    print('OBSERVABLE_SESSION',thread,'messages',len(messages),'tools',len(tool),'PARTIAL',h(body))
if __name__=='__main__':main()
