# SonoField-FPGA v5 — AX7020 / NU40C10T PCB 落地前全系统开发正式指令

**执行对象：Codex 6.1 Sol · Extra High（模型选择由用户在 Codex 界面完成）**  
**指令日期：2026-10-09**  
**PROJECT_ID：`SONOFIELD_FPGA`；正式版本：`v5`；Repository：`https://github.com/loverlike1216/SonoField-FPGA.git`**  
**工具链：Vivado / Vitis 2025.2，Windows 优先 PowerShell 7 (`pwsh`)**  
**工作范围：PCB 制造/上板之前，尽可能完成真实可执行的 FPGA、PS、PL、协议、上位机、校准算法、接口、硬件候选设计及独立验证。**

> **先阅读本文全部内容后执行。本文是用户当次目标与工程开发边界，不是对未发生硬件测试的完成证明。**
> **禁止**因本指令建立 v6；禁止擅自更换正式仓库、删除/重写 Git 历史、force push、修改冻结历史、直接生成/发布 Gerber 或购买器件。若新沙盒和 `history_old/` 尚在迁移中，应先确认当前仓库真实状态和迁移门禁，**不得抢先进行破坏性迁移**。

---

## 1. User Goal / 必须达成的端到端路线

建成一个基于 **ALINX AX7020，XC7Z020 速度等级 -2、工业温度等级 I（这两项由用户声明，正式芯片丝印/厂家证据仍需复核）** 的 128 路 40 kHz 超声双阵列控制平台：

1. **中央 PCB ×1**：直接连接 AX7020 的两组 2×20 扩展头 J10/J11；中央板安装唯一的 8 通道同时采样 ADC、数据/时序接口、供电保护、环境参考 TMP117 和可选但推荐的 SHT45 湿度传感器。**中央板要求由 AX7020 扩展口供电**，必须先真实验证 J10/J11 电源引脚和剩余电流预算，否则停在设计待核验，不准通过回灌、电源偷接或未经批准的额外供电隐瞒不足。
2. **上阵列 PCB ×1、下阵列 PCB ×1**：尽量采用**同一套 PCB 设计/相同元件布局、不同板位标识与装配方向**；每片 8×8 的 NU40C10T 发射器，共 128 TX；每片四角 4 个接收器，共 8 RX（RX 精确 MPN 尚待选型，不能把 NU40C10T 当 RX 使用）。两阵列各有**自己的外置电源输入、eFuse/保险/监测/断电安全控制**，电源不通过 AX7020 传输。功率驱动、电平转换、串行寄存器尽量靠近本阵列。
3. PS/PL 上电后系统保持 **SAFE/OFF**。PS KEY1 长按确认安全预备；PL KEY1 长按触发稀疏几何自校准（设计见后）；任一失能、超温、通信错误、急停时双阵列切到安全状态。**机载按钮不是唯一急停措施**，必须有独立常闭急停和默认失能硬件路径。
4. 自校准阶段：按既定方向逐个激励**两条对角线及用户指定补充点**，从当前 TX 到**对侧四个 RX**收集波形，结合 3 个 TMP117 与必要的湿度/声速模型，拟合可辨识的阵列位姿、传输延迟、参考相位和工作空间几何；通过 UART 将质量分级的校准/空间边界/8 RX 位置与诊断报告交给 PC。
5. 校准后由 PC 上位机编辑任意目标点或**用户自己一步步绘制**直线/折线/曲线/平面/三维轨迹；运行前先计算/仿真相位图、边界检查与运动约束，上传运动任务，由 PS/PL 可靠排队及原子提交相位图，逐步完成定点悬浮、XY 直线/曲线、Z 向移动、XYZ 任意轨迹。
6. 平台不能虚构“实时观察小球位置”的能力：若没有摄像头/其他定位传感器，**运动为开环声场控制 + 电气/温度/校准状态反馈**，并非小球位置闭环。GUI 应明确显示这个事实。

### 不改变的继承约束

- `v5`、Vivado/Vitis 2025.2；128 TX、8 RX、每路 8-bit requested/calibration 独立相位、atomic map commit、同一时间基准与原安全协议。
- 上下对称 8×8；TX 辐射面中心 pitch=12 mm；名义面对面间距 100 mm、90–115 mm 可调；几何原点在两阵列中心；上辐射面 `z=+gap/2` 朝 -Z、下 `z=-gap/2` 朝 +Z。
- TX XY 坐标 `{−42,−30,−18,−6,6,18,30,42} mm` × 对应 y；RX 四角候选 `(±54, ±54) mm`，须与机械孔位、封装外径、实际安装一致。
- 演示目标轻质泡沫球，最终尝试 50 mg；尚无物理证据保证悬浮或运动。
- **发射器型号固定 `NU40C10T`**。先取得对应厂家/批次资料与测量，不可搬用 `NU40C16T` / TCT40 的电压、声压、焊脚、等效电容等指标。
- 温度补偿是正式功能，不是单纯 GUI 显示，不可将三颗 TMP117 的配置降级为“可选”。

### 用户草图的工程解读

- 图一“中央板”：外框为 PCB；顶部两组 `2×20` 为 AX7020 扩展头；中间 ADC；左右逻辑数据交互与向两片阵列的边缘接口。具体 PCB 连接器数量/形态允许按信号完整性、接地/线束和加工装配重新优化，必须保留左右明确功能分区。
- 图二“阵列板”：正面以辐射面和装配几何优先，红点表示四角 RX/安装参考，黑点为布局示意；**图中的边缘黑点不能理解成把全部 64 TX 改成周边一圈**。正式电气几何始终是 8×8=64 TX + 四角 4 RX。背面优先安排驱动、移位、保护、采样前端和电源。留可维护的接线、通风/散热及机械定位。
- 请用户将这两张草图作为附件上传给 Codex；若图片无法实际读取，标记 `DIAGRAM_REFERENCE_NOT_ACCESSIBLE`，**本文文字约束仍有效**。

---

## 2. 先执行 Repository Reconciliation（禁止从记忆继续编码）

