# DDR 实物证据与 PS 配置只读检测结果

日期：2026-10-04（Asia/Shanghai）。PROJECT_ID：SONOFIELD_FPGA；项目 SonoField-FPGA；分支 main；活动版本 v2；模型记录 GPT-6.1 Sol High（用户声明，平台未暴露精确运行变体）。Stage 保持 TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE。本次子任务 DDR_PHOTO_AND_PS_CONFIGURATION_PREFLIGHT。

**D9PSK 对应的 Micron 完整料号已经由官方查询确认；本板 512 MiB 容量及 32 位总线仍为 CANDIDATE。** 自动只读检测已完成，缺少板型匹配的 PS/DDR 配置或连接资料，不能完成板级交叉验证。

## 已确认与候选参数

| 项目 | 发现 | 证据状态 |
|---|---|---|
| FPGA JTAG 身份 | XC7Z020，IDCODE 0x23727093 | 本次 Vivado 2025.2 实测身份 |
| ARM DAP | IDCODE 0x4BA00477 | 本次 Vivado 实测 |
| 完整 FPGA 料号 | XC7Z020-1CLG400C | 已有用户确认；JTAG 不识别全部封装/速度等级 |
| DRAM 数量 | 照片可见两颗 Micron，丝印 D9PSK | 用户实物照片，已检查；没有电气连通性测量 |
| D9PSK 解码 | MT41K128M16JT-125 IT:K | Micron 官方实际查询响应 |
| 单颗目录规格 | 2 Gb、x16、128M×16、96-ball、1.35 V；DDR3L 系列 | 器件规格；不是板级测量 |
| 标称速度等级 | 800 MHz / 1600 MT/s | 器件额定等级；实际 DDR 运行频率 UNKNOWN |
| 总容量 | 2×2 Gb÷8 = 536,870,912 bytes = 512 MiB | **CANDIDATE**；通常口语写作 512 MB |
| 总线宽度 | 32 bit | **CANDIDATE**；两颗 x16 不足以证明并联 DQ 拓扑或 rank 数量 |
| 实际 DRAM 电源 | UNKNOWN | 未测量；不将 1.35 V 器件参数当作板上电压 |

