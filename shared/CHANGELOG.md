# Changelog

## VN1 — 2026-09-19

- Established user-selected repository context and audited all supplied board references.
- Applied user's `.const` source precedence; documented 33 MHz/N18 without guessing full device/VCCO.
- Implemented common fractional phase reference, complete-map shadow/active commit, calibration and masks.
- Added digital serializer/safety integration, bandwidth fail-closed guard and Python/RTL tests.
- Added directional acoustic model, planar/cap comparison, mismatch/count studies and particle validity checks.
- Ran Icarus and Vivado 2025.2 XSim with identical repeat traces; target synthesis remains explicitly blocked.
- Added characterization schemas, modular PCB interface, experimental roadmap and reproduction instructions.
- Retained initial launcher failure and successive verification evidence. No fabricated hardware results or XDC.
- Fresh local clone of 6b29f8b plus new venv passed complete dual-simulator validation and model CSV reproduction.
- Preserved the earlier wrong-checkpoint reproduction failure, added a source-clean guard, and verified original board files unchanged.
