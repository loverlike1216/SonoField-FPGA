# DDR identification and PS configuration preflight

Project SONOFIELD_FPGA; active v2; unchanged Stage TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE. Date 2026-10-04 Asia/Shanghai. Current model GPT-6.1 Sol High, user-declared; exact runtime variant not exposed. Source Codex thread01a0b538-9430-7561-9ba4-623f57501f43. Coverage PARTIAL: curated observable execution, not private reasoning or a full raw tool transcript.

## Trigger and reviewed input

Direct user DDR instruction: two Micron D9PSK devices;512MB/32bit candidate; crossverify PS preset/BD/XSA/HDF/ps7_init/Robei reference and actual config before confirmation. User-designated directory parameter_detection. Current repository preflight and new personalized AGENTS/checkpoint rules reviewed first. Previous source86b56b20433fb3ddc2d35d4101b1bac6ab312cd8; main origin fetched, zero divergence at preflight. Existing current-core validation commit9936a737c45bf61f1908863a94f6374c6b5c828c is historical, not rerun in this task.

## Actual tool sequence

1. PowerShell7.6.5 CLI: current Git/identity/state/version/checkpoint/plan/decisions/blockers/acceptance/indexes and reference inventory. Board photo inspected from existing user original; public reference and original hash retained; GPS-bearing image stayed local.
2. Official Micron decoder and part page inspected. Their publicly exposed form/specification routes returned actual JSON200: D9PSK→MT41K128M16JT-125 IT:K,2Gb/x16/1.35V/800MHz/1600MTPS/96ball. Public API response paths came from actual public site attributes; no inferred authentication API or credential access. Actual response contents and source URLs saved in parameter_detection/20261004_ddr/micron_*.json.
3. Read installed XSDB2025.2 help for targets/mrd/AP0. Started hidden localhost-only hw_server with `-stcp:127.0.0.1:3121 -p0`, no GDB ports. Original user Vivado GUI PID53284 was preserved.
4. Executed read_ddrc.tcl through xsdb.bat. Exactly one APU required; read-only documented controller addressesF8006000/F8006060 viaAP0. Actual values512/62 (hex200/3E), both documented reset values. BothCortex-A9 targetsRunning before/after. Native startup path warning retained. No CPU stop/reset/init,force,mwr,DDR RAM access or program download.
5. Native Vivado2025.2 batch read_jtag.tcl scanned two-device chain: ARM DAP4BA00477,XC7Z02023727093,DONE0. Batch exit0. JTAG clock15MHz is not a PLclock. Original GUI unchanged. Public log cable identifiers redacted; raw logs ignored.
6. Bounded rg reference searches across nine specified local roots: no matching project/BD/XSA/HDF/ps7_init/preset; rgexit1 recorded as no matches. Robei5.0.2 installation identified. Generic AMD templates excluded as non-board evidence. Current GUI journal has zero project/BD-open commands; no direct GUI Tcl capability, so no active-GUI config read claimed.
7. Persisted detection report/scripts/candidate classification/current state/guide and checkpoint. Canonical result parameter_detection/20261004_ddr/summary.json; v2/evidence/parameter_detection/20261004/summary.json is only an index. Hardware and Tcl safety/candidate status, message hashes and staged public privacy checks precede normal Git synchronization; outcomes recorded in audit.json/delivery_sync.json. GitHub publication is to the user's pre-existing authorized repository, not a new repository or Release.

## Decision impact and execution boundary

Official component code is confirmed. Board512MiB/32bit remain CANDIDATE: reset-default width is insufficient proof. No fabricated preset or memory map added. Actual board memory clock/voltage/ranks remain unknown. Core sources/RTL/PCB/frozen history untouched. B01 prior full-part user confirmation retained; B03 physical platform/routing gaps still open. Real transport and whole-platform Quality Gate remain blocked. No external ChatGPT decision/review is invented; history access remains BLOCKED.

## Recovery

Read parameter_detection/20261004_ddr/RESULT.md and shared/CONTEXT_CHECKPOINT before continuing. Obtain matching manufacturer/reference data in parameter_detection/inputs, crossverify and review before any platform initialization. Current task stops at read-only inspection. Results HTML provides a human-readable offline view; it does not claim to control Vivado GUI.
