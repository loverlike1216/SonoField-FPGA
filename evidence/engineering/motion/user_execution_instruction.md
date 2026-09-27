# SonoField-FPGA v2
# Stage: INTERACTIVE_LEVITATION_AND_TRAJECTORY_CONTROL

## 0. PROJECT IDENTITY

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

primary_FPGA:
Robei Octagonal Board / Zynq-7020

primary_EDA:
AMD Vivado 2025.2

PC side:
Windows PC

Current user-authorized target:

建立第一版“PC端交互控制 → FPGA声场控制 → 小球运动”的完整数字控制系统，
重点完成：

1. 定点悬浮；
2. 平面直线移动；
3. 平面轨迹移动；
4. Z轴上下直线移动。

任意空间三维轨迹：

同时改变 X/Y/Z 的复杂3D路径

NOT REQUIRED in this stage.

完成上述功能后再讨论进一步空间运动能力。

---

# 1. VERSION RULE

This task CONTINUES CURRENT v2.

Do NOT:

- create v3;
- modify frozen v1;
- modify project goal;
- fabricate physical test results;
- claim physical levitation before real hardware evidence.

All new implementation belongs to:

v2/

Maintain v2 as a complete independently runnable project.

---

# 2. FIRST ACTION — READ CURRENT REPOSITORY FACTS

Before coding, inspect:

README.md
AGENTS.md

shared/PROJECT_STATE.json
shared/VERSION_STATE.json
shared/CURRENT_PLAN.md
shared/DECISIONS.md
shared/ACCEPTANCE.md
shared/BLOCKERS.md
shared/HANDOFF.md

v2/software/control/
v2/software/acoustic_model/
v2/software/calibration/
v2/config/
v2/rtl/
v2/tb/
v2/tests/
v2/docs/
v2/evidence/

Especially inspect and reuse:

v2/software/control/host.py

v2/software/acoustic_model/phase_solver.py
v2/software/acoustic_model/phase_lut_generator.py
v2/software/calibration/pipeline.py

v2/config/system_baseline.json
v2/config/register_map.json

Do NOT rewrite already validated self-calibration or phase engine architecture.

---

# 3. CURRENT VERIFIED BASELINE TO REUSE

Current v2 already contains:

- 128-channel phase engine;
- requested_phase;
- calibration_phase;
- channel mask;
- complete 128-channel map;
- atomic MAP_COMMIT;
- calibrated geometry;
- common f_work;
- per-channel phase calibration;
- target coordinate phase LUT generation;
- host Controller abstraction;
- NORMAL_FIELD operating mode;
- Python/Icarus/XSim validation.

Current software already supports conceptually:

target = (x,y,z)
→ phase_lut(...)
→ 128-channel map
→ MAP_COMMIT
→ field update.

Therefore this stage must NOT redesign the phase engine.

This stage adds:

USER INTERACTION
+
MOTION PLANNING
+
TRAJECTORY GENERATION
+
CONTINUOUS FIELD UPDATE
+
FPGA/PC CONTROL CONTRACT.

---

# 4. IMPORTANT PHYSICAL INTERPRETATION

The GUI must clearly distinguish:

COMMAND POSITION

from:

MEASURED BALL POSITION.

At this stage no camera or real-time optical tracker exists.

Therefore:

Current Position shown by software means:

COMMAND / TRAP POSITION

not independently measured particle position.

Do NOT display:

"Actual Ball Position"

unless a future tracking sensor is implemented.

At startup:

the commanded trap position defaults to:

(0,0,0)

and the operator physically places the test ball near the center trap.

The program shall require an explicit operator confirmation:

BALL_AT_CENTER_CONFIRMED

before enabling motion commands.

---

# 5. COORDINATE SYSTEM

Use the existing calibrated acoustic coordinate system.

Origin:

(0,0,0)

=

geometric center of the two opposing radiating surfaces.

Coordinate directions shall be explicit:

+X:
right in system view

+Y:
forward/up in plan view according to documented board convention

+Z:
toward the upper array.

The GUI shall include a small coordinate diagram and current boundaries.

Use:

millimetres

for the PC user interface.

Internal algorithms may use:

metres.

All conversions shall be explicit and unit-tested.

---

# 6. WORKSPACE BOUNDARY POLICY

