# AX7020 v5 实板只读检测与 BOM 集成结果

日期：2026-10-09。PROJECT_ID：SONOFIELD_FPGA；main；v5；模型记录 GPT-6.1 Sol High（用户声明）。本次以真实照片、Windows、Vivado/XSDB 2025.2、原厂资料和当前数字回归为依据。整机结论 **REVISE / 制造 HOLD**。

## 实际确认与证据边界

| 项目 | 结果 | 证据 / 限制 |
|---|---|---|
| 板卡与 PCB Revision | ALINX AX7020；AX701020.3.0，Revision 3.0 | 用户说明与两张实板照片；photo_provenance.json |
| FPGA family / 封装 | Zynq-7000 XC7Z020；CLG400 | JTAG 加芯片照片；完整速度/温度等级 UNKNOWN |
| JTAG 链 | ARM DAP 0x4BA00477；XC7Z020 0x23727093 | vivado_readonly.log；Vivado 2025.2 可直接连接 |
| 下载器 | Digilent JTAG-HS1；FTDI VID0403/PID6014 | Windows + Vivado 实际枚举；FT2232 未确认，不沿用旧 Robei 结论 |
| 驱动 | FTDI 2.12.28.0，签名有效，状态 OK | windows_public.json；没有证据需要更换驱动 |
| PL 当前状态 | DONE=1；EOS=1；PLL_LOCK=1；未发现支持的 soft debug core | 板上已有配置；本次没有下载 bitstream |
| PS 当前状态 | 两个 Cortex-A9 均 Running | XSDB 检测前后状态；程序来源/内存所有权不明 |
| 启动状态 | BOOT_MODE=0x5；照片可见 SD 卡与 SD 跳帽 | 只读取 0xF800025C；没有改变启动方式或访问 SD 内容 |
| DDR 控制器 | CTRL=0x81，CTRL_REG1=0x3E；控制器配置为 32 bit，已释放复位 | 只读取控制寄存器，未读写 DDR RAM；不证明容量、拓扑和稳定性 |
| DDR 物理容量 | UNKNOWN；官方 1 GiB 为文档预期 | 手册 Hynix 与 hello XSA Micron 预设不同，尚未匹配本板 Revision |
| 时钟 | 原厂文档 PL 50 MHz/U18，PS 33.333333 MHz/E7 | 未实测；hello XSA FCLK0=50 MHz；当前核心目标仍为 132 MHz |
| IO | J10/J11 文档共 68 GPIO；Vivado 库 68 个球位/Bank 对应通过 | V2.0 原理图与 Rev3.0 板尚未匹配，VCCO/方向/连通未实测 |
| UART | 本次无 COM 枚举 | 用户仅接供电/JTAG；官方 CP2102、UART1 MIO48/49 是候选路线；没有证明 UART 坏或驱动有错 |
| Ethernet | 照片存在 RJ45，官方有以太网接口 | 未接网线，未验证 PHY、链路、地址、协议栈或数据通信 |
| XADC / 温度电压 | 无有效读数 | 工具返回 -273.1°C 与 0.000V，标为 INVALID；不得解读为实际电源/温度 |

只读命令脚本：`v5/scripts/ax7020_readonly.tcl`、`ax7020_ps_readonly.tcl`。XSDB 仅通过 DAP/AP0 读取三个上述寄存器，未 stop/reset/init/download/mwr，未碰 DDR RAM。原始完整日志、USB 序号、照片和桌面截图保留于本目录 local_raw（不公开）；公开日志已删除设备序号及 DNA/EFUSE 字段。

## PS 配置交叉核对

读取固定官方提交 fcf1e4a239b0f47e8ee95dfde7c2eedc5685c327 的 hello XSA，并提取 HWH/ps7_init 参数；**没有执行 ps7_init**。见 `hardware/integration_candidates/20261009/official_ps_reference.json` 与 reference_sources.json。

官方手册描述 2×H5TQ4G63AFR-PBC / 1 GiB / 32 bit；XSA 配置 32 bit、15 行/10 列/3 bank、DDR 533.333333 MHz、MT41J256M16 RE-125 预设。预设可存在兼容料号的可能，但这不是本板 DDR 实物证据。XSA 为 2023.1，原理图为 V2.0，本板为 Rev3.0；须确认匹配关系再生成本板 BSP。已安装目录没有找到可用 ARM gcc/clang，目标 ARM 工具链尚未资格确认。

Gate A 实际只读检测完成。Gate B 临时 PL、Gate C PS/DDR、Gate D UART/AXI **NOT_RUN**：未知已运行镜像和 RAM 所有权、器件完整等级/Rev3 配置缺失、UART 未连接。没有将已配置 PL 误认为 SonoField 已上板，没有为了测试停止已有程序。

## 本次实际通过的离线验证

