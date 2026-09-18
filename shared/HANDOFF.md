# VN1 handoff

Internal stage status: READY_FOR_REVIEW for the digital/model baseline, with board/physical blockers.
Full VN1 acceptance cannot close while exact device identity is missing.

## What changed
128-channel phase engine, separate request/calibration/mask, full-map boundary commit, safety and
32-lane serializer candidate. Directional Python model, planar/concave comparisons, scaling/mismatch
scans, particle sizes/validity flags, phase CSV generation. Added hardware interface, characterization,
bring-up, board audit and from-zero operating guide. Original 12 board references remain unchanged/local.

## Commands and results
- scripts/audit_board.py: 12 files / 101 documented pin candidates; no inferred IO standards.
- scripts/validate.py --output evidence/simulation/vn1_release: PASS.
- Python: 12 tests; Icarus: 1/2/7/32/72/128 channels; integrated serializer/safety/fault and model-map tests.
- XSim 2025.2: core, system, fault and model-map tests PASS.
- TB15: 3 Icarus and 3 XSim 128-channel traces byte-identical, SHA-256
  `63bfad4c5c08fa75d5b2b3b95b37fed7276a5a51052c091b71c9d94544a58054`.
- visualize_field: 12 scaling, 6 geometry, 5 particle scenarios plus CSV maps and two PNG figures.
- Vivado create_project gate: expected exit 1 without documented part; **synthesis not executed**.
- pip check: no broken requirements.

## Failures / limitations
Initial XSim command-line forwarding failure retained in evidence/simulation/vn1/; fixed without changing
assertions. Successful intermediate runs vn1_final/vn1_complete are historical, vn1_release is authoritative.
No target synthesis, place/route, bitstream, PS transport, physical timing, pressure, thermal or levitation tests.
Reproduction status is recorded in evidence/reproducibility/ after clean-checkout execution.

## Decisions needed before next hardware stage
Obtain full FPGA part/package/speed grade and bank VCCO; clarify malformed .const entries.
Validate a 33→132 MHz clock implementation or revise the serial interface through a recorded ADR.
Verify 5 V AHCT input compatibility and buffered clock distribution. Characterize purchased TCT40 batch.
No more emitter count/voltage escalation without failure root cause evidence.

## Next step
Independent review of digital evidence and hardware assumptions, then verified-board synthesis/integration,
then PH0 single-channel electrical measurements and P0 two-transducer standing-wave experiments.
Optional later improvements: measured directivity fit, finite-particle scattering model, finer trap proxy grid,
PS AXI bridge and external watchdog integration. Do not expand main VN1 scope merely to optimize simulation.