1. 确认实际本地工作路径、Git remote、`main`/开发分支、当前 HEAD、上游 HEAD、`git status --porcelain=v1`、未跟踪资产、Git LFS/忽略文件、工作区是否已迁移为 `history_old/` + 活动 `v5/`；不指定或猜测一个不存在的工作目录。旧沙盒若存在，应只读。
2. 只优先读取活动入口 `README.md`、`AGENTS.md`、`shared/PROJECT_STATE.*`、`VERSION_STATE.json`、`CONTEXT_CHECKPOINT.*`、`CURRENT_PLAN.md`、`DECISIONS.md`、`ACCEPTANCE.md`、`BLOCKERS*`、`AI-problem` 当前 v5 Problem、`v5/README.md`、`v5/evidence` 新证据、当前 `v5/config/*`、`v5/hardware/integration_candidates/`、`v5/hardware/bom/working/` 以及上一迁移交接文档。
3. 若已经建立 `history_old/`：**仅在需要比对来源或回归且有明确任务时**点对点读取；否则不搜索、不引用、不加载、不构建、不将旧文件拷入 v5 的编译源。若尚未建立，仅保留现状并遵守之前的独立迁移门禁，本任务不取代它。
4. GitHub 在 2026-10-09 的已观察 HEAD 曾是 `ecd32e76e9b6`，**不是未来的固定 HEAD**；新运行必须重新获取。前次实测仅证实实板 `AX701020.3.0`、XC7Z020 JTAG、CLG400，已有 SD 上电程序和两 CPU 运行；完整级别、Rev3 PS/DDR 匹配、BANK VCCO、UART、ADC/声学均仍未完整实测。
5. 读取正式已有代码的接口/数据结构/GUI，而不是从零发明或为方便重写核心。保留已有 115 个 Python tests、3 Icarus + 1 XSim 的 3696 帧等价测试和黄金参考；需要调整相位/接口时必须建立变更前后基准比较，不能降低标准。
6. 对历史 `shared/BLOCKERS.md` 和 `shared/BLOCKERS_ENGINEERING.md` 仍以 v2/Robei 口吻叙述的问题，进行**不破坏历史证据的现行 v5 状态分流**。历史的 Robei J3/J4/J5/J6、N18、COM4、旧 FTDI/512MiB 等不得在当前 AX7020 XDC/PS/PCB 里当事实。
7. 用户这条指令代表要求增加功能和 PCB 设计边界；如发现与已批准的核心合同冲突，先列出 `DECISION_REQUIRED`，不得以“优化”名义悄悄换芯片或修改验收。

**输出：** `v5/evidence/pre_pcb_20261009/REPOSITORY_RECONCILIATION.md`（日期按实际执行日更新）、当前已完成与缺失证据矩阵、唯一活动构建源清单、不可更改的接口哈希/黄金行为摘要。

---

## 3. 硬件总体系、接口分层和电源架构

### 3.1 三 PCB 划分

```text
PC GUI / pyserial (UART1 via AX7020 on-board USB-UART)
                 <----> PS Cortex-A9 firmware/service
                              | AXI-Lite / BRAM / IRQ
AX7020 J10,J11 <--verified GPIO/XDC--> CENTRAL PCB
                              |-- AD7606B/C-16 (8 RX simultaneous sampled, 1 ADC)
                              |-- TMP117_CENTER + optional SHT45 RH
                              |-- monitored 3.3/5 V from AX7020 only if within measured budget
                              |
                   signal/ground distribution
             +----------------+----------------+
             |                                 |
      UPPER ARRAY PCB                    LOWER ARRAY PCB
      local external 12V IN              local external 12V IN
      own fuse/eFuse/PGOOD               own fuse/eFuse/PGOOD
      16 serializers / 32 dual drivers  16 serializers / 32 dual drivers
      64 × NU40C10T                      64 × NU40C10T
      4 × 10mm RX + AFE                  4 × 10mm RX + AFE
      TMP117_UP, local watchdog         TMP117_DN, local watchdog
             |                                 |
             +------- acoustic workspace ------+
```

**强制电源原则：** AX7020 → 中央板仅承担被核实的中央控制/ADC 低功耗供电；上、下阵列的**功率电源**各自独立外部输入，不可经过 FPGA 扩展针供电或把 12V/15V 连到 FPGA 接口。三板之间共享信号参考地应是受控、低阻、明确的连接，**不能误理解为三板电源负极全部电气隔离**；请进行地回路/噪声/回流路径与安全评审。

### 3.2 供电容量 —— 先按充分余量候选，后以实测锁定

- 推荐 **上板独立 12 V / 5 A (60 W) 电源一套、下板独立 12 V / 5 A 一套**，或具独立限流/熔断/开关且经过论证的同额定多路隔离输出供电系统。此为**外部电源额定输出能力选型起点**，不是 NU40C10T 或驱动器实际耗功/许可电压的结论，绝对不可据此直接以 60 W 连续驱动换能器。
- 初次测试单路或少路时使用台式限流 12V，逐级抬高可用总电流；阵列每板已有候选 eFuse 上限约 2A 的工作基线，在电源大于保护阈值时，**不能声称阵列获得 5A 可用功率**。保护阈值只能根据起动浪涌、连续/峰值波形、热测量及器件额定重新计算，经安全评审再变更。
- 计算报告必须给出测得的 `C_eq(f,T,V)`、电流波形、供电峰值/均值、供电容量与利用率、端口功率、驱动 IC 功耗、降压效率、热余量和电缆/保险容量；采用不同电压/频率上限的 sensitivity sweep。初步容性估算可用 `P_switch≈C_eq·V²·f` 作为理想电容全摆幅充放电规模，但**它不涵盖机械谐振、驱动损耗及换能器真实输入功率**。
- TX 驱动 `TC4427AEOA713` 候选，每板 32 颗双通道、两板合计 64 颗；**根据真正的负载/额定电压/热升测试确认是否适合直接驱动压电负载**。禁止把“峰值 1.5 A MOSFET 栅极驱动器”误当成已验证的 128 通道功放。低于安全限制才启动。
- 每板至少：反接保护、保险/可复位安全保护、eFuse（如 TPS25947 候选，但规格/OVLO/TVS 配合重新算）、电压/电流监测（INA226 + Kelvin shunt）、bulk/高频去耦、本地 3.3 V 逻辑/5 V 模拟电源、温度/热关断、硬件 KILL、默认 OFF 的双重独立使能、稳压与欠压故障记录、连接器正负极永久标识。
- 旧 `SMBJ20A` + eFuse/TC4427A 保护配合已识别为**浪涌钳位不闭合的待解决问题**，不得直接照搬旧 BOM 宣称安全；给出浪涌测试定义和器件能量/钳位/瞬态工作范围表，没闭合则 `POWER_DESIGN_HOLD`。
- 中央板：先计算 AD7606 模拟 5 V + VDRIVE 3.3 V、逻辑电平转换、温度传感器、I²C 隔离、时钟/接口缓冲的**最大工作与启动电流**，结合 J10/J11 官方 +5V/+3.3V 接口的 Rev3 限流/热/线束压降；只从**一个经过保护与反灌分析的来源**取得对应电压，不能将 J10/J11 的同名电源未经分析并联，也不能给 AX7020 反向供电。若无法满足，记录 `CENTRAL_POWER_BUDGET_BLOCKED`，给出小电流降本/隔离供电替代建议待用户批准；不可直接改变“由 AX7020 供电”的用户约束。
- 驱动逻辑要在“阵列外部电源已上但 AX7020 关机 / FPGA IO Hi-Z / 线缆脱落 / 单侧欠压 / 两侧启动顺序颠倒”时仍保持 OUT_OFF，不能依赖软件初始化才安全。

