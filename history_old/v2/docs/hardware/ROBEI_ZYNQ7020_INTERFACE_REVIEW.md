# Robei Zynq-7020 interface review

Authoritative input: user-supplied root Zynq7020, with constrain-file precedence
explicitly selected by the user. Documented clock is N18 / 33 MHz. This does not
identify the FPGA package/speed grade or establish the physical oscillator tolerance.

Family Zynq-7020 is known; exact ordering code remains B01. Connector ambiguities
inside .const (duplicate/missing entries) and bank VCCO remain B03. A connector's
5 V supply label is not evidence of 5 V tolerant FPGA IO.

FPGA_CORE_INTERFACE must list logical RTL signals without assigning guessed balls
or connector pins. AXC VCCA must follow measured/documented FPGA bank VCCO.
AXC8T245 has two direction control groups; pin2 DIR1 and pin11 DIR2 both matter.
Its /OE must default disabled while either side is unpowered or unconfigured.

No new XDC, guessed part selection or bitstream is authorized by the schematic stage.
132 MHz core / 66 MHz serializer timing requires verified board clock generation,
device timing, level translation and external skew analysis.
