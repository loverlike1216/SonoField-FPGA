"""User-authorized low-risk archival. Requires real PASS and a recovery commit first."""
from pathlib import Path
import json, hashlib, shutil, subprocess, zipfile, datetime
R=Path(__file__).resolve().parents[2]
O=R/'shared/organization'
V=R/'v5'

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def write(p,s):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s,encoding='utf-8',newline='\n')

def dump(p,obj):write(p,json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def preservation():
    m=json.loads((O/'local_raw/preservation_hashes_before.json').read_text(encoding='utf-8'))
    errors=[n for n,e in m.items() if not (R/n).is_file() or sha(R/n)!=e['sha256_bytes']]
    report={'status':'FAIL' if errors else 'PASS','files_checked':len(m),'errors':errors,
        'scope':'Exact original bytes for inventoried non-cache historical files, including untracked/private originals',
        'cache_policy':'Retained in place; not exhaustively hashed','old_sources_modified':False if not errors else 'REVIEW_REQUIRED'}
    dump(O/'HISTORICAL_INTEGRITY.json',report)
    if errors:raise RuntimeError('Historical preservation conflict: '+repr(errors[:10]))
    return m

if __name__=='__main__':
    b=json.loads((V/'evidence/baseline/before_migration_complete/summary.json').read_text(encoding='utf-8'))
    assert b['status']=='PASS' and b['python_tests']==115 and b['frame_count']==3696
    recovery=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
    tracked=subprocess.check_output(['git','ls-tree','--name-only',recovery,'v5','shared/organization'],cwd=R,text=True)
    assert 'v5' in tracked and 'shared/organization' in tracked,'Commit validated v5 recovery point before archive'
    if (R/'archive/manifests/MIGRATION_MANIFEST.json').exists():raise RuntimeError('Refuse overwriting archive event')
    originals=preservation()
    # Save untracked original assets privately; never publish private originals by blanket staging.
    backup=O/'local_raw/untracked_originals_before_archive.zip'
    assert not backup.exists()
    with zipfile.ZipFile(backup,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=3) as z:
        for name,entry in originals.items():
            if not entry['git_tracked']:z.write(R/name,arcname=name)
    with zipfile.ZipFile(backup) as z:
        assert z.testzip() is None
        for name in z.namelist():assert hashlib.sha256(z.read(name)).hexdigest()==originals[name]['sha256_bytes']
    dump(O/'UNTRACKED_BACKUP_RECEIPT.json',{'status':'PASS','files':sum(not x['git_tracked'] for x in originals.values()),
        'sha256_zip':sha(backup),'local_only':'shared/organization/local_raw/untracked_originals_before_archive.zip',
        'not_published_reason':'Preserve user/private/untracked originals without exposing them to public GitHub',
        'restore':'Extract chosen member into a separate review folder and compare inventory; never overwrite current files blindly'})
    a=R/'archive';manifest=[]
    snap=O/'local_raw/pre_v5_governance'
    for src in sorted(snap.rglob('*')):
        if not src.is_file():continue
        rel=src.relative_to(snap);dst=a/'historical_evidence/pre_v5_20261008'/rel
        dst.parent.mkdir(parents=True,exist_ok=True);assert not dst.exists();shutil.copy2(src,dst)
        assert sha(src)==sha(dst)
        manifest.append({'operation':'COPY_SNAPSHOT','original_path':rel.as_posix(),
            'target_path':dst.relative_to(R).as_posix(),'sha256_bytes':sha(src),
            'reason':'Preserve pre-v5 governance before current state updates',
            'restore':'Read this snapshot or git show recovery/base commit; restore only after review'})
    groups={
      'legacy_versions':['v1','v2','v3'],
      'legacy_board':['Zynq7020','parameter_detection'],
      'legacy_pcb':['PCB','BOM'],
      'historical_evidence':['evidence'],
      'deprecated_designs':[]}
    audit=json.loads((O/'DIRECTORY_AUDIT.json').read_text(encoding='utf-8'))
    entries={x['original_path']:x for x in audit['entries']}
    for group,names in groups.items():
        text='# '+group+' — frozen index\n\nOriginal files are kept in place. This index is excluded from normal v5 builds/search.\n\n'
        for name in names:
            info=entries[name]
            text+=f"- [{name}](../../{name}/): {info['purpose']}. Historical references: {info['reference_count']}. Reason retained: {info['risk']}.\n"
            manifest.append({'operation':'INDEX_KEEP_IN_PLACE','original_path':name,'target_path':name,
                'index':f'archive/{group}/README.md','sha256_manifest':'shared/organization/HISTORICAL_HASHES_BEFORE.json',
                'reason':'Existing historical source/reproduction links; no risky relocation needed',
                'restore':'No restore necessary: original path/bytes unchanged; Git history and private backup retained'})
        if not names:text+='No candidate design was moved or deleted. Paused drafts remain historical and are not active inputs.\n'
        if group=='legacy_versions':text+='\nv1 frozen; v2 retained/frozen by current explicit v5 approval; v3 paused incomplete/untracked, not falsely promoted into validated history. No v4 exists.\n'
        write(a/group/'README.md',text)
    write(a/'README.md','''# SonoField-FPGA historical archive

Frozen by default. Do not scan or load in normal v5 development. Authorized historical comparison, regression, provenance conflicts or restoration may read only the needed entry.

This is an indexed archive with byte-identical prior governance snapshots. Referenced v1/v2/v3/PCB/BOM/old-board/evidence trees remain at their original locations to preserve reproduction. No source tree was moved or deleted; archive is not a second active source.

Indexes: legacy_versions, legacy_board, legacy_pcb, historical_evidence, deprecated_designs. Complete operation/hash/recovery information: manifests/MIGRATION_MANIFEST.json and .md. Private originals stay local and are not implied to be on GitHub.
''')
    write(a/'AGENTS.md','''# Frozen historical scope

Read-only by default. No ordinary edits, builds, broad search or hardware assumptions here. Only explicitly authorized historical recovery/comparison or a concrete regression/decision-provenance need may consult a targeted entry. Current project source is ../v5 and current state ../shared. Historical model names, decisions, tests and file bytes must retain original provenance.
''')
    result={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'recovery_commit':recovery,
        'baseline':'v5/evidence/baseline/before_migration_complete/summary.json','baseline_status':b['status'],
        'moves':0,'deletions':0,'governance_snapshot_files':sum(x['operation']=='COPY_SNAPSHOT' for x in manifest),
        'operations':manifest,'local_private_backup_receipt':'shared/organization/UNTRACKED_BACKUP_RECEIPT.json'}
    dump(a/'manifests/MIGRATION_MANIFEST.json',result)
    text=f"# Migration manifest\n\nRecovery commit: `{recovery}`. Baseline PASS before archival. Moves0/deletions0.\n\n| Operation | Original | Destination / retained path | Hash / inventory | Reason / recovery |\n|---|---|---|---|---|\n"
    for x in manifest:text+=f"| {x['operation']} | {x['original_path']} | {x['target_path']} | {x.get('sha256_bytes',x.get('sha256_manifest'))} | {x['reason']}; {x['restore']} |\n"
    write(a/'manifests/MIGRATION_MANIFEST.md',text)
    preservation()
    print(json.dumps({'status':'PASS','recovery_commit':recovery,'snapshot_files':result['governance_snapshot_files'],
        'untracked_backed_up':sum(not x['git_tracked'] for x in originals.values()),'preserved_files':len(originals),'moves':0,'deletions':0}))