### 3.3 AX7020 引脚/接口

- 官方 AX7020 2023.1 手册规定 J10/J11 **各为 40 针 2×20，其中各 34 GPIO，另有 GND/+5V/+3.3V**。不能把 80 个接点都算可用 GPIO；官方资料也提示 VCCO、电平和版次匹配，旧资料可能与本实物 PCB `AX701020.3.0` 存在差异。
- 优先使用仓库 `v5/hardware/integration_candidates/20261009/` 的**已经离线审计的 80-pin / 68 GPIO / 63 assigned + 5 spare** 候选作为起点：逐行检查 J10/J11 实物方向、A/B 侧、FPGA 球位/Bank、VCCO、逻辑方向、负载、线缆地及针脚重用；用 Vivado 2025.2 的真实 package 数据和 Rev3 原理图/连续性验证比对。
- 制作完整机器可读 `AX7020_GPIO_MAP.csv` 与逻辑信号 `SIGNAL_CONTRACT.json`，至少字段 `connector,connector_pin,package_pin,bank,vcco,io_standard,dir,net,clock_class,reset_level,pull,power_domain,harness_pin,source,verification,status`；每个引脚必须唯一、无多驱动、无电源误用，`UNKNOWN` 不得作为生产 XDC。
- 提供**两套可区分的约束**：`ax7020_candidate.xdc`（若引脚尚未物理核验，明确 `NON_DEPLOYABLE`）和在完备核验后生成的 `ax7020_production.xdc`；生产 XDC 缺少 VCCO/外部 min/max 延迟时不可生成可用板级 BIT。禁止使用旧 Robei N18、J3..J6、旧 DDR preset。
- 固定 FPGA 器件目标必须以用户说明 `-2 / I` 与实物芯片完整丝印交叉核验；文档公开候选 `XC7Z020-2CLG400I`，Vivado 合法 part 字符串由 `get_parts`/器件库查询确认，不手写未验证型号。
- AX7020 官方板载 PL 输入时钟候选 `50 MHz / U18`、PS 参考 `33.333 MHz`；继承 **132 MHz 是内部目标**而非晶振。通过 PS FCLK 或经确认的 Clocking Wizard/MMCM 建立实际时钟树，满足频率/抖动/启动锁定/CDC。需真正完成综合、布局布线、物理外部 IO timing，不能把 132 MHz OOC WNS 当整板结论。
- 现有高速接口**32 并行 serial lanes，每侧 16 lanes，每颗 595 只用 Q0–Q3**，共 32 颗 SN74LVC595APWR；TX shift ~66 MHz、ADC serial ~33 MHz 是原目标量级，必须检验真实数据/时钟/锁存/OE/复位经缓冲/电平转换/线缆的 setup/hold、skew、fanout、源端阻尼与 EMC。严禁不经设计审查改为 16 lanes/8bit 或多级级联，避免无意降低通道刷新能力。
- 使用 `SN74AXC8T245PWR` 时 VCCA/VCCB 均不得超过 **3.6V**，方向控制按器件真实 DIR1/DIR2 分组；**不可当 5 V translator**。I²C 是开漏协议，不能直接把这个普通方向控制的推挽电平芯片当 I²C 隔离器；优先验证 TCA4307 等具受控上/掉电行为的开漏总线隔离候选。
- 未经用户进一步确认，暂不改变 32 lane、ADC 通道顺序、protocol/regmap、上/下 TX 唯一 ID。引脚如实配置**可以由 Codex 自行选取候选映射**，但绝不可以“自行认为电气验证已完成”。

---

## 4. 按键、启动和安全状态机（明确指定）

### 官方按键候选定义（须核实 Rev3）

- **PS KEY1**：`PS_MIO50_501 / B13`，低电平有效，承担人工**ARM / 授权预备**。建议长按 >=1.0 s，按键消抖和释放验证后生效；不可复用为异步硬件急停。
- **PL KEY1**：`IO_L21P_T3_35 / N15`，低电平有效，承担**CALIBRATE / 开始测量**。只在 `ARMED_SAFE` 且温度/供电/链路合规时长按 >=1.0 s 触发；不允许单按键直接开启所有 128 通道持续发射。
- 可将 **PL KEY2** `N16` 设为**软件 ABORT**，或按实际按键数量和 XDC 审核，用户可在软件上按 STOP；真正硬件急停依赖独立**常闭电气回路**，掉线立即断开上、下驱动有效使能。
- 该信号名称/球位来自 AX7020 官方手册，尚需 PCB Rev3 匹配。若复核不符，依据实际资料更新映射，保留 PS ARM + PL CALIBRATE 的语义分工。

### 状态机

`POWER_OFF → RESET_SAFE → BOARD_CHECK → ARMED_SAFE → CAL_SPARSE → CAL_QUALITY_GATE → CAL_READY → IDLE_TRAP → MOTION_EXEC → IDLE_TRAP`。

`FAULT_LATCHED/ESTOP` 可以从任何发射阶段异步进入（安全失能路径必须独立且有物理最坏延时验证）；`CLEAR_FAULT → RESET_SAFE` 要求故障源恢复 + 人工重新 ARM，**禁止自动恢复声功率**。

每状态必须有 entry/exit 条件、最长超时、relay/eFuse 输出、心跳、双板 PGOOD/FAULT、UART 断链动作、TX OE、local watchdog、恢复手段和日志码；所有传感器丢失按风险分类，不能用静态假读数让校准 PASS。任何阵列丢失 PGOOD、温度越限、超流/欠压、watchdog、硬件急停，**两侧一起停发**；采样异常则结束当前 calibration，安全退出。

