# v2 self-calibration digital/software architecture

Status: IMPLEMENTED / behavioral SIMULATION_ESTIMATE. Frozen v1 is untouched.
The user instruction is archived at AI-interaction-memory/codex/instructions/v2_self_calibration.md (repository root).

## End-to-end ownership

Host Controller -> synchronous 32-bit register bus -> mode/configuration -> common PL clock ->
single-TX burst and 128-channel field map -> serializer -> external driver boundary.
AD7606B -> four-lane capture -> 1024-frame buffer -> host read/ACK -> raw signed samples ->
TOF -> 6DoF geometry -> frequency response -> common f_work -> relative phase -> JSON/CSV ->
separate requested/calibration phase map -> atomic PL commit -> normal field.

`sono_digital_system.sv` is the integrated top. `sono_top.sv` and its inherited tests remain intact.
Modes 0..5 are SAFE_DISABLED, NORMAL_FIELD, CALIBRATE_GEOMETRY, CHARACTERIZE_TX,
CALIBRATE_PHASE, VALIDATE_FIELD. Three calibration modes share the acquisition engine; the
host selects estimation/sweep processing. VALIDATE_FIELD drives a supplied map; it does not
pretend an unimplemented physical closed-loop feedback system exists.

The current transport contract is real synchronous read32/write32, NOT a completed AXI/PS platform.
`software/control/host.py` implements configuration, read/ACK, errors, abort and atomic map upload.
A board-specific PS transport adapter is required before hardware deployment. No GPIO bit-banging
controls carrier timing. The timestamp counter, carrier, burst, ADC and serializer use one PL clock.

## Geometry and calibration references

128 TX: upper 0..63, lower 64..127, y-major/x-minor 8x8 at 12 mm radiating-face pitch.
8 RX: upper ADC0..3 and lower ADC4..7, corner order (+,+),(-,+),(-,-),(+,-) at 54 mm.
Pose is upper board in a lower-board local frame: tx,ty,gap (metres), roll,pitch,yaw (degrees),
SciPy extrinsic xyz Euler convention. Field coordinates subtract the mean of all TX radiating
centres; this is the user-defined geometric centre, including calibrated tilt/translation.
Nominal gap 100 mm, configurable physical range 90..115 mm. No PCB surface is a coordinate origin.

512 directed paths = lower TX64..127 to four upper RX, then upper TX0..63 to four lower RX.
All eight channels remain in each raw capture, even when only the opposite four are used.
RX blank bits are active high (bit0 upper, bit1 lower); default both blanked. Opposite RX is
unblanked during SETTLE/CAPTURE/DRAIN; transmitter-side RX remains blanked. The capture window
starts before TX and includes propagation, burst and ringdown. Capture data cannot be reused
until ACK. Abort disables TX and lets the outstanding ADC conversion drain.

## Estimators and identifiability

Raw ADC codes retain 2.5 V bias and noise; fitting removes DC explicitly. Quadrature matched
filter estimates integer TOF, parabolic peak refines it, and an envelope/carrier least-squares
fit resolves fractional samples. Coarse distance subtracts the known pretrigger offset.
Bounded robust least squares fits six pose parameters, rejects >1 mm path residuals and checks
Jacobian rank. Missing/rejected paths remain identified; no ground-truth pose enters the estimator.

A 31-bin 38.5..41.5 kHz sweep fits each TX peak by three-point log-amplitude interpolation.
Measured path magnitudes retain directivity; normalized median response and a weak-channel
penalty choose exactly one shared f_work. Bandwidth is null if the sweep does not bracket both
half-power crossings. Response amplitude is an analysis weight, not unimplemented analog amplitude control.

At f_work, subtract propagation and fit circular RX phase differences and per-TX phase. The two
opposed graphs have TWO independent phase gauges. Each bank requires an RX reference. The default
anchors are explicitly SIMULATION_REFERENCE_ONLY, NOT measured receiver calibration. Without
those references only per-bank relative TX phase is identifiable; absolute cross-bank phase must
not be presented as calibrated. Real captures are rejected if paired with the simulation reference.
Unmeasured RX group delay and TX ringup are confounded with distance. Initial coarse absolute
geometry comes from the envelope; conditional coarse+fine fusion uses fitted chain phase and the
coarse wavelength branch, then refits pose. Both poses are saved. Its small residual is internal
consistency, not independent evidence of physical accuracy or a removal of gauge ambiguity.

