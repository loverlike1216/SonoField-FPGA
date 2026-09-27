# Engineering blockers — v2

Stage: BOARD_TRANSPORT_AND_PS_PL_INTEGRATION_PREFLIGHT. Owner: Codex; independent review pending.

| Gate | Current engineering fact | Evidence required |
|---|---|---|
| B01 | PARTIALLY_RESOLVED_STILL_BLOCKING: JTAG confirms xc7z020; user photo confirms CLG400. Speed, temperature and full ordering code UNKNOWN | Independent speed/temperature/ordering evidence; do not infer ABX22 |
| B03 | OPEN: package audit complete; routing/VCCO remain unverified. CEC=J5 is PS DDR, not PL. Connector numbering, J4 pin1/duplicate pin6, V16/Y16 conflicts retained | Revision-matched schematic/continuity, VCCO and clock evidence, UART MIO routing |
| B04 | OPEN: 66 MHz serializer external setup/hold, independent watchdog and power qualification unverified | Physical timing budget and measured waveforms; no PCB freeze |
| CORE_TIMING | All three candidates synthesize; 132 MHz OOC WNS -8.128/-4.995/-3.609 ns | P-20260927-001 decision and timing revalidation; no guessed-target deployment |
| PS_TRANSPORT | PC/C and AXI/native segments tested offline; COM4 route and real PS readback unverified | Exact target, PS platform/XSA/BSP, safe smoke top, UART route, real PING/PONG and PL STATUS |
| B05/B06 | No physical levitation/batch qualification | Characterized 10 mm emitters and measured particles |
| B07 | Real receive reference and analog timing unverified | Calibrated reference and hardware acquisition traces |
| EXTERNAL_REVIEW | Codex checkpoint is not Chat acceptance | Independent review of final commit/evidence |

Evidence: v2/evidence/board_transport/. Prior identification evidence remains in board_bringup/.
No port opened, no driver/EEPROM/boot change, no program download, no unknown GPIO, no external PCB operation.

DOCUMENTATION_UPDATE_REQUIRED: general README, v2/README, CURRENT_PLAN, HANDOFF, PROJECT_STATE.md, DECISIONS and ACCEPTANCE remain historical. Work is OFF; no narrative or memory update is attributed to Work. Task-specific technical evidence is explicitly authorized by current instruction sections22/26. External Chat history remains BLOCKED; observable interaction memory remains PARTIAL at its existing cutoff.
