# SonoField-FPGA — AX7020 v5

SONOFIELD_FPGA · sole active v5 · Vivado/Vitis2025.2 · same formal repository.
Current branch is a hardware design candidate stacked on unmerged PR4; main is not promoted.

Current design:128TX/8RX, separate8bitrequested/calibration,32lanes×4used, shared timebase,
atomic maps and50Hz trajectory updates;12mm radiating-face pitch, nominal100mm gap
adjustable90–115mm, geometric-center origin. Formal ADC AD7606C-16, one central PCB,
two64TX arrays,3TMP117. Current physical target is EPS diameter2–5mm; no levitation
or real acoustic acceptance is claimed.

Central power is independentUSB-C5V; AX7020 J10/J11 power pins are NC. Each array has
independent12V DC5.5×2.5 center-positive input and local default-off cutoff.60W path
capacity and63/68GPIO with shared2-wireI2C mux are review candidates. Actual VCCO,
continuous load, nativeCAD/ERC and external timing are unqualified.

Start with [current state](shared/PROJECT_STATE.json), [checkpoint](shared/CONTEXT_CHECKPOINT.md),
[design review](v5/docs/hardware/DESIGN_REVIEW.md), [reproduction](v5/docs/hardware/REPRODUCE.md),
[new working BOM](v5/hardware/bom/working/2026-10-11/BOM_V5_FOUR_SOURCE_20261011.xlsx),
[power](v5/docs/hardware/POWER_AND_FAIL_OFF.md), [IO/SI](v5/docs/hardware/IO_BUDGET_AND_SI.md),
[schematic status](v5/docs/hardware/SCHEMATIC_STATUS.md) and [risks](v5/docs/hardware/RISKS.md).

From PowerShell7 at repository root, create a local Python3.10/Tk venv and install
v5/requirements-lock.txt. Enter v5 and run `../.venv/Scripts/python.exe -m unittest discover -s tests -v`.
Expected current suite243 tests (original203 plus40). Full offline entry from root:
`.venv/Scripts/python.exe v5/scripts/run_nextstage.py --output v5/evidence/manual_unique`.
Set actual VIVADO_BIN/IVERILOG_BIN/CC first; use fresh output directories. This includes
3696frames×3Icarus+1XSim and existing C/AXI/calibration/safety/equivalence, temperature,
sparse calibration, runtimeGUI and C16 capture checks. [Trajectory editor guide](v5/docs/next_stage/GUI_REAL_BOARD_USER_GUIDE.md)
and [prior native BSP evidence](v5/docs/uart_resume/RESULT.md) retain their stated scopes.

Current stage ACCEPT WITH LIMITATIONS; whole physical platform REVISE; manufacturing
and procurement HOLD. No board programming/UART packets/physical cutoff or particle
motion was performed in this hardware-design iteration. UserGUI sessions and local
AX7020 material remain intact. OOC/packageDB/model tests do not prove board closure.

[Gate evidence](v5/evidence/hardware_design_20261011/), [rollback](v5/docs/hardware/ROLLBACK.md)
and the publication receipt under shared/hardware_design provide actual source/remote provenance.
Root shared/current indexes govern current work. Previous v5 documents/evidence preserve
original dates and counts; their older central-header-power/171-test/B-formal wording is
superseded by ADR042/current state, not silently altered.

Historical project is frozen and excluded from default source discovery/build/test/
packaging/IDE. Never read it or the original physical sandbox without a new explicit
history/recovery authorization. Use [current-scope search](shared/repository_cleanup/search_current.ps1).
GitHub website search indexing is not controlled by local exclusions. ExternalChatGPT
reader BLOCKED; observable Codex interaction records PARTIAL. User authorized normal
GitHub synchronization; unresolved engineering gates prevent main/production acceptance.
