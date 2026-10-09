# SonoField-FPGA v2 / pre-PCB interface review

Current model: GPT-6.1 Sol High. Status: CANDIDATE / NOT ELECTRICALLY FROZEN.

Measure actual VCCO for bank34 and bank35 on this board revision against ground, using a manufacturer-identified rail/test point. Do not probe arbitrary package balls or infer VCCO from connector5V. Record board revision, point identifier, voltage, instrument, photo and date. J3/J6/N18 use bank34; J4 uses bank35; J5 spans both. Compare proposed translator VCCA and ADC VDRIVE to measured bank voltages before choosing LVCMOS18/25/33 or emitting XDC. Disable outputs and leave external PCB disconnected until the match is verified. A schematic with identified bank supply nets may replace exploratory measurement for documenting the intended voltage, but does not replace electrical qualification.
