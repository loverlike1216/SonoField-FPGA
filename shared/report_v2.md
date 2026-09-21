# v2 self-calibration software/digital review report

PROJECT_ID: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
workspace_path: E:\Codex-project\AMD-SonoField-FPGA
branch: main
active_version: v2; v1 FROZEN
stage: SELF_CALIBRATION_SOFTWARE_AND_DIGITAL_SYSTEM
local HEAD / origin HEAD at preflight: 5fa046d0ad3dd7fe0c44824b74b71f974f9a09bc
validated source checkpoint: PENDING_SOURCE_COMMIT
delivery: PENDING_FINAL_CHECKPOINT

Pre-commit calibration records identify the then-current Git parent. Exact changed implementation
is identified by source hashes in the validation summary. Clean-clone records identify the committed
source used. A later evidence-only delivery commit does not change validated sources.

## Inherited Baseline

All inherited sources retained in v2. Original 212-file v1 and Git tree
1d2bec2f8eb1c2151e7bf31f0c72fc88391d8a2d unchanged. Phase generation, safety, atomic commit,
serializer order, geometry and acoustic models rerun. Bootstrap evidence remains separate.

## Implemented

Integrated register-controlled PL top, runtime carrier, calibration modes, finite burst,
opposite-RX blanking, 128-TX scheduler, ADC interface and bounded capture/read/ACK. Python
raw-to-geometry/response/phase/database/LUT pipeline, generated registers, host API,
synthetic generator, noise/repeatability tools, plots and hardware/software contract.

## AD7606B Configuration

Software mode OS111 / serial selected. Four DOUT, eight signed 16-bit channels, 800 kSPS profile
and tested 400 kSPS option. CONFIG/range writes and readback; +/-5 V with 2.5 V AFE bias.
No CRC/status/oversampling. Full reset/setup, initial >2 s power wait (only that wait shortened in TB).
Rev B Figure73: A=V1/V2, B=V3/V4, C=V5/V6, D=V7/V8. No physical ADC result claimed.

## FPGA/PL Architecture

Shared simulated 132 MHz, 33 MHz SPI, 32 serializer lanes/four used outputs each. Shadow/active
phase bank with separate requested/calibration/mask and atomic commit; 16 KiB frame RAM.
Safe reset, asynchronous hardware kill/synchronous release, fault/abort disable, ACK before reuse.
Synchronous host domain, synchronized BUSY, source-synchronous DOUT. Physical PLL/CDC/timing
reports require the exact FPGA and constraints. Those facts are not invented.

## PS/Software Architecture

Controller read32/write32 API implements configuration, capture/ACK, abort and map upload.
Actual PS AXI/transport adapter remains a board integration boundary. No live hardware or GPIO
carrier control claimed. Sound speed takes explicit temperature/RH/pressure/CO2. Machine-readable
configuration and metadata; SHA256 archive plus atomically replaced latest calibration file.

## Calibration Pipeline

128 TX captures x four opposite RX = 512 paths at 31 frequencies. Raw frames retain all eight
channels, DC/noise/gain/phase/delay/directivity/resonance and envelope dynamics. Quadrature
matched filter plus fractional envelope fit -> robust pose -> response/common carrier -> circular
chain/TX phase -> conditional coarse/fine geometry -> separate LUT fields. Estimators receive no truth object.

## Geometry Calibration

12 mm radiating-centre pitch, +/-42/30/18/6 mm grid, 100 mm nominal / 90..115 mm gap.
Four RX corners per bank at +/-54 mm. Pose uses the lower-board frame; field coordinates recentre
the actual TX geometry. Ten poses cover nominal/gap/XY/roll/pitch/yaw/combined/noise/outliers/missing paths.
35 dB baseline translation error 0.020748 mm; angle error 0.016860 degrees; refined residual
0.006803 mm. Refinement depends on fitted chain phase; its residual is not independent physical accuracy.

## Frequency Characterization

38.5..41.5 kHz / 100 Hz steps, interpolated per-TX f0 and one common f_work = 40300 Hz.
f0 RMSE 51.679 Hz at 35 dB. No per-channel drifting oscillators.

## Phase Calibration

Baseline phase RMSE 0.607345 degrees. Opposite banks form two independent phase gauges;
two reference measurements are required. Default anchors are SIMULATION_REFERENCE_ONLY.
Real records cannot use simulated references. Unreferenced/active-invalid LUTs fail closed.
Recommended weak-channel masks stay distinct from active masks. Requested and calibration phases
remain separate 8-bit fields; physical polarity and RX group delay remain unmeasured.

## Validation

