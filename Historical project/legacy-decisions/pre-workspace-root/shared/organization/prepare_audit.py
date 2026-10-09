"""Read-only directory audit and preservation hashes; never moves engineering files."""
from pathlib import Path
import hashlib, json, subprocess, os, re

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'shared/organization'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    tracked=set(filter(None,git('ls-files','-z').decode('utf-8').split('\0')))
    head=git('rev-parse','HEAD').decode().strip()
    rows=[]; hashes={}; refs={}
    needles=['Zynq7020','PCB/','BOM/','parameter_detection','v1/','v2/','v3/','build/','evidence/']
    for n in tracked:
        p=ROOT/n
        if p.suffix.lower() in {'.py','.ps1','.tcl','.json','.md','.yml','.yaml','.toml','.sv','.svh'} and p.is_file() and p.stat().st_size<200000:
            t=p.read_text(encoding='utf-8',errors='replace').replace('\\','/')
            for needle in needles:
                if needle in t:refs.setdefault(needle,[]).append(n)
    purposes={
      '.git':('A','Repository history','KEEP','Unmodified'),'.venv':('A','Existing pinned Python dependencies','KEEP','Required until v5 environment verified'),
      '.Xil':('E','Vivado runtime/cache','KEEP_IGNORED','May belong to live process; no cleanup'),
      'build':('E','Root generated tool products','KEEP_IGNORED','Need reference/process inspection; no blind removal'),
      'AI-chat-memory':('A','External ChatGPT source and access limits','KEEP','Do not fabricate history'),
      'AI-interaction-memory':('A','Observable AI/tool provenance','KEEP','Preserve historical payloads'),
      'AI-problem':('A','Original problems and decisions','KEEP','Old version provenance retained; no automatic v5 execution'),
      'shared':('A','Current state and historical recovery metadata','KEEP_UPDATE_CURRENT_ONLY','Prior state snapshot saved before activation'),
      'v1':('C','Frozen original engineering','KEEP_IN_PLACE','Moving breaks historical paths; no relocation'),
      'v2':('C','Latest validated digital source and Robei evidence','KEEP_IN_PLACE_COPY_SELECTED','Preserve bytes/history and old reproduction paths'),
      'v3':('C','User-paused incomplete historical draft','KEEP_IN_PLACE','Untracked files registered; not promoted to v5 baseline'),
      'v5':('A','User-created AX7020 active development destination','POPULATE_BY_COPY','Initially empty; never overwrite user files'),
      'PCB':('D','Historical native schematic, libraries and untracked backup','KEEP_IN_PLACE_COPY_REFERENCE','Old paths used in reports/scripts; no high-risk move'),
      'BOM':('D','User originals, canonical v2 import exists','KEEP_IN_PLACE','Referenced historical source; manufacturer/user assets'),
      'Zynq7020':('D','Old Robei original board documents','KEEP_IN_PLACE','Old scripts reference root; historical reproduction retained'),
      'parameter_detection':('D','Prior real DDR/JTAG evidence and private raw data','KEEP_IN_PLACE','Historical result links and private originals; never v5 hardware facts'),
      'evidence':('C','Historical root verification/handoff evidence','KEEP_IN_PLACE','Cross-document references; do not move entire tree'),
      'dfx_runtime.txt':('E','Untracked Vivado runtime file','KEEP_IGNORED','Inspect live processes; preserve user/runtime bytes')}
    for p in sorted(ROOT.iterdir(),key=lambda p:p.name.lower()):
        if p.name=='.git': entries=[]
        elif p.is_dir() and p.name not in ('.venv','.Xil','build'):
            entries=[x for x in p.rglob('*') if x.is_file() and not any(k in x.relative_to(p).parts for k in ('__pycache__','build','.Xil','xsim.dir','.cache'))]
        else:entries=[p] if p.is_file() else []
        names=[x.relative_to(ROOT).as_posix() for x in entries]
        default=('A','Root governance/entry file','KEEP_UPDATE_CURRENT_ONLY','Preserve prior contents through Git/snapshot')
        cl,purpose,action,risk=purposes.get(p.name,('E','Vivado runtime trace','KEEP_IGNORED','No active process/cache deletion') if p.suffix=='.str' else default)
        referenced=refs.get(p.name+'/',refs.get(p.name,[]))
        rows.append({'original_path':p.name,'classification':cl,'purpose':purpose,'tracked_files':sum(n in tracked for n in names),
          'enumerated_non_cache_files':len(entries),'reference_count':len(referenced),'reference_examples':referenced[:6],
          'historical_evidence':cl=='C' or p.name in ('parameter_detection','PCB','Zynq7020'),
          'recommendation':action,'risk':risk,'target_path':p.name,
          'scope':'Caches and dependency internals intentionally not recursively audited' if p.name in ('.git','.venv','.Xil','build') else 'File inventory excluding generated subtrees'})
        if p.name in ('v1','v2','v3','PCB','BOM','Zynq7020','parameter_detection','evidence'):
            for x,n in zip(entries,names):hashes[n]={'sha256_bytes':sha(x),'size_bytes':x.stat().st_size,'git_tracked':n in tracked}
    private=OUT/'local_raw';private.mkdir(exist_ok=True)
    put(private/'preservation_hashes_before.json',hashes)
    # Full project-relative hash registry contains no file contents, credentials or photo metadata.
    put(OUT/'HISTORICAL_HASHES_BEFORE.json',{n:v for n,v in hashes.items() if '/local_raw/' not in n})
    put(OUT/'DIRECTORY_AUDIT.json',{'project_id':'SONOFIELD_FPGA','date_local':'2026-10-08','source_commit':head,
        'branch':git('branch','--show-current').decode().strip(),'initial_git_status':git('status','--short').decode('utf-8'),
        'v5_initial_file_count':sum(x.is_file() for x in (ROOT/'v5').rglob('*')),'entries':rows,
        'missing_expected_aliases':{'parameter-detection':'Actual directory is parameter_detection; no automatic rename'},'references':refs})
    lines=['# Directory audit — 2026-10-08','',f'PROJECT_ID SONOFIELD_FPGA; main; source `{head}`. User authorizes existing empty v5 for AX7020. No engineering file moved/deleted/renamed during this audit.',
        '', 'A=current management/dependencies; B=selected reusable v2 files (separate VERSION_MIGRATION_PLAN); C=formal history; D=historical reference; E=rebuildable/runtime candidates. Classification alone never authorizes deletion.',
        '', '| Original path | Class / purpose | Git tracked / inventoried | References | Historical evidence | Action / target | Risk |','|---|---|---|---|---|---|---|']
    for row in rows:
        lines.append('| '+ ' | '.join([row['original_path'],row['classification']+' / '+row['purpose'],str(row['tracked_files'])+' / '+str(row['enumerated_non_cache_files']),str(row['reference_count']),str(row['historical_evidence']),row['recommendation']+' / '+row['target_path'],row['risk']])+' |')
    lines+=['','## Preservation and current facts','',
      'Per-file byte hashes: HISTORICAL_HASHES_BEFORE.json. Private raw paths additionally covered by local_raw/preservation_hashes_before.json, not published. Cache and .venv internals are retained in place, not claimed exhaustively inspected.',
      'Historical versions/root PCB/Zynq7020/parameter_detection/evidence have cross-path references. They stay in place, read-only for normal v5 development; moving them is unnecessary and would risk reproduction. No high-risk movement is proposed in this iteration.',
      'v4 does not exist and will not be fabricated. v3 is untracked paused history, not a validated source. Latest validated functional source is v2 at9936a737c45bf61f1908863a94f6374c6b5c828c, with subsequent detection/docs commits through startingHEAD. No old PASS is inherited as v5 PASS.',
      'Low-risk archival scope after v5 baseline: copy prior root management snapshots and categorized historical indexes into archive; do not relocate referenced native engineering. Runtime/cache files stay ignored; live Vivado is not terminated.',
      'External ChatGPT history capability remains BLOCKED; current source observable Codex record will be PARTIAL. No independent review invented.']
    (OUT/'DIRECTORY_AUDIT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'status':'AUDIT_WRITTEN_NO_ENGINEERING_MOVES','root_entries':len(rows),'preserved_files':len(hashes),'v5_initial_file_count':sum(x.is_file() for x in (ROOT/'v5').rglob('*')),'source_commit':head}))
