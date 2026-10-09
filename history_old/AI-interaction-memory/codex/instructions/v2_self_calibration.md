# SonoField-FPGA v2
# Stage: SELF_CALIBRATION_SOFTWARE_AND_DIGITAL_SYSTEM

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

active_version:
v2

primary_FPGA:
Robei Octagonal Board / Zynq-7020

primary_EDA:
AMD Vivado 2025.2

---

# 1. VERSION RULE

This task CONTINUES v2.

Do NOT create v3.

v1 remains frozen.

All implementation must occur inside the complete standalone:

v2/

project.

v2 must continue to remain independently runnable without normal engineering dependencies on:

../v1/

This stage adds software, RTL, models, tests, configuration and Vivado integration to the existing complete v2 baseline.

---

# 2. THIS STAGE GOAL

Complete the SOFTWARE / DIGITAL DESIGN of the current SonoField-FPGA architecture before PCB implementation.

This stage shall implement and validate:

1. complete 128-TX phased-array control;
2. complete 8-RX calibration acquisition architecture;
3. AD7606B digital acquisition interface;
4. automatic TX-by-TX calibration scheduling;
5. ultrasonic burst generation;
6. RX blanking/control logic;
7. raw ADC capture;
8. coarse Time-of-Flight estimation;
9. carrier-phase fine estimation;
10. automatic upper/lower array relative-pose estimation;
11. transducer frequency sweep and response characterization;
12. common operating-frequency selection;
13. per-channel phase correction;
14. per-channel amplitude/health characterization;
15. environment-dependent sound-speed compensation;
16. automatic Phase LUT regeneration;
17. calibration database;
18. software/RTL cross-validation;
19. Vivado 2025.2 project integration;
20. full v2 digital-system validation.

PCB physical layout, Gerber and manufacturing files are explicitly OUT OF SCOPE for this stage.

---

# 3. FIRST ACTION — READ CURRENT REPOSITORY FACTS

Before changing code, read:

README.md
AGENTS.md

shared/PROJECT_STATE.json
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

and the complete current:

v2/

tree.

Also inspect the available Zynq board references under:

E:\Codex-project\AMD-SonoField-FPGA\Zynq7020

Do not guess unresolved board facts.

Before implementation report:

PROJECT_ID
repository
workspace
branch
active_version
current_stage
local HEAD
origin/main HEAD
current blockers.

---

# 4. HARDWARE PARAMETERS ARE FIXED BY THE BOM BASELINE

For this software stage, treat the following hardware architecture as the authoritative target.

Do NOT stop merely because the PCB has not yet been designed.

The software shall be developed against these parameters.

## TX

Transmitter:

TCT40-10T

nominal:
40 kHz
10 mm class

TX count:

128

Upper:
64

Lower:
64.

Geometry:

8 × 8 per board.

Pitch:

12 mm.

Local TX coordinates:

X,Y =
{
-42,
-30,
-18,
-6,
+6,
+18,
+30,
+42
} mm.

Coordinate reference:

CENTER OF RADIATING SURFACE.

Nominal face gap:

100 mm.

Mechanical allowable range:

90–115 mm.

---

# 5. RX TARGET

Receiver:

TCT40-10R

RX count:

8.

Upper:

4 RX.

Lower:

4 RX.

Initial local coordinates:

(+54,+54)
(-54,+54)
(-54,-54)
(+54,-54) mm.

These values shall exist in software configuration, not be scattered as magic numbers.

---

# 6. ADC TARGET

Primary ADC:

AD7606BBSTZ-RL.

The digital architecture and model shall match this component.

Target ADC properties:

channels:
8 simultaneous

resolution:
16 bit

maximum sample rate:
800 kSPS/channel.

Initial software baseline:

ADC_SAMPLE_RATE_HZ = 800_000

TX nominal carrier:

40_000 Hz class.

Therefore nominal:

20 ADC samples / carrier cycle.

The ADC model and acquisition RTL must support lower configurable sample rates if required.

Do NOT hard-code all DSP to exactly 800 kSPS.

Use configuration parameters.

---

# 7. AD7606B INTERFACE

Implement a real AD7606B-oriented digital interface architecture.

Prefer a serial interface using multiple DOUT lanes if this provides sufficient bandwidth and reduces FPGA IO.

At minimum model/control:

CONVST
BUSY
RESET
CS
SCLK
DOUTA
DOUTB
DOUTC
DOUTD

and any other required signals according to the actual AD7606B datasheet.

