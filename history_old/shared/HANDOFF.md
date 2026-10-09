# AX7020 v5 交接 — 2026-10-09

模型：GPT-6.1 Sol High（用户声明）。基准 HEAD：4dc8e765403561e9aff9980a54390cdbb01ea0ed。检查点 CP-20261009-001；Stage AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT；版本 v5 未变。

## Goal / Inputs

核验连接的 AX7020，保留既有基线，形成独立 BOM 修订与三板准备。已读当前治理/证据、正式用户附件、实板照片、72 行原始 BOM、原厂器件资料和固定 ALINX XSA。

## Changes

只读脚本/脱敏证据；保留未知字段的 board_facts；BOM 工作副本和 72 行审查；63 GPIO/ADC/安全/电源/时序候选；当前状态/计划/阻塞/检查点/AI 记录。没有核心 RTL、旧历史或原生 PCB 改动。

## Tests / Evidence

完整数字基线 PASS；15 个候选检查 PASS；ADC256帧 Icarus+XSim PASS；Vivado68球位 Bank 核验 PASS；BOM 原件 Hash、公式、缓存与预览 PASS。结果入口 v5/evidence/board_bringup/20261009/RESULT.md，完整数字结果在 evidence/baseline/board_integration_20261009/summary.json。

## Failures / Limits

包脚审查首次缺少 open design，修复输入后 PASS；XSim drive-path 参数首次失败，使用本地向量文件后同一 TB PASS；原厂 PDF 首次截断后完整重试。失败记录保留于 execution_failures.json 及对应日志。

实板只有 JTAG/三个 PS 寄存器读取。已有 PL DONE、双 CPU Running、SD boot 保持原样；XADC 无有效测量。DDR RAM/UART/PS→AXI→PL/模拟采样/安全/声学 NOT_RUN。原生 ERC NOT_RUN。

## Unresolved / Next

补全 Rev3 PS/DDR/时钟/IO、完整等级/VCCO、当前程序可用内存说明；连接 UART，资格确认 ARM BSP/工具链。独立审核 ADC/安全/浪涌，测 TX/RX。候选原理图准备可审阅，制造 HOLD。恢复时以 CONTEXT_CHECKPOINT 和最新 GitHub 回执为入口，不绕过门禁。
