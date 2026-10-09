> v5 inherited design/reference documentation. Original source is recorded in config/inheritance_manifest.json. Technical behavior/requirements are retained; historical numeric results are reference inputs, not v5 validation or AX7020 electrical qualification. Current board facts are config/board_facts.json; baseline results are evidence/BASELINE_VALIDATION.md.

# Interactive control architecture — v5

Stage: INTERACTIVE_LEVITATION_AND_TRAJECTORY_CONTROL. Project version stays v5.
Scope: **open-loop commanded trap position**, never measured particle position.
Validation status is recorded in `history_old/evidence/engineering/motion` as a frozen historical reference (explicit history access only); current validation is in `v5/evidence/migration/20261009/`;
this design document does not grant independent acceptance.

## Data and timing ownership

```
Tk desktop UI: binary framed high-level command + exact preview
  -> MotionController: PS execution reference running on the host
  -> Planner: bounded XY/Z paths, fixed 50 Hz logical samples
  -> TrapSolver: calibrated STANDING_WAVE LUT + local potential inspection
  -> Controller.stream_map: 128 complete register writes + COMMIT
  -> RegisterTranscriptTransport: validate and pack the register transactions
  -> SimulationTransport: real Icarus or Vivado 2025.2 XSim process
  -> sono_motion_system: bounded queue, clocked register-bus master
  -> existing sono_digital_system / phase_bank / serializer
  -> real RTL MAP_ACK and independently checked effective phase/mask
```

The GUI sends command envelopes, not ASCII phase maps. Hex files are private
simulator input artifacts made by the execution adapter. Their contents are
derived from the existing Controller API. Transcript generation never invents
a read acknowledgement: its `read32` explicitly rejects live reads.

The production queue interval is 2,640,000 core cycles at the inherited digital
132 MHz profile. It does not use a Windows GUI timer. Model samples carry 20 ms
logical target times. The full waveform regression shortens the interval to
8192 cycles to bound simulation cost; the unshortened production counter is
tested independently on both simulators. COMMIT is requested after the complete
map load; activation waits for a carrier boundary. Request cadence is exact;
activation has a bounded carrier-period latency. These are different metrics.

## Reuse and additions

Reuse: calibration database and calibrated geometry, selected `f_work`, separate
requested/calibration phases, common carrier, phase bank, output serializer,
ADC setup/model and static `Controller.apply_map` behavior.

Additions: motion profile/planner/trap inspection, command envelope, execution
model, GUI, transcript/simulation adapters, ring buffer and a digital wrapper.
`Controller.stream_map` leaves the active field enabled during shadow loading.
The sole addition to the existing digital-system port list is an internal
`motion_map_ack` output. No physical connector signal is assigned or required.

## Execution boundary and limitations

The PS execution model currently runs on the PC. Zynq PS firmware, AXI bridge,
serial/USB/Ethernet board transport, physical pins and clock synthesis are not
deployed. `BoardTransport` fails closed. A future board backend must enforce
verified hardware profile, calibration provenance, interlock and timeout gates.

Each user command is a fresh file-driven RTL simulation snapshot, not a live
board connection. The complete demonstration is one continuous 3696-frame RTL
run across all trajectory segments; no reset or disable is inserted between
its motion segments. The simulation ends with an explicit STOP check. The UI
retains the final *logical commanded position*, not a running physical output.
Desktop responsiveness and simulated field timing are intentionally separate.

Work remains OFF. The user explicitly authorized these six stage documents in
instruction sections 64 and 67. Other narrative plans/memories remain in Work's
domain; engineering facts take precedence if their older stage text differs.
