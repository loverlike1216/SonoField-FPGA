# SonoField 单张原理图 — 项目 v2 / 原理图修订 V1

优先打开 **SonoField-SingleSheet.pdf**：单页矢量图，可连续放大；建议先看全图分区，再放大到一个模块。SVG 同样可缩放，画布约 15622 × 6701；不建议把整张图缩印为 A4 阅读。

在嘉立创EDA专业版打开 **SonoField-FPGA-v2-Schematic-V1-SingleSheet.eprj2**。跨电脑导入使用同名 `.epro2`。均为一张原理图，无 PCB。蓝色实线是分区边界，不是电气导线；同名网络相连。

128 TX / 8 RX，83 个命名模块，1561 个元件。10 mm 名义外径、12 mm 辐射面中心间距，上下面名义100 mm、允许90–115 mm；原点为几何中心。电气符号位置不表示机械坐标。

**设计草案，不能直接投板。** 板卡物理引脚/VCCO、66 MHz 串行保持时间、独立失钟/电源合格保护、采购料号及模拟实测尚未闭环。原生 ERC 有45条警告，详见 `../log/review/ERC_DISPOSITION.md`。

`*_design.json` 是意图清单，`native_sheet_map.json` 仅用于保留的83模块历史生成源；最终单页UUID见校核报告。完整坐标和 RTL/网络对应表在 `v2/docs/hardware/SCHEMATIC_CHANNEL_MAP.md`。
