# SonoField-FPGA engineering rules

Project SONOFIELD_FPGA; repository loverlike1216/SonoField-FPGA; branch main.
Workspace E:\Codex_project\AMD-SonoField-FPGA. Active version v2; engineering root v2/.
The user-provided personalized rules govern execution. This file is their project-specific application.

## Current governance — 2026-09-27-r1

- The user's latest Chat/Codex/Work policy supersedes older workflow text below.
- Codex owns engineering sources, tests, configuration, Git, engineering evidence and machine state.
- Work owns general narrative docs, formal decision persistence and AI memories. Work is OFF unless
  the user explicitly starts it. Do not spawn auxiliary agents or claim independent Chat acceptance.
- The current user instruction authorizes continuing v2 at INTERACTIVE_LEVITATION_AND_TRAJECTORY_CONTROL.
  Its sections 64 and 67 explicitly authorize the six v2/docs/motion documents and interaction records
  as a task-specific exception. This does not authorize broad edits to Work-owned plans or memories.
- Engineering checkpoint authority: evidence/engineering/motion/EXECUTION_CONTRACT.md.
- Keep PCB files and frozen v1 untouched. No v3, deployment, release or fabricated board constraints.
- Default all Windows orchestration to pwsh (PowerShell 7). No automatic PowerShell 5.1 fallback.
- Mark stale general narratives DOCUMENTATION_UPDATE_REQUIRED; use canonical engineering state.

- Preflight local/remote Git, shared/PROJECT_STATE.json, VERSION_STATE.json, plan, decisions, blockers,
  acceptance, AI-chat-memory/INDEX.md, AI-interaction-memory/INDEX.md and open AI-problem records before changes.
- Continue means the current version. Stages do not create versions. No v3 without explicit user approval.
- Root holds cross-version state and AI coordination. v2 holds runnable sources, tests, scripts,
  dependencies, technical docs, hardware and evidence. Run engineering commands from v2.
- User approved same-version layout cleanup and removal of obsolete records from current tree.
  Keep Git history. Future version upgrades copy reusable content and freeze the old version intact.
- Update execution contract before major changes; baseline, implement, run, cross-check, save engineering
  evidence/state, commit/push and verify remote. Work updates shared/HANDOFF when authorized.
  Never weaken tests for PASS.
- Stable module names stay stable. Directory changes require full path/build/EDA/test regression.
- Chat source is SonoField-FPGA. Verify real reader capability before importing history. BLOCKED means
  no fabricated transcript or decision. Current Codex messages are not external ChatGPT history.
- Major unresolved decisions use AI-problem/problem; decisions require actual source, matching ID,
  body SHA256 and active version. User remains authority for versions/cost/publication/major scope.
- Preserve root Zynq7020 user references; constrain files have user-selected precedence.
  Do not guess device ordering code, pins, clock, bank VCCO or IO standards. No invented XDC/bitstream.
- Vivado 2025.2 is authoritative. Keep simulation, synthesis, implementation and hardware distinct.
- Never directly drive transducers from FPGA. No physical levitation claim without measurements.
- Requested and calibration phase stay separate; complete maps commit atomically.
- Inspect sensitive/licensed/private files before push. No release/deploy/visibility change without approval.
- Final review result: ACCEPT / ACCEPT WITH LIMITATIONS / REVISE, scoped to the reviewed work.
  Whole-platform acceptance is external; hardware blockers prohibit claiming full project ACCEPT.

## Observable interaction checkpoints
- Interaction memory is Work-owned by default; only use a current explicit user exception to persist it as Codex.
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
