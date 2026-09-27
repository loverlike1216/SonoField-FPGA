# Engineering blockers — v2

Current stage: BOARD_ONLY_IDENTIFICATION_AND_TRANSPORT_PREFLIGHT.
Canonical machine state: PROJECT_STATE.json and ENGINEERING_STATE.json.
Owner: Codex. No hardware acceptance is granted by this file.

| Gate | Engineering fact | Required next evidence |
|---|---|---|
| B01 | PARTIALLY RESOLVED: Vivado JTAG twice identifies xc7z020 / 0x23727093. Exact package/speed/ordering code remains unknown | Legible chip marking or revision-matched manufacturer documentation |
| B03 | OPEN: VCCO, IO standards, connector errors and PS UART wiring remain unverified | Electrical documentation/physical confirmation; JTAG does not prove these |
| B04 | Serializer/driver physical setup/hold and independent watchdog remain unresolved | Timing budget, circuit review and measured waveforms |
| B05/B06 | No physical levitation/batch qualification | Characterized 10 mm transmitters, conservative voltage/current/temperature records and measured particles |
| B07 | Real receive phase reference and analog acquisition timing unverified | Calibrated cross-bank reference and hardware acquisition traces |
| PS_TRANSPORT | Motion execution is a host reference model with RTL simulation | Real PS firmware, verified bus/transport and hardware interlock |
| EXTERNAL_REVIEW | Codex self-check is not independent acceptance | Chat/user review of the final commit and engineering evidence |

These gates block physical deployment, not the completed board-only identification. Evidence: v2/evidence/board_bringup/RESULT.md. FT2232H A JTAG works directly in Vivado 2025.2; B COM4 exists but has not been opened. No driver change or download performed.
No new physical pin or PCB requirement has been introduced by the motion wrapper.

DOCUMENTATION_UPDATE_REQUIRED: general shared/CURRENT_PLAN.md, HANDOFF.md,
PROJECT_STATE.md, DECISIONS.md and ACCEPTANCE.md still describe earlier stages.
Work is OFF. The current user instruction explicitly authorizes the six motion
stage documents; it does not imply that Work ran or that Chat approved a new decision.
External ChatGPT history access remains BLOCKED; observable Codex records are PARTIAL.