### 核心安全流程测试

- FPGA 未配置、复位、PL 时钟停止、PS 程序挂起、UART 插拔、J10/J11 电缆脱落、上/下独立供电缺一、I²C 卡死、ADC BUSY stuck、RX 饱和、电源瞬变、eFuse 过热、温度传感器离线。
- 验证 DATA 单独断线/时钟短路/锁存毛刺等情形，不能仅监测通用心跳就声称所有物理线缆故障已覆盖。
- 硬件 KILL、看门狗、local OE 默认无效、复位消隐、单步驱动使能必须有门级及物理设计约束；候选仿真不能替代实板失电测量。

---

## 5. 温度/湿度测量与声速-相位补偿（正式模块）

### 必需硬件

| 位置 | 器件 | 角色 | I²C 7-bit 地址候选 | 位置/热设计 |
|---|---|---|---|---|
| 中央 PCB | `TMP117MAIDRVR` ×1 | 环境参考温度 `T_center` | 0x48（ADD0=GND） | 中央板**远离 ADC 电源与大功率热源**；如不代表声场真实空气温度，结构上引到板边通风测点 |
| 上阵列 PCB | `TMP117MAIDRVR` ×1 | 上侧声场附近 `T_up` | 0x49（ADD0=V+） | 接近发射面/气流但与 TC4427A 热源隔离；标明测到的是局部板附近温度 |
| 下阵列 PCB | `TMP117MAIDRVR` ×1 | 下侧声场附近 `T_dn` | 0x4B（ADD0=SCL） | 与上板相同布局和对应镜像几何；核对 ADD0 绑法 |
| 中央 PCB | `SHT45-AD1B-R2` ×1 推荐 | 空气湿度/二次温度交叉校核 | 0x44 固定候选 | 环境通风区域，避免凝露/驱动热量；作为**湿度质量增强**，不代替三颗 TMP117 |

需要统一 I²C 物理层：独立供电的三个板域、隔离/上电时序、开漏、合法上拉、电容/线长、漏电/倒灌、地址冲突、真实 ACK/CRC（SHT4x）、断电/卡死恢复；如果跨板单总线风险高，允许采用**中央控制器下三路可隔离总线/独立 segment**并保存逻辑地址，须论证实际可用的 PS/PL I²C GPIO 资源。既有 `INA226/TMP117` 监测地址及 SHT45 地址不得冲突。

### 声速模型

- 首版干空气估算 `c_approx(T) = 331.3 + 0.606*T_°C [m/s]`（适用性与不确定度标注）；有可信湿度与压力参数可使用带来源的修正公式，**没有实时气压传感器时必须标记 `pressure_assumed`**。
- 对温度梯度，可从三测点拟合/插值一种**带明确假设的有效传播声速**，例如沿上/下分层 `T(z)`，估计传播时间 `τ_i = ∫_path ds / c(T(s),RH,...)`，再算驱动传播相位 `φ_prop = 2π f τ_i`；路径积分离散化并与均温模型数值比较。三点不能观测完整三维温度场，不能宣称已测得任意 `T(x,y,z)`。
- 温度数据结构至少 `{sensor_id,location,timestamp,reading_C,uncertainty,status,staleness_ms,calibration_offset,provenance}`；计算每帧 `c_eff`、相位补偿差 `Δφ(T)`、温度置信度，纳入 LUT/phase solver 和 PC 校准报告。
- 确保相位量化（8 bit，mod 256）、收发两方向相位基准、requested/calibration 分离、atomic commit 不被温度更新破坏；温度突变按安全门限渐变/短暂 HOLD，不能在运动中突然替换半幅相位地图。
- 超温**驱动级安全**不可只依靠离开热源的 TMP117；驱动组热热点另用合适的模拟温感/热监测与本地硬件比较器（型号和阈值在选型计算后确定），保证 PS 卡死/传感器 I²C 断线仍能停发。
- 验收：传感器断线/冲突/CRC/读取延迟/极限值/温度梯度/湿度缺失，公式对比与参考实现、重复性测试、真实读数证据门禁；无实板温度不得报物理补偿 PASS。

---

## 6. 自校准：稀疏几何先行，逐路响应后续独立处理

### 6.1 扫描点选择与编号

在每侧 8×8 TX 上，行列 **1-based**：先按 `(1,1),(2,2),...,(8,8)` 主对角线 + `(1,8),(2,7),...,(8,1)` 副对角线，共 **16 个不重复 TX 位置/板**（8 为偶数，两条对角线不重合），可加入用户所述指定控制点/非共线基准 TX，提高几何可观测性；仍需事先通过 rank/SVD/条件数/噪声实验判断测点充分性，不足时**自动生成建议的额外 TX 测量位置**并等待用户配置，不偷偷输出确定的 6DoF。

- `UPPER_TX[r,c]` → `LOWER_RX[0..3]`，同一时刻**一个 TX 发射**，对侧四 RX 同步采样。反向 `LOWER_TX[r,c]` → `UPPER_RX[0..3]`。
- 两侧按 16 TX 计算：`16×4×2 = 128` 条候选有向 TX→RX 观测；仅对角线扫描，不是过去的 `128×4=512` 条**全通道**测量。
- 不要把同侧 RX 混进跨板几何的主方程；8 RX 的绝对位置、相对位姿、发射器方向、阵列物理辐射面中心和板间距按刚体几何/机械先验清晰建模。
- 每一次发送前检查 PGOOD、保护、温度、所有通道默认关闭，使用可控 burst（候选 16 周期/扫描流程以真实 40 kHz 器件 ring-up/down 测量为准），切换接收 blank，记录完整 timestamp，并在失败后立即 safe-off。

### 6.2 测量数据与模型

采集 `ADC0..3=UPPER_RX0..3`、`ADC4..7=LOWER_RX0..3`，8×16bit 同步数据；局部增益/开关、信号延迟和两板接收链参考延迟需作为待标定量。

