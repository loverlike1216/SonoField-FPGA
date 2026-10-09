# Schematic tools (v2, schematic V1)
Run from repository root using pwsh and the existing Python environment.

1. `tx_design.py`, `system_design.py`, `power_design.py` describe explicit intended circuit connectivity. They do not prove electrical correctness.
2. `capture_tx.py` / `clone_tx.py` and `capture_sheet.js` performed bounded native capture through the official local gateway. Do not rerun mutation scripts on the delivered sheet.
3. `consolidate_native.py` transforms the preserved official modular checkpoint into a one-page interchange. Re-running overwrites the interchange; back up the delivered native export first. GUI import and native verification are required after regeneration. Never edit the live `.eprj2` database.
4. `audit_tx.py --sheets 32 --extra system_design.json --extra power_design.json --netlist single_native_netlist.json --output single_connectivity_audit.json` checks3992 native pins against intent.
5. `audit_mapping.py` independently checks128TX /8RX, serializer ordering, geometry and return links, and verifies frozen v1 hashes.

Native export recipe (reviewed gateway project guard): `eda.sch_ManufactureData.getExportDocumentFile(name, 'PDF')` or `'SVG'`; getNetlistFile(name,'JLCEDA'); getProjectFile(name,undefined,'epro2'). Read File bytes and save without printing binary data. Do not use newer optional PDF parameters with client3.2.149. Save, close/reopen and re-export before auditing.

Source TEXT uses x/y/align. Attribute API fontSize uses inches while interchange source uses hundredths. Final labels source7 = API0.07. All net labels horizontal; ADC left labels right-aligned before pin numbers. No tests weaken electrical gates.

Source checkpoint: PCB/V1/log/review/SonoField_modular_checkpoint.epro2. Earlier capture calls/netlists are preserved in capture_history.zip. All generated outputs are drafts until separate timing/safety/board/analog gates close.
