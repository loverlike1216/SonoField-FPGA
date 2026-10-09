# Goal
Isolate AX7020-only v5 in an independent clone and preserve the fixed old Git tree in history_old.

# Scope
Phase0–7 audits, independent environments, archive mapping, current state/root cleanup, safe output/path parameters, regression/OOC/reopen, candidate commits and Draft PR.

# Non-Goals
No new version, core redesign, formal ADC substitution, board operations, new PCB/manufacturing or main merge.

# Constraints / Invariants
Original sandbox is immutable. Preserve protocol/registers/phase/geometry/safety/motion/128TX/8RX and all acceptance criteria. No skipped tests or changed goldens. Archive is exact BASE blob/mode/raw-byte copy. Public material must exclude private raw/credentials.

# Architecture / Allowed Changes
Keep v5's existing production modules; add only explicit output/work parameters and isolation/metadata checks. Current root contains current documentation/AI scope and v5. Tool installations are host facts, not board facts.

# Inputs / Dependencies
User Phase0–7 instruction, local read-only handoff, fixed BASE Git tree, actual Python3.10/Tk/Icarus/GCC/Vivado2025.2. No unsupported chat API.

# Validation / Evidence Required
All MIG01–12;115Python,3696frames×4, C/AXI/safety/calibration/equivalence, native OOC/reopen/source list, exact archive hashes/modes, original rehash, second clean clone with its own locked venv. Preserve failed evidence.

# Rollback
Candidate failure leaves main and original sandbox unchanged. Future approved revert commit restores pre-migration tree; never rewrite history.

# Done When
Candidate regression and integrity gates pass, evidence/risk/rollback/checkpoint are reviewable and Draft PR is submitted. Formal main switch awaits explicit user approval; post-merge remote fresh clone is deferred until that approval.
