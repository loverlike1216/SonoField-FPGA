# CODEX_RESULT — v2 bounded timing and model-continuity recovery

Current analysis model: GPT-6.1 Sol High (user-declared manual selection). Record date: 2026-10-03. Historical Vivado runs retain their native 2026-09-29 dates and model provenance.

PROJECT_ID: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
branch: main
active_version: v2
stage: CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST
starting HEAD: b11c80ca3e7fc7745241c32f8f80d95329ca4ddf
ending HEAD: recorded by subsequent delivery_sync.json; avoid a self-referential commit hash

## Physical Board Facts
Historical real Vivado JTAG scans confirmed Zynq-7000 XC7Z020, IDCODE0x23727093 and ARM DAP0x4BA00477. User photograph confirms CLG400. FT2232H0403:6010 A/B and COM4/B were observed. Physical speed/temperature/full ordering code and bridge-to-PS UART MIO route remain unconfirmed. Hardware scans were not repeated during a model transition. Nominal N18/33MHz follows user-selected constraint-file precedence; oscillator frequency is not measured.

## Conservative -1 Engineering Assumption
Explicit user authorization selects xc7z020clg400-1 for bounded engineering analysis, not physical part identity. Keep physical speed UNKNOWN. No full-board timing or external-I/O qualification is claimed by OOC synthesis/routing.

## P-20260927-001 Decision
User approved APPROVE_LIMITED_TIMING_REFACTOR_IN_V2; original problem body hash 0bf40cdd79faaf5fd4aca4af6e1f7cf85eab8662128f4633ea1acb3b4ef61916. Preserved formal approval file records exact source and revalidated base. Two substantial rounds were executed; next selector/control proposal is P-20260929-001, OPEN.

## Original Timing Baseline
Fresh original synthesis reproduced WNS-8.128ns,TNS-2868.007ns,491failing endpoints,WHS+0.164ns,THS0. Worst carrier_acc→serializer CE delay15.451ns,24levels. This is synthesis; compare routed rounds separately.

## Timing Changes
Round1 replaced phase division by exact rational phase accumulation. Round2 did the same for the burst generator. Both preserve per-cycle master phase, tick, period boundary, all burst offsets/done behavior, register/channel/atomic map/calibration semantics and zero external latency change. No third RTL round, false-path/multicycle masking or relaxed production clock. Reproduction Tcl selects preserved baseline inputs and removes a deprecated report option; no model-driven RTL change occurred during recovery.

## Timing Results / Post-Route Results

|Run|State|WNS ns|TNS ns|Failing endpoints|WHS ns|THS ns|
|---|---|---|---|---|---|---|
|Original|Synthesis|-8.128|-2868.007|491|+0.164|0|
|Round1|Synthesis|-7.911|-1304.552|284|+0.164|0|
|Round1|Routed|-7.160|-11281.662|12261|+0.093|0|
|Round2|Synthesis|-3.997|-107.126|92|+0.164|0|
|Round2|Routed|-4.515|-6007.936|9921|+0.070|0|

Round2 uses8170LUT,17979FF,4BRAM,1DSP. Worst queue channel→bus_wdata has12.039ns/eight levels. 32-bit channel×17 variable part select merits range-safe selection refactor. Failing path classes:7993CE,418D,1502CLR,8PRE; high fanout controls and internal async reset recovery need explicit review. No unconstrained internal endpoints;2324input and285output ports lack delays, so full board path qualification remains absent. DRC/methodology warnings, native logs and all failed timing reports are retained. Deprecated report_timing -nets critical warnings were reporting-option warnings; corrected script removes the option. Do not infer timing PASS from tool exit0.

Minimum throughput at41.5kHz:41500×256×11=116.864MHz core,58.432MHz shift. Tested fixed-route screens:132/123.75/121/118.8MHz still timing FAIL;115.5/99MHz also FAIL throughput;82.5MHz reaches+0.030ns diagnostic slack but fails throughput. MMCM ratio checks are synthesized primitive checks, not final clock or board implementation. Official132/66MHz remains. Timing decision:CORE_TIMING_REVISE.

## Functional Regression
Independent Icarus and Vivado2025.2 XSim checks:486026phase comparisons and5066261burst comparisons, including all256burst offsets,min/nominal/max frequency,live phase-frequency changes,reset/abort:PASS. Offline AXI bridge/full system/safe leaf:PASS in both tools. Earlier full regression:112Python tests,3696trajectory frames,three Icarus plus one XSim canonical hash equality,production cadence/faults,inherited phase tests,self-calibration and exact ADC roundtrip PASS.

