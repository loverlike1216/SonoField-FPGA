# SonoField-FPGA v5 — AX7020 三板硬件定型、供电、IO、BOM、嘉立创原理图：Codex 正式执行指令

> **交付时间**：2026-10-11  
> **执行代理**：Codex（可选择 GPT-6.1 Sol Extra High）  
> **任务性质**：继续现有 `v5`，硬件架构落地与制造前候选工程，不是版本升级或正式制造许可。  
> **主控**：ALINX AX7020 Rev3.0 / XC7Z020；实际完整芯片标识/Bank 电压须实证核验。  
> **工具链**：Vivado/Vitis 2025.2；PCB：嘉立创 EDA 专业版。  
> **当前目标**：上下各 64 个 NU40C10T、各 4 个匹配 RX、中央 1 颗 AD7606C-16、TMP117×3；首先实现直径 **2–5 mm EPS 小球**的稳定悬浮和可编程移动；1 mm 液滴与更大负载属于未来探索，不在本次硬件候选验收内。  
> **用户指定资料目录**：`E:\Codex_project\AMD_Sonofield\AX7020`（由 Codex 在 Windows 主机上实际枚举、校验；ChatGPT 未直接访问该本地路径）。

## 0. 一键启动总指令

在已授权的当前 v5 工作区执行本文件的 Gate 0–Gate 7。你应先恢复 Repository 的真实事实，再完成本阶段全部**离线可验证**的理论预算、引脚/网表合同、电源/安全电路、原生原理图（工具可用时）、BOM 与交叉验证。普通代码/原理图工具问题自行有限闭环；未取得 Rev3 实板匹配资料或关键电气数据时，保留 `HOLD` 和证据，不得猜测数据、绕过 ERC/DRC 或假称可制造。不得在本任务中未经明确许可合并 `main`、采购、下单、下载比特流、修改未知板上程序、启用超声输出或进入 v6。

---

## 1. Goal / Scope / Non-Goals

### Goal

交付一套可独立审查、可重复生成、与当前 AX7020 v5 RTL/固件/上位机一致的**三 PCB 原理图候选与完整采购审核 BOM**，实现：

- 中央 PCB 自身 **USB-C 5 V / 最多 3 A，独立供电**；与 AX7020 J10/J11 的供电轨隔离，只连接必要数字信号和经过设计的参考地。
- 上、下阵列 PCB 每块各有一个独立 **DC 5.5×2.5 mm / 12 V** 电源入口、各自 eFuse/保护/使能/温度/电流监测、硬件默认 OFF。
- AX7020 通过 J10/J11 **仅提供数据与控制**；不从 FPGA/开发板电源向阵列驱动负载供电。
- 128TX / 8RX / 32 parallel serial lanes ×4 used outputs / 8bit requested+calibration / atomic phase commit / shared timebase 不被破坏。
- 中央一颗 AD7606C-16，8 路同步采集和软件高带宽初始化/读回，八路 RX AFE 靠近各自换能器。
- 三颗 TMP117（中央环境/上阵列/下阵列）进入声速传播积分和相位补偿；可选湿度保留 DNP。
- 10×10 虚拟几何网格：内部 8×8 TX、外圈四角 RX，12 mm pitch；两辐射面名义 100 mm，可调 90–115 mm。
- 可用于下一轮单通道、少通道、电气安全、ADC、全阵列和声场调试的测试点、线束、互锁、调试文件齐备。

### Scope

架构研究、Datasheet 比较、理论最坏功率模型、选择决策/约束、可复现计算脚本、全网表/接口合同、针脚逐点审核、正式 BOM 工作表、原生 EasyEDA 原理图和真实 ERC（有工具时）、全部可运行 FPGA/软件回归与资料同步。

### Non-Goals

不得制造/采购、自动生成生产 Gerber、修改冻结版本或 `Historical project/`、启用真实超声阵列、证明实际 2–5 mm EPS 悬浮、以仿真取代真实功耗/温升/AFE/声压/绝缘/EMC 证据；不擅自改变目标、主 Repository、版本或已经过用户批准的核心架构。已连接 JTAG/UART 不代表可以停止、复位、下载或写入板上现有程序。

### 硬约束

- `PROJECT_ID=SONOFIELD_FPGA`；Repository：`https://github.com/loverlike1216/SonoField-FPGA.git`；active_version=`v5`。
- 不在生产 XDC 中使用旧 Robei/ EBAZ4205 的引脚、时钟、Bank、PS preset、UART COM。
- 测试不可放宽或删除；旧的历史证据不能覆盖；新旧结果应保持来源、时间、Hash 与作用范围。
- 当前**新批准**的正式 ADC 为 `AD7606C-16`，B 型只保留历史兼容回归；本次源文件内的 `50 mg` 目标应在**当前活动需求/验收**中更新为直径 2–5 mm EPS，历史记录只补注释不改写原文。
- 四路供电入口：原厂方式供 AX7020；中央 USB-C 5 V；上阵列 12 V；下阵列 12 V。严禁把不同电源轨直接并联或通过 J10/J11 GPIO/电源脚反向供电。

---

## 2. Gate 0 — 事实、附件与分支恢复（先做，再设计）