- 40 kHz 单频相位只能给 `path length modulo λ`，`λ≈8.6 mm`；面对面约 100 mm 时**不可仅凭单频 carrier phase 得绝对距离**。
- 需使用机械几何先验 + 校验性的 ToF/宽带扫频/多频粗估 + 载波相位细化，明确 NU40C10T 共振带宽限制、系统 ring-up/down、ADC 采样时钟和 TX/RX 固定延迟不确定度；不能声称 38.5–41.5kHz 的小范围扫频能无条件得到毫米级绝对 ToF。
- 每观测记录 `tx_id,rx_id,board,cmd_start_tick,actual_tx_onset_tick,convst_first_tick,sample_period,raw_ref,carrier_frequency,temperature_vector,humidity,quality_flags,SNR,amplitude,phase,TOF_candidate,coarse_ambiguity,frontend_delay,source_commit,provenance`。
- 优先求 **两块阵列相对 6DoF / 间距 / 倾角 + 接收路径延迟/相位的受限拟合**，使用带界的鲁棒最小二乘、离群剔除、多初值及不确定度；对照固定夹具真值/参考模型测试 rank，带有接收链相位 gauge 的**非唯一参数必须显式固定锚点或标为不可辨识**。
- **稀疏对角线无法逐通道实测 128 个 TX 的相位/幅度/共振偏差**，因此要分级：`GEOMETRY_SPARSITY_CALIBRATED`（整体空间与稀疏路径有效）和 `FULL_CHANNEL_CALIBRATED`（另外执行全部 TX 检查、接收参考相位对齐且各通道质量通过）。不要把前者命名为后者。
- 用户本次**优先稀疏上电校准**，不得强迫每次启动跑 128 TX 全扫描；若未全通道测量则各 TX 单体校准标记 `UNMEASURED`，运行时按已验证的历史/默认校准质量限制可用功能，必要时要求一次维护校准。可让 PC 用户选择扩展扫描并显示预计用时。
- 自校准仅评估/构建声场**模型和可计算的 trap feasibility envelope**；8 RX 的离散数据不能直接证明任一点真实三维声压分布或小球位置。

### 6.3 校准结果与质量门禁

校准报告包括：8 RX 真实/名义坐标来源；上下板相对 transform 及协方差；工作频率候选/置信度；声速模型版本；每 TX phase offset、增益/通道 mask 与 provenance；usable spatial bounds（区分机械边界、模型可信区和实际已验证可悬浮区）；TOF 的非唯一性告警；体积网格预测 trap map（清楚标记 `SIMULATED`）；每次板间温差和时间戳。

定义最低 acceptance 试验：合成已知相对几何 6DoF、固定 seed、重复≥10 次、噪声/异常相位/坏通道/温差/缺测、留出非扫描 TX/RX 路径进行验证；误差阈值先写为基于 SNR、模型、仪器分辨率的**可论证门限**并独立锁定，严禁为了通过随意调宽阈值；不可辨识时 `CALIBRATION_BLOCKED_BY_OBSERVABILITY`。

### 6.4 声场陷阱求解器（不能只做单点相位同相聚焦）

- 复核既有 `STANDING_WAVE / FOCUS` 求解器：明确两个阵列的发射面法向、反相/同相的物理含义、距离传播、接收相位基准及每路 NU40C10T 声幅/相位响应；必须区分**声压最大值聚焦**与**对小球稳定的声辐射力势阱**，不能把一个“焦点”画在 GUI 上就当作可悬浮陷阱。
- 数学参考应至少能计算复声压 `p(r)=Σ_i A_i G_i(r) exp(jφ_i)`、幅度/相位/频率、声压空间梯度与合理的小粒子辐射势近似；对于具体泡沫球的密度、半径、压缩率、黏滞、流场和近场效应，明确模型假设适用区。稳定目标应评估 `F_acoustic(z)−mg` 是否可能平衡、附近恢复趋势、XY/Z 曲率、对电压/误差/温度的敏感度，并说明没有声压标定时只能做**归一化模型趋势比较**，不能计算可靠最大承载质量。
- 40 kHz、室温空气波长约 8.6 mm，而 `pitch=12 mm≈1.4λ`，大角度扫描可能出现栅瓣/副陷阱。因此工作空间 `x/y/z` 可控范围由离散相位阵列在频率/功率/偏差下的**仿真与实测**决定，不得预设整块 130×130 mm 区域均可以悬浮。检测副瓣、势阱消失、z 越界或相位步进突变应拒绝目标或降速。
- 8-bit phase LUT 的每档角度 1.40625°；要求数值参考与硬件 LUT 对比并验证取整、模 256、全 128 路原子提交、独立温度偏移的单调过渡、掉线和 fault 下的阵列停止。上、下阵列不能只对各自独立算相位而忽略共同载波、相对相位与时序。
- GUI 动态规划可采用低速路径，每个轨迹段按可配置最大位移/速度/加速度/jerk/相位图变化量自适应细分。阶段化验证：TRAP_VALID 定点 → 低速 XY → 自定义曲线 → Z → XYZ；只有真实质量测量及硬件压力/位姿证据才能提升为 `PHYSICAL_LEVITATION_VERIFIED`。

---

## 7. ADC / AFE / 数字协议

