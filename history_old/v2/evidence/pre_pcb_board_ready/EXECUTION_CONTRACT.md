# Execution contract — current v2

Current model: GPT-6.1 Sol High. Direct input: AI-interaction-memory/codex/instructions/v2_final_pre_pcb_board_integration.md. Starting HEAD: bd9e79f622ee58ea970870071702eb24596cd753. Stage: TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE.

Goal: verified single-board control and safe pre-PCB interface freeze, subject to real board facts.
Scope: read-only USB/JTAG/package detection; classify uploaded references; bounded queue/control timing implementation; simulator/original equivalence; full regression; source/throughput/clock analysis; PS/transport preflight; current state/checkpoint/Git synchronization; visible result page.
Non-goals: external PCB operation, PCB files, fabricated VCCO/MIO, driver/EEPROM/boot changes, guessed preset, physical acoustic claims.
Architecture: existing128channel/8bit coherent phase engine with separate requested/calibration and atomic commit, existing packet/AXI bus, one central8RX AD7606B.
Allowed changes: confirmed identity and current sourced connector candidates, proven-equivalent queue/serializer implementation, stage records. Existing frozenv1, prior evidence and native PCB remain unchanged.
Invariants: same cycle-visible queue behavior, channel order, register/packet protocol and fault-safe disable. Core132MHz remains a design target, not an asserted final board clock.
Validation: original/new cycle equality at depths2/4/5, both Icarus and XSim, serializer11-cycle proof, full existing motion/calibration/AXI gates and routed timing. Do not ignore CLR/PRE recovery or external timing omissions.
Rollback: ordinary Git revert of this stage; new failed logs remain evidence. No deployment unless timing and all PS/UART facts are verified. Stop unsafe dependent work when exact physical prerequisites are unavailable, retaining a precise acquisition list.
