# Hardware/source conflict disposition

| Source | Purpose | Valid scope | Decision/status |
|---|---|---|---|
| v5/config/hardware_parts.json TCT40 TX/RX | Preserved inherited digital fixture | Historical/simulation component assumptions; no purchasing authority | Byte-identical; current TX is NU40C10T and actual RX MPN UNKNOWN |
| v5/config/acoustic_baseline.json / visualize_field.py TCT40 approximation | Preserved numerical model/reference | Synthetic directional approximation; no measured NU40 parameters | Do not rename parameters or change golden behavior to imply measured equivalence |
| v5/hardware/integration_candidates/20261009/current_hardware_scope.json | Current hardware scope | AX7020 + NU40 + three boards + independent upper/lower power | Authoritative design input, unqualified electrical implementation |
| Formal AD7606BBSTZ-RL vs working BOM C-16 | Production versus recommendation | AD7606B remains formal; C-16 only isolated candidate | P-20261008-001 OPEN; independent review + user approval required |
| ALINX V2.0 schematic/XSA vs actual AX701020.3.0 | Vendor reference versus observed revision | Candidate preset/pin/DDR only | P-20261009-001 OPEN; no PS init/unknown RAM access |
| Previous shared v2 blockers/ENGINEERING_STATE | Old hardware stage | HISTORICAL_READ_ONLY | Current state rebuilt as v5; historical decisions retained verbatim |
| board_clock_candidate.sv low-level old defaults | Inherited unused candidate | Not included in OOC production source list, not AX7020 clock fact |132MHz internal target preserved; physical clocks remain unqualified |

The 128TX/8RX/32×4 architecture, formal ADC, protocol/registers/calibration/motion/safety/goldens and acceptance are unchanged. No new formal Problem is necessary for path organization: the two current hardware Problems already cover the substantive pending decisions.
