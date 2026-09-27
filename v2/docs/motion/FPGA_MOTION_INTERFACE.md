# FPGA motion interface — v2

`sono_motion_system` wraps the existing digital core with `motion_queue` and a
register-bus multiplexer. It is a digital integration boundary, not a board top
with pin constraints or deployed PS firmware.

## Complete-map ingress

| Signal | Meaning |
|---|---|
| frame_data[2175:0] | 128 × 17-bit words; word i at [17*i +: 17] |
| Word bits [7:0] | requested_phase |
| Word bits [15:8] | calibration_phase |
| Word bit [16] | channel enable |
| frame_sequence[31:0] | Contiguous sequence beginning at zero after reset |
| frame_last | Final map; normal completion holds it |
| frame_valid / frame_ready | Enqueue pulse only when ready; retry if not ready |
| motion_arm | Start after at least two maps, or one final map, are buffered |
| motion_stop | Immediate output gate plus latched stop/queue clear |
| acknowledged_sequence | Sequence whose entire map received real MAP_ACK |

Default capacity is four maps; minimum is two. `frame_ready` is low during a pop
to avoid simultaneous count-update ambiguity. A producer must not assert an
enqueue pulse on full: that is an overflow fault, not an implicit overwrite.
No map is accepted after the final marker. All-disabled frames and invalid
sequence are rejected. An incomplete packed frame cannot be enqueued because
the complete payload is one transfer; register transcripts independently verify
exactly 128 unique channel writes before packing.

## Existing register bus

The queue writes MAP_CHANNEL (0x54), MAP_DATA (0x58), MAP_WRITE (0x5c) for all 128
channels, then MAP_COMMIT (0x60). Existing phase-bank shadow/active semantics
remain authoritative. The wrapper consumes the internal `motion_map_ack` pulse.
It emits no success based solely on COMMIT acceptance. Host accesses while the
queue owns the bus are rejected; configuration is performed before arming.

The existing static `Controller.apply_map` remains available. New
`Controller.stream_map` uses the same map/register representation but does not
abort, change mode or enable output between frames. The execution adapter owns
cadence, buffering and acknowledgement. GUI commands contain magic SONO,
version, sequence, bounded payload length, command ID and CRC32; maximum payload
is 16 KiB. The host-side PS model decodes this high-level envelope.

## Timing and evidence

At 132 MHz, the production interval is 2,640,000 cycles (50 Hz). A map load takes
770 bus-master cycles before waiting for a carrier-boundary ACK. The active field
continues during shadow writes. Request intervals are exact; map activation can
vary within one carrier period after commit. Missing ACK or a deadline overrun
disables outputs. Existing 32-lane serializer timing is reused, not assumed to
be physically qualified by these tests.

`tb_motion` drives the integrated wrapper, verified ADC model and actual phase
bank. For every ACK, it checks all requested codes, all calibration codes and all
mask bits against Python-generated input, detects changes outside atomic commit,
and checks interval/sequence/STOP. Python independently checks the output ACK
trace's effective phase and mask. `tb_motion_faults` injects buffer and control
failures; it uses a bus responder for isolated queue testing. The full integration
test is separate and does not substitute that responder for the actual core.

Both Icarus and Vivado 2025.2 XSim run the isolated faults, production cadence,
and integrated demonstration. Simulation-only changes: shortened ADC power wait
(32 cycles), 8192-cycle full-demo interval. ADC reset/setup and carrier frequency
are not shortened. The production cadence is tested at its full count separately.

No new physical pins, connector signals, XDC or PCB edits are introduced. PS
arbitration software, hardware transport and target synthesis/timing remain
NOT_VERIFIED. Simulation cannot establish external shift-register setup/hold.
