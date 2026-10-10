# SonoField-FPGA v5 — AX7020 JTAG/UART 实板闭环、AD7606C-16 正式换型、NU40C10T/R-2 资格验证与三板原理图一体化执行指令

> **执行对象**：Codex 6.1 Sol · Extra High / XHigh。  
> **任务类型**：`CONTINUE_CURRENT_VERSION`，**始终 v5，不进入 v6**。  
> **PROJECT_ID**：`SONOFIELD_FPGA`  
> **Repository**：`https://github.com/loverlike1216/SonoField-FPGA.git`  
> **正式工具链**：Vivado 2025.2；配套 Vitis 2025.2 / 合格 ARM 工具链；Windows 默认 PowerShell 7 (`pwsh`)。  
> **用户当前环境**：AX7020 的 **JTAG 和 USB-UART 均已接入电脑，Vivado 2025.2 已打开**。先检测这些真实端口与既有会话，不要因已连接而默认可写/可覆盖。  
> **推荐工作区候选（以真实 Git 核对为准）**：`E:\Codex_project\AMD_Sonofield`。原沙盒 `E:\Codex_project\AMD-SonoField-FPGA` 保留冻结，不得修改。  
> **授权性质**：本文件明确授权在当前 v5 新开发分支内实施可逆的软件/RTL、ADC 适配、文档、BOM 和原理图候选开发，以及安全的只读实板检测；**没有授权未经核实的 CPU halt/reset、下载覆盖已有运行镜像、写未知 DDR、改 SD/QSPI/启动方式、带电超声功率输出、正式采购制板或合并 main**。影响既有程序/硬件状态的步骤必须单独说明后等待用户确认。

---

## 0. 本轮必须采纳的正式用户决定（Decision 输入）

### D-NEW-01 — ADC 正式换型，已获用户明确批准

- v5 **正式 ADC**：从 `AD7606BBSTZ-RL` 改为 `AD7606C-16BSTZ-RL`（订货后缀仍要与原厂数据、采购包装和 CAD 封装确认）。
- **仅一颗中央 ADC、8 路同时采样**；UP 4 RX + DOWN 4 RX；先评审并尽可能保留 4-DOUT serial 接口与原有 1024×8×16bit 捕获抽象。新 ADC 的真实寄存器协议和转换时序应单独适配。
- 用户的当前指令是**正式换型授权**，覆盖既有仓库里“AD7606C-16 pending user approval”旧状态。Codex 必须在当前 `shared/DECISIONS`、当前 BOM/硬件配置、版本状态和 `AI-problem/decision` 路径中按工程流程持久化；**历史原始 BOM、旧版证据及 frozen files 不可篡改**。
- 如 `P-20261008-001` 有 Problem Hash，读取问题原件，核对版本与内容；用户决定为方向授权，不可伪造 Problem Hash 或假称其他审查已经通过。若旧问题证据冲突，标 `REVALIDATE_DECISION` 并将电气/寄存器/实物门禁保留。

### D-NEW-02 — 换能器及供电布局

- 正式 TX 系列为 **NU40C10T**；用户新提供的供应商图片具体标为 **`NU40C10T/R-2`**。建表时将 `NU40C10T-2` 发射候选与 `NU40C10R-2` 接收候选**分别建档**，向供应商确认确切 T/R 订货编码，不得把合并规格表等同于各自的独立实测规格。
- 两块阵列 PCB 各自**独立外部 12 V 电源输入**、保险/限流/欠压/过压/温度/失联安全硬件。AX7020 **仅控制数据与信号**，绝不为 TX 功率级供电。外部 `12 V / 5 A` 每侧只作为可用电源容量候选，**不是负载实测、不是必须持续消耗、不是已审定保护电流**。
- 中央板按用户要求**仅由 AX7020 扩展口供电**。必须从 Rev3.0 板卡资料、接插件电流、AX7020 剩余电流、供电上电序列和实测预算证明其可行；若不足则 `CENTRAL_POWER_BUDGET_BLOCKED`，提出对比方案并请求用户批准，**不擅自新增中央独立供电**。
- 三块 PCB：中央接口采集板×1；**上/下尽量用同一块阵列 PCB 设计和装配配置**。每侧 `8×8 = 64` TX，加外围 4 RX，合计 `128 TX + 8 RX`。每侧的4RX为阵列外侧四角，实际坐标需机械图与用户草图核对。
- 环境参考 `TMP117 ×1` 放在**中央板气流代表位置且远离热源**；上/下阵列各 `TMP117 ×1`。三温度均参与声速/相位；SHT45 湿度为辅助输入，其模型没有验证前只作诊断。

### D-NEW-03 — 本轮重点

- 用户现已连接 JTAG + UART、打开 Vivado2025.2。优先打通**安全只读识别 → 真实串口 → 条件满足时的 PC→UART→PS→AXI→PL→PS→UART→PC**。同时推进 ADC/AFE 与硬件候选和可执行 GUI/软件；尽量一次闭环所有当前可执行任务，但必须按 Gate 决定是否实际操作硬件。
- 用户提供测量：信号源 40 kHz 正弦、标称 10 Vp-p，T/R 相对约 5 cm；自动测频多数 39.68 kHz，移动器件偶见 40.00/40.32 kHz。**这是初步观测**，不是电声共振测量或正式工作频率，更不代表声波传播导致频率偏移。先确定测量原因并给无 FPGA 的入料测试 SOP。
- 目前没有授权合并 PR #1/#2/#3 至 main，也不允许自动开启下一版本或制造放行。

---

## 1. 强制 Repository Reconciliation（Gate 0：先执行）

在任何改动/操作前，真实读取 GitHub 和本地：