1. 用 Windows PowerShell 7 枚举 `E:\Codex_project\AMD_Sonofield\AX7020`（文件树、大小、修改时间、SHA256、类型/版本）。只读取本次任务相关官方原厂资料、现有 Rev3 实物照片、XDC、XSA/PS 配置、线路图；不执行压缩包/镜像/陌生脚本。若路径不可访问，准确报告，不假装已读取。
2. 至少核对用户已提供的两个附件：
   - `3716080086AX7020开发板用户手册V3.0(1).pdf`：2026 V3.0 修订记录（DDR3 型号、PS PMOD 修正）；第 13 页 PS E7/33.333 MHz、PL U18/50 MHz；22–23 页 CP2102GM、MIO48/49；28–33 页 J10/J11；第 34 页 PL 按键。
   - `AX7020开发板原理图V2.0(1).pdf`：内容封面电路版本/日期仍显示较老 REV/2018 信息，应按**上传文件版本 + 实际页头**分别记录；第 13 页串口 CP2102-GM / TXS0102；第 15 页两组 40Pin/33Ω；第 16 页原厂电源。**它不是已证明匹配 AX701020.3.0 的 Rev3 原理图。**
3. 读取 `README`, `AGENTS.md`, 当前 `shared/PROJECT_STATE.*`, `VERSION_STATE`, `CONTEXT_CHECKPOINT`, `CURRENT_PLAN`, `DECISIONS`, `ACCEPTANCE`, `BLOCKERS`, `AI-problem/{problem,decision}`, 最新 v5 证据和正式 BOM；不默认读取 `Historical project/` 内容。
4. 检查 `main`、PR #1/2/3/4、各自 HEAD/base/共同祖先；截至本指令生成时：`main=ecd32e76...`；PR1→PR2→PR3→PR4 为历史叠加依赖，**四者都 Draft/未合并**。必须现场重新核验；不得重复 cherry-pick，亦不能认为 PR4 功能已在 `main`。
5. 优先在 `codex/v5-ad7606c16-nextstage-20261010` 的最新有效候选树继续建立新分支；如 HEAD/工作区已有变更，先保存非破坏性状态/差异，不使用 `git reset --hard`。
6. 最新已有候选：203 测试、AD7606C 数字接口、OCM ARM ELF 编译、COM3 驱动恢复、JTAG/PS 只读识别；**UART 尚未打开/验证 PS 实板数据通信，完整 Rev3/DDR/Bank/当前镜像所有权仍不明**。本阶段不把相关能力重写，也不自动进行 A0 串口打开或 A2 下载/写入。
7. 在 `v5/evidence/hardware_design_20261011/` 新建来源索引与资料比较矩阵：`SOURCE_MANIFEST.json`, `BOARD_REVISION_CONFLICTS.md`, `REPOSITORY_RECONCILIATION.md`。对每条板级事实标注 `MANUAL_V3 / SCHEMATIC_OLD / PHOTO / ACTUAL_READONLY / DATASHEET / CANDIDATE / UNVERIFIED`。

### Rev3 电气门禁

- 厂家手册将 J10/J11 默认为 3.3 V，但 Bank35 VCCIO 可改电压；真正 Rev3 板的 VCCO/扩展座方向/连接必须由匹配资料或非侵入验证确认。
- J10/J11 各 40 个物理触点，其中仅 **34 GPIO、3 GND、1×5V、2×3.3V**；不能当作 80 路数字信号。主板 5V/3.3V 引脚在中央 PCB 原理图中原则上 `NC/隔离`，不接中央 USB 轨。GND 必须做专用低噪声参考和大电流回流规划。
- 厂家手册 PS UART1 `MIO48=B12 TX`, `MIO49=C12 RX`（PS Bank501 1.8 V、板载 CP2102GM 3.3 V，经翻译）；具体 Rev3 UART bridge、DTR/RTS/自动复位须仍保持 `UNVERIFIED`。COM 号动态检测。

---

## 3. Architecture — 三板职责、10×10 布局与设计冻结

### 中央接口采集 PCB ×1

- USB Type-C 5 V Sink 接口、输入保护/电源管理、必要的 5V AVCC / 3.3V/模拟基准（单源自供，避免反灌）；在独立 USB-C 电源缺失时，不允许让 AX7020 J10/J11 供电维持中央半上电状态。
- AX7020 J10/J11 对接、数字数据整形/缓冲、时钟及 RCLK/OE/RESET/SYNC/heartbeat、状态采集、独立硬件安全互锁参考接口。
- `AD7606C-16BSTZ-RL` 64-LQFP ×1；8 路 RX 后置模拟输入、ADC 5V/数字 VDRIVE、基准/旁路/配置/四 DOUT/CONVST/BUSY。
- 环境 TMP117×1，INA226×1，必要 I²C mux/隔离/复位；SHT45 作为可选 DNP 而非必需。
- 八路接收电缆接口（每块阵列 4 路）；输入保护、屏蔽/回流、AGND/数字地策略；调试点和对侧接口防呆。

### 两块共用制造设计的阵列 PCB ×2

