"""Reconcile current v5 state after real before/after/standalone gates pass."""
from pathlib import Path
import json,datetime,subprocess,hashlib,shutil
from archive_after_baseline import preservation,write,dump
R=Path(__file__).resolve().parents[2];V=R/'v5';O=R/'shared/organization'

if __name__=='__main__':
    names=['before_migration_complete','after_migration','standalone']
    results={n:json.loads((V/'evidence/baseline'/n/'summary.json').read_text(encoding='utf-8')) for n in names}
    for n,b in results.items():
        assert b['status']=='PASS' and b['python_tests']==115 and b['frame_count']==3696,(n,b.get('error'))
        assert b['determinism']['runs']==4 and b['determinism']['status']=='PASS'
    before=results[names[0]]
    native=(V/'evidence/synthesis/project_reopen.log').read_text(encoding='utf-8')
    assert 'V5_NATIVE_PROJECT_REOPEN_PASS source_files=18 internal_period_ns=7.576' in native
    assert 'No legacy candidate MMCM exists in the synthesized design.' in native
    assert all(b['source_sha256']==before['source_sha256'] for b in results.values()),'Source delta during organization'
    assert all(b['determinism']['hashes']==before['determinism']['hashes'] for b in results.values()),'Behavior delta'
    fixed=[];calibration_records=[];provenance=[]
    for n in names:
        rr=V/'evidence/baseline'/n/'motion/regression'
        wave=json.loads((rr/'summary.json').read_text(encoding='utf-8'))
        cal=json.loads((rr/'self_calibration/summary.json').read_text(encoding='utf-8'))
        assert wave['status']==cal['status']=='PASS'
        record=json.loads((rr/'self_calibration/calibration.json').read_text(encoding='utf-8'))
        calibration_records.append(record)
        provenance.append({'baseline':n,'git_commit':record['git_commit'],
            'calibration_raw_artifact_sha256':cal['repeated_artifacts'][0]['calibration.json']})
        fixed.append({'waveform_TB15':wave['TB15']['hashes'],
            'ADC_roundtrip_sha256':[a['sha256'] for a in cal['adc_roundtrips']],
            'calibration_repeated_numerical_artifacts':[{k:v for k,v in a.items() if k!='calibration.json'} for a in cal['repeated_artifacts']],
            'calibration_all_fields_except_git_commit_sha256':hashlib.sha256(json.dumps(
                {k:v for k,v in record.items() if k!='git_commit'},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()})
    assert all(x==fixed[0] for x in fixed),'Waveform/ADC/calibration fixed-input delta'
    archive_record=json.loads((R/'archive/manifests/MIGRATION_MANIFEST.json').read_text(encoding='utf-8'))
    expected_commits=['851d1ef747cd95da13e5eb0705b5a7885b68d83c',archive_record['recovery_commit'],'851d1ef747cd95da13e5eb0705b5a7885b68d83c']
    assert [p['git_commit'] for p in provenance]==expected_commits,'Unexpected calibration provenance'
    for record in calibration_records[1:]:
        assert set(record)==set(calibration_records[0])
        assert all(record[k]==calibration_records[0][k] for k in record if k!='git_commit'),'Additional calibration field difference'
    dump(V/'evidence/baseline/CALIBRATION_PROVENANCE_DIFF.json',{'status':'EXPECTED_METADATA_DIFFERENCE',
        'changed_fields_only':['git_commit'],'raw_records_preserved':True,'records':provenance,
        'all_other_fields_exactly_equal':True,'comparison_rule':'Only the independently verified recovery Git provenance may differ; no numerical or arbitrary metadata normalization'})
    preserved=preservation()
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
    base='851d1ef747cd95da13e5eb0705b5a7885b68d83c'
    archive=json.loads((R/'archive/manifests/MIGRATION_MANIFEST.json').read_text(encoding='utf-8'))
    prior=json.loads((O/'local_raw/pre_v5_governance/shared/PROJECT_STATE.json').read_text(encoding='utf-8'))
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    stage='AX7020_V5_SAFE_ORGANIZATION_AND_STANDALONE_BASELINE'
    comparison={'status':'PASS','active_version':'v5','source_hashes_identical':True,'fixed_input_behavior_hashes_identical':True,
      'python_tests_each':115,'frames_each':3696,'simulator_runs_each':4,'baseline_names':names,
      'historical_files_preserved':len(preserved),'history_moves':0,'history_deletions':0,
      'hardware_verified':False,'full_board_timing':'NOT_RUN','classification':'ORGANIZATION_AND_DIGITAL_BASELINE_ONLY',
      'recovery_commit':archive['recovery_commit'],'checked_at':now}
    comparison['independent_fixed_inputs']=fixed[0]
    comparison['calibration_raw_json']='DIFFERENT_ONLY_EXPECTED_GIT_COMMIT; see CALIBRATION_PROVENANCE_DIFF.json'
    dump(V/'evidence/baseline/COMPARISON.json',comparison)
    write(V/'evidence/BASELINE_VALIDATION.md',f'''# AX7020 v5 baseline validation — 2026-10-08

Current model: GPT-6.1 Sol High (user-declared). Scope: directory integrity, independent digital/software operation and documented-part OOC synthesis; not whole-platform acceptance.

| Actual gate | BEFORE_MIGRATION | AFTER_MIGRATION | Standalone without old versions/shared |
|---|---|---|---|
| Full orchestrator | PASS | PASS | PASS |
| Python unit tests | 115/115 | 115/115 | 115/115 |
| GUI-driven motion | 3696 frames ×4 | 3696 frames ×4 | 3696 frames ×4 |
| Fixed input hashes | 3 Icarus +1 XSim identical | Identical to before | Identical to before |
| Waveform/Python oracle, calibration/raw ADC, safety/regression | PASS | PASS | PASS |
| C service/protocol, AXI bridge/system/smoke PL simulation | PASS | PASS | PASS |
| Queue/scheduler golden comparison, serializer throughput, safe array interface | PASS in both tools | PASS in both tools | PASS in both tools |
| Phase/burst exact-cycle equivalence | PASS in both tools | PASS in both tools | PASS in both tools |
| Source and inherited-copy hash integrity | PASS | Identical | Identical |

Summaries/logs: baseline/before_migration_complete, baseline/after_migration, baseline/standalone; canonical COMPARISON.json. Calibration raw JSON hashes differ only in git_commit(base vs recovery commit); CALIBRATION_PROVENANCE_DIFF.json preserves actual raw hashes/commits, checks those exact expected commits and exact equality of every other field. Numerical calibration/LUT/quality/ADC/waveform results remain identical; raw JSON byte identity is not claimed across different provenance commits. The standalone workspace contains only a v5 copy, no v1/v2/v3/shared/archive at its parent. It uses the declared external Python interpreter and tool binaries; this proves source/data path independence, not a fresh dependency installation or another computer.

Earlier failures preserved: before_migration missing motion_gate.py; before_migration_repaired missing an implicit synthetic calibration input (72 tests ran, FAIL). Dependency RCA is shared/organization/DEPENDENCY_RCA.md. Repaired by explicit copies/local input paths, never dropping assertions/tests. No previous failed result overwritten.

Native Vivado2025.2: scripts/create_project.tcl executed successfully for the manufacturer-documented xc7z020clg400-2, top sono_axi_system; own RTL source list in synthesis/loaded_sources.txt. OOC synthesis:7219 LUT,17918 registers,4 RAMB36; synthesized internal timing WNS+0.994ns/WHS+0.157ns at inherited132MHz target. These are pre-route values. Report also has2324 no-input-delay and256 no-output-delay warnings for OOC boundary ports; they are not waived or represented as constrained physical IO. Native project reopen proof is synthesis/project_reopen.log.

Full-board placement/routing, reviewed AX7020 production XDC/PS preset, bitstream, UART/PS-PL runtime and acoustic hardware: NOT_RUN/NOT_VERIFIED. Missing revision-matched integration inputs make a board implementation inapplicable here. No false paths, guessed IO or removed constraints used to fabricate a Timing PASS. Native build logs/report evidence remain separate from simulation results.

Historical integrity: {len(preserved)} inventoried non-cache original files retain exact byte hashes, including untracked/private originals; caches/dependencies remain in place and are not claimed fully audited. Recovery commit: {archive['recovery_commit']}. Archive snapshot count:{archive['governance_snapshot_files']}; source moves0/deletions0.

Available digital/organization gates PASS; physical acceptance remains blocked. External ChatGPT review/history access BLOCKED, observable Codex capture PARTIAL. No independent AI review invented.
''')
    versions={'active_version':'v5','highest_version':'v5','status':'ACTIVE','version_status':'ACTIVE',
      'upgrade_pending':False,'pending_target':None,'version_directory':'v5','frozen_versions':['v1','v2'],
      'paused_versions':['v3'],'legacy_versions':[],'absent_versions':['v4'],
      'approval_source':'User actual attachment e8213cac-ae60-4eee-bb3e-6461d16eaf66, explicit existing v5 AX7020 development authorization',
      'v3_baseline':'INCOMPLETE_USER_PAUSED_UNTRACKED_LOCAL_HISTORY','updated_at':now}
    dump(R/'shared/VERSION_STATE.json',versions)
    blockers=[
      {'id':'V5-B01','issue':'Physical AX7020 board/revision/order code/VCCO and documented-pin match not verified','status':'OPEN'},
      {'id':'V5-B03','issue':'Revision-matched PS DDR/clock/preset, XSA/BSP and real host transport/PS-PL runtime absent','status':'OPEN'},
      {'id':'V5-B04','issue':'Production IO/XDC/external timing, actual serializer/driver/ADC/safety qualification not completed','status':'OPEN'},
      {'id':'V5-B05','issue':'10mm emitter batch, RX phase reference, physical trap and measured particle milestones not tested','status':'OPEN'},
      {'id':'CHAT_MEMORY_ACCESS_BLOCKED','issue':'No supported tool to read external ChatGPT SonoField-FPGA history/review','status':'OPEN'}]
    state={'project_id':'SONOFIELD_FPGA','project_name':'SonoField-FPGA','repository':'https://github.com/loverlike1216/SonoField-FPGA.git',
      'workspace_path':str(R),'branch':'main','current_branch':'main','active_version':'v5','current_version':'v5',
      'version_status':'ACTIVE','current_stage':stage,'status':'PROJECT_ACTIVE','execution':'PROJECT_ACTIVE',
      'current_model':'GPT-6.1 Sol High','model_provenance_basis':'USER_DECLARED_MANUAL_SELECTION',
      'chat_source_name':'SonoField-FPGA','chat_access_status':'CHAT_MEMORY_ACCESS_BLOCKED','chat_sync_status':'BLOCKED',
      'open_ai_problems':[],'historical_problem_index':'AI-problem/','problem_revalidation':'No historical board-specific decision automatically executed on AX7020',
      'blocking_issues':[b['id'] for b in blockers],'critical_issues':[],
      'organization_blockers':[],'organization_result':'ACCEPT WITH LIMITATIONS','whole_platform_result':'REVISE',
      'digital_validation':'PASS','digital_evidence':'v5/evidence/BASELINE_VALIDATION.md',
      'reproducibility':'PASS_OLD_WORKTREE_INDEPENDENCE_SAME_INSTALLED_DEPENDENCIES','hardware_verified':False,
      'board':'ALINX AX7020','board_facts':'v5/config/board_facts.json','physical_part':None,
      'documented_ooc_part':'xc7z020clg400-2','board_synthesis':'SYNTHESIZED_DOCUMENTED_PART_OOC',
      'implementation':'NOT_RUN_FULL_BOARD_CONSTRAINTS_AND_PS_PLATFORM_UNVERIFIED',
      'source_inheritance_commit':base,'validated_parent_core_commit':'9936a737c45bf61f1908863a94f6374c6b5c828c',
      'pre_archive_recovery_commit':archive['recovery_commit'],'geometry':prior['geometry'],
      'bom':'v5/hardware/bom/BOM_MASTER.xlsx','bom_status':'INHERITED_PROPOSED_NOT_AX7020_ELECTRICAL_RELEASE',
      'interaction_memory_index':'AI-interaction-memory/INDEX.md','interaction_memory_status':'PARTIAL',
      'codex_thread_id':prior.get('codex_thread_id','UNKNOWN'),
      'verified_previous_workspaces':prior.get('verified_previous_workspaces',[]),
      'latest_context_checkpoint':'shared/CONTEXT_CHECKPOINT.md','checkpoint_status':'VALID',
      'next_action':'Verify actual AX7020 revision and official matching PS/DDR/clock/IO platform; define board integration contract before implementation or programming',
      'updated_at':now}
    dump(R/'shared/PROJECT_STATE.json',state)
    write(R/'shared/PROJECT_STATE.md',f'''# Current SonoField-FPGA state

PROJECT_ID SONOFIELD_FPGA · main · active v5 · ALINX AX7020. Stage:{stage}. Model:GPT-6.1 Sol High (user-declared).

Current available digital baseline PASS in three environments/runs: before archival, after archival, old-worktree-free copy. Real OOC synthesis completed; full-board timing/PS/physical tests NOT_RUN. Organization ACCEPT WITH LIMITATIONS; whole platform REVISE. Details in PROJECT_STATE.json and v5/evidence/BASELINE_VALIDATION.md.

v1/v2 preserved frozen; v3 paused historical local draft; v4 absent. Current source and build use v5 only. archive is frozen index/snapshot scope. External ChatGPT history BLOCKED, Codex observable capture PARTIAL. Next: actual AX7020 revision/PS platform/IO qualification. No board-specific v2 evidence becomes AX7020 proof.
''')
    write(R/'shared/CURRENT_PLAN.md','''# Current plan — AX7020 v5

1. DONE read-only directory/state/Git audit and explicit user authorization reconciliation.
2. DONE copy186 reviewed reusable assets; isolate all runtime sources/configs/fixtures in v5.
3. DONE full115-test digital baseline, two simulators, C/AXI, native OOC synthesis before archival.
4. DONE recoverable Git point, original byte inventories, private untracked backup; low-risk governance snapshot archive and indexes, originals kept in place.
5. DONE repeat full baseline after archival and in standalone v5-only workspace; exact source/behavior hashes match,3343 original non-cache files preserved.
6. CURRENT reconcile checkpoint/observable AI records; normal commit/push and remote verification at delivery.
7. NEXT verify actual AX7020 revision/device/VCCO/clock and matching official PS/DDR/preset/XSA/BSP, allocate reviewed IO/transport and integration contract. No bitstream or unknown GPIO allowed before qualification.

Do Not Change: stable core/protocol/registers/calibration separation/atomic update/safety/geometry/test criteria; frozen histories; no new version without explicit approval; do not import Robei board configurations or historical PASS. Stop if new facts require core architectural change. Default read scope v5/shared/current valid decisions only.
''')
    # Keep prior acceptance/blocker/decision text with original provenance; append the current scoped gate.
    for name,title,body in [
      ('DECISIONS.md','ADR-035 — VERSION_UPGRADE_APPROVED: AX7020 v5',
       'Decision Type: VERSION_UPGRADE_APPROVED. From:v2 active /v3 paused local history; To:v5. Approved By:User. Source:actual attachment e8213cac-ae60-4eee-bb3e-6461d16eaf66, archived in AI-interaction-memory/codex/instructions/ax7020_v5_safe_organization.md. Explicit user authority supersedes previous no-upgrade/default-v2 execution restrictions. No v4 fabricated. Selective copy, no source redesign; v1/v2 preserved frozen, v3 stays paused. Official documented AX7020 part/clock/DDR are candidate physical-board facts, not old Robei inheritance. Keep referenced history in place; archive indexes/snapshots only. Real evidence: v5/evidence/BASELINE_VALIDATION.md. External ChatGPT decision/review not claimed. Current recording model GPT-6.1 Sol High.'),
      ('ACCEPTANCE.md','Current AX7020 v5 organization gate — 2026-10-08',
       'The preceding criteria/results retain historical version scope. New user-authorized scope: safe organization and available AX7020 v5 baseline, without lowering inherited algorithm/protocol tests. Required:115 Python tests/full motion4runs3696frames/waveform+calibration/C+AXI/safety+equivalence pass before and after archival; isolated v5-only run and exact source/behavior hashes; native documented-part OOC synthesis/reopen; historical hashes and recoverable commit; state/search scope and Git sync. Evidence: v5/evidence/BASELINE_VALIDATION.md and baseline/COMPARISON.json. Available gates PASS. Independent tool cross-check Icarus+XSim, no external AI review fabricated. Physical PS/IO/UART/route/levitation NOT_VERIFIED; full-project ACCEPT forbidden. Organization ACCEPT WITH LIMITATIONS; whole platform REVISE.'),
      ('BLOCKERS.md','Current AX7020 v5 blockers — 2026-10-08',
       'Prior B01/B03 etc above retain Robei/v2 historical scope; they are not reopened or closed as AX7020 facts. Current blockers:\n\n'+'\n'.join('- '+b['id']+': '+b['issue'] for b in blockers)+'\n\nNo organization/source-path blocker remains after real gates. These blockers prevent physical/full-platform acceptance, not continuation of current digital development. No board access/programming was performed this iteration.')]:
        p=R/'shared'/name;old=p.read_text(encoding='utf-8');write(p,old+'\n\n## '+title+'\n\n'+body+'\n')
    log='\n\n## 2026-10-08 — authorized AX7020 v5 safe organization\n\nCopied186 reviewed source/reference assets; isolated paths and explicit synthetic fixtures; full115 tests and dual-simulator digital gates pass before/after and standalone. Native documented-part OOC synthesis completed. Original3343 non-cache files unchanged; prior governance snapshots/indexes archived, no source move/deletion. v5 is active, v1/v2 frozen, v3 paused, v4 absent. Physical integration NOT_VERIFIED. Current model GPT-6.1 Sol High.\n'
    for p in [R/'CHANGELOG.md',R/'shared/CHANGELOG.md']:
        write(p,(p.read_text(encoding='utf-8') if p.exists() else '# Changelog\n')+log)
    dump(R/'shared/versions/v2_freeze_20261008.json',{'version':'v2','status':'FROZEN','user_authorized_target':'v5','created_at':now,
      'base_commit':base,'validated_core_commit':'9936a737c45bf61f1908863a94f6374c6b5c828c',
      'files':{n:e for n,e in preserved.items() if n.startswith('v2/')},
      'scope':'No historical source mutated; cache excluded; v2 physical limitations retained in archived governance snapshots'})
    write(R/'README.md','''# SonoField-FPGA

PROJECT_ID **SONOFIELD_FPGA** · active **v5** · **ALINX AX7020 / Zynq-7020** · Vivado2025.2 · main. Same repository and history; v5 was explicitly authorized by the user on2026-10-08. No v4 was created.

Start here: [v5开发入口](v5/README.md) · [完整运行指南](指南.md) · [当前状态](shared/PROJECT_STATE.json) · [恢复检查点](shared/CONTEXT_CHECKPOINT.md) · [真实基线结果](v5/evidence/BASELINE_VALIDATION.md).

128-channel40kHz acoustic field with8bit programmable phase, separate per-channel calibration, atomic maps, acquisition/calibration, trajectory and PS/PL protocol infrastructure. Geometry: opposed8×8+8×8,10mm candidate emitters,12mm radiating-center pitch, nominal100mm face-to-face gap adjustable90–115mm, origin at geometric center. 50mg EPS remains a staged final physical target, not a demonstrated result.

Current available digital gates pass; native documented-part OOC synthesis is complete. Actual AX7020 revision, production IO/PS platform, full board timing, host-board runtime and physical levitation remain unverified. Organization result ACCEPT WITH LIMITATIONS; whole platform REVISE.

Root shared/ and AI records hold cross-version governance/provenance; v5/ is the sole active implementation; archive/ is frozen indexed history. v1/v2 and referenced old hardware/PCB/evidence remain at original locations to preserve history, excluded from default v5 builds/search. Paused v3 is incomplete local history and is not claimed published/validated; no v4 exists. Original private/local assets and generated caches are intentionally not mirrored to public GitHub.

Audit/reuse/archive manifests: shared/organization/ and archive/manifests/. External ChatGPT source SonoField-FPGA is BLOCKED; observable Codex transcript PARTIAL, never invented history. All future Windows commands default to PowerShell7.
''')
    write(R/'AGENTS.md','''# SonoField-FPGA current engineering scope

PROJECT_ID SONOFIELD_FPGA. Repository https://github.com/loverlike1216/SonoField-FPGA.git. Active version v5, target ALINX AX7020, authoritative Vivado2025.2. Current model record GPT-6.1 Sol High (user-declared). Explicit user attachment e8213cac-ae60-4eee-bb3e-6461d16eaf66 authorizes v5 and supersedes prior active-v2 restrictions. No v4. Historical model records must retain provenance.

## Recovery and default search

Read README, shared/PROJECT_STATE.*, VERSION_STATE.json, CONTEXT_CHECKPOINT.*, CURRENT_PLAN, current DECISIONS/BLOCKERS/ACCEPTANCE and current v5 evidence before changes. Default implementation/search/build scope: v5/, shared/, root README/AGENTS, current valid AI-problem decision and necessary current AI-interaction records. Do not routinely scan archive/, v1/, v2/, v3/, old large logs or full historical chats. Targeted historical access only when user requests, regression/comparison, decision provenance, restoration or evidence conflict requires it. archive is frozen by default; originals kept in place are equally historical read-only.

## Invariants and boundaries

All new implementation belongs in v5. Preserve stable names/interfaces,128channels/8bit/common timebase/requested-calibration separation/atomic commit/safety/protocol/registers/motion cadence. Geometry is10mm candidate emitters,12mm radiating-face-center pitch, nominal100mm face gap configurable90–115mm, opposed8×8, geometric-center origin. Preserve algorithm behavior and inherited acceptance; no skipped tests/relaxed thresholds/fake results. v1/v2 frozen, v3 paused local draft; do not edit them or invent v4. Continue never implies another version. New versions need explicit user approval and copy-based migration.

v5 must load its own RTL/config/fixtures/XDC. Generic old source may be inherited only by reviewed copy and recorded hash; never silently read old worktrees. Do not carry Robei pins, N18 clock, COM4, FTDI IDs or512MiB candidates into AX7020 physical facts. Official reference differs from actual revision verification. Current132MHz is an internal design target. Only OOC clock constraint exists; physical deployment blocked until actual part/revision/VCCO/PS DDR/clock/preset/XSA/BSP/IO/external timing are verified. This organization task permits no program download, unknown GPIO, driver/boot/reset changes or PCB editing.

## Execution, evidence and persistence

Use pwsh7 on Windows, not powershell.exe5.1 except explicit necessity. Use real tool output; distinguish implementation/test/simulation/synthesis/routed timing/hardware. Full digital baseline entry v5/scripts/run_baseline.ps1;115 Python tests and four3696-frame GUI/RTL runs plus existing waveform/calibration/C/AXI/safety gates must pass. No previous PASS becomes current physical verification. Keep failed evidence.

No force push,history rewrite,blanket clean,reset--hard or unreviewed deletion/move. Preserve untracked user assets; stage only reviewed changes. Public GitHub requires secret/privacy scan; local_raw,private docs,caches/builds and untracked paused drafts are not published blindly. Explicit current source/provenance changes use normal commits/push and remote verification.

Persist observable user/Codex messages and key tool flows in AI-interaction-memory with source IDs/hashes/PARTIAL limits; never hidden reasoning. External ChatGPT history is BLOCKED unless a real reader/export is available; do not fabricate ChatGPT decisions/review. Major decisions use AI-problem with source/hash/version checks, ordinary implementation defects are handled directly. No subagents requested for this task. After meaningful changes reconcile current state/plan/blockers/decisions/acceptance and create CONTEXT_CHECKPOINT with real evidence and commits. Current scoped organization acceptance does not accept the hardware platform.
''')
    write(R/'指南.md','''# SonoField-FPGA v5 接续开发指南

从GitHub克隆完整项目后，首先阅读v5/README.md、shared/PROJECT_STATE.json、shared/VERSION_STATE.json、shared/CONTEXT_CHECKPOINT.md及CURRENT_PLAN。当前唯一开发版本v5，平台ALINX AX7020，Vivado2025.2；没有v4。源码位于v5，不要从旧v2启动当前任务。

## 运行环境与命令

Windows使用PowerShell7（pwsh）。安装Python3.10（含Tk）、Vivado2025.2及Zynq7000器件、Icarus Verilog和GCC。依赖锁位于v5/requirements-lock.txt；串口可选依赖v5/requirements-board.txt不代表当前已具备实板协议。

```powershell
git clone https://github.com/loverlike1216/SonoField-FPGA.git
Set-Location SonoField-FPGA
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r v5/requirements-lock.txt
$env:VIVADO_BIN='D:/Vivado/2025.2/2025.2/Vivado/bin' # 修改成本机路径
$env:IVERILOG_BIN='C:/iverilog/bin'
$env:CC='D:/DevC++/Dev-Cpp/TDM-GCC-64/bin/gcc.exe'
./v5/scripts/run_baseline.ps1 -Output evidence/baseline/colleague_run
```

输出路径相对v5自动定位，不依赖克隆盘符；可以-Python指定其他环境。请使用新的证据目录，不覆盖已有summary.json。成功标准：总PASS，115测试、3696帧×4、Icarus三次/XSim一次固定输入Hash相同，波形/校准/ADC/C协议/AXI/安全及等价检查全部通过。完整版会打开并自动关闭Tk演示窗口；Icarus完整运动回放耗时较长，应查看日志而非把UI出现当作成功。默认子进程有超时，保留失败日志并调查，不要使用skip参数降低验收。

从v5运行离线综合：`& "$env:VIVADO_BIN/vivado.bat" -mode batch -source scripts/create_project.tcl -tclargs config/ax7020_ooc.tcl`。加载build/vivado/sonofield_v5.xpr查看工程；当前报告在evidence/synthesis。OOC只证明文档器件上的内部设计综合，不可直接下载。综合前须保留报告，重新运行将生成本机新输出。

## 各目录与故障排查

rtl/tb/tests/software/firmware是当前实现和测试；simulation/fixtures是明确合成输入；config/inheritance_manifest.json记录186复制文件的来源/适配Hash；config/board_facts.json区分文档参数和实际板卡事实；hardware/ax7020/sources.json记录官方资料URL/Commit/Hash；hardware/bom未获生产释放。evidence/BASELINE_VALIDATION.md及baseline/COMPARISON.json是本轮结果入口。

若工具找不到，核对三项环境变量和可执行文件；若Tk缺失，修复桌面Python环境；若继承Hash失败，检查本地修改与记录后重新审核，不能删检查；若输出已存在，换新目录保留旧结果。不要补入v2路径来解决输入缺失；显式夹具路径已本地化。跨机器/新虚拟环境回归需真实运行后才能宣称该机器通过。本轮独立性验证复用本机已安装解释器/依赖，并非另一台电脑验证。

## 下一阶段与禁止边界

先核验实际AX7020修订版、完整器件、VCCO、时钟、PS DDR拓扑及厂家匹配preset/XSA/BSP，完成IO/串口/网络选择和外部时序/安全合同，再进入PS-PL单板集成。没有生产XDC和可下载bitstream；当前任务未访问板卡、下载或操作外部PCB。10mm换能器批次及真实场/质量分级仍需实验，不保证50mg悬浮。

历史v1/v2/PCB/原始资料保留原位，archive是冻结分类索引与旧管理文件快照，默认不参与构建。用户本机私有原始资料、生成物、未跟踪v3草稿不会因git clone自动出现；以archive清单和本地备份回执为准。恢复某项历史文件请逐项核对Hash并在单独目录审阅，不要覆盖当前v5。

AI交互记录仅保存可观察内容，外部ChatGPT聊天读取BLOCKED；所有新记录标注GPT-6.1 Sol High，旧模型历史不改写。继续开发保持v5，阶段变化不自动升版本。当前目录整理ACCEPT WITH LIMITATIONS，整个平台仍REVISE。
''')
    write(R/'shared/HANDOFF.md',f'''# AX7020 v5 organization handoff

Goal: standalone current source with recoverable history. Inputs: direct user authorization, base{base}, validated parent core, official ALINX documents, real installed tools. Changes:186 copies/local fixtures/board gates,current v5 scripts/docs; frozen governance snapshots/index archive, no original moves/deletions. Tests: full115 and two-tool regression three complete baseline runs; native OOC synthesis/reopen. Evidence:v5/evidence/BASELINE_VALIDATION.md,baseline/COMPARISON.json,shared/organization/HISTORICAL_INTEGRITY.json. Failures: two omitted dependency attempts retained then repaired without relaxing tests. Unresolved: AX7020 actual revision/PS platform/production IO/timing/real transport/acoustics; external ChatGPT inaccessible. Next: current checkpoint and normal remote sync, then board-integration preflight contract. Current model GPT-6.1 Sol High. Recovery:{archive['recovery_commit']}.
''')
    print(json.dumps(comparison,indent=2))