1. `git remote -v / status --short / branch -vv / rev-parse HEAD / log`、remote `main`、所有活跃 PR/commit/ancestor关系、是否存在工作树未提交内容；备份有意义的本地未提交/未跟踪成果，禁止粗暴 clean/reset。
2. 特别核对（以下为 **2026-10-10 检索得到的参考**，不是永远固定 HEAD）：
   - `main = ecd32e76e9b6...`；
   - PR #1 `chore/v5-ax7020-workspace-isolation` HEAD `d7f7b60ae8ed...`，`base=main`，DRAFT/OPEN；
   - PR #2 `feat/v5-prepcb-full-system` HEAD `7dda49f00983...`，`base=PR#1`，DRAFT/OPEN；
   - PR #3 `codex/v5-historical-project-isolation-20261009` HEAD `b08ccf58c984...`，`base=main`，**已包含 PR#1/#2 的祖先提交**，DRAFT/OPEN，归档路径 `Historical project/`。
   - 对 PR#3 分支 `v5/` 当前 `shared/PROJECT_STATE.json` 记录的执行工作区 `E:\Codex_project\AMD_Sonofield`；迁移独立复现累计 171 tests、3696 frames ×4、Vivado OOC 证据通过，**所有以上均是候选，不是主分支合并或实板验收**。
3. **如 PR#3 仍包含 PR#1/#2 且当前新沙盒使用该分支**：以 PR#3 HEAD 建立**新的下一阶段开发分支**（例如 `feat/v5-ad7606c16-real-pspl-nextgate`）；不得从 `main` 重做 v5，也不得对 PR#1/#2 再做重复 cherry-pick。PR#3 必须单独审查，不能在无批准下合并。若远端祖先关系已变化，以最新 Git 事实重算并记录替代策略。
4. 默认只读当前 `README.md / AGENTS.md / shared/PROJECT_STATE.* / VERSION_STATE / CONTEXT_CHECKPOINT.* / CURRENT_PLAN / DECISIONS / ACCEPTANCE / BLOCKERS / AI-problem/problem 与 decision / v5/` 及最新报告；**不要读取 `Historical project/` 历史正文**。仅在用户明确授权或审计必须读特定文件时定点访问；本轮默认不需打开旧 Robei/EBAZ 源码。
5. 核对并维护当前真实证据路径：`v5/docs/pre_pcb/PRE_PCB_COMPLETE_REPORT.md`、`PRE_PCB_OPEN_BLOCKERS.md`、`v5/evidence/pre_pcb_20261009/FINAL_VERIFICATION.json`、`v5/evidence/board_bringup/20261009/RESULT.md`、`v5/config/board_facts.json`、`v5/hardware/prepcb/AX7020_REV3_PINMAP.csv`、`v5/config/SIGNAL_CONTRACT.json`、`v5/hardware/bom/working/2026-10-09/prepcb/`、`v5/scripts/run_baseline.ps1` 与 prePCB runner。
6. 不将旧版 `shared/` 中遗留 v2 叙述视为当前电气结论。确认当前 v5 被审定的文件优先，保留原始信息的引用来源。
7. 固定迁移前所有受保护 RTL/C/协议/测试/golden/原始 BOM 的 SHA256、工具版本和运行配置。先跑可复现**完整前测**，否则不得比较迁移回归。

**Gate 0 Done When**：提交 `REPOSITORY_RECONCILIATION.md`、基础 commit/PR 图、当前工作区、安全 Git 状态、版本、唯一活动 v5、已有 PASSED 和 13 项未关闭门禁。若没有最新 git 访问则标 BLOCKED，不得补猜。

---

## 2. 架构固定约束和本轮不做事项

### 2.1 绝不破坏的功能

- TX =128，RX =8；上下对置 8×8+8×8；辐射面中心 pitch=12 mm，面间 nominal=100 mm，可调90–115 mm；原点为两板几何中心。每板 TX XY 为 `[-42,-30,-18,-6,6,18,30,42] mm`；RX 角落 `(±54, ±54) mm` 是**候选坐标**而不是已确认机械样件。
- 32 串行 lane × 4 有效输出；128×8-bit requested phase 和独立 calibration phase；公共时基、全图原子提交/ACK、故障锁存、安全默认 OFF、位精确 golden、已有寄存器及 PC 协议不破坏。
- Host 只提出声场/轨迹参数，**40kHz 输出和运动队列由 PS/PL 本地定时**；原来动态点/贝塞尔/XYZ 用户自绘 GUI 必须完整保留，不允许换成预制路径冒充。
- 既有稀疏几何校准（16+16 对角/对侧四 RX，128 定向路径）**不等价于** 128 TX 全通道电声幅相校准。实际阵列中两侧接收器的相位参考（gauge）独立，粗 ToF/已知几何解除周期模糊后才允许细相位使用。
- 无真实球体位置检测时，系统仅可声称**开环运动指令/声场模型控制**，不能称粒子跟踪闭环。

### 2.2 本轮 Non-Goals

- 不开启 v6、不删除 frozen 版本、不读取历史目录正文；不代用户批准 PR main 合并或正式发布。
- 不以现有已配置 PL 为 SonoField bitstream 的运行证据；不改原 SD 镜像、永久 Flash/Boot、JTAG/Windows 驱动、未知 DDR RAM 或未知 IO。
- 不为追求 100% 而制造 40 kHz 驱动板、输出高功率、连接 TX 功率级，或凭模拟归一化势声称 50 mg 悬浮。
- 原生嘉立创 EDA 工程只在工具/真实库与引脚齐全时生成、运行**真实** ERC；没有 CAD 环境时生成可审查符号网络合同与阻塞，不假冒已完成 ERC/DRC/Gerber。

---

## 3. Gate A — 当前连线下 AX7020 JTAG + UART 安全资格检测与条件性实板闭环（最高优先级）

### A0. 不破坏板上现状的自动识别

