"""Reconcile observed stage evidence, without changing Acceptance or physical facts."""
from datetime import datetime,timezone
import hashlib
import html
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
OUT=ROOT/'evidence/pre_pcb_board_ready'
STAGE='TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE'
MODEL='GPT-6.1 Sol High'

def load(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def save(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def write(path,text):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')

def main():
    gate=load(OUT/'regression_release/summary.json')
    independent=load(OUT/'independent_checks_complete/summary.json')
    timing=load(OUT/'timing/core_timing_pass.json')
    axi=load(OUT/'axi_offline_release/axi_bridge_tests.json')
    assert all(d['status']=='PASS' for d in [gate,independent,timing,axi]),'Do not finalize a failed/missing gate'
    assert gate['regression']=='PASS' and gate['frame_count']==3696
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()
    summary={'project_id':'SONOFIELD_FPGA','project_name':'SonoField-FPGA','active_version':'v2','branch':'main',
       'current_stage':STAGE,'current_model':MODEL,'model_provenance':'USER_DECLARED_MANUAL_SELECTION',
       'starting_head':'bd9e79f622ee58ea970870071702eb24596cd753','reconciled_head':head,
       'exact_part':'xc7z020clg400-1','physical_order_code':'XC7Z020-1CLG400C',
       'part_provenance':'USER_CONFIRMED_PHYSICAL_FACT','board_jtag':'HARDWARE_VERIFIED_IDENTITY_ONLY',
       'idcode':'0x23727093','arm_dap_idcode':'0x4BA00477','ftdi_reported_variant':'FT2232H',
       'usb_descriptor':'VID0403/PID6010/REV0700','uart':'COM4_ENUMERATED_ROUTE_NOT_VERIFIED',
       'ethernet':'HOST_REALTEK_DISCONNECTED; BOARD_ROUTE_NOT_VERIFIED',
       'documented_input_clock_hz':33333000,'input_clock_pin':'N18',
       'input_clock_provenance':'USER_APPROVED_DOCUMENT_FALLBACK_NOT_MEASURED',
       'core_timing':timing,'serializer_acceptance_cycles':11,'maximum_phase_update_hz':10624000,
       'minimum_core_hz':116864000,'core_design_target_hz':132000000,
       'fallback_mmcm_core_hz':131998680,'final_board_clock':'NOT_FROZEN_PENDING_PLATFORM_INTEGRATION',
       'digital_regression':'PASS','python_tests':115,'motion_frames_per_run':3696,'motion_runs':4,
       'determinism':gate['determinism'],'independent_queue_scheduler_array_checks':'PASS_ICARUS_AND_XSIM',
       'offline_axi_protocol':'PASS','ps_target_elf':'NOT_BUILT_MISSING_VERIFIED_XSA_BSP_AND_ARM_TOOLCHAIN',
       'real_ping_pong_1000':'NOT_RUN','real_axi_readback':'NOT_RUN','real_phase_map_ack':'NOT_RUN',
       'gui_real_board_transport':'NOT_RUN','native_gui_evidence':'SIMULATION_ONLY',
       'array_adapter':'IMPLEMENTED_DUAL_SIMULATOR_TESTED_NOT_BOARD_INTEGRATED',
       'j3_j4_j5_j6':'CANDIDATE_DOCUMENT_AND_PACKAGE_VERIFIED_NOT_ELECTRICALLY_FROZEN',
       'vcco':'UNKNOWN_BANK34_BANK35','iostandard':'UNASSIGNED','external_timing':'NOT_QUALIFIED',
       'drc_warnings':{'REQP-1839':'RAMB36 async control;20 reported,report limit reached',
                       'ZPS7-1':'PS7 absent in OOC block','CHECK-3':'Rule limit reached'},
       'methodology_warnings':['LUTAR-1','SYNTH-6','TIMING-18'],
       'timing_margin_risk':'WNS+0.082ns is small; new board clock/reset/IO integration requires renewed implementation',
       'pre_pcb_board_ready':'NO','overall_result':'REVISE',
       'blocking':['B03_VCCO_AND_CONTINUITY','PS_UART_MIO_ROUTE','PS_REFERENCE_CLOCK_RESET_PRESET',
          'VERIFIED_PS_PLATFORM_AND_TARGET_BUILD','REAL_TRANSPORT_AND_MAP_COMPLETION',
          'BOARD_WRAPPER_ARRAY_DISABLE_INTEGRATION','EXTERNAL_IO_TIMING_AND_HARDWARE_QUALIFICATION'],
       'not_validated':['bitstream','PS execution','1000 real packets','external PCB/ADC/TCT40 operation','physical levitation'],
       'safety':{'programmed':False,'serial_opened':False,'drivers_changed':False,'boot_changed':False,
          'gpio_driven':False,'pcb_modified':False,'external_loads_operated':False},
       'evidence_refs':['timing/strategy3/routed/timing_summary.rpt','timing/strategy3/route_status.rpt',
          'regression_release/summary.json','independent_checks_complete/summary.json','axi_offline_release/axi_bridge_tests.json',
          'board_identity/jtag_identity.json','board_identity/windows_inventory.json','connector_reference/connector_audit.json'],
       'created_at':datetime.now(timezone.utc).isoformat()}
    save(OUT/'summary.json',summary)
    report=f'''# SonoField-FPGA v2 — current pre-PCB result

PROJECT_ID: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
workspace_path: {REPO}
branch: main
active_version: v2
stage: {STAGE}
current_model: {MODEL} (user-declared; exact runtime variant not exposed)
starting_HEAD: {summary['starting_head']}
ending_HEAD: see repository `git rev-parse HEAD` and delivery_sync.json; later checkpoint commits follow validated source

## Implemented / tested

New personalized rules reviewed before work. Current-version/decision/evidence continuity preserved. Complete part user-confirmed. Bounded queue pointer/channel/timer/watchdog/occupancy and balanced17-bit selection, plus a measured scheduler CE repair, preserve observable cycle behavior. Original/new comparisons cover depths2/4/5 and64,096scheduler cycles, successful captures, rejected commands and faults. The inherited serializer is restored unchanged; the first strict-guard failure remains archived.

115Python tests; complete inherited waveform/calibration/ADC regression;3696-frame motion demonstration in three Icarus runs and one Vivado XSim run; exact map/trajectory/trap/ACK hashes; current-source offline AXI/host-C protocol checks PASS. Separate upper/lower array-disable adapter is implemented and tested in both simulators, with shared clocks and fresh-frame release; it is not integrated into a physical wrapper.

## Real tool evidence

Vivado2025.2 strategy3 fully routed21,475nets,zero routing errors. Internal132MHz OOC WNS+0.082ns,TNS0,WHS+0.072ns,THS0; internal unconstrained endpoints0 and no_clock0. Both normal synchronous and asynchronous recovery/removal paths remain analyzed; no false/multicycle exceptions were added. Strategy2 remains archived with WNS-0.284ns and84failed setup endpoints. Strategy1 was interrupted after measured prolonged congestion; it has no final post-route result.

Current serializer accepted100consecutive starts spaced11cycles in each simulator. Minimum core frequency at41.5kHz×256 is116.864MHz;132MHz meets digital throughput. N18/33.333MHz is the latest approved document fallback. A vendor-synthesized MMCM candidate gives131.998680MHz (10ppm below nominal132MHz); it is not integrated or selected as a final board clock.

Windows USB descriptors VID0403/PID6010/REV0700 identify a reported FT2232H variant, interfaces MI00/MI01 and COM4. Managed COM enumeration sees COM4 even though Win32_SerialPort returned no rows. Official FTDI descriptor basis: [FT2232H datasheet](https://www.ftdichip.cn/Support/Documents/DataSheets/ICs/DS_FT2232H.pdf). Vivado directly discovered ARM DAP0x4BA00477 and XC7Z0200x23727093. No driver replacement was needed. Cable descriptor naming is not a board-model proof.

## Board facts / connector references

XC7Z020-1CLG400C is USER_CONFIRMED_PHYSICAL_FACT; JTAG independently confirms family only. The new Excel/image supersede legacy pin/clock-document precedence. All64connector signal pins are legal and unique in the confirmed part database. J3/J6 bank34, J4 bank35, J5 spans34/35; N18 is bank34 MRCC. Document mapping is verified, actual continuity/voltages are not. B01 resolved. B03 partially resolved: document conflicts resolved, electrical and physical routing gates remain OPEN.

J3upper/J4lower each16lanes for64TX. J5/J6 control budgets retain ONE central8RX AD7606B, not two ADC buses.5V connector pins are AUX/UNUSED and do not specify VCCO. Candidate config/docs are provided; no fabricated XDC or electrical freeze. ADC SCLK is core/4≈33MHz, distinct from TX shift core/2≈66MHz. [AD7606B Rev B](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606b.pdf) supports a frequency check, but off-chip min/max delay/loading still need qualification.

## Not validated / blocking

Bank34/35VCCO and IO standards; physical connector orientation/continuity; FTDI-B TX/RX↔PS UART/MIO and DTR/RTS routing; actual PS reference clock/reset/preset; reviewed XSA/BSP and linked Cortex-A9 firmware; real100/1000PING/PONG; PC↔PS↔AXI↔PL readback; real128-channel map/ACK generation; real GUI transport; ILA; external timing and fail-safe driver/ADC qualification. The current PS service advertises BASIC only and rejects reserved map commands; future implementation must distinguish fresh map completion from raw write_ready or an old active_valid. See PS_PLATFORM_AND_TRANSPORT_REMAINING.md.

Routed DRC retains RAMB36async-control,missing-PS7 and rule-limit warnings. Methodology retains LUT-derived-reset and missing external-delay warnings. These are not waived by internal timing PASS. Final board/PS integration must re-run implementation and review reset/BRAM behavior. An exact manual acquisition list is MISSING_PHYSICAL_FACTS.md; N18frequency measurement and unreadable part digits are not reintroduced as blockers because the user supplied explicit fallback/identity authorization.

## TCT40 and next physical hardware

10mm body,12mm radiating-center pitch,opposed8×8arrays,100mm face gap adjustable90..115mm,origin at geometric center remain the approved geometry. Vendor image claims are not batch electrical measurements. Keep independent requested/calibration, polarity/load/phase characterization and conservative10→12→16→~20Vpp qualification. No emitter, externalPCB, ADC board or levitation test was performed.50mg remains a staged final target, not a guarantee; measured5/10/25/50mg milestones follow basic particle bring-up.

## Integrity / synchronization / next stage

Frozenv1 and historical tool/model records remain unchanged; native PCB files unchanged. Uploaded active-project instructions, pin workbook/image and available references are classified with original hashes. GPS-bearing original board photograph and raw USB/cable/network identifiers are local-only; public records are sanitized. External ChatGPT history remains BLOCKED; actual observable current Codex transcript is PARTIAL. No ChatGPT decision or review is fabricated.

Next: obtain exact physical facts, construct verified PS/clock/reset/AXI platform and gated bare-board firmware; validate real transport/map/GUI; freeze bank voltages/IO/external budgets and independent disables; only then connect arrays/ADC and enter measured characterization. No program was downloaded, COM was not opened, drivers/boot/GPIO/externalPCB were not changed.

PRE_PCB_BOARD_READY = NO

REVISE
'''
    write(OUT/'RESULT.md',report)
    state_path=REPO/'shared/PROJECT_STATE.json';state=load(state_path)
    state.update(current_stage=STAGE,status='INTERNAL_TIMING_PASS_PHYSICAL_INTEGRATION_BLOCKED',stage_status='PHYSICAL_INTEGRATION_BLOCKED',
       digital_validation='PASS',candidate_core_timing='PASS_INTERNAL_OOC_132MHZ',gate_a='POST_ROUTE_INTERNAL_TIMING_PASS',
       gate_b='NOT_RUN_MISSING_VERIFIED_PLATFORM_FACTS',current_report='v2/evidence/pre_pcb_board_ready/RESULT.md',
       current_stage_evidence='v2/evidence/pre_pcb_board_ready/summary.json',digital_evidence='v2/evidence/pre_pcb_board_ready/regression_release/summary.json',
       final_source_regression='v2/evidence/pre_pcb_board_ready/regression_release/summary.json',current_regression_evidence='v2/evidence/pre_pcb_board_ready/regression_release/summary.json',
       motion_evidence='v2/evidence/pre_pcb_board_ready/regression_release/summary.json',python_tests=115,motion_python_tests=115,
       functional_recovery='PASS',board_synthesis='SYNTHESIZED_USER_CONFIRMED_PART',implementation='ROUTED_OOC_INTERNAL_132MHZ_TIMING_PASS; FULL_BOARD_NOT_VERIFIED',
       board_identification_evidence='v2/evidence/pre_pcb_board_ready/board_identity/jtag_identity.json',board_identification='JTAG_IDENTIFIED_DIRECT_VIVADO',
       board_transport_evidence='v2/evidence/pre_pcb_board_ready/axi_offline_release',motion_stage_result='SIMULATION_VALIDATED',
       overall_iteration_result='REVISE',whole_platform_result='REVISE',pre_pcb_board_ready='NO',
       next_action='Acquire bank34/35 VCCO, physical UART/MIO/DTR route and PS clock/reset/preset; build verified bare-board PS/PL platform before real transport',
       next_owner='Physical board facts / Codex verified integration',next_stage='CURRENT_V2_VERIFIED_PS_PL_PLATFORM',
       scope_of_block='Physical IO/PS platform facts and actual transport/external timing; internal core timing closed',
       current_model=MODEL,current_validation_date='2026-10-03',review_scope=STAGE,
       source_reproduction='CURRENT_STAGE_FRESH_CHECKOUT_PENDING',
       reproducibility='CROSS_SIMULATOR_PASS_CURRENT_FRESH_CHECKOUT_PENDING',
       self_calibration_evidence='v2/evidence/pre_pcb_board_ready/regression_release/regression/self_calibration/summary.json')
    state['blocking_issues']=[x for x in state['blocking_issues'] if x not in ['B01','CORE_TIMING']]
    state['blocking_ids']=[x for x in state['blocking_ids'] if x not in ['B01','CORE_TIMING']]
    state['current_core_timing_scope']=timing
    state['schematic_blocking_issues']=[x for x in state['schematic_blocking_issues'] if x!='B01']
    state['hardware_status']['board_identity']='HARDWARE_VERIFIED_IDENTITY_ONLY'
    save(state_path,state)
    eng_path=REPO/'shared/ENGINEERING_STATE.json';eng=load(eng_path)
    eng.update(current_stage=STAGE,current_model=MODEL,status=state['status'],candidate_core_timing='PASS_INTERNAL_OOC_132MHZ',
       current_report=state['current_report'],evidence=state['current_stage_evidence'],final_source_regression=state['final_source_regression'],
       python_tests=115,motion_python_tests=115,motion_full_gate='PASS',final_regression='PASS',next_action=state['next_action'],
       next_owner=state['next_owner'],hardware='HARDWARE_VERIFIED_IDENTITY_ONLY; PS/PL execution NOT_RUN',
       pre_pcb_board_ready='NO',board_identification_evidence=state['board_identification_evidence'],
       source_reproduction='PREVIOUS_SCOPE_PRESERVED; CURRENT_STAGE_FRESH_CHECKOUT_PENDING',independent_review='PENDING')
    eng.update(stage_status=state['stage_status'],gate_a=state['gate_a'],gate_b=state['gate_b'],
        implementation=state['implementation'],physical_speed_grade='-1',current_stage_evidence=state['current_stage_evidence'],
        digital_evidence=state['digital_evidence'],motion_evidence=state['motion_evidence'],current_regression_evidence=state['current_regression_evidence'],
        current_interaction_session='S-20261003-codex-002',review_scope=STAGE)
    eng['open_ai_problems']=[x for x in eng.get('open_ai_problems',[]) if x!='P-20260929-001'];save(eng_path,eng)
    blockers='''# Current v2 blockers — 2026-10-03

Current model: GPT-6.1 Sol High. B01 RESOLVED: XC7Z020-1CLG400C user-confirmed. Internal CORE_TIMING RESOLVED in strategy3: routed132MHz WNS+0.082,TNS0,WHS+0.072,THS0,zero routing errors. B02 current source priority superseded by explicit N18/33.333MHz fallback; measurement is not required to proceed with that documented fallback.

| Gate | Current status | Required next evidence |
|---|---|---|
| B03 | DOCUMENT_MAPPING_RESOLVED; ELECTRICAL_ROUTE_OPEN | Bank34/35 VCCO,actual connector orientation/continuity,matched IO standard and translator voltage |
| PS/UART | BLOCKED | FTDI-B TX/RX/DTR/RTS to UART instance/MIO; PS reference clock/reset; reviewed preset/XSA/BSP/ARM build |
| Real transport | NOT_RUN |100/1000 packets,safe MMIO,atomic map/ACK generation,real GUI/ILA after verified platform |
| B04 | OPEN | Off-chip min/max timing,loading,watchdog,power and ADC/driver qualification; review retained DRC/methodology warnings |
| B05/B06/B07 | OPEN_PHYSICAL | Actual10mm batch load/polarity/phase/amplitude,receiver/ADC reference and measured levitation |
| Independent Review | PENDING | External review of actual source,warning scope and hardware evidence; no fabricated ChatGPT approval |

Detailed acquisition list: v2/evidence/pre_pcb_board_ready/MISSING_PHYSICAL_FACTS.md. No unknown-pin XDC,driver replacement,boot change,serial opening,bitstream download or PCB operation occurred. External ChatGPT history is BLOCKED and observable Codex transcript PARTIAL; these do not prevent sourced digital work.
'''
    write(REPO/'shared/BLOCKERS_ENGINEERING.md',blockers)
    old=(REPO/'shared/BLOCKERS.md').read_text(encoding='utf-8');write(REPO/'shared/BLOCKERS.md',blockers+'\n---\n\nThe following historical blocker narratives retain original provenance; current status is above.\n\n'+old)
    plan='''# Current v2 continuation — 2026-10-03

Current model: GPT-6.1 Sol High. Stage: TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE.

Completed: latest personalized-rule review; uploaded-file classification and hash audit; direct USB/JTAG identity; user-confirmed exact part and updated document precedence;64legal connector signals; proven-equivalent queue/scheduler timing changes; actual132MHz post-route internal timing PASS;115Python tests and complete four-run3696-frame motion/calibration/ADC regression; offline AXI/host-C; both-simulator queue/scheduler/throughput/independent-array-disable checks; vendor-synthesized clock candidate. Failures preserved.

Next: exact physical VCCO and PS clock/reset/UART/MIO/connector facts; verified XSA/BSP/target build and safe bare-board wrapper; real transport/map completion/GUI/ILA; complete electrical/disable budgets and then PCB interface freeze. No new version. Follow MISSING_PHYSICAL_FACTS.md and PS_PLATFORM_AND_TRANSPORT_REMAINING.md. Do not repeat core optimization without a newly evidenced failure.

Do Not Change: frozenv1/history/model provenance,packet/register interface,128channels/8bit,requested/calibration split,atomics,upper/lower mapping,38.5..41.5kHz and current radiating-center geometry. No failing-design or guessed-platform deployment.132MHz is a routed internal design target; final board clock and external constraints require reviewed integration. Do not waive DRC/warnings or declare PCB ready from OOC PASS.
'''
    write(REPO/'shared/CURRENT_PLAN.md',plan)
    write(REPO/'shared/HANDOFF.md',plan+'\nCurrent full result: v2/evidence/pre_pcb_board_ready/RESULT.md. Current source commit and sync evidence follow the checkpoint. Hardware status remains identification only.\n')
    write(REPO/'shared/PROJECT_STATE.md',report)
    write(ROOT/'docs/CONTINUE_CURRENT_V2.md',plan+'\nTeam setup: root 指南.md. Current evidence: evidence/pre_pcb_board_ready/.\n')
    with (REPO/'shared/ACCEPTANCE.md').open('a',encoding='utf-8') as f:
        f.write('\n\n## Current pre-PCB contract — 2026-10-03\n\nCurrent model: GPT-6.1 Sol High. Original Acceptance thresholds unchanged. Actual internal timing/complete simulation gates PASS as recorded in v2/evidence/pre_pcb_board_ready/summary.json. Full PRE_PCB_BOARD_READY remains NO because electrical/PS/real transport/map/GUI conditions are unverified. External review PENDING; no full-project ACCEPT.\n')
    for rel in ['shared/CHANGELOG.md','CHANGELOG.md']:
        p=REPO/rel
        with p.open('a',encoding='utf-8') as f:f.write('\n\n2026-10-03 /v2 /GPT-6.1 Sol High: reviewed new rules and sourced board facts,classified uploads,closed internal132MHz routed core timing with proven-equivalent queue/scheduler control changes,complete115-test/four-run motion regression PASS. Preserved failures and inherited/frozen sources. Pre-PCB electrical/PS/real transport readiness remains NO. No hardware programming or PCB edits.\n')
    guide='''# SonoField-FPGA 当前 v2 接手指南

更新：2026-10-03。当前模型记录：GPT-6.1 Sol High；版本仍为 v2，分支 main。

**内部132MHz核心时序和完整数字回归已通过；PRE_PCB_BOARD_READY=NO。不要直接下载并连接阵列。** 最新恢复入口依次是 README、AGENTS、shared/PROJECT_STATE.json、VERSION_STATE.json、CONTEXT_CHECKPOINT、CURRENT_PLAN、DECISIONS、BLOCKERS、ACCEPTANCE、v2/evidence/pre_pcb_board_ready/RESULT.md。

## 获取完整历史与受支持的活动工作区

使用 Git clone 继续开发；GitHub ZIP 可用于查看源码/原理图，但不包含用于冻结核验的 Git 历史。完整历史保留在克隆对象中；推荐 sparse 工作区仅展开活动工程与资料，避免历史v1原始CRLF字节哈希和平台 checkout 规范化的已知差异。不要为解决差异修改冻结v1。

```powershell
git -c core.autocrlf=false clone --filter=blob:none --sparse https://github.com/loverlike1216/SonoField-FPGA.git SonoField-FPGA
Set-Location SonoField-FPGA
git sparse-checkout set v2 shared AI-interaction-memory AI-chat-memory AI-problem PCB Zynq7020
git status --short
git branch --show-current
```

根目录文件自动展开，所有版本历史可用。工作区路径由同事自行选择，不依赖本机E/G盘。新 pin workbook/image 位于 v2/hardware/board/references/20261003_user；BOM位于v2/hardware/bom；原理图位于PCB/V1，仍是草稿，禁止据此直接制造。

## Windows 环境

默认PowerShell7 (`pwsh`)，不使用WindowsPowerShell5.1。已验证Python3.10.11、Vivado2025.2、Icarus和本机GCC；本机路径不是同事默认路径。安装同版本工具并设置自身路径。

```powershell
py -3.10 -m venv .venv
.venv/Scripts/python.exe -m pip install -r v2/requirements-lock.txt
$env:VIVADO_BIN='D:/Vivado/2025.2/2025.2/Vivado/bin' # 换成自身安装路径
$env:IVERILOG_BIN='C:/iverilog/bin'                  # 换成自身安装路径
$env:CC='D:/DevC++/Dev-Cpp/TDM-GCC-64/bin/gcc.exe'   # 换成自身GCC
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
```

真实串口依赖requirements-board.txt，但安装依赖不意味着允许打开串口。ARM目标工具链和BSP单独核验，hostGCC的DLL不是PS可运行ELF。

## 快速与完整数字复现

```powershell
pwsh -NoProfile -File v2/scripts/run_pre_pcb.ps1
.venv/Scripts/python.exe v2/scripts/board_transport_gate.py --output evidence/pre_pcb_board_ready/team_axi
.venv/Scripts/python.exe v2/scripts/motion_gate.py --output evidence/pre_pcb_board_ready/team_regression
```

快速门禁应返回队列/调度器原新逐周期相等、11周期吞吐、双阵列独立禁用双模拟器PASS和冻结核验PASS。完整门禁应返回115Python测试、全部继承/ADC/校准、3次Icarus+1次XSim、每次3696帧、四组 canonical哈希相同。使用新证据目录，保留所有失败。GUI关闭不代表工程通过，读取summary.json。

仿真进程900秒wall-time超时是SIMULATOR_PROCESS_TIMEOUT，区别于RTL周期超时；不要增大RTL ACK参数或删assert。首次并行两次Vivado布线与多次GUI仿真曾造成进程超时，失败保留。复现完整运动门禁时避免同时运行多个重型EDA任务。

## Vivado 内部时序复现与结果窗口

```powershell
New-Item -ItemType Directory -Force v2/build/pre_pcb | Out-Null
& "$env:VIVADO_BIN/vivado.bat" -mode batch -source v2/scripts/pre_pcb_timing.tcl -log v2/build/pre_pcb/team_timing.log -journal v2/build/pre_pcb/team_timing.jou -tclargs strategy3 evidence/pre_pcb_board_ready/timing/team_reproduction
& "$env:VIVADO_BIN/vivado.bat" -mode gui -source v2/scripts/show_pre_pcb_results.tcl
```

策略源码快照在timing/strategy3；DCP按脚本在本机生成，未提交大型生成物。已有归档输出目录会拒绝覆盖。PASS标准WNS>=0,TNS0,WHS>=0,THS0,路由错误0,内部无约束0；本次实测+0.082/0/+0.072/0。余量较小，板级集成必须重新实现。OOC报告保留外部延时缺失、PS7缺失、BRAM异步控制和LUT复位警告，不得当作完整板级PASS。结果页在evidence/pre_pcb_board_ready/RESULT.html，可离线浏览。

## 板卡检测、已确认和未确认

```powershell
pwsh -NoProfile -File v2/scripts/pre_pcb_detect.ps1 -OutputPath v2/evidence/pre_pcb_board_ready/team_board
```

仅枚举设备，不打开COM。JTAG脚本pre_pcb_jtag.tcl需要现有hw_server localhost3121，限定单目标，读取后关闭批处理连接；不得改驱动/EEPROM/Boot或下载程序。当前VID0403/PID6010/REV0700、COM4、ARM DAP4BA00477、XC7Z02023727093均为实读；完整XC7Z020-1CLG400C来自用户确认。COM编号可能变化，不能硬编码COM4作为通用默认。

新Excel优先于历史const；N18/33.333MHz是用户批准fallback。clock_facts记录候选MMCM131.998680MHz与名义132MHz的10ppm差异，最终板级参数/PLL/PS/AXI配置尚未冻结。J3/J6 bank34、J4 bank35、J5跨两bank；5V引脚不说明VCCO。具体缺失事实与操作要求见MISSING_PHYSICAL_FACTS.md和MANUAL_VCCO_MEASUREMENT_REQUIRED.md。

## 下一开发顺序

1. 获取本板 bank34/35电压、连接器方向/连续性、FTDI-B的UART/MIO与DTR/RTS、PS参考时钟/复位/匹配preset。
2. 生成并审查XSA/BSP/目标ELF、PS↔PL时钟复位/AXI；裸板烟雾顶层禁用所有外部输出。
3. 真实100→1000PING/PONG、安全寄存器回读、既有MAP命令实现与原子提交/ACK序列、错误/断链/超时、ILA、真实GUI。当前C服务只有BASIC，不假装已实现真实MAP。
4. 资格化独立阵列禁用适配器和J3/J4/J5/J6、电气预算/负载、IO标准和外部时序，再冻结PCB接口并连接外部硬件。
5. 10mm换能器逐颗测量，再做两只对向与轻粒子测试；5/10/25/50mg需称重、尺寸/密度和电气/环境证据。

## 连续性与证据维护

只继续v2，不自动升级，不改历史模型来源或冻结v1，不改接口/寄存器/相位语义、不force-push。重大结果更新shared、CONTEXT_CHECKPOINT、AI-interaction-memory，提交并验证远端commit。ChatGPT聊天不可访问时保持BLOCKED，不伪造历史/Decision。GPS原照片和原始USB/网络标识只保留本地，公开引用和哈希已保存。原始上传文件可不可用不影响已归档源码/引脚资料的数字复现。

下面旧指南保留其历史标签范围，不能覆盖上述当前恢复入口。

---

'''
    old=(REPO/'指南.md').read_text(encoding='utf-8');write(REPO/'指南.md',guide+old)
    rows=[('内部132MHz布线','PASS','WNS+0.082 / WHS+0.072 / 路由错误0'),
          ('数字回归','PASS','115测试；4次×3696帧；双模拟器'),('板卡身份','已确认','用户完整料号＋实读JTAG'),
          ('J3/J4/J5/J6','候选','文档/封装已核验；电气未冻结'),('真实PS/串口/MAP/GUI','NOT_RUN','缺PS平台及实际线路事实'),
          ('VCCO与外部时序','BLOCKED','bank34/35、电平、min/max预算未验证')]
    table=''.join(f'<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td><td>{html.escape(c)}</td></tr>' for a,b,c in rows)
    page=f'''<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SonoField-FPGA v2 — 当前工程结果</title><style>body{{font:18px/1.65 system-ui,"Microsoft YaHei";max-width:1120px;margin:36px auto;padding:0 24px;color:#162330;background:#f6f8fc}}h1{{font-size:32px}}.card{{background:white;padding:24px;border-radius:14px;margin:20px 0;border:1px solid #d5dfea}}.no{{color:#9b2424;font-weight:700}}table{{border-collapse:collapse;width:100%}}td,th{{padding:12px;border-bottom:1px solid #dce3ed;text-align:left}}a{{color:#145db4}}code{{background:#e8edf4;padding:3px 6px}}pre{{white-space:pre-wrap}}</style><h1>SonoField-FPGA · v2 当前结果</h1><p>GPT-6.1 Sol High · main · 2026-10-03</p><div class="card"><h2>内部时序闭合，板级集成仍需事实与验证</h2><p class="no">PRE_PCB_BOARD_READY = NO · REVISE</p><p>未下载程序、未打开COM、未驱动GPIO、未操作外部PCB。当前Vivado窗口显示真实routed DCP的内部时序结果。</p></div><div class="card"><table><tr><th>项目</th><th>状态</th><th>依据</th></tr>{table}</table></div><div class="card"><h2>恢复与交接</h2><p><a href="RESULT.md">完整阶段报告</a> · <a href="summary.json">机器可读结果</a> · <a href="MISSING_PHYSICAL_FACTS.md">准确缺失事实</a> · <a href="../../docs/hardware/PS_PLATFORM_AND_TRANSPORT_REMAINING.md">PS与通信边界</a></p><p><a href="timing/strategy3/routed/timing_summary.rpt">实际时序报告</a> · <a href="regression_release/summary.json">最终回归</a> · <a href="connector_reference/connector_audit.json">连接器核验</a></p><p>当前实际工作区：<code>{html.escape(str(REPO))}</code>；从GitHub继续开发先读根目录《指南.md》与shared/CONTEXT_CHECKPOINT。</p></div><div class="card"><h2>下一步</h2><p>取得两bank电压、实际UART/MIO与PS时钟/复位/preset；构造 verified XSA/BSP/安全裸板平台；完成真实通信/原子MAP/GUI；资格化电气与双阵列禁用，再连接阵列和ADC。</p></div></html>'''
    write(OUT/'RESULT.html',page)
    print('Reconciled evidence/state/guide: internal timing and digital PASS; PRE_PCB_BOARD_READY NO; REVISE')

if __name__=='__main__':main()
