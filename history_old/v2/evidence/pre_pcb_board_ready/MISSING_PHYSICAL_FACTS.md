# Exact missing facts after automatic inspection

Current model: GPT-6.1 Sol High. No physical step below has been performed.

| Fact | Why it blocks | Sources searched | Required evidence/action |
|---|---|---|---|
| Bank34/35 VCCO | IO standards and translator voltages cannot be frozen | All Zynq7020 files, current Excel/image, package database, previous board audit | Revision-matched schematic naming the rails, or identified test-point measurements as specified in MANUAL_VCCO_MEASUREMENT_REQUIRED.md |
| FT2232-B TX/RX to PS UART instance/MIO | COM4 is enumerated but no verified PS path exists | USB descriptors, board pin tables/const/images, firmware platform profile | Manufacturer UART schematic, or unpowered continuity test of identified FTDI TX/RX to documented PS MIO pads; record instance and MIO pair |
| PS input reference clock, reset source and board preset | Safe PS initialization/XSA/BSP cannot be inferred from PL N18 | Board sources, installed Vivado/Vitis, generic PS7 templates | Correct board preset or schematic/clock values; generic Zed/zc702 ps7_init is not a Robei preset |
| Connector pin1 orientation and real continuity | Excel resolves documentation but actual PCB routing is not measured | New Excel/image and legal package pin query | Board-revision matched connector drawing or unpowered continuity verification of intended signal pins |
| TX/ADC link delay and loading | Off-chip setup/hold cannot be accepted from OOC timing | Existing BOM/native schematic and official part datasheets | Approved component/voltage/load/cable budget plus min/max timing constraints; later scope evidence on actual prototype |

N18 nominal33.333MHz is an explicitly approved fallback, so physical oscillator measurement is not reintroduced as a blocking requirement. No need to reread full chip ordering code: XC7Z020-1CLG400C is already USER_CONFIRMED_PHYSICAL_FACT.

Separate development prerequisites: install/locate a valid ARM Cortex-A9 baremetal target compiler/BSP; construct verified PS/AXI clock/reset platform; implement and test separate array-disable integration; obtain full-board integrated post-route timing closure (internalOOC is now PASS) and then run the real transport tests. These are engineering work, not claimed missing physical measurements.