先辨认当前 Vivado2025.2/Hardware Manager 实际已连接的 adapter 和 target；确认 `AX701020.3.0 / PCB Rev3.0` 的用户照片与板号；只读 IDCODE、ARM DAP、PL DONE/EOS、PS clock/reset/boot 控制状态和**可安全读取的寄存器**。若检测有当前程序正在运行（历史证据两 Cortex-A9 RUNNING、SD boot），不得自动 halt/reset/init。原有窗口保持，不在未说明情况下关闭或启动其他 Vivado 占用硬件。

同步在 Windows 使用 PnP/设备管理器/PowerShell 查询新增 USB-UART VID/PID、芯片驱动、COM号与热插拔差分（不假定 COM4/FT2232，也不把 JTAG-HS1 当串口）；确认使用合适数据线与 USB-UART 物理接口。官方 CP2102 + PS UART1 / MIO48–49 **仅为待核对的参考**；核对 Rev3.0 原理图/接口资料、MIO、VCCO、RX/TX方向、GND 和 DTR/RTS 是否可能控制复位后才安全打开 COM。默认 `115200 8N1，无硬件/软件流控，不主动切换 DTR/RTS`；禁止抢占用户串口/自动发送危险控制命令。

若无 COM：依序区分线材/接口/枚举/驱动/设备被占用/USB-UART wiring，而不是直接推断 AX7020 损坏。保留 `Windows/USB PnP`、`Vivado/XSDB` 与时间戳、工具版本、截图/日志（公开时脱敏设备序号）。

### A1. 审定实际板级平台和目标工具链

需要来源匹配 **Rev3.0** 的完整 FPGA 型号、速度/温度等级（用户确认目标 `-2 / I`，仍需核验具体实物芯片标识）、DDR 厂牌/容量/拓扑/timing、VCCO、PL 50MHz U18、PS 33.333MHz E7、PS7 preset、UART1 MIO、J10/J11 68GPIO、时钟/复位/启动配置。旧 V2.0 schematic、2023.1 XSA 的 Micron vs 手册 Hynix DDR 冲突必须保持 OPEN，直到有厂商或实物证据。132MHz 是 PLL/FCLK 内部目标，不是板载振荡器。

检查 Vitis2025.2 实际 ARM cross compiler / xsct / system software platform / linker / BSP/FSBL/OCM RAM 策略，不能因工具启动 exit0 就把含 traceback 的执行判为 PASS。真实编译 `arm-none-eabi-gcc` 或实际合格 compiler，显示输出 target architecture 和生成 ELF 可读结果。初始化/写 RAM 需要满足 A2 门禁。

### A2. 物理写入授权门禁（不可跳过）

以下所有条件满足，才可提出下一步**临时非持久化、隔离外部输出**的实板测试方案：

1. 实板完整 FPGA / PS / DDR / 复位/IO事实获得匹配来源，生产或临时 XDC 和时钟可审查；有可信硬件镜像、其来源/所有者与启动控制策略。
2. 已确认已有 SD/PS/PL 程序能否被安全暂停/替换、谁使用 RAM/CPU，以及是否有无副作用的 OCM/指定空间；事先备份合法可读的配置与恢复方式；未确认则 `RUNNING_IMAGE_OWNERSHIP_BLOCKED`。
3. 所有外部功率/超声输出均断开，安全输出默认 LOW/Hi-Z 的行为由独立线路/约束证明，不以仿真 OFF 代替实物 OFF；在不接功率阵列时做限界测试。
4. 凡需 halt/reset 两个 ARM、ps7_init、下载临时 bitstream、下载 ELF 或写 RAM，**先给出操作清单、影响、恢复步骤并请求用户这一次明确许可**，不把本指令的一般“尽可能实板测试”当作许可。SD/QSPI/BOOT 更改另需单独批准。
5. 任何事实缺失立即在 A2 STOP；继续跑其他纯软件/ADC/原理图工作，不允许停住全部任务，也不准填造 PASS。

### A3. 符合 A2 后的有界实板闭环测试

按由低风险到高风险：实际 UART loop/echo（不可假定旧运行镜像支持）→ 读板版本与 SAFE → 真 PS 到 AXI 寄存器读写（安全影子寄存器；写入必须避开现有运行程序）→ phase requested/calibration map 的整图提交和 ACK → 100/1000 次 CRC/sequence PING/PONG → 时序/掉线/超时/软安全锁存/恢复 → GUI UART 协议兼容性。测试先用**板内存/寄存器模拟输出**，不产生超声功率输出。

必须记录：bitstream/ELF source hash、Vivado/Vitis 版本、实板ID、COM和波特率、发送接收原始日志、丢包、ACK、时延分布、100/1000 次 PASS 标准、故障处理、GPIO物理输出已安全隔离证据。未授权/资料不足则 Gate A 结论 `READ_ONLY_PASS / TARGET_BUILD_PASS|BLOCKED / REAL_TRANSPORT_NOT_RUN`，不可冒充实板闭环。

---

## 4. Gate B — AD7606C-16 正式数字/模拟系统迁移

**优先复用** AD7606B 的寄存器总线抽象、8ch/16bit/4DOUT/缓存 ACK 和 PS 数据接口，**器件特定**的启动、模式、时序、校准和读回由 `AD7606C16` adapter 隔离；不得直接仅重命名。

### B1. 正式器件参数（基于 Analog Devices Rev.A 原厂资料；实施前再校对）

