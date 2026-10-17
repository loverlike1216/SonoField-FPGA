# 新旧指南独立一致性报告 — 2026-10-17

**表述转换核对：PASS，电气连接合同差异：0。文档交付结论：ACCEPT。原工程ACCEPT WITH LIMITATIONS与待独立Review状态不变。**

| 检查 | 状态 | 实际核对范围 |
| --- | --- | --- |
| 原Markdown ↔ 原CSV | PASS | 5205个物理脚、1259个无源器件双端，字段逐项一致 |
| 新Markdown ↔ 原Markdown/CSV | PASS | 982个模板器件、3241个模板引脚；展开三板后1611器件/5205引脚，0差异 |
| 型号/数量/封装/无源值/极性 | PASS | 全部85种BOM数量；新器件元数据与原CSV逐项核对；极性保留在操作段落 |
| 图页与步骤 | PASS | CENTRAL7页、ARRAY6页；每器件唯一页/唯一顺序，连续步骤，无遗漏 |
| 逐页分册 | PASS | 13份分册与已核对全文的相应段落逐字一致，同网链接回链全文，末尾空行统一 |
| 同网器件端点 | PASS | 685个模板网络完整端点；每脚直接连接对象/高扇出链接逐项核对 |
| 接口对应 | PASS | 80个FPGA触点和128个上下阵列触点；表格和每脚接线文字均核对 |
| 原技术约束 | PASS | 原指南第1–7节正文完整保留，标题增加一级、文件末尾空行统一 |
| 错误注入 | PASS | 8项实际内存负向测试全部拒绝；没有修改交付文件 |
| 原输入保护 | PASS | 8个原输入SHA256前后不变 |
| 新电气仿真/原生ERC/实物 | NOT_CHECKED | 本轮是指南表述转换，不新增此类验收 |

原指南SHA256：`8db415eb181ea840831148a40458620974d549f5b8052f325b23a7e89f21b9ee`。

新指南SHA256：`d897bad1cf87862eeee3d632321b8b23ebea5d8108426947e50715a3b4bb1c48`。

核对器独立读取最终Markdown，不导入生成器、不以生成器输出JSON作为电气真相。原指南表格先与独立CSV核对，再与新指南展开后的引脚集合、同网端点和BOM数量比较。新增加的图页归属/纸面顺序属于文档组织，不冒充旧指南已有的图页元数据。

## 实际错误注入

- missing_SER_physical_pin：PASS_REJECTED；final physical pin omission/extra
- wrong_SER_network：PASS_REJECTED；final/original pin mismatch ('ARRAY', 'U_SR00', '14') net
- wrong_series_resistor_value：PASS_REJECTED；passive value mismatch ('ARRAY', 'R_TX00')
- wrong_connected_device_pin：PASS_REJECTED；wrong direct same-net peer ('CENTRAL', 'J_PWR', '1')
- wrong_FPGA_cable_pin：PASS_REJECTED；FPGA 80-contact mapping changed
- wrong_component_page：PASS_REJECTED；pin row page differs from placement ('CENTRAL', 'U_EF', '1')
- wrong_polarized_capacitor_orientation：PASS_REJECTED；passive polarity mismatch ('CENTRAL', 'C_EF_OUT')
- missing_full_net_endpoint：PASS_REJECTED；wrong/incomplete full net endpoints N0001

## 本页器件数量

- CENTRAL/00_POWER：55
- CENTRAL/01_FPGA_HEADERS：3
- CENTRAL/02_TX_BUFFERS：167
- CENTRAL/03_ARRAY_HEADERS：2
- CENTRAL/04_ADC：52
- CENTRAL/05_RX_INPUT：40
- CENTRAL/06_I2C_TEMP_SAFETY：34
- ARRAY/00_POWER：80
- ARRAY/01_LINK_BUFFERS：40
- ARRAY/02_595：96
- ARRAY/03_UCC_TX：324
- ARRAY/04_RX：38
- ARRAY/05_SAFETY_TEMP：51

复现：PowerShell7运行科学Python解释器执行`scripts/check_guide_consistency.py`。源输入来自本目录上一级；仅在原公开文件存在CRLF/LF格式差别时，source_inputs保留对应本地原始字节副本并优先读取，全部字段相同、原文件不改。脚本只将核对报告写到本目录。实际运行日志见logs/check_guide_consistency.log。