Physical operating boundaries have NOT yet been verified.

Therefore create two different concepts:

## A. SOFTWARE_MODEL_LIMIT

Initial provisional model envelope:

X:
-15 mm ... +15 mm

Y:
-15 mm ... +15 mm

Z:
-10 mm ... +10 mm

These are:

PROVISIONAL_SIMULATION_LIMITS

not physical guarantees.

## B. DEFAULT_DEMO_LIMIT

Use a more conservative first-demo envelope:

X:
-10 mm ... +10 mm

Y:
-10 mm ... +10 mm

Z:
-6 mm ... +6 mm

Default GUI uses:

DEFAULT_DEMO_LIMIT.

A configuration flag may allow:

SOFTWARE_MODEL_LIMIT

during simulation and engineering tests.

The program MUST reject any target outside the active workspace.

Do NOT silently clip invalid coordinates.

Return:

TARGET_OUT_OF_WORKSPACE.

After real hardware testing, these limits shall be replaced by:

HARDWARE_VERIFIED_WORKSPACE.

---

# 7. DEFAULT START CONDITION

On program startup:

commanded_target = (0,0,0)

motion_state = SAFE_DISABLED

trajectory = NONE

velocity = 0

The sequence shall be:

CONNECT FPGA
→ CHECK STATUS
→ LOAD CALIBRATION
→ VERIFY f_work
→ APPLY CENTER TRAP
→ WAIT FOR OPERATOR
→ BALL_AT_CENTER_CONFIRMED
→ ENABLE MOTION.

Do not automatically move the field immediately after connection.

---

# 8. FIRST VERSION MOTION MODES

Implement exactly these user-visible modes first:

MODE 1:
HOLD / FIXED LEVITATION

MODE 2:
POINT MOVE

MODE 3:
PLANAR LINE

MODE 4:
PLANAR TRAJECTORY

MODE 5:
VERTICAL MOVE

MODE 6:
RETURN CENTER

MODE 7:
EMERGENCY STOP.

Do NOT add arbitrary simultaneous 3D trajectory in this stage.

---

# 9. FIXED LEVITATION MODE

User selects target:

X
Y
Z

within allowed workspace.

The controller shall create a calibrated trap command for that point.

Do NOT call this simply:

PRESSURE FOCUS

in the architecture.

Create a higher-level abstraction:

LEVITATION_TRAP.

The existing FOCUS/STANDING_WAVE models may be reused internally.

The software shall attempt to create a locally stable acoustic trap, not merely maximize pressure.

---

# 10. LEVITATION TRAP MODEL

Add a module such as:

v2/software/motion/trap_solver.py

or equivalent.

For the dual opposing planar arrays, use the existing phase solver and standing-wave model to generate a trap around:

P_target = (x,y,z).

For the first implementation:

XY steering:
use calibrated geometric phase steering.

Z steering:
use controlled relative phase offset between upper/lower arrays and calibrated geometry.

The ideal standing-wave relationship may be used as an initial reference:

node displacement is related to relative upper/lower phase shift.

However:

do NOT rely only on a closed-form ideal equation.

Use the calibrated acoustic model to verify the predicted trap position.

---

# 11. TRAP STABILITY CHECK

Before accepting a requested target point:

evaluate a small local neighbourhood around the target.

Example:

target ±1 mm or configurable neighbourhood.

Calculate a relative trap stability metric using the existing field model and, where justified, a normalized Gor'kov/acoustic-potential approximation.

Required checks:

- target is inside workspace;
- trap candidate exists;
- local gradients are finite;
- model does not indicate obvious unstable direction;
- field does not exceed configured model limits.

Return:

TRAP_VALID

or:

TRAP_INVALID_MODEL.

Do NOT claim this metric proves physical levitation.

It is a software safety/quality filter.

---

# 12. POINT-TO-POINT MOVEMENT

User specifies:

Target X
Target Y
Target Z
Speed.

Current project scope does NOT require arbitrary simultaneous 3D motion.

Therefore if both:

XY change
and
Z change

exist in one target command,

the first implementation shall decompose the movement into:

PHASE A:
planar XY movement at current Z

then:

PHASE B:
vertical Z movement at final XY.

This allows the user to reach a specified XYZ location without claiming general 3D trajectory control.

Future stages may optimize simultaneous XYZ movement.

