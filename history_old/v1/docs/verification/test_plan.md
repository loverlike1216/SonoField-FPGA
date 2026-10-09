# v1 automated evidence matrix

| Requirement | Executable evidence |
|---|---|
| TB01 40 kHz | tb_core: analytic fractional timebase every clock; 825 clocks per 33 MHz period |
| TB02 zero phase | first-map channels 0 and 1; all waveform bits checked each clock |
| TB03 90 degrees | first-map channel 2 = 64; discrete phase timing checked |
| TB04 180 degrees | first-map channel 3 = 128 |
| TB05 wrap | master counter wraps and requested 255 + calibration 1 = 0 |
| TB06 128 coherent channels | per-clock checker plus 1,056,000 Python bit comparisons per full run |
| TB07 separate calibration | nontrivial independent patterns across all channels, modulo addition checked |
| TB08 atomic commit | full-map completeness, rejected empty/partial transaction, frozen pending map, period-boundary ACK, no mixed map |
| TB09 reset/disable | tb_system asynchronous reset and mid-clock hardware kill; masked output zero |
| TB10 enable | no enable without map/frame, synchronized reenable, software disable |
| TB11 parameters | Icarus CHANNELS = 1,2,7,32,72,128 |
| TB12 serializer order | external shift-register behavioral scoreboard, expected serial edge count |
| TB13 channel map | every lane/Q mapping, odd channel padding, upper/lower IDs in Python map checks |
| TB14 Python cross-validation | independent analytic check of every trace row; acoustic-map hex vectors tested in RTL |
| TB15 determinism | 3 Icarus runs and 3 XSim runs; identical SHA-256 for the 128-channel trace |

Additional checks: serializer sticky overrun disables output, insufficient-clock profile fails with a
specific bandwidth error, channel masks commit with the phase map, simultaneous WRITE+COMMIT rejected,
19 Python checks including analytic superposition, directivity, gradient convergence, exact radiating-center
coordinates, face-gap travel limits, global symmetry, channel corners, envelope and gap-dependent phase maps.
Current configured 128-channel STANDING_WAVE/FOCUS maps at 90/100/115 mm pass through the RTL bench
in both simulators. Historical counts and trace evidence below remain associated with their original revision.

Both simulators use the same self-checking benches, but the Python oracle computes expected time/intervals
independently. The physical shift register, propagation skew and bridge are not modeled as timing-annotated
electrical circuits. This is independent **tool** validation, not external human acceptance or hardware testing.

Initial XSim launch failed because Windows batch forwarding split an `=` plusarg. The fix uses the
testbench default filename and copies completed traces; no assertion was removed. Initial failure evidence
is retained in Git history; current successful runs are under evidence/validation/.

No target synthesis PASS is available without a documented FPGA ordering code. `create_project.tcl`
fails closed if verified part/clock source configuration is absent. No implementation or bitstream is claimed.
