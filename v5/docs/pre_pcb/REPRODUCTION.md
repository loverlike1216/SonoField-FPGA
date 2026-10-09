# Reproduce from a clean clone

Use PowerShell7, Python3.10.11 with Tk8.6, installed Vivado/Vitis2025.2,
Icarus and GCC. Same-machine second clone/venv is an independent source and
Python environment check; EDA installations/license and OS are shared.
No physical board, FPGA load or historical source import is needed.

```powershell
git clone --branch feat/v5-prepcb-full-system https://github.com/loverlike1216/SonoField-FPGA.git SonoField-check
Set-Location SonoField-check
py -3.10 -m venv .venv
& .venv/Scripts/python.exe -m pip install -r v5/requirements-lock.txt
$env:CC='D:\DevC++\Dev-Cpp\TDM-GCC-64\bin\gcc.exe'
$env:IVERILOG_BIN='C:\iverilog\bin'
$env:VIVADO_BIN='D:\Vivado\2025.2\2025.2\Vivado\bin'
$env:PYTHONUTF8='1'
& .venv/Scripts/python.exe v5/scripts/run_prepcb.py --output v5/evidence/manual_prepcb_run
```

Adjust tool locations to the actual installation. Output must be fresh;
never overwrite an earlier result. Expected: original115+new56=171tests;
3696frames×3Icarus+1XSim with canonical hashes; originalC/AXI/calibration/safety/
equivalence; supervisor/mailbox in both tools;10sparsefits, independent
20480channelword comparisons; five runtimeGUI/C/twoRTL cases;37frame actual
newtop BRAM/supervisor/core chain. Each subgate records actual commands/logs,
ACKs and failure status. A Windows interactive desktop is required for the
Tk callback and native-window-render evidence; captures exclude desktop.

Build the candidate PS7/AXI/IIC platform and PL OOC route separately:

```powershell
& "$env:VIVADO_BIN/vivado.bat" -mode batch -source v5/scripts/build_prepcb_platform.tcl -log v5/evidence/manual_platform.log -journal v5/build/manual_platform.jou -tclargs manual_platform
```

`-tclargs` is last. Existing output project labels are rejected. Build creates
v5/build/manual_platform/platform.xpr and evidence/manual_platform/logicalXSA,
BD recreation, loadedsources, timing/utilization/DRC/CDC and routedDCP in build.
Six64KiB PS windows and five propagated IRQs are asserted, and ps_address_map.tsv
records the actual assigned segments. Logical XSA has no bitstream, DDR is disabled; fullboard constraints/BSP and
actual ARM firmware build remain gated. Never load candidateXDC into a
production flow: it deliberately errors. Do not program a device.

An optional real routed-DCP reread without disabling DRC rules:

```powershell
& "$env:VIVADO_BIN/vivado.bat" -mode batch -source v5/scripts/review_prepcb_drc.tcl -log v5/evidence/manual_drc.log -journal v5/build/manual_drc.jou -tclargs v5/build/manual_platform/prepcb_pl_routed.dcp v5/evidence/manual_drc_review
```

The default REQP-1839 report stops at20entries, so its warning count is a
reported subset. Review output does not qualify board reset/CDC or offchip
timing. Inspect required report content in addition to OS return codes;
in particular Vitis can return0 while the actual script raises a traceback.

Standalone tests must use a clone-local build TMP/TEMP directory; the original
board-project path tests deliberately reject globalWindowsTEMP fixtures.
The unified runner sets this itself. GUI start/stop guide is separate.
If a test fails, keep its exactlog, sourcecommit and sourcehash; fix the actual
cause and use a new output label. Never skip, lower a limit or edit goldens.

The new BOM is supplied as an editable workingxlsx with formulas and verification
status. Its optional authoring script uses the Codex bundled artifact-tool
runtime; that runtime is not a dependency of software/RTL validation. Original
three sourceworkbooks remain byte-equal to the migration candidate. Formula
recalculation/sensitivity and rendered sheet previews are retained separately.