---

# 13. SPEED BOUNDARIES

Physical maximum speed has NOT been measured.

Therefore define conservative provisional values.

## Horizontal movement

Minimum non-zero user speed:

0.5 mm/s

Default:

3 mm/s

Recommended first-demo range:

1 ... 5 mm/s

Initial hard software maximum:

10 mm/s.

## Vertical movement

Minimum non-zero user speed:

0.5 mm/s

Default:

2 mm/s

Recommended first-demo range:

0.5 ... 3 mm/s

Initial hard software maximum:

5 mm/s.

Velocity = 0 is reserved for:

HOLD.

Do not accept negative speed.

These values must be tagged:

PROVISIONAL_UNTIL_HARDWARE_VALIDATED.

---

# 14. ACCELERATION BOUNDARIES

Do not instantly change particle velocity.

Initial provisional limits:

horizontal acceleration max:

20 mm/s²

vertical acceleration max:

10 mm/s².

These limits shall be configurable.

Do not expose acceleration to the basic competition GUI unless Advanced Mode is enabled.

Use these values internally.

---

# 15. TRAJECTORY INTERPOLATION

Do NOT use a simple position jump between endpoints.

Use smooth trajectory interpolation.

Preferred initial method:

quintic smooth-step / minimum-jerk style interpolation.

Boundary conditions:

at start:

v = 0
a = 0

at destination:

v = 0
a = 0.

Use:

s(tau) = 10 tau^3 - 15 tau^4 + 6 tau^5

or an engineering-equivalent method.

For constant-speed middle sections, generate:

acceleration segment
→ cruise
→ deceleration segment.

---

# 16. FIELD UPDATE RATE

Initial trajectory update target:

50 Hz.

One field update every:

20 ms.

If profiling proves reliable:

allow:

100 Hz.

Do not exceed 100 Hz in the default first version without evidence.

At:

10 mm/s
and
50 Hz

maximum nominal horizontal waypoint spacing is:

0.2 mm.

At:

5 mm/s
and
50 Hz

vertical spacing is:

0.1 mm.

These values are suitable provisional first-version discretization targets.

---

# 17. TRAJECTORY COMMAND STRUCTURE

Every trajectory point shall contain at least:

sequence_id
timestamp_target
x_mm
y_mm
z_mm
velocity_mm_s
mode
phase_map_reference
validity
trap_score.

Do not represent a trajectory as anonymous arrays with no metadata.

---

# 18. PLANAR LINE MODE

Implement:

START = (x0,y0,z_const)

END = (x1,y1,z_const)

User specifies:

end X
end Y
speed.

Z remains constant.

Trajectory planner generates smooth XY motion.

Reject if any trajectory sample exits the active workspace.

---

# 19. PLANAR TRAJECTORY MODE

First-version planar trajectories operate in:

XY plane

with:

constant Z.

User can select:

CIRCLE
SEMICIRCLE
ELLIPSE
HYPERBOLA_SEGMENT
TRIANGLE
RECTANGLE
CUSTOM_WAYPOINTS.

Do NOT implement arbitrary 3D path here.

---

# 20. CIRCLE

Parameters:

center_x
center_y
radius
start_angle
end_angle
direction
speed
z.

Verify every sampled point is inside workspace.

---

# 21. SEMICIRCLE

Parameters:

center_x
center_y
radius
orientation
direction
speed
z.

Allow:

upper half
lower half
left half
right half

or angle-based equivalent.

---

# 22. ELLIPSE

Parameters:

center_x
center_y
semi_major_axis
semi_minor_axis
rotation_angle
speed
z.

Reject ellipse if any point exceeds workspace.

---

# 23. HYPERBOLA

Hyperbola is mathematically unbounded.

Therefore NEVER allow an unrestricted hyperbola.

Implement:

HYPERBOLA_SEGMENT

with explicit finite parameter interval.

User defines:

center
a
b
rotation
branch
parameter_start
parameter_end
speed
z.

Every generated point must pass workspace validation.

If any point exits the workspace:

reject the trajectory.

---

# 24. TRIANGLE

User may specify:

three vertices

or:

center
size
rotation.

Because a geometric triangle contains sharp corners:

DO NOT command instantaneous 90/acute direction changes.

Apply corner smoothing.

Use either:

