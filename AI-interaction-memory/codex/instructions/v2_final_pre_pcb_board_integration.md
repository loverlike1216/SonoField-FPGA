# SonoField-FPGA v2
# GPT-6.1 Sol High — Final Pre-PCB Board Integration Contract
# Stage:
# TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE

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

primary_tool:
AMD Vivado 2025.2

physical_board:
Robei Octagonal Zynq-7020

execution_agent:
Codex

reviewed_direction:
GPT-6.1 Sol High

---

# 0. USER AUTHORIZATION / VERSION GATE

Continue CURRENT v2.

DO NOT create v3.

DO NOT modify frozen v1.

The user has explicitly confirmed the physical FPGA as:

Device:
XC7Z020

Package:
CLG400

Speed Grade:
-1

Temperature Grade:
C

Therefore the current physical FPGA shall be recorded as:

XC7Z020-1CLG400C

Vivado part:

xc7z020clg400-1

These are no longer temporary engineering assumptions.

Classification:

USER_CONFIRMED_PHYSICAL_FACT

Historical reports that correctly recorded earlier uncertainty must remain unchanged.

Update CURRENT canonical project state only.

---

# 1. NEW USER-APPROVED PHYSICAL ARCHITECTURE

The following board-interface architecture is now formally approved for current v2.

## PC / USER INTERFACE

J2 Type-C:

Windows PC
    ↓
J2 Type-C
    ↓
FT2232H
    ├── Channel A → JTAG / Vivado / programming / ILA
    └── Channel B → user command transport → Zynq PS

Final intent:

PC SonoField Application
→ J2 Type-C
→ Zynq PS
→ AXI
→ PL.

The actual FT2232 Channel-B → PS UART physical route must still be VERIFIED rather than assumed.

---

## UPPER ARRAY PCB

J3:

UPPER ARRAY DATA INTERFACE

Purpose:

16 serializer DATA lanes for the upper 64-TX array.

J5:

UPPER ARRAY CONTROL + RX/ADC INTERFACE

Purpose includes:

SHIFT_CLK_UPPER

LATCH_UPPER

OE_UPPER

BOARD_ENABLE_UPPER

RX_BLANK_UPPER

and required upper-board RX / ADC control and return signals.

---

## LOWER ARRAY PCB

J4:

LOWER ARRAY DATA INTERFACE

Purpose:

16 serializer DATA lanes for the lower 64-TX array.

J6:

LOWER ARRAY CONTROL + RX/ADC INTERFACE

Purpose includes:

SHIFT_CLK_LOWER

LATCH_LOWER

OE_LOWER

BOARD_ENABLE_LOWER

RX_BLANK_LOWER

and required lower-board RX / ADC control and return signals.

---

# 2. DUAL-BOARD SYNCHRONIZATION REQUIREMENT

J5 and J6 control paths are physically independent outputs.

However:

UPPER and LOWER control timing MUST originate from the same FPGA master timing domain.

Normal operation shall guarantee:

SHIFT timing coherence

LATCH / COMMIT coherence

phase-state coherence

frame-sequence coherence

upper/lower acoustic-field coherence.

Normal dual-board mode:

UPPER + LOWER update on the same logical field boundary.

The architecture shall also permit:

UPPER independent safe disable

LOWER independent safe disable.

Do NOT implement two unrelated free-running timing domains.

---

# 3. POWER POLICY

J3/J4/J5/J6 5V connector pins are NOT the default SonoField array power supply.

Do NOT assume that board connector 5V can safely power:

TC4427 drivers

NU40C transducers

AFE

AD7606B

or the complete array PCB.

Default architecture:

J3/J4/J5/J6:
digital signals + reference grounds

SonoField PCB:
dedicated external power input for driver / analog power.

The connector 5V pins shall remain:

UNUSED / AUXILIARY

unless actual board current capability and noise implications are independently verified.

---

# 4. EVIDENCE PRECEDENCE — USER APPROVED

For board interface facts use this order:

1. REAL PHYSICAL DETECTION / TOOL EVIDENCE
2. user-supplied connector image + user-supplied Excel
3. verified revision-matched manufacturer documentation
4. current board constraint files
5. converted XDC
6. historical screenshots / secondary references

