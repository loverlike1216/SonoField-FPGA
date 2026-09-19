# v1 layout handoff

## Goal / inputs reviewed
Apply user's new governance rules and explicit same-version cleanup request to local and GitHub layouts.
Read current source, shared decisions, board blockers and latest complete digital evidence at ada1b20.

## Changes
Engineering files moved into v1; root retains governance/state/AI coordination. Current version is v1,
not a new generation. Updated scripts, Tcl project label and manual commands. Original board folder stays
at root. Obsolete current-tree records removed after integrity passed; Git history remains.
Chat source SonoField-FPGA recorded as BLOCKED, with no fabricated import or decision.
Three hardware consultation problems created with source evidence and body SHA256; external delivery blocked.

## Validation / evidence
Baseline and current 19 tests PASS; complete Icarus/XSim regression PASS. RTL/TB/tests and 12 board files
unchanged; six model CSVs and 19 coordinate/phase CSVs identical; trace hash unchanged.
Evidence: v1/evidence/validation, model, integrity and board_inventory. Fresh reproduction pending.
Vivado target gate correctly blocks missing part; no synthesis performed. No hardware acceptance implied.

## Unresolved / next action
Complete local/clean-clone gates, remove obsolete records, publish/verify main. Then supply actual board
and transducer facts for the open hardware problems; import external chat only through a real source.
