# PC control application — v2

Use PowerShell 7. From the repository root:

```powershell
./v2/scripts/run_motion_app.ps1
```

Or from `v2`, with the existing Python 3.10 environment:

```powershell
../.venv/Scripts/python.exe -m software.ui.app
```

Tk is included in the verified local Python environment. PySide6 is absent;
the user-permitted built-in GUI fallback avoids changing the pinned dependencies.
Motion logic is independent of Tk. The initial window is 1360×920, resizable.

## Operation

1. Connect simulation. This does not start motion.
2. Load the calibration. The default is the previously validated synthetic
   calibration dataset, explicitly SIMULATION_ESTIMATE. `f_work` is shown.
3. Apply center trap. A real RTL simulation must acknowledge it before the
   operator-confirmation control becomes enabled.
4. Confirm ball at center. In simulation this is a workflow acknowledgement,
   not a statement that a real sphere exists or has been observed.
5. Preview and send a point/planar path, use vertical controls, hold or return.
6. STOP cancels generation/execution and invalidates the pending worker result.
   A fresh center preparation and confirmation are needed before further motion.

Position fields say **Commanded trap position**. Actual position is NOT_MEASURED.
The displayed position is the last completed logical command, not live particle
telemetry. Each command waits for a real file-driven RTL run; it is not a board
connection or a real-time Windows waveform generator. During the full demo,
the UI remains responsive while the worker runs the complete continuous path.

Planar parameters are editable structured fields in the JSON panel: distances
are mm, angles degrees. Presets exist for every supported shape. Bounds, speeds,
repeat count, start/end markers and coordinate directions are visible. Acceleration
and engineering workspace are advanced configuration choices rather than basic
controls. The board backend intentionally rejects all connection attempts.

## Reproduction and evidence

```powershell
# From v2: complete GUI-to-RTL demo and cropped screenshot
../.venv/Scripts/python.exe -m software.ui.app --automated-demo --output build/motion_gui

# Full tests, three Icarus GUI runs, independent XSim GUI run and prior regression
../.venv/Scripts/python.exe scripts/motion_gate.py --output build/motion_gate
```

Automation records `SIMULATION_AUTOMATION_ONLY` for center confirmation; it never
pretends a human observed physical levitation. Command JSONL and readable text,
trajectory JSON, map/ACK hashes, cropped app screenshots and tool logs are saved.
Wall-clock timestamps are excluded from deterministic comparisons.

If a tool is missing, the GUI reports failure and stays disabled. Configure
`IVERILOG_BIN` / `VIVADO_BIN` to actual installation directories. The default
paths match the verified local tool environment. No tool failure is converted
to a synthetic successful ACK.
