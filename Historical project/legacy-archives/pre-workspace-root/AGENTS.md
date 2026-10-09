# SonoField-FPGA current engineering scope

PROJECT_ID SONOFIELD_FPGA. Repository https://github.com/loverlike1216/SonoField-FPGA.git. Active version v5, target ALINX AX7020, authoritative Vivado2025.2. Current model record GPT-6.1 Sol High (user-declared). Explicit user attachment e8213cac-ae60-4eee-bb3e-6461d16eaf66 authorizes v5 and supersedes prior active-v2 restrictions. No v4. Historical model records must retain provenance.

## Recovery and default search

Read README, shared/PROJECT_STATE.*, VERSION_STATE.json, CONTEXT_CHECKPOINT.*, CURRENT_PLAN, current DECISIONS/BLOCKERS/ACCEPTANCE and current v5 evidence before changes. Default implementation/search/build scope: v5/, shared/, root README/AGENTS, current valid AI-problem decision and necessary current AI-interaction records. Do not routinely scan archive/, v1/, v2/, v3/, old large logs or full historical chats. Targeted historical access only when user requests, regression/comparison, decision provenance, restoration or evidence conflict requires it. archive is frozen by default; originals kept in place are equally historical read-only.

## Invariants and boundaries

All new implementation belongs in v5. Preserve stable names/interfaces,128channels/8bit/common timebase/requested-calibration separation/atomic commit/safety/protocol/registers/motion cadence. Geometry is10mm candidate emitters,12mm radiating-face-center pitch, nominal100mm face gap configurable90–115mm, opposed8×8, geometric-center origin. Preserve algorithm behavior and inherited acceptance; no skipped tests/relaxed thresholds/fake results. v1/v2 frozen, v3 paused local draft; do not edit them or invent v4. Continue never implies another version. New versions need explicit user approval and copy-based migration.

v5 must load its own RTL/config/fixtures/XDC. Generic old source may be inherited only by reviewed copy and recorded hash; never silently read old worktrees. Do not carry Robei pins, N18 clock, COM4, FTDI IDs or512MiB candidates into AX7020 physical facts. Official reference differs from actual revision verification. Current132MHz is an internal design target. Only OOC clock constraint exists; physical deployment blocked until actual part/revision/VCCO/PS DDR/clock/preset/XSA/BSP/IO/external timing are verified. This organization task permits no program download, unknown GPIO, driver/boot/reset changes or PCB editing.

## Execution, evidence and persistence

Use pwsh7 on Windows, not powershell.exe5.1 except explicit necessity. Use real tool output; distinguish implementation/test/simulation/synthesis/routed timing/hardware. Full digital baseline entry v5/scripts/run_baseline.ps1;115 Python tests and four3696-frame GUI/RTL runs plus existing waveform/calibration/C/AXI/safety gates must pass. No previous PASS becomes current physical verification. Keep failed evidence.

No force push,history rewrite,blanket clean,reset--hard or unreviewed deletion/move. Preserve untracked user assets; stage only reviewed changes. Public GitHub requires secret/privacy scan; local_raw,private docs,caches/builds and untracked paused drafts are not published blindly. Explicit current source/provenance changes use normal commits/push and remote verification.

## Current authorization — 2026-10-09

User attachment 4b78522d-e640-448c-8788-c916d293b560 supersedes the earlier organization-only task boundary for this v5 iteration. Read-only AX7020 detection, official configuration review, isolated board candidates, BOM working revision and schematic preparation are authorized. Volatile PL/PS testing remains conditional on matched device/revision/configuration, safe boot/external state and verified memory ownership. Actual read-only scan found an already configured PL and both CPUs running; do not overwrite unknown running contents. No permanent storage writes, driver changes, boot/jumper changes, unknown GPIO, fabrication or formal ADC substitution. Preserve original submitted BOM and core/inherited acceptance. Three required PCBs; remote environment board optional. Actual photo/user PCB revision is AX701020.3.0. Public vendor V2.0 schematic and reference XSA are not yet revision-matched. Current task stage and findings are in shared/CONTEXT_CHECKPOINT.*.

Persist observable user/Codex messages and key tool flows in AI-interaction-memory with source IDs/hashes/PARTIAL limits; never hidden reasoning. External ChatGPT history is BLOCKED unless a real reader/export is available; do not fabricate ChatGPT decisions/review. Major decisions use AI-problem with source/hash/version checks, ordinary implementation defects are handled directly. No subagents requested for this task. After meaningful changes reconcile current state/plan/blockers/decisions/acceptance and create CONTEXT_CHECKPOINT with real evidence and commits. Current scoped organization acceptance does not accept the hardware platform.
