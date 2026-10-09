# Native API reliability findings

Environment: EasyEDA Pro 3.2.149, Run API Gateway 1.0.6, easyeda-api skill 1.1.36.
Skill source ccfaf28a577b61a09ebc907f0a943d1e6c782def. Local bridge only (127.0.0.1).

- An oversized sequential capture exceeded the bridge's 30-second response deadline.
  The editor continued the changes. Never automatically retry timed-out mutations.
  Read native contents first. Four-component capture batches avoid this deadline.
- `createNetLabel` returned undefined; `setDocumentSource` returned false. These
  beta paths are not used for delivery. No project database is edited directly.
- Copy-page creates fresh designators. Rebind parts by verified template positions,
  with a one-to-one check; do not assume old designators survive.
- Passing only a new designator to component modification did not preserve all
  custom qualification properties in the exported netlist. Write the full required
  property set, then inspect exported manufacturer/assembly/value fields.
- Null manufacturer/supplier properties did not remove inherited library values.
  Unselected template parts now explicitly use MPN_TBD / UNQUALIFIED / TBD.
- The first copied page's netlist retained old names after edits; later it reported
  nine disconnected test points despite correct native wire endpoints. Closing and
  reopening the saved page refreshed the netlist and all 138 pins passed.
  Internal caching is a hypothesis, not a proven implementation diagnosis.
- The accepted copy path rebuilds wires from the intended pin map and the actual
  library pin coordinates, saves, closes, reopens, then independently exports and
  compares native connectivity. No old-net rename result is trusted alone.

Failure evidence: tx_copy_initial_failure.json, tx_copy_rename_failure.json,
wire_api_scope.json, copied_testpoint_pins.json, copied_wires.json.
Resolution evidence: native_copy_reopen.json and tx_connectivity_audit.json.
An API success response or a displayed drawing alone is not electrical verification.

## Final consolidation and export (2026-09-26)
- Initial source TEXT `positionX/positionY` did not survive this client. Its actual format requires `x/y/align`; corrected import restored all 381 texts.
- Bulk attribute edits disconnected the renderer after about 400 edits. Closed the application, preserved a backup, rebuilt and reimported the complete interchange. No connectivity was inferred from a timeout.
- Current-client attribute API fontSize is in inches: 0.07 maps to source fontSize 7. Passing 7 produced giant labels; visual QA detected it and the 32 ADC labels were corrected before delivery.
- getSvgFile is absent in 3.2.149. getExportDocumentFile(name, 'SVG') and (name, 'PDF') succeeded with defaults. Explicit newer optional parameters had stalled at 1%; do not reuse them here.
- Final native save/reopen, PDF/SVG export, 3992-pin audit and 1338 independent mapping checks passed. 45 native warnings remain; see ERC disposition.
- Native baseline has 83 modules on ONE page, not 83 final pages. Retired experimental source is locally retained in ignored build/schematic_api.
