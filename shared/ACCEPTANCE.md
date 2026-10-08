# v2 bootstrap acceptance

Scope: V2_BOOTSTRAP_AND_INHERITED_BASELINE only. This does not accept the full self-calibrating hardware platform.

| Gate | Evidence / criterion |
|---|---|
| User authorization | Archived formal v2 instruction sections 1 and 75; ADR-029 |
| Frozen v1 integrity | shared/versions/v1_freeze.json; 212 files unchanged and identical Git tree |
| Complete migration | v2/docs/architecture/migration_inventory.json; no subsystem dropped |
| Python/acoustic geometry | 19 inherited tests; configurable directional model and 128 radiating centers |
| RTL inherited functionality | TB01–TB15, Icarus 1/2/7/32/72/128 and Vivado 2025.2 XSim |
| Repeatability | Three 8250-cycle traces per simulator, same SHA256 and Python waveform oracle |
| Requested/calibration/atomic/safety | Inherited full-map tests, nontrivial calibration and fault cases |
| Independent reproduction | Fresh sparse Git clone without v1 directory, new venv, locked v2 dependencies |
| Model and coordinates | Six model CSVs and 19 coordinate/phase CSVs match canonical LF text exactly |
| BOM import integrity | Unchanged Excel SHA256, nine complete sheets, 65 arithmetic checks, independent cell audit |
| AI interaction provenance | PARTIAL visible messages with hashes; private reasoning excluded; external chat BLOCKED |
| Target synthesis | BLOCKED_BY_BOARD_FACT, no guessed part or constraints |
| Hardware / fabrication | NOT_RUN / PCB_PROPOSED; no calibration or levitation claim |

Current results: shared/PROJECT_STATE.json and shared/report_v2.md. Whole-project blockers remain in BLOCKERS.md.
Future ADC/calibration/pose/temperature work requires later stage verification; no fake PASS or empty runtime modules.

Completed scoped gates: PASS at e353c16d35da2b430f46ba5b83a5a9a79dd749b7. V2_STANDALONE_REPRODUCIBILITY PASS.
Review result: ACCEPT WITH LIMITATIONS for bootstrap only. No full v2 hardware acceptance.


# Current v2 software/digital acceptance

The table above remains bootstrap history. Current scope is SELF_CALIBRATION_SOFTWARE_AND_DIGITAL_SYSTEM.

| Gate | Criterion and evidence |
|---|---|
| Inherited integrity | Same frozen 212-file v1 tree; all inherited tests and source coverage retained |
| Python | 45 tests: 19 inherited + 26 calibration/control tests; full raw pipeline included |
| PL/ADC | CAL-TB01..15 plus fault tests under Icarus and Vivado 2025.2 XSim |
| Raw roundtrip | 1024x8 signed samples, negative corner codes, exact Python->behavioral ADC->RTL->Python identity |
| Sequence | Lower64..127 then upper0..63, four opposite RX paths each; 128 shorter RTL captures |
| Geometry | Ten independent poses with translations, rotations, combined errors, missing paths and outliers |
| Synthetic end-to-end | All 512 paths at 31 sweep frequencies; no injected truth passed to estimators |
| Baseline thresholds | 35 dB: translation norm <0.1 mm; angle norm <0.1 deg; f0 RMSE <80 Hz; phase RMSE <2 deg |
| Reproducibility | Three identical JSON/CSV outputs, three identical Icarus captures, XSim byte equality; 1e-12 numerical repeat tolerance |
| Robustness | Same thresholds at 35/25/15/5 dB; 25 dB exceeds f0 limit; 15/5 dB rejected; failures retained |
| Safety | Safe reset/kill/abort/timeout, no overwrite before ACK, invalid/unreferenced LUT rejected |
| Calibration output | Separate requested/calibration phases; full generated map committed and normal field restored in RTL |
| Standalone | Fresh Git clone without v1 working directory + isolated locked venv + full gate PASS at 9c058fe3b02469a6d36a08e3a7cbedd19076e67b |
| Interface | docs/hardware/PCB_SOFTWARE_INTERFACE.md; register map generated from JSON; no connector guesses |
| Physical and target EDA | NOT_VERIFIED / BLOCKED, explicitly outside this stage's digital acceptance |

Whole-platform result remains REVISE; independent ChatGPT/user review is pending. Stage acceptance
must not be interpreted as physical levitation, absolute force, board timing or synthesis acceptance.

