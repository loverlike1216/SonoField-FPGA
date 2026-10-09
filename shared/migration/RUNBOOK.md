# New clone runbook

PowerShell7; Python3.10 with Tk, installed Icarus/GCC and Vivado2025.2. Clone this same repository into a new empty directory and switch to the reviewed candidate commit/branch. No old sandbox is needed. The current candidate is not main until the user approves merging.

Observed installations on this host, verified during this migration:

| Purpose | Actual path / version |
|---|---|
| Candidate clone | `E:\Codex_project\AMD_Sonofield` |
| Independent test clone | `E:\Codex_project\AMD_Sonofield\.portability\clean` |
| Python3.10.11 | `C:\Users\loverlike\AppData\Local\Programs\Python\Python310\python.exe` |
| Icarus | `C:\iverilog\bin` |
| GCC9.2.0 | `D:\DevC++\Dev-Cpp\TDM-GCC-64\bin\gcc.exe` |
| Vivado2025.2 build6299465 | `D:\Vivado\2025.2\2025.2\Vivado\bin` |

Use `pwsh`7.6.5 and verify `python --version` is3.10 before creating the venv; otherwise invoke the full verified Python path. These are host installation paths, never board/pin/clock facts. After checkout, verify `git rev-parse HEAD` equals the concrete candidate reviewed in the PR; source/evidence commit scopes are recorded in the publication receipt.

```powershell
git clone -c core.longpaths=true -c core.autocrlf=false -c core.eol=lf https://github.com/loverlike1216/SonoField-FPGA.git <new-empty-directory>
Set-Location <new-empty-directory>
git switch chore/v5-ax7020-workspace-isolation
git remote -v
git rev-parse HEAD
git status --porcelain=v1
python -m venv .venv
./.venv/Scripts/python.exe -m pip install --no-cache-dir --disable-pip-version-check -r v5/requirements-lock.txt
./.venv/Scripts/python.exe -m pip check
# Set these to actual verified installations on this machine:
$env:VIVADO_BIN='<installed-Vivado2025.2-bin>'
$env:IVERILOG_BIN='<installed-Icarus-bin>'
$env:CC='<installed-gcc.exe>'
$pythonExe=(Resolve-Path ./.venv/Scripts/python.exe).Path
$runId=Get-Date -Format 'yyyyMMdd-HHmmss'
./v5/scripts/run_baseline.ps1 -Python $pythonExe -Output "evidence/migration/$runId/full"
./.venv/Scripts/python.exe v5/scripts/check_workspace_migration.py
./.venv/Scripts/python.exe v5/hardware/integration_candidates/20261009/verify_candidates.py --output "evidence/migration/$runId/candidates"
# The additional ADC-candidate cross-simulator gate is offline, not ADC approval:
./.venv/Scripts/python.exe v5/scripts/run_candidate_regression.py --label "manual-$runId"
Push-Location v5
& "$env:VIVADO_BIN/vivado.bat" -mode batch -source scripts/create_project.tcl -tclargs config/ax7020_ooc.tcl "evidence/migration/$runId/ooc" "build/migration/$runId/ooc"
& "$env:VIVADO_BIN/vivado.bat" -mode batch -source scripts/reopen_ooc.tcl -tclargs "build/migration/$runId/ooc/sonofield_v5.xpr" "evidence/migration/$runId/reopen"
Pop-Location
```

Success: full/summary.json PASS;115Python,3696frames×3Icarus+1XSim; exact canonical trace hashes, all waveform/calibration/C/AXI/safety/equivalence gates; candidate_checks.json15PASS; OOC marker and18v5RTL sources; reopened project marker and same18sources. Source/RAM/DDR/IO/physical board are not validated by these commands. Two independent new environments are required for the migration acceptance matrix.

For an explicitly user-authorized archive/recovery audit only, append `--archive-audit` to check_workspace_migration.py. Normal check compares Git metadata and does not read archive source. Baseline refuses an existing summary; equivalence and OOC refuse existing evidence. Use a fresh runId after a failure and retain the failed logs. Do not use skip flags. Tk needs an interactive desktop; no GUI skip substitutes for full PASS. A missing compiler/simulator/dependency is a failure to resolve or a stated blocker.

The clone options keep raw archived bytes at canonical LF on Windows and avoid path-length defaults. If running original negative Tcl gate tests directly, first create a scratch directory under this clone's `v5/build/` and point `TMP` and `TEMP` there. `run_baseline` does this automatically. Tcl accepts verified configurations under this clone's `v5/config/` or temporary configurations under its `v5/build/`; external workspace and archive configurations remain rejected.

Target ARM service still requires a revision-matched XSA/BSP and SF_UART_DEVICE_ID/SF_UART_BAUD/SF_PL_BASE. Serial profile rejects unverified board facts; do not enter guessed COM/pins. Host GCC is not ARM runtime evidence. BOM generator additionally needs Node and @oai/artifact-tool or ARTIFACT_TOOL_MODULE; the workbook is readable and fifteen checks run using Python standard library without that proprietary generation dependency. No manufacture/package is claimed.
