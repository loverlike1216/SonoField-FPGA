# SonoField-FPGA v5 — PCB 独立 Codex 任务线启动

## 一、身份与任务定义

本 Codex 对话正式作为 SonoField-FPGA 的 PCB 专项工程执行任务线。

TASK_NAME：`SonoField-FPGA-PCB`

PROJECT_ID：`SONOFIELD_FPGA`

Repository：`https://github.com/loverlike1216/SonoField-FPGA`

Active Version：`v5`

Target Board：`ALINX AX7020 Rev3.0`

EDA：嘉立创 EDA 专业版

Toolchain：`Vivado 2025.2 / Vitis 2025.2`

本次不是建立新项目，也不允许创建新的正式 GitHub Repository。

继续当前 v5，不得擅自开启 v6。

本任务线专门负责 PCB 硬件的工程实现、验证、测试和证据管理。

原 Codex 主开发任务线继续负责 RTL、PS/PL、AXI、通信、运动算法和系统联调。

两条任务线共享同一个 GitHub 工程事实源，但必须避免直接修改彼此正在开发的文件。

---

## 二、先执行 Repository 恢复

在任何 Git 修改之前，首先只读检查现有 Repository。

记录：

- 实际工作目录。
- Repository URL。
- 当前 Git branch。
- HEAD Commit。
- Git status。
- 当前活动版本。
- 当前开发 Stage。
- 最新 Draft PR。
- 已完成及未完成的测试。
- 当前硬件相关 Blockers。

上一轮 GitHub 记录的工作区为：

`E:\Codex_project\AMD_Sonofield`

但必须以本机实际 Git 根目录为准，不应直接假设其他历史路径仍然有效。

优先读取：

- README.md。
- AGENTS.md。
- shared/PROJECT_STATE。
- shared/VERSION_STATE。
- shared/CONTEXT_CHECKPOINT。
- shared/CURRENT_PLAN。
- shared/DECISIONS。
- shared/ACCEPTANCE。
- shared/BLOCKERS。
- AI-problem/problem。
- AI-problem/decision。
- v5/hardware。
- v5/config。
- v5/docs/next_stage。
- v5 现有 PCB、BOM、IO 和 ADC 资料。

必须确认已获得用户批准的 AD7606C-16 换型决策。

并核对当前 PR #4 及其基于 PR #3 的实际依赖关系。

不得因为 main 较旧而丢失未合并的 v5 功能。

---

## 三、Git Worktree 隔离方案

本任务采用：

**一个正式 Repository + 两个独立工作目录 + 两条开发分支。**

主任务线保留原工作区。

PCB 专项使用独立 Git Worktree。

建议分支名称：

`feat/v5-pcb-design`

建议工作目录候选：

`E:\Codex_project\AMD_Sonofield_PCB_v5`

此路径仅为建议值。由于用户尚未单独指定 PCB Worktree 的最终绝对路径，执行前先核对原仓库位置和目标目录是否空闲，再提交建议路径供用户确认。

在用户确认新工作目录之前，不得擅自创建或迁移正式 PCB Worktree。

### 3.1 Worktree 创建原则

在路径获批后：

1. 检查原始 Repository 是否干净。
2. 检查是否已有相同分支或 Worktree。
3. 读取当前 PR #4 最新有效提交。
4. 以审核后的最新 v5 集成基线创建 PCB 分支。
5. 使用 git worktree 创建独立目录。
6. 确认 Worktree 指向同一个 Git Repository。
7. 检查 Git 状态和源码完整性。
8. 运行基线测试。

不得使用第二次普通 git clone 冒充共用工作树，也不要在原工作树内部嵌套另一套未经隔离的 .git 仓库。

不修改原主线工作区，不触碰冻结历史版本。

### 3.2 主线与 PCB 任务线的文件职责

PCB 专项优先允许修改：

- v5/hardware/pcb/
- v5/hardware/bom/
- v5/hardware/next_stage/
- v5 与 PCB 相关的设计文档
- PCB 原理图、元件库和封装
- PCB 接口、供电及机械约束
- PCB 验证脚本与 Evidence
- PCB 专项索引和任务状态

避免直接修改：

- RTL 核心模块。
- PS/PL 正式控制代码。
- 运动控制算法。
- 主线测试 Goldens。
- AXI 正式协议。
- 未经审查的生产 XDC。
- 冻结的历史版本。

如果 PCB 设计必须改变 FPGA IO 或控制接口：

先生成接口变更提案，说明原因、信号数量、电压、引脚、RTL 影响和验证要求。

