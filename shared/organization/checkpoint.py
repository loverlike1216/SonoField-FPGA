"""Generate evidence-reconciled checkpoints with explicit commit scope."""
from pathlib import Path
import argparse,json,subprocess,datetime,hashlib
from archive_after_baseline import write,dump,preservation
R=Path(__file__).resolve().parents[2];O=R/'shared/organization';V=R/'v5'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('phase',choices=['pre','final']);args=ap.parse_args()
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
    branch=subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip();assert branch=='main'
    state=json.loads((R/'shared/PROJECT_STATE.json').read_text(encoding='utf-8'))
    versions=json.loads((R/'shared/VERSION_STATE.json').read_text(encoding='utf-8'))
    baseline=json.loads((V/'evidence/baseline/before_migration_complete/summary.json').read_text(encoding='utf-8'))
    assert baseline['status']=='PASS' and baseline['python_tests']==115
    originals=preservation()
    final=args.phase=='final'
    if final:
        comp=json.loads((V/'evidence/baseline/COMPARISON.json').read_text(encoding='utf-8'));assert comp['status']=='PASS'
        assert state['active_version']==versions['active_version']=='v5'
    else:assert state['active_version']==versions['active_version']=='v2','Pre-activation checkpoint retains actual current state'
    cp='CP-20261008-002' if final else 'CP-20261008-001'
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    data={'checkpoint_id':cp,'project_id':'SONOFIELD_FPGA','project_name':'SonoField-FPGA','repository':state['repository'],
      'workspace_path':str(R),'branch':branch,'base_commit':'851d1ef747cd95da13e5eb0705b5a7885b68d83c','head_commit':head,
      'commit_scope':'Evidence-bearing source/recovery HEAD observed before this checkpoint commit; not a self-referential checkpoint commit',
      'active_version':state['active_version'],'authorized_target_version':'v5','version_status':'ACTIVE',
      'current_stage':state['current_stage'],'current_model':'GPT-6.1 Sol High','created_at':now,'created_by':'Codex',
      'checkpoint_reason':'Complete organization/standalone evidence reconciled' if final else 'v5 baseline passes before archive; pending activation from historical v2',
      'source_of_truth':'repository','status':'VALID',
      'architecture_ref':'v5/docs/architecture/SELF_CALIBRATION.md',
      'architecture':'Host solver/trajectory -> PS C/transport boundary -> AXI PL ->128 coherent 8bit phase channels with independent calibration and atomic commits ->serializer -> future qualified drivers/TX; central ADC/calibration feedback currently simulated',
      'completed':[{'item':'186 selective source/reference copies and local fixture/path isolation','status':'IMPLEMENTED'},
        {'item':'115Python tests/full waveform/calibration/motion3696frames×4 and C/AXI/safety/equivalence','status':'SIMULATED'},
        {'item':'Documented xc7z020clg400-2, native Vivado2025.2 own-source OOC project','status':'SYNTHESIZED'},
        {'item':'Historical original byte preservation','status':'TESTED','files':len(originals)}],
      'next_actions':(['Commit/push/verify current scoped delivery','Verify actual AX7020 revision/PS DDR/clock/XSA/BSP/IO before board integration'] if final else ['Commit recovery point','Archive only snapshots/indexes, preserve old paths','Repeat full baseline after archival','Activate v5 per actual user approval']),
      'active_decisions':['Explicit user v5 authorization e8213cac-ae60-4eee-bb3e-6461d16eaf66; no v4','Preserve core behavior/interfaces/acceptance; historical board decisions do not apply automatically'],
      'blockers':['AX7020_PHYSICAL_REVISION','MATCHED_PS_DDR_XSA_BSP','PRODUCTION_IO_EXTERNAL_TIMING','REAL_TRANSPORT_AND_ACOUSTICS','CHAT_MEMORY_ACCESS_BLOCKED'],
      'critical_issues':[],'latest_validation':[{'evidence':'v5/evidence/baseline/before_migration_complete/summary.json','status':'PASS'},
        {'evidence':'v5/evidence/synthesis/','status':'SYNTHESIZED','scope':'OOC; not routed board timing'}]+([{'evidence':'v5/evidence/baseline/COMPARISON.json','status':'PASS'}] if final else []),
      'known_limitations':['No physical board/PS initialization/programming/UART/GPIO/PCB test this iteration','Full-board implementation/bitstream NOT_RUN','Standalone uses same installed dependencies, not another computer','External ChatGPT BLOCKED; observable Codex transcript PARTIAL','Untracked/private originals remain local; not all local data is published'],
      'do_not_change':['Frozen original versions/byte hashes/history','Core algorithms/protocol/registers/calibration/atomic/safety/geometry/test thresholds','Do not import old Robei board constraints or historical PASS','No new version without explicit user approval','No board programming without reviewed integration facts'],
      'invariants':['128channels;PHASE_BITS8;common master phase','Separate requested+calibration mod256;atomic map switch','10mm candidate;12mm radiating-center pitch;100mm face gap adjustable90..115mm;dual8x8;origin center','Default Windows shell pwsh7','All runtime inputs local to v5; tool binaries/interpreter may be external'],
      'open_ai_problems':[],'historical_ai_problems':'AI-problem (retained original version provenance, no automatic execution)',
      'evidence_refs':['shared/organization/DIRECTORY_AUDIT.md','shared/organization/VERSION_MIGRATION_PLAN.json','v5/config/inheritance_manifest.json','shared/organization/HISTORICAL_INTEGRITY.json','v5/evidence/baseline/before_migration_complete/summary.json','v5/evidence/synthesis/loaded_sources.txt'],
      'resume_from':'Read v5/README.md and current shared state/checkpoint/plan; verify current Git then actual AX7020 platform preflight; do not scan all history',
      'repository_delta_since_previous_checkpoint':'User now explicitly authorizes AX7020 v5; no model-only change;186 copies and fresh current digital/OOC evidence, isolated old board state; prior records retain original provenance',
      'state_conflicts':[{'old':'shared activev2 and pausedv3','new':'Direct user explicitly authorizes existingv5 for AX7020','resolution':'Retain prior governance snapshot, advance only after available gates; no fabricatedv4'}],
      'provenance':['actual formal user instruction','repository source/config reviewed hashes','fresh tool outputs','original historical byte inventory','Git observed HEAD'],
      'organization_result':'ACCEPT WITH LIMITATIONS' if final else 'PENDING_AFTER_ARCHIVE_REGRESSION','whole_platform_result':'REVISE'}
    path=R/'shared/context-checkpoints'/f'{cp}__v5__{"organization" if final else "pre-archive"}.md'
    assert not path.exists(),'Never overwrite archived checkpoint'
    text=f'''---
checkpoint_id: {cp}
project_id: SONOFIELD_FPGA
active_version: {data['active_version']}
authorized_target_version: v5
branch: main
base_commit: {data['base_commit']}
head_commit: {head}
created_at: {now}
status: VALID
source_of_truth: repository
---

# Context Checkpoint

Current identity/version/stage and exact validation/commit scope are in the paired JSON. Current model GPT-6.1 Sol High (user-declared); historical models/records unchanged. This is an evidence checkpoint, not a new version/release. User explicitly authorized v5; no v4.

## Current goal and architecture

Safely establish standalone AX7020 v5 source while preserving original engineering/history. {data['architecture']}. Physical operation not verified. Core geometry and safety behavior stay fixed.

## Completed and current plan

186 copied assets; own runtime fixtures/config/source; full115 tests/3696frame4runs cross-simulator PASS; native documented-part OOC synthesis complete. {len(originals)} historical original non-cache files preserved. {'Archive snapshots/indexes completed; after/standalone exact comparisons PASS; current v5 active.' if final else 'No historical archive yet; current shared state remains v2 until post-archive verification; v5 is authorized target with tested digital baseline.'}

## Next actions

'''+ '\n'.join('- '+x for x in data['next_actions'])+'''

## Active decisions and state conflicts

Direct user authorization overrides old default-v2/no-upgrade execution restrictions. Old shared v2/v3 records are original historical facts; v5 platform transition is user-driven, not a model switch. Preserve them in Git and archived snapshots. No automatic old board decision executes on AX7020. Current blockers and acceptance remain separate from old results.

## Blockers, validation and limitations

'''+ '\n'.join('- '+x for x in data['blockers']+data['known_limitations'])+'''

## Do Not Change / Invariants

'''+ '\n'.join('- '+x for x in data['do_not_change']+data['invariants'])+f'''

## Repository delta / resume / evidence provenance

{data['repository_delta_since_previous_checkpoint']}. Open current-version AI problems:none newly created; historical problems retain their scopes. Recovery HEAD:{head}. {data['commit_scope']}.

{data['resume_from']}.

'''+ '\n'.join('- '+x for x in data['evidence_refs'])+'\n'
    write(path,text);dump(path.with_suffix('.json'),data)
    if final:
        write(R/'shared/CONTEXT_CHECKPOINT.md',text);dump(R/'shared/CONTEXT_CHECKPOINT.json',data)
        state.update(latest_context_checkpoint=cp,checkpoint_commit=head,checkpoint_status='VALID')
        dump(R/'shared/PROJECT_STATE.json',state)
    print(json.dumps({'checkpoint':cp,'phase':args.phase,'head_commit':head,'active_version':data['active_version'],'status':'VALID'}))

if __name__=='__main__':main()