Positive RTL phase is temporal lag. Carrier fit uses cos(+omega*t+error); correction is positive
error. Acoustic field phasors use exp(-j*omega*t), so their intrinsic error is the negative of the
fitted temporal error. Requested geometric phase is -k*r; calibration remains an independent field.
Standing-wave mode adds pi to the lower bank. Hardware polarity still needs measurement.
Health GOOD/WEAK/OUTLIER/INVALID generates a recommended mask; active mask is unchanged unless
explicit application is enabled. Invalid phase never becomes a physical calibration claim.

## Environment and database

Cramer 1993 zero-frequency humid-air approximation takes temperature, RH, pressure and CO2.
Pressure 101325 Pa and CO2 420 ppm are explicit assumptions; temperature 26.5 C / RH55% is synthetic.
Validity checked: 0..30 C, 76..102 kPa, water fraction <=0.06. Ultrasonic dispersion, temperature
gradients and airflow remain physical error sources. Three values are checked against the Cramer
column of an independent 2026 JPCRD paper; no precision claim is inferred from those unit tests.

Calibration JSON records schema/version, source Git commit, board IDs, TX/RX batches, timestamp,
environment, sound speed, sample rate, burst parameters, raw source/hash/layout, pose/coarse pose,
common frequency, each channel's f0/quality/amplitude/phase/masks and reference provenance.
Archive files are addressed by SHA256; latest is atomically replaced. Synthetic epoch is fixed for
repeatability and explicitly labelled, never a measurement timestamp. Raw arrays stay under ignored
build/calibration_raw; regenerate from fixed seed and verify hash. No full raw waveform dump enters Git.

## Safety, timing and memory

Reset assertion and hardware disable force OE off asynchronously. Reset/enable release is
synchronized; a new serialized frame is required before publishing. ADC BUSY uses two-flop
synchronization. DOUT is source-synchronous and deliberately does not pass through a two-flop
bit synchronizer. The source-clock launch/capture timing requires real input/output constraints.
Host registers belong to the PL clock domain; an asynchronous host requires a proper bridge.
Configuration writes are permitted only in SAFE_DISABLED; phase map shadow writes are separate.
ADC, buffer, serializer and invalid-control faults fail closed. Fault recovery requires reset.
No FPGA-only design can guarantee OE turns off after loss of its own clock; external pullups and
power-stage interlock/watchdog are hardware requirements.

Clock profile: simulated 132 MHz; source reference documented N18/33 MHz. No PLL primitive,
legal MMCM parameters, target synthesis, CDC report, board XDC or timing closure is claimed.
At 41.5 kHz, 256 phase states need 10.624 MHz refresh: minimum 12 system cycles per sample.
32 lanes x four used outputs require 11 cycles per serializer frame. Shift-clock edges are 66 MHz
within a frame. Output sample quantization is <= one phase tick plus fixed serializer latency.
Burst onset and ADC first sample are timestamped; TX_ENABLE_TIMESTAMP records first published
burst frame. Physical calibration must use the actual serialized TX reference/latency, not assume
that a software trigger or PCB pin edge is the acoustic emission instant.

1024 * 8 * 16 bits = 16384 bytes (16 KiB) bounded frame RAM, plus registers. Synchronous 128-bit
read is coded for block RAM inference; resource mapping is unverified until a real part is known.
Host reads four little-endian uint32 words per frame (two int16 channels per word); writes
BUFFER_ADDR in words, waits one PL cycle, then reads BUFFER_DATA. Frame index is the conversion
index within that capture. Sample timestamp = first_sample_tick + frame_index*sample_period_ticks.
Future DDR/DMA attaches at this boundary, not to an invented current implementation.

## Reproduction and evidence

Run `python scripts/validate.py --output build/verification_review` from v2. It runs inherited
unit/RTL/map tests, the new software tests, three synthetic artifact repeats, three Icarus
acquisition repeats and XSim independent acquisition. Missing XSim yields PARTIAL.
`self_calibration_gate.py` is available separately. Full software test covers 512 paths at 31
frequencies. RTL exact round-trip covers 1024x8 samples; the 128-TX RTL sequencing test uses shorter
32-frame one-cycle captures. These scopes are recorded separately, not conflated.
Noise sweeps use unchanged baseline thresholds and retain failed/rejected levels.
Plots show normalized resonance, f0 distribution, phase/amplitude heatmaps, pose residuals and
XY/XZ/YZ fields for nominal versus calibrated LUTs evaluated in the same estimated geometry.
All pressure is relative. Nothing predicts guaranteed 50 mg levitation.

Sources: [AD7606B Rev B](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606b.pdf),
[Cramer original](https://doi.org/10.1121/1.405827),
[ETH acoustics equations](https://people.ee.ethz.ch/~isistaff/courses/ak1/skriptA1-english_2024.pdf),
[independent humid-air reference](https://doi.org/10.1063/5.0294663).