由 PCB ChatGPT 窗口分析，再交主窗口审核接口合同。

只有经过批准的接口变更，才能协调修改主线。

---

## 四、共享工程事实与状态同步

继续沿用 Repository 的：

- shared/PROJECT_STATE。
- shared/VERSION_STATE。
- shared/CURRENT_PLAN。
- shared/DECISIONS。
- shared/ACCEPTANCE。
- shared/BLOCKERS。
- shared/CONTEXT_CHECKPOINT。
- AI-problem/problem。
- AI-problem/decision。
- AI-chat-memory。

建议建立独立 PCB 专项状态：

`v5/hardware/pcb/PCB_PROJECT_STATE.md`

或者使用当前 Repository 已有的 PCB 状态文件，不重复创建同类文件。

PCB 专项文件记录：

- PCB 当前 Stage。
- 硬件架构版本。
- IO 分配状态。
- BOM 状态。
- 电源设计状态。
- 原理图状态。
- ERC 结果。
- 尚未完成的电气验证。
- 当前阻塞。
- 下一步行动。

正式共享状态由 Codex 在完成 Repository 对账之后受控更新，避免两条任务线同时覆盖同一个 shared 文件。

必要时通过独立提交、审核后的合并或小范围变更同步。

---

## 五、正式 PCB 硬件要求

### 5.1 三 PCB 系统

中央接口采集 PCB ×1：

- AX7020 J10/J11。
- 独立 USB Type-C 供电。
- 1×AD7606C-16。
- 八路同步接收。
- 时钟和控制信号分配。
- I²C 管理。
- 环境 TMP117。
- 电源和安全监测。

上阵列 PCB ×1：

- 64T + 4R。
- 12mm 网格。
- 正面 TX/RX。
- 背面外部延伸区安排驱动和处理电路。
- 独立 12V 电源。

下阵列 PCB ×1：

- 与上阵列对称。

完整系统为：

`128T + 8R + AD7606C-16 + 3TMP117 + AX7020`

### 5.2 固定供电接口

中央板：

- USB-C。
- 优先 5V/3A。

上下阵列分别：

- DC 5.5×2.5mm。
- 12V。
- 额定电流选型范围 1～5A。
- 优先评估 40W。
- 必要时评估 60W。
- 上下分别使用独立适配器。

适配器和 PCB 插座的具体 MPN、中心极性、插入深度、电流额定及温度降额必须匹配。

功率余量：

- 最低 20%。
- 目标 30%。
- 不允许低于 20%。

本阶段依据原厂资料和理论最坏工况计算，不要求用户立即开展实际功率测试；未经实测的共振负载损耗不得伪称确定值。

### 5.3 阵列空间

每块板采用 10×10 虚拟网格：

- 内圈 8×8 共 64T。
- 外围四个顶角 4R。
- 其他外围位置留空。
- 阵元中心横纵间距 12mm。
- RX 位于 (±54mm, ±54mm)。

上下板标称辐射面间距 100mm，可调 90～115mm。

正面仅安装换能器，主要处理模块放在阵列投影区域以外的背面延伸区。

### 5.4 必须实现的硬件功能

- 128 路独立相位驱动。
- 32-lane 数据接口。
- 66MHz 候选移位时钟。
- CLK/LATCH/OE/SYNC。
- 8 路 RX AFE。
- AD7606C-16 高带宽采样。
- 3 颗 TMP117 温度补偿输入。
- INA226 电源监测。
- I²C 总线优化与隔离。
- 上下阵列独立供电。
- 硬件看门狗。
- 硬件急停。
- 故障关闭与受控重新使能。
- 防倒灌、过流、过压、欠压、温度保护。

正式演示目标为直径 2～5mm 的 EPS 小球，原 50mg 目标不再作为当前需求。

---

## 六、PCB 开发任务阶段

### PCB-S1：工程资料审计

读取用户提供的：

- AX7020 V2.0 原理图。
- AX7020 V3.0 手册。
- AX7020 官方硬件资料。
- NU40C10T/R 参数。
- AD7606C-16 数据手册。
- 当前 v5 BOM 与三板接口合同。

对于 V2/V3，记录厂家已说明硬件一致、V3 手册修改部分定义的事实，并据此开展交叉核对。

先输出当前设计与缺失资料情况。

### PCB-S2：IO 分配优化

重新核对 J10/J11 的 68 根 PL IO。

重点：

