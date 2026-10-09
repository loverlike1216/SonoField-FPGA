# v5 historical-isolation reproduction

The migration candidate uses the original SonoField-FPGA repository and v5. Main remains unmerged until user review. These commands perform digital/offline verification only. They never program, reset or initialize AX7020.

## 1. Clone current content without expanding historical files

Use PowerShell 7, a new empty destination and the actual reviewed candidate SHA from the PR/publication receipt.

```powershell
git clone --no-checkout --branch codex/v5-historical-project-isolation-20261009 https://github.com/loverlike1216/SonoField-FPGA.git '<new-empty-directory>'
Set-Location '<new-empty-directory>'
git config core.autocrlf false
git config core.eol lf
git config core.longpaths true
git sparse-checkout init --cone
git sparse-checkout set v5 shared AI-problem AI-chat-memory AI-interaction-memory .github .vscode
git checkout codex/v5-historical-project-isolation-20261009
git rev-parse HEAD
git status --porcelain=v1
Test-Path -LiteralPath 'Historical project' # must be False
```

Git history and index metadata retain the archived identities, but historical worktree files are absent. Local verification used `git clone --no-hardlinks` from the candidate clone and a separate repository/venv, with the official remote added and publication checked afterwards. This proves an independent checkout and Python installation on the same machine, with shared installed EDA; it is not a second computer.

## 2. Install locked dependencies and identify tools

```powershell
python --version # use Python 3.10
python -m venv .venv
.venv/Scripts/python.exe -m pip install --no-cache-dir -r v5/requirements-lock.txt
.venv/Scripts/python.exe -m pip check
.venv/Scripts/python.exe -c "import tkinter; print(tkinter.TkVersion)"
$env:VIVADO_BIN='<actual-Vivado-2025.2-bin>'
$env:IVERILOG_BIN='<actual-Icarus-bin>'
$env:CC='<actual-gcc.exe>'
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
```

Verify the paths/version output instead of copying another machine's installation paths. Tk tests need a usable desktop. Missing tools or GUI capability are blockers; do not use skip flags or reinterpret partial output as PASS.

## 3. Execute current integrity and full functional gates

```powershell
.venv/Scripts/python.exe v5/scripts/check_workspace_migration.py
.venv/Scripts/python.exe v5/scripts/run_prepcb.py --output v5/evidence/repository_cleanup/manual_full
```

Use a fresh output directory. `run_prepcb.py` includes the complete inherited baseline: 171 Python tests, 3,696-frame traces in three Icarus runs and one XSim run, calibration/C/AXI/safety/equivalence. It then runs supervisor/mailbox, numerical temperature/sparse calibration, five real GUI callback cases and the actual new top in both simulators. For only the preserved core baseline, use `./v5/scripts/run_baseline.ps1 -Output evidence/repository_cleanup/manual_core` instead. Do not run both merely to duplicate the inherited baseline.

Success requires every summary PASS, 171 tests with no core skips, all four deterministic hashes matching, 375 GUI frames across five cases, 20,480 Python/C channel words, ten sparse fits and the actual-top 37-frame ACK matching in both tools. The supplemental sensor/calibration data is synthetic. GUI automation is not a human manual drawing test or measured particle movement.

## 4. Rebuild the documented-device Vivado project

```powershell
Push-Location v5
& "$env:VIVADO_BIN/vivado.bat" -mode batch -source scripts/create_project.tcl -tclargs config/ax7020_ooc.tcl evidence/repository_cleanup/manual_ooc build/manual_ooc
& "$env:VIVADO_BIN/vivado.bat" -mode batch -source scripts/reopen_ooc.tcl -tclargs build/manual_ooc/sonofield_v5.xpr evidence/repository_cleanup/manual_reopen
Pop-Location
```

The current core project must load exactly the 18 v5 RTL sources in `config/ooc_source_list.txt`. Native synthesis/reopen reports in the reviewed evidence compare before, after and the independent clone: xc7z020clg400-2, 7.576 ns internal target, 7,219 LUT / 17,918 FF / 4 BRAM, synthesis WNS +0.994 ns / WHS +0.157 ns. Preserve the 28 synthesis warnings and 2,324 input / 256 output delay omissions. These are synthesized OOC results; full-board timing and production PS/DDR/UART/IO are unqualified.

## 5. Search, evidence and recovery

```powershell
./shared/repository_cleanup/search_current.ps1 -Engine rg -Pattern 'ALINX AX7020'
./shared/repository_cleanup/search_current.ps1 -Engine git -Pattern 'ALINX AX7020'
```

The wrapper supplies explicit current paths. `git grep` does not honor `.ignore`/`.rgignore`; do not run it across the whole repository. Ignore/IDE files cannot control GitHub website indexing. The default integrity checker reads active mappings and Git metadata only; a Python open audit recorded zero historical content attempts. Historical content reads, including `--archive-audit`, require a separate explicit user history/recovery authorization after this migration.

Compare new logs with `v5/evidence/repository_cleanup/20261009/FINAL_VERIFICATION.json`, `DIGITAL_BEFORE_AFTER.json`, `VIVADO_COMPARISON.json` and `CLEAN_SOURCE_COMPARISON.json`. Native dates/absolute report paths and explicitly excluded wall-clock timestamps can differ; canonical trajectory/map/trap/ACK values and current source identities must agree. A discrepancy requires analysis, not golden replacement.

Before merge, closing/leaving the Draft PR unmerged keeps main intact. After an approved merge, use a reviewed normal revert as described in the root [rollback plan](../../ROLLBACK_PLAN.md). The exact pre-migration complete source is `7dda49f00983c57d06ac639ad70bdaff9696e900`; the original root is `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`. Recovery reads must be authorized and performed in a separate clone. Gate7 post-merge verification remains deferred until the user approves the concrete PR.
