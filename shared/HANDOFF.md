# Current VN1 handoff — 10 mm / 128-channel face geometry

## Goal / scope
Execute user's 2026-09-19 geometry revision: nominal 10 mm emitters, 12 mm radiating-center pitch,
upper/lower 8x8 arrays, 100 mm nominal face gap adjustable 90..115 mm. Origin stays at the common
geometric center; upper/lower z=+/-g/2. Physical electrical bring-up remains staged.

## Decisions / what changed
ADR-020..024 record explicit replacement of the former 16 mm / 72-emitter assumptions. The selected
current assembly is planar; curved comparison data cannot silently change its coordinates.
Model/default configuration, exported coordinates/maps, gap studies, supplier provenance, mechanical
datums, tests, guide and BOM were updated. Timing RTL is unchanged and its calibrated atomic-map interface is reused.

## Evidence / results
- Baseline f215460: 12 Python tests passed before changes.
- Current: 19 Python tests passed; exact grid, symmetry, normals, gap limits, channel corners and dimensions checked.
- Icarus + Vivado 2025.2 XSim: 128-channel standing/focus maps at 90/100/115 mm passed.
- Three repeated traces per simulator still share hash 63bfad4c5c08fa75d5b2b3b95b37fed7276a5a51052c091b71c9d94544a58054.
- Current full tool evidence: evidence/geometry_10mm/simulation_current/summary.json.
- Model/scaling/gap outputs: evidence/geometry_10mm/model/; all estimates, no calibrated pascals/force.
- Mechanical coordinates/figures/maps: hardware/mechanical/geometry_10mm/.
- Fresh reproduction at a01629c: PASS in a new local clone/venv, complete dual-simulator validation.
- Six model CSVs and 19 coordinate/phase CSVs reproduced; raw tool logs retained under reproducibility/validation.
- All 12 original board files and historical evidence unchanged; preservation check PASS.

## Open issues / failures
No new RTL functional failure. Existing board part/VCCO/pin gaps, serializer physical timing and hardware
characterization remain. New 10 mm exact part, drive rating, capacitance, active aperture, tolerances and
PCB mounting offset are unknown. Store missing quantities as unknown; do not borrow 16 mm ratings.
The image's '+' / shell claim requires continuity and acoustic verification. PCB gap is not 100 mm by definition.

## Historical evidence
Initial 16 mm reference results remain under evidence/model/vn1, evidence/simulation/vn1_release and
evidence/reproducibility. Original theory/transducer documents are preserved in docs/history/vn1_16mm.
shared/VN1_REPORT.md remains the initial report; shared/GEOMETRY_10MM_REPORT.md describes the current revision.
The original XSim launcher and wrong-checkpoint reproduction failures remain in their historical evidence directories.

## Next step
Review new coordinate and phase artifacts; identify/characterize actual 10 mm samples and mounting datums,
resolve board facts, then perform target synthesis/integration and one/two-emitter low-power experiments.
The 128-position design is now explicit, but full-array power-up is not authorized by simulation alone.