- 每板64×NU40C10T 发射器、4×匹配 RX（准确接收 MPN/后缀由供应商审核）、32×TC4427A 双路驱动、16×SN74LVC595A（每器件 Q0..Q3 用于 4 个通道，其他输出不挂载负载）、局部时钟分配和接收 AFE×4。
- 每板独立 DC5.5×2.5 12V 输入、fuse/反接/TVS/eFuse/主动受控 TX 电源切断、稳压/温度/INA226、独立硬件看门狗和温度比较器；对 FPGA 仅有数据/控制和反馈。
- 正面：内部 `x,y∈{-42,-30,-18,-6,6,18,30,42} mm` 的 8×8 TX；四 RX 在 `(-54,-54),(-54,54),(54,-54),(54,54) mm`；外圈其余 32 个虚拟点不装器件。上/下辐射面中心间距 100 mm，可调 90–115 mm。
- NU40C10T/R-2 用户图片：标称40±1kHz，C0=2200pF±20%，最大输入40Vp-p（**不能当连续额定**），发射110dB min、接收−68dB min，外径9.8±0.5mm、高7±0.5mm、脚距5±0.5mm、脚径0.7±0.1mm、脚长7±0.5mm；实际 TX/RX 精确型号/脚极性、焊盘/孔径、公差堆叠必须对照原厂和实物，**不得以 RX 产品分类行推断 TX 电气规格一致**。
- 正背面约束：正面仅 TX/RX；背面电子器件尽量位于 10×10 声学投影框**之外**的 PCB 延伸区。先做二维可制造性/信号完整性/热耦合/机械包络评估，若面积或走线与声学目标冲突，以正式 `LAYOUT_EXCEPTION_REQUEST` 请求用户批准，不得自行修改 12 mm pitch 或 RX 坐标。
- 上下板应尽量采用同一 PCB 原生工程，使用可审计上下侧装配 ID/方向编码，不能简单镜像后反接 RX/电源/极性。

### 接口和线束

- 每阵列16个 DATA、专用 CLK/LATCH/OE/RESET/SYNC/BLANK/HEARTBEAT/PGOOD/FAULT，1 组下游 I²C、4 组 RX AFE 模拟输出，独立 DC 电源与硬件 NC E-STOP 链；必须按实际线缆长度/返回电流/屏蔽和防呆选择物理连接器。
- 66 MHz SRCLK 是候选，不是已验证的线束时序；禁止把 2×20 2.54mm 排针或扁平排线直接当成已验证的 66 MHz 传输介质。提供每线 min/max、延迟、扇出、串扰和眼图/示波器后测清单。

---

## 4. 决策 D-POWER — 理论功率及四源供电

### 4.1 固定接口与候选电源

| 所属 | 入口 | 候选 | 决策状态 |
|---|---|---|---|
| AX7020 | 原厂 5V 电源入口 | 原厂配套适配器/板载保护 | 保持现状，不由自制 PCB 反灌 |
| 中央 PCB | USB-C Sink, 5 V / 3 A 优先 | STUSB4500L + 低 RDS(on) load switch/eFuse、5V模拟稳压策略 | 架构已由用户提出，负载/电源容差待审查 |
| 上阵列 | DC 5.5×2.5 mm 中心正极 12 V | MEAN WELL GST40A12-P1M (40 W)/GST60A12-P1M (60 W) | 接口电压锁定、具体功率依据证明 |
| 下阵列 | 同上独立一套 | 同上 | 同上 |

**12 V/40 W：**`I_rated=3.34 A`；在源有效额定40W假设下，30%头寸要求 `P_worst≤40/1.3≈30.77W/board`；最低20%余量则 `≤40/1.2≈33.33W`。  
**12 V/60 W：**`I_rated=5 A`；30%头寸时 `P_worst≤60/1.3≈46.15W/board`；20%时 `≤50W`。  
**中央 5 V/3 A：**额定15W；30%余量下 `P_worst≤15/1.3≈11.54W`，20%时 `≤12.5W`。这些边界还需按适配器温度/电缆/保护器件实际额定降额，不能直接代表有效负载功率。

**当前推荐：**先按每阵列 **12 V / 5 A、60 W 供电路径额定能力**设计电源/线束/接插件/限流及散热审查边界，BOM 同时保留 40 W 节约成本方案。**没有压电共振有功损耗和驱动损耗数据时，不能宣称40W满足全部最坏工况，也不能宣称60W已经通过理论最坏功率证明；正式采购均 HOLD。** 得到可审计的 P_worst≤30.77W/board 且满足降额/峰值/故障后才优先释放 40 W 版本，否则审查 60 W。

### 4.2 可复现的电容驱动模型（只作为边界项）

对每路初始候选单端0–12V方波、40kHz、最大静态电容 `C0_max=2.2nF×1.20=2.64nF`：

- 理想非能量回收充放电损耗量级 `P_C = C·(ΔV)^2·f = 2.64e−9×(12)^2×40000 ≈0.01521W/TX`。
- 每板64TX：`≈0.973W/board`；全128TX：`≈1.946W`。这项估算的含义是**指定开关路径中的电容切换能量损耗量级**；不代表压电共振时的总实功率、效率、超声声功率或适配器实耗。
- 对桥式两端24Vp-p的候选，电容项约变为4倍，但需要重新计算驱动器数量和通道拓扑；**现有64个双路 TC4427A 驱动128个单端 TX，不等于每个TX都已有双端桥驱动**。不得为凑高声功率把软件和BOM悄悄改为桥式。
- 必须参数化：`C(f,T,V)`，驱动上下沿、导通损耗/静态电流、共振实部导纳/机械声学损耗、全部64路相位并发、Buck/LDO效率、负载峰值、温升和线缆损耗。明确最坏工况表和敏感度：`C ±20%`、驱动电压、40±1kHz、同时开启率和制造容差。
- 对供应商未给出的实部导纳/热阻/连续激励功率，允许保守“设计待定界限 + 未知参数符号 + 边界功率曲线”，**不得随意写成已知最大有功功耗**。无证明则 Gate POWER_RELEASE 保持 HOLD；但可完成相应候选原理图。

