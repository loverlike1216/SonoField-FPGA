# VN1 iteration report

| Identity | Value |
|---|---|
| PROJECT_ID | SONOFIELD_FPGA |
| project_name | SonoField-FPGA |
| repository | https://github.com/loverlike1216/SonoField-FPGA.git |
| workspace_path | E:\Codex-project\AMD-SonoField-FPGA |
| current_branch | main |
| current_version | VN1 |
| current_stage | DIGITAL_PHASED_ARRAY_BASELINE_AND_TCT40_HARDWARE_ARCHITECTURE |

## IMPLEMENTED
128-channel digital core, 8-bit common phase reference, independently stored calibration, per-channel mask,
complete shadow-map validation, atomic boundary commit, digital reset/disable/overrun protection and
32-lane serializer candidate. Python directional field solver, standing/focus maps, planar/concave geometry,
2/8/16/32/72/128 scaling, phase/amplitude mismatch scenarios, particle mass/dimension/density model.
Board audit, modular PCB/driver interface, TCT40 measurement templates and staged hardware bring-up guide.

## VALIDATED
12 Python tests. TB01–TB15 digital coverage; Icarus channel counts 1/2/7/32/72/128. Complete system
serializer/mapping/safety tests and Python-generated acoustic-map integration. Three repeated 128-channel
traces under each of Icarus and Vivado XSim agree byte-for-byte. Each full trace checks 1,056,000 channel-cycles.

## REAL TOOL EVIDENCE
`evidence/simulation/vn1_release/summary.json` and raw logs: PASS, actual commands/exit codes recorded.
`evidence/model/vn1/`: generated tables, assumptions and plots.
`evidence/preflight/`: all 12 board files inventoried with SHA-256; 101 verbatim pin candidates.
`evidence/synthesis/board_gate.log`: real Vivado 2025.2 invocation, expected missing-facts rejection.
`evidence/reproducibility/summary.json`: **PASS**, fresh local clone of source checkpoint 6b29f8b,
new venv, full dual-simulator tests and matching model CSV content hashes. Repeated raw tool logs are preserved.
`evidence/hygiene/`: structure/link/source-hash checks PASS; all 12 user board originals unchanged.

## NOT VALIDATED
Board-target synthesis, implementation/timing/DRC, bitstream, physical FPGA outputs, actual PS communication,
driver electrical/thermal behaviour, purchased transducer calibration, acoustic pressure/force, mechanical
working volume and any real levitation (including 5/10/25/50 mg).

## BLOCKING
Full FPGA ordering code/package/speed grade, bank VCCO/IO standard, duplicate J4 Pin6 and missing J6
number within authoritative .const. These are still absent after adopting user-selected source precedence.
Serializer PLL and electrical distribution/level compatibility require board verification before PCB freeze.

## RISKS
132 MHz / 32-lane is a simulated candidate. Physical signal integrity and interlock behaviour are unmeasured.
Clock-stop safety requires external hardware. Piston directivity, no coupling and illustrative mismatch/air
properties limit acoustic estimates. Large EPS particles invalidate the small-particle potential approximation.
The model does not convert normalized pressure into a supported mass.

## BOARD FACTS FOUND
Robei Zynq-7020 family; per user's instruction hardware.const gives clock N18 / 33 MHz. GPIO/peripheral
pin candidates are exported exactly from `.const`. Complete part and IO voltage are unknown. Connector
5 V supply labels do not establish FPGA 5 V compatibility. No pin constraints were fabricated.

## TCT40 ASSUMPTIONS
40 kHz, approximately 16 mm, roughly 2–2.5 nF class. Reference SPL values and ambiguous 80 V maximum
are not purchased-batch measurements or continuous-drive limits. Initial characterized range is planned
10→12→16→~20 Vpp, contingent on waveform/current/temperature. No measurements are filled in yet.

## NEXT PHYSICAL HARDWARE REQUIRED
Verified board documentation, at least two characterized TCT40-16T, a TCT40-16R/suitable receiver,
reviewed current-limited two-channel driver, suitable oscilloscope/differential probing, LCR meter,
calipers, calibrated mass scale, temperature measurement and adjustable opposed fixture.

## NEXT STAGE
Resolve board facts → actual target synthesis/integration and physical digital timing checks → PH0 single
transducer characterization → P0 two-emitter standing-wave experiment. Review the existing evidence
before proceeding. The digital/model portion is READY_FOR_REVIEW; whole-project final acceptance is external.

## Result
REVISE

Reason: mandatory exact-device acceptance remains unresolved. Digital tests passing does not close this
hardware fact gap, and no physical levitation claim is made.
