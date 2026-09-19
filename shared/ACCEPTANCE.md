# VN1 acceptance matrix — current 10 mm geometry revision

Automated evidence is ready for independent review. Overall VN1 acceptance remains external.

| # | User criterion | Evidence/status |
|---:|---|---|
| 1 | Clean repository | Classified folders, ignored build/tool outputs; hygiene audit |
| 2 | All Zynq references inspected | 12/12 files, manifest and board_facts.md |
| 3 | Exact device/clock facts | **PARTIAL / BLOCKING**: 33 MHz/N18 per user-selected .const; complete part still missing |
| 4 | TCT40 baseline documented | docs/hardware/tct40_baseline.md, characterization procedure |
| 5 | Python acoustic model | software/acoustic_model, analytic unit tests |
| 6 | Configurable geometry | config/acoustic_baseline.json |
| 6a | User's radiating-face geometry | 128 centers, 12 mm pitch, z=+/-g/2, nominal g=100 mm, range 90..115 mm; dedicated 7-test suite |
| 7 | 2/32/72/128 geometries | Also 8/16; identity tests and field output |
| 8 | RTL up to 128 | Icarus sizes 1/2/7/32/72/128 |
| 9 | One deterministic timebase | tb_core + analytic Python oracle |
| 10 | Programmable phase | Requested map transactions and model-map integration |
| 11 | Independent calibration | Separate registers, columns and nontrivial calibration test |
| 12 | Atomic updates | Completeness bitmap, boundary ACK, entire-map checking |
| 13 | Safe reset/disable | **DIGITAL SIMULATION PASS**, physical interlock validation pending |
| 14 | Automated RTL tests | TB01–TB13 in Icarus/XSim, fault cases |
| 15 | Python-vs-RTL | TB14 and model-generated vector tests |
| 16 | Vivado synthesis if sufficient board data | **BLOCKED** by complete part; Vivado gate rejects missing configuration |
| 17 | No invented pins/results | No XDC/bitstream; no hardware PASS |
| 18 | PCB/driver interface | docs/hardware/interface.md |
| 19 | Bring-up plan | docs/experiments/bringup.md |
| 20 | Explicit blockers | shared/BLOCKERS.md |

TB15: three repeat traces per simulator, byte-identical. This satisfies the defined digital determinism
check, not analog drift or measured field repeatability. Final board synthesis/timing and physical acceptance
must remain open. No self-issued whole-project final acceptance is recorded.

Historical REPRODUCIBILITY_CHECK: fresh local clone at 6b29f8b passed the prior 16 mm revision.
Current geometry evidence is under evidence/geometry_10mm; do not reuse historical hashes as its acceptance.
The selected 128-position design supersedes the former 72-emitter demonstration requirement by explicit user instruction.

Current REPRODUCIBILITY_CHECK: clean local clone at a01629c and new venv PASS.
Complete digital gate, six model CSVs and 19 coordinate/phase CSVs reproduced on the same Windows host.
Evidence: evidence/geometry_10mm/reproducibility/summary.json and validation/.