### 4.3 上下阵列完整电源树

`DC 12V → 防反/极性保护 → 熔断器 → TVS/浪涌协调 → TPS26631RGER eFuse → 独立硬件受控 load switch / driver rail cutoff → TC4427A_VDD`。

分路生成3.3V数字/监控、AFE模拟供电及本地安全监控电源。功率回路只留在阵列板本地，不能通过中心/FPGA排线回流；为跨板信号建立单点/受控参考，评估四电源与PC/JTAG/UART USB屏蔽引入的地回路和机壳泄漏。

- `PJ-002BH` 为 Same Sky 5.5×2.5 mm、24V/5A、直角THT，带附加开关接点；须按原厂尺寸建封装、开关接点不得误作独立供电脚，并核查 P1M 插入深度、极性和机械拉力。5A是器件标称，考虑温升降额。
- `TPS26631RGER` 为 TI 4.5–60V、限流可调0.6–6A、31mΩ标称集成FET，**不等于把限流直接设成5A就是安全**。按持续负载、短路容量、L/R线束、热耗与上电浪涌选择 RILIM、UVLO/OVP、dV/dt、模式、PGOOD、FET外接反向电流阻断，逐脚复核。
- 禁止沿用未经协调的 SMBJ20A 假设；确定适合12V持续、正常适配器最高电压与浪涌波形的 TVS VRWM/VBR/VC，与 eFuse 绝对最大、滤波电容和 driver limits 协调，并输出计算。
- 独立NC ESTOP硬件串联链路、局部窗口看门狗、过温模拟比较器、eFuse fault、PGOOD状态、线缆断开检测 → 有线 OR 的安全禁止 → 电源切断与各输入默认低。**595 OE 关闭后 Q变高阻不能保证驱动输入为低。** 输出端应有可核实下拉/强制失能策略，电源掉落时输出不反供到TX/前级。故障恢复必须本地硬件锁存+人工重新使能，不因PS重启自动重启。
- `TPS3431` 可作为独立 watchdog 候选，必须验证工作电压、watchdog开窗、上电默认输出、掉电行为；硬件过温开断不能只依赖 TMP117/I²C 或PS/PL软件轮询。
- 3.3V/5V Buck `TPS54202` 是 4.5–28V/2A **降压**器件；12V→5V/3.3V 合理，但不能从低于5V的输入用其输出稳压5V。用于不同电源轨要分别列公式、效率和电流。

### 4.4 中央 USB-C 单源 5V设计

`USB-C 5V Sink → CC/VBUS检测 → TVS/ESD → 开关/eFuse/欠压/浪涌 → CENTRAL_5V`；从此派生 ADC AVCC、数字3.3V/基准/安全电源。STUSB4500L 原厂支持 5V-only Sink / 源宣告默认、1.5 A、3 A。**只有连接电源能力被识别/协商为可用 ≥实际需求时才能启用负载**；电源头标称“5V3A”不是任何接口都天然可吸3A。仅 5V 时不必无意义增加20V PD升压模块。

USB-C VBUS实际可低于5V，保护开关/线缆有压降；AD7606C-16 的5V AVCC容差必须满足原厂数据表。普通“5V输入→5V LDO”不可能在输入低于所需输出+dropout时稳定5V。优先优化低压降路径，若最坏输入不能满足 AVCC 允许区间，则评估合适升降压并审核噪声/EMI/ADC SNR/参考地；真正需要USB PD高压才另行用户批准。

所有中央与AX7020共享通信管脚需 **Ioff/断电容限及防回灌**；连接器上开发板+5V和+3.3V默认NC，独立 USB-C 不能以常规并联或 diode-OR 隐式接到开发板原有5V/3.3V。若双方GND接通，须记录地参考回路及 ESD 防护，不可声称四电源“完全电气隔离”。

---

## 5. 决策 D-IO — 仅63根GPIO的候选逻辑分配

依厂家 V3 J10/J11 每个 **PIN3–PIN36 共34GPIO**，`PIN1,37,38=GND`，`PIN2=+5V`，`PIN39,40=+3.3V`。下表是待电气核验的**候选**：**不可直接变为生产 XDC、不可直接接带电外设**。手册表的 PACKAGE_PIN、BANK、信号名称须由 Codex 自动解析/逐行对照、原生Vivado2025.2合法性和Rev3物理连通复核后再升级。

