> v5 inherited design/reference documentation. Original source is recorded in config/inheritance_manifest.json. Technical behavior/requirements are retained; historical numeric results are reference inputs, not v5 validation or AX7020 electrical qualification. Current board facts are config/board_facts.json; baseline results are evidence/BASELINE_VALIDATION.md.

# Safety limits — v5 motion digital stage

All physical limits remain **PROVISIONAL_UNTIL_HARDWARE_VALIDATED**.
SIMULATION_VALIDATED can describe the archived digital gate only.
No component, board, workspace or particle is marked HARDWARE_VERIFIED.

Startup is SAFE_DISABLED with commanded (0,0,0), no trajectory and zero velocity.
Motion requires connected simulation, loaded calibrated record, valid working
frequency, center map acknowledgement and explicit operator confirmation.
Connecting alone never moves or arms the field. Nominal uncalibrated motion is
not offered by the normal UI. Synthetic calibration is confined to simulation.

The software rejects invalid/nonfinite targets, out-of-bounds paths, speeds,
overlarge commands, unsupported trajectories, stale previews, repeated command
sequences, CRC errors and missing/invalid local trap solutions. Calibration
codes are checked for consistency throughout each path. Full map validation
precedes COMMIT; partial or duplicate-channel maps are rejected.

The ring buffer accepts complete 128-channel maps with contiguous sequence IDs.
Normal completion holds the last map; unexpected underflow disables. Overflow,
invalid frame/sequence, bus fault and lost ACK disable. STOP clears queued work
and latches the disabled condition; merely releasing STOP cannot restart stale
motion. Reset is required to clear that latch. Hardware disable gates output
independently of GUI processing. A reset discards incomplete map loads.

Software STOP cancels the simulation process and increments a generation token,
so an old worker cannot publish a successful position after cancellation.
This is a desktop/simulation guarantee, not a certified physical emergency stop.
The real independent watchdog, power qualification and physical kill circuit
remain blocked by the existing hardware review.

The normalized potential test is not a safety certificate. Real bring-up still
starts with conservative transducer voltage and a small particle, records mass,
diameter and density, then advances through 5/10/25/50 mg as measured evidence
allows. Increasing emitters or drive without root-cause analysis is not authorized.

Board deployment additionally requires exact FPGA ordering code/package, VCCO,
connector/pin mapping, clock implementation, serializer timing, qualified driver
and transducer batch, calibrated receive reference, and real PS transport.
Those gates are unchanged; no new XDC or PCB edits were made for this stage.
