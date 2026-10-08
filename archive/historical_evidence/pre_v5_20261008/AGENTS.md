# SonoField-FPGA engineering rules

Project SONOFIELD_FPGA; repository loverlike1216/SonoField-FPGA; branch main.
Workspace E:\Codex_project\AMD-SonoField-FPGA. Active version v2; engineering root v2/.
The user-provided personalized rules govern execution. This file is their project-specific application.

## Current governance — replacement rules 2026-10-03

The user's latest replacement policy supersedes prior AGENTS instructions. Source: AI-interaction-memory/codex/instructions/codex_engineering_rules_20261003.md. Codex maintains engineering facts, current plans, decisions, checkpoints and observable interaction records. No separate documentation agent is needed. Do not fabricate external ChatGPT history or decisions.

Primary scope is v2 single Robei octagonal Zynq-7020 acoustic control; stage CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST. Latest formal execution contract and user approval remain in v2/evidence/core_timing_real_loop/EXECUTION_CONTRACT.md and decision P-20260927-001. Two timing rounds are exhausted; Gate A FAIL. P-20260929-001 is the next bounded timing proposal, not an approved third round. No PCB changes, unknown GPIO, UART transmission or failing-design deployment.

On recovery, read README/AGENTS, PROJECT_STATE, VERSION_STATE, CONTEXT_CHECKPOINT, CURRENT_PLAN, DECISIONS, BLOCKERS, ACCEPTANCE, latest evidence, open problems and Git status/diff/HEAD/origin. Read interaction indexes only as needed. Real facts prevail over stale plans or model inference.

Create reconciled CONTEXT_CHECKPOINT.md/json and historical context-checkpoints after substantial validation, decisions, handoff or pause. Record identity, source commit, architecture, completed/verified states, next actions, blockers, limits, Do Not Change, invariants and evidence. Checkpoints never change versions or acceptance.

Continue means current v2. Preserve frozen v1 and historical artifacts. No new version, repository, core architecture/interface/hardware change, important data deletion, force push, history rewrite, release, deployment, visibility change or significant costs without required user approval. Ordinary reversible fixes within current contract are autonomous. No sub-agent work is requested.

Preserve 128-channel/8-bit capability, requested/calibration separation, atomic maps, common clock, register/packet/channel formats, safety behavior, motion cadence and zero added latency of the current refactors. Production remains132MHz core/66MHz shift pending valid quantitative decision. Conservative-1 is an engineering assumption, physical grade UNKNOWN. Gate B needs Gate A plus actual UART/PS facts. No guessed board constraints.

Use pwsh7 for Windows orchestration, Tcl inside Vivado2025.2. Preserve failures and thresholds; keep generated products separate. Diff/secret/privacy review, commit, push, verify remote and publish checkpoint after significant work. Final acceptance is independent; simulation is not hardware.

## Observable interaction checkpoints
- Codex persists observable interaction memory under the latest replacement rules.
- Read its INDEX at preflight. If authorized, use AI-interaction-memory/tools/sync_codex.py with the verified rollout before
  stage/session commit; capture the previous final response at the next checkpoint. No background hook is installed.
- Keep only actual observable messages. Never export reasoning, analysis, compaction summaries, system/developer
  prompts or raw source-log/tool payloads that might echo them. Preserve PARTIAL/BLOCKED truthfully.
- Keep ChatGPT canonical history in AI-chat-memory and reference it. Work/other-ai/cross-agent records require
  real participation. Formal prompts may remain verbatim in the transcript, including historical quoted labels.
- Run the exporter integrity/secret check and review privacy before committing records to GitHub.
- Full tool payload copying is disabled; curate critical commands/results with evidence links under tool-flow.
- Session ID/role/time/source ID/hash/cutoff distinguish recorded facts from unavailable history and summaries.

## v2 authorization and frozen parent
User attachment explicitly authorized v2. v1 is frozen and must remain byte-identical to shared/versions/v1_freeze.json.
Current user attachment v2_self_calibration.md authorizes the complete self-calibration software/digital stage in v2. Stop before PCB implementation.
No v2 execution may import sources/tests/config from v1. Root governance is shared. BOM source metadata does not override current user approval.

## Schematic stage authorization (2026-09-25)
User instruction v2_schematic_revision_V1.md supersedes the earlier stop boundary for
schematic capture only. Active project remains v2; schematic revision V1 lives in
the explicitly requested root PCB/V1/{project,log,device}. No PCB layout or fabrication.
Contract: PCB/V1/log/preflight/EXECUTION_CONTRACT.md. Native EDA results must be real.

## Windows terminal preference
Default to PowerShell 7 (`pwsh`) for all Windows commands. Do not use Windows PowerShell 5.1 unless the user explicitly requests another terminal or a documented dependency requires 5.1. Long-term preference explicitly requested 2026-09-26.

## Model continuity — 2026-10-03

User manually selected **GPT-6.1 Sol High**, replacing GPT-6 Astra High for subsequent work. Record this user-declared current model in new orchestration evidence, analyses, interaction events and state metadata. Preserve historical model provenance and native tool logs; use sidecars for generated outputs. Source: AI-interaction-memory/codex/I-20261003-0001__model-transition.md; metadata: shared/MODEL_ENVIRONMENT.json.

A model switch never authorizes version, stage, architecture, interface, parameter or Acceptance changes. Continue existing v2 single-board engineering state. New code/tool evidence or an explicit requirement change is needed to revise a valid technical decision. Follow the latest replacement ownership and checkpoint policy. The user explicitly authorizes Codex to persist this MODEL_TRANSITION event and its matching configuration/index.

## Active recovery context — 2026-10-03

Current model: GPT-6.1 Sol High. Active project memory and next actions cover **v2 single Robei octagonal Zynq-7020 acoustic control only**. User requested removal of inactive-project reminders from recovery memory. Do not load inactive source directories or propose their continuation. Preserve original historical evidence and user quotations. Focus event: AI-interaction-memory/codex/I-20261003-0002__v2-focus.md.

## Latest execution contract — 2026-10-03 pre-PCB integration

The direct user attachment `AI-interaction-memory/codex/instructions/v2_final_pre_pcb_board_integration.md` supersedes the previous exhausted timing-window restriction for the new current-v2 stage `TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE`. It explicitly approves P-20260929-001 queue/control/reset timing work and classifies XC7Z020-1CLG400C as USER_CONFIRMED_PHYSICAL_FACT. Preserve prior uncertainty reports.

New evidence precedence: real detection, current user Excel/image, revision-matched manufacturer data, existing constraints, converted XDC, secondary history. N18/33.333 MHz is the approved fallback if no measurement can resolve the old33MHz conflict. Production clock is selected only when both routed timing and actual serializer throughput pass;132/66MHz is preferred, not immutable. No guessed VCCO/UART/PS preset. J3/J4 have16upper/lower DATA lanes each;J5/J6 control timing shares one master and supports independent safe disable. Connector5V remains unused for array power. Existing central eight-channel ADC topology governs budgeting; do not invent a second ADC.

Fresh read-only board detection is authorized. Real safe bare-board programming/PS/transport tests are authorized only after Timing PASS and verified physical prerequisites; no external PCB/ultrasonic outputs, driver changes, EEPROM/boot changes or PCB layout edits. End with actual result view and categorized uploaded sources, state/checkpoint/interaction/Git sync. Stop when ready or all automatic work is complete with exact physical blockers documented. No repeated route retries without a materially new implementation strategy.