IMPORTANT:

Do not invent signal timing.

Before implementing:

read the AD7606B timing requirements.

Create:

v2/docs/hardware/AD7606B_INTERFACE.md

containing:

- chosen interface mode;
- sampling rate;
- conversion trigger timing;
- BUSY behavior;
- data-frame structure;
- SCLK requirement;
- capture ordering;
- channel ordering;
- reset/startup;
- oversampling configuration if used;
- timing margins.

Create a behavioral ADC model for RTL simulation.

---

# 8. ADC CHANNEL MAPPING

Define one permanent logical mapping.

Suggested:

ADC_CH0 = UPPER_RX0
ADC_CH1 = UPPER_RX1
ADC_CH2 = UPPER_RX2
ADC_CH3 = UPPER_RX3

ADC_CH4 = LOWER_RX0
ADC_CH5 = LOWER_RX1
ADC_CH6 = LOWER_RX2
ADC_CH7 = LOWER_RX3.

Store this mapping in a single configuration source.

Do not duplicate independent inconsistent mappings in:

Python
RTL
Vivado
documentation.

Generate other representations from one source where practical.

---

# 9. FPGA / PS ARCHITECTURE

Maintain a clear PS/PL partition.

## PL shall handle

Timing-critical real-time functions:

- common ultrasonic timebase;
- 128-channel TX waveform generation;
- requested-phase application;
- calibration-phase application;
- atomic map update;
- TX enable/mask;
- serializer output;
- calibration-mode switching;
- TX channel sequencer;
- burst generator;
- RX group selection;
- AD7606B sampling;
- ADC frame capture;
- timestamps;
- sample buffering;
- hardware safety;
- interrupt/event signaling.

PL must not perform complex nonlinear geometry optimization unless there is a measured need.

## PS / software shall handle

- calibration procedure orchestration;
- ADC trace processing;
- cross-correlation;
- TOF estimation;
- carrier phase estimation;
- frequency sweep processing;
- f0 extraction;
- response amplitude extraction;
- outlier rejection;
- 6DoF board-pose solve;
- environmental sound-speed correction;
- common f_work optimization;
- per-channel calibration generation;
- Phase LUT generation;
- calibration database management;
- reports and visualization.

---

# 10. REQUIRED RTL MODULES

Reuse valid inherited modules and add the missing v2 calibration/acquisition modules.

Suggested architecture:

v2/rtl/

timing/
  ultrasonic_timebase.sv
  burst_generator.sv

phase/
  phase_channel.sv
  phase_bank.sv
  calibration_ram.sv
  phase_commit.sv

output/
  channel_waveform.sv
  serializer.sv
  output_enable.sv

acquisition/
  ad7606b_if.sv
  adc_sample_buffer.sv
  adc_frame_unpack.sv

calibration/
  calibration_scheduler.sv
  tx_scan_controller.sv
  rx_group_controller.sv
  calibration_capture_controller.sv

control/
  register_bank.sv
  safety_controller.sv
  event_controller.sv

top/
  sono_top.sv

Existing stable module names shall remain stable where appropriate.

---

# 11. CALIBRATION MODE STATE MACHINE

Implement a formal hardware calibration controller.

Recommended states:

IDLE

PREPARE_CALIBRATION

SELECT_TX

SET_RX_GROUP

BLANK_SETTLE

TX_BURST

PROPAGATION_WAIT

RX_CAPTURE

RINGDOWN_CAPTURE

FRAME_DONE

NEXT_RX_OR_TX

DIRECTION_SWITCH

CALIBRATION_DONE

ABORT

ERROR.

All relevant delays must be parameterizable.

Do not encode unexplained timing constants in state logic.

Expose status registers.

---

# 12. TX CALIBRATION SEQUENCE

Support:

LOWER TX0..63
→
UPPER RX0..3

followed by:

UPPER TX0..63
→
LOWER RX0..3.

The complete sequence represents:

512 TX-RX paths.

Store identifiers with captured data:

TX array
TX index
RX array
RX index
capture sequence number
timestamp
carrier frequency
ADC rate
burst cycles.

This metadata must accompany raw samples.

---

# 13. BURST GENERATOR

Implement configurable ultrasonic burst generation.

Parameters:

carrier frequency
number of cycles
start phase
TX channel
guard time
drive enable.

Initial baseline:

16 cycles.

But:

BURST_CYCLES

must be configurable.

Support characterization sweeps where carrier changes between captures.

