# SonoField-FPGA v2 / pre-PCB interface review

Current model: GPT-6.1 Sol High. Status: CANDIDATE / NOT ELECTRICALLY FROZEN.

TX: one core cycle (~7.576ns at132MHz) separates data launch from shift-clock rising; one cycle separates final shift rising from latch rising. Budget must include FPGA tCO(min/max), package/pin skew, board routing, level translator and clock-only buffer delays,595 SER setup/hold and SRCLK-to-RCLK setup, loading, jitter and PVT. Clock-only buffering can improve setup while worsening hold; never use typical delays to certify either.

Receiver setup margin = available launch/capture interval + clock_path_min - data_path_max - required_setup - uncertainty. Hold margin = data_change_min - clock_capture_max - required_hold - uncertainty, using the relevant NEXT data-change edge. Values not measured or constrained remain UNKNOWN, not zero. No input/output delays, IOSTANDARD or unconstrained-path exclusions have been fabricated.

AD7606B: Rev B table5 specifies60MHz maximum SCLK at VDRIVE>=2.7V (40MHz below2.7V), DOUT access delay up to15ns (25ns below2.7V). Existing RTL SCLK=core/4≈33MHz and samples old DOUT at a subsequent rising launch; the nominal30.303ns cycle must cover maximum ADC output delay plus outgoing/incoming path delays and FPGA input setup. This frequency check alone cannot qualify capture timing.

Sources: [AD7606B Rev B](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606b.pdf), [SN74LVC595A](https://www.ti.com/lit/ds/symlink/sn74lvc595a.pdf), [SN74LVC244A](https://www.ti.com/product/SN74LVC244A/part-details/SN74LVC244APWR). Receiver voltage and exact routed loads remain unknown. No final positive margin asserted.
