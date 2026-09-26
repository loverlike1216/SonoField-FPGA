# SonoField-FPGA schematic V1 review — 2026-09-26

PROJECT_ID: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
workspace_path: E:\Codex_project\AMD-SonoField-FPGA
current_branch: main
current_version: v2 (v1 frozen)
current_stage: SCHEMATIC_DESIGN_JLCEDA_PRO
schematic_revision: V1
chat_source_name: SonoField-FPGA (external history BLOCKED)

## IMPLEMENTED
One editable native schematic,83named circuit modules,128TX /8RX,1561components and381annotations. Solid blue partitions group upper/lower TX, digital serialization and translation, ADC, RX/AFE, domain power/monitoring, core logical interface and environment sensing. All TX channels are expanded. Horizontal network labels, right-aligned long ADC/translator inputs and vector PDF/SVG support zoomed reading.

Delivered under PCB/V1/project: SingleSheet.eprj2 (native project), SingleSheet.epro2 (portable import), SonoField-SingleSheet.pdf, SonoField-SingleSheet.svg and README. The PDF contains1page,16956vector drawing objects and0embedded raster images; its large original page is intended for zooming, not A4 printing.

## VALIDATED / REAL TOOL EVIDENCE
- EasyEDA professional3.2.149 with Run_API_Gateway1.0.6 and easyeda-api skill1.1.36; actual GUI import and native save/close/reopen.
- single_connectivity_audit.json:1561components,3992pins match intended manifests, zero discrepancies. Hash unchanged after label adjustments.
- channel_mapping_audit.json:1338independent checks of geometry-to-TX,32lanes/four595outputs, driver pins,8RX-to-ADC paths and return links;128TX/8RX PASS.212frozen v1 files unchanged.
- Native strict ERC:0fatal,0error,45warning records.43supplier-template mismatch groups and2single-pin logical interface endpoints. Raw report and disposition retained; warnings not suppressed.
- Native PDF/SVG export and visual review of overview,TX,ADC,translation,RX/AFE and power. Corrected initial incompatible TEXT fields, huge API-font-unit error and label collisions before final export.
- PowerShell7.6.5 used; global preference saved in the user-authorized memory update note, project preference in AGENTS.md.
- Commands: audit_tx.py with32TX modules+system/power manifests; audit_mapping.py; native DRC/check/getNetlistFile/getExportDocumentFile; sync_codex.py source export and --check. No RTL behavior changed, so prior software/simulator results remain historical evidence rather than rerun claims.
Evidence root: PCB/V1/log/review. Earlier bounded capture evidence: capture_history.zip. Original modular interchange preserved for reproducibility.

## NOT VALIDATED / BLOCKING
Electrical release is blocked by exact core-board part/connector/VCCO facts; serializer worst-case hold closure; independent clock-loss watchdog and power qualification; final MPN/package/rating choices; physical analog settling/overload recovery and actual transducer batch qualification. HARDWARE_ENABLE/RST_N remain logical endpoints, not implemented external qualification circuits.
P-20260925-001 requests a sourced decision on timing/safety. No external ChatGPT output or decision was invented. Native ERC alone cannot close these gates. No PCB, routing, Gerber, target FPGA synthesis, bitstream, physical measurement or levitation was performed in this stage.

## RISKS / BOARD FACTS FOUND
User-selected constrain files establish documented N18/33MHz precedence. Exact ordering code/package, bank VCCO and duplicate/missing connector mappings remain unresolved. TP_CORE labels do not assign physical pins.
132MHz core/66MHz shift and clock-only LVC244 delay leave only0.176ns ideal hold margin at85C and negative1.124ns at125C before other skew. This is a worst-case analysis gap, not a measured failure. Clock-loss/output-disable and PSU startup need an independent design.
ADP7118 uses its actual6-lead+EP variant, SHT45 central pad is unconnected, and TPS259470L AUXOFF is not a complete power-good supervisor. Candidate UV/OV/current values and passive templates remain subject to tolerance/load review. RX blanking follows the amplifier and cannot protect it from overload.

## TCT40 ASSUMPTIONS
User-supplied10mm TCT40-10T/R1 baseline; no old16mm voltage/capacitance values transferred. Nominal12mm center pitch and100mm radiating-face separation, adjustable90–115mm, origin at geometric center. Manufacturer provenance, active aperture, polarity, resonance, continuous drive and temperature require purchased-batch measurement. No force or50mg levitation guarantee.

## NEXT PHYSICAL HARDWARE REQUIRED / NEXT STAGE
First obtain revision-matched core-board documentation and measured10mm samples; resolve timing/watchdog in review before electrical release. Subsequent PH0 needs current-limited supply, driver/receiver prototype, oscilloscope and calibrated object mass/dimensions. Do not fabricate128channels or increase voltage as a substitute for diagnosis.
Current next stage: independent schematic electrical review, followed by an approved, source-backed correction. No PCB stage is authorized.

## Git and interaction evidence
Start commit bad4f665889b12f8b75245d9513ae3919fa0cca3. Delivery commit is discoverable with `git log -1 -- PCB/V1/project/SonoField-SingleSheet.pdf`; later sync verification records it explicitly. Public repository receives only reviewed engineering records and observable sanitized Codex messages. External ChatGPT BLOCKED; current open Codex turn PARTIAL.

Final Codex Status: REVISE_REQUIRED
Final result: REVISE
