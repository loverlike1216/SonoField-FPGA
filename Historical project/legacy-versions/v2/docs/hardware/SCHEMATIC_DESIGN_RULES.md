# Schematic design rules

- Schematic-only capture. No PCB documents, routing or manufacturing outputs.
- One stable physical channel ID across geometry, RTL mapping, calibration and schematic.
- Global wire NET attributes are the authoritative electrical labels; readable text
  alone never connects pins. Compare native exported pin nets against the manifest.
- Validate pin number/function from the exact manufacturer package, not symbol appearance.
- Show unused IC pins with explicit no-connect where the datasheet allows it. Do not
  mark a missing required input as no-connect merely to clear ERC.
- Keep polarity and initial operating limits explicit. Driver output is a measured
  waveform specification, not an assumed safe maximum-voltage rating.
- Include input pull-downs, local supply bypass, output damping selection and accessible
  logic/driver/transducer test points. DNP parts must be identifiable in assembly data.
- Keep TX high-current return out of the RX return path. Ground joins and return-current
  routing must be reviewed before PCB work; separate names alone do not solve grounding.
- Repeated cells use native copy plus explicit pin/net rebinding and complete metadata.
  Save/close/reopen before native export to avoid stale editor connectivity results.
- Generic symbol templates must expose MPN_TBD; inherited procurement/footprint data
  cannot be treated as a BOM selection. Library standardization warnings remain visible.
- Do not freeze 66 MHz external timing on digital simulation alone. Do not claim clock
  loss shutdown without an independently qualified watchdog/power-enable circuit.
