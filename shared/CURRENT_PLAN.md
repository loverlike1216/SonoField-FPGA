# Current v2 execution position — 2026-10-03

Current model: GPT-6.1 Sol High. Active v2; stage CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST. Primary objective: single Robei octagonal Zynq-7020 acoustic control. Latest user rules authorize Codex to maintain plan and CONTEXT_CHECKPOINT.

Two timing rounds and clock/throughput analysis are complete. Gate A FAIL: routed WNS-4.515ns,TNS-6007.936ns. Exact-cycle phase/burst and safe offline AXI checks PASS. Previous complete regression PASS; failed retry preserved; recovery exposed a GUI evidence mismatch; the reversible snapshot/hash fix and complete 114-test/3696-frame dual-simulator regression PASS.

Next priorities:

1. Recovery regression is PASS. Complete source/hash reconciliation and traceable GitHub checkpoint.
2. Independent review of P-20260929-001 for the next bounded queue/enable/reset timing stage. Existing two-round contract is exhausted.
3. Establish verified UART-to-PS route, PS preset/XSA/BSP and target ARM toolchain.
4. After real routed Gate A and prerequisites pass, execute bare-board PC↔PS↔AXI↔PL safe transport.
5. Qualify digital-driver electrical timing/load and opposing-pair acoustics before measured array/particle milestones.

Do Not Change: interfaces/register/packet/channel maps,requested/calibration split,atomic maps,128-channel/8-bit capability,38.5–41.5kHz operating range,132/66MHz production clocks,safety,current geometry and historical evidence. No failing-design deployment.

Previous plan content below is historical and does not override current real evidence.

---

# Current execution contract — schematic revision V1

Active project v2; user-authorized schematic-only stage. Full contract: PCB/V1/log/preflight/EXECUTION_CONTRACT.md.

Completed: native128TX/8RX capture; one-page consolidation; solid module borders; horizontal net labels; ADC text alignment; vector PDF/SVG; save/reopen; connectivity and mapping audit; ERC classification; frozen v1 check.
Remaining electrical gates: P-20260925-001 serializer timing and independent watchdog/power qualification; B01/B03 physical core facts; exact MPN/packages and analog/batch measurements. Do not invent pins or waive warnings.
Next action: independent review of delivered draft; execute a sourced decision when available. No PCB layout, fabrication, version upgrade or physical claim authorized.

## Previous software-stage contract (historical)

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
