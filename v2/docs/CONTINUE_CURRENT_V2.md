# 当前 v2 接手补充 — 2026-10-03

当前记录模型：GPT-6.1 Sol High，依据用户手动选择声明。正式工程为 SonoField-FPGA，main，v2；阶段仍为 CORE_TIMING_CLOSURE_AND_REAL_PS_PL_SMOKE_TEST。本文件补充根目录《指南.md》的历史交接点，以当前 main 的状态和证据继续单块 Robei 八角板 Zynq-7020 声场控制。

首先阅读 [当前检查点](../../shared/CONTEXT_CHECKPOINT.md)、[机器状态](../../shared/PROJECT_STATE.json)、[当前计划](../../shared/CURRENT_PLAN.md) 和 [完整工程报告](../evidence/core_timing_real_loop/RESULT.md)。CP-20261003-001 的工程源码提交为 d6851070ca5aa98c95c2a6fd3f0344b78e799a9a；之后的检查点提交仅更新文档、状态和审计记录，不改变已经验证的工程源码。

当前证据：114 项 Python 测试通过，三次 Icarus 和一次 Vivado 2025.2 XSim 的 3,696 帧轨迹及相位图/声场报告/ACK 哈希一致；校准、ADC 和继承回归通过；所有保存轨迹点为 TRAP_VALID。这是数字仿真证据。界面保存当前预览而非实际执行轨迹的问题已修复，失败输出保留在独立目录。

上板门禁仍未通过：第二轮 OOC 布线后 WNS −4.515 ns、TNS −6007.936 ns、WHS +0.070 ns、THS 0。工程使用用户批准的保守 xc7z020clg400-1 假设，实际速度/温度等级未知。真实 UART 到 PS 的连接、PS preset、XSA、BSP 和目标 ARM 构建仍缺少证据。阶段结果 REVISE。不得下载当前失败设计或启用外部负载。

接手时用 PowerShell 7（pwsh）。依根目录《指南.md》的环境和稀疏检出步骤安装依赖，获取当前 main；历史标签只用于重现对应历史交接点。每台机器自行配置实际工具安装路径和 COM，不复制作者机器的端口号。进入项目根目录后可执行：

```powershell
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
.\.venv\Scripts\python.exe v2\scripts\check_repository.py
.\.venv\Scripts\python.exe AI-interaction-memory\tools\sync_codex.py --check
Set-Location v2
..\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

完整仿真在设置实际 VIVADO_BIN、IVERILOG_BIN 和 CC 后，从项目根执行以下命令，使用新的输出目录以保留旧失败：

```powershell
.\.venv\Scripts\python.exe v2\scripts\motion_gate.py --output build/colleague_motion_gate
.\.venv\Scripts\python.exe v2\scripts\board_transport_gate.py --output build/colleague_axi_gate
```

motion_gate 会实际启动仿真界面并运行多次轨迹，需要可用桌面会话；通过标准为退出码 0 和对应 summary.json 的 PASS，不能仅凭界面打开判断。board_transport_gate 输出的 axi_bridge_tests.json 只证明离线协议和 RTL 测试。

后续先审查 [P-20260929-001](../../AI-problem/problem/P-20260929-001__queue-control-timing.md) 的量化队列/使能/复位时序方案。前一合同允许的两轮 RTL 重构已经用完，该文件仍是待决策提案。获得适用决策后继续当前 v2，保持 128 路、8 bit、独立请求/校准、原子提交、频率范围和安全行为。真实布线门禁通过且 PS/UART 事实齐备后，再进行无外部负载的安全通信验证；驱动和换能器实测随后推进。

当前 [可观察交互索引](../../AI-interaction-memory/INDEX.md) 和 [模型切换记录](../../AI-interaction-memory/codex/I-20261003-0001__model-transition.md) 可追溯。外部 ChatGPT 对话仍无法直接访问，状态 BLOCKED；Codex 可见交互覆盖 PARTIAL，不把摘要或模型推断当作原始历史。
