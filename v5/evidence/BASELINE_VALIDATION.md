# AX7020 v5 baseline validation — 2026-10-08

Current model: GPT-6.1 Sol High (user-declared). Scope: directory integrity, independent digital/software operation and documented-part OOC synthesis; not whole-platform acceptance.

| Actual gate | BEFORE_MIGRATION | AFTER_MIGRATION | Standalone without old versions/shared |
|---|---|---|---|
| Full orchestrator | PASS | PASS | PASS |
| Python unit tests | 115/115 | 115/115 | 115/115 |
| GUI-driven motion | 3696 frames ×4 | 3696 frames ×4 | 3696 frames ×4 |
| Fixed input hashes | 3 Icarus +1 XSim identical | Identical to before | Identical to before |
| Waveform/Python oracle, calibration/raw ADC, safety/regression | PASS | PASS | PASS |
| C service/protocol, AXI bridge/system/smoke PL simulation | PASS | PASS | PASS |
| Queue/scheduler golden comparison, serializer throughput, safe array interface | PASS in both tools | PASS in both tools | PASS in both tools |
| Phase/burst exact-cycle equivalence | PASS in both tools | PASS in both tools | PASS in both tools |
| Source and inherited-copy hash integrity | PASS | Identical | Identical |

Summaries/logs: baseline/before_migration_complete, baseline/after_migration, baseline/standalone; canonical COMPARISON.json. Calibration raw JSON hashes differ only in git_commit(base vs recovery commit); CALIBRATION_PROVENANCE_DIFF.json preserves actual raw hashes/commits, checks those exact expected commits and exact equality of every other field. Numerical calibration/LUT/quality/ADC/waveform results remain identical; raw JSON byte identity is not claimed across different provenance commits. The standalone workspace contains only a v5 copy, no v1/v2/v3/shared/archive at its parent. It uses the declared external Python interpreter and tool binaries; this proves source/data path independence, not a fresh dependency installation or another computer.

Earlier failures preserved: before_migration missing motion_gate.py; before_migration_repaired missing an implicit synthetic calibration input (72 tests ran, FAIL). Dependency RCA is shared/organization/DEPENDENCY_RCA.md. Repaired by explicit copies/local input paths, never dropping assertions/tests. No previous failed result overwritten.

Native Vivado2025.2: scripts/create_project.tcl executed successfully for the manufacturer-documented xc7z020clg400-2, top sono_axi_system; own RTL source list in synthesis/loaded_sources.txt. OOC synthesis:7219 LUT,17918 registers,4 RAMB36; synthesized internal timing WNS+0.994ns/WHS+0.157ns at inherited132MHz target. These are pre-route values. Report also has2324 no-input-delay and256 no-output-delay warnings for OOC boundary ports; they are not waived or represented as constrained physical IO. Native project reopen proof is synthesis/project_reopen.log.

Full-board placement/routing, reviewed AX7020 production XDC/PS preset, bitstream, UART/PS-PL runtime and acoustic hardware: NOT_RUN/NOT_VERIFIED. Missing revision-matched integration inputs make a board implementation inapplicable here. No false paths, guessed IO or removed constraints used to fabricate a Timing PASS. Native build logs/report evidence remain separate from simulation results.

Historical integrity: 3343 inventoried non-cache original files retain exact byte hashes, including untracked/private originals; caches/dependencies remain in place and are not claimed fully audited. Recovery commit: 4cd42172dbbb1b4a2fc45d8f0d33d28f2efcc0fe. Archive snapshot count:15; source moves0/deletions0.

Available digital/organization gates PASS; physical acceptance remains blocked. External ChatGPT review/history access BLOCKED, observable Codex capture PARTIAL. No independent AI review invented.
