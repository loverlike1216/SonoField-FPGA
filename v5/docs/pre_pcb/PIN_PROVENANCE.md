# Pin and platform provenance

Canonical candidate map: `hardware/prepcb/AX7020_REV3_PINMAP.csv` and machine
contract `config/SIGNAL_CONTRACT.json`.80 physical contacts,68 documented GPIO,
67 assigned logical signals and1 reserved GPIO. Four formerly spare pins on
J11.32–35 provide the two additional I2C pairs; original63 candidate assignments
are retained. All rows are NON_DEPLOYABLE. Power pins are not GPIO.

Public ALINX manual plus Vivado2025.2 package database establish candidate
contact/package/bank relationships only. Local historical read-only board ID
AX701020.3.0, XC7Z020 JTAG and CLG400 does not verify complete industrial
grade, bank VCCO, routing revision or schematic identity. User describes−2/I;
Vivado's available legal candidate is xc7z020clg400-2, not an invented part name.
No production XDC was activated. `ax7020_candidate.xdc` intentionally errors
when loaded; commented package assignments are review data only.

The full PS7 candidate connects GP0 AXI to original core, BRAM task mailbox,
control/status GPIO and three AXI IIC blocks; five IRQ sources are connected,
FCLK132MHz and reset wiring are explicit. PS UART1 MIO48–49 is a public
candidate, not verified USB-UART1 ownership. DDR is disabled; no2023.1 DDR or
board preset is imported. The build emits xpr, logical xsa and BD recreation Tcl.
An XSA without an implemented bitstream and matchedBSP is NON_DEPLOYABLE.

`platform_connected4` performs PL-core OOC route on documented−2 candidate,
not routed fullPS7 top/board. WNS+.068ns, WHS+.070ns; internal unclocked and
unconstrained endpoints0.161 input and147 output external delays absent by
design rather than fabricated.22 DRC warnings include20 reported inherited
RAMB36 asynchronous-control checks, rule-limit warning, and PS7-required warning
for OOC. CDC explicitly skips unconstrained ports. Clock-source skew is not
board-qualified. **BOARD_TIMING_HOLD**; no bitstream or hardware validation.

Actual Vitis command reports2025.2 build6295257 with two missing-path messages;
installed UART/IIC driver headers are visible. A matched standalone Cortex-A9
compiler/BSP/linker/OCM and Rev3 startup target have not been established.
Portable C host tests do not qualify them. ARM_TARGET_BUILD_BLOCKED remains.

Sources and exact input hashes: `SOURCES.json`. Independent checks of actual
pins, VCCO, grounds, source capacity, cable delays, current and device ratings
are required before changing any deployment status.