All TX channels within a normal acoustic field still use one shared f_work.

---

# 14. CALIBRATION CAPTURE WINDOW

Provide configurable:

pre-trigger samples
main-capture samples
ringdown samples.

A capture should support:

burst arrival
steady carrier
post-burst ringdown.

Do not collect only one scalar amplitude.

Retain complete raw sample vectors for offline validation.

---

# 15. SIMULATED AD7606B

Because PCB/hardware is not yet available, implement a realistic behavioral model.

The simulation environment shall be able to inject:

8 ADC channels

with configurable:

TOF
carrier phase
amplitude
noise
DC offset
gain mismatch
channel delay
frequency response
ringdown
clipping.

This is critical.

Do NOT test calibration algorithms only on ideal clean sine waves.

---

# 16. SYNTHETIC ACOUSTIC SIGNAL MODEL

Create a software reference generator capable of producing realistic receiver traces.

For one TX→RX path model:

- propagation delay;
- geometric distance;
- inverse-distance amplitude term or documented approximation;
- transducer directional response approximation;
- channel gain;
- per-TX phase error;
- per-RX phase error;
- noise;
- environmental sound velocity;
- ring-up;
- ring-down.

Use this to generate reference ADC vectors.

Save deterministic test vectors.

---

# 17. TOF ESTIMATION

Implement:

cross-correlation
or
matched-filter

based coarse TOF estimation.

Inputs:

known transmitted burst
recorded ADC vector
sample rate.

Outputs:

sample_delay
fractional delay if implemented
TOF seconds
coarse distance
confidence
correlation peak
second-peak ratio or similar quality metric.

Test under:

noise
amplitude variation
phase variation
small offsets
large offsets.

---

# 18. SUB-SAMPLE TOF REFINEMENT

800 kSPS produces:

1.25 µs/sample.

Air propagation distance per raw sample is approximately:

~0.43 mm.

Do not assume raw integer-sample TOF is the final distance accuracy.

Implement at least one sub-sample refinement method such as:

parabolic peak interpolation

or another justified method.

Document achievable synthetic error.

---

# 19. CARRIER PHASE FINE ESTIMATION

After coarse distance resolves wavelength ambiguity:

estimate received carrier phase.

Possible robust method:

I/Q correlation
or
least-squares sinusoid fit.

Output:

phase_rad
phase_deg
quality/confidence.

Use:

delta_d =
lambda/(2*pi) * delta_phi

only after coarse wavelength index is known.

Handle phase wrapping correctly.

---

# 20. PHASE DATA MUST USE CIRCULAR MATH

Never perform naive arithmetic averaging of phase angles around:

-180° / +180°

boundary.

Implement:

circular mean
phase unwrap where justified
circular residual.

Add dedicated unit tests.

---

# 21. ENVIRONMENT MODEL

Implement sound-speed compensation based on:

SHT45 temperature
humidity.

Create:

software/calibration/sound_speed.py

or equivalent.

Input:

temperature
relative humidity.

Output:

sound speed.

Do not assume pressure if it is not measured unless explicitly documented.

Document the adopted approximation and error range.

Provide a default simulation environment.

---

# 22. GEOMETRY SELF-CALIBRATION

Implement the optimized method:

Do NOT solve independent positions for all 128 TX.

Use known rigid PCB geometry.

Solve one rigid transform:

R,t

between the upper and lower boards.

Unknowns:

tx
ty
tz
roll
pitch
yaw.

Use all valid directional paths.

Prefer:

robust nonlinear least squares.

Possible Python implementation:

scipy.optimize.least_squares

with robust loss.

Do not reinvent a numerical optimizer in RTL.

---

# 23. POSE SOLVER INPUT

Input shall contain:

known local TX coordinates
known local RX coordinates
measured path distances
measurement uncertainty/weights
environment sound speed.

Output:

translation
rotation
residuals
confidence
accepted/rejected paths.

Do not use direct simple averaging.

---

# 24. POSE SOLVER TESTS

Synthetic tests must include at least:

Case 1:
perfect nominal geometry.

Case 2:
Z gap deviation.

Example:
100 mm nominal
98.7 mm actual.

Case 3:
X/Y lateral offset.

Case 4:
roll.

Case 5:
pitch.

Case 6:
yaw.

Case 7:
combined 6DoF perturbation.

Case 8:
measurement noise.

Case 9:
outlier paths.

Case 10:
missing paths.

Recover the original synthetic transform.