- 中央仅 1×8ch simultaneous ADC：**正式当前 ADC 是 `AD7606BBSTZ-RL`**；仓库有经初步研究推荐的 **`AD7606C-16BSTZ-RL` 高带宽候选**，但对应 Problem/Decision 尚待独立审查与用户正式批准。**不得擅自替换当前生产硬件/初始化 RTL 和 BOM 权威**。
- AD7606B 官方 8×16bit 800kSPS 同步采样；AD7606C-16 官方 8×16bit 1MSPS，有 25k/220kHz 两档模拟带宽。应单独做 38.5–41.5kHz（特别是 40kHz）幅相频响/群延迟/SNR/带宽和抗混叠对比；如果 B 造成不可接受的幅相衰减/变化，提交 `ADC_UPGRADE_DECISION_REQUEST`，复用现有四路 DOUT 协议，并生成兼容层，但不可默认为换型已批准。
- 每侧 RX 模拟前端：4 个接收换能器 → 保护（不能接功率 TX 结点）→ AC 耦合/输入限幅 → TMUX1574 消隐 → OPA4192 增益（候选 11/22 需饱和/恢复论证）→ 局部有源/无源滤波 → 屏蔽线缆到中央 ADC。REF5025 的 2.5V 是 RX 偏置基准，不能误写为 ADC 的参考输入。双板 RX 每路噪声/漂移/延迟单独记录。
- 继续保留现有 phase map / C ps_service / AXI / register_map / packet parser / CRC/seq/timeout/ACK / Capture ACK 流程，并新增可协商的 `GET_BOARD_CAPS`、`GET_TEMP`、`CAL_START`、`CAL_PROGRESS`、`CAL_RESULT`、`CAL_ABORT`、`TRAJECTORY_UPLOAD`、`MOTION_START/PAUSE/RESUME/STOP`，优先延展现有协议版本而非破坏兼容；必要时提供 v2 客户端拒绝不兼容命令的行为。
- 串口优先 **AX7020 板载 USB-UART / PS UART1 候选，115200 8N1**；COM 号动态枚举、校验 CP2102 的真实 USB 路线与 UART MIO、console ownership，不得填死 COM4 或直接把 XDC GPIO 假装 PS UART。
- 性能预算：115200 8N1 实际单向线路上限约 `11520 byte/s`；原始 1024帧×8ch×2字节 = **16384 B**，理想无开销传完约 **1.42s**，完整稀疏校准若每个 TX 全量回传需考虑时间/缓冲/压缩。优先 PL/PS 真实计算包络/振幅/相位/粗测摘要，按需下载 raw chunk（每块 CRC、序号、重传），不能伪造“板端已经提取”的结果。日志精确区分 `RAW_ADC` 与 `ESTIMATED_FEATURES`。
- 运动时优先在 PS/PL 的确定性 motion queue 调度已验证任务，**不可依赖 PC GUI 按 Windows 时钟逐帧实时 40 kHz 控制**。GUI 只发目标/轨迹/速限，PS 或 FPGA 生成/提交相位计划，硬件 atomic publication。

---

## 8. 上位机：由用户自己一步一步定义轨迹

基于 v5 现有 GUI（首选延用当前 Python/Tk 等稳定组件，不要无批准重写所有 UI），建立模块化视图：

1. **连接/诊断**：串口发现、连接状态、AX7020/固件/协议版本、SAFE/FAULT、电源/温度/ADC/校准状态；显式显示 `SIMULATION` 或 `HARDWARE`。
2. **自校准**：显示 3×TMP117/湿度、sound-speed estimate、16+16 TX 扫描点可视列表、接收波形/SNR、标定步骤、拟合误差、接收器位置与缺失证据、重测/中止按钮。
3. **声场坐标**：中央零点、上/下阵列、8 RX 标记、法线方向、0.1m 面距、XYZ 边界、点选 target；**预测声场/陷阱必须标注为数值模拟而非实测**。
4. **手动轨迹编辑器**：用户可逐点点击放置空间 waypoint、拖拽/微调 XYZ 或文本输入，编辑顺序和速度/加速度/停留时间；连接两个点为线段；Bezier/样条段由用户选择控制点与切线；闭合任意图形、撤销/重做、删点、插入点、分段重排。允许在 XY/XZ/YZ/3D 视角自由编辑，不预先写死直线/椭圆/圆形/三角形/矩形的坐标序列，也不能靠预制 CSV 冒充用户轨迹。**几何算法（线段插值/Bezier/样条/弧线）可以是通用数学基元，具体轨迹必须在运行时由用户输入生成**。
5. **运行与回放**：动态 path sampling（以曲率/加速度/相位跳变控制细分）、运行前 validation/预览、速度上限/加速度/jerk/安全边界/ADC 量程等、开始/暂停/继续/停止、预计时长、命令 ACK、队列余量、轨迹与实际提交点对照。断开自动安全停止，非自动恢复。
6. **保存/导出**：保存 JSON schema+hash+时间+版本+用户绘制顶点/控制柄+速度/边界+校准快照引用；再次打开编辑器可重建同样轨迹。旧 GUI 功能必须仍能回归。

**用户任务类型**通过几何/运动学定义实现而不是硬编码演示资产：定点、XY 直线、平面自由曲线、Z 方向、任意三维空间路径。不能宣称“运动的泡沫球实际走到了目标坐标”除非以后加入实际位置采样验证。

上位机应显示缺失硬件时 `HARDWARE_NOT_READY`、仅可 simulation/preview，避免 GUI 演示与真硬件反馈混淆。

---

## 9. Vivado/Vitis 2025.2 工程与可复制开发资产

**只在活动 `v5/` 内落地新源码、脚本、测试、状态与候选硬件资料。** 建议新建（文件名可按现有规范协调）：

```text
v5/
  config/ax7020_rev3_pin_candidate.csv
  config/ax7020_power_budget.json
  config/temperature_sensors.json
  config/calibration_scan_plan.json
  hardware/ax7020/revision3_evidence/
  hardware/interfaces/CENTRAL_ARRAY_SIGNAL_CONTRACT.md
  hardware/power/ARRAY_POWER_AND_INTERLOCK.md
  hardware/constraints/ax7020_candidate.xdc
  hardware/bom/working/<date>/...
  docs/pre_pcb/ARCHITECTURE_AND_SAFETY.md
  docs/pre_pcb/BOM_DECISION_MATRIX.md
  docs/pre_pcb/PIN_BUDGET_AND_TIMING.md
  docs/pre_pcb/CALIBRATION_OBSERVABILITY.md
  docs/pre_pcb/GUI_OPERATION_GUIDE.md
  scripts/ax7020_platform_preflight.ps1
  scripts/board_prepcb_validation.ps1
  tests/... (新增完整单元/集成/故障回归)
  evidence/pre_pcb_<date>/...
```