| 物理引脚 | 数量 | 逻辑分配 | 方向 |
|---|---:|---|---|
| `J10 PIN3..18` |16| `TX_DATA_UP[0..15]` |PL→中央→上阵列|
| `J11 PIN3..18` |16| `TX_DATA_DN[0..15]` |PL→中央→下阵列|
| `J10 PIN19..27` |9|`UP_SRCLK, UP_RCLK, UP_OE_N, UP_RESET_N, UP_SYNC, UP_RX_BLANK, UP_HEARTBEAT, UP_PGOOD, UP_FAULT_N`|前7输出、后2输入|
| `J11 PIN19..27` |9|`DN_SRCLK, DN_RCLK, DN_OE_N, DN_RESET_N, DN_SYNC, DN_RX_BLANK, DN_HEARTBEAT, DN_PGOOD, DN_FAULT_N`|同上|
| `J10 PIN28..31` |4|`ADC_DOUT[0..3]`|ADC→PL|
| `J10 PIN32..36` |5|`ADC_BUSY, ADC_SCLK, ADC_CONVST, ADC_CS_N, ADC_SDI`|BUSY输入，其余输出|
| `J11 PIN28` |1|`ADC_RESET_N`|PL→ADC|
| `J11 PIN29..30` |2|`I2C_SCL,SDA`|双向开漏|
| `J11 PIN31` |1|`ESTOP_STATUS`|硬件状态→PL，不是安全关断唯一链路|
| `J11 PIN32..36` |5|`SPARE[0..4]`|保持高阻，不接未知电压|

总计 **63/68使用、5备用**。与旧候选 67/68 且三套 I²C（6 IO）相比，统一2线 I²C 在逻辑层面**净节省4个GPIO**；但最终是否能把5根都留给未来，取决于独立RESET/IRQ/紧急状态/ADC模式脚和 Rev3全网表审核。

重要：J10 PIN33–36 跨入 BANK35，J10/J11 的 Bank/VCCO 一致性、低电平阈值和物理地回流需明确审查。`J10 PIN28..31` ADC DOUT集中只代表候选逻辑位置，没有证明封装/线缆布线最优。PLL/MMCM产生高频内部时钟、通过合适 ODDR/IOB 输出 SRCLK；PL 50MHz实体引脚U18 与 PS33.333MHz E7不可混淆。66MHz SRCLK/32lane 仍需全系统同步、RCLK同步裕量和外部 setup/hold/PVT 校核。

### I²C优化架构

建议用 2PL IO (`I2C_SCL/SDA`) 接中央一颗 TCA9548A（如 `TCA9548APWR`，最终订货后缀需核对），通道0中央 TMP117+INA226，通道1上阵列TMP117+INA226，通道2下阵列TMP117+INA226，其他通道保留。TCA9548A上电默认全通道关闭，支持复位，额定至400kHz；首轮默认100kHz。不同段可复用相同 INA226 地址且故障分域，实际 SDA stuck-low/上拉电流/线束电容与阵列局部断电须做硬件级故障模型；必要时额外隔离/缓冲，不能依赖Mux本身宣称支持所有掉电情况。

`TMP117` 局部温度计测得的是板/安装点温度，不是无限精度 3D空气温场。保留分层声速模型、源可信度/时间戳、异常拒绝及温度超限硬件截止。PS已有程序不可被假设能访问I²C直到对应PS/PL控制器验证。

### 需要输出的针脚资产

- `v5/hardware/ax7020/AX7020_REV3_68GPIO_AUDIT.csv`：40×2触点，按 J10/J11、header.pin、FPGA_PACKAGE_PIN、BANK、VCCO、方向、IOSTANDARD、逻辑网名、物理线束、证据、状态一一列出；电源地脚也列清楚。
- `v5/hardware/ax7020/AX7020_REV3_PROPOSED_PINMAP.csv`：按上述候选逐针填满，产生 conflict/dup/IO bank/差分/时钟资源检查。没有 Rev3 电气证据只能保持 PROPOSED。
- `v5/hardware/constraints/ax7020_design_review_only.xdc`：仅供审查，故意防止作为正式 bitstream 直接调用；生产 XDC 需独立的正式核验门禁，不能写未测 VCCO/外部 IO delay。
- `v5/docs/hardware/IO_BUDGET_AND_SI.md`：逐线延迟/线束最长长度/PVT/setup/hold/回流/扇出说明，标清可计算值与未来示波器实测值。
- `v5/config/SIGNAL_CONTRACT.json`：与RTL端口、中央网表、上下阵列网表和软件配置自动对账。

---

## 6. 决策 D-ADC / D-AFE / D-TEMP

### 正式 AD7606C-16

- 仅一颗、中央 PCB、`AD7606C-16BSTZ-RL` 为拟采购完整 MPN，LQFP64 10×10 mm；原厂订购页/数据手册与嘉立创元件库符号/封装逐脚核对。
- 8×16bit同步采样；高带宽逐通道配置`BANDWIDTH=0x07`且读回，四路串行 DOUT 方案/CONFIG配置/工作模式、输入量程、OS/CRC、初始化与失败拒绝都要依据 ADI Rev.A 原厂表、现有 v5 ADC 合同和可复现设备模型，不能从旧 B 型假定数值。
- 量化ADC外部采样时钟边沿、所需SCLK：例如 `8channels×16bit =128bit/采样`，四 DOUT理想并行等价 `32bit/采样`，在800kSPS量级仅移位数据下界为 `25.6MHz SCLK`（未计命令/建立保持/片选）；真实性能必须按时序表重新论证，且采样率并不等于 UART 可连续输出速率。
- ADC 5V AVCC、VDRIVE按实际逻辑电平与原厂要求设计；参考、REGCAP/REFCAP/AGND、输入保护与RC滤波均逐引脚检查；ADC 对象是多通道**40kHz波形测量**而非“距离直接输出”。
- 真实接收器工作量级、AFE增益及偏置：应明确接受 0–5V or ±FS 方案，禁止因 AFE 出现负电压或复位尖峰损坏ADC；8通道相位延迟/增益/温漂/抗混叠/空白恢复预算，接收保护与发射blank协调。
- 当前 PR4已有 C-16 逻辑和数字接口回归，必须保留后做新增网表/固件/寄存器一致性检查，不要改写冻结的 AD7606B 历史数据；真实 ADC 的 220kHz/噪声/幅相仍需样机实测。

