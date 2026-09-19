# VN1 — 10 mm radiating-surface geometry revision

| Field | Value |
|---|---|
| PROJECT_ID / project_name | SONOFIELD_FPGA / SonoField-FPGA |
| repository | https://github.com/loverlike1216/SonoField-FPGA.git |
| workspace_path | E:\Codex-project\AMD-SonoField-FPGA |
| current_branch / current_version | main / VN1 |
| current_stage | RADIATING_SURFACE_GEOMETRY_128CH_10MM |

## IMPLEMENTED

User-selected planar upper/lower 8x8 arrays, 128 channels, nominal body diameter 10 mm and radiating-center
pitch 12 mm. Coordinates are radiating-face centers with global origin at the full assembly center.
Nominal z=+/-50 mm; face gap can be 90..115 mm, with z=+/-g/2. Gap limits are enforced by the current
profile and CLI, and phase maps are regenerated using the actual gap.

Center span is 84x84 mm; nominal body envelope 94x94 mm; nominal adjacent shell clearance 2 mm.
Symmetric travel is 12.5 mm per plane across the full 25 mm gap range. PCB planes and mounting standoffs
remain null until measured. Exported coordinates never quietly refer to PCB copper, board center or pin roots.

Artifacts: 128-row nominal CSV/JSON, six gap-coordinate profiles, 12 STANDING_WAVE/FOCUS maps,
dimensioned PNG/SVG, updated directional field/spacing/scaling results and supplier-image provenance.

## VALIDATED / REAL TOOL EVIDENCE

Before: clean source f215460, 12 Python tests PASS; historical reference and evidence preserved.
After: 19 Python tests PASS. New tests verify exact XY lattice, common origin, reflection and normals,
26 positions through the permitted travel, limits, corner channel IDs, envelope and gap-dependent phases.

Icarus and Vivado 2025.2 XSim pass complete digital regression and the actual 128-channel STANDING_WAVE
and FOCUS maps at 90/100/115 mm. Digital timing RTL is unchanged; the existing repeated-trace hash remains
`63bfad4c5c08fa75d5b2b3b95b37fed7276a5a51052c091b71c9d94544a58054`.
Current command logs and source hashes: evidence/geometry_10mm/simulation_current/summary.json.
Fresh-checkout reproduction status will be recorded in evidence/geometry_10mm/reproducibility/summary.json.

Model predicts about 11% loss in its normalized center-focus metric when reusing the 100 mm map at
115 mm; this motivates recomputing phase, not a claim about physical levitation capacity.

## NOT VALIDATED

Purchased batch mechanical dimensions, active radiating aperture, drive limits, capacitance, source strength,
electrical/acoustic polarity, PCB mounting offset, physical gap adjustment, target FPGA synthesis/implementation,
driver operation, absolute field pressure/force or any measured levitation mass.

## BLOCKING / BOARD FACTS FOUND

Documented .const board clock remains N18 / 33 MHz under the user's source precedence. Full FPGA part,
bank VCCO and malformed GPIO numbering remain unresolved (B01/B03). Serializer electrical timing/clock
generation remains B04. New part qualification is B06; physical measurements remain B05. This geometry
revision does not manufacture XDC, device identity, a bitstream or hardware PASS.

## TCT40 ASSUMPTIONS / RISKS

The attachment labels nominal 10 mm/40 kHz and 7 mm body height, but gives no identified manufacturer
part, capacitance or continuous voltage limit. Previous 16 mm electrical ratings are not transferred.
Supplier '+' and shell-connection markings are recorded as claims; acoustic calibration remains required.
The model assumes a 10 mm equivalent piston aperture, equal normalized source strengths and configurable
air properties. Finite-particle limits still prevent a 50 mg levitation guarantee.

## NEXT PHYSICAL HARDWARE REQUIRED / NEXT STAGE

Identify and measure the actual 10 mm batch, confirm allowed excitation and shell continuity, and establish
the face-to-mounting/PCB offset. Build an adjustable, measurable fixture with clearance beyond the 90..115 mm
working range for stops/locking. Resolve board facts before target synthesis. Start electrical validation with
one emitter and P0 with two, then commission the already selected 128-position design in verified modules.

Geometry/digital review status: READY_FOR_REVIEW after recorded gates.
Whole-platform hardware status: BLOCKED; final acceptance remains external.