Report:

translation error in mm
rotation error in degrees
RMS residual.

---

# 25. MANUAL REFERENCE COMPARISON

Even though software will calculate the real array pose automatically, keep support for manual measured geometry.

Input example:

manual_face_gap_mm

Purpose:

cross-check self-calibration.

Later hardware acceptance shall compare:

automatic estimate
vs
manual physical measurement.

Do not eliminate independent metrology.

---

# 26. FREQUENCY CHARACTERIZATION

Implement automatic per-TX frequency sweep.

Configurable initial range:

38.5 kHz
to
41.5 kHz.

Configurable step:

50 Hz
or
100 Hz.

For each TX:

trigger bursts at all frequencies.

Receive using opposite-side four RX.

Calculate:

response amplitude versus frequency
phase versus frequency
quality metric.

Do not interpret the received carrier frequency as "free-running TX resonance."

Estimate resonance from the response curve.

---

# 27. f0 EXTRACTION

For each channel estimate:

f0_i

from:

A_i(f).

Do not simply choose the maximum noisy bin if a better local interpolation can be implemented.

Possible:

quadratic peak refinement

around the maximum.

Store:

f0_i
peak amplitude
bandwidth estimate if reliable
quality flag.

---

# 28. ONE COMMON f_work

After all TX characterization:

calculate ONE:

f_work

for the full array.

Do not use:

f0_i

as individual per-channel operating frequencies.

Create:

software/characterization/fwork_optimizer.py

or equivalent.

Use robust objective.

Potential criteria:

maximize median normalized amplitude
minimize weak-channel count
avoid relying on extreme outliers
consider phase sensitivity.

Produce:

f_work
objective curve
selected channel count
rejected channels
justification.

---

# 29. CHANNEL PHASE CALIBRATION

At selected:

f_work

estimate for every TX:

delta_phi_i.

The calibration must compensate the actual acoustic phase difference, not merely digital output timing.

Use multiple opposite RX measurements.

First remove predicted propagation phase based on measured geometry.

Then estimate channel-specific residual phase.

Use circular statistics.

Store:

delta_phi_i
confidence
receiver agreement
measurement timestamp.

---

# 30. RX CALIBRATION CONSIDERATION

Do not blindly attribute all measured phase error to TX.

The measurement includes:

TX response
propagation
RX response
AFE
ADC timing.

At minimum document this identifiability limitation.

Because multiple TX are measured against the same RX set and measurements are bidirectional, implement a consistent relative calibration scheme.

The goal is:

reproducible array phase correction,

not falsely claiming an absolute intrinsic TX phase independent of receiver chain.

If necessary, choose a reference TX/RX and express values relative to it.

Document convention.

---

# 31. AMPLITUDE / CHANNEL HEALTH

At f_work derive:

relative amplitude A_i.

Classify channels using configurable thresholds:

GOOD
WEAK
OUTLIER
INVALID.

Do not permanently hard-code threshold without configuration.

Generate:

channel_health.csv

with:

channel
f0
A_fwork
phase_error
quality
status.

---

# 32. CHANNEL MASK

Integrate health result with the existing channel-mask architecture.

Do not automatically disable channels unless the policy is explicitly configured.

Support:

recommended_mask

and:

active_mask

as distinct concepts.

---

# 33. CALIBRATION DATABASE

Implement versioned calibration data storage.

Suggested structure:

v2/config/calibration/

latest/
archive/

Each calibration record shall include:

schema_version
project_version
Git commit
board_revision
upper_board_id
lower_board_id
TX batch
RX batch
timestamp
temperature
humidity
sound_speed
ADC_sample_rate
burst_configuration
measured_pose
f_work
per-channel f0
per-channel amplitude
per-channel phase
channel status
solver residuals
source raw-data paths.

Use JSON as canonical machine-readable format.

CSV may be exported for inspection.

---

# 34. RAW DATA RETENTION

Do not store only final calibration numbers.

Create structured raw evidence.

Example:

evidence/calibration/raw/

or build artifact path.

Raw samples must identify:

TX
RX
frequency
capture ID.

Avoid uncontrolled huge Git commits.

Large generated waveforms/raw captures may remain ignored locally while compact summary vectors/hashes are committed.

Document policy.

---

# 35. PHASE LUT REGENERATION

Use:

measured pose
+
f_work
+
sound speed
+
channel phase calibration

to regenerate field LUTs.

Implement:

