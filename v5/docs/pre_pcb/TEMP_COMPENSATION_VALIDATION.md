# Temperature compensation validation contract

Three separate TMP117 readings retain sensorID/location/time/value/uncertainty/
status/staleness/calibration offset/provenance. Missing, duplicated, unknown,
future, stale>2000ms, error, invaliduncertainty or out-of-range0–50°C values
are rejected; no default replaces a failed sensor. Signed16bit TMP1171/128°C
decode and SHT45 CRC are tested. Read callbacks require bounded hardware
timeouts. No real I2C/temperature acquisition occurred.

Dry approximation c(z)=331.3+.606T(z)m/s. Piecewise linear interpolation uses
lower/center/upper along nominal/measured gap anchors, clamped outside them;
each straight ray integrates1/c(z) and converts−fτ to requestedphase256codes.
Calibration bytes stay independent, complete128maps only. RH is recorded but
humidity_applied=false; pressure_assumed=true. No3D air-field measurement or
full thermodynamic correction is claimed. Three PCB temperatures need measured
air/board bias and sensor placement validation.

Independent algorithms: Python Gauss quadrature split at all three temperature
knots, SciPy adaptive integration, and C analytic inverse-linear-speed integral
using log1p. Current integrated gate compares160maps/20480channel words with
random calibration bytes and both nominal/fitted6DoF poses in uniform/gradient
temperature fields. It fails on any requested/calibration word difference.
Actual numeric results reside in successful `system*/phase/summary.json`.

New unit tests exercise stale/offline/shortread/CRC and propagation symmetry,
gradient and uniform checks. C sensor-failure injection rejects task start and
stops active motion. Consecutive map phase jump>8codes disconnects/HOLD;
Python transition helper supplies bounded2code atomic-ramp candidates up to
32code delta and holds larger changes. It is not a qualified physical thermal
control loop. Analog hotspot kill remains independent and unverified.
