---
checkpoint_id: CP-20261009-001
project_id: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
branch: main
base_commit: 4dc8e765403561e9aff9980a54390cdbb01ea0ed
head_commit: 4dc8e765403561e9aff9980a54390cdbb01ea0ed
active_version: v5
version_status: ACTIVE
current_stage: AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT
created_at: 2026-10-09T02:16:17.071733+00:00
created_by: Codex
checkpoint_reason: Real read-only board/BOM/candidate/regression milestone
source_of_truth: repository
status: VALID
model: GPT-6.1 Sol High
---

# Context Checkpoint — AX7020 v5

## 1. 当前身份

SONOFIELD_FPGA / SonoField-FPGA；仓库 https://github.com/loverlike1216/SonoField-FPGA.git；工作区 E:\Codex_project\AMD-SonoField-FPGA；main；唯一活动版本 v5；Stage AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT。模型记录 GPT-6.1 Sol High（用户声明）。

本检查点生成时的代码基准 HEAD 为 `4dc8e765403561e9aff9980a54390cdbb01ea0ed`，描述本次已审阅但尚未提交的证据与文件改动。检查点所在 commit 由推送后回执记录，不伪造自引用 Hash。

## 2. 当前目标

构建 128 通道、40 kHz 空气超声声场平台。50 mg 是分阶段最终实物目标，未证明悬浮。本阶段完成 AX7020 只读识别、板级配置核对、独立 BOM 修订与三板原理图准备，保持板上既有程序。

## 3. 正式架构

Host 声场/轨迹 → PS 传输与 C 服务 → AXI PL → 128 TX 共同时基、8 bit requested/calibration 独立相位与原子提交 → 32 lanes、每 lane 使用 4 个输出 → 后续经资格验证的驱动器。8 RX 的 ADC/校准反馈目前为数字仿真。核心架构、寄存器、协议、运动参数和验收阈值保持不变。

## 4. 已完成，按证据区分

- HARDWARE_VERIFIED，仅限识别/只读寄存器：AX701020.3.0、XC7Z020 JTAG 0x23727093、CLG400 照片、ARM DAP、既有 PL DONE 与双 CPU Running、SD 启动；读取三个 PS 控制寄存器。
- SIMULATED：115 Python 测试、3696 帧×三次 Icarus/一次 XSim、波形/校准/C/AXI/安全/黄金等价回归通过；ADC 候选 256 帧/两个模拟器通过。
- TESTED，离线范围：15 项候选检查；原始 BOM Hash 不变、工作副本重算/视觉检查；72 行封装状态审查；完整 80 针/63 GPIO 候选及 68 球位 Bank 核验。
- SYNTHESIZED：此前 v5 文档器件 OOC 综合保留原日期和范围。本次未改核心 RTL，没有新增整板综合、布线、bitstream 或部署结果。

## 5. 计划位置

全部当前安全可执行的识别、离线候选、BOM 和数字回归已完成；提交、推送并核验远端后，转入板级事实补全。CURRENT_PLAN.md 是执行入口。

## 6. 下一步

1. 获得厂家 Rev3 匹配的 PS/DDR/时钟/IO 资料、完整 FPGA 等级和 VCCO；明确当前 SD 程序与可安全使用的 CPU/RAM 范围。
2. 连接板上 UART 口、确认 CP2102/COM；资格确认 ARM BSP/编译器，再执行无外部负载的临时 PL/PS/DDR/UART/AXI 测试。
3. 对 ADC、关断/重新使能、浪涌、RX AFE、外部时序做独立 Review；获取 TX/RX 厂商数据与样品，决定正式 ADC 换型。
4. 连接真实 v5 EasyEDA 工程后建立候选原理图、网表/BOM 对账并实际运行 ERC。制造保持 HOLD。

## 7. 有效决策

ADR-035：用户明确批准 AX7020 v5；ADR-036：本轮只读资格确认与原件保留的候选实施边界。来源为实际用户附件、照片与工具输出，没有伪造 ChatGPT Decision。