target coordinate
→ real TX position
→ propagation distance
→ ideal phase
→ calibration correction
→ quantized 8-bit phase.

Retain:

requested phase
and
calibration phase

separately.

Do not directly bake them into one opaque table.

---

# 36. REAL GEOMETRY VS NOMINAL GEOMETRY

Software shall distinguish:

nominal_geometry

and:

calibrated_geometry.

Before calibration:

use nominal:
gap = 100 mm
zero pose offset.

After calibration:

use measured transform.

Allow the user to switch explicitly between:

NOMINAL
CALIBRATED

for comparison.

---

# 37. ACOUSTIC FIELD MODEL

Extend existing field model to support:

- actual board transform;
- measured f_work;
- per-channel phase correction;
- disabled channels;
- relative amplitude weighting for analysis;
- environment sound speed.

Produce visualization of at least:

XY pressure slice
XZ pressure slice
YZ pressure slice.

These are model outputs, not physical measurements.

Mark them accordingly.

---

# 38. CALIBRATION VISUALIZATION

Generate useful engineering figures:

1. measured TX resonance distribution;
2. amplitude response curves;
3. per-channel f0 heatmap;
4. per-channel phase-error heatmap;
5. per-channel amplitude heatmap;
6. board pose diagram;
7. distance residual histogram;
8. calibration residual by path;
9. nominal vs calibrated field comparison.

Use Matplotlib.

Do not use visualization as replacement for numerical validation.

---

# 39. HOST / PS SOFTWARE INTERFACE

Define a formal register/API contract between:

PS
and
PL.

Document:

v2/docs/architecture/PS_PL_CALIBRATION_INTERFACE.md

At minimum specify:

mode
TX channel
burst cycles
carrier setting
RX group
ADC capture length
start
abort
busy
done
error
buffer address
sample count
calibration-map write
commit
channel mask.

Do not allow software and RTL to use undocumented magic register offsets.

---

# 40. REGISTER MAP

Create a single authoritative machine-readable register specification.

Possible:

config/register_map.yaml

Then generate:

RTL definitions
Python constants
documentation

from it where practical.

Avoid maintaining three independent register maps manually.

---

# 41. ADC BUFFERING

Calculate required capture storage.

For:

8 channels
16 bits
N samples.

Memory:

8 × 2 × N bytes.

Design buffering accordingly.

Do not allocate arbitrarily huge BRAM.

Support configurable capture lengths.

Use BRAM for bounded short captures.

If future continuous capture requires DDR, leave a clean architecture boundary.

Do not overbuild DMA unless currently necessary.

---

# 42. ADC SAMPLE FORMAT

Define:

signed or unsigned interpretation
endianness
channel ordering
frame ordering
sample timestamp
conversion index.

Add round-trip tests:

behavioral ADC
→ RTL capture
→ software decode

must reproduce exact injected samples.

---

# 43. DIGITAL TIMING

ADC control, TX carrier and serializer clocks may belong to different rates.

Explicitly review:

clock domains
CDC
reset synchronization.

Do not pass control/status signals asynchronously without synchronization.

Run Vivado CDC/timing reports where possible.

Document clocks.

---

# 44. CURRENT BOARD CLOCK FACT

Repository currently records:

N18
33 MHz

as the documented reference-clock precedence.

Use this fact only as currently approved.

Do not invent exact PLL/MMCM values without calculating legal configurations.

Clock architecture shall support:

- FPGA system clock;
- ultrasonic phase timebase;
- serializer clock;
- ADC serial clock.

Use integer/fractional phase accumulation where appropriate.

---

# 45. FPGA PART BLOCKER

If exact Zynq-7020 package / speed grade remains unresolved:

generic RTL
behavioral simulation
Icarus
Python
Vivado XSim

may proceed.

Do NOT falsely claim:

target synthesis
implementation
bitstream
timing closure

for an invented part.

Keep the blocker explicit.

---

# 46. VIVADO 2025.2 PROJECT

Maintain a reproducible Vivado project.

Required:

v2/scripts/create_project.tcl

and/or equivalent scripts.

Include all:

RTL
TB
generated register definitions
simulation sources.

Provide commands for:

XSim
elaboration
simulation.

If target part becomes known during this stage:

attempt synthesis.

Otherwise clearly report:

TARGET_SYNTHESIS_BLOCKED_BY_B01.

---

# 47. SECOND RTL TOOLCHAIN

Continue using:

Icarus Verilog

where compatible.

Use it as independent RTL evidence.

