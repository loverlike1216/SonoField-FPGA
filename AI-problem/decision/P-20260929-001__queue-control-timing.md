---
problem_id: P-20260929-001
project_id: SONOFIELD_FPGA
active_version: v2
current_stage: TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE
status: ACTIONABLE
current_model: GPT-6.1 Sol High
decision_source: USER
problem_hash: a84242c69d945dc5989c8b708623657e61fe8eeb4af0782f4474531cfff9972b
problem_hash_scheme: SHA256 LF normalized newline + stripped body + newline
source: AI-interaction-memory/codex/instructions/v2_final_pre_pcb_board_integration.md
---

# Direct user authorization

The actual supplied formal instruction explicitly authorizes the next bounded P-20260929-001 queue/control timing work in CURRENT v2. This is a user decision, not an imported ChatGPT decision. Preserve the original Problem and earlier exhausted two-round reports.

# Chosen direction

First range-safe queue/serializer indices and static 8:1/16:1 selection; then, only with new routed evidence, a second control-cone change. Compare all observable outputs cycle-by-cycle against preserved original RTL, including DEPTH2/4/5 and fault cases. Run complete digital regression and Vivado2025.2 post-route timing. No false or multicycle path waivers.

# New facts and precedence

XC7Z020-1CLG400C / xc7z020clg400-1 is USER_CONFIRMED_PHYSICAL_FACT. Fresh JTAG confirms XC7Z020 family only. Excel/image connector mapping supersedes legacy const conflicts. N18/33.333MHz is an approved document fallback, not a measurement. Keep board VCCO, PS clock/reset/UART route unassigned until supported.

# Constraints / validation

128 channels,8-bit requested+calibration,atomic commit,register/packet compatibility,38.5..41.5kHz and common timing preserved. Final clock requires both routed timing and serializer throughput. J3/J4 each16data lanes; J5/J6 candidate control budgets respect one central8RX ADC. Separate array-disable hardware integration must be validated before freeze.

# User approval boundary

Authorization is already supplied for this stage. Bare-board temporary programming remains gated by actual timing PASS plus verified PS/UART/clock prerequisites. No driver replacement, boot changes, PCB edits or external output drive. PRE_PCB_BOARD_READY is NO until every formal readiness requirement is evidenced.