- 正式 MPN 候选：`AD7606C-16BSTZ-RL`，LQFP-64 订货/焊盘/Pin1/裸焊盘视具体原厂封装图确认；8 路 16-bit 同步 SAR；最高标称 1 MSPS/ch；AVCC 标称 5V，VDRIVE 与 Rev.A 电平/时序核对；每通道可选 ±5/±10 等量程。
- **默认低带宽 25 kHz (-3 dB) 不适合无补偿测 40 kHz**；正式使用**高带宽 220 kHz (-3 dB，量程相关：某些小量程可能150kHz)**，留出实际 40kHz 幅相校准预算。`BANDWIDTH` **寄存器 0x07、bit7..0 对应 CH8..CH1**；8通道全部打开需写 `0xFF` 并读回。
- 软件模式：`OS[2:0]=111`；Serial `PAR/SER SEL=1`；`CONFIG` register `0x02` 的 `[4:3]=10` 是 **4 DOUT**；保持 status header/CRC/oversampling 默认为与 frame model 一致，精确完整写值由驱动依据 datasheet 保留位合成并读回校验，不能盲写来源不明的旧 B 初始化字节。
- CONFIG reset、BANDWIDTH reset、输入量程、reference/regcap、analog bias、BUSY/CS/SCLK/SDI edge、serial register read latency、analog acquisition latency、DOUT source-synchronous max/min 等必须以 AD7606C-16 Rev.A 实表重新推导；编写**独立 state machine、参考模型、寄存器 readback sequence 和 fail-closed**。建议初期保持原 800kSPS/32bit per DOUT profile，是否可实现由实际 SCLK 和上板时序证明；不得因为新芯片最高 1 MSPS 就默认现有 PL/线束能跑 1 MSPS。
- 8×16bit×800kSPS=**12.8 MB/s 原始数据率**。115200 8N1 UART 有效上限约**11,520 B/s**（不含封装开销），无法持续发送完整 RAW_ADC；使用 1024帧×8×2=**16 KiB** 有界缓冲，安全 snapshot、metadata、ACK/backpressure、分批读取/主机读取完成后重用；相位/时延/健康摘要作为实时串口信息，不改变本地采样时钟。
- 推荐对 40kHz 用幅度、群时延、跨通道相位（参考探头+AFE+ADC 校准）定量对照旧低带宽假设；分离发射器响应、接收器响应、AFE及 ADC filter phase delay。**不可用 high-bandwidth 参数替代测量证据**。原厂 Rev.A 的典型 highBW phase delay ~1.1µs/匹配 ~30ns 是设计参考，不是完整测量链延迟。

### B2. RTL / PS / 软件 / BOM 可变更范围

允许：v5 AD7606C register constants、init ROM/state sequencing、读写/自检/错误码、DOUT mapping、捕获 path 的器件 adapter、板级电源/参考与引脚合同、C 服务 parse/config、GUI 版本/状态、BOM 工作副本、硬件配置和文档、增量回归/仿真 model。

禁止：随意改变 128TX 相位核心、加速/轨迹协议、buffer ownership、原测试 golden 和阈值；如确需改共享协议则给正式 `ARCHITECTURE_DECISION_REQUIRED` 并证明兼容迁移/版本字段。

新增有意的**ADC B/C 差异测试**：每通道高/低带宽开关、`0x07`全开且读回、4-DOUT 格式配置、负数/正数边界码、连续转换、BUSY超时、错CRC/错寄存器/设备不响应、错源选通、上电/复位/失电、参考电压/模拟量程、时钟偏差与跨通道采样一一对应。使用 Icarus + Vivado XSim 两套实际仿真；需要新 golden 时保留旧 B golden 的**历史来源**，不得改旧 golden 迎合实现。

### B3. 原理图必要电气审查

中央保留单 ADC。审查 AD7606C reference / REFCAP / REGCAP 去耦、电容额定/ESR、AVCC5V与VDRIVE、3.3V/IO匹配、地回流、差分或单端输入选择、独立 8 路 AFE 的动态范围、150/220kHz 带宽和保护对 40kHz 的影响。上/下阵列模拟传输为屏蔽对线与明确定义的 return，不跨 12V TX 节点采样。设计 AFE 单通道可重复 RC、gain、phase reference/blank、抗混叠（需单独设计，并非仅 ADC on-chip 220kHz 截止即足够）。

B 只在数字仿真完成时标 `DIGITAL_ADAPTER_PASS, ANALOG_UNVERIFIED`；没连真实 ADC 不得称同步采样实测。

---

## 5. Gate C — NU40C10T/R-2 参数锁定、驱动、电源/热、入料筛选

### C1. 用户供应商图片的可追溯**输入参数**（不要当成原厂认证/每批实测）

| 项目 | 用户图片读数 | 注意 |
|---|---|---|
| 型号图片 | `NU40C10T/R-2` | T/R 独立核对的候选，发射实际要求 NU40C10T |
| 开放型 / 收发分体 | Open type / TX & RX separate | 不混淆 T 与 R |
| 频率 | `40.0 ±1.0 kHz` | 不是所有器件 40.00kHz 共振 |
| TX 声压 / RX 灵敏度 | `110 dB min` / `−68 dB min` | 厂家测试距离、条件需核对，两个指标不能互代 |
| 电容 | `2200 pF ±20%` | 区分适用 T/R、测量频点及等效电路 |
| 最高输入 | `40 Vp-p` | **不是推荐连续驱动电压**；VDRV12V起点仍须限流实测 |
| 方向角 | `80°±15° (-6dB)` | 测试条件、阵列耦合待实测 |
| 温度 | 工作 -20..80°C；存储 -40..85°C | 热峰值需独立保护 |
| 结构 | 外径 Ø9.8±0.5mm；高7.0±0.5mm；脚距5.0±0.5mm；脚Ø0.7±0.1mm；脚长7.0±0.5mm | 真实打样前逐批测量；孔径/封装公差、装配/倾斜/隔声脚距必须核验 |

对 12 mm pitch，最大壳体直径约 10.3mm，理论邻体直径余隙仅 **1.7mm**，装配偏心/塑壳/焊锡/排布须实测；TX 封装不能机械套用 TCT40 或 NU40C16。4 RX 外侧角点不得与安装孔、线束、保护件相撞。供应商资料测试距离/探测精度是测距应用参数，**不证明驻波悬浮力或工作区**。

