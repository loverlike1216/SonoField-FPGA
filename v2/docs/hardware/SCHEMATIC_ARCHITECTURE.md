# Schematic architecture — project v2, schematic V1

Native project: PCB/V1/project/SonoField-FPGA-v2-Schematic-V1-SingleSheet.eprj2.
One page contains83named modules; native vector PDF/SVG are beside the project.
Status is tracked in shared/PROJECT_STATE.json; this architecture is not a completion claim.

| Block | Allocation | Interface / boundary |
|---|---|---|
| FPGA_CORE_INTERFACE | 1 | Logical RTL names; physical connector pins and VCCO blocked by B01/B03 |
| Output translation | 6 AXC8T245 | Two banks, 16 data lines plus clock/latch/disable per bank |
| Clock distribution | 2 LVC244 | Four branches each for SRCLK and RCLK per bank; B04 open |
| Serializer | 32 LVC595 | Four used outputs per lane, QA..QD; QE..QH and cascade output unused |
| Transmit | 64 TC4427, 128 TX | Two 8x8 arrays; one four-channel schematic cell per lane |
| Receive analog | 8 RX, 4 OPA4192 | Two amplification stages/channel; separate 2.5 V reference per bank |
| Blanking | 2 TMUX1574 | Four paths/bank, downstream of amplifiers; does not prevent AFE overload |
| ADC | 1 AD7606B | Eight simultaneous inputs, four DOUT paths, 5 V AVCC, 3.3 V VDRIVE |
| ADC translation | 2 AXC8T245 | Respect direction groups and unknown FPGA-side VCCA |
| Power | Upper/lower/ADC modules | eFuse, current/temperature sensing, buck rails, analog LDO/filter |
| Environment | SHT45 | Ambient sensor separated from self-heating power electronics |

The 32-lane output state is FPGA-owned. GPIO/software bit banging is not the timing
source. Host requested phase and hardware calibration remain separate, with atomic commit.
TX schematics use short electrical nets U_TXnn_IN/DRV/FACE and L_TXnn_IN/DRV/FACE;
physical component IDs remain UPPER_TX_00..63 and LOWER_TX_00..63.

Radiating-center pitch 12 mm, nominal diameter 10 mm, face-to-face gap 100 mm,
adjustable 90..115 mm. Origin is the radiating-center geometric midpoint. No footprint
or PCB standoff dimensions are frozen by these coordinates.

No manufacturing release until library/BOM, netlist, ERC, power, AFE, timing,
FPGA connector mapping and independent safety reviews close. See SCHEMATIC_OPEN_ITEMS.md.
