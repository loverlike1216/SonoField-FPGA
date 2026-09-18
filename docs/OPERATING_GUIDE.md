# 从零操作与复现指南

本工程当前是可验证的数字/模型基线，不是可直接下载上板的 bitstream。
工作目录必须为用户指定的 `E:\Codex-project\AMD-SonoField-FPGA`，已有板卡资料不要覆盖。

## 1. 确认版本与工作区

```powershell
Set-Location E:\Codex-project\AMD-SonoField-FPGA
git remote -v
git branch --show-current
git status --short
git log -3 --oneline
```

Remote 应为 SonoField-FPGA，分支 main。先阅读 shared/CURRENT_PLAN.md、PROJECT_STATE.json、
DECISIONS.md、HANDOFF.md、BLOCKERS.md、ACCEPTANCE.md。不要覆盖已有用户改动。
远端已有仓库由用户创建，本轮只关联并取回最初 README；没有自动创建新 GitHub 仓库。

## 2. 安装 Python 环境

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe -m pip check
```

本轮使用 Python 3.10.11；锁定依赖适合该环境。无需激活 PowerShell 脚本，直接调用 venv Python。
若网络安装失败，保留 pip 错误，不得把缺依赖标为模型通过。

## 3. 确认板卡资料

```powershell
.\.venv\Scripts\python.exe scripts/audit_board.py
```

它只提取事实，输出 evidence/preflight 下的清单及 CSV，不生成上板 XDC。
公开仓库不带原始截图时，此步骤必须先把用户合法持有的 Zynq7020 资料放回本地。
数字仿真不需要这些图片；板级验证必须需要实际板卡事实。
用户已裁决 `.const` 优先，采用其 N18 / 33 MHz。完整器件料号、VCCO、重复/缺失编号仍需补齐。

## 4. 运行声场模型

```powershell
.\.venv\Scripts\python.exe -m software.acoustic_model.visualize_field --output build/model_review
.\.venv\Scripts\python.exe -m software.acoustic_model.phase_lut_generator --output build/phase_map.csv
```

修改 config/acoustic_baseline.json 可调阵元数量、平面/凹面、间距、曲率、声速和目标点。
不要把 `SIMULATION_ESTIMATE` 改成实测。图中声压为任意单位；CSV 附有假设与误差情景。
phase_map.csv 固定 128 行，下阵列从 RTL 64 开始。未安装通道 enabled=0，仍要作为完整图写入。
请求与校准分开保存。只实现 STANDING_WAVE/FOCUS，其他模式不会返回假相位图。

## 5. 一键验证

本轮工具路径：Icarus `C:\iverilog\bin`，Vivado `D:\Vivado\2025.2\2025.2\Vivado\bin`。
更换电脑时用参数覆盖，不把本机路径当成固定事实。

```powershell
.\.venv\Scripts\python.exe scripts/validate.py --iverilog-bin C:\iverilog\bin --vivado-bin D:\Vivado\2025.2\2025.2\Vivado\bin --output build/verification_review
```

预计几十秒至数分钟。输出目录包含每条命令、退出码、原始日志及 summary.json。
只有最后 `status=PASS` 才表示这组数字测试通过；必须同时有 Icarus、Python、XSim 结果。
128 路每次检查 8250 个时钟、1,056,000 个通道时刻，三次重复、两种模拟器应得到同一轨迹哈希。
额外的低带宽配置应被明确拒绝，日志中的预期非零退出不等于正常配置失败。

若只想调试软件：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## 6. Vivado 工程与综合门禁

当前无法合法填写完整 FPGA part，所以不生成伪装成真实板卡的工程。
scripts/create_project.tcl 在缺少配置时必须报 BLOCKING。原始执行记录位于 evidence/synthesis/board_gate.log。
得到可信器件完整料号后，依据实际资料创建 config/verified_board.tcl，包含 PART、PART_SOURCE、
CORE_CLOCK_HZ、CLOCK_SOURCE；不要直接复制其他 Zynq 板的 part 或假定已经有 132 MHz 时钟。
然后才能执行：

```powershell
& 'D:\Vivado\2025.2\2025.2\Vivado\bin\vivado.bat' -mode batch -source scripts/create_project.tcl -tclargs config/verified_board.tcl
```

脚本只做 OOC 目标综合及报告，不能把结果叫布线时序通过。上板还需 PS/时钟 wrapper、
已验证 PACKAGE_PIN/IOSTANDARD、完整时序约束、实现、DRC、bitstream 和实物数字接口测量。

## 7. 连接真实硬件前

依次完成 docs/experiments/bringup.md 的 PH0→PH8。FPGA 与 TCT40 之间必须有数字接口、
门极/电平驱动和功率级。不要把发射器接到 FPGA/595 引脚。
先单个电气表征，再双发射器，再小阵列。先小颗粒，再 5/10/25/50 mg。
硬件关闭需要独立的上电默认禁用和功率互锁；数字仿真不能证明上电/掉电/失钟安全。

## 8. 常见问题

- 找不到 numpy/scipy：检查是否使用 .venv/Scripts/python.exe，以及锁文件安装是否成功。
- 找不到模拟器：覆盖对应 --*-bin 参数，确认版本。不能跳过后仍报告完整通过。
- XSim plusarg 报 `Expected a switch`：当前脚本使用 testbench 默认文件名，避免 Windows 批处理拆分等号。
- 日志出现 `The system cannot find the path specified`：本机 Vivado launcher 有此启动提示；继续检查实际
  子工具退出码、编译/展开错误、PASS 标记和 trace。不能仅据提示忽略真正失败。
- COMMIT 不接受：必须每个通道写过、没有 pending、WRITE 和 COMMIT 不能同拍。
- 33 MHz 集成序列器被拒绝：这是预期带宽保护；33 MHz 核心可工作，但该 32-lane 序列配置需更快核心时钟。
- 测试通过仍不能悬浮：数字时序不等于声学/功率/机械闭环；按根因清单检查并保留失败实测。