### C2. 39.68kHz 测试现象 — 优先排查测量系统

在同一信号源锁定 40kHz 且无故意频移的条件下，接收波形移动改变主要是相位、幅值、路径/反射与 SNR；不应无依据解释为某一颗换能器的固有中心频率“跳变”。对 `39.68,40.00,40.32 kHz` 间隔约0.32kHz的读数先做：

1. 示波器 CH1 并联/观察**实际信号源输出频率**，CH2 R 输出；分别保留实际采样率/记录长度/频率计量法/阈值与自动测频数据。
2. 核对信号源 50Ω与Hi-Z 设置造成的实际 Vp-p 差异、输入输出地/负载、AC/DC耦合、示波器触发、低 SNR、零交叉/FFT 稳定性；频率对比以 CH1 校准。
3. 固定两器件夹具的距离(约5cm候选)、朝向、环境和极性；先固定 Tref 扫 R，再固定 Rref 扫 T；每批复测参考配对。
4. 用相同实际电压、受控短 burst 和足够 settle 的 39–41kHz扫频（38.5–41.5kHz更宽区间可作探索），记录接收幅值/相位/重复性、峰值频点以及离群情况；仪器不得超出有效/额定条件。
5. 记录每颗 SN、批次、身高/外径/脚距/静态 C（有 LCR meter 才做，普通万用表不可冒充阻抗频扫）、通道电压、测试图谱和 pass/fail 判据；不根据一次 `39.68kHz` 改系统工作载波。

### C3. 数字驱动及供电的真实预算

64× `TC4427A`（每颗双路，上一下各32）、32× `SN74LVC595A`（每侧16）仍是**现有数字设计的候选**；物理驱动拓扑是否直接驱动 NU40C、峰值/均方根电流、器件输出摆幅、上升沿、相位一致性、振铃、功耗、负载频散需 review。高频 `66MHz` 是外部串行钟候选；必须有完整 setup/hold、扇出、线缆、IO VCCO 和示波器证据。

以 2.2nF 作为暂估负载可做**参数化** CV²f 能量/动态电流敏感度分析，但压电换能器为有谐振损耗的电声负载，**不能将该理想电容公式视为实际连续电流/声功率/器件温升上界**。上/下外部 `12V5A` 为源额定能力，不表示既有 **2A eFuse** 可以承载 5A。要求做供电树预算表（工作/峰值/启动/异常、电缆/保险/TVS/eFuse、buck/LDO与芯片输出损耗、温度）以及保守保护配合，引用原厂额定及实测位置。优先试验 1、4、16路，未有实测不冻结 64路/板功率布线。

安全线路必须硬件独立于 FPGA PL/PS：NC E-STOP、驱动电源独立 cutoff、局部 watchdog、温度硬件比较器、PGOOD、互锁、fail-closed OE 和冷启动/掉电/线缆断开/时钟停转/上电时序的受控关断。595 OE 高阻不是功率切断。禁止在无源仿真合格时宣称硬件保护已经实测。

---

## 6. Gate D — 三板 PCB 候选电路、Pinout/BOM 与中央供电问题

### D1. 拓扑与分板

- **中央板**：AX7020 J10/J11 适配、上/下阵列逻辑分发、完整安全状态/联锁、AD7606C-16、ADC模拟/数字电源与滤波、温度环境参考 TMP117、可选 SHT45、监测/调试 TP、以 AX7020 为唯一正常电源来源的可验证限流/浪涌/地回路设计。
- **上/下阵列板（镜像方向装配，同 BOM/同核心 PCB）**：64 NU40C10T、外角4 RX候选、16×595 32×TC4427A、4RX AFE/blank/bias、1×TMP117、1×电流监测 INA226、独立 XT30(或等效已验证防反接)电源入口、独立电源保护与 cutoff/FAULT、温度热点报警、数据接口/模拟屏蔽/线束；注意上板声辐射面朝 -Z，下板 +Z。
- J10/J11 **每个40Pin含电源/地，不是40 GPIO**。现有67/68 IO分配是候选，剩余1 GPIO的余量、方向、Bank/VCCO 必须按最新 Rev3 原厂料号和实际连线重新审核。不能把用户草图中的两个 `2×20` 当“40 路 TX 驱动引脚”。AX7020 不直接驱动 128颗 T，数据必须经 serializer/driver。
- `PSKEY1`(MIO50/B13)、`PLKEY1`(N15)、`PLKEY2`(N16)当前为官方资料**候选**；实际 Rev3 和 IO 后确定按钮功能，例如 PSKEY1授权、PLKEY1自校准、PLKEY2立即请求 SAFE；真正急停永远是独立硬件线路，用户按键不是安全断电替代品。不得在未知启动镜像下把按键误定义为安全可操作。

### D2. 原理图交付标准

在**嘉立创EDA专业版**存在真实可调用的项目/操作环境时，创建中央板+上下共用阵列设计的原生 v5 schematic（可采用多个 Sheet 且模块分区清晰，绝不将文件夹中的老 v2 原理图直接改名），补全：电源树、电压域、地/屏蔽/回流、时钟网络、逻辑层转换、所有匹配反相方向、驱动使能、故障反馈、RX保护/AFE滤波、ADC 64pin 引脚与去耦、可编程温湿、测试点、J10/J11信号、上下对称 BOM 与位号。输出**实际原生 netlist 与 BOM**、ERC运行日志、逐项warning处置、引脚/连接器/方向 pin-to-pin审查表、可读 PDF/SVG预览。若 EDA 当前不可用：只交付独立**机器可读网络合同**、完整待核验表与阻塞状态，不能自称有原生工程或真正 ERC PASS。

