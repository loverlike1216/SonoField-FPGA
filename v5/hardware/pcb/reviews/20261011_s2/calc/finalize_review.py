"""Reconcile this candidate worktree; preserve originals and publishable receipts.
No historical source-body access; explicit current paths only.
"""
from pathlib import Path
import datetime,hashlib,json,os,re,shutil,subprocess,sys
sys.stdout.reconfigure(encoding='utf-8')
R=Path(__file__).resolve().parent.parent;V5=R.parents[3];ROOT=V5.parent;E=V5/'evidence/pcb_s2_20261011'
BASE='8c27b5841b5494c3761ab211881a3ea2be63e8c8'
def sha(data):return hashlib.sha256(data).hexdigest()
def save(p,j):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def textfile(p,t):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t.rstrip()+'\n',encoding='utf-8')
def git(*args,cwd=ROOT):return subprocess.check_output(['git',*args],cwd=cwd)
def append_once(p,marker,t):
    old=p.read_text(encoding='utf-8')
    if marker not in old:textfile(p,old+'\n\n'+t)
def main():
    assert ROOT==Path('E:/Codex_project/AMD_Sonofield_PCB_v5')
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    # Undo only our documented EOL preparation, verifying exact pre-action SHA.
    prepared=json.loads((E/'BASELINE_EOL_PREPARATION.json').read_text(encoding='utf-8'));restored=[]
    for x in prepared['files']:
        rel=x['path'];assert not rel.startswith(('Historical project/','history_old/'))
        p=ROOT/rel;raw=p.read_bytes()
        if sha(raw)==x['before']:continue
        assert sha(raw)==x['after'],f'Unexpected later modification: {rel}'
        lf=raw.replace(b'\r\n',b'\n')
        candidate=next((b for b in [lf,lf.replace(b'\n',b'\r\n')] if sha(b)==x['before']),None)
        assert candidate is not None,rel
        p.write_bytes(candidate);restored.append(dict(path=rel,sha256=sha(candidate)))
    save(E/'EOL_RESTORE_RECEIPT.json',dict(status='PASS',restored=restored,scope='only documented current-worktree preparation; original workspace unchanged'))
    # Public summaries/logs; full raw replay files remain locally, ignored.
    selected={
      'digital_full/summary.json':'nextstage.json',
      'digital_full/full/summary.json':'prepcb.json',
      'digital_full/full/system/summary.json':'system.json',
      'digital_full/full/inherited_full/motion/summary.json':'motion.json',
      'digital_full/full/inherited_full/motion/regression/summary.json':'3696_regression.json',
      'digital_full/adc/summary.json':'adc_c16.json',
      'digital_full/capture_c16/summary.json':'capture_c16.json',
      'digital_full/top_c16/summary.json':'top_c16.json',
      'digital_full/software/summary.json':'software.json',
      'BASELINE_UNIT.log':'unit243.txt',
      'DIGITAL_RUN.log':'digital_runner.txt'}
    copied=[]
    for src,dst in selected.items():
        p=E/src
        if not p.exists():copied.append(dict(source=src,status='MISSING_NOT_CLAIMED'));continue
        dest=E/'published_baseline'/dst;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(p.read_bytes())
        copied.append(dict(source=src,published=str(dest.relative_to(E)),sha256=sha(p.read_bytes()),bytes=p.stat().st_size))
    digital=json.loads((E/'digital_full/summary.json').read_text(encoding='utf-8'))
    assert digital['status']=='PASS'
    assert 'Ran 243 tests' in (E/'BASELINE_UNIT.log').read_text(encoding='utf-8')
    # Reconcile primary repository without writing there.
    original=Path('E:/Codex_project/AMD_Sonofield')
    origin_status=git('status','--porcelain=v1',cwd=original).decode('utf-8')
    assert origin_status.strip()=='?? BOM/',repr(origin_status)
    origin_head=git('rev-parse','HEAD',cwd=original).decode().strip();assert origin_head==BASE
    assert not (ROOT/'Historical project').exists()
    for s in ['v5/rtl','v5/scripts','v5/tests','v5/config','v5/ps','v5/constraints']:
        assert subprocess.run(['git','diff','--quiet','HEAD','--',s],cwd=ROOT).returncode==0,s
    # Preserve all current-stage output hashes, not generated binary data in Git.
    outputs=[]
    for p in sorted((E/'digital_full').rglob('*')):
        if p.is_file():outputs.append(dict(path=str(p.relative_to(E)).replace('\\','/'),bytes=p.stat().st_size,sha256=sha(p.read_bytes())))
    save(E/'DIGITAL_OUTPUT_HASHES.json',dict(classification='OFFLINE_RAW_LOCAL_NOT_HARDWARE',files=outputs))
    # The problem body hash policy matches current project convention.
    body='''# PCB safety and electrical decisions required

## Decision Needed / Goal
Approve a concrete next-stage design direction that retains v5/AX7020/128TX8RX/C16/12V single-ended/geometry/protocol, implements default-off independent protection and enables honest passive specifications. TPS3851H33EDRBR x2 direction is already user-approved, but functional safety closure is not.

## Current State / Repository Facts
PCB worktree feat/v5-pcb-design based on Draft PR5 head 8c27b5841b5494c3761ab211881a3ea2be63e8c8; original workspace and unmerged main unchanged. Current prepcb_supervisor.sv line29 toggles heartbeat from timer tick independent of state progress. Existing SCHEMATIC_STATUS and ADR042 require independent window watchdog. New TPS3851 is a timeout watchdog; WDO pulses, RESET assertion makes WDO high-Z, below POR outputs undefined. No native schematic/ERC or qualified cutoff latch/FET network exists.

## Evidence
TPS3851 RevB pp5-7,17,23; TPS2663 RevG pp7,18,30; INA226 RevC p5; manufacturer URLs and hashes in v5/hardware/pcb/reviews/20261011_s2 and v5/evidence/pcb_s2_20261011. Current 243 tests and full3696x3Icarus+1XSim/nextstage digital baseline PASS. These prove only their offline scope. Workbook independently counted1205; approved supervisor-only replacement arithmetic1203. Old1.65k is invalid for TPS26631, 20mOhm*5A=100mV exceeds INA22681.92mV; C0/motional load/AFE/VCCO/externalSTA unknown.

## What Codex Tried / New Information
Read actual fixed-commit hardware files for four requested projects plus supplementary HV583 schematic; read primary datasheets, inspect current heartbeat RTL, independently parse workbook, calculate energy/LC/timing/threshold/range corners, cross-check numerical time-domain models. Preserved first fetch/extraction failures. Did not change RTL, lower35dB, invent loads, open archive bodies, operate board or release manufacturing.

## Root Cause Hypotheses
Old BOM contains functions and quantities before actual circuit design. Part-family substitutions do not preserve window/kill behavior. Free-running heartbeat checks clock presence, not useful control progress. Multi-domain fail-off and power/range coordination are unspecified at component level.

## Candidate Options
A (recommended for next-stage review): retain approved TPS3851x2; add independent too-early/window detector, progress-qualified heartbeat, cold-start-off fault latch/manual rearm and physically biased back-to-back cutoff/discharge. Extra device count is TBD until a concrete circuit is reviewed. Preserve required safety criteria.
B: request a different integrated window supervisor and re-review exact replacement; changes explicit approved part, requires user approval. Still needs physical cutoff/latch/discharge.
C: accept timer heartbeat, omit window and connect WDO directly to power enable. Rejected by current evidence and invariants; cannot justify release.
Power A: keep12V single-ended TC4427 with damping footprints; retain60W capacity candidate/40W controlled-current alternative, measure real load and coordinate ILIM/TVS/jack/shunt/SOA. Power B: bridge/differential is comparison only, requires separate architecture authorization.

## Constraints / Acceptance Impact
No v6/core/protocol/geometry change or main merge; no board/image/DDR/Flash/ultrasound operations.35dB and all243original tests/goldens unchanged. S2-C remains BLOCKED and BOM/HW/ERC/manufacturing HOLD while P0s open.

## Questions For User / Main Chat
1. Accept A as the next-stage circuit design scope, including independently qualified window/latch/cutoff and extra components, or request revised integrated supervisor?
2. What allowed heartbeat/startup/stop-to-safe timing applies; may the next-stage task implement progress tokens instead of timer heartbeat while preserving current protocol?
3. Accept measurement-first12V single-ended/60W-capacity direction and revised protection/shunt coordination, plus central5V regulation/CC budget review before freezing RCL?
4. Supply qualified TX/RX/load/VCCO/cable facts and an independent electrical review of the concrete candidate before native schematic/BOM release.

## User Approval Boundary
Existing approval authorizes this review, independent worktree and TPS3851x2 direction only. It does not approve newly proposed safety circuitry/RTL edits, a reduced safety contract, bridge drive, manufacturing, purchasing or hardware writes. External ChatGPT access BLOCKED; no fabricated external Decision. A real new decision must match this ID/body hash/v5.
'''
    ph=sha(body.encode('utf-8'));problem=ROOT/'AI-problem/problem/P-20261011-001__pcb-safety-and-electrical-gates.md'
    front=f'''---
problem_id: P-20261011-001
project_id: SONOFIELD_FPGA
active_version: v5
current_stage: PCB_S2_REVIEW
status: OPEN
created_at: {now}
created_by: Codex
chat_source_name: SonoField-FPGA
problem_hash: {ph}
hash_scope: UTF8 LF body after closing frontmatter plus blank line
---

'''
    textfile(problem,front+body)
    decision=ROOT/'AI-problem/decision/P-20261011-001__pcb-supervisor-user-direction.md'
    textfile(decision,f'''---
problem_id: P-20261011-001
project_id: SONOFIELD_FPGA
active_version: v5
current_stage: PCB_S2_REVIEW
status: PARTIAL_APPROVED_BY_USER_REMAINING_OPEN
decision_source: User
chat_source_name: SonoField-FPGA
chat_message_id: UNKNOWN
chat_message_time: UNKNOWN
problem_hash: {ph}
decision_sync_time: {now}
---

# Actual user direction, not independent safety approval

Actual reply: “按文件执行，并批准上述工作树路径”。Canonical instruction: AI-interaction-memory/codex/instructions/v5_pcb_architecture_parameter_review_20261011.md, section0. It directs TPS3851H33EDRBR x2 system total, one each array, replacing old B008/B009 physical placeholders, with functional gaps retained and separate P0 modules proposed when necessary.

## Chosen Direction / Execution Boundary
Create approved worktree E:\\Codex_project\\AMD_Sonofield_PCB_v5 from PR5 head8c27b58 on feat/v5-pcb-design; execute PCB-S2 offline review and normal Draft publication. Candidate old monitor rows installed0, newTPS3851x2. Do not infer that this chip selection implements window detection,12V protection or independent physical kill.

## Decision Status / Validation
Chip/worktree/review direction APPROVED_BY_USER and implemented. Problem remains OPEN for new options and electrical safety acceptance. No manufactured ChatGPT output, external review or broader user approval. Verify this ID/bodyhash/version before any future decision execution.
''')
    append_once(ROOT/'AI-problem/INDEX.md','P-20261011-001',f'| P-20261011-001 | [PCB safety/electrical](problem/{problem.name}) / [actual user direction](decision/{decision.name}) | TPSx2 direction approved; new safety/engineering decisions OPEN | {ph} |')
    append_once(ROOT/'shared/DECISIONS.md','ADR-043',f'''## ADR-043 — Actual user PCB-S2 / TPS3851 combined supervisor direction

2026-10-11, v5, source actual user reply and canonical S2 instruction. Worktree/branch/base authorized as recorded above. B008/B009 physical4->TPS3851H33EDRBR2 total, not2perboard. Native/electrical/safety acceptance remains HOLD. Existing window requirement is not withdrawn; new gaps P-20261011-001 OPEN, body SHA256 {ph}. No external ChatGPT decision. Extra protection/heartbeat architecture is a proposal, not approved by this record.
''')
    stage='V5_PCB_S2_REVIEW_DELIVERED_ELECTRICAL_HOLD'
    statep=ROOT/'shared/PROJECT_STATE.json';state=json.loads(statep.read_text(encoding='utf-8'))
    state['parent_workstream']=dict(branch=state.get('branch'),workspace_path=state.get('workspace_path'),stage=state.get('current_stage'),checkpoint=state.get('latest_context_checkpoint'),head=BASE)
    state.update(workspace_path=str(ROOT),branch='feat/v5-pcb-design',current_branch='feat/v5-pcb-design',current_stage=stage,
      latest_context_checkpoint='CP-20261011-002',checkpoint_commit=None,checkpoint_commit_resolution='git log -1 --format=%H -- shared/CONTEXT_CHECKPOINT.json',
      pcb_review='v5/hardware/pcb/reviews/20261011_s2/10_EXECUTIVE_SUMMARY.md',pcb_review_result='REVISE',pcb_passives='S2_C_BLOCKED',
      pcb_candidate_bom='v5/hardware/pcb/reviews/20261011_s2/BOM_INPUTS_S2_CANDIDATE.json',pcb_candidate_installed_arithmetic=1203,
      digital_evidence='v5/evidence/pcb_s2_20261011/FINAL_VERIFICATION.json',digital_validation='FRESH243+FULL3696x4+NEXTSTAGE_PASS',
      next_action='Independent review and actual safety/electrical decisions in P-20261011-001 before S2-C/native schematic/BOM release',updated_at=now)
    state['open_ai_problems']=list(dict.fromkeys(state['open_ai_problems']+['P-20261011-001']))
    state['blocking_issues']=list(dict.fromkeys(state['blocking_issues']+['S2-P01','S2-P02','S2-P03','S2-P04','S2-P05']))
    save(statep,state)
    versionp=ROOT/'shared/VERSION_STATE.json';ver=json.loads(versionp.read_text(encoding='utf-8'));ver.update(current_stage=stage,updated_at=now);save(versionp,ver)
    pcbstate=dict(project_id='SONOFIELD_FPGA',repository=state['repository'],workspace=str(ROOT),branch='feat/v5-pcb-design',
      base_commit=BASE,dependency_pr=5,active_version='v5',current_stage=stage,S2_A='DELIVERED',S2_B='REVISE',S2_C='BLOCKED',
      native_schematic='NOT_CREATED',ERC='NOT_RUN',manufacturing='HOLD',BOM='HOLD',problem_id='P-20261011-001',problem_hash=ph)
    save(V5/'hardware/pcb/PCB_PROJECT_STATE.json',pcbstate)
    textfile(V5/'hardware/pcb/PCB_PROJECT_STATE.md','# PCB workstream state\n\n'+json.dumps(pcbstate,ensure_ascii=False,indent=2)+'\n\nRead reviews/20261011_s2/10_EXECUTIVE_SUMMARY.md then the open problem. Preserve v5 and main HOLD.')
    append_once(ROOT/'shared/CURRENT_PLAN.md','PCB-S2 candidate workstream',f'''## PCB-S2 candidate workstream (current on feat/v5-pcb-design)

S2-A evidence/reconciliation DELIVERED. S2-B power/driver/safety proposal REVISE. S2-C fullRCL freeze BLOCKED. Fresh243/full digital gates PASS. Retain parent hardware stage above as provenance; no main promotion. Next: main-chat independent review of P-20261011-001; approve concrete safety/progress/regulation scope and supply electrical facts; then native circuit review, S2-C and future BOM candidate. See CP-20261011-002 and v5/hardware/pcb/PCB_PROJECT_STATE.json.
''')
    append_once(ROOT/'shared/BLOCKERS.md','PCB-S2 P0 additions','''## PCB-S2 P0 additions

S2-P01 window/progress coverage; S2-P02 cold-start/失电/锁存/physical cutoff/discharge; S2-P03 actual load and eFuse/TVS/source/jack/shunt coordination; S2-P04 centralAVCC/RX/AFE; S2-P05 fullIO/VCCO/externalSTA/BRAM. See v5/hardware/pcb/reviews/20261011_s2/08_RISK_BLOCKERS_AND_DECISION_REQUESTS.md. S2-C/BOM/manufacturing HOLD. These are current candidate facts, not main-merged implementation.
''')
    append_once(ROOT/'shared/ACCEPTANCE.md','PCB-S2 review boundary','''## PCB-S2 review boundary

Review artifact/calculation/baseline checks PASS in their stated scope. Circuit decision REVISE; S2-C BLOCKED; native schematic NOT_CREATED/ERC NOT_RUN/hardware NOT_VERIFIED. Neither1203arithmetic nor offline digitalPASS releases BOM/manufacturing. No acceptance threshold,35dB/test/golden/protocol was changed. External review remains required.
''')
    append_once(ROOT/'CHANGELOG.md','PCB-S2 architecture review','''## 2026-10-11 — v5 PCB-S2 architecture review

Independent approved worktree from Draft5; fixed-commit public hardware/primary-source review, reproducible power/timing/AFE calculations, independent101type workbook audit, explicit TPS3851x2 candidate and full860passive inventory. Fresh243/fullnextstage digitalPASS. ElectricalREVISE/S2-CBLOCKED; no core/hardware/manufacturing/main changes. CP-20261011-002 and P-20261011-001 retain unresolved decisions.
''')
    cp=dict(checkpoint_id='CP-20261011-002',project_id='SONOFIELD_FPGA',project_name='SonoField-FPGA',repository=state['repository'],
      workspace_path=str(ROOT),branch='feat/v5-pcb-design',base_commit=BASE,head_commit=None,head_commit_resolution='git log -1 --format=%H -- shared/CONTEXT_CHECKPOINT.json',
      active_version='v5',version_status='ACTIVE',current_stage=stage,created_at=now,created_by='Codex',checkpoint_reason='PCB-S2 read/review/calculation milestone and fresh digital baseline; electrical P0 hold',
      source_of_truth='repository',status='VALID_CANDIDATE_WITH_LIMITATIONS',architecture_ref='v5/hardware/pcb/reviews/20261011_s2/02_THREE_BOARD_ARCHITECTURE_REVIEW.md',
      completed=['IMPLEMENTED review/calculation/BOMcandidate/provenance files','TESTED243 original tests; review30 separate checks','SIMULATED full3696x3Icarus+1XSim and nextstage offlinePASS','NOT_VERIFIED hardware/electrical; no new synthesis'],
      next_actions=['Publish normal Draft stacked on PR5 and verify remote','Obtain real decisions to P-20261011-001','Resolve protection/load/AVCC/AFE/IO gates before S2-C/native/BOMrelease'],
      active_decisions=['ADC user direction retained','ADR042 four-power retained','ADR043 userTPS3851x2 and independentworktree direction'],
      blockers=['S2-P01','S2-P02','S2-P03','S2-P04','S2-P05'],critical_issues=state['critical_issues'],
      latest_validation=['v5/evidence/pcb_s2_20261011/FINAL_VERIFICATION.json'],known_limitations=['No original schematic/ERC','Unknown physical load/VCCO/AFE','ExternalChatGPTBLOCKED','S2-CBLOCKED'],
      do_not_change=['Frozen archive bodies','Original workspace dirty/untrackedBOM','Core RTL/PSPL/productionXDC/goldens/thresholds','v5/version/geometry/protocol; main remainsHOLD'],
      invariants=['128TX8RX','32lanesx4used','8bitrequested/calibrationseparate','commonclock/atomicmaps/signedcaptureACK','35dB','50Hz','12mmpitch/100mmgap90-115/centerorigin'],
      open_ai_problems=state['open_ai_problems'],evidence_refs=['v5/evidence/pcb_s2_20261011','v5/hardware/pcb/reviews/20261011_s2'],
      resume_from='README/AGENTS->shared state->this checkpoint->10_EXECUTIVE_SUMMARY->P-20261011-001; remainv5; do not blindly execute candidate safety options',
      state_conflicts=['Parent documents retain former monitor placeholders as provenance; S2 candidate supersedes physical counts only','Old window requirement remains; TPS3851selection does not close it','PCB worktree is candidate stacked on Draft5, not main'])
    save(ROOT/'shared/CONTEXT_CHECKPOINT.json',cp)
    md='---\n'+''.join(f'{k}: {cp[k]}\n' for k in ['checkpoint_id','project_id','repository','branch','base_commit','head_commit','active_version','version_status','current_stage','created_at','created_by','checkpoint_reason','source_of_truth','status'])+'---\n\n# PCB-S2 Context Checkpoint\n\n'
    for title,key in [('Current Identity','workspace_path'),('Current Goal / Architecture','architecture_ref'),('Completed','completed'),('Current Plan / Next Actions','next_actions'),('Active Decisions','active_decisions'),('Blockers','blockers'),('Latest Validation','latest_validation'),('Known Limitations','known_limitations'),('Do Not Change','do_not_change'),('Invariants','invariants'),('Open AI Problems','open_ai_problems'),('State Conflicts / Delta','state_conflicts'),('Resume Instruction','resume_from'),('Evidence References','evidence_refs')]:
        value=cp[key];md+=f'## {title}\n\n'+ ('\n'.join('- '+x for x in value) if isinstance(value,list) else str(value))+'\n\n'
    md+='## Provenance\n\nActual approved instructions, baseline8c27b58 current contracts/RTL/workbook, fixed-source manifest, fresh243/fulloffline gates, review calculations and source facts; all current repository paths. HEAD resolves from containing checkpoint commit, not self-referential guessed hash. No old archive body/ChatGPT history inferred.\n'
    textfile(ROOT/'shared/CONTEXT_CHECKPOINT.md',md)
    archive=ROOT/'shared/context-checkpoints/CP-20261011-002__v5__pcb-s2-review.md'
    assert not archive.exists(),'Do not overwrite historical checkpoint';textfile(archive,md)
    final=dict(project_id='SONOFIELD_FPGA',active_version='v5',base_commit=BASE,recorded_at=now,
      artifact_review='REVISE_ELECTRICAL_S2_C_BLOCKED',unit_tests=dict(status='PASS',count=243,evidence='published_baseline/unit243.txt'),
      digital=dict(status='PASS',scope='FULL3696x3Icarus+1XSim_C16_CAPTURE_TOP_SOFTWARE_OFFLINE',summaries=copied),
      review_checks=json.loads((E/'REVIEW_VERIFICATION.json').read_text(encoding='utf-8'))['status'],
      workbook=json.loads((E/'BOM_RECOUNT.json').read_text(encoding='utf-8')),original_workspace=dict(head=origin_head,status=origin_status.strip(),tracked_unchanged=True),
      protected_core_unchanged=True,historical_body_read=False,original_sandbox_modified=False,
      native_schematic='NOT_CREATED',ERC='NOT_RUN',DRC='NOT_RUN',board_operations='NONE',hardware='NOT_VERIFIED',manufacturing='HOLD',
      problem_id='P-20261011-001',problem_hash=ph,source_input_sha256=sha((ROOT/'AI-interaction-memory/codex/instructions/v5_pcb_architecture_parameter_review_20261011.md').read_bytes()))
    save(E/'FINAL_VERIFICATION.json',final)
    print('FINAL_RECONCILIATION PASS; electrical REVISE; checkpoint CP-20261011-002; problem body',ph)
if __name__=='__main__':main()
