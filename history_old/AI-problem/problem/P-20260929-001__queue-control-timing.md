---
problem_id: P-20260929-001
project_id: SONOFIELD_FPGA
active_version: v2
current_stage: CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST
status: OPEN
created_at: 2026-09-29
created_by: Codex
base_commit: b11c80ca3e7fc7745241c32f8f80d95329ca4ddf
problem_hash: a84242c69d945dc5989c8b708623657e61fe8eeb4af0782f4474531cfff9972b
---

# Decision Needed
Authorize a separate bounded v2 queue/control timing stage after the two-round contract ended. Do not deploy the current design.

# Goal
Complete the single Robei XC7Z020/CLG400 board acoustic-control path while retaining 128 channels, 8-bit phases, requested/calibration separation, atomic maps and 38.5-41.5 kHz operation.

# Current Engineering State
Gate A FAIL after two substantive refactors. Main phase division and calibration-burst division removed with zero cycle latency change, independent exact-cycle checks PASS. Round2 post-route WNS -4.515 ns, TNS -6007.936 ns, 9921 setup/recovery failing endpoints; WHS 0.070 ns, THS 0.000 ns. Functional regression is recorded separately; no hardware deployment.

# Repository Facts
Active v2, paused incomplete v3 excluded. Engineering part xc7z020clg400-1 is explicitly user-authorized conservative assumption, physical speed/temperature remain UNKNOWN. Production clock remains 132/66 MHz.

# Evidence
v2/evidence/core_timing_real_loop/round2/routed/critical_paths.rpt
v2/evidence/core_timing_real_loop/critical_paths.json
v2/evidence/core_timing_real_loop/clock_trade.json
v2/evidence/core_timing_real_loop/timing_refactor/equivalence.json
v2/evidence/core_timing_real_loop/final_regression/summary.json

# What Codex Tried
Round1 replaced main phase division with an exact rational phase accumulator. Round2 similarly replaced burst phase division. Each underwent synthesis, placement, physical optimization and routing. No false/multicycle exceptions or official clock reduction. Fixed-route diagnostic screens plus standalone MMCM synthesis checked 132,123.75,121,118.8,115.5,99,82.5 MHz.

# Root Cause Hypotheses
Worst routed path is queue/channel_reg[11]_replica to queue/bus_wdata_reg[15]/D: 12.039 ns, 8 levels. motion_queue uses 32-bit integer channel for active[channel*17+:17], although legal channel is 0..127. The inferred multiply/selection merits width reduction and hierarchical selection. This alone cannot establish closure: 7993 failing CE paths and 1510 internal asynchronous CLR/PRE recovery paths remain (plus 418 D paths). Control fanout and reset deassertion must be reviewed without masking them.

# Candidate Options
1. Next bounded stage: explicit range-safe indices and selector factoring, then proven-equivalent localized control fanout/register changes; review reset assertion/deassertion semantics separately. Preserve external map/cadence/ACK behavior, add original-vs-new cycle comparisons, repeat full regression and routed timing.
2. A formally approved deeper pipeline if same-cycle restructuring cannot close, with explicit common latency contract and updated independent oracle.
3. Do not adopt 82.5 MHz: although the existing route has +0.030 ns diagnostic WNS, serializer throughput fails. Minimum core is 41500*256*11=116864000 Hz. No tested profile satisfies both constraints. This is not a proof that a new implementation at another clock can never succeed.

# Constraints
Two-round contract exhausted. No third RTL micro-patch in this checkpoint. No interface/scope/hardware change without decision. No v3 work, PCB edits, UART transmission, external GPIO or bitstream download. Physical UART route, PS preset/XSA/BSP and embedded ARM toolchain remain blocking.

# Acceptance Impact
CORE_TIMING_REVISE. Gate B blocked even though offline AXI tests pass. No claim that single-board control or levitation is complete.

# Preliminary Engineering Assessment
Prioritize queue selection plus measured enable/reset cones in v2. A new bounded execution contract is needed for the next timing round. User latest steering confirms v2 single-board priority but does not waive quantitative timing or hardware gates.

# Questions For Chat
Approve the next bounded queue/control refactor and its exact-cycle acceptance, or specify a different timing architecture. Independently review all non-data reset paths and board clock scope.

# User Approval Boundary
User owns scope/hardware/interface changes. This record requests a bounded implementation decision, not a new version. No deployment until Gate A and real UART/PS prerequisites pass.