### 温度

- `TMP117AIDRVR`×3（原厂TI认证封装/库符号须确认），中央环境1，上阵列1，下阵列1；传感器远离驱动发热热点且保留与声传播路径的测量代表性分析。
- 数据进入 `T(r,t)估计→c(T,RH假设)→∫ds/c→传播相位/空间自校准→atomic map`；相位符号、校准项独立、超温/离线/滞后/骤变状态保持模型安全。
- 若使用选配 SHT45：默认 RH 仅诊断/来源标签，不因新增元件而假称通过湿度声速模型。
- 与缺少3D温场感知之间的差距应写入实验计划，避免从三点温度外推出虚假的绝对高精度。

---

## 7. Gate 1–Gate 7：分阶段 Codex 执行合同

### Gate 1: Source & Architecture Freeze

**Goal**：建立 Rev3 对照事实、四电源/三板信号清单、版本状态。  
**Allowed**：只读采集、来源Hash/资料索引、候选参数。  
**Done When**：每一候选器件/IO/机械/电源事实都有证据与状态；没有引用旧板管脚为当前事实；主板现有镜像绝无更改。

### Gate 2: Theory & Protection

**Goal**：输出计算脚本与 Worst-Case 供电、电源保护、硬件fail-off的候选图。  
**Must**：详细对比 12V 40/60W，提供20%最低/30%目标双门禁；中央5V/3A供电可用电流及典型/最坏表；从12V降压到5V/3.3V，eFuse/TVS/fuse/电缆/连接器/温升闭合计算。  
**Test**：边界扫描、断电/单边失电/反接/热故障/时钟中止的逻辑及物理截止链分析。  
**Done When**：已知量可重复算得相同结果，未知共振有功功耗以参数化边界和真实 HOLD 显示；不能为了给出40W结论虚构数字。

### Gate 3: IO / Synchronization / ADC Review

**Goal**：63/68候选 IO、I²C共享分支、AD7606C四DOUT、跨板同步/安全/电平审查。  
**Test**：脚位重复检查、Bank/VCCO、数字方向、power-off、时钟、66MHz外部min/max候选约束、信号不丢失的RTL/软件合同回归。  
**Done When**：逻辑网络双向对账完成；不合格 Rev3 资料不得被包装为可部署 XDC；必须保留生产 GPIO/IO 延迟 HOLD。

### Gate 4: BOM / Native Library Qualification

**Goal**：生成 5张关联表（中央、上、下、外部、整机汇总）的新工作 BOM，并记录从现有 v5 工作 BOM 的逐项变更。  
**Fields**：位号、器件中文名、型号完整MPN、原厂、数目+备件、组装侧、封装/Pin1/极性/EP、主要额定值、功率/电流/占空、用途、电源域、供应商链接、国内采购/替代件、Datasheet版本与访问日、认证/筛选/制造状态、谁批准、未知/证明路径。  
**Lock**：NU40C10T TX×128 + spare，RX×8 + spare，AD7606C-16×1，TMP117×3，TC4427A×64和595×32如拓扑未获变更批准，USB-C/J10/J11/独立DC接口、I²C选件、屏蔽线和机加工全部入BOM。现有原件与历史BOM保持原字节。  
**Done When**：有真实数据表的器件才可从 `CANDIDATE`→`DESIGN_SELECTED`；采购状态默认 HOLD；公式和汇总数量通过两种独立方法复核。

### Gate 5: 嘉立创 EDA 原生原理图

**Goal**：中央 PCB、统一阵列 PCB、上/下Assembly差异、线束/接口、保护/电源/ADC/AFE/TMP117完整原生工程。  
**Process**：先独立核对设计合同，再建功能清晰的模块页（Type-C/Power、AX7020、C16 ADC、I²C、TX serializer/clock、driver64、RX4 AFE、array12V保护、watchdog/eStop、testpoints）；每个差分/模拟/电源接口有净名和真实连接器方向；原始符号及封装来自原厂，用户文件里的概念草图**不是**可制造电路。  
**Testing**：真实打开/重开原生工程、真实 ERC+全部 warning 分类、原生 Netlist Export/比对BOM位号和数量/功率域审查、封装Pin1/EP/孔位、机械投影/孔位、无网络悬空或隐藏供电。ERC零严重错误也不等于电气放行。  
**Blocker**：若 Codex 无法接入真正嘉立创 EDA 专业版原生编辑器/工程，应交付审计的连接关系+符号/封装清单+原理图生成任务，明确 `NATIVE_SCHEMATIC_NOT_CREATED` / `ERC_NOT_RUN`，**不能以Markdown/图片/JSON冒充原生原理图**。