## 8. 阻塞与严重问题

V5-B01 部分解决；V5-B03/B04/B05/BOM_REVIEW 未关闭。当前运行镜像所有权、Rev3 匹配 PS 配置、完整等级、VCCO、真实 UART、目标 ARM 工具链、外部电气/声学与原生 EDA 工程仍缺失。独立 Review 待执行，外部 ChatGPT 读取 BLOCKED。已知 Critical 软件缺陷为零不代表硬件可放行。

## 9. 最新验证

日期 2026-10-09。`v5/evidence/baseline/board_integration_20261009/summary.json` 为完整数字结果；`v5/evidence/board_bringup/20261009/` 保存真实只读日志、summary、candidate_checks、ADC Icarus/XSim、包脚数据库和来源 Hash。日志的失败与重试分开保留，不能用自述替代工具结果。

## 10. 已知限制

DDR 控制器的 32 bit 配置不证明物理容量或稳定性；实际 DDR RAM/UART/PS→AXI→PL/ADC/安全/温升/声场未测试。XADC 返回无效值。公开 V2.0 原理图与实板 Rev3、Hynix 手册与 Micron 预设尚未匹配。原生 v5 原理图 NOT_CREATED / ERC NOT_RUN；ADC 正式替换未批准。

## 11. Do Not Change

保持冻结历史、原始 BOM 和当前运行镜像；不改 128TX/8RX/32lanes×4used/8bit/共同时基/校准分离/原子提交/协议/寄存器/运动/几何/阈值。无 v6，无永久存储/启动/驱动变更，无未知 GPIO，无制造。

## 12. Invariants

132 MHz 为内部目标，区别于原厂 50 MHz 物理参考。上下板各自独立供电，AX7020 不通过 GPIO 接口给 TX 供电。坐标采用辐射面中心、12 mm pitch、100 mm nominal/90–115 mm 可调间距与几何中心原点。候选不会因离线 PASS 自动成为生产实现。

## 13. Open AI Problems

P-20261008-001：ADC 带宽/正式选择；P-20261009-001：Rev3 PS 平台与现有镜像安全工作区。未收到外部 ChatGPT Decision。Codex 可观察交互记录 PARTIAL，仅保存可见人机消息和工具索引，不保存隐藏推理。

## 14. 相对上一检查点的增量

新增真实板卡身份/既有运行状态、BOM 工作副本、ADC/安全/电源/时序/GPIO 候选、当前完整数字回归和新 Problem。旧 v5 等价日志因自动回归被覆盖后，已将新日志另归档并恢复原字节。预存用户改动不加入本次提交。

## 15. 恢复指令

先读 README/AGENTS、PROJECT_STATE、VERSION_STATE、本检查点、CURRENT_PLAN、DECISIONS、BLOCKERS、ACCEPTANCE 与最新证据；核对 Git status/HEAD/远端回执。继续 v5 板级资格验证，不导入旧板 COM、引脚、512 MiB 或 FT2232 结论。

## 16. 证据索引

实板结果：`v5/evidence/board_bringup/20261009/RESULT.md`；BOM：`v5/hardware/bom/working/2026-10-09/`；三板准备：`v5/hardware/integration_candidates/20261009/`。原始照片、完整设备身份、桌面截图和厂商原文件仅本地 local_raw，公开副本经过脱敏并附原始/公开 Hash。

## 17. 来源与冲突处理

依据真实仓库基准、用户附件 4b78522d、Revision3.0 回答及照片、固定 ALINX 提交 fcf1e4a、Windows/Vivado/XSDB 2025.2、原厂资料和实际回归。

上一阶段“没有访问硬件”属于整理任务历史。本次用户明确授权检测，当前只读工具证据更新当前状态。历史 Robei 事实不迁移为 AX7020 事实；原理图版本和 DDR 预设差异保留 OPEN，不能凭推理升级为确认。
