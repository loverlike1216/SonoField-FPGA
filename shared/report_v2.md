# v2 bootstrap review report

PROJECT_ID: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
workspace_path: E:\Codex-project\AMD-SonoField-FPGA
current_branch: main
previous_version: v1 (FROZEN)
active_version / current_version: v2
current_stage: V2_BOOTSTRAP_AND_INHERITED_BASELINE
chat_source_name: SonoField-FPGA
local_HEAD_at_review: e353c16d35da2b430f46ba5b83a5a9a79dd749b7
origin_main_HEAD_at_review: e353c16d35da2b430f46ba5b83a5a9a79dd749b7

The HEAD fields identify the independently reproduced source checkpoint. This report and fresh clone evidence
are committed afterwards; the delivery commit is available from Git history and the user-facing final response.

## IMPLEMENTED
Complete v2 engineering snapshot, unchanged frozen v1, migration inventory, standalone reproduction tools,
documented approval and governance, version-aware Codex interaction capture, BOM import and text exports.

## INHERITED FROM v1
All 212 tracked assets accounted for. Same seven RTL modules, five testbenches, Python acoustic solver,
19 tests, geometry/phase exports, dependencies and technical procedures. Prior evidence retained separately
under v2/evidence/inherited_v1. Only version/path metadata and verification tooling changed.

## NEW IN v2
Explicit freeze/source hashes; independent sparse-clone gate; BOM_MASTER.xlsx/CSV and nine source sheet CSVs;
independent source-cell audit; documented approved hardware/calibration roadmap. No new calibration runtime claimed.

## VALIDATED / REAL TOOL EVIDENCE
- 19 Python tests PASS, Icarus sizes 1/2/7/32/72/128 PASS, all inherited TB01–TB15 checks PASS.
- Vivado 2025.2 XSim compile/elaboration/simulation PASS, including STANDING_WAVE/FOCUS maps at 90/100/115 mm.
- Three 128-channel traces per simulator, each 8250 clocks, match independent Python waveform oracle.
  SHA256: 63bfad4c5c08fa75d5b2b3b95b37fed7276a5a51052c091b71c9d94544a58054.
- Frozen 212-file audit and same v1 Git tree PASS; 12 original board references unchanged.
- Nine interaction exporter tests PASS (version change preserves messages), integrity and secret-pattern checks PASS.
- Source workbook preserved byte-for-byte: 750ad8cabe5279e2218d5d956f8154ae12444b21da76458ee0eb2aa6811c567c.
  Nine sheets, 65 master rows, all nonempty cells and installed-total arithmetic independently checked.
- Evidence: v2/evidence/validation, bootstrap, board_inventory, model and reproducibility.

## REPRODUCIBILITY
V2_STANDALONE_REPRODUCIBILITY: PASS. Fresh local Git clone, sparse checkout without v1 directory,
new venv, dependency lock installation and pip check, full Python/Icarus/XSim rerun, repository/BOM audits,
nine interaction tests. Six model CSVs and 19 coordinate/phase CSVs exactly match canonical LF content.
Same Windows host and installed simulators; this is not an independent OS or physical hardware test.

## HARDWARE STATUS / NOT VALIDATED
Target synthesis BLOCKED_BY_BOARD_FACT. Real Vivado gate exits 1 on missing verified configuration as expected.
Implementation/bitstream, physical drive/receive, ADC, real calibration, thermal/power, levitation: NOT_RUN.
Coarse TOF/fine phase, relative 6DoF solver, environment compensation, common f_work selection and acquisition
RTL are later v2 scope, NOT_IMPLEMENTED in this bootstrap. No PCB fabrication files generated.

## BLOCKING / RISKS / BOARD FACTS FOUND
No unresolved bootstrap gate failures. Whole-project B01/B03: complete FPGA part, VCCO, J4 Pin6 duplicate
D18/E18 and missing J6 V16 connector position remain unresolved. User-selected .const documents N18/33 MHz.
B04: 132 MHz core / 66 MHz shift candidate has simulation evidence only; cable/translator/595 timing unverified.
B05/B06: actual TX/RX batch ratings, dimensions, polarity and acoustic response unmeasured.
External ChatGPT history BLOCKED; no external final Quality Gate is invented.

## BOM / PCB STATUS / TCT40 ASSUMPTIONS
PCB_PROPOSED. BOM is approved input, not electrically validated production data. Old VERSION cell retained
in the immutable workbook and superseded by current user authorization. Price/stock/supplier claims remain
unverified source snapshots. No part substitutions or purchases performed.
Nominal 10 mm body and model piston aperture, 12 mm pitch, 100 mm face gap (90–115 mm adjustable),
128 TX and planned 8 RX. Current inherited simulation explicitly uses configurable c=343 m/s and arbitrary
pressure units; no measured amplitude, humidity model or absolute force claim.
Formal drive policy is 12 V initial, 12–15 V expected starting region, 18 V ceiling, subject to batch qualification.

## AI-PROBLEM STATUS
P-20260919-001/002/003 remain OPEN with original v1 provenance/body hashes. Gaps revalidated for v2;
no historical ChatGPT decision applied across versions. The new formal architecture is a direct user instruction.
No new unresolved bootstrap decision or fabricated cross-agent exchange.

## FILES CHANGED / GIT STATUS
v2 complete engineering tree, root README/AGENTS/shared state and reports, AI interaction records/tools,
BOM/README and .gitignore. No v1 changes; no force push/history rewrite. Freeze commit 6cbf241,
source checkpoint e353c16d35da2b430f46ba5b83a5a9a79dd749b7. Source checkpoint pushed and remote verified. Final report/evidence commit follows.

## NEXT PHYSICAL HARDWARE REQUIRED
Qualified TCT40-10T/10R samples, TC4427A prototype, suitable RX AFE/AD7606B and remote SHT45 test modules,
current-limited bench supply, oscilloscope, independent spacing/mass/dimension measurement. Verify FPGA
marking/schematic/VCCO before board constraints. No procurement or hardware completion is implied.

## NEXT RECOMMENDED STAGE
Stop for bootstrap review, then V2.2 calibration software model under current v2. No automatic v3,
no deeper ADC/PCB implementation in this iteration. Current final response is captured at the next checkpoint.

ACCEPT WITH LIMITATIONS
