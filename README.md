# SonoField-FPGA

128-channel ultrasonic phased-array project on Robei Zynq-7020, with nominal 10 mm transmitters,
12 mm radiating-center pitch and adjustable 90–115 mm face gap (100 mm nominal).

Current version **v2**, stage **CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST**. v1 is frozen intact; schematic revision remains **V1**.

**团队接手入口：[指南.md](指南.md)** — 当前进度、已解决/未解决问题、Windows环境、离线复现和后续开发。
当前 main 的恢复入口：[当前 v2 接手补充](v2/docs/CONTINUE_CURRENT_V2.md) 和 [CONTEXT_CHECKPOINT](shared/CONTEXT_CHECKPOINT.md)；下列标签保留其历史交接范围。
阶段标签：`v2-board-transport-offline-20260929`（离线工程检查点，非正式Release或硬件验收）。
2026-10-03 当前回归：114项Python测试、协议/AXI双模拟器、完整运动/校准回归通过；历史独立环境复现保留其原验证范围。
XC7Z020/CLG400已确认；速度等级、UART路由、VCCO/连接器和132 MHz核心时序仍阻塞上板。
User explicitly approved v2 and this software/digital stage. The complete inherited baseline is retained.
Self-calibration and ADC acquisition have automated synthetic/RTL validation. Physical acquisition,
PCB manufacture and levitation remain unverified. Native schematic draft is available; execution remains focused on the active single-board v2 project; PCB layout and fabrication remain unstarted.

| Directory | Purpose |
|---|---|
| v2/ | Complete runnable current engineering version and fresh evidence |
| v1/ | Frozen prior source, docs, tests and evidence; no edits |
| shared/ | Current state, approval, freeze manifest, plans, blockers and acceptance |
| AI-chat-memory/ | External ChatGPT source SonoField-FPGA; BLOCKED |
| AI-interaction-memory/ | Actual visible Codex messages, user instructions and tool-flow checkpoints |
| AI-problem/ | Existing board/serializer/transducer questions; no fabricated decisions |
| BOM/ and Zynq7020/ | User originals retained locally; canonical imported BOM is inside v2 |

Start with [v2 operating guide](v2/docs/OPERATING_GUIDE.md), [migration](v2/docs/architecture/V1_TO_V2_MIGRATION.md),
[BOM review](v2/hardware/bom/BOM_LOCK.md), [state](shared/PROJECT_STATE.md) and [handoff](shared/HANDOFF.md).
Run commands from v2. No bitstream, measured calibration or levitation result is claimed.

Current architecture: [self-calibration](v2/docs/architecture/SELF_CALIBRATION.md).
Future board boundary: [hardware/software contract](v2/docs/hardware/PCB_SOFTWARE_INTERFACE.md).

Read the [single-sheet schematic package](PCB/V1/project/README.md), [vector PDF](PCB/V1/project/SonoField-SingleSheet.pdf), [channel mapping](v2/docs/hardware/SCHEMATIC_CHANNEL_MAP.md) and [current review report](shared/report_schematic_v2_V1.md). Electrical release is **REVISE**, with45classified ERC warnings and unresolved hardware gates. Windows commands default to PowerShell7 (`pwsh`).

Current model environment: **GPT-6.1 Sol High**, user manual transition2026-10-03; [MODEL_TRANSITION](AI-interaction-memory/codex/I-20261003-0001__model-transition.md). Historical model provenance stays intact.
Current v2 checkpoint: [engineering report](v2/evidence/core_timing_real_loop/RESULT.md), [timing RCA](v2/evidence/core_timing_real_loop/timing_decision.md) and [recovery summary](v2/evidence/core_timing_real_loop/recovery_20261003/summary.json). Gate A FAIL: routed WNS -4.515ns; real PS/PL transport NOT_RUN. Next bounded timing proposal: [P-20260929-001](AI-problem/problem/P-20260929-001__queue-control-timing.md). Prior tagged guide remains a historical handoff.

恢复工程优先读 [CONTEXT_CHECKPOINT.md](shared/CONTEXT_CHECKPOINT.md) / [机器检查点](shared/CONTEXT_CHECKPOINT.json)，再读当前计划、决策与证据；当前模型来源与最新规则不触发版本升级。
