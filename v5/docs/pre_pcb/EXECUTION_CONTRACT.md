# v5 pre-PCB execution contract

Goal: S0-S7 offline software/RTL/algorithm/three-PCB preparation in existing v5.
Inputs: actual user full-system instruction and two sketches; current repository facts.
Architecture: preserve 128TX/8RX/32×4/8bit independent requested/calibration/common clock/atomic commit/50Hz.
Allowed: additive supervisory RTL, explicit PS/PL platform candidate, sensor/temperature/sparse solver,
negotiated optional protocol extensions, runtime path editor and tests, new working BOM and evidence.
Do not change: original goldens/thresholds, formal AD7606B, RX unknown, NU40C10T identity, frozen history.
Existing inherited core files remain fixed unless an explicit extension adapter is documented and reviewed.
Non-goals: version upgrade/main merge, board init/program/DDR access, physical acoustic acceptance, CAD/Gerber/orders.
Validation: original 115 tests+3696×4, new unit/fault tests, C host execution, two real simulators,
Vivado2025.2 PS7 candidate build/OOC route evidence, independent clean checkout/environment.
Evidence: actual logs/hashes/source commits/provenance, retain failures. No model self-certification.
Rollback: drop this development branch before merge; original migration candidate and physical sandbox persist.
Done: all feasible offline gates pass, physical holds recorded, S7 state/checkpoint and normal push verified.
