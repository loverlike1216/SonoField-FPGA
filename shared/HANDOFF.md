# v2 self-calibration handoff

## Goal and inputs
Complete user-authorized v2 software/digital stage; archived v2_self_calibration instruction,
BOM/configs, board facts, current AGENTS rules. Preserve frozen v1; no new version or PCB.

## Changes and tests
Integrated ADC initialization/readback/acquisition, bounded scan/capture/ACK, host frequency/map
control, geometry/response/phase/LUT pipeline, safety corrections and interface contract.
45 Python tests, inherited and CAL-TB01..15 Icarus/XSim PASS. Fresh clone excludes v1 worktree;
locked new venv, six model CSVs, 19 coordinate CSVs, BOM/repository audit and 10 transcript tests PASS.
212 frozen files and parent tree unchanged. Source 9c058fe3b02469a6d36a08e3a7cbedd19076e67b pushed and verified.

## Evidence
Report: shared/report_v2.md. Local validation: v2/evidence/self_calibration_stage/validation_frequency.
Fresh reproduction: v2/evidence/self_calibration_stage/reproducibility_review.
Cross-environment JSON records exact calibration payload/CSV and ADC binary identity.

## Failures and limitations
Initial reproduction failed raw source hashes after Git newline normalization; preserve its evidence.
Current source hashing explicitly uses UTF-8 LF; this does not change frozen-parent byte checks.
25 dB f0 fails the fixed accuracy threshold; 15/5 dB datasets rejected. No threshold relaxation.
Board part/VCCO/pins, physical timing, RX references and all physical measurements remain blocked.
External ChatGPT inaccessible; no fabricated decision or hardware result.

## Next action
STOP for user/ChatGPT independent review. No automatic PCB implementation or v3.
Optional future work requires user direction and physical prerequisites; see BLOCKERS.md.