If real physical detection is possible:

use it.

If real detection cannot establish the fact:

use the user-supplied connector image and Excel as the approved fallback baseline.

Do NOT silently replace a detected hardware fact with a historical file.

If two user-supplied sources truly conflict rather than merely showing different connector orientation:

record SOURCE_CONFLICT
and resolve by physical verification if possible.

Do not guess.

---

# 5. USER-SUPPLIED CONNECTOR BASELINE

The following connector mapping comes from the user's supplied Excel
`7020-400引脚配置`
and is cross-referenced with the supplied physical connector image.

Persist this information as USER_SUPPLIED_BOARD_REFERENCE.

Do not modify historical sources.

---

# 6. J3 — UPPER DATA CONNECTOR

Approved fallback pin map:

J3 Pin01 = U14
J3 Pin02 = U15
J3 Pin03 = T14
J3 Pin04 = T15
J3 Pin05 = T16
J3 Pin06 = U17
J3 Pin07 = V17
J3 Pin08 = V18

J3 Pin09 = VCC / 5V
J3 Pin10 = GND
J3 Pin11 = GND
J3 Pin12 = VCC / 5V

J3 Pin13 = U18
J3 Pin14 = U19
J3 Pin15 = T17
J3 Pin16 = R18
J3 Pin17 = N17
J3 Pin18 = P18
J3 Pin19 = T20
J3 Pin20 = U20

Therefore:

J3 contains exactly:

16 FPGA signal candidates
+
2 GND
+
2 5V.

Target logical use:

UPPER_DATA[15:0]

Do not place SHIFT/LATCH/OE on J3 unless new physical evidence forces an architecture change.

---

# 7. J4 — LOWER DATA CONNECTOR

Approved fallback pin map:

J4 Pin01 = F19
J4 Pin02 = F20
J4 Pin03 = D19
J4 Pin04 = D20
J4 Pin05 = C20
J4 Pin06 = B20
J4 Pin07 = B19
J4 Pin08 = A20

J4 Pin09 = VCC / 5V
J4 Pin10 = GND
J4 Pin11 = GND
J4 Pin12 = VCC / 5V

J4 Pin13 = E18
J4 Pin14 = E19
J4 Pin15 = E17
J4 Pin16 = D18
J4 Pin17 = F16
J4 Pin18 = F17
J4 Pin19 = H15
J4 Pin20 = G15

Target logical use:

LOWER_DATA[15:0]

IMPORTANT:

Old converted XDC / constraint evidence contained a duplicate/ambiguous J4 entry.

The user-supplied Excel now supplies a complete numbered mapping.

Attempt real verification where practical.

If real verification is unavailable, this Excel + connector image mapping is the approved fallback for the current board profile.

Do not retain the old duplicate J4 Pin6 interpretation as current truth.

---

# 8. J5 — UPPER CONTROL / RX / ADC CONNECTOR

Approved fallback pin map:

J5 Pin01 = N20
J5 Pin02 = P20
J5 Pin03 = M17
J5 Pin04 = M18
J5 Pin05 = M19
J5 Pin06 = M20
J5 Pin07 = L19
J5 Pin08 = L20

J5 Pin09 = VCC / 5V
J5 Pin10 = GND
J5 Pin11 = GND
J5 Pin12 = VCC / 5V

J5 Pin13 = K19
J5 Pin14 = J19
J5 Pin15 = H16
J5 Pin16 = H17
J5 Pin17 = G17
J5 Pin18 = G18
J5 Pin19 = G19
J5 Pin20 = G20

J5 provides:

16 programmable signal candidates.

Target responsibilities:

UPPER_SHIFT_CLK

UPPER_LATCH

UPPER_OE

UPPER_BOARD_ENABLE

UPPER_RX_BLANK

UPPER ADC / RX control

UPPER ADC return

optional fault/status

as required by the final hardware contract.

---

# 9. J6 — LOWER CONTROL / RX / ADC CONNECTOR

Approved fallback pin map:

J6 Pin01 = T11
J6 Pin02 = T10
J6 Pin03 = U12
J6 Pin04 = T12
J6 Pin05 = W13
J6 Pin06 = V12
J6 Pin07 = V13
J6 Pin08 = U13