- fillet;
- quintic corner transition;
- small-radius rounded vertex.

Default corner smoothing distance:

approximately 1 mm

subject to geometry size.

---

# 25. RECTANGLE

Parameters:

center
width
height
rotation
speed
z.

Rectangle corners must also be smoothed.

Do not command zero-time velocity direction reversal.

---

# 26. CUSTOM WAYPOINTS

Allow a user-defined ordered point list:

[(x0,y0), (x1,y1), ...]

at fixed Z.

Validate:

- point count;
- coordinate bounds;
- segment lengths;
- requested speed;
- trajectory continuity.

Apply automatic smoothing between segments.

---

# 27. VERTICAL MOVE MODE

User defines:

Target Z
Speed.

X and Y remain fixed.

Motion:

(x_current,y_current,z0)
→
(x_current,y_current,z1).

Initial vertical boundary:

-6 mm ... +6 mm

in DEFAULT_DEMO_LIMIT.

Hard provisional model boundary:

-10 mm ... +10 mm.

Initial maximum speed:

5 mm/s.

Recommended demo:

<=3 mm/s.

---

# 28. RETURN CENTER

Implement one button:

RETURN CENTER.

Current commanded position:

(x,y,z)

shall return using:

planar XY move
→
vertical Z move

or an equivalent safe staged sequence.

Final:

(0,0,0).

Do not teleport the trap.

---

# 29. EMERGENCY STOP

GUI must contain an obvious:

STOP

button.

STOP must:

1. cancel trajectory;
2. stop queue generation;
3. issue SAFE_DISABLED;
4. clear pending trajectory;
5. leave software in a known state.

The hardware KILL/OE path remains separate and authoritative.

Do not rely only on the GUI for hardware safety.

---

# 30. PC APPLICATION

Create a lightweight PC control application.

Preferred:

Python + PySide6.

If PySide6 creates environment issues, a simpler built-in GUI may be used, but keep architecture independent of the UI framework.

Suggested path:

v2/software/ui/

app.py
main_window.py
workspace_panel.py
point_control_panel.py
trajectory_panel.py
vertical_panel.py
status_panel.py

Keep UI thin.

Do not put acoustic mathematics directly inside button callbacks.

---

# 31. GUI LAYOUT

The application shall contain at least four visible functional areas.

## Panel A — SYSTEM / WORKSPACE

Display:

Connection:
CONNECTED / DISCONNECTED

FPGA:
READY / FAULT

Calibration:
VALID / INVALID

Mode

f_work

Workspace:

X_min / X_max
Y_min / Y_max
Z_min / Z_max

Origin:

(0,0,0)

Current commanded trap:

X
Y
Z.

Explicit text:

"Commanded trap position; actual particle position is not measured."

---

# 32. GUI PANEL B — POINT MOVE

Fields:

Target X (mm)
Target Y (mm)
Target Z (mm)

Speed (mm/s)

Buttons:

MOVE
HOLD
RETURN CENTER.

Before MOVE:

validate bounds
validate speed
validate calibration
validate trap model.

---

# 33. GUI PANEL C — PLANAR TRAJECTORY

Trajectory Type dropdown:

LINE
CIRCLE
SEMICIRCLE
ELLIPSE
HYPERBOLA SEGMENT
TRIANGLE
RECTANGLE
CUSTOM WAYPOINTS.

Display corresponding parameters dynamically.

Fields include:

Z plane
speed
direction
repeat count.

Provide:

PREVIEW
RUN
STOP.

A simple XY preview plot is allowed and recommended.

Do not turn the application into a complex CAD editor.

---

# 34. GUI PANEL D — VERTICAL CONTROL

Display current commanded Z.

User enters:

Target Z
Vertical Speed.

Buttons:

UP
DOWN
MOVE Z
CENTER Z.

UP/DOWN shall use a configurable step.

Initial default step:

1 mm.

Still apply smooth trajectory generation.

---

# 35. SYSTEM ARM SEQUENCE

The GUI shall not allow motion immediately after launch.

Required state flow:

DISCONNECTED
↓
CONNECTED
↓
CALIBRATION_LOADED
↓
CENTER_TRAP_READY
↓
WAIT_BALL_CONFIRMATION
↓
ARMED
↓
MOTION_ALLOWED.

Provide:

[Confirm ball placed at center]

button.

This is necessary because no real particle tracker exists.

---

# 36. SOFTWARE ARCHITECTURE

Create or extend:

v2/software/motion/

workspace.py
trajectory.py
profiles.py
trap_solver.py
motion_controller.py
commands.py
safety.py

and:

v2/software/ui/

Keep:

UI
Motion Planner
Trap Solver
FPGA Transport

separate.

Target architecture:

PC GUI
↓
Motion Command
↓
Workspace Validator
↓
Trajectory Planner
↓
Trap Solver
↓
Phase LUT Generator
↓
Motion Controller
↓
Board Transport
↓
Zynq
↓
PL phase engine.

---

# 37. TRANSPORT ARCHITECTURE

The existing:

Controller(read32, write32)

abstraction shall be preserved.

Add a transport abstraction.

Suggested:

Transport
├── SimulationTransport
├── RegisterTranscriptTransport
└── BoardTransport

Do NOT invent final physical FPGA connector pins.

The current board pin/VCCO blockers remain active.

---

# 38. PC ↔ ZYNQ COMMAND PRINCIPLE

Do NOT stream large ASCII phase maps from the GUI.

The GUI shall send structured binary/high-level commands.

Possible command types:

CONNECT
GET_STATUS
SET_TARGET
RUN_LINE
RUN_TRAJECTORY
RUN_VERTICAL
RETURN_CENTER
HOLD
STOP.

Include:

magic
protocol version
sequence number
payload length
command
payload
CRC.

Use acknowledgement and timeout.

---

# 39. BOARD-SIDE INTEGRATION STRATEGY

Preferred final architecture:

PC
→ command transport
→ Zynq PS
→ motion/phase control
→ AXI-Lite / BRAM
→ PL
→ phase engine.

PC shall mainly provide:

user interaction
trajectory definitions
status display.

Time-critical phase updates must not depend on Windows GUI timing.

Do not make:

Windows timer
→ direct phase update

the only final architecture.

---

# 40. PS / PL RESPONSIBILITY

## PC

User interaction
trajectory definition
visualization
high-level command
logging.

## PS

Trajectory execution
calibration loading
trap target generation
phase-map production or map scheduling
safety state
status reporting.

## PL

Deterministic phase engine
atomic map update
serializer
real-time timing
hardware safety.

If actual PS runtime environment is still unresolved:

implement and verify the software architecture using the current host model,

but preserve the PS execution boundary.

Do not fake a real PS deployment.

---

# 41. TRAJECTORY BUFFER

Add a bounded trajectory/map buffering mechanism.

Do not require PC to write all 128 channels synchronously every 20 ms forever.

Preferred architecture:

trajectory points / maps
→ buffer
→ deterministic scheduler
→ next map
→ atomic commit.

At minimum support:

double buffering.

Preferred future:

small ring buffer.

The buffer shall report:

empty
full
underflow
overflow
sequence ID.

Any underflow during motion:

SAFE HOLD

or

SAFE DISABLE

according to policy.

Do not continue with stale/random map data.

---

# 42. ATOMIC MAP UPDATE

Retain current:

MAP_WRITE
MAP_COMMIT
MAP_ACK

semantics.

Every trajectory frame must update:

all 128 channels

as one coherent map.

Never partially move the acoustic trap.

---

# 43. REQUESTED VS CALIBRATION PHASE

Continue to keep:

requested_phase

and:

calibration_phase

separate.

Motion only changes:

requested_phase.

Calibration remains from the latest valid calibration record unless a new calibration is loaded.

Effective phase:

requested + calibration.

Do not rewrite calibration for every waypoint.

---

# 44. CALIBRATED GEOMETRY

Movement shall default to:

CALIBRATED geometry.

If calibration is unavailable:

NORMAL physical motion shall be blocked by default.

Allow:

NOMINAL geometry

only in:

SIMULATION
or
explicit engineering debug mode.

Do not silently fall back to nominal geometry for competition operation.

---

# 45. FIELD MODE

Introduce a high-level motion field mode such as:

LEVITATION_TRAP_V1.

Internally it may use:

FOCUS
+
STANDING_WAVE
+
upper/lower phase relation.

Do NOT add:

"TRAJECTORY"

as a raw acoustic solver mode.