### Gate 6: FPGA / 软件 / 整理回归

**Goal**：所有变更与当前活动v5一致且无回归。  
**Baseline**：当前PR4约203 tests和早期3696帧×3 Icarus+1 XSim的封存证据；涉及RTL/协议/ADC/接口变更时须重跑完整数字验证，新增电源/IO/状态机测试不少于固定原有套件。复用现有 Vivado2025.2脚本；编译源只来自 v5，禁止 `Historical project/` 隐式读取。  
**Review**：声明OOC与完整板级STA、综合与Place/Route、模拟传感器与真实ADC、Host ARM ELF与真实PS运行的边界；残余BRAM异步控制DRC问题不得忽略。  
**Done When**：原有测试/黄金数据不被修改迎合实现，报告里能把旧 PASS/新 PASS/NOT_RUN/FAIL 分开，受保护文件Hash/新旧BOM差分、clean clone 可运行。

### Gate 7: GitHub 审核包

- 在已授权开发分支提交，Push并远端核对，Draft PR交用户审核；不主动合并main、force push、删除历史、冻结本版本或升级v6。
- 核对已有 #1 #2 #3 #4，新增PR必须如实声明叠加祖先与base，给出不丢失功能的审核/正常合并顺序（通常先审核 #3 对祖先包含关系，再审核 #4 /本次后续，不重复应用 #1/#2）。若PR状态已更新现场重判。
- 更新当前 shared 下 `PROJECT_STATE / VERSION_STATE / CURRENT_PLAN / DECISIONS / ACCEPTANCE / BLOCKERS / CONTEXT_CHECKPOINT`。Formal decision应显式记录本次用户四源供电、独立USB-C、12V DC5.5×2.5、20/30%余量、I²C优化、EPS2–5mm目标；不得用文字“已批准器件”替代实际器件电气验收。
- 至少保存 `DESIGN_REVIEW.md`, `POWER_BUDGET.csv/json`, `IO_PINMAP.csv`, `SCHEMATIC_STATUS.md`, `BOM_DIFF.md`, `RISKS.md`, `FINAL_VERIFICATION.json`, `MISSING_FACTS_AND_NEXT_MEASUREMENTS.md`, `DECISION_LOG.md`, `CHECKPOINT` 与 rollback/PR说明。

---

## 8. Acceptance / Evidence Required / Done When

| 门禁 | 可接受结果 | 阻塞与限制 |
|---|---|---|
| 架构 | 1中央+2对称阵列、128T/8R、单C16、3TMP117、10×10坐标与通道正确 | 几何变动须用户批准 |
| 电源 | 4个独立入口、上/下12V本地驱动、中央USB-C5V、自供且J10/11不反灌 | 未知有功负载→功率释放HOLD |
| 余量 | 至少20%、优先30%，各电源源温度降额与总负载可复现预算 | 不得将简单CV²f冒充总功耗 |
| 安全 | 默认OFF、NC ESTOP、watchdog、真实TX rail cutoff、PGOOD/FAULT、断电和失联安全有硬件路径 | 物理关闭延迟待样机实测 |
| 接口 | J10/J11 68GPIO完整审核，63 used候选+5 spare，电平/方向/Bank与回流一致 | Rev3 Bank35 VCCO/针脚仍需实证 |
| ADC/AFE | C16高带宽寄存器/四DOUT/8ch和8路AFE、参考/电源/保护/偏置接口合同可核查 | 模拟SNR/幅相/标定待实测 |
| BOM | 原厂MPN、封装、真实数量、外置适配器/线束/保护、公式与来源、采购HOLD标记 | 任何TBD不得伪造 |
| 原理图 | 只有真EasyEDA工程且真ERC记录才标通过；反之明确NOT_RUN | 生产制造仍需独立Review与用户许可 |
| 回归 | 原 v5 功能/协议/RTL/轨迹/温度/ADC通过，外部时序缺口保留 | 不能因OOC PASS宣称整板可运行 |
| 人工审核 | 提供真实证据和PR，三种标准结论之一 | 不自动merge/main或采购/制板 |

### 阶段性结论

- `ACCEPT`：本阶段要求中的全部*适用*硬件电气设计/原生原理图/ERC/审查标准均按真实工具满足，无影响原理图设计的重大未知；**不代表实际声学系统接受**。
- `ACCEPT WITH LIMITATIONS`：结构与计算/数字合同完整，但某些工具/Rev3数据、连续功耗或原生ERC尚待；须列明对下一步的限制。
- `REVISE`：逻辑网络/功率/安全/兼容性/原理图存在已确认关键缺陷，必须修复；不可靠测试数目掩盖。

**无真实器件/样机时，不因缺真实声压、功耗、温升、粒子运动而无限循环；本阶段的电气及制造HOLD必须被保留，达到可验证离线阶段目标后停止低价值优化。**

---

## 9. 已独立审核的关键取舍（供 Codex执行，不可自行扩大授权）

