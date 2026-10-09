# SonoField-FPGA v2
# Stage: CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST

PROJECT_ID: SONOFIELD_FPGA

project_name:
SonoField-FPGA

repository:
https://github.com/loverlike1216/SonoField-FPGA.git

workspace_path:
E:\Codex_project\AMD-SonoField-FPGA

branch:
main

active_version:
v2

primary_EDA:
AMD Vivado 2025.2

physical_board:
Robei Octagonal Board / Zynq-7020

physical_board_state:
CONNECTED_TO_CURRENT_WINDOWS_PC

---

# 0. USER AUTHORIZATION / VERSION GATE

This task CONTINUES CURRENT v2.

DO NOT create v3.

The user explicitly authorizes this stage:

1. use `XC7Z020CLG400-1` as the conservative ENGINEERING TIMING TARGET;
2. solve current CORE_TIMING;
3. after timing passes, use the currently connected bare Zynq board;
4. establish the first real:

PC
→ PS
→ AXI
→ PL
→ PS
→ PC

closed loop.

This authorization does NOT mean the physical chip speed grade has been identified as `-1`.

The physical fact must remain:

physical_silicon:
XC7Z020

physical_package:
CLG400

physical_speed_grade:
UNKNOWN

physical_temperature_grade:
UNKNOWN

engineering_timing_target:
xc7z020clg400-1

classification:
CONSERVATIVE_ENGINEERING_ASSUMPTION

Do NOT rewrite repository facts to claim:

PHYSICAL_SPEED_GRADE = -1.

---

# 1. CURRENT REPOSITORY FACTS

Before modifying anything, read and reconcile:

README.md
AGENTS.md

shared/PROJECT_STATE.json
shared/ENGINEERING_STATE.json
shared/VERSION_STATE.json
shared/CURRENT_PLAN.md
shared/DECISIONS.md
shared/ACCEPTANCE.md
shared/BLOCKERS.md
shared/HANDOFF.md