Trajectory is a sequence of trap targets, not a new acoustic wave equation.

---

# 46. WORKSPACE CONFIGURATION

Create one authoritative file, e.g.:

v2/config/motion_profile.json

containing:

workspace
default_demo_workspace
horizontal_speed
vertical_speed
acceleration
update_rate
corner_smoothing
center_position
coordinate convention.

Example conceptual content:

workspace.model:
x_mm: [-15,15]
y_mm: [-15,15]
z_mm: [-10,10]

workspace.demo:
x_mm: [-10,10]
y_mm: [-10,10]
z_mm: [-6,6]

horizontal:
speed_min_mm_s: 0.5
speed_default_mm_s: 3
speed_max_mm_s: 10
accel_max_mm_s2: 20

vertical:
speed_min_mm_s: 0.5
speed_default_mm_s: 2
speed_max_mm_s: 5
accel_max_mm_s2: 10

update_rate_hz: 50.

Mark all physical values as:

PROVISIONAL_UNTIL_HARDWARE_VALIDATED.

---

# 47. HARDWARE PROFILE OVERRIDE

Design the configuration so future physical validation can produce:

hardware_motion_profile.json.

When verified hardware limits exist:

HARDWARE_VERIFIED

shall take precedence over provisional simulation limits.

Do not require code changes to update the real workspace.

---

# 48. TRAJECTORY PREVIEW

Before running a planar trajectory:

show a preview.

Display:

XY plane
workspace boundary
origin
start
trajectory
end.

Use:

Matplotlib

or equivalent lightweight plotting.

The preview must use exactly the same generated points that will be sent to the controller.

Do not separately redraw an approximate path.

---

# 49. COMMAND LOGGING

Every motion command shall be logged.

Record:

timestamp
command
start
target
trajectory type
speed
duration
update rate
point count
calibration ID
f_work
workspace profile
result
abort/fault.

Do not store only GUI text.

Use machine-readable JSON or JSONL plus readable log.

---

# 50. SIMULATION MODE

The complete PC application must operate without real hardware.

Create:

SIMULATION MODE.

Simulation shall:

use current calibrated synthetic model
generate trajectory
generate phase maps
simulate FPGA acknowledgements
display motion state.

This allows immediate testing before PCB completion.

Clearly show:

SIMULATION

in the GUI.

Never present simulation as physical movement.

---

# 51. REAL HARDWARE MODE

When real hardware transport is available:

BOARD MODE.

Require:

FPGA connected
calibration valid
board status good
hardware enable good
motion profile valid.

Otherwise:

disable RUN.

---

# 52. REQUIRED UNIT TESTS — WORKSPACE

Add tests for:

MOTION-SW01:
origin = (0,0,0)

MOTION-SW02:
default workspace boundaries

MOTION-SW03:
reject X out of range

MOTION-SW04:
reject Y out of range

MOTION-SW05:
reject Z out of range

MOTION-SW06:
accept exact boundary values

MOTION-SW07:
unit conversion mm ↔ m.

---

# 53. REQUIRED TESTS — SPEED

MOTION-SW08:
0.5 mm/s accepted

MOTION-SW09:
10 mm/s horizontal accepted

MOTION-SW10:
>10 mm/s horizontal rejected

MOTION-SW11:
5 mm/s vertical accepted

MOTION-SW12:
>5 mm/s vertical rejected

MOTION-SW13:
negative speed rejected

MOTION-SW14:
zero interpreted only as HOLD.

---

# 54. REQUIRED TESTS — POINT MOVE

MOTION-SW15:
center → valid XY target.

MOTION-SW16:
center → valid Z target.

MOTION-SW17:
combined XYZ target decomposes into planar + vertical segments.

MOTION-SW18:
start/end velocity approximately zero.

MOTION-SW19:
trajectory points remain inside workspace.

---

# 55. REQUIRED TESTS — PLANAR SHAPES

MOTION-SW20:
line.

MOTION-SW21:
circle.

MOTION-SW22:
semicircle.

MOTION-SW23:
ellipse.

MOTION-SW24:
finite hyperbola segment.

MOTION-SW25:
triangle.

MOTION-SW26:
rectangle.

MOTION-SW27:
custom waypoints.

MOTION-SW28:
shape exceeding workspace rejected.

