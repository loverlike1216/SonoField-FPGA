# Current v2 continuation — 2026-10-03

Current model: GPT-6.1 Sol High. Stage: TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE.

Completed: latest personalized-rule review; uploaded-file classification and hash audit; direct USB/JTAG identity; user-confirmed exact part and updated document precedence;64legal connector signals; proven-equivalent queue/scheduler timing changes; actual132MHz post-route internal timing PASS;115Python tests and complete four-run3696-frame motion/calibration/ADC regression; offline AXI/host-C; both-simulator queue/scheduler/throughput/independent-array-disable checks; vendor-synthesized clock candidate. Failures preserved.

Next: exact physical VCCO and PS clock/reset/UART/MIO/connector facts; verified XSA/BSP/target build and safe bare-board wrapper; real transport/map completion/GUI/ILA; complete electrical/disable budgets and then PCB interface freeze. No new version. Follow MISSING_PHYSICAL_FACTS.md and PS_PLATFORM_AND_TRANSPORT_REMAINING.md. Do not repeat core optimization without a newly evidenced failure.

Do Not Change: frozenv1/history/model provenance,packet/register interface,128channels/8bit,requested/calibration split,atomics,upper/lower mapping,38.5..41.5kHz and current radiating-center geometry. No failing-design or guessed-platform deployment.132MHz is a routed internal design target; final board clock and external constraints require reviewed integration. Do not waive DRC/warnings or declare PCB ready from OOC PASS.

Current full result: v2/evidence/pre_pcb_board_ready/RESULT.md. Current source commit and sync evidence follow the checkpoint. Hardware status remains identification only.

Validated engineering source: 9936a737c45bf61f1908863a94f6374c6b5c828c. Checkpoint CP-20261003-002. Fresh sparse checkout115tests and212frozenfile coverage PASS on same machine using existingpinnedvenv. Later checkpoint/documentation commits preserve these source facts.

## DDR detection continuation — 2026-10-04

Model: GPT-6.1 Sol High. Active v2 and existing Stage unchanged. Current read-only native Vivado2025.2 scan confirms XC7Z020 IDCODE0x23727093; Micron public decoder identifies D9PSK as MT41K128M16JT-125 IT:K. Photo shows two2Gb x16 devices, but512MiB/32bit remain CANDIDATE. XSDB/AP0 reads DDRC_CTRL0x00000200 andCTRL_REG1 0x0000003E, both documented reset values; controller reset not released, so32bit default field is not board topology proof. No CPU halt/reset/init,DDR memory access,download,COM,GPIO orPCB operation. Original Vivado GUI preserved. Report: parameter_detection/20261004_ddr/RESULT.md; candidate: v2/config/ddr_candidate.json. Existing core115tests/132MHz timing retain their2026-10-03 source/date; not rerun today.

Next: obtain actual board-matched PS configuration/topology under parameter_detection/inputs; review before initialization. Existing physical board integration blockers remain. Stop further hardware operation at this inspection boundary.
