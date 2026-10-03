# Timing decision and bounded-stage result

Current analysis model: GPT-6.1 Sol High. Record date: 2026-10-03. Timing source: preserved Vivado 2025.2 runs from 2026-09-29.
User-approved decision P-20260927-001 and its body hash remain authoritative. Two substantive RTL rounds are complete. Result: CORE_TIMING_REVISE.

Keep the official 132 MHz core / 66 MHz shift profile. At 41.5 kHz and 256 phases, 32 lanes × four useful bits need 11 core cycles per refresh: minimum core 116.864 MHz, shift 58.432 MHz. Lowering the acoustic frequency or phase resolution to force PASS would violate the contract.

Fixed-route diagnostic results (no alternate-profile placement/routing performed):

| Core MHz | Shift MHz | WNS ns | TNS ns | Throughput |
|---|---|---|---|---|
|132|66|-4.515|-6007.936|PASS|
|123.75|61.875|-4.010|-2394.848|PASS|
|121|60.5|-3.827|-1691.737|PASS|
|118.8|59.4|-3.673|-1266.988|PASS|
|115.5|57.75|-3.433|-831.974|FAIL|
|99|49.5|-1.990|-30.337|FAIL|
|82.5|41.25|+0.030|0|FAIL|

Standalone MMCM primitive synthesis and DRC accepted these ratios from nominal 33 MHz under the engineering -1 target; ZPS7-1 warns that a PS7 block is required. This checks primitive legality, not real oscillator frequency, complete board clock configuration or electrical timing. Diagnostic clock re-evaluation is not a fresh implementation and cannot prove every alternate implementation would fail.

Round2 routed worst path is motion_queue/channel_reg[11]_replica/C to bus_wdata_reg[15]/D: 12.039 ns and eight levels. Code uses a 32-bit integer in active[channel*17+:17] although the legal range is 0..127. Failing path inventory: 7993 CE,418 D,1502 CLR,8 PRE, totaling9921. High fanout enables and internal asynchronous reset recovery remain measurable problems; narrowing the selector alone does not establish closure.

No unjustified timing exceptions, no relaxed production clock, no faster speed-grade assumption. External I/O delays and board clock pins are absent in the OOC build; internal clocked analysis is real, full-board timing remains unqualified. Raw critical warnings for deprecated report_timing -nets are retained; later script drops that reporting option, without altering RTL or constraints.

Do not start a third RTL optimization inside the exhausted two-round contract. P-20260929-001 contains the exact next-stage proposal and evidence. Keep Gate B unexecuted until Gate A and real PS/UART prerequisites pass.