J6 Pin09 = VCC / 5V
J6 Pin10 = GND
J6 Pin11 = GND
J6 Pin12 = VCC / 5V

J6 Pin13 = Y14
J6 Pin14 = W14
J6 Pin15 = W15
J6 Pin16 = Y16
J6 Pin17 = V15
J6 Pin18 = Y17
J6 Pin19 = W16
J6 Pin20 = V16

J6 provides:

16 programmable signal candidates.

Target responsibilities:

LOWER_SHIFT_CLK

LOWER_LATCH

LOWER_OE

LOWER_BOARD_ENABLE

LOWER_RX_BLANK

LOWER ADC / RX control

LOWER ADC return

optional fault/status

as required by the final hardware contract.

---

# 10. DO NOT PREASSIGN J5/J6 SIGNALS BLINDLY

The connector roles are frozen.

The exact J5/J6 logical-signal-to-pin assignment is NOT yet frozen.

Codex shall first query Vivado/package/device information and determine:

IO bank

bank VCCO

clock-capable status

electrical capability

package legality

routing suitability.

Then assign signals intelligently.

Priority:

SHIFT_CLK
→ best appropriate clock-capable / lowest-skew candidate where available

ADC source-synchronous clock where required
→ appropriate timing-capable candidate

ADC data inputs
→ grouped compatible pins / bank

LATCH
→ same logical timing group

OE / ENABLE / RX_BLANK
→ ordinary safe GPIO

BUSY / FAULT / STATUS
→ input-capable ordinary GPIO.

Do not put a critical clock onto an arbitrary pin merely to preserve connector numbering symmetry.

---

# 11. J5/J6 CONTROL-SIGNAL BUDGET

Each connector has 16 programmable signal positions.

Codex shall derive the actual required RX/ADC interface from:

current BOM

current schematic

current RTL

current ADC implementation

current self-calibration architecture.

Do NOT invent an ADC topology.

Create:

v2/config/j5_upper_signal_budget.json
v2/config/j6_lower_signal_budget.json

and:

v2/docs/hardware/J5_J6_SIGNAL_BUDGET.md.

A preferred starting concept, if compatible with the actual ADC topology, is:

SHIFT_CLK
LATCH
OE
BOARD_ENABLE
RX_BLANK

ADC_CONVST
ADC_RESET
ADC_CS
ADC_SCLK
ADC_SDI where required
ADC_BUSY
ADC_DOUT[...]

plus optional FAULT/STATUS.

This is a starting allocation only.

The real BOM/ADC contract governs.

---

# 12. IMPORTANT CONSEQUENCE FOR SERIALIZER ARCHITECTURE

Because:

J3 = 16 upper DATA lanes

J4 = 16 lower DATA lanes

and:

J5/J6 carry clock/control separately,

the existing:

32 DATA lane total

architecture is now connector-feasible.

Therefore:

UPPER:
16 lanes → 64 TX → 4 TX per lane

LOWER:
16 lanes → 64 TX → 4 TX per lane.

Do NOT redesign the lane count merely because J3/J4 appeared full in the previous analysis.

The connector-capacity blocker is now RESOLVED AT ARCHITECTURE LEVEL.

Any future lane-count change must be motivated by:

Timing

electrical performance

throughput

PCB complexity

or measured hardware evidence,

not connector availability alone.

---

# 13. REPOSITORY RECONCILIATION

Before editing code:

read:

README.md
AGENTS.md

shared/PROJECT_STATE.json
shared/ENGINEERING_STATE.json
shared/VERSION_STATE.json
shared/CONTEXT_CHECKPOINT.md
shared/CURRENT_PLAN.md
shared/DECISIONS.md
shared/ACCEPTANCE.md
shared/BLOCKERS.md
shared/HANDOFF.md

AI-problem/problem/P-20260927-001__candidate-core-timing.md
AI-problem/problem/P-20260929-001__queue-control-timing.md

v2/evidence/core_timing_real_loop/RESULT.md

v2/config/board_identity.json
v2/config/register_map.json

all relevant:

v2/rtl
v2/software
v2/tb
v2/tests
v2/scripts
v2/docs
v2/hardware

and:

E:\Codex_project\AMD-SonoField-FPGA\Zynq7020

