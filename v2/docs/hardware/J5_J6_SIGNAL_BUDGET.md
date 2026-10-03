# SonoField-FPGA v2 / pre-PCB interface review

Current model: GPT-6.1 Sol High. Status: CANDIDATE / NOT ELECTRICALLY FROZEN.

The existing architecture has ONE AD7606B for eight RX paths, four from each array. There is ONE ADC SPI bus, not two opposing ADC buses. Candidate J5 uses five upper TX/blanking controls, ten shared ADC signals and one proposed fault input (16/16). J6 uses five lower TX/blanking controls plus one proposed fault input (6/16), leaving ten unassigned pins. Lower analog RX reaches the shared ADC through its analog interconnect; it does not duplicate digital ADC ownership on J6.

UPPER/LOWER_FAULT_N are proposals requiring firmware/RTL/electrical implementation. Current core exports a global safety disable, not separately qualified per-array enables. The upper/lower controls must derive from the same timing reference and each board must remain disabled during reset, loss of lock, transport failure and absent external power. Exact assignments are provisional, not an accepted PCB freeze.

J5 spans banks34 AND35. J6 uses bank34. All5V pins are AUX/UNUSED, never a GPIO voltage specification.

| Connector pin | Package ball | Bank | Signal | Direction |
|---|---|---|---|---|
| 1 | N20 | 34 | UPPER_SHIFT_CLK | FPGA_TO_BOARD |
| 2 | P20 | 34 | UPPER_LATCH_CLK | FPGA_TO_BOARD |
| 3 | M17 | 35 | UPPER_OE_N | FPGA_TO_BOARD |
| 4 | M18 | 35 | UPPER_BOARD_ENABLE | FPGA_TO_BOARD |
| 5 | M19 | 35 | UPPER_RX_BLANK | FPGA_TO_BOARD |
| 6 | M20 | 35 | ADC_RESET | FPGA_TO_BOARD |
| 7 | L19 | 35 | ADC_CONVST | FPGA_TO_BOARD |
| 8 | L20 | 35 | ADC_CS_N | FPGA_TO_BOARD |
| 13 | K19 | 35 | ADC_SCLK | FPGA_TO_BOARD |
| 14 | J19 | 35 | ADC_SDI | FPGA_TO_BOARD |
| 15 | H16 | 35 | ADC_BUSY | ADC_OR_FAULT_TO_FPGA |
| 16 | H17 | 35 | ADC_DOUT_A | ADC_OR_FAULT_TO_FPGA |
| 17 | G17 | 35 | ADC_DOUT_B | ADC_OR_FAULT_TO_FPGA |
| 18 | G18 | 35 | ADC_DOUT_C | ADC_OR_FAULT_TO_FPGA |
| 19 | G19 | 35 | ADC_DOUT_D | ADC_OR_FAULT_TO_FPGA |
| 20 | G20 | 35 | UPPER_FAULT_N | ADC_OR_FAULT_TO_FPGA |

| Connector pin | Package ball | Bank | Signal | Direction |
|---|---|---|---|---|
| 1 | T11 | 34 | LOWER_SHIFT_CLK | FPGA_TO_BOARD |
| 2 | T10 | 34 | LOWER_LATCH_CLK | FPGA_TO_BOARD |
| 3 | U12 | 34 | LOWER_OE_N | FPGA_TO_BOARD |
| 4 | T12 | 34 | LOWER_BOARD_ENABLE | FPGA_TO_BOARD |
| 5 | W13 | 34 | LOWER_RX_BLANK | FPGA_TO_BOARD |
| 6 | V12 | 34 | LOWER_FAULT_N | ADC_OR_FAULT_TO_FPGA |
| 7 | V13 | 34 | RESERVED_00 | UNASSIGNED |
| 8 | U13 | 34 | RESERVED_01 | UNASSIGNED |
| 13 | Y14 | 34 | RESERVED_02 | UNASSIGNED |
| 14 | W14 | 34 | RESERVED_03 | UNASSIGNED |
| 15 | W15 | 34 | RESERVED_04 | UNASSIGNED |
| 16 | Y16 | 34 | RESERVED_05 | UNASSIGNED |
| 17 | V15 | 34 | RESERVED_06 | UNASSIGNED |
| 18 | Y17 | 34 | RESERVED_07 | UNASSIGNED |
| 19 | W16 | 34 | RESERVED_08 | UNASSIGNED |
| 20 | V16 | 34 | RESERVED_09 | UNASSIGNED |
