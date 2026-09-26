# Native ERC disposition — 2026-09-26
Actual EasyEDA 3.2.149 strict check: 0 fatal, 0 error, 45 warning records.
Raw exported report: native_erc_report.txt; API result: single_native_erc.json.

| Records | Category | Disposition |
|---|---|---|
| 2 | HARDWARE_ENABLE / RST_N have only one component pin | OPEN: logical FPGA interface endpoint only; independent reset, watchdog and power qualification are not complete. Do not suppress or invent connector pins. |
| 43 | Component attributes differ from supplier template | OPEN procurement qualification: generic values are explicit MPN_TBD; final passive/TX/RX/TP selections and package ratings remain unqualified. No automatic supplier standardization that would overwrite intended values. |

Warnings group multiple components; 43 is not a component count. Other information includes descriptive designators outside the library's letter+number recommendation. Canonical UPPER_TX IDs are intentional.
ERC proves only the configured native rules. Undefined/passive library pin types and named-net connectivity do not validate current, startup, propagation timing, analog recovery, or component ratings. Result: REVISE for electrical release; readable draft available for review.
