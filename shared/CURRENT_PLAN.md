# v1 execution contract — layout and governance

## Goal
Organize the existing project locally and on GitHub as a single active v1. No version upgrade.

## Inputs / authorization
User explicitly requested the new personalized rules, stated 目前还是v1, and subsequently directed
removal of obsolete version records after integrity validation. Chat Source: SonoField-FPGA.
Baseline commit ada1b2062756a2b852ed643a6eaa04fdc746323b; clean main matched remote before work.

## Scope / architecture / allowed changes
Root: README, AGENTS, CHANGELOG, shared, AI-chat-memory and AI-problem.
v1: RTL, TB, software, tests, config, constraints, scripts, requirements, docs, hardware and evidence.
Remove obsolete reports, evidence directories and migration snapshots from current tree only after fresh
validation. Preserve existing Git commits. Keep stable module names and functional behavior.

## Do not change / non-goals
No v2, no new hardware claims, no part/pin/rating guesses, no bitstream. Preserve original Zynq7020
location and file hashes. No fabricated ChatGPT transcript or Decision. No release/visibility change.

## Dependencies / risks
Python 3.10, locked dependencies, Icarus and Vivado 2025.2. Root-to-v1 path boundaries require correction.
ChatGPT history access is blocked; this does not block file organization. Hardware blockers remain open.

## Validation / evidence
Before: 19 Python tests passed. After: complete Python/Icarus/XSim regression, independent waveform oracle,
repeat trace hashes, unchanged RTL/TB bytes, six model CSVs and 19 coordinate/phase CSVs equal to baseline,
12 board references unchanged, required documents/links/state/problem hashes correct, clean checkout/new venv.
Capture real commands/exit codes in v1/evidence. Remove obsolete current-tree records after these gates.

## Rollback
Revert the scoped organization commits using normal Git history; never force push or erase old commits.

## Done when
Only v1 current layout remains locally and remotely, documented commands execute, new evidence passes,
state/hand-off complete, secret/license check passes, Git pushed and remote commit confirmed.

## Progress
Source relocated and tool paths updated. Full Python/Icarus/XSim regression PASS; model/coordinate equality and source/board integrity PASS.
Obsolete current-tree records and obsolete local clone caches removed under user authorization.
Repository audit PASS. Fresh checkout/new-venv reproduction at 0b257de PASS: complete digital gate, six model CSVs and 19 coordinate/phase CSVs identical.
All requested local organization work complete. Final evidence/state commit and remote synchronization follow.