MOTION-SW29:
triangle/rectangle corner smoothing.

---

# 56. REQUIRED TESTS — VERTICAL

MOTION-SW30:
Z positive move.

MOTION-SW31:
Z negative move.

MOTION-SW32:
X/Y remain unchanged.

MOTION-SW33:
vertical speed cap.

MOTION-SW34:
return Z center.

---

# 57. REQUIRED TESTS — PHASE MAP

For every generated motion point:

generate a complete 128-channel map.

Verify:

- all channel IDs exist;
- requested phase 0..255;
- calibration phase unchanged;
- mask preserved;
- map commit complete.

MOTION-SW35:
all trajectory frames produce valid maps.

MOTION-SW36:
same input produces deterministic maps.

MOTION-SW37:
calibration phase constant across motion.

---

# 58. REQUIRED TESTS — FPGA CONTROL

MOTION-RTL01:
trajectory-map load.

MOTION-RTL02:
atomic commit.

MOTION-RTL03:
double-buffer swap.

MOTION-RTL04:
fixed update interval.

MOTION-RTL05:
buffer underflow.

MOTION-RTL06:
buffer overflow.

MOTION-RTL07:
STOP mid-trajectory.

MOTION-RTL08:
reset mid-trajectory.

MOTION-RTL09:
invalid map rejected.

MOTION-RTL10:
return SAFE state.

Use:

Icarus
and
Vivado 2025.2 XSim.

---

# 59. END-TO-END DIGITAL DEMO

Create a complete software demonstration:

START:

(0,0,0)

Step 1:
hold center

Step 2:
move line to:

(+8,0,0) mm

Step 3:
move back to:

(0,0,0)

Step 4:
execute circle:

radius = 5 mm
Z = 0

Step 5:
execute rectangle inside safe workspace

Step 6:
move Z:

0 → +4 mm

Step 7:

+4 → -4 mm

Step 8:

return center.

The complete sequence must run through:

GUI
→ trajectory planner
→ trap solver
→ phase LUT
→ Controller
→ RTL simulation transport.

Store deterministic evidence.

---

# 60. DEMO SPEED PROFILE

Use conservative initial demonstration values:

Point move:

3 mm/s.

Planar figures:

2–4 mm/s.

Vertical:

1–2 mm/s.

Do not use the maximum software limits as default demo speeds.

Maximum limits exist as guard rails, not recommendations.

---

# 61. PHYSICAL VALIDATION RULE

When real hardware becomes available:

start with:

very low speed
small displacement.

Suggested first physical sequence:

center
→ +2 mm X
→ center
→ -2 mm X
→ center.

Then:

±5 mm.

Only after stable evidence expand toward:

±10 mm.

Same principle for Z.

Do NOT start real tests directly at software maximum boundaries.

---

# 62. NO PHYSICAL CLAIM YET

Until hardware test exists, all movement results shall be classified:

SIMULATION_VALIDATED

not:

PHYSICAL_MOTION_PASS.

Do not write:

"small ball successfully moves 10 mm"

unless real test/video/measurement exists.

---

# 63. NO CAMERA TRACKING IN THIS STAGE

Do not add computer vision now.

The current system is:

OPEN-LOOP TRAP COMMAND.

Future version/stage may add:

camera
→ ball tracking
→ position error
→ closed-loop motion correction.

Leave a clean interface for:

MeasuredPositionProvider

but do not implement CV unless needed for testing.

---

# 64. DOCUMENTATION

Create at minimum:

v2/docs/motion/INTERACTIVE_CONTROL_ARCHITECTURE.md

v2/docs/motion/COORDINATE_AND_WORKSPACE.md

v2/docs/motion/TRAJECTORY_PLANNER.md

v2/docs/motion/PC_CONTROL_APP.md

v2/docs/motion/SAFETY_LIMITS.md

v2/docs/motion/FPGA_MOTION_INTERFACE.md

Clearly mark:

PROVISIONAL
SIMULATION_VALIDATED
HARDWARE_VERIFIED.

---

# 65. PCB INTERFACE IMPACT

This stage must NOT redesign the PCB.

However review whether motion-control requirements introduce new necessary FPGA signals.

Prefer to reuse current:

phase map
commit
status
hardware enable
fault

interfaces.

Do not add physical connector signals unless necessary.