44 Python tests PASS (19 inherited + 25 new). Inherited TB01..15 and CAL-TB01..15 plus fault tests PASS.
[Validation summary](../v2/evidence/self_calibration_stage/validation/summary.json),
[calibration summary](../v2/evidence/self_calibration_stage/validation/self_calibration/summary.json).

## Vivado Evidence

Vivado 2025.2 XSim compile/elaboration/simulation PASS for inherited and integrated acquisition tests.
Target synthesis/implementation/bitstream/timing closure remain BLOCKED/NOT_RUN. Reproducible target
Tcl selects the integrated top and requests a CDC report only after the board gate is satisfied.

## Icarus Evidence

Inherited counts 1/2/7/32/72/128 PASS. Three integrated acquisition runs return identical samples.
128-TX scan covers both directions using 32-frame captures; full-buffer test uses 1024 frames.
The generated calibrated phase map is loaded into the actual bank and normal field operation resumes.

## Python Evidence

Raw decoding, environment, TOF, phase/circular arithmetic, coarse/fine distance, robust pose,
frequency optimizer, health, database and geometry/LUT tests pass. Relative-pressure plots:
[focus](../v2/evidence/self_calibration_stage/validation/self_calibration/plots/field_focus.png),
[standing wave](../v2/evidence/self_calibration_stage/validation/self_calibration/plots/field_standing_wave.png).
Research novelty is NOT_CONFIRMED; no novelty or absolute-force claim is inferred.

## End-to-End Synthetic Test

All 512 paths across 31 frequencies, fixed seed 7020, 35 dB and specified 6DoF perturbation.
Behavioral ADC -> RTL -> software roundtrip matches 1024x8 signed samples exactly, including
negative endpoint codes in the unused bank. Decoded opposite-bank samples feed the actual TOF
estimator unchanged. Roundtrip hashes and commands are in the calibration summary above.

## Robustness Test

Fixed limits: translation <0.1 mm, angle <0.1 degree, f0 RMSE <80 Hz, phase RMSE <2 degrees.
35 dB passes. 25 dB: translation 0.0762 mm, angle 0.0488 degrees, phase 1.8738 degrees,
but f0 RMSE 153.339 Hz exceeds the limit; 127 valid channels and a blocked full active LUT.
15 dB: phase graph rejected. 5 dB: too few characterized channels. Failures are retained.
This is a fixed-seed synthetic operating envelope, not a universal measured SNR specification.

## Reproducibility

Three byte-identical JSON / phase-LUT CSV / health CSV outputs per environment; numeric tolerance 1e-12.
Three Icarus ADC hashes and XSim hash agree. Inherited traces still match the Python oracle.
Fresh clone without v1 working directory and isolated locked venv: PENDING_FRESH_CLONE.

## Hardware Interface Contract

[Contract](../v2/docs/hardware/PCB_SOFTWARE_INTERFACE.md) specifies signals, blanking, ADC startup,
sample format/timestamps, registers/ACK, rails and future timing/AFE measurements. BOM strings retained.
SN74AXC8T245 is not a 5 V translator. No guessed connector pin, schematic or PCB layout is frozen.

## Not Yet Validated

Actual PS transport, PLL/IO timing, synthesis/resources, ADC/AFE electrical performance, receiver
phase/timing references, batch qualification, physical geometry/pressure/force and levitation.
No physical photos, scope traces or mass results exist. No 50 mg success claim is made.

## Blockers

B01 exact FPGA package/speed; B03 VCCO/connector ambiguity; B04 serializer electrical margin;
B05/B06 transducer and physical evidence; B07 real RX/TX timing/phase reference. External ChatGPT
access BLOCKED. These limit deployment/full-platform acceptance. Fresh-clone reproduction remains
the software delivery gate at this checkpoint.

## Risks

TOF depends on envelope/group-delay assumptions; phase gauges need external references. ADC return
timing and serializer timing require real translator/cable/skew constraints. Synthetic chip behavior
does not qualify real silicon. 12 mm pitch is not lambda/2, and relative pressure does not prove force.
External interlock must cover clock loss/power transients. Independent user/ChatGPT review pending.

## Files Changed

New acquisition/calibration RTL and integrated top, generated registers, ADC model/testbench,
software/calibration/characterization/control, configs and 25 tests. Validation/target Tcl extended.
Technical docs, shared state and observable interaction records updated. No frozen v1 edits,
build caches or raw capture cubes committed.

## Git Commit

PENDING_SOURCE_COMMIT, then fresh-clone evidence checkpoint and non-force push to main.

## Next Recommended Stage

Independent review of report/evidence. Only after user direction, close board/reference facts and
perform PH0 electrical/receiver/ADC characterization. Do not automatically start PCB implementation.

REVISE