## Current schematic V1 gate — 2026-09-26
Native single sheet,1561components/381texts; PDF and SVG: PASS.3992-pin intent audit and1338 independent channel/return checks: PASS. Save/reopen: PASS. Frozen v1:212/212unchanged. Native strict ERC:0fatal/0error/45warnings, classified and retained.
Electrical release: REVISE. B01/B03/B04, independent watchdog/power qualification, MPN/package and physical AFE/batch gates remain OPEN. No FPGA synthesis, PCB implementation or hardware test executed in this schematic iteration. Earlier software acceptance is a different scope.

## Current v2 gate — CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST

Recorded 2026-10-03 by GPT-6.1 Sol High; criteria are the user's existing formal instruction, not a model-driven revision.

Gate A requires real post-route WNS/WHS >=0 and TNS/THS=0 plus full functional regression, preserving all existing semantics and throughput. Round2 real routed results: WNS -4.515 ns,TNS -6007.936 ns,WHS +0.070 ns,THS0.000 ns. Gate A FAIL. Gate B additionally requires verified physical UART route, real PS firmware, PC↔PS↔AXI↔PL exchange,1000PING/PONG, version/status/read/safe-write/disconnect evidence and no external acoustic output. Gate B NOT_RUN.

Scope result remains REVISE pending timing closure and real transport evidence. Model-transition continuity is a separate administrative check and never accepts the physical platform. Current recovery result: v2/evidence/core_timing_real_loop/recovery_20261003/summary.json.


Current validation update — 2026-10-03, GPT-6.1 Sol High: fixed-source recovery PASS,114Python tests,3696TRAP_VALID frames,threeIcarus/oneVivadoXSim matching canonical hashes,calibration/ADC and frozen-parent gates. Saved-preview defect fixed and failure retained. Routed Gate A remains FAIL; physical PS/PL and acoustic operation NOT_RUN. Acceptance thresholds unchanged.


## Current pre-PCB contract — 2026-10-03

Current model: GPT-6.1 Sol High. Original Acceptance thresholds unchanged. Actual internal timing/complete simulation gates PASS as recorded in v2/evidence/pre_pcb_board_ready/summary.json. Full PRE_PCB_BOARD_READY remains NO because electrical/PS/real transport/map/GUI conditions are unverified. External review PENDING; no full-project ACCEPT.

## DDR detection continuation — 2026-10-04

Additional DDR evidence gate from direct user requirement; no existing Acceptance threshold changed. Official component decode can be confirmed independently;512MiB/32bit must remain CANDIDATE until board-matched PS/reference/topology crossvalidation succeeds. Reset-value DDRC width is insufficient. Rated800MHz/1600MT/s/1.35V do not establish actual board clock/power. Inspection is complete; whole platform remains REVISE. Model: GPT-6.1 Sol High. Active v2 and existing Stage unchanged. Current read-only native Vivado2025.2 scan confirms XC7Z020 IDCODE0x23727093; Micron public decoder identifies D9PSK as MT41K128M16JT-125 IT:K. Photo shows two2Gb x16 devices, but512MiB/32bit remain CANDIDATE. XSDB/AP0 reads DDRC_CTRL0x00000200 andCTRL_REG1 0x0000003E, both documented reset values; controller reset not released, so32bit default field is not board topology proof. No CPU halt/reset/init,DDR memory access,download,COM,GPIO orPCB operation. Original Vivado GUI preserved. Report: parameter_detection/20261004_ddr/RESULT.md; candidate: v2/config/ddr_candidate.json. Existing core115tests/132MHz timing retain their2026-10-03 source/date; not rerun today.


## Current AX7020 v5 organization gate — 2026-10-08

The preceding criteria/results retain historical version scope. New user-authorized scope: safe organization and available AX7020 v5 baseline, without lowering inherited algorithm/protocol tests. Required:115 Python tests/full motion4runs3696frames/waveform+calibration/C+AXI/safety+equivalence pass before and after archival; isolated v5-only run and exact source/behavior hashes; native documented-part OOC synthesis/reopen; historical hashes and recoverable commit; state/search scope and Git sync. Evidence: v5/evidence/BASELINE_VALIDATION.md and baseline/COMPARISON.json. Available gates PASS. Independent tool cross-check Icarus+XSim, no external AI review fabricated. Physical PS/IO/UART/route/levitation NOT_VERIFIED; full-project ACCEPT forbidden. Organization ACCEPT WITH LIMITATIONS; whole platform REVISE.
