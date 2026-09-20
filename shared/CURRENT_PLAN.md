# Execution contract: V2_BOOTSTRAP_AND_INHERITED_BASELINE

## Goal and approval
User attachment explicitly approves v2. Freeze v1 without changing any file, then provide a complete standalone v2 baseline.

## Scope / allowed changes
Copy all tracked engineering inputs, preserve historical evidence, adapt version paths and tooling, import the supplied BOM unchanged with readable text exports, update root governance and AI checkpoints.

## Non-goals / constraints
Do not implement future self-calibration, ADC RTL, fabricate PCBs or claim hardware success. No guessed part/XDC or new version beyond v2. New BOM is a design input, not measurement or fresh supplier verification.

## Inputs / dependencies
User formal instruction, root BOM workbook, existing v1 source/evidence, board references, Python 3.10, Icarus and Vivado 2025.2. External ChatGPT reader remains unavailable.

## Validation / required evidence
Frozen-file SHA256 audit; full inherited Python/Icarus/XSim tests and waveform comparison; model/coordinate regeneration; clean clone/new venv with v1 absent from checkout; no runtime ../v1 imports; BOM cell/quantity audit and secret check; commit/push with remote equality.

## Rollback / done when
Normal revert of v2/governance changes, retaining v1 and Git history. Stop after bootstrap report for review. Full v2 hardware/calibration acceptance remains future work.

## Completed checkpoint

All scoped bootstrap gates PASS, including v1-absent clean reproduction. Source e353c16d35da2b430f46ba5b83a5a9a79dd749b7.
Stopped for user/reviewer assessment. Next proposed stage V2.2 remains unstarted. Hardware blockers persist.
