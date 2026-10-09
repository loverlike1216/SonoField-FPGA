# Execution contract — v2 motion digital stage

Authority: current user continuation and attached stage instruction, preserved alongside this file.
Policy: 2026-09-27-r1; Codex engineering window; Work OFF. No independent acceptance inferred.

Goal: commanded trap motion from desktop UI through calibrated model, bounded planning,
Controller register writes, buffered RTL, real simulation ACK and safety verification.
Reuse the calibrated acoustic model, 128-channel phase bank, carrier and serializer.
Preserve separate requested/calibration phase and existing static-map API.

Allowed: v2/software, rtl, tb, tests, config, scripts; engineering state and evidence.
User sections 64/67 additionally authorize six v2/docs/motion documents and interaction records.
Do not modify frozen v1, PCB, physical pins, XDC, project version, repository visibility,
release/deployment, or unrelated Work narrative/memory. No paid service or Work launch.

Validation: 37 motion software cases plus regressions; 10 motion RTL cases on Icarus and
Vivado 2025.2 XSim; GUI end-to-end demonstration; three identical path/map/ACK runs;
production cadence test; failure injection; frozen-parent and standalone-v2 checks.
Simulation acceleration must be disclosed. Physical motion, PS runtime, board timing and
mass support remain NOT_VERIFIED. Prototype BoardTransport must fail closed.

Rollback: additive modules and reviewed commit; no history rewrite or deletion of user data.
Done when the digital gate has real archived evidence and local/remote commits match.
Return to independent Chat/user review; stop before PCB work, camera control or v3.