**本轮仍为原理图阶段，不自动生成生产 PCB、Gerber、采购订单。** 目标是达到“经用户和独立电气审查后可进入制板布局”的候选状态。失效注入/复电逻辑、电子学热估算不闭合则制造 `HOLD`。

### D3. BOM 工作表与精确归档

生成更新后的完整 `.xlsx`（不要覆盖历史采购基准），按 `Review/Upper/Lower/Central/External/Source_References/Decisions` 或同等清晰 Sheet；列包括 item、正式 MPN、供应商、封装与Pin、每板数量、总装机/备件、候选/已批准、额定电压电流功耗、供应商链接、原生 EDA footprint核验、替代策略、测量/阻塞和价格币种。正式ADC仅 **C-16**，B 旧表保留到历史路径作 provenance；T/R 精确后缀明确；每侧12V独立、安全元件与线束/插座必列；三颗 TMP117 和可选 SHT45列明。BOM/原理图/JSON/PINMAP 位号和电路零件数完全对账。

**决策门禁**：凡真实 RX 完整 MPN、电源芯片保护配合、中央扩展口 5V/3V3 负载、TVS/eFuse、驱动拓扑、NU40C连续电压/电流和Rev3 connector信息不明，关键项必须 `HOLD`；其余有完整厂家规格的项可实现候选电路，不强制所有部分都停工。

---

## 7. Gate E — 温度/湿度补偿、Sparse 自校准、完整响应与运动闭环

- 三 `TMP117` 必须真实具有地址、上电/CRC(仅有该器件支持的检测)/I2C ack、读出/时间戳/可信区间/掉线处理的板级 adapter；算法使用它们的实测或明确 SYNTHETIC 数据给出 `c(T,RH)` 及每条 TX→RX 传播相位路径积分。三温度样点只能构成**估计模型**，不能冒充真实 3D 空气温场。SHT45 的湿度若参与实际数值，应给与干空气模型的独立 oracle 对照、适用条件和用户说明。
- Sparse 几何扫描沿两对角与补充代表TX，UP→DN的4RX / DN→UP的4RX；独立粗TOF绝对距离约束、carrier phase周期展开、每侧RX电气延迟与phase gauge、6DoF拟合的可观测性(SVD/rank/condition)和异常观测拒绝。用户明确指定的 (1,1),(2,2),(3,3),(4,4),(8,1),(7,2) 等均覆盖（0-index/1-index显式映射），不把16+16稀疏扫描当全通道幅相实测。
- 所有128 TX per-channel 的幅度/相位/极性/频响/弱通道/温漂记录在实际板到手后完成；在无相阵PCB实物时标 `UNMEASURED`。二维/三维空间边界、焦点、场图、置信度、独立上下参考和异常码由 UART 协议提供摘要/快照。
- PC GUI 必须保留用户自由定义和动态调整的点、贝塞尔曲线柄、XYZ移动、闭环图形与时间/速度/加速度/jerk限制，路径由用户当场操作产生，不允许预制图形点集合或虚假回放。屏幕状态区明确 `SIMULATION/HOST_FIXTURE/REAL_BOARD`，真实板未验证时不解锁危险动作。模拟移动光标不等于小球位置。
- 原始波形需要慢速UART分帧/流控；不要声称115200可无损持续传输 800kSPS×8ch。PS和PL本地调度50Hz及40kHz，GUI只处理用户意图和异步状态显示。

---

## 8. Gate F — 验证矩阵（所有新的实际修改必须通过）

### F0 基础无回归

- 原有 **115 项测试完全保持**，加新增56项的现有 **171/171 baseline** 必须继续 PASS，不得删/skip/放宽。新 ADC/PS/GUI/电气合同测试**额外新增**，不能以171冻结上限阻止加测。
- 原完整 GUI驱动轨迹 3696 帧×3 Icarus+1 XSim，跨工具 fixed seed/canonical map/trap/ACK Hash；C/AXI/safety/calibration/serializer/golden全保留。
- 新 temperature 160 maps/20480words Python/C bit-exact、Sparse 5 seeds/10fits/5starts/384 holdouts、5动态GUI案例375frames、新supervisor+BRAM top在两工具一致。新ADC实现须新增高带宽/4DOUT/读回负例和源自原厂的数据手册边界，不要求新器件数据与老B逐字节一致，但**旧测试历史不被改写**。
- 编译目标 ARM 与主机 C 区分；真实工具输出及退出码+log文本都审阅。不可用时明确 `ALTERNATIVE_VALIDATION` 不称目标实板PASS。

### F1 Vivado/Vitis 2025.2 平台

- 离线真实创建/reopen：`xpr/BD/XSA/Tcl`，完整source-file审计，当前 v5-only依赖，检查PS7、DDR、UART、AXI GP0、BRAM, IRQ, IIC, ADC和IO。
- 如果仍只有 PL OOC 正时序，必须保留 `TIMING_HOLD_MISSING_BOARD_FACTS`。只有真实 Rev3 production pin/XDC、外部 serializer 66MHz min/max/时钟/IO延时、VCCO、跨域与布线路径解决后，才能宣称 full board timing `WNS/WHS≥0,TNS/THS=0`。
- 已知继承异步 BRAM 控制 DRC（此前20项规则报表截断）、161 input/148 output缺真实delay，需要保留并重新查完整；禁止 waiver、false_path、故意不约束来买时序。
- 真实硬件测试若因当前 SD 镜像所有权/Rev3资料缺失受阻，须有独立 STOP 记录；**不允许为冲目标伪造 board timing / PING证据**。

### F2 稳定性与故障注入

- ADC配置读回错误/超时/错 CRC；串口损坏包/重放包/断线/恢复；I2C断线/坏温度；电源未 ready/上下独立 fault/紧急停止；logic power丢失/硬件watchdog模拟。未知电气环节标 `SIMULATED_ONLY`，不要把RTL fault test称硬件 cutoff验证。
- 在可控且获许可的真实板状态下验证 100/1000 次 UART/AXI控制协议（含输出禁用），并附时延分布与对应 source commit；未获许可先完成主机/RTL软件替代模拟。