If a new PCB requirement appears:

document it

but do NOT alter PCB files without user approval.

---

# 66. CURRENT BOARD FACT BLOCKERS

Do not invent:

Zynq exact package
VCCO
FPGA pinout
physical PC transport pins.

Current software can proceed with simulation/abstract transport.

Real board deployment remains gated by existing board facts.

---

# 67. ALLOWED CHANGES

You may modify/add:

v2/software/
v2/rtl/
v2/tb/
v2/tests/
v2/config/
v2/docs/
v2/evidence/
v2/scripts/

You may update project state and interaction records.

Do NOT modify:

frozen v1.

Do NOT enter PCB layout.

Do NOT create v3.

---

# 68. VALIDATION EVIDENCE

Required evidence:

Python test results

Trajectory JSON

Phase-map hashes

GUI simulation screenshot

Icarus logs

Vivado XSim logs

deterministic repeated runs

end-to-end transcript

motion-profile configuration

failure/rejection cases.

At least:

3 identical runs

for the fixed digital motion demo.

Verify trajectory/path hash consistency.

---

# 69. ACCEPTANCE CRITERIA

This stage may be accepted when all are true:

1. PC application starts normally.
2. Simulation mode works.
3. workspace is displayed correctly.
4. origin is (0,0,0).
5. center is default trap position.
6. user must confirm ball-at-center before motion.
7. point target accepts X/Y/Z.
8. invalid target is rejected.
9. horizontal speed is bounded.
10. vertical speed is bounded.
11. point movement is smooth.
12. planar straight line works.
13. circle works.
14. semicircle works.
15. ellipse works.
16. bounded hyperbola segment works.
17. triangle works.
18. rectangle works.
19. custom waypoint path works.
20. sharp corners are smoothed.
21. vertical movement keeps X/Y fixed.
22. return-center works.
23. emergency stop works.
24. each trajectory point produces a complete 128-channel phase map.
25. calibration_phase remains separate.
26. atomic commit remains intact.
27. trajectory buffer does not partially update a map.
28. fixed demo passes Python tests.
29. Icarus passes.
30. Vivado 2025.2 XSim passes.
31. three deterministic repetitions match.
32. no physical result is fabricated.
33. current PCB files remain untouched.
34. v1 remains frozen.
35. v2 remains independently runnable.

---

# 70. THIS STAGE DOES NOT REQUIRE

Do NOT spend time now on:

camera tracking
AI
voice control
mobile phone app
arbitrary 3D spline motion
multiple particles
multi-trap control
gesture control
advanced graphics
remote cloud control.

Those are later optional improvements.

---

# 71. FIRST VERSION DEMO TARGET

The intended user-facing first-version demonstration is:

## Demo A — Center levitation

Start:
(0,0,0)

Hold.

## Demo B — Point movement

User inputs:

X = +5 mm
Y = 0
Z = 0
Speed = 3 mm/s

Move.

## Demo C — Horizontal line

(-5,0,0)
→
(+5,0,0)

## Demo D — Planar path

circle / semicircle / ellipse / triangle / rectangle.

## Demo E — Vertical movement

(0,0,-3)
→
(0,0,+3)

with slow controlled motion.

## Demo F — Return center

Any allowed position
→
(0,0,0).

These are the primary competition demonstration functions.

---

# 72. END-OF-STAGE REPORT

At completion report:

PROJECT_ID
repository
branch
active_version
stage
local HEAD
remote HEAD

## Existing Functions Reused

## New Motion Architecture

## PC Application

## Workspace Limits

## Speed / Acceleration Limits

## Trajectory Types

## Trap Solver

## FPGA Integration

## Simulation Evidence

## Python Results

## Icarus Results

## Vivado XSim Results

## Determinism

## Failure Cases

## Not Physically Validated

## Board Blockers

## Files Changed

## Git Status

## Next Recommended Step

Final conclusion must be exactly one:

ACCEPT
ACCEPT WITH LIMITATIONS
REVISE.

---

# 73. EXECUTION STOP CONDITION

After the interaction/motion software and RTL control system passes the above digital validation:

STOP.

Do not automatically begin:

camera tracking
arbitrary 3D motion
PCB modifications
physical levitation claims
v3.

Return results for independent ChatGPT/user Review.

This remains:

v2.
