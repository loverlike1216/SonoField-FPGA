# v2 digital architecture and synchronous command interface

`sono_core` is a deterministic synthesizable RTL core, default CLOCK_FREQ=33,000,000 from hardware.const.
`sono_top` adds reset release synchronization, output serializer and safety gating. It requires an explicit
core clock; 132 MHz is the **simulated integration profile**, not a board-proven operating point.
The command interface is synchronous to this core clock. An AXI-Lite/PS/UART bridge and its CDC remain
board integration work; do not connect asynchronous host pins directly.

## Phase and timing

All channels share one integer fractional accumulator. Every clock, add `40000 * 256 = 10240000`;
when accumulated value reaches CLOCK_FREQ, subtract CLOCK_FREQ and increment the 8-bit master phase.
At 33 MHz a carrier period is exactly 825 clocks; phase bins last 3 or 4 clocks. At 132 MHz a period
is 3300 clocks; phase bins last 12 or 13 clocks. Phase quantization is 1.40625 degrees, with additional
edge placement quantization less than one core clock. Nominal 40 kHz still depends on the actual clock.

Each channel stores separate requested and calibration codes. Effective phase is their modulo-256 sum.
Positive effective phase is a **delay**: waveform is high when `(master_phase - effective_phase) mod 256 < 128`.
This matches the Python convention `Re[p exp(-j*omega*t)]` and propagation `exp(+j*k*r)` with requested
focus phase `-k*r`. This sign is documented so later PS code does not silently reverse steering.

## Command transactions

| Signal | Meaning |
|---|---|
| write_valid / write_ready | One channel transaction when ready; reject writes during pending commit |
| write_channel | RTL ID 0..CHANNELS-1; upper 0..63 and lower 64..127 in the physical 128-channel configuration |
| requested_phase / calibration_phase | Independent unsigned 8-bit phase values |
| channel_enable | Per-channel mask stored and committed with the phase map |
| commit | One-clock pulse after all channel entries have been written |
| pending | Complete shadow map frozen until next carrier boundary |
| commit_ack | One-clock pulse when all active entries change together at phase zero |
| command_error | One-clock rejection indication; caller must observe/log it |
| hardware_enable | Active-high external permit; asynchronous assertion of disable |
| software_enable | Synchronous user drive permission |
| output_disable | Active-high external OE/driver disable request |
| serializer_fault | Sticky overrun indication; reset required |

Write all CHANNELS entries, including disabled channels. A bitmap verifies completeness. COMMIT and WRITE
on the same edge are rejected together. Repeated commits while pending are rejected. A commit arriving on a
boundary is queued for the next boundary. After ACK, shadow completeness clears for the next full map.
Requested values and calibration are never merged in persistent storage. Actual storage is parallel register
banks, deliberately not inferred sequential BRAM: all 128 active phases/masks update on the same edge.

Host recipe: export CSV → retain the separate calibration column → write all 128 rows with ready handshake
→ pulse COMMIT → wait ACK → assert software permission only after electrical checks.
The map-to-RTL test exercises the exported field maps for 2/32/72/128 emitters. No real PS transport is claimed.

## Serializer candidate

32 parallel lanes, each drives one shift register; only Q0..Q3 of each 8-bit package are used. Q4..Q7 are
unconnected. Channel `c` maps to lane `c//4`, output `c%4`. Send bits 3,2,1,0, then one shared latch.
Do not cascade these candidate registers. The FPGA captures the entire 128-bit waveform before shifting.
All registers latch simultaneously; shared-clock electrical skew is a later board timing constraint.

At 132 MHz: SCLK=66 MHz during a frame, 7.576 ns half-period; sample-to-latch=9 clocks=68.18 ns.
The frame requires 11 clocks before the next capture; shortest phase bin is 12 clocks. Thus digital simulation
does not lose samples. A bandwidth guard refuses a 33 MHz / 32-lane top configuration instead of reducing
phase accuracy silently. The core itself works at 33 MHz. Serialized carrier phase has a common fixed
pipeline delay relative to the internal phase reference; relative channel phase remains coherent.

Physical candidate: 5 V 74AHCT595 (TTL input thresholds), conditional on verified FPGA VOH/VCCO,
buffer loading, fanout and worst-case timing. At 3.0–3.6 V the 74AHC595's full-temperature guaranteed
frequency is insufficient for this profile. See hardware/interface.md for component evidence and limits.

## Safety boundary

Reset asserts asynchronously, releases through two flops. Hardware disable suppresses outputs even between
clock edges; release is synchronized and requires a fresh completed frame. No map means no drive.
Serializer overrun is sticky and immediately disables output. Software disable also forces low logical outputs.
Enable can start mid-carrier; no claim of pulse-length-preserving enable or glitch-free phase jump is made.
Atomic phase changes can intentionally shorten a transition pulse; power-stage design must tolerate that.

`safe_waveform` is a logical debug/reference bus, not 128 board pin assignments. Production board wrappers
must not map command/debug buses to package pins. Hardware must independently pull OE inactive and
driver inputs safe while FPGA is unconfigured, clock-stopped or unpowered. FPGA OE high means external
595 outputs are high impedance, not inherently a safe bridge state. Pull-downs and power-stage interlock
are mandatory. Clock-loss protection requires external watchdog/power gating and is not implemented in this core.