### F3 第二环境/复现性

- 在独立Git clone（无 hardlinks、无 `Historical project`正文、锁定 fresh venv）跑 F0/F1可执行门禁；对比当前工作区的 source hashes、功能/波形/TRACE/报告。
- 检查不加载 Robei/EBAZ旧XDC/preset/source，不默认检索 `Historical project/`；只允许索引元数据审计。
- 运行后完整生成 `TEST_MATRIX.csv`、`EVIDENCE_INDEX.md` 和失败日志；每项用：`PASS / FAIL / BLOCKED / NOT_RUN / SIMULATED / HARDWARE_VERIFIED` 精确区分。

---

## 9. 最少人工干预的执行顺序与可停止分界

| 阶段 | 默认允许 Codex 自主执行 | 遇阻应如何处理 | Done When |
|---|---|---|---|
| S0 | Git/PR/依赖/用户新Decision核对、留复现Hash、确定开发分支 | 未核实工作区则STOP，不能误改老沙盒 | Repo facts + ADC授权已记录 |
| S1 | JTAG/USB/COM只读识别、Vivado/Vitis工具核验、Rev3资料比对 | 不得 halt/reset/覆盖，A2需用户独立许可 | 实际板状态与串口路径日志 |
| S2 | ADC C-16正式适配、BOM/adapter/初始化/读回/独立模型/回归 | 非目标硬件就明示SIMULATED | C-16 数字门禁PASS，正式型号更新 |
| S3 | 温度、稀疏几何、GUI/PS C/PL supervisor 补强及前测回归 | 缺实际阵列数据仅 synthetic，不封全通道校准 | 自校准/GUI/协议回归无减项 |
| S4 | AX7020 PS平台与临时安全board smoke工程，目标交叉工具链验证 | 板级资料或镜像所有权缺失则申请授权/另列STOP | TARGET_BUILD_PASS或明确BLOCKED |
| S5 | **仅当A2全部满足且用户批准有影响的板级写入**，执行有界volatile UART/AXI回环 | 未批准本轮停止物理写入，仍可提交全部离线产物 | 真实100/1000通信日志，或清楚NOT_RUN |
| S6 | 三PCB原理图候选、BOM Excel、网络合同、已有实物接口审查/原生ERC条件性运行 | 缺Cad/供应商原件保留电气HOLD | Netlist/BOM/候选审查结果一致 |
| S7 | 两仿真器、干净克隆、真实 Vivado回归、证据归档、更新 shared/GitHub开发分支 | 大问题2–3轮无进展触发RCA并停止重复 | 完整汇报+Draft PR+可恢复checkpoint |

串口当前已连接，**先做 S1**，但各 S2/S3/S4/S6 可以在硬件 A2 阻塞时继续。不要为一个硬件阻塞让本轮所有可执行工作无限停等。常规 Bug 自主2–3轮有界修复；结构/版本/芯片/外部电源不可逆重构先升级决策；达到离线Blocking0、关键质量≥约90%且没有高收益事项时 `STOP_OPTIMIZATION_AND_DELIVER`。

---

## 10. 交付路径、证据和 GitHub 政策

- 建议全部**当前活动**产物写进 `v5/` 和根 `shared/` 当前状态、`AI-problem/decision` 或 `AI-interaction-memory` 正式索引；不要读/写 `Historical project/` 历史正文或旧沙盒。
- 本轮报告建议：
  - `v5/docs/next_stage/ARCHITECTURE_DECISIONS.md`
  - `v5/docs/next_stage/ADC7606C16_MIGRATION_REVIEW.md`
  - `v5/docs/next_stage/NU40C10T_VENDOR_AND_BENCH_SOP.md`
  - `v5/docs/next_stage/AX7020_JTAG_UART_BRINGUP.md`
  - `v5/docs/next_stage/THREE_BOARD_SCHEMATIC_PLAN.md`
  - `v5/docs/next_stage/POWER_SAFETY_SI_REVIEW.md`
  - `v5/docs/next_stage/GUI_REAL_BOARD_USER_GUIDE.md`
  - `v5/docs/next_stage/OPEN_GATES.md`
  - `v5/evidence/next_stage/<真实时间戳>/`（总summary、真实JTAG/UART日志、ADC两工具回归、C/RTL/GUI测试、Vivado STA、PS/ARM构建、ERC真实日志或N/A、SHA/provenance、失败原因、Git证据）
  - `v5/hardware/bom/working/<日期>/BOM_AX7020_NU40C10T_AD7606C16_WORKING.xlsx`
- 修改后同步 `README/AGENTS` 中必要当前指引、`shared/PROJECT_STATE.* / VERSION_STATE / CURRENT_PLAN / DECISIONS / BLOCKERS / ACCEPTANCE / CONTEXT_CHECKPOINT.*`，显示当前真实来源/模型未知时不得编造模型执行详情。
- **开发分支**允许常规reviewed commit/push并建立 Draft PR、远端哈希核验、CI运行；不得自动合并 `main` 或取消原 PR#1/#2/#3，不能force push/rewrite、不能把 Windows 用户身份、COM序号、EFUSE、原始私有照片或客户资料推公开GitHub。
- 在回答中列出所有新或旧 PR 祖先关系；PR#3内含#1/#2，**新开发PR如基于#3，明确 stacked dependency**，避免多重合并/重复搬迁、变更树异常。只有用户明确批准的具体 PR 才能正常合并；合并后需 fresh remote-main clone 全回归。
- 产出的 CAD、电气/订货状态分 `PROPOSED / DIGITAL_VERIFIED / BENCH_VERIFIED / BOARD_VERIFIED / ELECTRICAL_RELEASED`；BOM只到工作候选时禁止声称“可直接投板/采购”。

