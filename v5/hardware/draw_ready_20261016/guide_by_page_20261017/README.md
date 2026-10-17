# 按板卡、图页逐步连接指南入口

本目录是原02指南的追加表述转换包，原文件与电路不改。完整指南包含全部步骤、接口和完整同网端点；下方13份分册便于一页一页照着连接，内容来自同一份已核对全文。

- [完整步骤指南](13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)
- [独立一致性报告](14_GUIDE_CONSISTENCY_REPORT.md)
- [机器可读核对结果](results/CONSISTENCY.json)

| 板卡 | 图页分册 |
| --- | --- |
| CENTRAL | [00_POWER](pages/CENTRAL_00_POWER.md) |
| CENTRAL | [01_FPGA_HEADERS](pages/CENTRAL_01_FPGA_HEADERS.md) |
| CENTRAL | [02_TX_BUFFERS](pages/CENTRAL_02_TX_BUFFERS.md) |
| CENTRAL | [03_ARRAY_HEADERS](pages/CENTRAL_03_ARRAY_HEADERS.md) |
| CENTRAL | [04_ADC](pages/CENTRAL_04_ADC.md) |
| CENTRAL | [05_RX_INPUT](pages/CENTRAL_05_RX_INPUT.md) |
| CENTRAL | [06_I2C_TEMP_SAFETY](pages/CENTRAL_06_I2C_TEMP_SAFETY.md) |
| ARRAY | [00_POWER](pages/ARRAY_00_POWER.md) |
| ARRAY | [01_LINK_BUFFERS](pages/ARRAY_01_LINK_BUFFERS.md) |
| ARRAY | [02_595](pages/ARRAY_02_595.md) |
| ARRAY | [03_UCC_TX](pages/ARRAY_03_UCC_TX.md) |
| ARRAY | [04_RX](pages/ARRAY_04_RX.md) |
| ARRAY | [05_SAFETY_TEMP](pages/ARRAY_05_SAFETY_TEMP.md) |

先完成CENTRAL的00_POWER→01_FPGA_HEADERS→02_TX_BUFFERS→03_ARRAY_HEADERS→04_ADC→05_RX_INPUT→06_I2C_TEMP_SAFETY；再完成ARRAY的00_POWER→01_LINK_BUFFERS→02_595→03_UCC_TX→04_RX→05_SAFETY_TEMP。ARRAY仅画一套，UP/DN分别实例化，电源不互并。

复核命令：PowerShell7执行`./CHECK_GUIDE.ps1`；可用`-Python`指定任意可用Python3.10+解释器。检查器只用标准库，不安装工具，不执行EDA操作。实际命令、输出与错误注入结果保存在logs和results。
