# UART continuation amendment — 2026-10-10

Current result: offline ACCEPT WITH LIMITATIONS; real-board/whole-platform REVISE.
COM3 now Code0 with driver11.6.0.420; pyserial3.5 locked. New read-only SLCR check
kept both CPUs Running, originalVivado retained; no UARTopen/TX/boardwrite.
Actual2025.2nativeSDT/BSP+ArmGNU13.2 linked safe/status ARMELF and OCM audit PASS
in current/newcleanclone;203+203tests PASS. FullELF is not claimed bit-exact;
application .text matches. Vitis platformAPI missingQEMU failure and RWX warning
remain. Prior1160sealedfiles and original criteria preserved.
User correction: recovery files are remote references only, no local verified
backup. Rev3 DTR/RTS A0 and image/platform/recovery/isolation/permission A2 gates
remain open. PC-B08 logicalbuild subgate closed; physical13PC-B scopes/BRAMProblem
and independentreview stay open. Samev5/mainunmerged/Draft4 update authorized.
See v5/docs/uart_resume/RESULT.md, v5/evidence/uart_resume/20261010_01/FINAL_VERIFICATION.json,
CP-20261010-002 and shared/uart_resume/PUBLICATION_RECEIPT.json. Prior snapshots
below retain provenance; this amendment supersedes only their stale current facts.

---

# Current next-stage v5 candidate (2026-10-10)

Formal ADC direction **AD7606C-16**, approved by the user; active top `v5/rtl/board/nextstage_pl.v`. Original B top/model and old BOM are regression provenance. Current instruction: `AI-interaction-memory/codex/instructions/v5_nextstage_20261010.md`. Branch stacks on unmerged PR3 (which includes PR1/PR2), main is unchanged. No new version.

Current completed evidence: [final report](v5/docs/next_stage/FINAL_REPORT.md), [test matrix](v5/evidence/next_stage/20261010/TEST_MATRIX.csv), [reproduction](v5/docs/next_stage/REPRODUCE.md), [open gates](v5/docs/next_stage/OPEN_GATES.md) and [publication receipt](shared/next_stage/PUBLICATION_RECEIPT.json). Offline ACCEPT WITH LIMITATIONS; real-board/whole-platform REVISE.

See [current contract](v5/docs/next_stage/EXECUTION_CONTRACT.md), [decisions](v5/docs/next_stage/ARCHITECTURE_DECISIONS.md), [hardware STOP](v5/docs/next_stage/AX7020_JTAG_UART_BRINGUP.md) and [GUI guide](v5/docs/next_stage/GUI_REAL_BOARD_USER_GUIDE.md). Native CAD/ERC and manufacturing remain HOLD.

From the repository root in PowerShell7, after installing `v5/requirements-lock.txt` in a local venv and setting VIVADO_BIN/IVERILOG_BIN/CC, run `.venv/Scripts/python.exe v5/scripts/run_nextstage.py --output v5/evidence/next_stage/reproduction_unique`. Run native offline EDA with `vivado.bat -mode batch -log <fresh-log> -nojournal -source v5/scripts/build_nextstage_platform.tcl -tclargs <fresh_label>`. No command opens/programs board hardware. Do not reuse an output label. The Vitis preflight is not a board application build.

The section below preserves prior candidate delivery provenance; its prior B pending-approval text is superseded by the actual2026-10-10 user decision.

# SonoField-FPGA — AX7020 v5

**SONOFIELD_FPGA · v5 ACTIVE · ALINX AX7020 · Vivado/Vitis 2025.2**

128 TX / 8 RX acoustic field and trajectory control, opposed 8×8 arrays, separate 8-bit requested/calibration phases, atomic maps, shared timebase and 32 lanes × 4 used. Current v5 adds fail-closed power/safety supervision, temperature compensation, bounded sparse geometry calibration, optional PS/PL service and a user-drawn trajectory editor at 50 Hz. Formal ADC is AD7606BBSTZ-RL; TX NU40C10T, RX MPN unqualified. Array geometry is 12 mm pitch, 100 mm nominal radiating-face gap adjustable 90–115 mm, origin at geometric center.

Start with [v5 run instructions](v5/README.md), [current state](shared/PROJECT_STATE.json), [recovery checkpoint](shared/CONTEXT_CHECKPOINT.md), [acceptance](shared/ACCEPTANCE.md), [hardware contract](v5/docs/pre_pcb/CENTRAL_ARRAY_HARDWARE_CONTRACT.md) and [runtime trajectory guide](v5/docs/pre_pcb/GUI_USER_DRAWN_TRAJECTORY_GUIDE.md). v5 is the sole active implementation. Root shared and current AI indexes retain decisions and provenance. This branch is a migration candidate containing earlier unmerged v5 work; main promotion requires user review.

From the repository root in PowerShell 7, create a Python 3.10 venv with Tk and install locked dependencies:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r v5/requirements-lock.txt
# Set VIVADO_BIN, IVERILOG_BIN and CC to actual installed 2025.2/Icarus/GCC tools.
./v5/scripts/run_baseline.ps1 -Output evidence/manual_baseline
.venv/Scripts/python.exe v5/scripts/run_prepcb.py --output v5/evidence/manual_prepcb
```

Choose one runner: `run_prepcb.py` includes the full baseline plus the additive gates; `run_baseline.ps1` runs the preserved core gates. Use fresh output directories. The complete current baseline requires 171 tests, 3,696 frames in each of three Icarus runs and one XSim run, plus C/AXI/calibration/safety/equivalence checks. The pre-PCB entry adds two-simulator supervisor/top verification, temperature/C comparison, sparse calibration and actual GUI callbacks. See [reproduction commands](v5/docs/pre_pcb/REPRODUCTION.md). For GUI use, enter v5 and run `../.venv/Scripts/python.exe -m software.ui.prepcb_app`; simulated sensor/calibration inputs are explicitly synthetic.

Current evidence: [pre-PCB results and limits](v5/docs/pre_pcb/PRE_PCB_COMPLETE_REPORT.md), [historical-isolation gates](v5/evidence/repository_cleanup/20261009/), [active dependency report](V5_ACTIVE_DEPENDENCY_REPORT.md) and [rollback plan](ROLLBACK_PLAN.md). Default search uses [current-scope search](shared/repository_cleanup/search_current.ps1), explicit v5 source lists and current root governance. Local ignore/IDE rules do not control GitHub website indexing.

Both 64-TX arrays use independent external power/protection/default-off cutoff. Central power uses protected single sources from AX7020 J10/J11 only; capacity, Rev3-matched PS/DDR/VCCO/pins, real UART/ADC/power cutoff, board timing and acoustics remain unqualified. OOC synthesis is documented-device evidence. No board programming or PCB release is authorized. Native v5 schematic NOT_CREATED, ERC_NOT_RUN, manufacturing HOLD; whole platform **REVISE**. No physical levitation/50 mg EPS result is claimed. ChatGPT access BLOCKED; current observable Codex records PARTIAL.

[Frozen historical project index — explicit user authorization required to read](<Historical project/README.md>)