---

## 11. 最终 Quality Gate 与答复结构

本次完成后请提交下列表格，不要只说“完成”：

1. `PROJECT_ID / Repo / branch / HEAD / v5 / stage / workspace / tool versions / latest user decision evidence`。
2. `Decision`：C-16用户已批准；具体RevA软件模式/帧协议、NU40C10T/R-2、中央供电/独立阵列供电、接口/pin、安全拓扑候选；对每项标 `PROPOSED / APPROVED / BLOCKED`、Rationale/Rejected options/Risks/User Approval Required。
3. `Actual Work`：代码/RTL/PS软件/C接口/UI/Excel/netlist/EasyEDA实际完成与文件路径、diff统计、原受保护文件Hash/旧版本完整性。
4. `Tests`：171旧+新多少、3696帧四轮、跨模拟器Hash、160 maps、Sparse数字结果、ADC芯片配置读回/异常、clean clone、Vivado/XSim/XSCT、如实板成功则100/1000次读写统计及板态恢复证据。
5. `Physical State`：JTAG读出、实际 UART/COM、有无目标ARM构建、PS/AXI/PL 实板真闭环、有无实际 ADC/TMP117/NU40C数据，各用 `HARDWARE_VERIFIED` vs `NOT_RUN`。
6. `PCB/Power`：NU40C10T/R-2、ADC C-16、3TMP117、每板独立12V与中央板受限额定、元件完整MPN/原理图网表/真实ERC、热/保护/时序和所有电气 HOLD。
7. `Remaining Blockers`：责任人、关闭所需最小证据、风险优先级、下一步最小闭环、`Decision Status`；没有新证据不重复旧讨论。
8. `GitHub`：当前开发 Draft PR、main 未合并、base/heads、CI证据、checkpoint、失败和回滚链。
9. **仅使用**：`ACCEPT / ACCEPT WITH LIMITATIONS / REVISE`，但要分别标注 `offline scope`、`real-board scope`、`whole platform`，不可用单项合格冒充全项目ACCEPT。

### 显式停止条件

- **真实 JTAG/串口查不到相关硬件**：记 `REAL_BOARD_GATE_BLOCKED`，保留日志并继续非板级工作。
- **确认 Rev3/PS/DDR/运行镜像所有权不足**：只读到此为止；必须请求新的明确写入授权，不能擅自覆盖。
- **AD7606C-16 电气或寄存器条件矛盾**：保持生产电气 HOLD，但用户已批准的型号决策不被单独撤销；报告冲突和替代路径供用户定夺。
- **真实原生CAD环境缺失**：机读电路合同完成，`ERC_NOT_RUN`，不输出伪造制造文件。
- **重大 Blocker/质量回归**：RCA、保留失败证据、选择替代方案后由用户作不可逆决策；不能降低阈值掩盖。

---

## 12. 官方来源与输入资料（Codex 必须保存链接、实际版本/检索时间与来源可信度）

**官方/主资料**：

1. ALINX AX7020 官方开源资料（2023.1，**与真实Rev3有匹配差异，须重新核对**）：https://github.com/alinxalinx/AX7020_2023.1
2. AX7020 官方手册入口：https://ax7020-20231-v101.readthedocs.io/zh-cn/latest/AX7020UserManual_CN/AX7020UserManual.html
3. AD7606C-16 Analog Devices Rev.A 原厂数据手册（重点寄存器0x02/0x07、Table26、38、Figure104-113、analog BW/phase delay/AVCC/VDRIVE）：https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf
4. AD7606C-16 官方产品：https://www.analog.com/en/products/ad7606c-16.html
5. AD7606B 原有参数用于迁移差异对照（**不是生产依据**）：https://www.analog.com/en/products/ad7606b.html
6. TC4427A Microchip 官方：https://www.microchip.com/en-us/product/TC4427A ；数据表：https://ww1.microchip.com/downloads/aemDocuments/documents/APID/ProductDocuments/DataSheets/TC4426A-TC4427A-TC4428A-1.5A-Dual-High-Speed-Power-MOSFET-Drivers-20001423.pdf
7. TMP117 TI官方：https://www.ti.com/product/TMP117
8. 本仓库的当前事实：`https://github.com/loverlike1216/SonoField-FPGA`，以及具体活动分支的 `shared/`、`v5/`、`AI-problem/`、PR#1/#2/#3。不得用本文件的旧HASH覆盖实际仓库新事实。

**用户提供实物图片**（在 Codex 会话单独上传；路径未必与本环境共享）：

- 图片1：`NU40C10T/R-2` 供应商规格截图（文字读数见 §5.1）；
- 图片2：`NU40C10T-R-2` 类机械尺寸与极性图（Ø9.8、5.0mm pin spacing、7.0mm高度/脚长、正负极标识）。

供应商截图是**有出处的用户输入**，并非能证明原厂完整连续驱动规格；若用户实物是 T-2，须把 RX 的真实 R-2 MPN 向供应商核对。任何完全没有官方说明的数据保持 `UNKNOWN`。

---

### 完成定义（交付给用户审核）

此轮的理想交付是：**当前 v5 不回退、全部能离线验证的 ADC C-16/PS/PL/温度/自校准/GUI/三板硬件候选真实完成、JTAG+UART 一次安全资格检测有真实证据、符合外部操作许可时尽可能获得真实 PS/PL UART 1000 次控制链、阻塞明确、Cad可执行时有可审查原理图/真实ERC、GitHub开发分支可复现。**

没有接通功率阵列时，不能要求制造物理悬浮 PASS；没有实物 ADC 时，必须如实标记 ADC模拟链 NOT_RUN；不能将工程候选通过等同于整机 ACCEPT。
