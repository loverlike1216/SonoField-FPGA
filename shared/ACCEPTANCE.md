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