- 上下 16+16 DATA。
- ADC 四路 DOUT 集中。
- I²C 总线复用与故障隔离。
- CLK/LATCH/OE/SYNC。
- PGOOD/FAULT。
- 电源域与逻辑电平。
- 备用 IO。

必须形成完整：

`PACKAGE_PIN → J10/J11 → 中央PCB → 阵列PCB → 终端器件`

对应表。

完成逻辑、电气和 Vivado 约束两轮审核。

### PCB-S3：电源、安全和模拟电路

完成：

- 中央 USB-C 电源。
- 上下独立 12V 供电。
- DC 适配器和插座选型。
- 稳压器。
- TVS/eFuse/Fuse。
- 反接和反向电流保护。
- 真实硬件驱动关断。
- TC4427A 驱动拓扑审核。
- ADC 模拟前端。
- 温度、电流监测和电气隔离。

所有电源轨需要理论预算和余量说明。

### PCB-S4：关键 BOM 基线

更新：

- 中央 PCB BOM。
- 上阵列 BOM。
- 下阵列 BOM。
- 系统适配器/线束/机械件 BOM。
- 总 BOM。

要求 MPN、数量、电压、电流、功耗、封装、原厂资料和采购状态均可追溯。

正式器件的采购数量应与三板原理图一致。

### PCB-S5：嘉立创 EDA 原理图

在实际可用的嘉立创 EDA 专业版环境中完成候选原理图。

要求：

- 全部核心功能模块。
- 准确的元件引脚。
- 规范的网络标签。
- 三板接口一致。
- 完整的电源和安全电路。
- 正确的原理图库和封装。
- 实际 ERC。
- 电气与接口 Review。

如果没有可用的原生 EDA 能力，明确说明工具限制，不允许生成伪原理图或假 ERC 结果。

### PCB-S6：回归与独立验证

检查：

- 现有数字功能未回归。
- FPGA IO 与硬件设计一致。
- 电源预算满足最低 20% 余量。
- 电路默认安全关闭。
- ADC 和 AFE 满足设计要求。
- 阵列机械坐标正确。
- BOM 与原理图逐项对应。
- ERC 与独立电气 Review。
- 最新证据真实可复现。

### PCB-S7：GitHub 交付

保存：

- 原生原理图。
- 完整 BOM。
- IO 映射。
- 电源预算。
- 关键原厂资料索引。
- 电气审核。
- ERC 报告。
- 设计决策。
- 未关闭的 Blockers。
- CONTEXT_CHECKPOINT。

提交至 PCB 独立分支。

需要时创建 Draft PR，基于经确认的当前 v5 集成分支，避免未合并开发成果丢失。

不可未经用户批准合并到 main。

---

## 七、质量门禁

以下情况不能宣布 PCB 设计完成：

- 关键器件没有准确型号。
- 保护电路没有形成完整闭环。
- IO 和 XDC 不一致。
- 电源预算缺少重要负载。
- ADC 参考、输入或高带宽配置存在缺陷。
- 上下阵列连接方向不一致。
- 原理图缺少必要的无源器件。
- ERC 未真实运行。
- BOM 与原理图数量不一致。
- 依赖伪造的测试或占位模块。
- 出现未说明的电气风险。

没有真实样机时，物理声压、真实功耗、温升及悬浮效果仍为 NOT_RUN。

本次不允许自动生产 Gerber、制造订单或正式采购。

---

## 八、首次启动时立即执行的工作

首次启动先执行：

1. 只读检查 GitHub 和本地 Repository。
2. 确认主任务线与 PCB 任务线的隔离方式。
3. 检查 Git Worktree 建立条件。
4. 读取当前 v5 硬件设计事实。
5. 识别已经确定和仍然开放的硬件决策。
6. 明确 PCB 文件管理范围。
7. 列出 PCB-S1 的可执行任务。
8. 提交候选 Worktree 位置、分支基线和启动检查结果。

在用户确认新 Worktree 路径后，才执行正式隔离创建和 PCB-S1 开发。

本次不直接修改 FPGA 核心 RTL，也不自动合并任何已有 Draft PR。

最终初始报告要求给出：

- Repository、Branch、Commit。
- 当前 v5 状态。
- PCB Worktree 的拟定位置及是否已获批准。
- PCB 资料完整情况。
- 最新 BOM 与 IO 状态。
- 当前 Blockers。
- 下一阶段具体动作。

**任务原则：PCB 支线独立执行、共享 GitHub 事实、同步正式决策、保护已有数字基线，最终通过主窗口和用户审核实现完整系统集成。**