including:

hardware.const
gpio.const
converted XDC
existing images.

Report internally:

local HEAD

origin/main HEAD

working tree status

current version

current stage

validated source commit.

Do not overwrite uncommitted user work.

---

# 14. CURRENT VERIFIED DIGITAL BASELINE

Preserve current validated capabilities:

128 TX logical channels

8-bit phase

requested_phase

calibration_phase

requested/calibration separation

atomic map commit

motion queue

self-calibration

ADC behavioral acquisition

PC GUI

point movement

line movement

planar trajectory

circle

rectangle

vertical movement

binary PC protocol

offline PS service

AXI bridge.

Current recovery evidence contains approximately:

114 Python tests PASS

3696 TRAP_VALID frames

3 Icarus deterministic executions

1 Vivado XSim execution

self-calibration PASS

ADC roundtrip PASS

AXI simulation PASS.

Do not rewrite working subsystems without measured reason.

---

# 15. BOARD IDENTITY UPDATE

Current repository still contains historical:

speed_grade = null
temperature_grade = null
physical_speed_grade = UNKNOWN.

Update current canonical state to:

silicon:
XC7Z020

package:
CLG400

speed_grade:
-1

temperature_grade:
C

physical_device:
XC7Z020-1CLG400C

vivado_part:
xc7z020clg400-1

provenance:
USER_CONFIRMED_PHYSICAL_FACT.

B01 shall be re-evaluated.

Missing complete ordering text shall NOT continue blocking normal Vivado implementation if:

device
package
speed
temperature

are sufficient for the required target.

---

# 16. CLOCK SOURCE REVALIDATION

User-approved source precedence has changed for this stage:

REAL MEASUREMENT FIRST.

If the physical input oscillator frequency can be safely measured or established by reliable hardware evidence:

use the real measured value.

If actual detection cannot distinguish the source:

use the current user-supplied image/Excel reference.

The supplied Excel records:

N18
33.333 MHz.

Historical project state used:

N18
33 MHz

from older constraint precedence.

Therefore this is a CURRENT SOURCE CONFLICT.

Do NOT silently retain one.

Attempt real verification first.

If real verification cannot be obtained:

record:

CLOCK_SOURCE_FALLBACK =
N18 / 33.333 MHz

because current user instruction gives the new image/Excel fallback precedence.

Recalculate MMCM/PLL parameters accordingly.

Preserve the historical 33 MHz decision in history.

---

# 17. APPROVE NEXT BOUNDED TIMING STAGE

P-20260929-001 next bounded timing work is authorized in CURRENT v2.

Current historical routed result:

WNS ≈ -4.515 ns
TNS ≈ -6007.936 ns
WHS ≈ +0.070 ns
THS = 0.

Main current classes include:

motion_queue dynamic selector

channel selection

bus_wdata

CE high fanout

asynchronous reset recovery.

Allowed changes:

replace wide integer indexing with bounded indices

factor 128×17 selection

hierarchical bank selection

reduce variable-part-select depth

reduce bus_wdata combinational depth

local registered enables

enable replication where justified

reset synchronization

synchronous reset release

remove unnecessary asynchronous CLR/PRE use

local retiming

bounded pipeline insertion.

Do NOT change:

128 channels

8-bit phase

requested/calibration separation

atomic map semantics

upper/lower channel ordering

PC packet protocol

register-map semantics

38.5–41.5 kHz supported acoustic range.

---

# 18. TIMING MUST BE REAL

Target:

XC7Z020-1CLG400C

Vivado:

xc7z020clg400-1.

Run:

synthesis

opt_design

place_design

phys_opt_design where justified

route_design.

Final acceptance is POST-ROUTE:

WNS >= 0

TNS = 0

WHS >= 0

THS = 0.

Preferred:

WNS >= +0.5 ns

if achievable without unnecessary architecture distortion.

Do not use false-path or multicycle exceptions to hide ordinary synchronous failures.

---

# 19. RE-DERIVE THROUGHPUT

Because the 32-lane topology is now retained:

recalculate the minimum real serializer/core frequency directly from CURRENT RTL.

Use worst supported acoustic frequency:

41.5 kHz

Phase resolution:

256 states.

Determine actual:

