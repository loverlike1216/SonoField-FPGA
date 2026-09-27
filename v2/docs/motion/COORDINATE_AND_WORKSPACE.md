# Coordinates and workspace — v2

Transducer coordinate = **radiating surface center**. The origin is the geometric
center of all 128 radiating-face centers after applying the calibrated upper
array pose. Nominal arrays are 8×8 each, 12 mm XY pitch, 10 mm nominal bodies,
and 100 mm opposing radiating-face separation. Mechanical range remains 90–115 mm.
PCB height and the housing rear surface are not coordinate references.

The UI uses mm; acoustic calculations use m. Explicit `mm_to_m` / `m_to_mm`
conversion functions are covered by tests. +X points right, +Y upward in the
plan-view diagram, +Z toward the upper array. A lower-array origin is not exposed
to the UI; the calibrated geometry is recentered before the field calculation.

| Profile | X/Y | Z | Meaning |
|---|---:|---:|---|
| Default demo | ±10 mm | ±6 mm | PROVISIONAL_UNTIL_HARDWARE_VALIDATED |
| Engineering model | ±15 mm | ±10 mm | Explicit simulation-only option |
| Future hardware profile | File-defined | File-defined | Must declare HARDWARE_VERIFIED |

`v2/config/motion_profile.json` is authoritative for the current defaults.
The hardware loader prefers `hardware_motion_profile.json` when present and
refuses hardware operation unless its classification is HARDWARE_VERIFIED.
Profile validation rejects invalid limits and unsupported update rates. Limits
can be changed in configuration; this is not permission to mark unmeasured
limits as verified. The current BoardTransport still blocks deployment.

Targets on the exact boundary are legal. Nonfinite coordinates and values beyond
the boundary are rejected with `TARGET_OUT_OF_WORKSPACE`; no clipping is used.
All sampled paths are checked, together with a dense geometric inspection before
time sampling. The modeled local trap must also remain inside the model envelope.

The model envelope is not a measured stable levitation volume. Particle size,
density, mass, airflow, array loading, alignment and drive limits remain unknown
until the staged physical bring-up. No 50 mg capacity is inferred here.
