# SonoField-FPGA — v2 Formal Development Instruction

## 0. PROJECT IDENTITY

PROJECT_ID: SONOFIELD_FPGA

project_name:
SonoField-FPGA

repository:
https://github.com/loverlike1216/SonoField-FPGA.git

workspace_path:
E:\Codex-project\AMD-SonoField-FPGA

board_reference_path:
E:\Codex-project\AMD-SonoField-FPGA\Zynq7020

branch:
main

previous_version:
v1

active_target_version:
v2

primary_FPGA:
Robei Octagonal Board / Zynq-7020

primary_EDA:
AMD Vivado 2025.2

Chat Source:
SonoField-FPGA

---

# 1. USER VERSION AUTHORIZATION

The user has explicitly approved creation and development of:

v2

This is a formal VERSION_UPGRADE_APPROVAL.

Do not ask again whether v2 may be created.

However:

v2 is the only newly authorized version.

DO NOT automatically create:

v3
v4
or any later version.

If later work appears to justify v3, create a:

VERSION_UPGRADE_REQUEST

and wait for explicit user approval.

The words:

continue
继续
继续开发
继续优化
继续修复
继续测试

always mean:

CONTINUE_CURRENT_VERSION

and must remain in v2 after this upgrade.

---

# 2. FIRST ACTION — PREFLIGHT

Before changing any engineering file, inspect the real repository.

Read at minimum:

README.md
AGENTS.md

shared/PROJECT_STATE.json
shared/PROJECT_STATE.md
shared/VERSION_STATE.json
shared/CURRENT_PLAN.md
shared/DECISIONS.md
shared/ACCEPTANCE.md
shared/BLOCKERS.md
shared/HANDOFF.md
CHANGELOG.md

AI-chat-memory/INDEX.md
AI-interaction-memory/INDEX.md

