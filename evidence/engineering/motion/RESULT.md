# CODEX_RESULT — SonoField-FPGA v2 motion stage

PROJECT_ID: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
workspace_path: E:\Codex_project\AMD-SonoField-FPGA
branch: main
active_version: v2
stage: INTERACTIVE_LEVITATION_AND_TRAJECTORY_CONTROL
Starting commit: 78f2be1678fbbb65e039bc9054ee0fef9653f647
Engineering source checkpoint: PENDING_COMMIT
Fresh-clone reproduction: PENDING
Codex: ACTIVE; Work: OFF. No v3, release or deployment.

## Implemented / reused

Reused calibrated geometry, selected working frequency, per-channel calibration,
existing Controller register representation, 128-channel phase bank, common carrier,
serializer and ADC initialization/model. Added continuous stream_map without the
static API's per-map abort, a four-map ring, deterministic cadence, real ACK checking,
and sono_motion_system integration. No PCB source or physical pins changed.

Added local Tk UI, command CRC/sequence envelope, bounded planner, PS execution
reference model, calibrated LEVITATION_TRAP_V1 inspection, simulation/register
transcript adapters, explicit confirmation and STOP. BoardTransport fails closed.
Supported line, circle, semicircle, ellipse, finite hyperbola, rounded triangle,
rounded rectangle and bounded custom waypoints; mixed point movement is XY then Z.

## Workspace and motion limits

Origin is the geometric center of radiating-face centers. UI mm, internal m.
+X right, +Y up in plan view, +Z toward upper array. Default demo X/Y ±10 mm,
Z ±6 mm; engineering simulation envelope ±15/±15/±10 mm. No clipping.
Horizontal command speed 0.5–10 mm/s, default 3; vertical 0.5–5, default 2.
Acceleration defaults 20/10 mm/s²; quintic endpoints have zero velocity/acceleration.
50 Hz logical update rate; the 100 Hz option has not been validated in this stage.
All physical limits remain PROVISIONAL_UNTIL_HARDWARE_VALIDATED.

## Real evidence

- 90 final Python tests passed, including MOTION-SW01–37 and prior regressions.
- MOTION-RTL01–10 plus missing-ACK fault passed Icarus and Vivado 2025.2 XSim.
- Production 2,640,000-cycle cadence checked on both tools.
- Complete 3696-frame GUI→planner→trap→Controller→RTL demonstration passed three
  independent Icarus runs and one XSim run. All path, map, trap-report and ACK hashes matched.
- Demonstration: hold center → +8 mm X → center → 5 mm radius circle → rectangle
  → center → Z +4 mm → Z −4 mm → center, with explicit smooth lead-in segments.
- Every frame checked against all 128 requested/calibration codes and enable bits;
  Python independently checked effective-phase/mask ACK traces.
- Prior core, model-map, serializer and self-calibration Icarus/XSim regression passed.
- GUI starts and requires center ACK and explicit confirmation. DPI-correct full
  window screenshot was visually inspected. Actual particle position is NOT_MEASURED.
- Frozen v1 and native PCB sources unchanged; repository integrity and secret scan passed.

Evidence: validation/summary.json, regression/summary.json, final_python_tests.log,
presentation/, failures/, supplemental_validation.json. Large working simulator
files remain under ignored v2/build; curated evidence is archived here.

## Rejected/fixed cases

Out-of-workspace/nonfinite points, excessive/negative/invalid-zero speed, bounded
path limits, bad CRC/sequence, partial maps and invalid trap models are rejected.
Buffer underflow/overflow, STOP/reset mid-load, invalid frames and missing ACK fail
safe. STOP remains latched after release until reset. Failure evidence includes
XSim declaration ordering and Windows .bat parameter-tokenization, corrected without
weakening assertions. The existing adjacent SHA256 problem-record format is now
verified without rewriting its original problem or decision. Screenshot capture now
uses physical window bounds rather than Windows virtualized coordinates.

## Not validated / risks

No physical levitation, motion, mass support, driver voltage/current/temperature,
real acquisition, real PS deployment, board synthesis, implementation, timing closure
or bitstream is claimed. Whole-platform hardware gates B01/B03/B04/B05/B06/B07 remain.
Exact FPGA package, bank VCCO/pins, external serializer hold timing, independent
watchdog, batch characterization and real phase reference still require evidence.
The documented 33 MHz board clock and simulated 132 MHz digital profile are not
interchangeable with verified physical clock/pin constraints.

Trap scores use a directional-piston/high-contrast Rayleigh proxy in relative units,
not calibrated pressure or force. Gravity, streaming and finite-particle scattering
are omitted. Final 50 mg levitation remains a staged experimental target.

Full waveform simulation shortens the field interval to 8192 core cycles; production
50 Hz timing is independently counter-tested. Each interactive command is a fresh
simulation snapshot; the complete demo is continuous within one RTL run. The UI
retains logical command state after simulation, not a live physical waveform.

## Governance / next owner

Current user instruction sections 64/67 explicitly authorize the six stage docs and
observable interaction checkpoint. Work was not started. Chat history stays BLOCKED;
Codex transcript is PARTIAL and privacy-filtered. General shared narrative plans,
acceptance and handoff need a future authorized Work update; canonical engineering
state is current. This is not independent Chat acceptance.

Next owner: Chat/user independent review of this checkpoint. Stop before physical
bring-up, PCB changes, CV or v3. NOT RELEASED. NOT DEPLOYED.

Digital engineering self-check: ACCEPT WITH LIMITATIONS. Independent review pending.
