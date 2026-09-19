# Current 10 mm / 128-channel radiating-surface model

All numerical results are **SIMULATION_ESTIMATE**. The old 16 mm report was preserved unchanged in
docs/history/vn1_16mm/model_and_results.md and evidence/model/vn1/. Do not compare arbitrary pressure
units between different real transducer types as if their source strengths had been measured equal.

## User geometry and model inputs

config/acoustic_baseline.json: 128 emitters, two planar 8x8 grids, 12 mm XY center pitch,
10 mm nominal bodies, default radiating-face gap 100 mm. All positions are radiating-surface centers;
upper/lower normals point inward. The actual active aperture is unknown; the model assumes a 10 mm
equivalent baffled piston. Air c=343 m/s, f=40 kHz, normalized equal source amplitudes and zero fitted
absorption are explicit assumptions. No PCB plane is used in propagation distances.

The solver retains spherical spreading and signed piston directivity, independent intrinsic error and
calibration correction. It neglects mutual coupling, cavity multiple reflections, measured response curves,
airflow/streaming, driver nonlinearities and finite-particle scattering. Strong reflections can make a
real gap sweep differ materially from this free-field superposition estimate.

## Gap sweep (quantized 8-bit focus map)

| Face gap mm | Regenerated map pressure a.u. | Reusing 100 mm map, a.u. | Reuse / regenerated |
|---:|---:|---:|---:|
| 90 | 1156.70 | 1080.37 | 0.9340 |
| 95 | 1161.82 | 1143.19 | 0.9840 |
| 100 | 1164.23 | 1164.23 | 1.0000 |
| 105 | 1164.24 | 1148.15 | 0.9862 |
| 110 | 1162.17 | 1101.37 | 0.9477 |
| 115 | 1158.24 | 1031.00 | 0.8901 |

The modeled focal metric remains similar across the permitted gap range when phases are recomputed.
Reusing the nominal map loses about 6.6% at 90 mm and 11.0% at 115 mm in this scenario. This is why
gap-specific maps are exported and atomically committed. It does not identify a measured optimal gap.
STANDING_WAVE adds a lower-array half-cycle shift and has a central pressure node; the focal pressure
table above is a field-strength metric, not the pressure at that node or a measured trapping force.

## Emitter scaling and alternate geometry

At 100 mm face gap, the planar 2/8/16/32/72/128 cases give approximately
40.00 / 150.45 / 270.59 / 489.43 / 851.30 / 1164.23 a.u. respectively.
The 72→128 ratio is about 1.37, below the emitter-count ratio; no perfect linear/N² physical scaling is assumed.
At 128 planar emitters, 50 trials with seed 7020, 15-degree RMS phase error and 10% RMS amplitude mismatch
give a 5–95% interval of about 1108.72–1145.39 a.u. These are assumed errors, not batch statistics.

A shallow-cap comparison is retained in geometry_comparison.csv but is **not the selected mechanical geometry**.
Its on-axis separation convention cannot be substituted for equal-height planar face coordinates.

## Trap proxy and particle limitations

The potential proxy, finite-difference curvature and coarse connected region remain research metrics:
`U'=|p|² - 3|grad p|²/(2k²)` assumes unit high-contrast coefficients and a Rayleigh-sized particle.
It omits gravity and absolute pressure. At the nominal planar geometry its coarse 1 mm-grid region is
21 mm³ inside the selected +/-10 mm analysis cube; this is not a usable physical working-volume specification.

At the illustrative density 20 kg/m³, 50 mg corresponds to a 16.84 mm sphere and ka≈6.17, outside the
small-particle approximation. Changing emitter diameter does not resolve that limitation. Actual object
mass, dimensions and material response, plus measured source strength or a finite-size solver, are needed.
The physical path remains initial measured small particle → 5 → 10 → 25 → 50 mg, without a guarantee.

Current outputs: evidence/geometry_10mm/model/. Coordinate and phase tables:
hardware/mechanical/geometry_10mm/. Source assumptions are recorded alongside the results.