shift cycles

latch cycles

guard/setup cycles

core cycles per state.

Do not blindly reuse historical:

116.864 MHz

unless the current implementation proves the same requirement.

Generate:

v2/docs/hardware/SERIALIZER_THROUGHPUT_PROOF.md.

Final clock must satisfy:

TIMING PASS

AND

THROUGHPUT PASS.

---

# 20. CLOCK POLICY

132/66 MHz is preferred only if it can be reliably closed.

It is NOT a sacred project requirement.

After timing refactor, compare legal candidates above the proven throughput floor.

The final production clock shall prioritize:

stability

timing margin

determinism

over maximum frequency.

Do not use 82.5 MHz simply because historical diagnostic slack became positive if throughput fails.

---

# 21. FULL REGRESSION

After accepted RTL changes rerun:

114+ Python tests

Icarus

Vivado XSim

3696-frame motion regression

phase/burst exact-equivalence checks

self-calibration

ADC roundtrip

AXI bridge

safe-disable tests

atomic map tests.

No Timing optimization may be accepted by weakening existing Acceptance.

---

# 22. CONNECTED BOARD DETECTION

The user will physically connect and power the Robei board and open Vivado 2025.2.

Perform fresh non-destructive detection:

Windows USB

FT2232 A/B

COM ports

network interfaces

Vivado hw_server

Hardware Manager

JTAG chain

XC7Z020

ARM DAP.

Confirm identity consistency.

Do NOT:

replace drivers

use Zadig

modify FTDI EEPROM

guess Boot configuration.

---

# 23. J2 TYPE-C USER TRANSPORT

The final system requires:

PC
→ J2 Type-C
→ user-command channel
→ Zynq PS.

Attempt to VERIFY:

FT2232H Channel B
→ TX/RX
→ PS UART instance
→ exact MIO pair.

Use:

real board evidence

local files

manufacturer documentation

reference projects

user-provided material.

COM4 existence alone is not proof.

If verified:

UART_ROUTE = VERIFIED.

If not verified:

do not fabricate it.

JTAG may temporarily complete PS↔AXI↔PL debugging,

but:

PRE_PCB_BOARD_READY

requires a repeatable J2 user communication path.

---

# 24. PS PLATFORM

Build the simplest reliable real PS platform.

Prefer:

bare-metal standalone

for first bring-up.

Use:

UART/user transport

packet parser

CRC

sequence

watchdog

AXI MMIO

status responses.

Prefer OCM for early smoke testing if practical.

Do not add Linux unless there is a real requirement.

Generate/review:

PS configuration

clock/reset

AXI GP master

address assignment

XSA

BSP

ARM executable.

---

# 25. FIRST REAL PC → PS → AXI → PL → PC LOOP

After Timing PASS:

program only a SAFE bare-board build.

No PCB connected.

No external ultrasonic output enabled.

Execute:

PING
→ PONG

then:

GET_VERSION

GET_CAPABILITIES

GET_STATUS

then:

PC
→ READ_REGISTER
→ J2
→ PS
→ AXI
→ PL VERSION/STATUS
→ PS
→ J2
→ PC.

This establishes the first real:

PC → PS → AXI → PL → PS → PC

loop.

---

# 26. TRANSPORT STRESS

Start at:

115200
8N1
no flow control

if UART is verified.

Run:

100 exchanges

then:

1000 exchanges.

Measure:

CRC failures

sequence failures

timeouts

median RTT

P95

maximum RTT.

Then evaluate higher supported baud rates.

Use the highest rate with proven reliability and adequate margin.

---

# 27. REAL SAFE WRITE

After read path succeeds:

perform only a harmless write:

SAFE_DISABLE

or an isolated diagnostic register.

Verify:

PC
→ PS
→ AXI write
→ PL
→ AXI readback
→ PS
→ PC.

External outputs remain disabled.

---

# 28. REAL PHASE MAP

After the base transport succeeds:

exercise on REAL FPGA:

MAP_CHANNEL

MAP_DATA

MAP_WRITE

MAP_COMMIT

MAP_STATUS.

Verify:

128-channel complete-map load

atomic commit

sequence

ACK

queue behavior

underflow

overflow

reset

STOP.