AI-problem/problem/*
AI-problem/decision/*

v1/README.md

and all relevant:

v1/rtl/
v1/tb/
v1/tests/
v1/software/
v1/scripts/
v1/config/
v1/constraints/
v1/hardware/
v1/docs/
v1/evidence/

Also inspect all available board references in:

E:\Codex-project\AMD-SonoField-FPGA\Zynq7020

Before implementation report:

PROJECT_ID
project_name
repository
workspace_path
current_branch
previous_version
target_version
current_stage
Chat Source
Git status
local HEAD
origin/main HEAD

If local and remote differ unexpectedly:

STOP implementation
and report the mismatch.

---

# 3. SOURCE OF TRUTH PRIORITY

When facts conflict, use:

1. user's current explicit instruction;
2. user-approved formal decisions;
3. actual source code/configuration;
4. real tool evidence;
5. shared repository state;
6. AI-problem/decision;
7. AI-chat-memory;
8. AI-interaction-memory;
9. model inference.

Do not overwrite newer evidence with historical assumptions.

GitHub Repository is the long-term engineering source of truth.

---

# 4. VERSION MODEL — COMPLETE STANDALONE PROJECT

This project uses COMPLETE VERSION SNAPSHOTS.

Every version directory:

v1/
v2/
v3/
...

represents a complete, independently usable SonoField-FPGA project.

v2 is NOT:

"a directory containing only changes since v1."

v2 MUST be:

"the complete inherited v1 project + all approved v2 improvements."

The upgrade process is:

freeze v1
→ copy the complete reusable engineering baseline into v2
→ preserve v1 unchanged
→ update explicit version metadata
→ add v2 functionality
→ run inherited regression
→ run new v2 validation
→ establish v2 baseline

---

# 5. v1 FREEZE RULE

After v2 migration begins:

v1 is FROZEN.

Do not modify:

v1/rtl
v1/tb
v1/tests
v1/software
v1/scripts
v1/config
v1/constraints
v1/hardware
v1/docs
v1/evidence

Do not move files out of v1.

Do not make v1 depend on v2.

If a historical v1 defect is discovered:

document it
→ fix it in v2
→ leave v1 unchanged.

Git history remains intact.

---

# 6. v2 MUST BE SELF-CONTAINED

v2 must contain its own complete project.

Normal v2 execution MUST NOT depend on:

../v1/

Prohibited examples:

../v1/rtl
../v1/software
../v1/config
../v1/tests
../v1/scripts
../v1/requirements-lock.txt

Repository-level governance may remain outside version directories:

shared/
AI-chat-memory/
AI-interaction-memory/
AI-problem/

But all runnable engineering assets required to operate the current project must exist under:

v2/

Another engineer must be able to use:

repository root governance
+
v2/

without opening v1 for normal execution.

---

# 7. REQUIRED v2 DIRECTORY BASELINE

Preserve all useful v1 directories and add v2-specific ones where necessary.

Target structure approximately:

v2/
  README.md
  requirements-lock.txt

  rtl/
    timing/
    phase/
    output/
    control/
    calibration/
    acquisition/

  tb/

  tests/

  software/
    acoustic_model/
    calibration/
    characterization/
    geometry/
    control/

  scripts/

  config/

  constraints/

  hardware/
    board/
    transducers/
    pcb/
    adc/
    calibration/
    mechanical/
    bom/
    characterization/

  docs/
    architecture/
    theory/
    hardware/
    experiments/
    verification/
    operating/

  evidence/
    baseline/
    simulation/
    model/
    validation/
    reproducibility/
    synthesis/
    implementation/
    hardware/
    characterization/
    calibration/

Stable module names must not receive meaningless:

_v2

suffixes.

Version semantics come from the containing directory.

---

# 8. MIGRATION MANIFEST

Create:

v2/docs/architecture/V1_TO_V2_MIGRATION.md

Classify each major v1 component as:

COPY_UNCHANGED
COPY_AND_EXTEND
REPLACE_IN_V2
DEPRECATED_IN_V2
NEW_V2

For each item record:

v1 path
v2 path
classification
reason
validation required

Do not silently drop a validated v1 subsystem.

---

# 9. v1 CAPABILITIES THAT MUST BE INHERITED

v2 must retain and independently validate the useful v1 baseline including:

- 128-channel digital phased-array architecture;
- 8-bit phase representation;
- common deterministic phase timebase;
- programmable requested phase;
- independent calibration phase;
- complete-map atomic commit;
- safe digital reset / disable;
- configurable channel count where appropriate;
- Python acoustic field model;
- 8×8 upper TX array;
- 8×8 lower TX array;
- 12 mm radiating-center pitch;
- nominal 100 mm face gap;
- configurable 90–115 mm gap;
- coordinate reference = radiating surface center;
- global origin = geometric center between arrays;
- STANDING_WAVE mode;
- FOCUS mode;
- Python reference versus RTL verification;
- deterministic repeated simulation;
- current repository hygiene and reproducibility mechanisms.

Do not weaken any inherited acceptance criterion simply to make v2 pass.

Any inherited failure is:

REGRESSION.

---

# 10. v2 PRIMARY ENGINEERING GOAL

v2 upgrades SonoField-FPGA from:

OPEN-LOOP PROGRAMMABLE PHASED ARRAY

to:

SELF-CALIBRATING PROGRAMMABLE ULTRASONIC PHASED ARRAY

The full v2 platform shall support:

128 TX
+
8 calibration RX

and create a measured acoustic system model from:

real board geometry
+
real environment
+
real transducer response
+
real per-channel phase error

rather than assuming ideal geometry and identical transducers.

---

# 11. SYSTEM ARCHITECTURE

Overall path:

PC / Host
→ Zynq PS
→ acoustic target / mode / phase map
→ Zynq PL
→ 128-channel deterministic phase engine
→ serializers
→ TC4427A drivers
→ 128 ultrasonic TX
→ acoustic field

Calibration return path:

selected TX
→ acoustic propagation
→ opposite-board RX ×4
→ analog front end
→ central 8-channel ADC
→ Zynq PL acquisition
→ Zynq PS estimation
→ geometry / frequency / phase calibration
→ calibration database
→ regenerated phase map.

---

# 12. PHYSICAL TX GEOMETRY

Primary transmitter:

TCT40-10T
10 mm class
40 kHz nominal

Upper:

8 × 8 = 64 TX

Lower:

8 × 8 = 64 TX

Total:

128 TX.

Pitch:

12.00 mm

TX center coordinates in each board local frame:

X,Y ∈
{
-42,
-30,
-18,
-6,
+6,
+18,
+30,
+42
} mm

Coordinate position means:

CENTER OF RADIATING SURFACE

not package center
and not PCB drill origin.

Nominal array face gap:

100 mm

Mechanical adjustment range:

90–115 mm.

---

# 13. GLOBAL COORDINATE SYSTEM

Use right-handed acoustic coordinates.

Nominal system origin:

(0,0,0)

at the geometric center between the two TX arrays.

For nominal 100 mm gap:

upper radiating plane:

z = +50 mm

lower radiating plane:

z = -50 mm.

But in v2 these values are:

NOMINAL_GEOMETRY

not guaranteed real geometry.

Actual board pose must be measured by calibration.

---

# 14. CALIBRATION RECEIVERS

Add:

4 RX per array PCB.

Total:

8 RX.

Primary receiver candidate:

TCT40-10R

same nominal frequency family.

Preferred local coordinates:

(+54,+54)
(-54,+54)
(-54,-54)
(+54,-54) mm

relative to each array local coordinate frame.

These values can only change if actual PCB/mechanical geometry proves them impractical.

RX placement goals:

- large geometric baseline;
- symmetry;
- minimal collision with mounting holes;
- minimal acoustic obstruction;
- sufficient PCB-edge clearance.

---

# 15. ARRAY SELF-LOCALIZATION

PCB internal TX/RX coordinates are known rigid geometry.

Do NOT solve 128 independent TX positions.

Solve the relative rigid-body transformation between:

Upper PCB
and
Lower PCB.

Represent:

translation:

t = (tx,ty,tz)

rotation:

R = roll,pitch,yaw.

If lower PCB is reference:

known lower TX position:

P_i

known upper RX local position:

Q_j

global upper RX:

Q_j_global =
R Q_j + t

predicted acoustic distance:

d_ij =
||Q_j_global - P_i||

measured:

dhat_ij.

Estimate:

R,t

by robust nonlinear least squares:

min Σ w_ij(d_ij-dhat_ij)^2

Store:

tx
ty
tz
roll
pitch
yaw
RMS residual
maximum residual
number of valid paths
number of rejected paths
timestamp
environment parameters.

---

# 16. BIDIRECTIONAL CALIBRATION

Calibration sequence A:

LOWER TX0
→ UPPER RX0..3

LOWER TX1
→ UPPER RX0..3

...

LOWER TX63
→ UPPER RX0..3

256 paths.

Calibration sequence B:

UPPER TX0
→ LOWER RX0..3

...

UPPER TX63
→ LOWER RX0..3

256 paths.

Total:

512 directional acoustic paths.

Use redundant measurements to improve robustness.

Do NOT directly average four distance values because each RX has a different position.

Use geometry-aware fitting.

---

# 17. RX BLANKING

During lower TX calibration:

UPPER RX:
ACTIVE

LOWER RX:
BLANK / IGNORE.

During upper TX calibration:

LOWER RX:
ACTIVE

UPPER RX:
BLANK / IGNORE.

Implement hardware-assisted blanking using:

TMUX1574PWR

or the approved equivalent from the formal BOM.

State machine must support:

IDLE
SET_CHANNEL
SETTLE
BURST
RX_CAPTURE
RINGDOWN_CAPTURE
PROCESS_READY
NEXT_CHANNEL
DONE

Guard times must be configurable.

---

# 18. RANGE ESTIMATION

Do not estimate physical distance from carrier phase alone.

Use:

COARSE TOF
+
FINE CARRIER PHASE.

## Coarse stage

Generate a configurable finite burst.

Initial baseline candidate:

16 cycles.

Use cross-correlation or matched filtering.

Estimate:

tau_coarse

distance:

d_coarse =
c(T,H) × tau_coarse.

## Fine stage

After integer-wavelength ambiguity is resolved:

delta_d =
lambda/(2*pi) × delta_phi.

Combine both measurements.

Store uncertainty/confidence.

Do not hard-code 16 cycles if another burst length proves better.

---

# 19. ENVIRONMENT COMPENSATION

Use remote:

SHT45-AD1B-R2

for:

temperature
relative humidity.

Place it away from:

TC4427A
Buck converters
hot PCB areas.

Calculate:

c(T,H)

with documented formula and version.

Store:

temperature
RH
calculated sound speed
timestamp.

Do not permanently assume:

c = 343 m/s.

---

# 20. TRANSDUCER CHARACTERIZATION

TCT40 nominal:

40 ± approximately 1 kHz class

does NOT mean each TX shall operate at its own frequency.

Implement per-channel characterization.

For every TX store:

channel_id
array
local_position
batch_id
sweep_result
f0_i
amplitude_at_fwork
phase_error_at_fwork
relative_quality
polarity
optional capacitance
temperature
timestamp
valid/invalid flag.

Initial configurable sweep:

38.5 kHz
→
41.5 kHz

step:

50 or 100 Hz.

Do not assume the exact sweep limits are immutable.

---

# 21. SINGLE COMMON OPERATING FREQUENCY

ABSOLUTE RULE:

All 128 TX channels must use ONE:

f_work.

Prohibited:

TX0 = 39.7 kHz
TX1 = 40.1 kHz
TX2 = 40.5 kHz

during normal array operation.

Different channel frequencies destroy stable relative phase.

Use measured frequency-response data to select one common:

f_work

that gives good aggregate performance.

Document the objective function.

Possible factors:

median response
weak-channel penalty
response uniformity
phase sensitivity
number of usable channels.

---

# 22. PHASE CALIBRATION

For target position:

P_target

and actual measured TX position:

P_i

distance:

r_i =
||P_target-P_i||

wave number:

k =
2*pi*f_work/c

ideal phase:

phi_ideal_i =
-k*r_i

measured acoustic channel phase error:

delta_phi_i.

Final command:

phi_cmd_i =
phi_ideal_i
-
delta_phi_i
mod 2*pi.

Preserve two independent software/RTL concepts:

requested_phase[i]

calibration_phase[i].

Do not bake measured correction permanently into requested field maps.

---

# 23. AMPLITUDE CHARACTERIZATION

Measure:

A_i(f_work)

for every channel.

v2 does NOT need to falsely claim continuous analog amplitude control.

Use amplitude measurements for:

- channel health;
- weak-element detection;
- transducer selection;
- outlier rejection;
- calibration confidence;
- optional channel mask;
- future solver weighting.

If hardware only supports binary excitation, document that limitation.

---

# 24. HARDWARE TOPOLOGY

Final v2 hardware is:

1. Zynq-7020 main board
2. Upper 64TX + 4RX array PCB
3. Lower 64TX + 4RX array PCB
4. Central 8-channel ADC / calibration PCB
5. Remote SHT45 environmental sensor PCB
6. regulated external 15 V supply
7. defined digital / analog / power harnesses.

Final competition hardware should not depend on hobby breakout modules.

Temporary modules may be used only for:

PH0 verification

and must be clearly marked:

TEMPORARY_VALIDATION_HARDWARE.

---

# 25. ARRAY PCB

Two identical boards.

Target:

130 × 130 mm

4 layers
FR-4
1.6 mm
1 oz.

Recommended:

L1:
TCT40 + critical local routes

L2:
solid GND

L3:
VDRV / 3V3 / 5V analog power

L4:
logic / driver / AFE / regulators.

Do not split the ground plane without a demonstrated reason.

Keep switching regulator high-dV/dt loops away from:

RX AFE
VREF
clock routes.

---

# 26. ARRAY PCB ACTIVE BOM

Per array PCB:

64 × TCT40-10T
4 × TCT40-10R

32 × TC4427AEOA713

16 × SN74LVC595APWR

3 × SN74AXC8T245PWR

1 × SN74LVC244APWR

1 × SN74LVC1G32DBVR

1 × TMUX1574PWR

2 × OPA4192IPWR

1 × REF5025AIDR

1 × TPS259470LRPWR

1 × INA226AIDGSR

1 × TMP117MAIDRVR

1 × AP63203WU-7

1 × AP63200WU-7

1 × ADP7118ACPZN5.0-R7

1 × BLM21PG221SN1D

2 × 6.8 uH / >=5 A buck inductors

1 × passive 8P8C calibration connector

1 × 2×25 digital IDC connector

1 × XT30 PCB power connector

plus passives defined in the approved v2 BOM.

Do not replace models silently.

---

# 27. TX SERIALIZER

Per array:

16 data lanes:

DATA[15:0].

Use:

16 × SN74LVC595A.

Each serializer package uses only:

Q0–Q3

for four acoustic TX outputs.

Therefore:

16 × 4 = 64 TX.

Q4–Q7:

RESERVED.

This deliberately trades component count for timing margin.

Do not revert to one long serial chain.

Do not automatically optimize component count before physical timing evidence exists.

---

# 28. CLOCK DISTRIBUTION

Use:

SN74LVC244A

to distribute:

SRCLK
RCLK.

Baseline:

4 SRCLK branches
+
4 RCLK branches.

Each branch drives:

4 serializer ICs.

Use:

33 Ω

source-series damping as baseline.

Actual routed timing must be reviewed before PCB freeze.

Digital simulation PASS does not equal:

PCB electrical timing PASS.

---

# 29. TX DRIVER

Use:

TC4427AEOA713.

One IC:

2 TX channels.

Per array:

32 IC.

Per driver:

100 nF / 50 V
+
1 uF / 25 V

close to VDD/GND.

Per 4-driver group:

22 uF / 25 V.

Each digital driver input:

100 kΩ pulldown.

Each TX channel:

TC4427A OUT
→ 0 Ω series footprint
→ TCT40(+)

TCT40(-)
→ GND.

Reserve optional:

1.2 kΩ

parallel damping footprint.

Default:

DNP.

Do not add a discrete MOSFET power stage unless real measurement proves TC4427A inadequate.

---

# 30. TX DRIVE VOLTAGE

Initial bring-up:

12 V.

Formal expected operating region:

12–15 V initially.

Absolute project design maximum while TC4427A is used:

18 V.

Do not exceed 18 V.

Recommended final external PSU:

MEAN WELL GST120A15-R7B

15 V
7 A
105 W.

Initial hardware testing should use:

current-limited adjustable bench supply.

---

# 31. RX ANALOG FRONT-END

Per RX:

TCT40-10R
→ 1 kΩ
→ BAT54S protection
→ 10 nF C0G AC coupling
→ TMUX1574
→ 100 kΩ bias to VREF
→ OPA4192 stage 1
→ OPA4192 stage 2
→ output filter
→ cable.

Stage 1:

Rf = 100 kΩ
Rg = 10 kΩ

gain ≈ 11.

Stage 2:

Rf = 10 kΩ
Rg = 10 kΩ

gain ≈ 2.

Provide:

0 Ω bypass

around stage 2.

Therefore hardware can operate approximately at:

gain ≈ 11

or:

gain ≈ 22.

Keep the analog path sufficiently wide for:

38.5–41.5 kHz sweep

plus practical margin.

Do not use an excessively narrow 40 kHz analog filter.

---

# 32. RX REFERENCE

Use:

REF5025AIDR

for stable:

2.5 V VREF.

Do not substitute a simple resistor divider for final hardware.

Route VREF quietly and separately from high-current driver returns.

---

# 33. ANALOG CALIBRATION LINK

Each array PCB uses one passive:

8P8C / RJ45-style

connector without Ethernet magnetics.

Baseline:

KH-5224-8P8C.

This is NOT Ethernet.

PCB silkscreen:

CAL ANALOG ONLY
NOT ETHERNET.

Use shielded Cat6 cable.

Mapping:

Pair 1:
RX0 + GND

Pair 2:
RX1 + GND

Pair 3:
RX2 + GND

Pair 4:
RX3 + GND.

---

# 34. CENTRAL ADC PCB

Primary ADC:

AD7606BBSTZ-RL.

Requirements:

8 simultaneous channels

16 bit

800 kSPS/channel class.

At 40 kHz this provides up to approximately:

20 samples/carrier-cycle.

Do not replace with a multiplexed ADC architecture.

ADC PCB active baseline:

1 × AD7606BBSTZ-RL
2 × SN74AXC8T245PWR
1 × TPS259470LRPWR
1 × INA226AIDGSR
1 × TMP117MAIDRVR
1 × AP63203WU-7
1 × AP63200WU-7
1 × ADP7118ACPZN5.0-R7
1 × BLM21PG221SN1D
2 × passive 8P8C inputs
1 × 2×10 digital IDC
1 × XT30 power input
1 × JST-XH 4P environment-sensor port.

Follow Analog Devices datasheet requirements for:

AVCC
VDRIVE
REGCAP
REFCAP
REF

exactly.

---

# 35. ADC INPUT BASELINE

Per ADC channel:

analog cable
→ 47 Ω
→ AD7606B input.

Reserve/use:

1 nF C0G

for high-frequency cable filtering as designed.

Do not filter out the frequency-sweep band.

Capture raw data before optional DSP filtering.

---

# 36. FPGA DIGITAL CABLES

Zynq → Upper Array:

50-conductor IDC.

Zynq → Lower Array:

50-conductor IDC.

Target:

2×25
2.54 mm
keyed connector where practical.

Cable:

UL2651
28 AWG
50 conductor.

Recommended length:

100–150 mm.

Maximum target:

<=200 mm.

Use ground-adjacent signal mapping.

DO NOT use individual Dupont wires for the final high-speed serializer connection.

---

# 37. ADC DIGITAL CABLE

Central ADC PCB → Zynq:

20 conductor IDC

2×10

target length:

<=200 mm.

Signals may include:

CONVST
BUSY
RESET
CS
SCLK
DOUTA
DOUTB
DOUTC
DOUTD
VIO_REF
GND

depending on final AD7606B serial interface architecture.

The final pin map must be derived from real FPGA connector facts.

Do not invent Zynq pins.

---

# 38. POWER ARCHITECTURE

Main:

15 V PSU

star-distributed to:

Upper Array
Lower Array
ADC Board.

Do not daisy-chain power through one PCB to another.

Use:

18 AWG class power harness

and:

XT30 connectors.

Each major PCB input:

XT30
→ physical fuse
→ TVS
→ TPS259470 eFuse
→ INA226 / shunt
→ board power.

---

# 39. POWER COMPONENT BASELINE

Use:

TPS259470LRPWR

for electronic input protection.

Initial values:

ILIM resistor approximately:
1.65 kΩ

target current limit:
~2 A

OVLO candidate:
1.37 MΩ top
100 kΩ bottom

target around:
~17.6 V

dV/dt capacitor:
3.3 nF initial.

ITIMER:
2.2 nF provisional.

These are initial engineering values.

They may only be changed based on datasheet calculations or measured evidence.

Document all changes.

---

# 40. BOARD CURRENT MONITORING

Use:

INA226AIDGSR.

Shunt:

20 mΩ
2 W
1%.

Use Kelvin routing.

Record:

bus voltage
current
power.

Use this data during:

single-channel test
16-channel test
64-channel test
full 128-channel test.

---

# 41. LOCAL POWER RAILS

Digital:

AP63203WU-7

15 V → 3.3 V.

Analog pre-regulator:

AP63200WU-7

15 V → approximately 5.5 V.

Low-noise analog:

ADP7118ACPZN5.0-R7

5.5 V → 5.0 V.

Use:

BLM21PG221SN1D

or approved ferrite isolation where defined.

Do not power the RX AFE directly from a noisy unfiltered switching rail.

---

# 42. BUCK INDUCTOR

Primary:

FXL0630-6R8-M

6.8 uH
5 A class.

Equivalent only if:

L ≈6.8 uH
Irated >=5 A
Isat >=5.5 A
acceptable DCR
acceptable package/layout.

---

# 43. ENVIRONMENT SENSOR PCB

Use:

SHT45-AD1B-R2.

Small remote PCB.

Approximate size:

20 × 20 mm.

Interface:

I2C

3V3
GND
SCL
SDA

using JST-XH 4P.

Place near acoustic working volume but away from PCB heat.

---

# 44. FPGA / PS / PL RESPONSIBILITY

## PL responsibility

PL handles timing-critical functions:

- shared ultrasonic timebase;
- 128-channel waveform generation;
- requested/calibration phase application;
- atomic map commit;
- serializer scheduling;
- TX channel sequencing;
- burst generation;
- RX capture timing;
- AD7606B acquisition interface;
- timestamps;
- capture buffers;
- basic phase/correlation primitives only if justified;
- hardware safety gating.

## PS responsibility

PS handles complex low-rate estimation:

- calibration sequencing orchestration;
- frequency sweep analysis;
- f0 extraction;
- amplitude analysis;
- carrier phase estimation;
- outlier filtering;
- robust nonlinear 6DoF solve;
- environment compensation;
- f_work selection;
- calibration database;
- Phase LUT generation.

Do not implement SVD/nonlinear optimizer in RTL merely to claim "all FPGA."

---

# 45. SOFTWARE ARCHITECTURE

Extend the inherited v1 software into at least:

v2/software/acoustic_model/

v2/software/calibration/

v2/software/characterization/

Suggested modules:

geometry.py
array_pose.py
sound_speed.py
tof.py
correlation.py
phase_estimator.py
frequency_sweep.py
transducer_characterization.py
fwork_optimizer.py
channel_calibration.py
calibration_database.py
phase_solver.py
field_solver.py

Names may differ if architecture improves.

Keep concepts modular.

---

# 46. CALIBRATION DATA FORMAT

Create machine-readable calibration storage.

Suggested:

v2/config/calibration/

or:

v2/hardware/characterization/

Use:

JSON
CSV
or both.

Each dataset must identify:

project version
hardware revision
PCB serial
TX batch
RX batch
date/time
temperature
humidity
sound speed
face geometry
f_work
per-channel measurements
source measurement files
software version
Git commit.

Do not create calibration constants with unknown provenance.

---

# 47. PCB BOM SOURCE OF TRUTH

Use the approved complete BOM baseline generated for v2.

If available locally, import it into:

v2/hardware/bom/

Recommended canonical artifacts:

BOM_MASTER.xlsx
BOM_MASTER.csv
BOM_LOCK.md

Do not let the runtime project depend on Excel parsing.

Generate a text/CSV form that Codex and humans can inspect.

BOM substitution status classes:

LOCK
PREFERRED
PRIMARY / BATCH-QUALIFY
DNP / TUNING
PROVISIONAL.

Codex must not stop simply because a PREFERRED part is temporarily unavailable if a qualified alternate rule exists.

---

# 48. TCT40 PROCUREMENT POLICY

Recommended purchase:

TCT40-10T:
160 units

installed:
128.

TCT40-10R:
16 units

installed:
8.

Purpose:

screening
batch matching
spares
replacement.

Do not mix arbitrary vendors/batches in the final competition array unless characterization proves compatibility.

---

# 49. HARDWARE BRING-UP — DO NOT POPULATE EVERYTHING FIRST

Perform staged hardware validation.

## PH0 — module/prototype validation

May use temporary:
- AD7606 module;
- SHT45 module;
- 1–2 TX;
- 1 RX;
- bench PSU.

Goal:
verify the measurement concept.

Do not call PH0 final hardware.

---

## PH1 — single TX/RX electrical validation

Validate:

TX logic
TC4427 waveform
TCT40 transmission
RX response
OPA response
ADC acquisition
frequency sweep
burst capture.

Evidence:

scope screenshots
raw ADC traces
power measurements.

---

## PH2 — serializer / small channel block

Validate:

4 TX
then
16 TX.

Verify:

relative phase
clock integrity
latch timing
OE safety
current
temperature.

---

## PH3 — one complete 64TX+4RX PCB

Validate:

all TX channels
all RX channels
serializer map
channel identity
phase consistency
power
temperature
calibration scan.

---

## PH4 — dual board geometry calibration

Install:

Upper
+
Lower.

Run:

512-path calibration.

Estimate:

tx,ty,tz
roll,pitch,yaw.

Compare measured:

tz

to manual mechanical reference as independent validation.

Do not remove manual reference measurement entirely.

Self-calibration must be independently checked.

---

## PH5 — complete 128-channel phase calibration

Characterize:

f0_i
A_i
delta_phi_i.

Select:

single f_work.

Generate:

calibration table.

---

## PH6 — acoustic levitation

Start:

very lightweight EPS

then staged mass:

5 mg
10 mg
25 mg
50 mg target.

Record:

mass
diameter
material
density estimate
gap
f_work
VDRV
temperature
humidity
calibration version
duration.

No visual-only claim.

---

# 50. IMPORTANT — SELF-CALIBRATION DOES NOT REMOVE ALL MANUAL METROLOGY

The new calibration system shall reduce reliance on manually entering:

100 mm gap

but must not eliminate independent verification.

During engineering validation compare:

automatically measured gap
vs
caliper/ruler/reference measurement.

Acceptance shall quantify:

absolute error
repeatability
pose residual.

Only after validation may self-calibration become normal operational input.

---

# 51. RTL VERIFICATION

All inherited v1 RTL tests must run against v2.

Add new tests for:

RX acquisition controller
burst generator
channel scan scheduler
AD7606B interface
calibration mode switching
RX blank logic
timestamp consistency
capture buffer boundaries
safe interrupt/abort
calibration-to-normal-mode transition.

Do not weaken inherited tests.

---

# 52. SOFTWARE TESTS

Add unit/integration tests for:

sound speed calculation
synthetic ToF recovery
carrier phase refinement
integer wavelength disambiguation
6DoF pose recovery
noise sensitivity
outlier rejection
bidirectional measurement
f0 extraction
common f_work selection
phase correction
calibration database serialization.

Synthetic pose test should inject known:

translation
roll
pitch
yaw

then recover them.

Report numerical error.

---

# 53. DETERMINISM

For fixed:

geometry
environment
measurement vectors
seed
calibration parameters

software calibration result must be deterministic within defined floating-point tolerance.

For RTL fixed input:

trace must remain deterministic.

Document:

seed
repeat count
comparison method
hashes/tolerances.

---

# 54. CROSS VALIDATION

Use independent evidence.

Preferred:

A:
Python/unit tests

B:
Icarus or Verilator RTL tests

C:
Vivado 2025.2 XSim

D:
Vivado synthesis when exact device becomes available

E:
hardware oscilloscope / ADC measurements when physical hardware exists.

Do not confuse these levels.

---

# 55. VIVADO 2025.2

Vivado 2025.2 is authoritative for target FPGA work.

Maintain reproducible project scripts.

Prefer:

v2/scripts/create_project.tcl

over a manually configured project only.

If exact FPGA ordering code/package remains unknown:

do NOT guess.

Generic simulation can continue.

Target synthesis/implementation must remain:

BLOCKED_BY_BOARD_FACT.

---

# 56. EXISTING BOARD BLOCKERS

Revalidate current blocker records.

Known classes include:

- exact Zynq part/package/speed grade;
- connector/pin conflicts;
- GPIO bank VCCO;
- serializer real electrical timing;
- actual TCT40 mechanical/electrical batch data;
- physical levitation data.

Do not silently mark them resolved because v2 exists.

If new evidence resolves one:

record:
source
date
method
affected files
validation.

---

# 57. PCB FREEZE GATE

DO NOT produce a "manufacturing-ready" claim until:

1. TCT40 real body diameter measured;
2. TX/RX pin pitch measured;
3. pin diameter measured;
4. package height measured;
5. batch safe drive range confirmed;
6. Zynq connector pin mapping confirmed;
7. FPGA VCCO confirmed or final translator architecture verified;
8. serializer timing validated;
9. power design ERC/check complete;
10. analog front-end gain checked;
11. AD7606 reference schematic checked;
12. connector pin mapping reviewed;
13. DRC passes;
14. BOM contains no unresolved mandatory parts.

Before this gate use:

PCB_PROPOSED

not:

PCB_MANUFACTURING_READY.

---

# 58. PCB DELIVERABLES

When the PCB design phase begins, maintain:

v2/hardware/pcb/

with:

schematics
PCB source
PDF schematic export
BOM
placement
Gerbers
drill files
assembly drawings
connector pinouts
power tree
test point map
bring-up checklist
revision history.

Do not commit huge temporary EDA cache.

---

# 59. TEST POINT REQUIREMENT

At minimum expose:

TP_VDRV
TP_3V3
TP_5V_A
TP_VREF

TP_SRCLK
TP_RCLK
TP_OE
TP_CLR

selected serializer DATA points

driver inputs

driver outputs

RX preamp stages

ADC input test points

current-monitor points.

Do not design a 128-channel board with no accessible debugging points.

---

# 60. SAFETY

Default physical state:

outputs disabled.

Conditions that must result in safe acoustic shutdown:

FPGA reset
missing digital cable
OE fault
software stop
hardware KILL
power brownout where possible.

Do not depend solely on software for safety.

The hardware KILL path must remain independently understandable.

---

# 61. AI-PROBLEM / DECISION WORKFLOW

For any major unresolved issue create:

AI-problem/problem/P-YYYYMMDD-NNN__topic.md

Include:

Problem ID
Current Version
repository facts
evidence
attempted approaches
constraints
options
affected modules
risk.

Do not repeatedly ask the same question without new evidence.

If a matching decision exists:

verify:
Problem ID
Problem Hash
Version
evidence freshness.

If mismatch:

REVALIDATE_DECISION.

---

# 62. AI MEMORY / INTERACTION RECORD

Follow current project AGENTS.md.

Maintain:

AI-chat-memory/

for actual external ChatGPT source when accessible.

Maintain:

AI-interaction-memory/

for observable Codex/user project interaction.

Do not fabricate external ChatGPT history.

If access is blocked:

record:

CHAT_MEMORY_ACCESS_BLOCKED

and continue using repository facts.

Do not export hidden reasoning/system prompts/private provider content.

---

# 63. VERSION INTERACTION MEMORY

This explicit user instruction approving v2 and defining v2 as a complete inherited standalone project must be persisted according to the repository interaction-memory rules.

The record must make clear:

- user explicitly approved v2;
- v1 becomes frozen;
- v2 inherits the complete useful v1 project;
- v2 is independently runnable;
- future "continue" remains in v2;
- v3 requires another explicit user approval.

---

# 64. REPOSITORY CLEANLINESS

At every major stage review:

imports
paths
scripts
configs
Vivado source lists
test discovery
packaging
Git ignore rules
generated artifacts.

Do not leave:

test2
new_final
final_final
backup2

style directories.

Use meaningful engineering names.

Keep root clean.

---

# 65. v2 STANDALONE REPRODUCIBILITY GATE

Before v2 completion:

perform a clean reproduction.

Required procedure:

1. clone repository cleanly;
2. checkout tested commit;
3. enter v2;
4. create fresh environment;
5. install v2 dependencies only;
6. run Python tests;
7. run acoustic model;
8. run calibration tests;
9. run RTL regression;
10. run available Vivado/XSim checks;
11. verify no normal execution path points into v1;
12. hash important generated reference outputs.

Required status:

V2_STANDALONE_REPRODUCIBILITY = PASS.

If normal v2 operation needs v1 engineering files:

REVISE.

---

# 66. INHERITED BASELINE GATE

Before claiming new v2 work successful:

run inherited v1 acceptance tests on v2.

Required status:

INHERITED_BASELINE_PASS.

This must include at least:

128-channel generation
requested phase
calibration phase
atomic commit
safe reset
deterministic timebase
geometry model
12 mm pitch
configurable face gap
STANDING_WAVE
FOCUS
Python/RTL comparison.

---

# 67. v2 NEW ACCEPTANCE CRITERIA

v2 digital/software architecture passes when:

1. v2 is a complete standalone project;
2. v1 is frozen and unchanged;
3. inherited v1 regression passes;
4. 128 TX + 8 RX architecture is represented;
5. 4 RX per board coordinates exist;
6. bidirectional 512-path calibration is modeled;
7. synthetic TOF estimation passes;
8. phase refinement passes;
9. 6DoF pose recovery passes;
10. robust outlier handling is tested;
11. environment sound-speed compensation exists;
12. frequency sweep pipeline exists;
13. one common f_work is selected;
14. per-channel phase calibration is produced;
15. amplitude/channel-health records exist;
16. RX blanking control exists;
17. AD7606B acquisition interface is implemented or accurately modeled;
18. hardware architecture/BOM is documented;
19. PCB interfaces are documented;
20. inherited digital safety remains intact;
21. no invented FPGA pins exist;
22. no fake hardware results exist;
23. reproducibility passes.

---

# 68. HARDWARE ACCEPTANCE REMAINS SEPARATE

Digital/software v2 completion DOES NOT mean:

physical hardware accepted.

Physical hardware acceptance requires real:

oscilloscope traces
ADC traces
current/voltage data
temperature data
frequency sweeps
geometry measurements
phase calibration data
levitation data.

Use statuses:

NOT_RUN
BLOCKED
PASS
FAIL

accurately.

Never write:

"50 mg levitation PASS"

without physical evidence.

---

# 69. V2 EXECUTION STAGES

Recommended sequence:

STAGE V2.0
Version migration + freeze v1

STAGE V2.1
Inherited baseline reproduction

STAGE V2.2
Calibration architecture + synthetic model

STAGE V2.3
RX / ADC RTL architecture

STAGE V2.4
Transducer characterization software

STAGE V2.5
6DoF geometry solver

STAGE V2.6
Unified calibration database + f_work optimizer

STAGE V2.7
PCB schematic architecture + BOM freeze candidate

STAGE V2.8
Target-board integration when board facts permit

STAGE V2.9
PH0 / prototype hardware

STAGE V2.10
Array PCB hardware bring-up

STAGE V2.11
Full self-calibration

STAGE V2.12
Levitation validation.

Stages do NOT create new versions.

---

# 70. LIMITED ITERATION RULE

Do not enter endless repair loops.

Architecture review:
1–2 meaningful rounds.

Major technical problem:
2–3 evidence-backed rounds.

Reviewer correction:
2–3 rounds.

If no progress after repeated attempts:

perform:

Root Cause Analysis
→ assumption review
→ compare v1 baseline
→ alternative architecture
→ escalate to user if major decision required.

No repeated identical prompts without new evidence.

---

# 71. STOP OPTIMIZATION RULE

When all are true:

Blocking critical to current stage = 0
Critical Bugs = 0
Core functionality complete
Inherited regression PASS
New v2 tests PASS
Cross-validation acceptable
Repository clean
Reproducibility PASS
No known fake/stub path
Overall quality approximately >=90%

then:

STOP_OPTIMIZATION_AND_DELIVER

List low-value remaining tasks under:

OPTIONAL_IMPROVEMENTS.

Do not endlessly polish.

---

# 72. FORBIDDEN BEHAVIORS

Do NOT:

- modify frozen v1;
- create v3 without approval;
- guess Zynq pins;
- guess FPGA package;
- guess VCCO;
- fabricate Vivado PASS;
- fabricate physical levitation;
- fabricate TCT40 measurement;
- claim a module test as final hardware;
- weaken acceptance criteria for PASS;
- use mock data while reporting it as real measurement;
- silently replace BOM parts;
- individually drive each TX at a different frequency;
- average geometrically different RX distances directly;
- use only carrier phase as absolute range;
- use loose Dupont wiring as final high-speed interconnect;
- directly connect raw RX to FPGA;
- directly drive TCT40 from FPGA GPIO;
- overwrite previous evidence;
- force push;
- delete Git history;
- publish/release/deploy without user approval.

---

# 73. REQUIRED DOCUMENTATION

At minimum v2 must document:

1. complete system architecture;
2. v1→v2 migration;
3. standing-wave principle;
4. acoustic radiation force principle;
5. FPGA phased-array principle;
6. self-calibration principle;
7. TOF + carrier phase method;
8. 6DoF pose estimation;
9. common f_work selection;
10. transducer phase calibration;
11. TX/RX PCB architecture;
12. ADC architecture;
13. power architecture;
14. cable/interface mapping;
15. coordinate definition;
16. characterization workflow;
17. hardware bring-up;
18. validation matrix;
19. blockers;
20. limitations.

---

# 74. FINAL v2 REPORT FORMAT

At the end of every major Codex iteration report:

PROJECT_ID
project_name
repository
workspace_path
branch
active_version
stage
local_HEAD
origin_HEAD

Then:

## Implemented

## Inherited From v1

## New in v2

## Validated

## Real Tool Evidence

## Reproducibility

## Hardware Status

## Not Validated

## Blocking

## Risks

## BOM / PCB Status

## AI-problem Status

## Files Changed

## Git Status

## Next Recommended Stage

End with exactly one engineering review result:

ACCEPT
ACCEPT WITH LIMITATIONS
or
REVISE

Scope the result to the work actually reviewed.

Do not issue whole-platform ACCEPT while physical hardware blockers remain.

---

# 75. FIRST v2 TASK TO EXECUTE NOW

Execute only the following first major stage before expanding scope:

## V2_BOOTSTRAP_AND_INHERITED_BASELINE

Goal:

1. preflight repository;
2. capture current Codex/user interaction checkpoint;
3. freeze v1;
4. create full standalone v2 by inheriting complete valid v1 engineering baseline;
5. create V1_TO_V2_MIGRATION.md;
6. update root version metadata;
7. update README / AGENTS / shared state;
8. rerun inherited Python tests;
9. rerun Icarus regression;
10. rerun Vivado 2025.2 XSim regression where available;
11. run repository/path audit;
12. perform clean v2 standalone reproduction;
13. prove v2 does not depend on ../v1;
14. store fresh v2 evidence;
15. commit and push to the existing repository;
16. verify remote SHA.

Do NOT yet fabricate PCB Gerbers.

Do NOT claim target synthesis if exact Zynq part is still unresolved.

Do NOT yet claim physical self-calibration.

Done When:

v1 is frozen
AND
v2 is complete
AND
v2 inherited regression passes
AND
v2 standalone reproducibility passes
AND
root current state points to v2
AND
GitHub remote matches the reviewed local commit.

Then stop and return the required final report for independent ChatGPT/user review before proceeding deeper into v2 hardware implementation.