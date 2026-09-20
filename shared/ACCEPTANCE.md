# v1 acceptance matrix — current 10 mm geometry revision

Automated evidence is ready for independent review. Overall v1 acceptance remains external.

| # | User criterion | Evidence/status |
|---:|---|---|
| 1 | Clean repository | Classified folders, ignored build/tool outputs; hygiene audit |
| 2 | All Zynq references inspected | 12/12 originally inspected; current v1/evidence/board_inventory hashes and v1/docs/hardware/board_facts.md |
| 3 | Exact device/clock facts | **PARTIAL / BLOCKING**: 33 MHz/N18 per user-selected .const; complete part still missing |
| 4 | TCT40 baseline documented | v1/docs/hardware/tct40_baseline.md, characterization procedure |
| 5 | Python acoustic model | v1/software/acoustic_model, analytic unit tests |
| 6 | Configurable geometry | v1/config/acoustic_baseline.json |
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
| 18 | PCB/driver interface | v1/docs/hardware/interface.md |
| 19 | Bring-up plan | v1/docs/experiments/bringup.md |
| 20 | Explicit blockers | shared/BLOCKERS.md |

TB15: three repeat traces per simulator, byte-identical. This satisfies the defined digital determinism
check, not analog drift or measured field repeatability. Final board synthesis/timing and physical acceptance
must remain open. No self-issued whole-project final acceptance is recorded.


## Current-layout review
Only v1 is active. Root governance, AI source status, unique Problem IDs/body hashes and working
root-to-v1 paths are required. Current digital evidence: v1/evidence/validation/summary.json.
Fresh-checkout reproduction: v1/evidence/reproducibility/summary.json: PASS at source 0b257de.
Organization acceptance is scoped separately from whole-platform hardware acceptance.

Layout gate: PASS. Active engineering version directories: v1 only; historical wording may occur in quoted interaction records. Chat history synchronization: BLOCKED, accurately reported.

Interaction capture gate: real source identity verified, visible-message allowlist, public redaction, hashes,
repeat sync and tamper tests PASS. Historic wording is preserved only in transcript quotations.
Coverage is PARTIAL; external ChatGPT history remains BLOCKED.
