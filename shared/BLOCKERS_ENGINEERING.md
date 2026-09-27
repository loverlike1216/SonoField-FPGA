# Engineering blockers — v2

Current stage: INTERACTIVE_LEVITATION_AND_TRAJECTORY_CONTROL.
Canonical machine state: PROJECT_STATE.json and ENGINEERING_STATE.json.
Owner: Codex. No hardware acceptance is granted by this file.

| Gate | Engineering fact | Required next evidence |
|---|---|---|
| B01/B03 | Exact FPGA package/ordering code, connector assignment and VCCO remain unverified | Authoritative board documents and physical confirmation |
| B04 | Serializer/driver physical setup/hold and independent watchdog remain unresolved | Timing budget, circuit review and measured waveforms |
| B05/B06 | No physical levitation/batch qualification | Characterized 10 mm transmitters, conservative voltage/current/temperature records and measured particles |
| B07 | Real receive phase reference and analog acquisition timing unverified | Calibrated cross-bank reference and hardware acquisition traces |
| PS_TRANSPORT | Motion execution is a host reference model with RTL simulation | Real PS firmware, verified bus/transport and hardware interlock |
| EXTERNAL_REVIEW | Codex self-check is not independent acceptance | Chat/user review of the final commit and engineering evidence |

These gates block physical deployment, not the authorized digital motion stage.
No new physical pin or PCB requirement has been introduced by the motion wrapper.

DOCUMENTATION_UPDATE_REQUIRED: general shared/CURRENT_PLAN.md, HANDOFF.md,
PROJECT_STATE.md, DECISIONS.md and ACCEPTANCE.md still describe earlier stages.
Work is OFF. The current user instruction explicitly authorizes the six motion
stage documents; it does not imply that Work ran or that Chat approved a new decision.
External ChatGPT history access remains BLOCKED; observable Codex records are PARTIAL.
