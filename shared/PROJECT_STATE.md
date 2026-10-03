# Current engineering state — 2026-10-03

Current model: GPT-6.1 Sol High (user-declared manual selection). Project SONOFIELD_FPGA/SonoField-FPGA,main,activev2,workspaceE:\Codex_project\AMD-SonoField-FPGA. Stage CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST. Primary scope: single Robei octagonal Zynq-7020 controller.

Current machine state: [PROJECT_STATE.json](PROJECT_STATE.json), [ENGINEERING_STATE.json](ENGINEERING_STATE.json). Recover via [CONTEXT_CHECKPOINT](CONTEXT_CHECKPOINT.md) after real evidence reconciliation. Model transition changes no version,architecture,interface,parameter or Acceptance. Current formal model/focus events are in AI-interaction-memory.

Timing Gate A FAIL: conservative engineering-1 round2routedWNS-4.515ns,TNS-6007.936ns,WHS+0.070ns,THS0. Physical speed UNKNOWN. Offline equivalence/AXI simulation PASS. Current recovery regression and known failures: [engineering report](../v2/evidence/core_timing_real_loop/RESULT.md) and [recovery summary](../v2/evidence/core_timing_real_loop/recovery_20261003/summary.json).

Real PS firmware,UARTrouting,PC↔PS↔AXI↔PL exchange,external acoustic operation and levitation NOT_VERIFIED. Next bounded timing decision: P-20260929-001. Stage and whole physical platform remain REVISE. Historical entries below retain their original evidence scope.

---

# Current project state

SONOFIELD_FPGA / SonoField-FPGA / main / active v2 / frozen v1.
Repository: https://github.com/loverlike1216/SonoField-FPGA.git
Workspace: E:\Codex_project\AMD-SonoField-FPGA (actual path; earlier hyphen path obsolete).
Stage: SCHEMATIC_DESIGN_JLCEDA_PRO; schematic revision V1, no project version change.

Single native sheet:128TX,8RX,1561components,83named modules. Native PDF/SVG exported and representative TX/ADC/RX/power views reviewed.3992-pin intent audit and1338 independent mapping checks PASS.212 frozen v1 files unchanged.
ERC:0fatal/0error/45warnings; electrical release REVISE. Timing, watchdog/power qualification, physical FPGA pins/VCCO and MPN/batch qualification remain open. No PCB/bitstream/hardware claim.

Earlier software validation remains historical PASS (not rerun for presentation edits). External ChatGPT BLOCKED; observable Codex transcript PARTIAL. Read report_schematic_v2_V1.md and PCB/V1/project/README.md.