The last 2026-09-29 GUI retry failed with exit1 and no diagnostic; retain it without guessing root cause. A separate 2026-10-03 recovery run is under recovery_20261003/regression_fixed; its real summary is PASS:114Python tests,3696TRAP_VALID frames,threeIcarus/oneXSim exact canonical hashes,production cadence/faults,inherited tests,self-calibration and ADC regression. Model-transition checks never promote a failed run into PASS.

## UART Route Evidence
REAL_UART_ROUTE_BLOCKED_BY_MISSING_EVIDENCE. Real local documentation inventory and prior evidence do not establish PS UART instance/MIO. COM4 enumeration alone does not prove UART data routing. No UART opened or transmitted.

## PS Firmware
Portable host C service/protocol was compiled and tested by actual host GCC. Target ARM compile/link/run is NOT_RUN: no reviewed PS preset,XSA,BSP or confirmed ARM toolchain. Real Vitis2025.2 Python preflight was attempted; it reports missing platform. Safe PL leaf exists and is simulated; it is not a complete PS block design or ELF. Deployment preflight is intentionally fail-closed and contains no programming commands.

## AXI Integration
Bridge/system/safe-leaf Icarus and XSim PASS. Safe leaf exposes AXI and clock/reset only; acoustic/ADC/external motion controls are inactive internally. Real PS↔AXI↔PL hardware integration remains NOT_RUN.

## Real PING/PONG / Real PL Register Roundtrip / Safe Write Test / Fault-Disconnect Test / ILA Evidence
All real board tests NOT_RUN: Gate A failed, physical UART route and PS platform unverified. Required result JSONs contain NOT_RUN with reasons; there are no synthetic hardware success counts. Fault injection and safe-disable behavior have simulation evidence only. No ILA capture, bitstream build or download.

## B01 / B03 / B04
B01 PARTIALLY_RESOLVED: family/package known, physical grade/order unknown. Conservative-1 target not yet timing validated.
B03 OPEN: UART/MIO,VCCO and connector facts unverified; blocks physical pins and real transport.
B04 OPEN: serializer physical timing/loading/distribution/watchdog/power qualification unverified; digital core timing also FAIL.

## Remaining Blockers
CORE_TIMING; actual UART-to-PS route; reviewed PS preset/XSA/BSP and target ARM build; B01/B03/B04; physical batch/calibration/levitation B05/B06/B07. External ChatGPT history remains BLOCKED. Current recovery memory covers single-board v2 only. Historical artifacts stay preserved and are not execution inputs.

## Files Changed
Phase/burst RTL; safe PL leaf; exact-cycle and AXI leaf TBs; reproducible Vivado Tcl/pwsh,equivalence and preflight scripts; engineering evidence/state; user-approved decision and new evidence-backed problem; MODEL_ENVIRONMENT and formal MODEL_TRANSITION/focus events. Frozen v1, PCB and previous transcripts are hash-protected. Latest user replacement rules authorize Codex to maintain current plans/state and reconciled checkpoints.

## Git Commit / GitHub Sync
Final commit and remote comparison are recorded after review in delivery_sync.json. No force push,release,deployment or new-version creation. This report does not claim synchronization before real Git output.

## Next Recommended Stage
Independent review of the quantified next bounded v2 queue/control timing contract. Preserve current128-channel/8-bit/frequency/atomic/safety semantics; range-safe selector and measured enable/reset path improvements need equivalence and full routed closure. Then establish real PS/UART facts and execute gated bare-board transport; external acoustic bring-up follows measured electrical qualification and P0/P1 milestones.

Stage result: **REVISE**. This applies to CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST only. Model transition itself is an administrative continuity check, not acceptance of the physical platform.

## New recovery evidence and bounded local correction

The first2026-10-03 full run completed all four real motion executions with identical trajectory/map/trap/ACK hashes, but failed the unchanged trap-validity assertion because GUI stored an unevaluated preview path. Failure:recovery_20261003/regression/summary.json. Reversible fix uses a snapshot of the exact dispatched evaluated path/result and verifies the saved path digest against actual execution. Two new provenance tests bring the Python suite to114; the complete fixed-source gate is PASS in a separate run under recovery_20261003/regression_fixed. Historical failures remain unmodified. This local evidence persistence correction is based on new tool/file evidence and changes no architecture,parameters,RTL or Acceptance.
