# Runtime trajectory editor

From the independent repository root in PowerShell7:

```powershell
$env:CC='D:\DevC++\Dev-Cpp\TDM-GCC-64\bin\gcc.exe'
$env:IVERILOG_BIN='C:\iverilog\bin'
Set-Location v5
& ../.venv/Scripts/python.exe -m software.ui.prepcb_app
```

Create points using XYZ text or clicks, edit speed/dwell, select and drag points
and orange Bezier handles, insert/delete/reorder and undo/redo. Use XY/XZ/YZ
planes or3D projection;3D dragging holdsZ and inverse-projectsX/Y, so changeZ
with text/other planes. Closed toggles an arbitrary user figure. No preset
coordinate sequence is used by this editor. Topology changes invalidate curve
handles explicitly. Save JSON and load it to recover vertices/handles/limits/
timestamp/v5/calibration reference with SHA256 integrity checks.

Preview produces50Hz rest-to-rest bounded segments and validates finite3D bounds,
step, velocity, acceleration, jerk, phase delta and normalized local force-
potential minimum. STANDING_WAVE uses opposite bank phase128codes. Stable
local modeled curvature is not proof of an acoustic trap, real global-side-lobe
clearance or supported mass. Existing GUI remains available through its button.

The three temperature fields are visibly SYNTHETIC_REFERENCE. Calibration runs
an explicitly generated sparse numerical reference; real128TX responses remain
UNMEASURED. Start is an explicit manual simulation action: actual compiled C
service receives original CRC/sequence framed bytes, negotiated optional
commands and complete nanometre coordinates, generates maps on logical20ms
ticks, then inherited RTL verifies actual batchACK. Execution cursor/position
represents a command model, never measured particle position. C capacity512
frames is negotiated; planning may produce12000 and upload rejects oversize.

Pause/resume exchange real extension commands; pause holds C cursor while
heartbeat and safety checks continue. STOP/disconnect cancels work and requires
another manual start. CRC/sequence/watchdog/sensor fault rejection is tested.
Real physical UART/USB connection is gated by PC-B01/B08; port enumeration
never opens/toggles a device. Optional pyserial enables enumeration; no COM
number is fixed. The current runnable mode is HOST_FIXTURE plus RTL simulation.

Five integration cases are generated during `prepcb_system_gate.py` execution
by actual Entry variables and GUI add/drag/Bezier/closed/edit callbacks. They
are automated UI tests, not fabricated human-drawn demonstrations. Each saved
runtime input is reloaded, hashed, bounded, checked against independent Python
phase/trap calculation, sent through actual C packets and replayed in both
Icarus and XSim. Evidence is under the current successful `system*/gui/case_*`
directories; each includes exactinput, protocol trace, maps and actualACK.

Hardware bring-up remains a separate approved procedure after matched board,
power, cutoff, ADC, BSP and timing gates. Never use the simulation ARM/calibration
flags as permission to energize physical drivers.
