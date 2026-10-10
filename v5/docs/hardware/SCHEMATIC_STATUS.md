# 原生原理图、库资格和建图任务

NATIVE_SCHEMATIC_NOT_CREATED；ERC_NOT_RUN；MANUFACTURING_HOLD。
真实EasyEDA桥GET /health返回edaConnected=false、窗口数0。可用Node桥不等于
可用编辑器，JSON/CSV/SVG不冒充.epro2/.eprj2或原生Netlist。
使用技能：`C:/Users/loverlike/.codex/skills/easyeda-api/SKILL.md`，
真实编辑器应加载run-api-gateway扩展，先选唯一项目，再执行原生建图与ERC。
本轮没有编辑/安装用户CAD工程，也没有对制造接口发出操作。

建图分成中央、统一阵列、线束三项原生设计任务；上/下阵列是同一PCB的两份
Assembly，顶面向-Z、底面向+Z，通道索引各0..63，装配ID而非镜像反极性。
首轮禁止Gerber、下单和采购。以下是生成任务，完成状态均NOT_RUN。

| 页 | 必须出现的电路和审核 | 完成证据 |
|---|---|---|
| C1 Type-C/Power | CC1/2、STUSB4500L、ESD、VBUS检测、3A许可、保护开关、buck-boost/滤波、AVCC/3V3 | 原生连接/默认态、NVM读回/启动状态、低VBUS计算 |
| C2 AX7020 | 两组80触点、电源针NC、Ioff缓冲/默认OE、地回路、待定wrapper/同步信号 | 每触点方向/Bank/电压/网络清单，未定义接口不隐藏 |
| C3 C16 | 完整64pin、四DOUT、RESET高有效、OS111/PARSER1/软件模式、AVCC/VDRIVE/参考 | ADI Rev.A逐脚和现有ADC64合同交叉检查 |
| C4 I2C | TCA9548A0x70，中央/上/下单域、3TMP117、3INA226、独立RESET、上拉/隔离 | 卡死及单边掉电恢复真实电路和所有地址表 |
| C5 RX接口 | 八通道屏蔽参考、保护、RC、量程、blank、TP | AFE8→C16V1..8和模拟回流，无负压/尖峰损坏路径 |
| A1 DC/Protection | DC中心正极、防反/fuse/TVS/eFuse/反向阻断、3V3/5.5V→AFE5V | RILIM/UVLO/OVP/dVdt/峰值/热/EP/所有被动值 |
| A2 Safety | 窗口watchdog、硬件过温、NC ESTOP、本地锁存/人工重启、独立TX rail cutoff/放电 | 电源缺失默认OFF、故障恢复不自动重启 |
| A3 Serializer/Clock | 16×595，Q0..Q3使用，其他不挂载；clock/RCLK/OE/reset/sync/blank | 每lane4ch和端口未接项关闭，PVT/扇出/布局 |
| A4 Driver64 | 32×TC4427A、64单端TX、64输入下拉、局部去耦 | 不误作128路桥式；默认态和持续负载资格 |
| A5 RX4 | 精确RX、保护/blank/偏置/滤波、各路群延迟、AFE近传感器 | 参数、8路匹配、噪声/饱和恢复和40kHz实测计划 |
| A6 Monitoring/TP | TMP117、INA226、热比较器、所有power/test点、装配ID | 温度探头代表性、电流方向、testpoint清单 |
| H1 Harness | 数据/时钟返回地、模拟屏蔽、DC、独立NC安全环、防呆/应力 | min/max长度/阻抗/线序/Pin1/插入深度 |

库资格清单见LIBRARY_QUALIFICATION.json。完整MPN不等于正确库UUID。
每个器件须保存manufacturer/datasheet/page/symbol UUID/footprint UUID、
原厂Pin1和EP、引脚编号和功能、焊盘编号、机械公差、版本、审核者、截图。
不允许隐藏供电或将EP当唯一地连接，不使用同名不同封装库器件。
TPS26631RGE为24pin VQFN，PWP20pin不可套用；TCA9548APW为24pinTSSOP，
TMP117DRV为6pinWSON，STUSB4500LQTR为QFN24EP。所有UUID未取得。

开/重开原生工程后导出真实Netlist与BOM，比较本候选237条连接、64ADC脚和
全部位号。聚合电阻/电容/保护组须拆到真实位号和值后才能ERC。全部warning
逐条分类，不能隐藏警告、自动豁免或以ERC零严重错误宣称电气/制造通过。
ADC、AFE、Ioff、eFuse、安全锁存、窗口watchdog仍有影响原理图的重大未知，
当前结果只能是有范围限制的离线候选，未完成原生原理图交付。
