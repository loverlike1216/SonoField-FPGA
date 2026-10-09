# SonoField-FPGA

PROJECT_ID **SONOFIELD_FPGA** · active **v5** · **ALINX AX7020 / Zynq-7020** · Vivado2025.2 · main. Same repository and history; v5 was explicitly authorized by the user on2026-10-08. No v4 was created.

Start here: [v5开发入口](v5/README.md) · [完整运行指南](指南.md) · [当前状态](shared/PROJECT_STATE.json) · [恢复检查点](shared/CONTEXT_CHECKPOINT.md) · [真实基线结果](v5/evidence/BASELINE_VALIDATION.md).

128-channel40kHz acoustic field with8bit programmable phase, separate per-channel calibration, atomic maps, acquisition/calibration, trajectory and PS/PL protocol infrastructure. Geometry: opposed8×8+8×8,10mm candidate emitters,12mm radiating-center pitch, nominal100mm face-to-face gap adjustable90–115mm, origin at geometric center. 50mg EPS remains a staged final physical target, not a demonstrated result.

2026-10-09: actual AX7020 PCB AX701020.3.0, XC7Z020 JTAG and CLG400 photo confirmed. The existing PL/PS/SD image was preserved. Full 115-test/four-run digital baseline passes again. Full FPGA grade, DDR capacity, revision-matched PS platform, VCCO, actual UART/PS-PL and acoustic operation remain unverified; whole platform REVISE, electrical/manufacturing HOLD.

Latest [board/BOM results](v5/evidence/board_bringup/20261009/RESULT.md) · [separate BOM working copy](v5/hardware/bom/working/2026-10-09/) · [three-board preparation](v5/hardware/integration_candidates/20261009/SCHEMATIC_PREPARATION.md). No core RTL or formal ADC selection changed. Native v5 schematic and ERC have not run.

Root shared/ and AI records hold cross-version governance/provenance; v5/ is the sole active implementation; archive/ is frozen indexed history. v1/v2 and referenced old hardware/PCB/evidence remain at original locations to preserve history, excluded from default v5 builds/search. Paused v3 is incomplete local history and is not claimed published/validated; no v4 exists. Original private/local assets and generated caches are intentionally not mirrored to public GitHub.

Audit/reuse/archive manifests: shared/organization/ and archive/manifests/. External ChatGPT source SonoField-FPGA is BLOCKED; observable Codex transcript PARTIAL, never invented history. All future Windows commands default to PowerShell7.