J3/J4/J5/J6 outputs remain SAFE_DISABLED.

Use ILA for independent evidence.

---

# 29. GUI → REAL FPGA

Switch the existing user application from:

SimulationTransport

to:

verified real BoardTransport.

Run the existing digital motion demonstrations:

CENTER

point move

line

circle

rectangle

Z up

Z down

return center.

The trap moves digitally inside the real FPGA.

No ultrasound is emitted yet.

---

# 30. J3/J4 DATA INTERFACE FREEZE

After Timing and real internal operation pass:

freeze:

J3 = UPPER_DATA[15:0]

J4 = LOWER_DATA[15:0].

Create:

v2/config/j3_upper_data_interface.json

v2/config/j4_lower_data_interface.json

and:

v2/docs/hardware/J3_J4_DATA_INTERFACE.md.

For every lane include:

logical lane

connector pin

package pin

IO bank

VCCO

IOSTANDARD

idle state

maximum frequency

reset behavior

PCB destination.

---

# 31. J5/J6 CONTROL INTERFACE FREEZE

Freeze:

J5 = UPPER CONTROL + RX/ADC

J6 = LOWER CONTROL + RX/ADC.

Create:

v2/config/j5_upper_control_adc_interface.json

v2/config/j6_lower_control_adc_interface.json

and:

v2/docs/hardware/J5_J6_CONTROL_ADC_INTERFACE.md.

For every signal include:

signal

connector pin

package pin

direction

bank

VCCO

IOSTANDARD

clock relationship

idle level

power-up state

maximum frequency

PCB destination.

---

# 32. VCCO / IOSTANDARD

Do not infer VCCO from connector 5V.

For every used FPGA bank:

determine actual VCCO.

Priority:

real detection / measurement

manufacturer hardware documentation

approved user reference.

Then assign legal IOSTANDARD.

Converted-XDC LVCMOS33 values are NOT proof of physical VCCO.

If VCCO cannot be established automatically:

create:

MANUAL_VCCO_MEASUREMENT_REQUIRED.md

containing exactly:

bank

required rail

measurement location

expected range

what it blocks.

---

# 33. FPGA → PCB EXTERNAL TIMING CONTRACT

Before declaring PCB-ready, define external timing for:

UPPER DATA

LOWER DATA

UPPER SHIFT_CLK

LOWER SHIFT_CLK

LATCH

OE

ENABLE

ADC clocks

ADC returns.

Generate:

v2/docs/hardware/FPGA_TO_PCB_TIMING_BUDGET.md.

Include:

clock frequency

launch edge

capture edge

setup margin

hold margin

connector/cable skew

translator delay budget

PCB routing skew

clock jitter margin.

This becomes the formal PCB implementation input.

---

# 34. SAFETY

All J3/J4/J5/J6 hardware outputs shall default to:

SAFE_DISABLED

until PCB bring-up is explicitly authorized.

On:

power-up

reset

PS crash

PC disconnect

UART loss

CRC fault storm

watchdog expiry

FPGA reconfiguration

the system must remain or return to:

SAFE_DISABLED.

UPPER and LOWER arrays must each support independent disable.

---

# 35. PRE_PCB_BOARD_READY ACCEPTANCE

Declare:

PRE_PCB_BOARD_READY = YES

only if ALL are true:

1. XC7Z020-1CLG400C canonical state updated.

2. physical board detected successfully.

3. production input clock resolved.

4. final production core/serializer clock selected.

5. post-route Timing PASS.

6. full regression PASS.

7. real safe bitstream runs on the Robei board.

8. PS firmware runs on real hardware.

9. J2 user transport verified.

10. 1000-packet transport stress PASS.

11. real PC→PS→AXI→PL→PS→PC loop PASS.

12. real safe write/readback PASS.

13. real internal 128-channel phase-map commit PASS.

14. GUI controls real FPGA digital state.

15. J3 upper DATA interface frozen.

16. J4 lower DATA interface frozen.

17. J5 upper control/RX/ADC interface frozen.

18. J6 lower control/RX/ADC interface frozen.

19. VCCO verified.

20. IOSTANDARD verified.

21. external timing budget complete.

22. all PCB-facing outputs remain safely disabled.

