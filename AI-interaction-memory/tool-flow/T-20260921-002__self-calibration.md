# T-20260921-002 — v2 self-calibration software/digital stage

Project SONOFIELD_FPGA; active v2; stage SELF_CALIBRATION_SOFTWARE_AND_DIGITAL_SYSTEM.
Source session 01a0b538-9430-7561-9ba4-623f57501f43. Observable record, not private reasoning.
Status PARTIAL: curated important commands/results; source cutoff is in the session manifest.

## Trigger and files reviewed

User's exact instruction: ../codex/instructions/v2_self_calibration.md with source hash sidecar.
Preflight Git main/remote 5fa046d0ad3dd7fe0c44824b74b71f974f9a09bc, shared state, version freeze,
BOM, source/architecture/tests/AI indexes and board inventory. Existing v1 remains frozen.
External ChatGPT reader capability remains BLOCKED. No new external consultation or decision invented.

## Tool sequence and observable results

- PowerShell/Git/Python preflight: repository identity matched, original board hashes/freeze verified.
- Official AD7606B Rev B PDF read including visual Figure73 mapping; Cramer/primary reference checked.
- New RTL, software, config and test files written within v2; shared governance updated.
- Python first pipeline run exposed a NumPy integer JSON serialization error; fixed by canonical scalar conversion.
- Initial unit tests exposed missing test provenance and an over-tight 1e-16 m floating-centroid tolerance.
  Added required fixture metadata and used 1e-15 m numerical roundoff bound. Engineering limits unchanged.
- Initial RTL elaboration found a testbench hierarchical signal-name mismatch; corrected testbench name.
- Actual Python 512-path / 31-bin processing, three repeat artifacts, noise envelope and plots executed.
- `scripts/validate.py --output evidence/self_calibration_stage/validation`: inherited/core/map and new
  calibration tests; 44 Python tests, Icarus and Vivado 2025.2 XSim PASS. Logs and hashes saved.
- Exact 1024x8 ADC roundtrip includes signed boundary codes; 128-TX scan uses 32-frame short captures.
- 35 dB accuracy passed; 25 dB f0 error exceeded fixed bound; 15/5 dB rejected. Retained in robustness.json.
- `check_migration.py`: 212 frozen files / Git tree unchanged.
- Fresh clone, isolated environment, privacy scan, source commit/push and remote verification are
  recorded in the stage report and reproducibility summary when completed.

## Skills / boundaries

PDF skill used read-only to inspect the ADC timing/mapping figure. No PDF authored.
No other AI agent participated. No schematic, PCB, purchase, deployment or force push.
Tool outputs containing provider/private prompts are not copied; safe exporter records visible conversation only.

## Evidence and decision impact

../../v2/evidence/self_calibration_stage/validation/summary.json and self_calibration/summary.json.
ADCs require actual software initialization; RX phase references remain explicit hardware prerequisites.
Software source and checks are reviewable without the physical board. No physical success is inferred.


## Review and fresh-clone correction

Source checkpoint 4e5f0478e036cfefbadb2f6ceeb2ef1d180b6467. The first sparse clone's full tests and
model ran successfully, but repository audit rejected three RTL hashes after CRLF->LF checkout.
Failure preserved in evidence/self_calibration_stage/reproducibility/summary.json. The hash policy
now explicitly uses canonical UTF-8/LF for source text; frozen v1 byte hashes remain unchanged.
Review also found a stale frame-enable token could survive a rapid abort/re-enable transition.
Clearing the token on kill and gating calibration OE by live burst activity closes it; a new assertion
checks no OE outside the burst. Full validation is rerun under validation_review before a new clone.
Added a complete report generator with per-path quality CSV and health/mask/metadata summary.
Privacy scan flagged only the public Icarus copyright email in --version output; manually reviewed
as public license attribution and preserved. No credential was found; this is not private user data.

Final integration gate also uploads computed f_work before the generated LUT, measures the
normal carrier period, and tests the host transaction order (SW26). Final source validation
is validation_frequency, 45 Python tests; earlier evidence retained with its original scope.

## 2026-09-24 resume and workspace location

The previously supplied E:\Codex-project path is absent. The same repository, HEAD 4e5f047
and staged changes are present at E:\Codex_project\AMD-SonoField-FPGA. No move was performed
by this resume. Current operational paths updated; historical evidence and frozen v1 unchanged.
Fetch confirmed main is one local commit ahead, zero behind. ChatGPT history reader remains
unavailable in the exposed tool catalog. Next: commit reviewed corrections and run fresh clone.

## Final standalone reproduction and source synchronization

Source 9c058fe3b02469a6d36a08e3a7cbedd19076e67b. Command from v2: `../.venv/Scripts/python.exe scripts/reproduce.py --target build/repro_v2_calibration_review --output evidence/self_calibration_stage/reproducibility_review`.
Actual exit 0; all child commands exit 0. No v1 worktree; new locked environment, full 45 Python
tests and Icarus/XSim, model, repository/BOM audits, 10 transcript tests, 19 coordinate CSVs PASS.
Cross-environment calibration JSON (excluding Git commit only), canonical CSVs and binary ADC
hashes match. `git push origin main` succeeded; `git ls-remote origin refs/heads/main` returned
the source commit above on 2026-09-24. Final evidence/report checkpoint follows, with final
remote hash reported directly. Public repository: privacy scan required before final push.
Stage stopped before PCB implementation; hardware blockers and external ChatGPT BLOCKED remain.