Preferred verification layers:

Python reference
+
Icarus
+
Vivado XSim.

If Verilator is useful, it may be added but is not mandatory.

---

# 48. REQUIRED NEW RTL TESTS

Add self-checking tests.

At minimum:

CAL-TB01:
burst length / frequency.

CAL-TB02:
single TX selection.

CAL-TB03:
64-channel scan order.

CAL-TB04:
lower-to-upper direction.

CAL-TB05:
upper-to-lower direction.

CAL-TB06:
RX blank state.

CAL-TB07:
AD7606 BUSY timing model.

CAL-TB08:
ADC frame capture.

CAL-TB09:
8-channel ordering.

CAL-TB10:
capture-buffer boundaries.

CAL-TB11:
abort during calibration.

CAL-TB12:
return to normal field mode.

CAL-TB13:
safe OE during reset.

CAL-TB14:
frequency sweep control.

CAL-TB15:
behavioral ADC injected-vector exact comparison.

Inherited phase tests must also continue passing.

---

# 49. REQUIRED SOFTWARE TESTS

At minimum:

SW-T01:
sound-speed model.

SW-T02:
synthetic burst generation.

SW-T03:
integer-sample TOF.

SW-T04:
fractional TOF.

SW-T05:
TOF under noise.

SW-T06:
carrier phase.

SW-T07:
phase wrap.

SW-T08:
distance coarse+fine fusion.

SW-T09:
nominal pose solve.

SW-T10:
translation-only pose.

SW-T11:
rotation-only pose.

SW-T12:
combined 6DoF.

SW-T13:
outlier rejection.

SW-T14:
missing path.

SW-T15:
frequency sweep f0 recovery.

SW-T16:
common f_work optimizer.

SW-T17:
per-channel phase calibration.

SW-T18:
calibration JSON round-trip.

SW-T19:
nominal vs calibrated geometry.

SW-T20:
Phase LUT regeneration.

---

# 50. SYSTEM-LEVEL SYNTHETIC TEST

Create one complete synthetic system test.

Example:

Known ground truth:

gap:
98.8 mm

tx:
+0.7 mm

ty:
-0.5 mm

roll:
+0.35°

pitch:
-0.20°

yaw:
+0.15°

temperature:
26.5°C

humidity:
55%

TX resonance distribution:
synthetically varied around 40 kHz.

TX phase errors:
random fixed deterministic seed.

Generate:

all 512 path captures.

Then run the COMPLETE v2 calibration pipeline from raw synthetic ADC traces.

Expected outputs:

pose recovery
f0_i recovery
f_work selection
delta_phi_i
calibration database
corrected Phase LUT.

Compare against injected ground truth.

This shall be a major v2 acceptance test.

---

# 51. NOISE / ROBUSTNESS TEST

Repeat synthetic calibration under increasing noise.

At least several SNR levels.

Determine when:

pose
TOF
phase
f0

begin to fail.

Do not simply say:

"algorithm is robust."

Produce numerical limits from simulation.

---

# 52. DETERMINISTIC REPRODUCIBILITY

Use fixed random seeds.

For deterministic synthetic validation:

run at least:

3 repeated runs.

Compare:

calibration JSON
important CSVs
key numerical outputs.

Floating point tolerance must be explicitly defined.

Record hashes where appropriate.

---

# 53. CONFIGURATION

Create one authoritative system configuration.

Suggested:

v2/config/system_baseline.yaml

or JSON.

Include:

TX count
RX count
pitch
nominal gap
gap range
TX coordinates
RX coordinates
ADC sample rate
ADC channels
carrier nominal
frequency sweep
phase bits
burst cycles
capture lengths
hardware part names.

Do not distribute these constants across source files.

---

# 54. HARDWARE PART CONFIG

Create a machine-readable:

v2/config/hardware_parts.yaml

containing the approved BOM device identifiers relevant to software.

At minimum:

TX = TCT40-10T
RX = TCT40-10R

ADC = AD7606BBSTZ-RL

TX_DRIVER = TC4427AEOA713

SERIALIZER = SN74LVC595APWR

LEVEL_TRANSLATOR = SN74AXC8T245PWR

CLOCK_BUFFER = SN74LVC244APWR

RX_SWITCH = TMUX1574PWR

RX_OPAMP = OPA4192IPWR

RX_VREF = REF5025AIDR

ENV_SENSOR = SHT45-AD1B-R2.

Software should be traceable to the hardware BOM.

