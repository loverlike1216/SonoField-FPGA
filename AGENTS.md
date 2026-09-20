# SonoField-FPGA engineering rules

Project SONOFIELD_FPGA; repository loverlike1216/SonoField-FPGA; branch main.
Workspace E:\Codex-project\AMD-SonoField-FPGA. Active version v2; engineering root v2/.
The user-provided personalized rules govern execution. This file is their project-specific application.

- Preflight local/remote Git, shared/PROJECT_STATE.json, VERSION_STATE.json, plan, decisions, blockers,
  acceptance, AI-chat-memory/INDEX.md, AI-interaction-memory/INDEX.md and open AI-problem records before changes.
- Continue means the current version. Stages do not create versions. No v3 without explicit user approval.
- Root holds cross-version state and AI coordination. v2 holds runnable sources, tests, scripts,
  dependencies, technical docs, hardware and evidence. Run engineering commands from v2.
- User approved same-version layout cleanup and removal of obsolete records from current tree.
  Keep Git history. Future version upgrades copy reusable content and freeze the old version intact.
- Update execution contract before major changes; baseline, implement, run, cross-check, save evidence,
  update shared/handoff, commit/push and verify remote. Never weaken tests for PASS.
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
- Persist user/Codex project instructions, corrections, approvals and visible responses in AI-interaction-memory.
- Read its INDEX at preflight. Use tools/sync_codex.py with the verified local rollout at task start and before
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
This stage only bootstraps a complete standalone v2 and repeats inherited verification. Stop for review before calibration/ADC development.
No v2 execution may import sources/tests/config from v1. Root governance is shared. BOM source metadata does not override current user approval.
