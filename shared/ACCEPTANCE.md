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
