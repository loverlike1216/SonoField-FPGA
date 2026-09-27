# Clock engineering review

Input precedence is N18 / 33 MHz from supplied hardware.const; measured frequency and bank VCCO remain unknown. A 33.333 MHz claim elsewhere is retained as a conflict, not silently substituted.

The diagnostic MMCME2_BASE uses M=24, D=1 and output divides 6/12: VCO=792 MHz, outputs=132/66 MHz. AMD DS187 Table 72 gives VCO minimum 600 MHz and maxima 1200/1440/1600 MHz for -1/-2/-3, so this frequency plan fits all candidates. CLKIN=33 MHz is within the documented 10–800 MHz range. This arithmetic and synthesized clock reports do not identify the board speed grade.

STA input jitter=100 ps is an explicit analysis assumption, not a measurement. REF_JITTER1=0.010 is a separate simulation-only fractional setting (about 303 ps at 33 MHz); neither establishes oscillator quality. Candidate resets assert on reset/LOCKED loss and release after three destination-clock edges. Startup, lock loss and board reset have not been exercised physically.

Existing serializer logic stays entirely at 132 MHz and produces 66 MHz serial toggles; do not clock that same logic from clk66 or it halves throughput. ADC serial clock is 132/4=33 MHz under current parameters. ADC input/output delays, converter clock relationship and serializer setup/hold require board constraints and measurement (B03/B04/B07).

Core CDC report says all paths safely timed only because the OOC wrapper is a single clock domain. It does not verify a future PS FCLK crossing. Put AXI and native logic on the same reviewed clock or add a properly verified AXI clock converter; synchronize reset release independently. No such physical PS block design is delivered here.

All three clock-only candidates synthesized. Full core OOC setup WNS is -8.128/-4.995/-3.609 ns; timing is FAIL. Reports have 2324 input and 285 output ports without delays and missing OOC HD.CLK_SRC skew information. No external timing or placement/routing claim is possible. Clock-only DRC reports missing PS7 (ZPS7-1) because this is a diagnostic fragment.

Sources: [AMD UG865](https://docs.amd.com/v/u/en-US/ug865-Zynq-7000-Pkg-Pinout), [AMD DS187](https://docs.amd.com/v/u/en-US/ds187-XC7Z010-XC7Z020-Data-Sheet), [AMD UG472](https://www.amd.com/content/dam/xilinx/support/documents/user_guides/ug472_7Series_Clocking.pdf). Actual reports: candidate_synthesis/*/{clocks,clock_timing,timing,cdc}.rpt.
