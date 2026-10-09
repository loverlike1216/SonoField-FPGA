> v5 inherited design/reference documentation. Original source is recorded in config/inheritance_manifest.json. Technical behavior/requirements are retained; historical numeric results are reference inputs, not v5 validation or AX7020 electrical qualification. Current board facts are config/board_facts.json; baseline results are evidence/BASELINE_VALIDATION.md.

# SonoField-FPGA v5 / pre-PCB interface review

Current model: GPT-6.1 Sol High. Status: CANDIDATE / NOT ELECTRICALLY FROZEN.

Actual RTL lifecycle: accepted start at cycle0; four high/low shift pairs at cycles1..8; latch high at9; completion and busy release at10; next accepted start at11. Icarus and Vivado XSim each executed100 consecutive starts spaced11 cycles, four shift edges per frame and done offset10, with no overrun. Evidence: pre_pcb_board_ready/throughput/0..4.log and cross_simulator_checks.json.

Maximum phase refresh demand =41500×256=10,624,000 updates/s. Minimum core frequency =11×10,624,000=116,864,000Hz. At nominal132MHz the frame capacity is12,000,000/s; slack to demanded capacity is1,376,000/s (12.95% of demand). At33.333MHz input and a3.96 ratio, candidate core131,998,680Hz has capacity11,999,880/s and still meets throughput. Final board clock remains NOT FROZEN pending routed timing and verified clock integration. Throughput does not validate off-chip setup/hold.

ADC clock is independently derived: adc_serial uses a modulo-four divider, therefore nominal33MHz at132MHz core, not66MHz. TX shift clock nominal66MHz only during serialization.