| 决策 | Rationale | Rejected Options / Risks | Approval / Status |
|---|---|---|---|
| 中央 USB-C独立5V | 杜绝占用主板扩展电源供电额度，分离ADC噪声源 | 不用J10/J11主供电；但要防源间反灌与地回路 | 用户新需求；电源额度/类型C检查HOLD |
| 阵列 12V/5A电气容量作候选 | 原器件动态功耗未知，先预留60W路径可给更高边界 | 40W优先只在最坏持续负载证明后选择；不得把60W当实际耗电量 | 60W=架构候选，采购用户批准 |
| PJ-002BH/TPS26631RGER | 原厂型号参数匹配电压/额定电流范围 | 连接器高温降额、TVS协调与限流可能造成热瓶颈 | 电路设计候选，尚未释放 |
| STUSB4500L Type-C | 正式5V Sink、可识别source CC3A，易于fail-off | 不用没有源电流判别的任意5V3A假设、无必要不用PD升压 | 推荐候选，端口/元件验证需Codex |
| 2线I²C + TCA9548A 3域 | 节省四GPIO、可处理同地址器件，故障分支管理 | 不是无限线长/无源掉电隔离证明，需Ioff/局部缓冲 | 推荐候选，须通过线束分析 |
| 63/68 GPIO候选 | 数据/ADC/两侧安全状态全部保留，可有5备用 | 外部时序、VCCO和Rev3误配风险 | 候选，不得部署 |
| 单端12V TC4427A/595既有逻辑 | 与当前已验证32lane×4和64驱动器相容、变更风险低 | 桥式可更大Vpp但倍增驱动资源/引脚及安全问题 | 先保留，桥式方案另行申请 |
| 三测温参与补偿 | 相位温漂不能只用GUI监测代替 | 三个探头不足以测全部空气三维温场 | 正式需求，实测门禁保留 |

## 10. 权威资料与仓库事实链接（务必记录检索日和精确版本）

**用户提供的本地资料：**

- `E:\Codex_project\AMD_Sonofield\AX7020` — 待Codex真实枚举、Hash、版本审查。
- `3716080086AX7020开发板用户手册V3.0(1).pdf` — 35页；2026年V3修订页2；J10 p28–30 / J11 p31–33；PS UART p22；时钟p13；DDR p14；按键p25/34。
- `AX7020开发板原理图V2.0(1).pdf` — 16页；第13页串口、第15页扩展、第16页电源；文件名V2与封面REV/2018存在版本差异。不得据此认定硬件Rev3原理图已取得。
- NU40C10T/R-2用户图片 — 有水印/裁切；记录用户提供参数，必须追加厂家完整料号/原厂PDF及样品量测。

**官方/原厂外部参考：**

1. ADI AD7606C-16 产品和Rev.A datasheet：https://www.analog.com/en/products/ad7606c-16.html / https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf
2. TI TPS2663x / TPS26631RGER（电压和0.6–6A范围）：https://www.ti.com/product/TPS2663/part-details/TPS26631RGER / https://www.ti.com/lit/ds/symlink/tps2663.pdf
3. Same Sky PJ-002BH（5.5×2.5、5A）：https://www.sameskydevices.com/product/resource/pj-002bh.pdf
4. ST STUSB4500L（5V/3A Type-C Sink）：https://www.st.com/en/interfaces-and-transceivers/stusb4500l.html
5. TI TPS54202（12V→5V/3V3 Buck，2A额定）：https://www.ti.com/product/TPS54202
6. TI TCA9548A（8路I²C mux，power-on全断开、reset）：https://www.ti.com/product/TCA9548A
7. TI TMP117：https://www.ti.com/product/TMP117
8. Microchip TC4427A：https://www.microchip.com/en-us/product/TC4427A
9. MEAN WELL 40W P1M 参数及插头规格：https://www.digikey.si/en/products/detail/mean-well-usa-inc/GST40A12-P1M/10659924
10. 60W P1M 应索取MEAN WELL官方固定后缀 Datasheet，型号核对无误才允许采购。第三方网页参数不可取代厂家Datasheet。
11. 正式仓库：https://github.com/loverlike1216/SonoField-FPGA；PR #1、#2、#3、#4 和新工作分支源证据。

---

## 11. 提交前必须返回给用户的简明报告

报告格式：

```
PROJECT_ID / repository / workspace / branch / commit / active_version / Stage

Decisions Adopted / Pending / Rejected

Power:
  upper P_worst / max accepted adapter power / >=20% / target30% / unknown motional term
  lower ditto
  central total budget / USB-C CC3A verification / 5V AVCC policy

IO:
  63used/5spare candidate vs actual approved map; bank/voltage/signal ownership

Hardware:
  manufacturer qualified MPNS / still TBD
  central + upper + lower native schematics created? ERC executed? counts?
  12V TX shutdown safety reviewed? physical tests NOT_RUN?

Digital:
  old baseline / new tests / XSim / Icarus / Vivado scope

Migration/Repo:
  PR#1/#2/#3/#4 ancestry, current Draft URL, main unchanged

Blockers / Evidence links / Changes / Rollback / User Approval Required

Decision status: ACCEPT | ACCEPT WITH LIMITATIONS | REVISE
```

**不得仅回复“已完成”；交付真实文件、命令、日志、SHA256、工具版本、原理图截图及对应原生工程。当前任务不要启用真实超声或修改已运行未知AX7020配置。**
