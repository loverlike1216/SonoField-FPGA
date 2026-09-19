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
Evidence: v1/evidence/validation, model, integrity and board_inventory. Fresh clone/new venv at 0b257de PASS, all six model and 19 coordinate/phase CSVs match.
Raw fresh-checkout tool evidence retained in v1/evidence/reproducibility/validation.
Vivado target gate correctly blocks missing part; no synthesis performed. No hardware acceptance implied.

## Unresolved / next action
Local and clean-clone gates complete; obsolete records removed; final evidence commit is synchronized to main. Next supply actual board
and transducer facts for the open hardware problems; import external chat only through a real source.

## Scope result
ACCEPT WITH LIMITATIONS for requested v1 organization: external ChatGPT history cannot be imported with
current tools. No messages/decisions fabricated. Whole-platform hardware acceptance remains pending.
