# v2 software validation matrix

Scope: software and behavioral digital simulation. Source/evidence version v2; v1 frozen.
Paths below are relative to v2. `V` means evidence/self_calibration_stage/validation_frequency.
`C` means V/self_calibration. `R` means evidence/self_calibration_stage/reproducibility_review.
PASS entries have actual tools behind them. R passed on 2026-09-24 at 9c058fe3b02469a6d36a08e3a7cbedd19076e67b.

| Requirement | Implementation | Unit test | Integration test | Independent oracle | Evidence | Status | Limitation |
|---|---|---|---|---|---|---|---|
| Inherited 128 phase engine | rtl/sono_core.sv, phase_bank | TB01..15 | tb_system, tb_phase_map | Python + Icarus + XSim | V/summary.json | SIMULATED PASS | No target timing |
| CAL-TB01 burst/frequency | burst_generator | Burst duration assertion | tb_calibration | System clock count | C/icarus_0.log, xsim.log | SIMULATED PASS | Serialized edges quantized |
| CAL-TB02 one TX | integrated top waveform mux | One-hot assertion | All scan captures | Testbench TX identity | C/icarus_0.log | SIMULATED PASS | No power driver |
| CAL-TB03 64-order | calibration_scheduler | Each selected ID asserted | Both banks | Expected 64..127,0..63 | C/icarus_0.log | SIMULATED PASS | Shorter scan captures |
| CAL-TB04/05 directions | scheduler/mux | TX and blank bank assertions | 128 captures | Configured RX map | C/icarus_0.log | SIMULATED PASS | No acoustic path |
| CAL-TB06 blank | rx_blank FSM decode | State/bank assertions | Settle/capture/drain/abort | TB opposite-bank rule | C/icarus_0.log | SIMULATED PASS | Switch electrical settling unmeasured |
| CAL-TB07 BUSY | ad7606b_if | 650/850 ns completion + timeout | adc_serial | Independent datasheet model | C/xsim.log | SIMULATED PASS | No actual silicon |
| CAL-TB08 capture | ADC interface/buffer | Every 128-bit frame compared | 1024-frame readback | Python-generated raw vector | C/summary.json | SIMULATED PASS | One full-size roundtrip capture |
| CAL-TB09 ordering | Four lanes -> eight words | Every channel/word compared | Host raw decode | Signed code vector | C/summary.json | SIMULATED PASS | Fixed software-mode profile |
| CAL-TB10 bounds | Bounded RAM/ACK | 1024 frames, no overwrite | Read all 4096 words | Expected vector and held first word | C/icarus_0.log | SIMULATED PASS | BRAM mapping not synthesized |
| CAL-TB11 abort | CONTROL/kill FSM | Abort during active burst | Disable/blank check | TB output assertions | C/xsim.log | SIMULATED PASS | External interlock still needed |
| CAL-TB12 normal return | phase bank/serializer | Calibrated sum each TX | Load actual Python LUT, restore field | Generated LUT + inherited waveform oracle | C/xsim.log | SIMULATED PASS | No PS AXI wrapper |
| CAL-TB13 reset OE | async kill/sync release | OE/reset checks | Hardware enable + faults | Two simulators | C/xsim.log | SIMULATED PASS | Clock-loss safety external |
| CAL-TB14 sweep | Runtime frequency register | 38500/40000/41500 | Captures at 400/800 kSPS | Burst counter + register values | C/icarus_0.log | SIMULATED PASS | Analog transfer synthetic |
| CAL-TB15 exact vector | adc model -> RTL -> decode | int16 signed corners | Read/ACK -> TOF | Raw byte equality | C/summary.json | SIMULATED PASS | Simulator device model |
| SW-T01 environment | sound_speed.py | SW03/04 | Full pipeline | Published Cramer reference values | V/python_tests.log | TESTED PASS | Zero-frequency approximation |
| SW-T02 burst | synthetic.py | SW22 deterministic | 512-path experiment | Ground truth only in evaluation | C/summary.json | TESTED PASS | Synthetic transfer model |
| SW-T03/04 integer/fractional TOF | signal.py | SW05/24 | Raw end-to-end | Known delayed waveform | V/python_tests.log | TESTED PASS | Envelope/group-delay assumptions |
| SW-T05 noisy TOF | signal.py | SW24 | 35/25/15/5 dB experiment | Fixed seed truth | C/robustness.json | TESTED, LIMITS REPORTED | 25 dB f0 fails;15/5 rejected |
| SW-T06/07 phase/wrap | signal.py | SW06/07 | Full phase calibration | Analytic cosine and circular cases | V/python_tests.log | TESTED PASS | RX references required |
| SW-T08 coarse/fine | signal.py, pipeline | SW08 | Conditional pose refinement | Known distances + full synthetic truth | C/metrics.json | TESTED PASS | Fitted phase is not independent ranging |
| SW-T09..12 6DoF | geometry.py | SW09 ten cases | Full raw pipeline SW13 | Injected pose only evaluated afterwards | V/python_tests.log, C/metrics.json | TESTED PASS | Physical geometry unmeasured |
| SW-T13/14 outlier/missing | robust solve_pose | SW09/10 | Combined pose cases | Known geometry, corrupt/NaN paths | V/python_tests.log | TESTED PASS | Unobservable graph rejected |
| SW-T15 f0 | response.py | SW11/15 | 31-bin raw sweep | Injected independent resonances | C/metrics.json | TESTED PASS at35 dB | Boundary peaks/bandwidth flagged |
| SW-T16 f_work | common_frequency | SW12 | One common LUT frequency | Optimizer objective saved | C/calibration.json | TESTED PASS | Objective is an engineering policy |
| SW-T17 channel phase | pipeline circular fitting | SW14/21/23/25 | Full pipeline to RTL map | Truth error RMSE; invalid-reference guards | C/metrics.json | TESTED PASS | Simulated anchors only |
| SW-T18 database | database.py | SW18/19 | Three saved artifacts | Hashes + signed decode | C/summary.json | TESTED PASS | Synthetic epoch labelled |
| SW-T19 geometry switch | phase_lut | SW17 | Nominal/calibrated plots | Same estimated actual field geometry | C/plots | TESTED PASS | Relative pressure only |
| SW-T20 LUT regeneration | pipeline + phase_bank | SW17/23 | Generated LUT -> real RTL bank | Requested/calibration sum | C/xsim.log | SIMULATED PASS | No hardware output measurement |
| Mask and safety API | host.py/pipeline | SW16/20/23/25 | ACK/map/fault RTL tests | State/phase/mask checks | V/python_tests.log | TESTED PASS | Hardware adapter future |
| Determinism | calibration gate | SW22 | Three JSON/CSV, three RTL runs | XSim vs Icarus raw hash | C/summary.json | TESTED PASS | Fixed stack/seed,1e-12 tolerance |
| Standalone | reproduce.py | Environment/pip audit | Entire gate without v1 worktree | New venv/clone | R/summary.json | TESTED PASS | Same Windows host |
| Frozen parent | check_migration.py |212 hashes | Git tree/content audit | Git objects | Repository audit | VERIFIED | No v1 edits |
| Target synthesis | create_project.tcl | Missing-part guard | Actual Vivado rejection | Verified board facts | evidence/self_calibration_stage/board_gate | BLOCKED | Exact part/VCCO unknown |
| Hardware | Hardware contract | None | None | No physical evidence | shared/BLOCKERS.md at root | NOT_VERIFIED | No levitation claim |

No asserts were removed or thresholds relaxed to hide failures. The only initial test correction was
centroid roundoff tolerance 1e-16 ->1e-15 m (far below engineering scale), plus required metadata in
the database fixture. Actual algorithm precision thresholds were fixed before acceptance runs.

SW26 checks the host transaction writes computed f_work before enabling NORMAL_FIELD; CAL-TB12
measures the resulting period. Artifact repeat hashes describe generated files before Git text
normalization; compare CSV/JSON content as UTF-8 with LF when inspecting Git checkout copies.
ADC binary hashes are byte-exact and independent of line endings. Source hashes explicitly use
CANONICAL_LF_UTF8; frozen v1 still uses its original byte hashes.
