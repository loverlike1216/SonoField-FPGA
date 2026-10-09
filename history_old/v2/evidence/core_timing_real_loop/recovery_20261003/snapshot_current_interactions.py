"""Append observable model-transition-era messages, leaving old transcripts intact."""
from pathlib import Path
import importlib.util
import json
import re

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]


def main():
    spec=importlib.util.spec_from_file_location('capture',REPO/'AI-interaction-memory/tools/sync_codex.py')
    capture=importlib.util.module_from_spec(spec);spec.loader.exec_module(capture)
    source=Path.home()/'.codex/sessions/2026/09/18/rollout-2026-09-18T23-52-59-01a0b538-9430-7561-9ba4-623f57501f43.jsonl'
    meta,messages,calls,boundary=capture.extract(source,REPO)
    starts=[i for i,event in enumerate(messages) if event['role']=='user' and '【模型切换与工程连续性要求】' in event['text']]
    assert starts,'No observable transition boundary'
    visible=messages[starts[-1]:];sid='S-20261003-codex-001'
    old_path=REPO/f'AI-interaction-memory/sessions/{sid}.json'
    if old_path.exists():
        by_id={event['id']:event['sha256'] for event in visible}
        for event in json.loads(old_path.read_text())['messages']:
            assert by_id.get(event['id'])==event['sha256'],'Previously captured source changed'
    transcript=('# Observable Codex messages from the manual model transition\n\n'
                'Current Model: GPT-6.1 Sol High (user-declared manual selection)\n'
                'PROJECT_ID: SONOFIELD_FPGA\nActive Version: v2\n'
                'Current Stage: CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST\n'
                'Coverage: PARTIAL — actual visible source from transition to current cutoff; previous transcript unchanged.\n'
                f'Thread: {meta["id"]}\n\n')
    for i,event in enumerate(visible,1):
        fence='`'*max(3,1+max((len(x) for x in re.findall('`+',event['text'])),default=0))
        transcript+=(f'## Message {i:04d}\n\nRole: {event["role"]}\nTime: {event["time"]}\n'
                     f'Source ID: {event["id"]}\nSource line: {event["source_line"]}\n'
                     f'Sanitized SHA256: {event["sha256"]}\n\n{fence}text\n{event["text"]}\n{fence}\n\n')
    # Normalize before Windows output translation; preserve message-source digests.
    transcript=transcript.replace('\r\n','\n').replace('\r','\n')
    assert capture.sanitize(transcript)==transcript,'Unredacted current transcript'
    capture.write_changed(REPO/f'AI-interaction-memory/codex/{sid}.md',transcript)
    manifest={'project_id':'SONOFIELD_FPGA','current_model':'GPT-6.1 Sol High',
              'model_provenance_basis':'USER_DECLARED_MANUAL_SELECTION','session_id':sid,'thread_id':meta['id'],
              'active_version':'v2','current_stage':'CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST',
              'sync_status':'PARTIAL','source_file':source.name,'started_at':visible[0]['time'],**boundary,
              'message_count':len(visible),'messages':[{k:v for k,v in event.items() if k!='text'} for event in visible],
              'files':{f'codex/{sid}.md':capture.file_digest(transcript)}}
    capture.write_changed(old_path,json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'status':'PARTIAL','message_count':len(visible),'existing_historical_transcript_modified':False}))


if __name__=='__main__':main()
