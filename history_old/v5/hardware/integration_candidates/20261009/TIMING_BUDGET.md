# External timing remains an independent gate

Preserve132MHz internal target,66MHz SRCLK and32 lanes/four used595 outputs. AX7020 documented physical input is50MHz/U18; vendor hello XSA FCLK0 is50MHz. Neither creates132MHz without a qualified clock adaptation. This iteration did not instantiate or download a PS/PL clock adapter. No new board-level routed timing claim is made.

Current serializer changes DATA with the falling SRCLK launch and samples into595 on a later rising SRCLK. Core period≈7.576ns, SRCLK period≈15.152ns. At3.3V SN74LVC595A specified minimum clock ceiling is104MHz under specified test load; setup requirement2.5ns leaves approximately5.076ns **before** worst-case FPGA pin timing, AXC, fanout, cable skew and jitter. Frequency capability alone is not interface closure.

For each branch and direction:

```
setup_margin = Tcore + CLK_path_min - DATA_path_max - t_setup_595 - jitter
hold_margin  = Tcore + DATA_next_path_min - CLK_path_max - t_hold_595 - jitter
```

Check first DATA bit, final SRCLK→RCLK setup, SRCLK/RCLK pulse widths, SRCLR recovery/removal, and RCLK→TC4427A output skew. Fanout delay on clocks without matching data can improve setup but reduce hold. Both array branches must share a verified latch epoch; independent local qualification may disable one branch without silently claiming a complete two-array field.

Include AX7020 documented33ohm source resistor arrays, central buffering, each array's4-output SRCLK and4-output RCLK distribution,≤20cm candidate ribbon with paired return paths, actual load/fanout and min/max PVT delays. Do not automatically add another33ohm in series everywhere. Review overshoot/edge quality with real cable/receiver before fixing termination.

ADC candidate four-DOUT mode needs32 SCLK edges per8-channel frame. Current adc_serial at132MHz uses33MHz SCLK; confirm the first-MSB interval, C-16 output-valid delay, board/cable return path and setup at the actual sampling edge. Monitor BUSY via existing synchronizer; do not use it as an unconstrained clock.

Required release evidence: production matched pin XDC, clock definitions, board route WNS/TNS/WHS/THS, unconstrained endpoints, CDC, IO delays/min/max constraints with source attribution, DRC, and oscilloscope/logic-analyzer input/clock/latch traces at each worst-case branch/load. Existing OOC or internal simulation PASS is not this result.

Source: [TI SN74LVC595A](https://www.ti.com/lit/ds/symlink/sn74lvc595a.pdf), [SN74AXC8T245](https://www.ti.com/lit/ds/symlink/sn74axc8t245.pdf), existing serializer.sv/adc_serial.sv. Status: NOT_VERIFIED_EXTERNAL_TIMING.
