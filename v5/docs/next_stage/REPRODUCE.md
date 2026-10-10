# Reproduce the current offline candidate

Use a fresh independent clone of the current development branch; never reset, clean or reuse the frozen physical sandbox. A remote clone downloads Git objects, but the sparse worktree below never materializes historical source. Main and PR3 remain separate unmerged candidates.

```powershell
git clone --no-hardlinks --no-checkout https://github.com/loverlike1216/SonoField-FPGA.git <fresh-clone>
Set-Location <fresh-clone>
git config core.autocrlf false
git sparse-checkout init --cone
git sparse-checkout set v5 shared AI-problem AI-chat-memory AI-interaction-memory .github .vscode
git checkout codex/v5-ad7606c16-nextstage-20261010
python -m venv .venv
& .venv/Scripts/python.exe -m pip install -r v5/requirements-lock.txt
```

Replace `<fresh-clone>` with an unused directory. Use Python3.10 and inspect actual tool locations. The measured Windows environment used the following paths; these are tool installation paths, not board pin/clock/DDR assumptions:

```powershell
$env:VIVADO_BIN='D:/Vivado/2025.2/2025.2/Vivado/bin'
$env:IVERILOG_BIN='C:/iverilog/bin'
$env:CC='D:/DevC++/Dev-Cpp/TDM-GCC-64/bin/gcc.exe'
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
& .venv/Scripts/python.exe v5/scripts/check_structure.py
& .venv/Scripts/python.exe v5/scripts/check_migration.py
& .venv/Scripts/python.exe v5/scripts/check_prepcb_preservation.py
& .venv/Scripts/python.exe v5/scripts/check_workspace_migration.py --freeze-base b08ccf58c984ca7e6250d9e8489a24bc0789c4b0
& .venv/Scripts/python.exe v5/scripts/prepare_nextstage_checkout.py
& .venv/Scripts/python.exe v5/scripts/check_nextstage_preservation.py
& .venv/Scripts/python.exe v5/scripts/run_nextstage.py --output v5/evidence/next_stage/reproduce_full
```

Every command must exit0; inspect each summary and failure log. `run_nextstage` includes every original baseline/pre-PCB gate, all current unit tests, three Icarus plus one XSim3696-frame runs, C/AXI/safety/equivalence, temperature/sparse/runtime-GUI, C-16 adapter, full1024-frame capture/BRAM/read/ACK, actual C-16 integrated top and portable host-C/ARM object. Never skip a failed stage or reuse an old result directory. The software gate's1000PING measurements are in-process host fixtures, never UART/PS/AXI hardware evidence. Startup-only acceleration in ADC benches does not qualify real supply/reset timing.

For a scoped standalone unit rerun, start in `v5`, create a fresh `v5/build` scratch directory and set both `TMP` and `TEMP` there; the existing path guards intentionally reject system temp outside the clone. Full runners already do this.

For the native logical platform, choose an unused alphanumeric build label (example `review_native_01`). Run from the clone root. The Tcl creates `v5/build/<label>/platform.xpr`, a routed DCP and new evidence; it never connects hardware or writes a bitstream:

```powershell
$cloneRoot=(Get-Location).Path
Push-Location v5/build
& "$env:VIVADO_BIN/vivado.bat" -mode batch -log review_native_01.log -journal review_native_01.jou -source "$cloneRoot/v5/scripts/build_nextstage_platform.tcl" -tclargs review_native_01
& "$env:VIVADO_BIN/vivado.bat" -mode batch -log reopen_native_01.log -journal reopen_native_01.jou -source "$cloneRoot/v5/scripts/review_nextstage_platform.tcl" -tclargs "$cloneRoot/v5/build/review_native_01/platform.xpr" "$cloneRoot/v5/build/review_native_01/nextstage_pl_routed.dcp" "$cloneRoot/v5/evidence/next_stage/reopen_native_01"
Pop-Location
```

Success means logical BD validation, explicit current-v5 source loading, six AXI windows/five IRQs, reopening and positive internal setup/hold slack. Full DRC currently exposes346REQP-1839 and one OOC ZPS7-1 warning. External input/output delays, production XDC and matched Rev3 platform remain HOLD. No amount of positive OOC slack constitutes board timing closure or physical release. The native review raises only the report-message limit; it does not waive rules or change severity/constraints.

GUI: `.venv/Scripts/python.exe v5/software/ui/nextstage_app.py --mode HOST_FIXTURE --output v5/build/manual_gui`. Use runtime points/Bezier/XYZ and save/load; this controls requested/model trajectories. `--mode REAL_BOARD` is locked and opens no port. Native EasyEDA/ERC is NOT_RUN; the JSON/SVG/Excel contracts are review candidates.

Before publishing new logs, preserve their raw originals in the new run's ignored `local_raw/`, redact Windows identity/private device serials/private paths, record raw and public SHA256, and scan credentials. Do not redact or rewrite frozen historical evidence. Rollback is a separate clean checkout of PR3, or a reviewed normal revert plus full regression; never force-push or reset the old sandbox. Main merge and a fresh postmerge remote-main run require the user's explicit candidate approval.
