> v5 inherited design/reference documentation. Original source is recorded in config/inheritance_manifest.json. Technical behavior/requirements are retained; historical numeric results are reference inputs, not v5 validation or AX7020 electrical qualification. Current board facts are config/board_facts.json; baseline results are evidence/BASELINE_VALIDATION.md.

# Trajectory planner — v5

`software/motion/trajectory.py` owns paths; the GUI has no trajectory formulas.
Preview points are the actual submitted points. Their canonical hash must match
a new plan at submission, or `STALE_PREVIEW` is raised. Each row carries sequence,
logical target timestamp, X/Y/Z mm, velocity, mode, map hash, validity and trap score.

## Motion profiles

Quintic progress `s(u)=10u³−15u⁴+6u⁵` gives zero endpoint velocity and acceleration.
Duration considers both the first and second derivative of the complete curve,
including curvature acceleration; discrete speed/acceleration are checked again.
Sampling uses 50 Hz by default. The 100 Hz option requires a validation-evidence
entry; values above 100 Hz are rejected. Production integration must validate
throughput before selecting a faster rate.

Mixed XYZ moves use XY at the current Z, then Z at the final XY. Return-center
uses the same rule. Vertical moves keep X/Y exactly constant. HOLD is the only
mode for which zero requested speed is valid.

| Axis class | Minimum nonzero | Default | Maximum | Acceleration |
|---|---:|---:|---:|---:|
| Horizontal | 0.5 mm/s | 3 mm/s | 10 mm/s | 20 mm/s² |
| Vertical | 0.5 mm/s | 2 mm/s | 5 mm/s | 10 mm/s² |

All are PROVISIONAL. Acceleration is an advanced configuration-file setting,
not a basic UI control. Numerical duration includes 1% margin and is rounded up
to a complete sample period. Reported velocity is sampled, not measured motion.

## Shapes

LINE accepts two XY endpoints and fixed Z. CIRCLE and SEMICIRCLE accept center,
radius, starting angle, sweep and direction. Starting angles 0/90/180/270 cover
upper/left/lower/right half-circles. ELLIPSE accepts axes and rotation.
HYPERBOLA_SEGMENT requires finite explicit interval within [-3,3], positive a/b,
branch ±1 and optional rotation; all points still pass the workspace check.

TRIANGLE accepts vertices or center/radius/rotation. RECTANGLE accepts center,
width, height and rotation. Closed polygon corners use tangent-continuous
quadratic arcs, nominal 1 mm, reduced to fit short edges, with a periodic cubic
interpolant over the dense path. The full acceleration test includes corners.
Open CUSTOM_WAYPOINTS use quintic stop-and-go segments: each corner is reached
at zero velocity and acceleration, so there is no instantaneous velocity-vector
change. Closed custom paths use the rounded-polygon rule. Open paths cannot
repeat without an explicit return. At most 64 custom points, 10 repetitions,
12,000 frames and 240 seconds are allowed.

## Trap model

LEVITATION_TRAP_V1 reuses the calibrated `STANDING_WAVE` LUT, including its
opposite-bank π phase shift and target-dependent propagation compensation.
Each frame keeps the hardware calibration codes unchanged. Relative amplitude,
calibrated pose, normals, active mask and phase error are included in the field.

A baffled-piston directional model evaluates the normalized high-contrast
Rayleigh potential `U' = |p|² − 3 |∇p|²/(2 k²)` using the existing field convention.
The vectorized evaluator is cross-checked against the earlier scalar field and
potential implementation. A bounded local search inspects the full Hessian,
gradient residual, ±1 mm neighborhood shell and location error. Nonpositive
curvature, invalid values, excessive displacement or missing minimum produce
TRAP_INVALID_MODEL and prevent transmission.

TRAP_VALID means a local minimum in this approximate relative model. It omits
gravity, streaming, absolute SPL and finite-size scattering, and uses f1=f2=1.
It cannot prove stable particle motion or mass support. All such predictions
remain SIMULATION_ESTIMATE.