AI-problem/problem/P-20260927-001*
AI-problem/decision/*

v2/evidence/board_transport/RESULT.md

v2/config/board_identity.json
v2/config/register_map.json

v2/rtl/
v2/software/
v2/scripts/
v2/tests/
v2/tb/

Current remote facts observed before this instruction:

latest documentation checkpoint:
b11c80ca3e7fc7745241c32f8f80d95329ca4ddf

validated engineering source:
b7f285896f78334d66091328f46aa4f657504430

Do not assume these are still current locally.

First report:

PROJECT_ID
repository
workspace
branch
local HEAD
origin/main HEAD
active_version
current_stage
working tree status.

If local work is newer than GitHub:

preserve it
and inspect it before proceeding.

---

# 2. FORMAL DECISION FOR P-20260927-001

Persist a formal decision corresponding to:

P-20260927-001

Decision:

APPROVE_LIMITED_TIMING_REFACTOR_IN_V2

Current Version:
v2

Decision:

Use:

xc7z020clg400-1

as the conservative engineering timing target.

Allow limited internal RTL timing refactoring.

Do NOT alter externally visible functional semantics unless strictly necessary and separately documented.

Rationale:

All three candidate speed grades currently fail the 132 MHz setup requirement:

-1:
WNS ≈ -8.128 ns

-2:
WNS ≈ -4.995 ns

-3:
WNS ≈ -3.609 ns

Therefore the problem is not solved by assuming a faster speed grade.

Design shall be improved so that it can meet timing under the conservative -1 target where reasonably possible.

Rejected options:

- declaring physical chip as -1 without evidence;
- selecting -3 merely to improve WNS;
- hiding violation with false paths;
- adding unjustified multicycle constraints;
- relaxing clocks without throughput proof;
- changing tests to match a broken implementation;
- creating v3;
- downloading a timing-failing design to hardware;
- driving unknown external PL pins.

User approval required:

NO for this stage.

Current user instruction explicitly approves this decision.

---

# 3. STAGE GOAL

This stage has TWO sequential gates.

## GATE A — CORE TIMING CLOSURE

Achieve a timing-clean FPGA digital core under:

PART:
xc7z020clg400-1

with a justified clock architecture.

Primary goal:

retain current 132 MHz core / 66 MHz serializer architecture if timing can be closed with reasonable internal refactoring.

If this is not achievable after bounded engineering attempts:

evaluate a lower-clock architecture that still satisfies the REAL serializer throughput requirement.

Do not reduce frequency arbitrarily.

## GATE B — REAL BARE-BOARD DIGITAL LOOP

After GATE A passes:

use the physically connected bare Zynq board to establish:

Windows PC
→ board transport
→ Zynq PS
→ AXI4-Lite
→ existing PL register system
→ PS
→ Windows PC.

No SonoField PCB.

No ADC PCB.

No TCT40.

No TC4427.

No external PL acoustic outputs.

---

# 4. NON-GOALS

This stage shall NOT attempt:

- PCB layout;
- PCB modification;
- real serializer electrical output;
- AD7606B physical capture;
- TCT40 drive;
- acoustic calibration;
- levitation;
- particle motion;
- camera tracking;
- arbitrary external GPIO validation;
- production deployment;
- v3.

Do not use this stage to add GUI features or new trajectory modes.

---

# 5. PRESERVE EXISTING VALIDATED FUNCTIONAL CONTRACT

The following functional behavior is FROZEN unless a real blocker proves change is necessary:

128 TX logical channels

8-bit requested_phase

8-bit calibration_phase

channel mask

requested/calibration phase separation

atomic MAP_COMMIT

motion queue semantics

register map

PC SFP2 packet format

trajectory behavior

calibration database semantics

50 Hz motion-control contract

existing channel ordering

existing deterministic tests.

Timing optimization may alter internal latency.

If latency changes:

document exact latency change

and update reference models only to represent actual new hardware latency.

Do NOT change user-visible functionality merely to make tests pass.

---

# 6. GATE A — ESTABLISH TIMING BASELINE

First rerun the current candidate target:

xc7z020clg400-1

with fresh reports.

Generate:

report_timing_summary
report_timing -max_paths
report_high_fanout_nets
report_clock_utilization
report_methodology
report_drc
report_utilization

Capture at least:

WNS
TNS
WHS
THS
number of failing endpoints
top 20 failing paths
startpoints
endpoints
logic levels
route delay
logic delay
fanout
clock uncertainty.

Do not optimize based only on one reported path.

Identify whether failures cluster around:

carrier accumulator

phase generation

tick generation

serializer enable

serializer bit index CE

map publication

or another subsystem.

Save raw baseline evidence.

---

# 7. CURRENT KNOWN TIMING PROBLEM

Current evidence indicates the -1 worst path is approximately:

carrier_acc_reg
→ phase/control combinational logic
→ serializer bit_index_reg / CE

with a data-path magnitude around the 15 ns class.

Do NOT assume this is the only problem.

Confirm with fresh Vivado reports.

---

# 8. TIMING OPTIMIZATION PRIORITY

Attempt optimizations in this order.

## A. REMOVE EXPENSIVE COMBINATIONAL PHASE SCALING

Review expressions equivalent to:

carrier accumulator
→ multiply/scale/divide
→ master phase
→ serializer/control.

Prefer FPGA-native fixed-point phase accumulation.

Consider:

phase_acc[n+1]
=
phase_acc[n] + phase_increment

and use upper accumulator bits as phase state where mathematically valid.

Avoid combinational division on the critical path.

Preserve numerical phase accuracy.

Cross-check against the Python phase model.

---

## B. REGISTER CONTROL BOUNDARIES

Where safe:

register carrier tick

register serializer start

register map publication trigger

register large combinational control results.

One or more cycles of COMMON deterministic latency are acceptable if:

all channels observe the same latency;

atomic publication remains coherent;

the acoustic phase relationship is unchanged;

software/reference latency metadata is updated.

---

## C. SERIALIZER ENABLE / CE PATH

Investigate:

bit_index CE
serializer state CE
global tick fanout
large fanout control signals.

Potential fixes:

local registered enables
balanced fanout
hierarchical control
register duplication
state-machine retiming.

Do not generate a large combinational CE cone if a registered enable can be used.

---

## D. FANOUT

Inspect high-fanout:

reset
commit
tick
enable
mask
phase-valid

signals.

Apply structural duplication or hierarchical buffering only where Vivado evidence supports it.

Do not manually duplicate logic without measurement.

---

## E. PIPELINE

Pipeline arithmetic/control where needed.

Every pipeline insertion must have:

documented stage
latency
functional equivalence test.

Do not pipeline across an atomic-map boundary in a way that mixes old/new channel states.

---

# 9. DO NOT CHEAT TIMING

Forbidden unless mathematically and architecturally proven:

set_false_path

set_multicycle_path

set_max_delay

set_clock_groups -asynchronous

or any timing exception

used merely to silence a failing synchronous path.

Every exception must have:

source
destination
clock-domain reasoning
CDC mechanism
formal justification.

Otherwise reject it.

---

# 10. CLOCK ARCHITECTURE FALLBACK

First attempt to retain:

core:
132 MHz

serializer:
66 MHz.

If after at most TWO serious RTL timing-refactor rounds:

WNS remains materially negative

and there is no new evidence suggesting another local fix,

perform a formal clock-rate trade study.

Do NOT simply choose 100/50 MHz.

Calculate the actual minimum serializer rate from the implemented serializer FSM.

Include:

effective bits per lane per frame
number of shift cycles
latch cycles
guard cycles
setup cycles
required phase-state refresh
required margin.

Current architecture uses:

32 lanes
4 used serialized states per lane

but actual minimum frequency must be derived from code.

Produce a matrix such as:

core MHz
shift MHz
MMCM legality
serializer throughput margin
phase-engine behavior
WNS
resource impact.

Evaluate only clock pairs that are legal from the current board clock architecture.

Do not change the official clock profile unless:

serializer throughput remains sufficient
AND
phase resolution remains sufficient
AND
all regression tests pass
AND
the new profile has clearly better timing margin.

If a clock change is selected:

record it as an engineering decision.

Do not call it a hardware fact.

---

# 11. GATE A ACCEPTANCE

Preferred:

xc7z020clg400-1

132 MHz core
66 MHz serializer

with:

WNS >= 0
TNS = 0
WHS >= 0
THS = 0.

If an approved alternate clock profile is required:

same timing acceptance applies.

Also require:

112+ Python tests PASS

all existing Icarus tests PASS

Vivado XSim PASS

full 3696-frame motion regression PASS

self-calibration regression PASS

ADC behavioral roundtrip PASS

AXI bridge tests PASS

three deterministic repetitions PASS.

No reduction of Acceptance thresholds solely to get PASS.

---

# 12. IMPLEMENTATION, NOT ONLY SYNTHESIS

Once synthesis timing looks acceptable:

run full:

opt_design
place_design
phys_opt_design where justified
route_design.

Then generate post-route:

report_timing_summary
report_utilization
report_clock_utilization
report_drc
report_methodology.

The important gate is POST-ROUTE timing.

Do NOT call:

post-synthesis WNS >= 0

a final timing closure.

Required status:

POST_ROUTE_TIMING_PASS.

---

# 13. BOARD SMOKE TEST TARGET POLICY

The physical chip speed grade remains UNKNOWN.

However the user explicitly authorizes:

xc7z020clg400-1

as the conservative board-smoke-test engineering target.

Therefore a minimal bare-board smoke-test build MAY use:

xc7z020clg400-1

provided that:

- silicon XC7Z020 is physically confirmed;
- CLG400 is physically confirmed;
- the design passes post-route timing on -1;
- no unknown PL external pin is driven;
- acoustic outputs do not leave the FPGA;
- the build is labeled:

BOARD_SMOKE_TEST_ENGINEERING_TARGET

not:

PHYSICAL_EXACT_PART_VERIFIED.

Do not update:

physical_speed_grade

from UNKNOWN.

---

# 14. CREATE A DEDICATED SAFE BARE-BOARD TOP

Do NOT program the complete acoustic external-I/O top first.

Create a dedicated safe top, for example:

sono_board_smoke_top

with:

Zynq PS
AXI interconnect / AXI4-Lite
existing AXI-to-native-register bridge
existing internal sono_motion_system/register system
optional ILA.

External acoustic outputs:

NOT EXPOSED
or
FORCED DISABLED.

Do not instantiate unknown connector outputs as active top-level pins.

No external serializer output is required for the first loop.

This build exists only to prove:

PC
↔
PS
↔
AXI
↔
PL.

---

# 15. CLOCK FOR BOARD SMOKE BUILD

If practical, the bare-board transport smoke top may use a PS FCLK for the PS/PL integration path.

Do not confuse this with the final SonoField acoustic clock architecture.

The smoke test only needs a deterministic safe PL clock sufficient for:

AXI
register access
internal status.

If PS FCLK is used:

document:

frequency
reset
clock domain
difference from production clock architecture.

Do not use this to claim production serializer timing.

---

# 16. UART ROUTE VERIFICATION BEFORE REAL TRANSMISSION

Current facts:

FT2232H:
VERIFIED

A interface:
JTAG VERIFIED

B interface:
COM4 EXISTS

COM4 → PS UART:
NOT VERIFIED.

Before transmitting bytes:

find independent evidence that FT2232 B is physically routed to a Zynq PS UART/MIO pair.

Search:

local Zynq7020 board documentation
revision-matched schematic
manufacturer files
existing local board project
verified constraint/reference material.

If a reliable source confirms:

FT2232 B
→ PS UART

persist:

UART_ROUTE = VERIFIED.

If not:

do NOT silently assume it.

Stop physical UART deployment with:

REAL_UART_ROUTE_BLOCKED_BY_MISSING_EVIDENCE.

Offline AXI/timing work may still complete.

---

# 17. DO NOT USE PL GPIO FOR UART AS A GUESS

Do not bypass missing PS UART evidence by choosing arbitrary PL pins.

Do not drive:

J3
J4
J6
or other connectors

while B03 remains unresolved.

The first real loop should preferably use the board's onboard PS-side communication path.

---

# 18. REAL BOARD PS SOFTWARE

Reuse the existing tested PS communication C core.

Integrate it into a real Zynq standalone/bare-metal application using the supported AMD 2025.2 tool flow available on this machine.

Responsibilities:

PS UART RX/TX
SFP2 framing
CRC checking
sequence checking
timeout
watchdog
command dispatch
AXI MMIO access
response framing
SAFE_DISABLE.

Keep acoustic mathematics on the PC for this stage.

Do not port motion planning/calibration to PS yet.

---

# 19. FIRST REAL COMMAND SET

Only enable:

PING
GET_VERSION
GET_CAPABILITIES
GET_STATUS
SAFE_DISABLE
READ_REGISTER

WRITE_REGISTER shall remain restricted.

No motion commands.

No MAP_COMMIT.

No external waveform enable.

No calibration command.

No serializer physical enable.

---

# 20. REAL UART INITIAL CONFIGURATION

If UART route is VERIFIED and no board-specific value overrides it:

use a conservative bring-up baud rate such as:

115200 baud

for the first PING/PONG.

Reason:

bandwidth is irrelevant for the first smoke test;
reliability and observability are more important.

Do NOT yet optimize to:

460800
or
921600.

Higher rates can be evaluated after the physical loop works.

---

# 21. REAL BOARD PROGRAMMING METHOD

Prefer JTAG-based temporary bring-up.

Do not modify permanent boot media.

Do not change boot switches unless required and explicitly documented.

Recommended high-level sequence:

Vivado/XSCT/Vitis supported flow
→ initialize PS
→ program safe PL bitstream
→ download PS ELF
→ run PS application.

No QSPI/SD permanent programming in this stage.

Create a reproducible script where possible.

Example conceptual artifact:

v2/scripts/board_smoke_test.ps1

and supporting Tcl/XSCT scripts.

Do not hard-code undocumented device paths.

---

# 22. FIRST HARDWARE TEST — PING/PONG

With:

bare board only

no SonoField PCB

no external load,

execute:

PC
→ PING
→ FT2232 B / UART
→ PS
→ PONG
→ PC.

Acceptance:

100 consecutive exchanges PASS first.

Then:

1000 exchanges.

Record:

sent
received
timeouts
CRC errors
sequence errors
latency min
latency median
latency p95
latency max.

Required for 1000-run gate:

CRC error:
0

sequence mismatch:
0

unexpected response:
0

transport crash:
0.

Timeouts should be investigated, not hidden.

---

# 23. SECOND HARDWARE TEST — VERSION / CAPABILITIES

PC sends:

GET_VERSION
GET_CAPABILITIES.

PS returns:

firmware version
SFP2 protocol version
capabilities.

Confirm PC backend and PS binary agree.

Protocol mismatch must:

FAIL CLOSED.

---

# 24. THIRD HARDWARE TEST — PC → PS → AXI → PL → PS → PC

This is the core acceptance test.

Use a known READ-ONLY PL register from:

v2/config/register_map.json

such as:

VERSION
STATUS
or equivalent verified read-only field.

Sequence:

PC
→ READ_REGISTER
→ UART
→ PS
→ AXI4-Lite
→ AXI/native bridge
→ PL register bank
→ AXI response
→ PS packet
→ UART
→ PC.

Record the complete transaction.

The value returned by PC must equal:

the value observed from the PL register system.

This establishes the first real:

PC
→ PS
→ AXI
→ PL
→ PS
→ PC

closed loop.

---

# 25. FOURTH SAFE WRITE TEST

Only after read path passes.

Use an inherently safe operation.

Preferred:

SAFE_DISABLE

or another existing safe control bit.

Sequence:

PC
→ SAFE_DISABLE
→ PS
→ AXI write
→ PL
→ readback STATUS
→ PS
→ PC.

The PL shall remain in:

SAFE_DISABLED.

Do NOT write:

hardware enable
normal field enable
serializer external OE
acoustic drive
motion arm.

If no safely readable/writeable control exists:

do not invent one in the canonical production register map merely for the test.

A dedicated smoke-test diagnostic register may be added only if clearly isolated from production semantics.

---

# 26. ILA OPTIONAL CROSS-CHECK

If useful:

add a temporary debug ILA observing:

AXI AW/W/B
AXI AR/R
native bus valid/write/address/data
status read
SAFE_DISABLE
IRQ.

Do not expose acoustic outputs.

If ILA is used:

run implementation/timing again.

A debug build that fails timing is not acceptable merely because the non-ILA build passed.

Save ILA evidence separately.

---

# 27. DO NOT CONTINUE TO PHASE MAP YET

The STOP condition for this stage is:

real read/write-safe control loop established.

Do NOT automatically continue into:

128-map physical transfer
serializer output
array board
ADC
TCT40.

Those belong to the next stage after independent review.

---

# 28. FAILURE HANDLING

If Timing Closure fails after two substantive optimization rounds:

do not keep cycling identical changes.

Create:

Root Cause Analysis

including:

critical path class
logic depth
routing share
fanout
clock uncertainty
resource placement
proposed alternate clock profile.

If UART route cannot be proven:

report:

REAL_TRANSPORT_BLOCKED_BY_UART_ROUTE

but still finish:

Timing Closure
offline PS build
AXI integration
scripts.

If PS firmware cannot link/run:

save:

BSP/XSA/tool errors
actual logs
attempted fixes.

Do not fake real transport.

---

# 29. REQUIRED TESTS

## Timing

TIMING-01:
fresh -1 baseline

TIMING-02:
post-refactor synthesis

TIMING-03:
post-place

TIMING-04:
post-route

TIMING-05:
hold analysis

TIMING-06:
clock utilization

TIMING-07:
CDC/methodology

TIMING-08:
3 repeated implementation summaries where deterministic where reasonable.

## Regression

REG-01:
112+ Python tests

REG-02:
Icarus inherited tests

REG-03:
XSim inherited tests

REG-04:
self-calibration

REG-05:
ADC roundtrip

REG-06:
3696-frame motion regression

REG-07:
AXI bridge

REG-08:
fresh-clone reproduction where practical.

## Real hardware

HW-01:
JTAG reconnect

HW-02:
UART route evidence

HW-03:
PS application starts

HW-04:
100 PING/PONG

HW-05:
1000 PING/PONG

HW-06:
GET_VERSION

HW-07:
GET_STATUS

HW-08:
PL read-only register roundtrip

HW-09:
SAFE_DISABLE write/readback

HW-10:
disconnect → safe state.

---

# 30. DISCONNECT / FAULT BEHAVIOR

Real transport must fail safely.

If:

UART disconnects

CRC repeatedly fails

protocol version mismatches

watchdog expires

PS software crashes

AXI timeout occurs,

then the system must remain or return to:

SAFE_DISABLED.

No stale motion command may continue.

---

# 31. NO EXTERNAL PL OUTPUTS

During ALL real-board tests in this stage:

external acoustic outputs MUST remain physically inactive.

No:

TCT40
TC4427
SN74LVC595
AD7606
AFE

is connected.

Do not use unresolved connector pins.

The board is a bare digital integration target only.

---

# 32. EVIDENCE DIRECTORY

Create:

v2/evidence/core_timing_real_loop/

Suggested structure:

baseline/
timing_refactor/
implementation/
regression/
board_smoke/
uart/
ps/
axi/
ila/
reproducibility/
failures/

Required artifacts include:

tool_versions.json
part_assumption.json
timing_baseline.rpt
timing_postroute.rpt
utilization.rpt
clock_report.rpt
methodology.rpt
drc.rpt
critical_paths.json
timing_decision.md
uart_route_evidence.json
ps_build.log
bitstream_build.log
ping_100.json
ping_1000.json
version_response.json
pl_register_roundtrip.json
safe_disable_roundtrip.json
RESULT.md.

---

# 33. REPOSITORY FACT DISCIPLINE

Update:

shared/PROJECT_STATE.json
shared/ENGINEERING_STATE.json
shared/DECISIONS.md
shared/BLOCKERS.md
shared/ACCEPTANCE.md
CHANGELOG.md

but preserve truth.

Expected example:

physical_speed_grade:
UNKNOWN

engineering_timing_target:
xc7z020clg400-1

timing:
PASS / FAIL

real_transport:
PASS / BLOCKED

ps_pl_real_loop:
PASS / NOT_RUN / FAIL.

Do NOT convert assumptions into physical facts.

---

# 34. B01 STATUS

Even if -1 Timing Closure passes:

B01 remains partially unresolved because physical speed/temperature/full ordering code remain unknown.

However the stage may record:

CONSERVATIVE_-1_ENGINEERING_TARGET_VALIDATED

if post-route timing succeeds.

That is NOT the same as:

B01 RESOLVED.

---

# 35. B03 STATUS

B03 remains open for:

PL connector
VCCO
IOSTANDARD
pin contradictions.

If PS UART route becomes independently verified:

only the PS UART sub-item may be marked resolved.

Do not close all B03 merely because PC communication works.

---

# 36. B04 STATUS

B04 physical serializer timing remains OPEN.

Even if internal RTL timing passes:

66 MHz external electrical path through:

FPGA
→ translator
→ buffer
→ serializer
→ PCB

has not been validated.

Do not close B04.

---

# 37. ACCEPTANCE — GATE A

GATE A PASS requires:

engineering part:
xc7z020clg400-1

POST-ROUTE:

WNS >= 0
TNS = 0
WHS >= 0
THS = 0

plus:

all major regressions PASS.

No unjustified timing exceptions.

---

# 38. ACCEPTANCE — GATE B

GATE B PASS requires REAL hardware evidence:

JTAG:
PASS

UART physical route:
VERIFIED

PS firmware:
RUNNING ON REAL BOARD

1000 PING/PONG:
PASS

GET_VERSION:
PASS

GET_STATUS:
PASS

PC→PS→AXI→PL read:
PASS

safe PL write/readback:
PASS

disconnect safe behavior:
PASS

no external acoustic output:
VERIFIED.

---

# 39. DONE WHEN

This stage is DONE when:

## Case A — Full success

Timing Closure PASS
+
real PC→PS→AXI→PL→PS→PC loop PASS.

Then stop.

Do not proceed to array output automatically.

## Case B — Timing PASS, UART blocked

Report:

TIMING_PASS
OFFLINE_PS_PL_PASS
REAL_TRANSPORT_BLOCKED_BY_UART_ROUTE.

Stop.

## Case C — Timing FAIL

Report:

CORE_TIMING_REVISE

with quantified root cause.

Do not deploy a failing design.

---

# 40. FINAL REPORT FORMAT

At completion output:

PROJECT_ID
project_name
repository
branch
active_version
stage
starting HEAD
ending HEAD

## Physical Board Facts

## Conservative -1 Engineering Assumption

## P-20260927-001 Decision

## Original Timing Baseline

## Timing Changes

## Timing Results

## Post-Route Results

## Functional Regression

## UART Route Evidence

## PS Firmware

## AXI Integration

## Real PING/PONG

## Real PL Register Roundtrip

## Safe Write Test

## Fault / Disconnect Test

## ILA Evidence

## B01

## B03

## B04

## Remaining Blockers

## Files Changed

## Git Commit

## GitHub Sync

## Next Recommended Stage

Finish with exactly one:

ACCEPT
ACCEPT WITH LIMITATIONS
REVISE

The conclusion must apply only to:

CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST.

Do not claim the complete SonoField-FPGA physical platform is accepted.