# MODEL_TRANSITION

Event ID: I-20261003-0001
Record Date: 2026-10-03 (Asia/Shanghai; exact user-message timestamp unavailable)
PROJECT_ID: SONOFIELD_FPGA
Project: SonoField-FPGA
Repository: https://github.com/loverlike1216/SonoField-FPGA.git
Branch: main
Workspace: E:\Codex_project\AMD-SonoField-FPGA
Project Version: v2 — Unchanged
Project Stage: CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST — Unchanged

- Previous Model: GPT-6 Astra High
- Current Model: GPT-6.1 Sol High
- Transition Type: Manual Model Switch
- Architecture: Unchanged unless new evidence justifies revision
- Engineering State: Continue from current repository state
- Historical Records: Preserve original model provenance
- Future Primary Model: GPT-6.1 Sol High
- Authorization: Direct user instruction in the current Codex conversation, 2026-10-03
- Model Provenance Basis: USER_DECLARED_MANUAL_SELECTION
- Runtime Exact Variant Independent Verification: NOT_EXPOSED
- Work Status: OFF

## Observable user requirement

User explicitly requested continued engineering from the existing version, stage, branch, repository and workspace; preservation of valid decisions, interfaces, parameters, Acceptance and historical model provenance; and one formal MODEL_TRANSITION event. A manual model switch does not authorize a project version upgrade, reset, architecture rewrite or reinterpretation of earlier evidence.

This record documents the observable user instruction. It does not claim access to external ChatGPT history or record hidden reasoning. External ChatGPT source SonoField-FPGA remains BLOCKED. The existing Codex transcript remains PARTIAL and is not rewritten or re-exported by this event.

## Repository and evidence checked

Starting local HEAD and origin/main: b11c80ca3e7fc7745241c32f8f80d95329ca4ddf. Existing engineering changes are uncommitted at transition start; preserve them. Active v2; current execution is the single-board v2 project. Frozen v1 and PCB files remain protected.

Read README, AGENTS, PROJECT_STATE, VERSION_STATE, ENGINEERING_STATE, CURRENT_PLAN, DECISIONS, ACCEPTANCE, BLOCKERS, CHANGELOG, AI-chat-memory, AI-interaction-memory and current timing/simulation/hardware evidence. CURRENT_PLAN and older narrative tables still describe historical stages; real engineering evidence prevails. Model change supplies no new evidence that would invalidate existing technical decisions.

Historical v2 results: phase/burst equivalence and offline AXI PASS; round2 routed WNS -4.515 ns, TNS -6007.936 ns, WHS +0.070 ns, THS 0.000 ns. Gate A FAIL. The earlier full motion regression PASS is preserved; the last GUI retry exited 1 and is also preserved. Recovery revalidation is recorded separately under the current model, without rewriting either prior run.

## Persistence and continuity policy

New analysis, reviews, decisions, summaries, interaction events and model metadata use GPT-6.1 Sol High from this point. Raw tool-generated logs retain native contents; new-run MODEL_PROVENANCE.json sidecars identify the orchestration model and output hashes. Generated source files follow existing formats; model identity is orchestration metadata and never changes logic.

Relevant continuity evidence: [preflight and protected hashes](../../v2/evidence/core_timing_real_loop/recovery_20261003/continuity_baseline.json).
Current model configuration: [MODEL_ENVIRONMENT.json](../../shared/MODEL_ENVIRONMENT.json).

Engineering priority: finish the current v2 single Robei octagonal Zynq-7020 sound-field controller. Keep current bounded timing contract and Gate A/Gate B safety conditions. No new version, PCB changes or unverified physical claims follow from this model switch.