Micron 官方 [FBGA Decoder](https://www.micron.com/sales-support/design-tools/fbga-parts-decoder) 返回了带工业温度后缀 IT:K 的完整料号；实际公开响应保存在 [micron_fbga_D9PSK.json](micron_fbga_D9PSK.json)。[官方器件页面](https://www.micron.com/products/memory/dram-components/ddr3-sdram/part-catalog/part-detail/mt41k128m16jt-125-it-k) 的实际规格响应保存在 [micron_part_spec.json](micron_part_spec.json)。两次查询使用页面自身公开表单/产品规格路由，没有账户访问或绕过授权。

照片采用已有用户原图，参见 [脱敏照片来源说明](../../v2/hardware/board/references/20261003_user/chip_marking_public_reference.md)。原图含 EXIF 隐私信息，仅留本地；没有将原图重新推送。

## 本次真实寄存器读数

通过 XSDB 2025.2 → localhost hw_server → APU/DAP 的 AP0 地址空间，只读两个 AMD 文档明确列出的 DDR 控制器寄存器。不是 DDR RAM 地址空间探测。

| 寄存器 | 地址 | 本次值 | 解释 |
|---|---|---|---|
| DDRC_CTRL | 0xF8006000 | 0x00000200 | 等于文档复位值；bits[3:2]=00 对应 32 位默认字段，bit0=0 表示控制器软复位未释放 |
| DDRC_CTRL_REG1 | 0xF8006060 | 0x0000003E | 同样等于文档复位值 |

AMD [DDRC_CTRL 地址/复位值](https://docs.amd.com/r/en-US/ug585-zynq-7000-SoC-TRM/Register-ddrc-ddrc_ctrl)、[字段定义](https://docs.amd.com/r/en-US/ug585-zynq-7000-SoC-TRM/Register-ddrc_ctrl-Details)、[CTRL_REG1 地址/复位值](https://docs.amd.com/r/en-US/ug585-zynq-7000-SoC-TRM/Register-ddrc-ctrl_reg1) 支持以上解释。

**32 位复位默认字段不能充当板级 32 位布线的交叉证据。当前没有有效初始化后的 PS DDR 配置。复位状态不说明 DRAM 损坏。** 两颗 Cortex-A9 在检测前后列表均为 Running。本次没有 halt/resume/reset、ps7_init、寄存器写入、DDR RAM 读写、memory test、固件或 Bitstream 下载。

可核对 [XSDB 脱敏输出](xsdb_read_ddrc_sanitized.log)、[寄存器机器记录](ddrc_registers.json) 和 [Vivado JTAG 脱敏输出](vivado_jtag_sanitized.log)。native batch 返回成功；保留工具启动时出现的路径警告，没有删掉警告来制造无错误日志。JTAG 的 15 MHz 是扫描频率，不是 PL 或 DDR 时钟。

## PS 参考配置搜索

实际限定搜索 parameter_detection、Zynq7020、活动 v2、Robei 安装目录及本机明确列出的 Documents/Desktop 目录，查找 .xpr、.bd、.xsa、.hdf、ps7_init 和 preset Tcl/XML。九个范围均未找到匹配文件。rg 返回 1 表示没有匹配；范围和数量保存在 [reference_search.json](reference_search.json)。这不是全盘所有可能目录的穷尽证明。

Robei 5.0.2 安装目录已检查。AMD 安装中的 ZedBoard/ZC702 等通用示例存在，不能当作本八角板的 preset。当前 Vivado GUI 的本次 journal 未出现加载 project/BD 的命令；此项是 journal 观察，工具没有直接查询 GUI 活动工程的能力，详见 [gui_observation.json](gui_observation.json)。

原 Vivado GUI 保持运行，没有切换其工程或关闭其窗口。本次另外运行只读 batch 和仅绑定 127.0.0.1 的 hw_server，未开放 GDB 端口。

## BLOCKING 与下一步

1. 缺少本板、对应硬件版本的真实 PS preset / Block Design / XSA 或 HDF / ps7_init / Robei 工程，或可确认 DQ、地址线、rank 和电源的厂家原理图。
2. 当前 DDR 控制器仍为复位值，没有有效配置可以交叉验证；本次不主动初始化来消除该状态。
3. 原有 PS 时钟/reset、UART/MIO/FTDI 路由、bank34/35 VCCO 及外部时序门禁继续有效。B01 已有完整料号事实保持解决；B03 仍只部分解决。

将真实厂家/此前可运行工程资料放入 `parameter_detection/inputs/`。之后先比对板型、芯片料号和拓扑，再解析 PS 配置中的总线宽度、容量/地址范围、速度和延时；匹配后才能提升容量/位宽状态。新建一个填写 512 MiB / 32 位的工程、套用通用 preset，不能验证同一假设。经过有效平台和授权边界后，实际运行频率、电压和 DDR memory test 仍需各自独立证据。

## 范围与交付

新证据在用户指定 parameter_detection 下；候选配置在 [v2/config/ddr_candidate.json](../../v2/config/ddr_candidate.json)。源码、RTL、PCB、冻结版本及历史证据没有改动。原先数字仿真/132 MHz 内部 OOC 时序结果保持原日期和验证 commit，本次没有重新运行，不把它们计作本次新测试。ChatGPT 外部历史仍 BLOCKED；当前可观察 Codex 记录 PARTIAL。

状态：AUTOMATIC_READ_ONLY_INSPECTION_COMPLETED_CROSS_VALIDATION_BLOCKED。完整平台仍有阻塞，PRE_PCB_BOARD_READY=NO。

REVISE
