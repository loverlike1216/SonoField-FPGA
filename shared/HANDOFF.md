# Schematic V1 handoff

Goal: editable one-sheet schematic and readable export; active v2, frozen v1 unchanged.
Inputs: user schematic instruction,10mm geometry, existing RTL/interface and BOM, constrain precedence, selected library pins and manufacturer sources.
Changes: PCB/V1 native project,83module consolidation, horizontal/right-aligned labels, vector exports, audits, open Problem and governance/interaction records.
Validation:3992native pins and1338independent mapping checks pass;212frozen files intact; save/reopen and PDF visual QA pass. ERC0fatal/0error/45warnings.
Failures retained: capture timeouts, cache refresh discrepancies, old TEXT fields, renderer disconnect on bulk styling, font unit mismatch, optional export API incompatibility. Final artifacts re-exported after corrections.
Unresolved: core-board pins/VCCO/package, serializer hold timing, independent watchdog/power qualification, exact generic MPNs and analog/batch measurements. External ChatGPT inaccessible. No PCB/hardware PASS.
Evidence: PCB/V1/log/review; report: shared/report_schematic_v2_V1.md.
Next: review P-20260925-001 and electrical gates. Read PROJECT_STATE and VERSION_STATE; do not create v3 or alter frozen v1. Windows terminal defaults to pwsh7.