Do not make software electrical limits contradict the BOM.

---

# 55. ADC CONFIGURATION SOURCE OF TRUTH

Create explicit:

ADC model/config.

Example fields:

part_number:
AD7606BBSTZ-RL

channel_count:
8

resolution_bits:
16

sample_rate_hz:
800000

interface_mode:
chosen serial mode

vdrive:
3.3V target

analog_range:
must be selected according to the actual datasheet and AFE design.

IMPORTANT:

Do NOT guess AD7606B analog input range configuration.

Read the datasheet and document the selected range.

Make RX AFE gain consistent with selected ADC input range.

If there is uncertainty:

model multiple valid range options
and identify which must be physically strapped/configured later.

---

# 56. ADC SATURATION HANDLING

Calibration software must detect clipping/saturation.

For every capture compute:

max/min ADC code
clipping count
RMS
peak amplitude.

If saturated:

mark measurement invalid

or request/use a lower AFE gain configuration in future hardware.

Do not feed saturated captures into pose/phase solving as valid data.

---

# 57. SOFTWARE OUTPUT REPORT

Create a calibration report generator.

For each calibration run output:

system metadata
environment
measured pose
manual vs auto geometry if available
f_work
valid TX count
weak TX count
invalid TX count
pose residual
TOF quality
phase residual
recommended channel mask.

Generate:

JSON
CSV
human-readable Markdown.

---

# 58. OPERATING MODES

The software architecture shall support at least:

NORMAL_FIELD

CALIBRATE_GEOMETRY

CHARACTERIZE_TX

CALIBRATE_PHASE

VALIDATE_FIELD

SAFE_DISABLED.

Do not allow calibration routines to run while normal field control is silently active.

Mode transitions must be explicit.

---

# 59. SAFETY SOFTWARE

Any:

ADC error
calibration abort
invalid state
buffer overflow
configuration mismatch

must be able to request:

SAFE_DISABLED.

The hardware OE/KILL path remains authoritative.

Software safety does not replace physical interlock.

---

# 60. PCB IS OUT OF SCOPE

For this stage:

DO NOT:

- produce final schematic;
- produce PCB layout;
- generate Gerber;
- route traces;
- claim DRC completion;
- claim manufacturing readiness.

You MAY:

- document expected connectors;
- document interfaces;
- document electrical parameter assumptions;
- provide pin-count/interface requirements for the future PCB stage.

Create:

v2/docs/hardware/PCB_SOFTWARE_INTERFACE_REQUIREMENTS.md

so the next PCB phase has a precise digital/analog interface contract.

---

# 61. PCB NEXT-STAGE HANDOFF REQUIREMENTS

At the end of this stage, the future PCB engineer must already know:

- required FPGA signals;
- number of digital lanes;
- clock frequencies;
- ADC signals;
- RX analog channels;
- nominal ADC range;
- AFE gain modes;
- power domains;
- calibration control lines;
- cable/interface requirements;
- safety signals;
- register semantics.

Do not leave PCB-critical interface behavior ambiguous.

---

# 62. NO PLACEHOLDERS IN CORE PIPELINE

Core calibration functionality must not be:

stub
TODO-only
fake PASS
hard-coded expected answer
mock-only without real implementation.

Mocks/models are allowed for physical hardware simulation.

But the actual algorithms must exist.

Example:

Allowed:
behavioral AD7606B model feeding real acquisition RTL.

Not allowed:
test simply returns "ADC PASS" without data flow.

---

# 63. VALIDATION MATRIX

Create:

v2/docs/verification/V2_SOFTWARE_VALIDATION_MATRIX.md

For each requirement list:

Requirement
Implementation
Unit test
Integration test
Independent oracle
Evidence path
Status
Limitation.

Keep:

SIMULATION
SYNTHESIS
HARDWARE

clearly separate.

---

# 64. EVIDENCE

Save fresh evidence under:

v2/evidence/

Do NOT reuse copied v1 PASS files as v2 evidence.

Required groups:

baseline/
simulation/
model/
calibration/
validation/
reproducibility/

Include:

commands
tool versions
logs
summary JSON
hashes where useful.

---

# 65. INHERITED REGRESSION

Before considering this stage successful:

rerun all relevant inherited v1/v2 baseline tests.

Must continue to pass:

128-channel phase generation
requested phase
calibration phase
atomic commit
safe reset
deterministic timebase
geometry
standing wave
focus
Python/RTL comparison.

A calibration feature may not break normal acoustic-field operation.

