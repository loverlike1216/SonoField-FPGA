# 从零操作与复现指南

本工程当前是可验证的数字/模型基线，不是可直接下载上板的 bitstream。
仓库根目录为 `E:\Codex_project\AMD-SonoField-FPGA`；运行目录为其 `v2` 子目录，已有板卡资料不要覆盖。

## 1. 确认版本与工作区

```powershell
Set-Location E:\Codex_project\AMD-SonoField-FPGA\v2
git remote -v
git branch --show-current
git status --short
git log -3 --oneline
```

Remote 应为 SonoField-FPGA，分支 main。先阅读 ../shared/CURRENT_PLAN.md、PROJECT_STATE.json、
DECISIONS.md、HANDOFF.md、BLOCKERS.md、ACCEPTANCE.md。不要覆盖已有用户改动。
远端已有仓库由用户创建，本轮在同一仓库按明确授权建立 v2，并冻结 v1；没有自动创建新 GitHub 仓库。

## 2. 安装 Python 环境

```powershell
python --version
python -m venv ..\.venv
..\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
..\.venv\Scripts\python.exe -m pip check
```

本轮使用 Python 3.10.11；锁定依赖适合该环境。无需激活 PowerShell 脚本，直接调用 venv Python。
若网络安装失败，保留 pip 错误，不得把缺依赖标为模型通过。

## 3. 确认板卡资料

```powershell
..\.venv\Scripts\python.exe scripts/audit_board.py
```

它只提取事实，输出新的 build/board_audit 下的清单及 CSV；该步骤不声称重新目视检查图片，不生成上板 XDC。
公开仓库不带原始截图时，此步骤必须先把用户合法持有的 Zynq7020 资料放回仓库根目录。
数字仿真不需要这些图片；板级验证必须需要实际板卡事实。
用户已裁决 `.const` 优先，采用其 N18 / 33 MHz。完整器件料号、VCCO、重复/缺失编号仍需补齐。

## 4. 运行声场模型

```powershell
..\.venv\Scripts\python.exe -m software.acoustic_model.visualize_field --output build/model_review
..\.venv\Scripts\python.exe -m software.acoustic_model.phase_lut_generator --output build/phase_map.csv
..\.venv\Scripts\python.exe -m software.acoustic_model.phase_lut_generator --gap-mm 115 --output build/phase_map_115mm.csv
..\.venv\Scripts\python.exe -m software.acoustic_model.export_geometry --output build/geometry_review
```

当前 config/acoustic_baseline.json 固定用户选定的 128 路平面、10 mm 名义直径、12 mm 中心距，
默认辐射面间距 100 mm。--gap-mm 允许 90..115 mm，越界拒绝；默认 z=±50 mm，原点居中。
声速、目标点可在配置中明确调整；凹面保留为研究比较，不自动替代用户机械方案。
不要把 `SIMULATION_ESTIMATE` 改成实测。图中声压为任意单位；CSV 附有假设与误差情景。
phase_map.csv 固定 128 行，下阵列从 RTL 64 开始。未安装通道 enabled=0，仍要作为完整图写入。
请求与校准分开保存。只实现 STANDING_WAVE/FOCUS，其他模式不会返回假相位图。

## 5. 一键验证

本轮工具路径：Icarus `C:\iverilog\bin`，Vivado `D:\Vivado\2025.2\2025.2\Vivado\bin`。
更换电脑时用参数覆盖，不把本机路径当成固定事实。

```powershell
..\.venv\Scripts\python.exe scripts/validate.py --iverilog-bin C:\iverilog\bin --vivado-bin D:\Vivado\2025.2\2025.2\Vivado\bin --output build/verification_review
```

预计几十秒至数分钟。输出目录包含每条命令、退出码、原始日志及 summary.json。
只有最后 `status=PASS` 才表示这组数字测试通过；必须同时有 Icarus、Python、XSim 结果。
128 路每次检查 8250 个时钟、1,056,000 个通道时刻，三次重复、两种模拟器应得到同一轨迹哈希。
额外的低带宽配置应被明确拒绝，日志中的预期非零退出不等于正常配置失败。

若只想调试软件：

