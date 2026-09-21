# SonoField-FPGA

128-channel ultrasonic phased-array project on Robei Zynq-7020, with nominal 10 mm transmitters,
12 mm radiating-center pitch and adjustable 90–115 mm face gap (100 mm nominal).

Current version **v2**, stage **SELF_CALIBRATION_SOFTWARE_AND_DIGITAL_SYSTEM**. v1 is frozen intact.
User explicitly approved v2 and this software/digital stage. The complete inherited baseline is retained.
Self-calibration and ADC acquisition have automated synthetic/RTL validation. Physical acquisition,
PCB manufacture and levitation remain unverified. No v3 or PCB implementation is started.

| Directory | Purpose |
|---|---|
| v2/ | Complete runnable current engineering version and fresh evidence |
| v1/ | Frozen prior source, docs, tests and evidence; no edits |
| shared/ | Current state, approval, freeze manifest, plans, blockers and acceptance |
| AI-chat-memory/ | External ChatGPT source SonoField-FPGA; BLOCKED |
| AI-interaction-memory/ | Actual visible Codex messages, user instructions and tool-flow checkpoints |
| AI-problem/ | Existing board/serializer/transducer questions; no fabricated decisions |
| BOM/ and Zynq7020/ | User originals retained locally; canonical imported BOM is inside v2 |

Start with [v2 operating guide](v2/docs/OPERATING_GUIDE.md), [migration](v2/docs/architecture/V1_TO_V2_MIGRATION.md),
[BOM review](v2/hardware/bom/BOM_LOCK.md), [state](shared/PROJECT_STATE.md) and [handoff](shared/HANDOFF.md).
Run commands from v2. No bitstream, measured calibration or levitation result is claimed.

Current architecture: [self-calibration](v2/docs/architecture/SELF_CALIBRATION.md).
Future board boundary: [hardware/software contract](v2/docs/hardware/PCB_SOFTWARE_INTERFACE.md).
