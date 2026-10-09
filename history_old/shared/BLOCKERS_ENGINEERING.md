# Current v2 blockers — 2026-10-03

Current model: GPT-6.1 Sol High. B01 RESOLVED: XC7Z020-1CLG400C user-confirmed. Internal CORE_TIMING RESOLVED in strategy3: routed132MHz WNS+0.082,TNS0,WHS+0.072,THS0,zero routing errors. B02 current source priority superseded by explicit N18/33.333MHz fallback; measurement is not required to proceed with that documented fallback.

| Gate | Current status | Required next evidence |
|---|---|---|
| B03 | DOCUMENT_MAPPING_RESOLVED; ELECTRICAL_ROUTE_OPEN | Bank34/35 VCCO,actual connector orientation/continuity,matched IO standard and translator voltage |
| PS/UART | BLOCKED | FTDI-B TX/RX/DTR/RTS to UART instance/MIO; PS reference clock/reset; reviewed preset/XSA/BSP/ARM build |
| Real transport | NOT_RUN |100/1000 packets,safe MMIO,atomic map/ACK generation,real GUI/ILA after verified platform |
| B04 | OPEN | Off-chip min/max timing,loading,watchdog,power and ADC/driver qualification; review retained DRC/methodology warnings |
| B05/B06/B07 | OPEN_PHYSICAL | Actual10mm batch load/polarity/phase/amplitude,receiver/ADC reference and measured levitation |
| Independent Review | PENDING | External review of actual source,warning scope and hardware evidence; no fabricated ChatGPT approval |

Detailed acquisition list: v2/evidence/pre_pcb_board_ready/MISSING_PHYSICAL_FACTS.md. No unknown-pin XDC,driver replacement,boot change,serial opening,bitstream download or PCB operation occurred. External ChatGPT history is BLOCKED and observable Codex transcript PARTIAL; these do not prevent sourced digital work.