```powershell
..\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## 6. Vivado 工程与综合门禁

当前无法合法填写完整 FPGA part，所以不生成伪装成真实板卡的工程。
scripts/create_project.tcl 在缺少配置时必须报 BLOCKING。原始执行记录位于 evidence/synthesis_gate/board_gate.log。
得到可信器件完整料号后，依据实际资料创建 config/verified_board.tcl，包含 PART、PART_SOURCE、
CORE_CLOCK_HZ、CLOCK_SOURCE；不要直接复制其他 Zynq 板的 part 或假定已经有 132 MHz 时钟。
然后才能执行：

```powershell
& 'D:\Vivado\2025.2\2025.2\Vivado\bin\vivado.bat' -mode batch -source scripts/create_project.tcl -tclargs config/verified_board.tcl
```

脚本只做 OOC 目标综合及报告，不能把结果叫布线时序通过。上板还需 PS/时钟 wrapper、
已验证 PACKAGE_PIN/IOSTANDARD、完整时序约束、实现、DRC、bitstream 和实物数字接口测量。

## 7. 连接真实硬件前

以 docs/architecture/V2_REQUIREMENTS.md 中正式 v2 PH0→PH6 为准，继承的 bringup.md 为历史参考。FPGA 与 TCT40 之间必须有数字接口、
电平接口和 TC4427A 功率驱动。不要把发射器接到 FPGA/595 引脚。
先单个电气表征，再双发射器，再小阵列。先小颗粒，再 5/10/25/50 mg。
硬件关闭需要独立的上电默认禁用和功率互锁；数字仿真不能证明上电/掉电/失钟安全。

## 8. 干净检出复现

target 路径相对仓库根目录，output 路径相对 v2。先提交源代码检查点，然后在全新、尚不存在的 build 子目录复现：

```powershell
..\.venv\Scripts\python.exe scripts/reproduce.py --target build/repro_review --output build/reproduction_review
```

脚本从本地 Git 稀疏检出已提交版本（工作树不含 v1），新建独立 venv，安装锁定依赖，运行完整双模拟器验证和模型，
再比较模型 CSV 的统一换行文本哈希及全部坐标/相位 CSV。输出指定目录内的 summary.json。
这验证同一 Windows 主机上的干净安装复现，不是第二块物理板或第二种操作系统。
若目标已存在，改用新的 build 子目录；脚本不会递归删除现有目录。
输出目录也必须是新的路径，脚本拒绝覆盖历史复现证据。

## 9. 常见问题

- 找不到 numpy/scipy：检查是否使用 .venv/Scripts/python.exe，以及锁文件安装是否成功。
- 找不到模拟器：覆盖对应 --*-bin 参数，确认版本。不能跳过后仍报告完整通过。
- XSim plusarg 报 `Expected a switch`：当前脚本使用 testbench 默认文件名，避免 Windows 批处理拆分等号。
- 日志出现 `The system cannot find the path specified`：本机 Vivado launcher 有此启动提示；继续检查实际
  子工具退出码、编译/展开错误、PASS 标记和 trace。不能仅据提示忽略真正失败。
- COMMIT 不接受：必须每个通道写过、没有 pending、WRITE 和 COMMIT 不能同拍。
- 33 MHz 集成序列器被拒绝：这是预期带宽保护；33 MHz 核心可工作，但该 32-lane 序列配置需更快核心时钟。
- 测试通过仍不能悬浮：数字时序不等于声学/功率/机械闭环；按根因清单检查并保留失败实测。

## v2 migration and BOM audit

Run `python scripts/check_migration.py`, `python scripts/audit_bom.py` and `python scripts/check_repository.py`.
The first audit checks immutable parent Git objects and local bytes when v1 is present. A sparse clone
can validate parent provenance without a v1 directory. BOM audit compares all nonempty source cells to CSV
using an independent reader. Imported prices/stock and electrical claims are not independently verified.


## v2 self-calibration reproduction

From v2 with the existing Python environment:

```powershell
..\.venv\Scripts\python.exe scripts/generate_system.py --check
..\.venv\Scripts\python.exe -m software.calibration.experiment --output build/calibration_review
..\.venv\Scripts\python.exe scripts/self_calibration_gate.py --output build/calibration_gate_review
..\.venv\Scripts\python.exe scripts/validate.py --output build/full_review
```

The full validation command includes the dedicated calibration gate; do not run both for routine
reproduction. The separate command is for targeted debug. Expect 45 Python tests, inherited TBs,
CAL-TB01..15, byte-identical ADC roundtrips, three JSON/CSV repeats, and explicit noise failures.
800 kSPS/132 MHz is a simulation profile, not a board clock assertion. `--skip-xsim` marks PARTIAL.
The raw calibration cube is ~65 MB and stays under build; 1024 frames per capture fit 16 KiB PL RAM.
The fresh-clone script also executes this full gate without any v1 working directory.

Register semantics and real-hardware prerequisites: docs/hardware/PCB_SOFTWARE_INTERFACE.md.
Invalid profile/unknown phase reference must fail; do not remove guards to produce a hardware LUT.