---

# 66. V2 SOFTWARE ACCEPTANCE

This stage is complete only when:

1. full v2 inherited baseline remains PASS;
2. AD7606B digital interface exists;
3. realistic behavioral ADC simulation exists;
4. 8-channel acquisition is verified;
5. TX calibration scheduler works;
6. 512-path bidirectional sequence works;
7. RX blank control works;
8. burst generation works;
9. raw ADC data path works;
10. TOF estimation works;
11. sub-sample TOF refinement works;
12. carrier phase refinement works;
13. synthetic 6DoF pose recovery works;
14. environmental sound-speed compensation works;
15. frequency sweep works;
16. f0 extraction works;
17. one common f_work optimizer works;
18. per-channel phase calibration works;
19. channel-health classification works;
20. calibration database exists;
21. calibrated Phase LUT regeneration works;
22. end-to-end synthetic calibration works;
23. noise/outlier validation exists;
24. Vivado XSim passes;
25. Icarus passes where applicable;
26. software tests pass;
27. fresh standalone reproducibility passes;
28. no normal v2 path depends on v1;
29. PCB interface requirements are fully documented;
30. physical hardware results are not fabricated.

---

# 67. HARDWARE-DEPENDENT LIMITATIONS

The following may remain legitimately blocked:

- target synthesis if exact Zynq package is unresolved;
- final FPGA pin mapping;
- final PCB pinout;
- real ADC waveform;
- real TCT40 frequency sweep;
- real self-localization;
- physical levitation;
- 50 mg capacity.

Mark these accurately.

Do NOT let these blockers stop software/model/RTL work that can be completed without the physical PCB.

---

# 68. AI-PROBLEM RULE

If a genuine architecture blocker appears:

create:

AI-problem/problem/P-YYYYMMDD-NNN__topic.md

Do not use AI-problem for routine implementation bugs.

Before escalating:

attempt normal engineering diagnosis.

Only escalate major choices that affect:

architecture
scope
hardware contract
version
irreversible design.

---

# 69. REQUIRED END-OF-STAGE REPORT

At completion provide:

PROJECT_ID
project_name
repository
workspace_path
branch
active_version
stage
local HEAD
origin HEAD

Then:

## Inherited Baseline

## Implemented

## AD7606B Configuration

## FPGA/PL Architecture

## PS/Software Architecture

## Calibration Pipeline

## Geometry Calibration

## Frequency Characterization

## Phase Calibration

## Validation

## Vivado Evidence

## Icarus Evidence

## Python Evidence

## End-to-End Synthetic Test

## Robustness Test

## Reproducibility

## Hardware Interface Contract

## Not Yet Validated

## Blockers

## Risks

## Files Changed

## Git Commit

## Next Recommended Stage

End with exactly one:

ACCEPT
ACCEPT WITH LIMITATIONS
REVISE

Do not call the complete physical SonoField-FPGA project ACCEPT before hardware exists.

---

# 70. EXECUTION BOUNDARY FOR THIS TASK

Execute the complete SOFTWARE / DIGITAL stage now.

You are authorized to:

- modify v2 source;
- add RTL;
- add testbenches;
- add Python software;
- add configuration;
- add Vivado scripts;
- run Python tests;
- run Icarus;
- run Vivado 2025.2 XSim;
- generate synthetic calibration data;
- generate verification reports;
- update repository documentation;
- update shared project state;
- commit and push to the existing repository.

You are NOT authorized in this task to:

- start v3;
- modify frozen v1;
- fabricate PCB;
- order hardware;
- create Gerber;
- claim physical measurement;
- claim physical levitation;
- force push;
- release/deploy.

---

# 71. DONE WHEN

This stage is DONE only when:

v2 remains a complete standalone project

AND

the inherited SonoField-FPGA phase-array system still passes

AND

the complete self-calibration software architecture works end-to-end using realistic synthetic ADC data

AND

AD7606B acquisition logic is implemented and verified

AND

the 128TX/8RX calibration sequence is implemented

AND

geometry/frequency/phase calibration algorithms are implemented

AND

one common f_work can be computed

AND

a calibrated Phase LUT can be generated

AND

Vivado XSim / Icarus / Python evidence is stored

AND

the future PCB stage has an unambiguous hardware/software interface specification

AND

the result is committed and pushed to GitHub.

Then STOP.

Do not automatically enter the PCB implementation stage.

Return the complete engineering report for ChatGPT/user independent review.