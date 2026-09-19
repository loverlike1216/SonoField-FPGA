# VN1 current plan — 10 mm / 128-channel radiating-surface revision

## Current Goal
Apply the user's new 10 mm transmitter, 12 mm radiating-center pitch, opposed 8x8 + 8x8 planar
geometry. Nominal face-to-face gap 100 mm, adjustable 90..115 mm; origin remains the geometric center.

## Scope
Record this explicit user decision as superseding the former 16 mm / 72-channel demonstration assumptions.
Update geometry configuration/defaults, coordinate exports and diagrams, gap-dependent maps and acoustic
comparisons. Regression-test new geometry through Python and both RTL simulators. Keep historical evidence
unchanged. Preserve staged low-power bring-up and existing board/driver electrical blockers.

## Non-Goals
No fabricated transducer model/ratings, final PCB drilling tolerances, assumed PCB-to-face distance,
guessed XDC/part, physical levitation claim or production fabrication.

## Files Expected To Change
config/, software/acoustic_model/, tests/, scripts/, docs/, hardware/mechanical/, evidence/, shared/, README.md.
RTL timing logic is expected to remain unchanged; map inputs change. User board files remain untouched.

## Risks
Image is a supplier dimension/reference sheet, not measured data: 10 mm body does not establish active aperture,
capacitance, voltage rating, exact part or acoustic polarity. Nominal 2 mm lateral clearance needs actual
tolerances. Radiating face gap must not be confused with PCB gap. Existing part/VCCO/serializer blockers remain.

## Validation
First record current 12-test baseline and source checkpoint. Add exact coordinate, reflection, normals,
gap-range/endpoints, channel mapping, physical envelope and regenerated-phase tests. Re-run full Python,
Icarus and XSim gate, including actual 90/100/115 mm maps. Compare deterministic regenerated artifacts
from a fresh committed checkout and new venv. Check documents/state no longer present old geometry as current.

## Evidence Required
Source image hash + transcribed supplier claims; baseline; 128 coordinate CSV/JSON; dimensioned layout;
90..115 mm gap sweep, per-gap maps, command logs/exit codes, tool/source hashes and fresh reproduction.

## Done When
User geometry encoded consistently, all feasible digital/model gates pass, historical results preserved,
limitations updated, reviewable coordinate/phase artifacts produced, source/evidence committed on main.

## Need ChatGPT Decision?
The user has already approved geometry/128-channel design changes; no further permission is needed for them.
Actual part identification, board facts and power/PCB freeze still require evidence; do not guess.

## Current execution result
PREFLIGHT: clean main at f215460, origin matched; prior shared state and acceptance read.
Previous digital/model evidence remains historical under evidence/simulation/vn1_release and evidence/model/vn1.
Current geometry exports, 19 Python tests, Icarus and Vivado 2025.2 XSim gates PASS.
Source-hash and repository audit PASS. New evidence is separate under geometry_10mm.
Fresh source checkpoint a01629c plus new clone/venv: PASS; six model CSVs and 19 coordinate/phase CSVs match.
Raw repeated tool evidence retained. Original 12 board files and historical evidence unchanged.
Geometry/digital stage READY_FOR_REVIEW; board/driver/physical gates remain BLOCKED.
Implementation complete for this revision; next work requires actual part and board evidence.
