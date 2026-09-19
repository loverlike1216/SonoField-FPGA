# SonoField-FPGA engineering rules

Project SONOFIELD_FPGA; repository loverlike1216/SonoField-FPGA; branch main.
Workspace E:\Codex-project\AMD-SonoField-FPGA. Active version v1; engineering root v1/.
The user-provided personalized rules govern execution. This file is their project-specific application.

- Preflight local/remote Git, shared/PROJECT_STATE.json, VERSION_STATE.json, plan, decisions, blockers,
  acceptance, AI-chat-memory/INDEX.md and open AI-problem records before changes.
- Continue means the current version. Stages do not create versions. No v2 without explicit user approval.
- Root holds cross-version state and AI coordination. v1 holds runnable sources, tests, scripts,
  dependencies, technical docs, hardware and evidence. Run engineering commands from v1.
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
