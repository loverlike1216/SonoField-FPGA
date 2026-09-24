# SELF_CALIBRATION_SOFTWARE_AND_DIGITAL_SYSTEM execution contract

Goal: complete the user-authorized v2 software and digital calibration chain; keep v1 frozen.
Input: attachment archived in AI-interaction-memory/codex/instructions/v2_self_calibration.md.
Scope: shared machine-readable configuration/registers, ADC/burst/scan/buffer/control RTL,
behavioral ADC, realistic raw synthetic traces, TOF/phase/pose/sweep/f_work/health/database/LUT,
plots and reports, Python/Icarus/XSim cross-check, standalone fresh reproduction and GitHub sync.
Non-goals: PCB schematic/layout/Gerber, purchases, v3, invented target part, synthesis/physical PASS.
Architecture: single synchronous PL command bus; bounded acknowledged captures; host nonlinear solver.
Constraints: preserve requested/calibration split and atomics; invalid/clipped inputs fail closed;
document ADC datasheet timing, hardware timing limitations and phase-reference identifiability.
Validation: inherited gates, CAL-TB01..15, SW-T01..20, 512-path end-to-end, noisy/outlier cases,
three deterministic runs, source hashes and clean v1-absent clone. Save failures and evidence.
Rollback: ordinary Git revert of this stage; do not modify frozen v1. Done only after actual tests,
reports, interface contract and commit/push verification. Stop before physical PCB work.

## Completed checkpoint: 2026-09-24

Implementation, full local and fresh-clone gates, source push/remote verification complete.
Source 9c058fe3b02469a6d36a08e3a7cbedd19076e67b. Evidence: v2/evidence/self_calibration_stage/reproducibility_review.
Final report and interaction/evidence checkpoint follows. STOP for independent review; no PCB stage.
