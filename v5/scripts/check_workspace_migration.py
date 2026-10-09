"""Check current scope and frozen Git identities without loading historical source.

Only --archive-audit reads archive file contents, for an explicitly authorized
migration/recovery audit. Normal checks/CI inspect Git index/tree metadata only.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, subprocess, sys
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[2]
V5=ROOT/'v5'

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def index():
    result={}
    for row in git('ls-files','--stage','-z').split(b'\0'):
        if row:
            meta,path=row.split(b'\t',1);mode,oid,stage=meta.split()
            if stage!=b'0':raise ValueError('Unmerged index: '+path.decode())
            result[path.decode('utf-8')]=(mode.decode(),oid.decode())
    return result

def tree(commit,prefix):
    result={}
    for row in git('ls-tree','-rz',commit,'--',prefix).split(b'\0'):
        if row:
            meta,path=row.split(b'\t',1);mode,kind,oid=meta.split()
            result[path.decode('utf-8')]=(mode.decode(),oid.decode())
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--archive-audit',action='store_true',help='Explicit authorized archive byte audit; never a default source read')
    parser.add_argument('--freeze-base',help='Reject changes to an already-existing frozen tree in this commit')
    parser.add_argument('--output')
    args=parser.parse_args();errors=[];checks={};tracked=index()
    manifest=json.loads((ROOT/'shared/migration/OLD_TRACKED_MANIFEST.json').read_text(encoding='utf-8'))
    metadata=json.loads((ROOT/'shared/migration/ARCHIVE_METADATA_HASHES.json').read_text(encoding='utf-8'))
    expected={'history_old/'+r['path']:(r['mode'],r['git_blob_sha']) for r in manifest['files']}
    expected.update({'history_old/'+name:(r['mode'],r['git_blob_sha']) for name,r in metadata['files'].items()})
    actual={k:v for k,v in tracked.items() if k.startswith('history_old/')}
    if actual!=expected:
        for key in sorted(set(actual)|set(expected)):
            if actual.get(key)!=expected.get(key):errors.append('Archive blob/mode/path mismatch: '+key)
    checks['archive']={'original_files':len(manifest['files']),'metadata_files':len(metadata['files']),'actual_files':len(actual),'raw_blob_bytes':manifest['bytes'],'content_read':bool(args.archive_audit),'mismatches':len(errors)}
    if args.freeze_base:
        if re.fullmatch('0+',args.freeze_base):raise ValueError('Supply a real freeze comparison commit')
        previous=tree(args.freeze_base,'history_old')
        if previous and previous!=actual:errors.append('Frozen history changed relative to '+args.freeze_base)
        checks['freeze_base']={'commit':args.freeze_base,'existing_tree_compared':bool(previous)}
    if args.archive_audit:
        for row in manifest['files']:
            p=ROOT/'history_old'/row['path']
            if not p.is_file() or p.is_symlink() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:
                errors.append('Archive raw SHA256 mismatch: '+row['path'])
    allowed={'.gitattributes','.gitignore','.ignore','README.md','AGENTS.md','CHANGELOG.md','shared','AI-problem','AI-chat-memory','AI-interaction-memory','v5','history_old','.github','.vscode'}
    extra=sorted({p.split('/')[0] for p in tracked}-allowed)
    if extra:errors.append('Unexpected active root entries: '+repr(extra))
    state=json.loads((ROOT/'shared/PROJECT_STATE.json').read_text(encoding='utf-8'))
    version=json.loads((ROOT/'shared/VERSION_STATE.json').read_text(encoding='utf-8'))
    if state['active_version']!='v5' or version['active_version']!='v5' or version['highest_version']!='v5' or version['upgrade_pending']:
        errors.append('Version changed during workspace migration')
    checks['identity']={'repository':state['repository'],'active_version':state['active_version'],'highest_version':version['highest_version'],'root_extras':extra}
    source_files=[]
    folders=('rtl','software','firmware','scripts','tests','tb','simulation','config')
    executable_extensions={'.py','.ps1','.tcl','.sv','.svh','.c','.h','.mjs'}
    for folder in folders:
        for p in (V5/folder).rglob('*'):
            if p.is_symlink():errors.append('Symbolic runtime input: '+str(p))
            if not p.is_file() or p.suffix not in executable_extensions:continue
            rel=p.relative_to(ROOT).as_posix();source_files.append(rel)
            if p.name=='check_workspace_migration.py':continue
            text=p.read_text(encoding='utf-8');norm=text.replace('\\','/')
            if re.search(r'(?i)[EG]:[/\\]Codex[-_]project',text):errors.append('Hard-coded project path: '+rel)
            if 'history_old/' in norm:errors.append('Historical source path in executable: '+rel)
    source_list=(V5/'config/ooc_source_list.txt').read_text(encoding='utf-8').splitlines()
    for name in source_list:
        p=(V5/name).resolve()
        if not name.startswith('rtl/') or not p.is_relative_to(V5/'rtl') or not p.is_file() or 'board/' in name:
            errors.append('Unapproved OOC source: '+name)
    checks['source_isolation']={'root':'v5','scanned_executables':len(source_files),'ooc_explicit_sources':len(source_list),'historical_sources_loaded':False,'source_list':source_list}
    for name in ['P-20261008-001__adc-40khz-bandwidth.md','P-20261009-001__ax7020-revision-ps-platform.md']:
        p=ROOT/'AI-problem/problem'/name;text=p.read_text(encoding='utf-8');front,body=text.split('---\n\n',1)
        match=re.search(r'^problem_hash:\s*([0-9a-f]{64})',front,re.M)
        if not match or hashlib.sha256(body.encode('utf-8')).hexdigest()!=match[1]:errors.append('Problem body hash mismatch: '+name)
        if not re.search(r'^active_version:\s*v5\s*$',front,re.M):errors.append('Problem version mismatch: '+name)
    checks['problems']='CURRENT_ID_HASH_VERSION_VERIFIED'
    docs=[ROOT/'README.md',ROOT/'AGENTS.md',V5/'README.md',*sorted((ROOT/'shared').rglob('*.md')),*sorted((V5/'docs').rglob('*.md')),*sorted((V5/'hardware').rglob('*.md'))]
    broken=[]
    for p in docs:
        text=re.sub(r'```.*?```','',p.read_text(encoding='utf-8'),flags=re.S)
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',text):
            target=unquote(target.strip('<>')).split('#',1)[0]
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
            if not (p.parent/target).exists():broken.append({'source':p.relative_to(ROOT).as_posix(),'target':target})
    if broken:errors.extend('Broken active doc link: '+str(x) for x in broken)
    checks['documentation']={'files':len(docs),'broken_links':broken}
    result={'status':'FAIL' if errors else 'PASS','scope':'CURRENT_WORKSPACE_INTEGRITY_NOT_BOARD_VERIFICATION','errors':errors,'checks':checks}
    if args.output:
        out=Path(args.output).resolve()
        if not out.is_relative_to(V5):raise ValueError('Evidence must stay inside this v5 clone')
        out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2));return bool(errors)

if __name__=='__main__':sys.exit(main())
