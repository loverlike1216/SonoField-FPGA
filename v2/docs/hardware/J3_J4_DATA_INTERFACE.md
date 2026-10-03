# SonoField-FPGA v2 / pre-PCB interface review

Current model: GPT-6.1 Sol High. Status: CANDIDATE / NOT ELECTRICALLY FROZEN.

J3 carries upper TX00..63 via serializer lanes00..15; J4 carries lower TX00..63 via lanes16..31. Each lane sends local channel3,2,1,0. This is the logical shift order; the physical 595 QA/QB/QC/QD wiring still requires netlist verification. A four-used-output 595 uses eight hardware stages; no claim of final QA mapping is made here. Both arrays share deterministic timing, with separate board enables required at integration.

Pins9/12 are AUX5V and unused for array/AFE/ADC power. Pins10/11 are ground. FPGA package legality is verified; actual bank34/35 VCCO, connector orientation/continuity and electrical timing are not.

| Connector pin | Package ball | Bank | Signal | Direction |
|---|---|---|---|---|
| 1 | U14 | 34 | UPPER_TX_DATA_00 | FPGA_TO_DRIVER |
| 2 | U15 | 34 | UPPER_TX_DATA_01 | FPGA_TO_DRIVER |
| 3 | T14 | 34 | UPPER_TX_DATA_02 | FPGA_TO_DRIVER |
| 4 | T15 | 34 | UPPER_TX_DATA_03 | FPGA_TO_DRIVER |
| 5 | T16 | 34 | UPPER_TX_DATA_04 | FPGA_TO_DRIVER |
| 6 | U17 | 34 | UPPER_TX_DATA_05 | FPGA_TO_DRIVER |
| 7 | V17 | 34 | UPPER_TX_DATA_06 | FPGA_TO_DRIVER |
| 8 | V18 | 34 | UPPER_TX_DATA_07 | FPGA_TO_DRIVER |
| 13 | U18 | 34 | UPPER_TX_DATA_08 | FPGA_TO_DRIVER |
| 14 | U19 | 34 | UPPER_TX_DATA_09 | FPGA_TO_DRIVER |
| 15 | T17 | 34 | UPPER_TX_DATA_10 | FPGA_TO_DRIVER |
| 16 | R18 | 34 | UPPER_TX_DATA_11 | FPGA_TO_DRIVER |
| 17 | N17 | 34 | UPPER_TX_DATA_12 | FPGA_TO_DRIVER |
| 18 | P18 | 34 | UPPER_TX_DATA_13 | FPGA_TO_DRIVER |
| 19 | T20 | 34 | UPPER_TX_DATA_14 | FPGA_TO_DRIVER |
| 20 | U20 | 34 | UPPER_TX_DATA_15 | FPGA_TO_DRIVER |

| Connector pin | Package ball | Bank | Signal | Direction |
|---|---|---|---|---|
| 1 | F19 | 35 | LOWER_TX_DATA_00 | FPGA_TO_DRIVER |
| 2 | F20 | 35 | LOWER_TX_DATA_01 | FPGA_TO_DRIVER |
| 3 | D19 | 35 | LOWER_TX_DATA_02 | FPGA_TO_DRIVER |
| 4 | D20 | 35 | LOWER_TX_DATA_03 | FPGA_TO_DRIVER |
| 5 | C20 | 35 | LOWER_TX_DATA_04 | FPGA_TO_DRIVER |
| 6 | B20 | 35 | LOWER_TX_DATA_05 | FPGA_TO_DRIVER |
| 7 | B19 | 35 | LOWER_TX_DATA_06 | FPGA_TO_DRIVER |
| 8 | A20 | 35 | LOWER_TX_DATA_07 | FPGA_TO_DRIVER |
| 13 | E18 | 35 | LOWER_TX_DATA_08 | FPGA_TO_DRIVER |
| 14 | E19 | 35 | LOWER_TX_DATA_09 | FPGA_TO_DRIVER |
| 15 | E17 | 35 | LOWER_TX_DATA_10 | FPGA_TO_DRIVER |
| 16 | D18 | 35 | LOWER_TX_DATA_11 | FPGA_TO_DRIVER |
| 17 | F16 | 35 | LOWER_TX_DATA_12 | FPGA_TO_DRIVER |
| 18 | F17 | 35 | LOWER_TX_DATA_13 | FPGA_TO_DRIVER |
| 19 | H15 | 35 | LOWER_TX_DATA_14 | FPGA_TO_DRIVER |
| 20 | G15 | 35 | LOWER_TX_DATA_15 | FPGA_TO_DRIVER |