23. no unresolved FPGA-side interface fact would require PCB redesign after fabrication.

If all pass:

the next major physical stage is:

CONNECT SONOFIELD PCB.

---

# 36. PCB BRING-UP CONTRACT FOR NEXT STAGE

Do NOT execute this stage now.

Only prepare the interface.

Future physical connection shall be:

J3
→ Upper PCB DATA

J5
→ Upper PCB CONTROL / RX / ADC

J4
→ Lower PCB DATA

J6
→ Lower PCB CONTROL / RX / ADC

J2
→ PC user/control/debug.

Upper and lower PCB driver power shall use dedicated external power unless separately qualified.

---

# 37. MISSING FACT HANDLING

Do not immediately stop with:

"Need more information."

First exhaust all digitally accessible evidence.

Only request manual user intervention when necessary.

If blocked, create:

v2/evidence/pre_pcb_board_ready/MISSING_PHYSICAL_FACTS.md

For every unresolved fact state:

fact

why needed

what it blocks

all sources searched

exact manual action.

Examples:

measure FPGA Bank VCCO

continuity-check a connector pin

identify FT2232-B UART route.

No vague requests.

---

# 38. EVIDENCE

Create:

v2/evidence/pre_pcb_board_ready/

with at least:

repository_reconciliation/

board_identity/

connector_reference/

clock/

timing/

throughput/

implementation/

j2_transport/

ps_platform/

axi_real/

phase_map_real/

gui_real/

ila/

j3/

j4/

j5/

j6/

vcco/

external_timing/

regression/

failures/

reproducibility/.

Do not overwrite historical evidence.

---

# 39. REPOSITORY UPDATE

After verified work update:

shared/PROJECT_STATE.json

shared/ENGINEERING_STATE.json

shared/CURRENT_PLAN.md

shared/DECISIONS.md

shared/BLOCKERS.md

shared/ACCEPTANCE.md

shared/CONTEXT_CHECKPOINT.md

v2/config/board_identity.json

CHANGELOG.md.

Persist the new current interface architecture:

J2 = PC USER / DEBUG

J3 = UPPER DATA

J5 = UPPER CONTROL/RX/ADC

J4 = LOWER DATA

J6 = LOWER CONTROL/RX/ADC.

---

# 40. DO NOT CHANGE

Do NOT:

create v3

modify frozen v1

modify PCB layout in this stage

reduce 128 TX

reduce 8-bit phase

change requested/calibration semantics

change atomic commit semantics

change coordinate-system definition

fake hardware validation

hide Timing failures

guess VCCO

guess UART routing

force push

release/deploy acoustic hardware.

---

# 41. STOP CONDITION

Stop when either:

## SUCCESS

PRE_PCB_BOARD_READY = YES

and the next project step is physically connecting:

J3 + J5 → Upper SonoField PCB

J4 + J6 → Lower SonoField PCB.

OR:

## BLOCKED

all automatically executable work is finished and only explicitly documented physical measurements remain.

Do not continue repeated Timing retries without a materially new implementation strategy.

---

# 42. FINAL REPORT

Return:

PROJECT_ID

project_name

active_version

branch

starting HEAD

ending HEAD

model/provenance:
GPT-6.1 Sol High reviewed execution contract

## Physical FPGA

XC7Z020-1CLG400C

## Repository Reconciliation

## Board Detection

## Clock Source

## Timing Root Cause

## Timing Refactor

## Throughput Proof

## Final Production Clock

## Final Post-Route Timing

## Functional Regression

## J2 Type-C User Transport

## PS Platform

## PC → PS → AXI → PL → PC

## Real Phase Map

## GUI → Real FPGA

## J3 Upper DATA

## J5 Upper CONTROL / RX / ADC

## J4 Lower DATA

## J6 Lower CONTROL / RX / ADC

## VCCO / IOSTANDARD

## External Timing Budget

## Safety Verification

## Remaining Blockers

## Exact Manual Actions Required

## Git Commit

## GitHub Sync

Final engineering conclusion exactly one:

ACCEPT

ACCEPT WITH LIMITATIONS

REVISE

Additionally output exactly:

PRE_PCB_BOARD_READY = YES / NO

If NO:

list ONLY the exact unresolved facts preventing PCB connection.