- 先解析官方 AX7020 2023.1 资料，区分 V2.0 公共原理图与实际 Rev3 板，验证当前运行 SD 镜像所有权。**当前板已有未知 PS/PL 在运行，非安全条件下不能使用 `ps7_init`、下载 bitstream、写 DDR、改变 boot/jumper/驱动或修改 QSPI/SD。** 用户允许的板上实验只能遵守当前项目另行授权且明确安全区的范围；缺少资格证据则离线工作并输出 blocker。
- 通过 Tcl 自动创建 Vivado 2025.2 PS7 + AXI interconnect + AXI-Lite/BRAM + 中断 + clocks/resets + RTL top + pin map；PS firmware 采用真实 Vitis 2025.2 可用工具链（查已安装 BSP/API）；必要时生成 `.xsa`、`.xpr` 与可复建脚本；禁止用 2023.1 XSA 直接冒充可下载 2025.2 BSP。
- 测试可重现性：固定 seed、同输入 Hash、重复次数、Icarus + Vivado XSim、C firmware host fixture、clean venv、无 `history_old` 依赖。禁止 stub/mock/synthetic 数据冒充真实 PS、实物温度或 ADC 结果；对不可硬件测量的部分可以 `ALTERNATIVE_VALIDATION`，明确证据等级。
- 尽可能完成真 Vivado synthesis/P&R/DRC/report_timing_summary + 时钟/CDC + min/max offchip timing；官方 2025.2 UG903 要求对外部时序使用 `set_input_delay` / `set_output_delay`，不能靠全部 IO 未约束就宣称 timing closed。无 Rev3/外部数据时报告 `TIMING_HOLD_MISSING_BOARD_FACTS`，绝不虚填约束数值。
- 记录 FPGA 实际资源（LUT/FF/BRAM/BUFG/MMCM）、32 lane IO 占用与保留、温度驱动资源、主时钟/外设时钟、可重复 bit-exact/phase exact-cycle 的测试结果。速度等级 -2 不自动证明 132MHz 路由通过。
- BOM 不覆盖原始提交：准备按板分类的新工作版 Excel（主控/上阵列/下阵列/外部器件/线束），列出 MPN、制造商、封装、数量、采购数量、需求电压/最大电流、输入/输出逻辑电平、封装证据、是否已测、货源、质量风险、用户批准状态；锁定 NU40C10T TX，每板 64；3×TMP117 正式保留；ADC 正式型号先不替换；RX 完整型号 `HOLD`；中央由 AX7020 供电和上下独立电源必须在 BOM 明示。
- 允许草拟 CAD 原理图模块图/逻辑 netlist/封装校核清单。**不在此任务内完成正式 PCB 布局/铺铜/Gerber/下单**。Native ERC 只有真实 EDA 工具执行后才能写 PASS；否则 NOT_RUN。

---

## 10. 分阶段执行顺序（Codex 可自主闭环普通缺陷）

| Stage | Goal / Allowed changes | Done When / Required evidence |
|---|---|---|
| **S0 — FACTS** | Repo/head、v5 现状、板卡 Rev3、速度/温度等级证据、来源与图纸、原始代码/BOM/阻塞 | 当前状态矩阵、无旧板依赖、来源等级、baseline 前的 Git/source hashes |
| **S1 — HARDWARE CONTRACT** | 3 PCB、独立供电、NU40C10T、RX/AFE/ADC、三温度、两按钮、完整逻辑 pin/signal/power 接口 | 通道数量/管脚预算无冲突、BOM 候选、功率预算和 unresolved 列表、无未知 5V↔IO |
| **S2 — OFFLINE PS/PL** | 正确 part、PS7、FCLK、AXI-Lite/BRAM、UART protocol、control/status、SAFE、时序 | 新旧数字 baseline 全 PASS，2 仿真器，Vivado2025.2 实际报告；若部署受阻明确 NON_DEPLOYABLE |
| **S3 — TEMP/ADC** | 3 TMP117+ SHT45、I²C 模型、ADC 捕获、温度积分声速及相位补偿、故障注入 | 多模型交叉、断线/陈旧/误码测试 PASS、真实数据与模拟严格区分 |
| **S4 — CALIBRATION** | 用户定义点/对角线、双向稀疏扫描、可辨识位姿解算、质量门禁、原始与特征报告 | 标定数值回归、秩/条件数/置信度、5+重复种子和坏数据拒绝；不虚称 FULL_CHANNEL |
| **S5 — PC UI** | 动态绘制轨迹、二维/三维 waypoint、用户控制柄、约束校验、串口任务队列/回放 | 无预制轨迹数据、可反复保存/加载、UI→protocol→phase-map 原子提交一体化仿真 |
| **S6 — INTEGRATION** | 联合固件与 RTL、断电安全、温度校准更新、协议故障及完整回归 | 全部原验收 + 新安全/GUI/温度/校准测试 PASS；无 placeholder/硬编码旁路 |
| **S7 — HANDOFF** | 归档 evidence，更新 shared、DECISIONS/BLOCKERS/ACCEPTANCE/CONTEXT_CHECKPOINT，推送已审核提交到同 Repo 的正常开发分支 | clean reproduction、commit/branch/hash、远端一致、Blockers、Review 状态、PCB ready NOT_RELEASED |

工作持续时无需每个小 bug 提问；同一重大问题连续 2–3 轮无实质进展，停止暴力迭代，做 RCA/复核前提/对比基线，再写正式 `AI-problem/problem/P-YYYYMMDD-NNN__topic.md`，附 hash/版本/证据，待 ChatGPT 决策及用户必要批准。

---

## 11. 硬性 Acceptance / Quality Gates

**不得只靠 Codex 自述完成。** 必须核实：

- [ ] 既有完整数字基线不回归：≥115 项既有 Python 单测（按真实最新仓库可新增）、3 Icarus + 1 XSim、每轮 3696 帧与 golden canonical hash/phase exact-cycle；所有旧已通过测试应在新活跃工作区重跑并保存日志。
- [ ] 三 PCB 与 `v5` 接口合同完整（128 TX/8 RX/32 lanes×4 used/独立 12V 功率供电/central AX7020 供电预算/温度）；所有候选 MPN 无 silently assumed 换型。
- [ ] 按钮/安全启动/急停/双侧联锁、失电和温度异常在独立参考模型及 RTL/TB 均有测试；未到实板前标签仅 `SIMULATED`。
- [ ] 3×TMP117 必需且参与 `sound_speed → propagation time → φ_comp → phase map` 的**真实软件代码路径**；中心温度不是 UI-only。
- [ ] 稀疏校准测量点、TX↔对侧 4RX、时序、秩/观测性、TOF 相位模糊、两个 gauge、坏数据拒绝与分级结果均验证。
- [ ] 用户能在 GUI 手动创建完全新的任意折线/Bezier 曲线/XYZ 路径，保存、重载并得到一致轨迹；存在预设示例仅能作测试，不能代替用户实时自定义功能。
- [ ] 40kHz 载波、motion tick 和 PS-UART 各有独立吞吐/延迟预算；低速 UART 不阻塞 PL 40kHz 相位更新。
- [ ] AX7020 `-2/I`、J10/J11、PL/PS KEY、PS UART、PL 时钟、Bank VCCO、PS DDR、Rev3 匹配有明确 VERIFIED/CANDIDATE/BLOCKED 字段；生产 XDC 不得伪造。
- [ ] 独立 clean checkout + clean environment 再执行基本回归，证明不依赖 `history_old` 或旧本地沙盒。GitHub 同一个 Repository 的新分支应正常同步并核对提交 SHA；不强推、不重写、不自动合并用户要求单独批准的迁移 PR。
- [ ] 关键跨层链路需 2 类独立证据（仿真器交叉/软件参考/真实 Vivado），物理数据若缺则 `ALTERNATIVE_VALIDATION`，不可冒充 real hardware。
- [ ] 不改测试阈值迎合实现；没有 stub/mock/synthetic 用于冒充通过；历史/当前状态分离；新 docs 无老 Robei/EBAZ 影响当前实现。
- [ ] **最终状态**：PCB 前阶段可 `ACCEPT WITH LIMITATIONS`（现阶段软件/FPGA 部分合格但待硬件）；全平台/真实声学仍应 `REVISE`，直到真实电气及声场/悬浮证据到位。严禁把“PCB 之前准备完成”等同“实际悬浮系统完成”。

