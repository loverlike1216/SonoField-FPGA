# Board evidence audit — 2026-09-19

Authoritative directory: `../Zynq7020/`. All 10 PNGs were viewed, both `.const` XML files read in full.
Manifest, file lengths, SHA-256 hashes and 101 verbatim pin records: `evidence/preflight/`.
No schematic, manufacturer manual, native XDC, reference project or BOM was present.

| Fact | Evidence | Status |
|---|---|---|
| Robei octagonal Zynq-7020 | Board photos and description screenshot | DOCUMENTED family |
| Complete ordering code | Photos too indistinct for reliable package/speed/temperature identification | BLOCKING |
| PL clock candidate N18, 33 MHz | hardware.const: `Name="N18" Function="33MHZ"` | DOCUMENTED, user chose .const precedence |
| 33.333 MHz in screenshots | 3.png and peripheral table | Superseded by user instruction; not silently averaged |
| SW1 W9 | hardware.const | DOCUMENTED function; polarity only auxiliary screenshot |
| GPIO candidate mappings | gpio.const; exported verbatim | DOCUMENTED, unresolved malformed entries excluded from assignment |
| FPGA I/O standard and VCCO | Not supplied | BLOCKING |
| Header supply 5 V | Auxiliary tables/layout | Does not imply 5 V FPGA IO |

## Per-file inspection

- `075c1b752e612dda8d314e4415b73c13.png`: board photograph and J3/J4/J5/J6 orientation; chip enlarged for inspection but complete marking not reliable.
- `1.png`: J3/J4 numbering tables; differs from .const.
- `2.png`: J5/J6 tables; V16 appears at two J6 positions; this table is not authoritative.
- `3.png`: peripheral table, 33.333 MHz, SW1 description, boot switch table.
- `396993c30e2d447db53dcf3b509222a1.png`: expanded peripheral table; CEC J15 differs from hardware.const J5.
- `1ec52b807edd6cf0dddcf8ffc4109a82.png`: Robei EDA view confirms 33MHZ label, no full part/voltage data.
- Both `4cb7b508670dc325da8448dbf51cb117*.png`: duplicate annotated board front/back pictures; no new electrical facts.
- `9268ababf01f495387fe9e2705411573.png`: connector orientation layout; useful visual reference, not chosen numbering authority.
- `屏幕截图 2026-09-18 232246.png`: introductory board description; claims 68 mm body and 2 mm connector pitch, not fabrication dimensions.
- `constrain/hardware.const`: complete peripheral mapping, no IO standards/part configuration.
- `constrain/gpio.const`: full GPIO candidate table; J4 Pin6 duplicated and V16 J6 pin number missing.

## Remaining use restrictions

User explicitly instructed `.const` precedence, resolving disagreement with screenshots. Within-file
errors remain: J4 Pin6 denotes both D18 and E18; V16's function is `J6 Pin` with no number.
No affected signal is assigned. Even unambiguous records are **pin candidates** until complete part,
bank supply, board revision and connector orientation are verified. Do not turn these CSV rows into XDC automatically.

33 MHz is the documented oscillator value, not a frequency-counter measurement. The proposed 132 MHz
serializer clock is 4x this value, but no MMCM configuration or routed clock has been validated.
Keep the original local images out of public Git until redistribution rights are clear; the audit records facts and hashes.