- 全 v5 数字基线：115 Python 测试；3696 帧运动 × 三次 Icarus 和一次 Vivado XSim；固定输入的四组 canonical Hash 一致；协议/C、AXI 离线桥、安全、时序等价全部通过。总入口结果：`evidence/baseline/board_integration_20261009/summary.json`。
- 黄金等价：burst 5,066,261 个向量、phase 486,026 个向量；此次日志单独归档在新基线 equivalence/，以前日志恢复原字节。
- GPIO 候选：完整 80 针、68 GPIO、63 使用/5 预留；Vivado 器件库球位/Bank 独立核对通过。它不是生产 XDC 或已核验线束。
- ADC 候选：固定 Seed=20261009 的 256 帧（含 signed 极值），四 DOUT/通道顺序经 Python、Icarus、XSim 检查；独立配置 ROM 包含 BANDWIDTH 写/读；参考策略拒绝 6 类损坏读回。未完成生产 ADC 初始化 RTL 适配，未验证真实模拟采样。
- 安全候选：1024 个组合及故障/重新使能/上下独立关闭场景，仅功能模型通过；异步门级、电压、失电和真实关断延迟未验证。
- BOM：72 行公式/缓存与数量、原件 SHA256、全部新增 SUM 与公式错误检查；工作副本经 artifact-tool 重算、导出并查看四处排版预览。无原始文件覆盖。
- 交付完整性：16 项治理/来源/原件/Problem Hash/脚本边界检查通过。新检查器第一次误用 raw CRLF Hash 对比 baseline 的 LF 规范化 Hash，按原 baseline 的明确计算方式修正；核心源文件没有因此修改。

本次未改生产核心 RTL，所以没有新增整板综合/布局布线结果。之前文档器件 OOC 综合保留其原日期/上下文；不能提升为本板时序或 PS/PL 实测。

## 九类 BOM 处置与原理图

详细依据：`hardware/integration_candidates/20261009/ADC_CANDIDATE_REVIEW.md`、`SAFETY_AND_POWER.md`、`TIMING_BUDGET.md`、`SCHEMATIC_PREPARATION.md`、72 行 package_procurement_audit.csv。

| 问题 | 本次状态 | 尚未关闭事项 |
|---|---|---|
| 1 ADC 模拟带宽 | 已提出可验证方案：AD7606C-16BSTZ-RL，软件高带宽模式 | 独立 Review、用户正式换型批准、初始化/读回 RTL、实测幅相/SNR |
| 2 硬件安全关断 | 已提出可验证方案：本地供电安全逻辑、TX 独立切断、锁存 rearm | 门级/时序/掉电/断线/重启样机验证，单 DATA 断线检测尚未覆盖 |
| 3 浪涌保护 | 仍然阻塞 | SMBJ20A 钳位与 eFuse/driver 限值不协调；需浪涌条件和闭合保护网络 |
| 4 封装 | 已解决 ADP7118 文字封装错误：LFCSP6 / CP-6-3 | 实际 CAD 符号/焊盘/Pin1/EP；其余未完整选型项不能宣称通过 |
| 5 TX/RX | 仍然阻塞 | NU40C10T 厂家/批次完整数据，RX 完整 MPN 与样品 |
| 6 外部时序 | 已提出可验证方案：保持 32 lane、分列 setup/hold 预算 | 66 MHz 实际扇出/线束/负载 min/max、生产约束和示波器验证 |
| 7 GPIO / I²C | 已提出可验证方案：63/68；AXC 4+4+2 候选；开漏分域隔离 | Rev3 连通/VCCO，具体器件时序/失电，原生网表方向审核 |
| 8 电源 / 热 | 已提出可验证方案：2.02 A 限流、4.096 A 测量量程、200 mA LDO 预算 | 动态/谐振负载、峰值/浪涌、实际温升、线宽/铜厚与公差 |
| 9 BOM 清晰性 | 已提出可验证方案：补原厂来源、去复合行重复、可选环境板 DNP | 精确采购 MPN、实际位号、门逻辑数量和原生 BOM/网表对账 |

三块板功能分区与逻辑网络表、驱动/采样/安全/独立电源候选已准备。当前无 EasyEDA 进程/网关连接/实际 v5 工程，**native schematic NOT_CREATED / ERC NOT_RUN**。未编辑旧 PCB 或生成制造文件。

## 下一步与保留页面

先获得 Revision 3.0 匹配原理图/PS 参考工程、完整 FPGA 等级、当前 SD 镜像和安全工作区说明；连接板上 UART 口后核验 CP2102/COM。推荐 UART1 做第一条实际 PC↔PS 控制路线，JTAG 保持诊断，Ethernet 在软件/PHY/协议链路验证后作为后续选项。

依据匹配参考建立 Vivado 2025.2 PS/时钟/AXI 最小平台、可用 ARM BSP/工具链；在明确可临时替换当前程序/内存范围后做无负载临时测试，再做 1000 PING/PONG 与版本/状态/安全读写/断线。完成实际电气门禁前不连接阵列、不冻结制造。

实际 Hardware Manager 窗口已连接并保留，原用户 Vivado 窗口未关闭；`ax7020_results_gui.tcl` 可重开同样只读页面。页面中的 Programmed 表示检测前已有配置，不表示本次进行了下载。GUI 原始截图 local_raw/results_gui_final.png 含设备身份，仅本地保存。
