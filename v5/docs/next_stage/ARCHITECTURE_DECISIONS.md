# Current v5 decisions, 2026-10-10

| Decision | Status | Rationale / rejected options | Risk / approval boundary |
|---|---|---|---|
| D-NEW-01 AD7606C-16 | APPROVED BY USER | Exact user approval and unchanged P-20261008-001 body hash in corresponding decision. B remains a regression reference only. | Device direction approved; electrical qualification and order suffix HOLD. |
| D-NEW-02 four-DOUT profile | DIGITAL CANDIDATE | OS111, PAR/SER1, CONFIG0x10, BW0xff, +/-5V SE, OSoff, CRCoff, initially800kSPS. Each register read back; fail closed. | No claim of measured analog bandwidth, CRC-enabled frame support or board timing. |
| D-NEW-03 temperature | IMPLEMENTED / OFFLINE TESTED | Three TMP117 segments center0x48/upper0x49/lower0x4b; ID, ready, EEPROM busy, NACK, signed range, timestamps. Three air samples estimate a vertical field. | Physical sensor placement, BSP I2C and measurements HOLD. SHT45 RH diagnostic only; no invented humidity correction. |
| D-NEW-04 array transducers | TX FAMILY APPROVED / SUFFIX HOLD | NU40C10T family; vendor T/R-2 images are user input, not complete rated test conditions. | RX exact MPN, continuous excitation and footprints require supplier/bench review. |
| D-NEW-05 power | PROPOSED / HOLD | Upper and lower independently protected external12V; central only AX7020 J10/J11, single source per rail, no backfeed. | Header capacity and TVS/eFuse/fuse/wire/inrush/thermal coordination unknown. |
| D-NEW-06 safety | RTL VERIFIED / CIRCUIT PROPOSED | NC estop, local watchdog, thermal comparator, PGOOD, cold-start rearm and actual rail cutoff independent of PS/PL. OE alone insufficient. | Electrical failure injection NOT_RUN; user keys not an emergency power disconnect. |
| D-NEW-07 board writes | BLOCKED | No enumerated JTAG; CP2102N Code28 and no COM. Rev3/DDR/clock/UART/VCCO and current image ownership unqualified. | No halt/reset/init/programming/RAM writes/driver installation. A2 facts plus separate user approval required. |
| D-NEW-08 publication | AUTHORIZED DRAFT ONLY | New branch stacks on PR3; PR1/2 ancestors retained. | Normal reviewed commit/push/Draft PR allowed; main merge requires user's concrete candidate approval. |

All changes continue active v5. No new version, no history body reads, no archived source edits. External ChatGPT reader BLOCKED; this document is Codex engineering normalization of actual user instructions, not a ChatGPT decision or independent electrical review.