### 必须交付给用户的结果文件

1. `PRE_PCB_COMPLETE_REPORT.md`：已完成与证据等级；未完成及原因；功能覆盖率/风险；数字/工具报告/测量/版本/日期。
2. `AX7020_REV3_PINMAP.csv` + 候选 XDC/可选生产 XDC（仅电气完成后）+ `PIN_PROVENANCE.md`。
3. `CENTRAL_ARRAY_HARDWARE_CONTRACT.md`、独立电源/保护/地/线束图、两侧一致性设计说明。
4. `BOM_AX7020_NU40C10T_PREPCB_WORKING.xlsx`，原版不覆盖；电源器件/数量/封装来源与热审计。
5. `TEMP_COMPENSATION_VALIDATION.md`、`SPARSE_CALIBRATION_VALIDATION.md`、自校准数据结构 JSON 与原始/模拟数据来源示例。
6. `GUI_USER_DRAWN_TRAJECTORY_GUIDE.md`、应用启动命令、至少五组**运行时手动输入**案例和可重放数据。
7. PS/PL/GUI/UART 全栈构建/测试脚本、Vivado2025.2 `.xpr` 可重建输入及 synthesis/implementation/timing/CDC 明确日志（哪一步缺事实不得伪装）。
8. `PRE_PCB_OPEN_BLOCKERS.md`：每个 blocker 的需求事实、证据、影响、可完成部分、用户决策需求，关联当前 AI-problem；`CONTEXT_CHECKPOINT.md/json` 以及 GitHub 最终提交/分支/同步回执。

### 停止与回报要求

当**现阶段**不存在可通过离线工作减少的阻塞、核心数字链完整、两类独立证据达标、当前阶段验收满足且质量约 90% 时，执行 `STOP_OPTIMIZATION_AND_DELIVER`，余下需 PCB/实板测量的事项写入下一阶段 blocker，而不是无意义地继续拓展功能。最后给出规范结论 `ACCEPT / ACCEPT WITH LIMITATIONS / REVISE`、`Blocking/Critical`、原先和新增测试数据、资源占用、时序余量和真实证据位置。

---

## 12. 正式资料索引（执行时重检版本，作为非仓库长期外部参考）

| 官方/可信来源 | 在项目中的用途 | 来源限制 |
|---|---|---|
| ALINX AX7020 2023.1 用户手册 `https://ax7020-20231-v101.readthedocs.io/zh-cn/latest/AX7020UserManual_CN/AX7020UserManual.html` | J10/J11 2×20、每侧 34 GPIO、PS KEY1 MIO50 B13、PL KEY1 N15、PL 50MHz、PS 参考、UART | 对应公共板版次与 Rev3 的差异，需实板核验 |
| ALINX 官方资料库 `https://github.com/alinxalinx/AX7020_2023.1` | 旧版硬件原理图、PS DDR/IO 参考、2023.1 示例 | 参考资料而非 Vivado2025.2 可直接部署工程 |
| AMD Vivado 2025.2 UG903 `https://docs.amd.com/r/2025.2-English/ug903-vivado-using-constraints/About-Constraining-I/O-Delay` | IO min/max setup/hold 真实约束 | 需用户实际器件、外设/线束数据 |
| TI TMP117 `https://www.ti.com/product/TMP117` / `https://www.ti.com/lit/ds/symlink/tmp117.pdf` | 三温度传感器、地址、精度、热布局 | 不能将 PCB 温度无条件解释为空气温度 |
| Sensirion SHT45 `https://sensirion.com/products/catalog/SHT45` | 环境湿度/温度质量增强 | 不等于压力传感器 |
| ADI AD7606B `https://www.analog.com/en/products/ad7606b.html` | 当前 ADC 正式器件 | 40kHz 模拟幅相链待测 |
| ADI AD7606C-16 `https://www.analog.com/en/products/ad7606c-16.html` | 高带宽候选，25/220k 模式 | 换型需用户审核 |
| Microchip TC4427A `https://www.microchip.com/en-us/product/TC4427A` | 双通道候选驱动 | 不证明兼容具体 NU40C10T 连续功率负载 |
| TI SN74AXC8T245 `https://www.ti.com/product/SN74AXC8T245` | 两电源域数据电平转换与断电隔离 | 任一电源最多 3.6V，不是 5V translator |
| NU40C16T/R 旧 PDF `https://files.seeedstudio.com/wiki/Grove_Ultrasonic_Ranger/res/NU40C16T-R-1.pdf` | **只作反例**：确认它不是 NU40C10T | **禁止套用**其 16mm、80Vp-p、压电参数 |
| Marzo et al. acoustic traps `https://www.nature.com/articles/ncomms9661` | 相控阵声陷阱与相位聚焦理论研究 | 不能替代具体硬件声压/悬浮实测 |

## 13. 最终执行指令

**现在开始：先完成 Stage S0 和 S1 的真实性核对，在同一 v5 内有界推进 S2–S7；可自主修复普通实现错误，保留原始失败证据。** 在缺少可安全操作的实际板级条件时，集中完成软件/RTL/算法/GUI/接口/候选 pinmap/功率电气审查和真实 Vivado 离线测试，并如实停在物理 blocker；不得为了“所有功能已完成”伪造 ADC、温度或声学数据。不创建新版本，不改变正式仓库，不使用强推，按用户已授权的正常工程变更将可验证增量同步到同一 GitHub Repository 的开发分支，提交最终验收包供用户审阅。
