# v1 organization report

PROJECT_ID: SONOFIELD_FPGA; project_name: SonoField-FPGA.
Repository: https://github.com/loverlike1216/SonoField-FPGA.git.
Workspace: E:\Codex-project\AMD-SonoField-FPGA. Branch: main. Active version: v1.
Stage: V1_LAYOUT_AND_GOVERNANCE.

## Implemented
Single v1 engineering tree; root shared/AI governance; current-version metadata and run paths updated.
User-approved cleanup preserves functioning source, current hardware geometry and Git commit history.

## Validation / real tools
Baseline/current 19 Python tests, complete Icarus and Vivado 2025.2 XSim regression PASS.
RTL/TB/tests and 12 board references unchanged. Six model and 19 coordinate/phase CSVs match;
three repeat traces per simulator retain identical hash. New evidence in v1/evidence.
Fresh local clone of 0b257de with new venv PASS. Both simulators, all Python tests, six model CSVs
and 19 coordinate/phase CSVs reproduced on the same Windows host. No second OS/physical board implied.

## Not validated / blocking / risks
External ChatGPT source SonoField-FPGA is named but unreadable; no original messages or decision invented.
Target part/VCCO/pin defects, output serializer physical timing and new transducer qualification remain open.
Synthesis, implementation, driver hardware, physical levitation and 50 mg capacity are not validated.

## Board / transducer facts
Original root Zynq7020 folder is preserved; constrain source declares N18 / 33 MHz. No complete part supplied.
Current transducer is nominal 10 mm / 40 kHz; exact continuous excitation, capacitance and mounting offset unknown.

## Next stage
Review scoped directory result; qualify actual board/transducer/interface before target integration and PH0.
Organization completion does not approve whole-platform hardware acceptance.

## Result (organization scope only)
ACCEPT WITH LIMITATIONS. Requested local/current GitHub layout is v1-only, with complete runnable source
and newly generated evidence. External ChatGPT import is BLOCKED; hardware acceptance is not granted.
See shared/HANDOFF.md and the machine-readable state for the next required inputs.

## Observable interaction configuration — 2026-09-20
Actual Codex transcript and tool-call provenance exported under AI-interaction-memory, coverage PARTIAL.
Eight capture tests plus integrity/secret-pattern and unchanged-source repository checks PASS.
No hidden reasoning, fabricated external history or automatic background recording claimed.
See shared/HANDOFF.md and AI-interaction-memory/README.md for checkpoint commands and limits.
