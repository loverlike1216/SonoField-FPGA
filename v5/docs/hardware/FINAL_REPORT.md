# v5 三板硬件设计本轮交付

阶段结论 **ACCEPT WITH LIMITATIONS**；整个实板系统 **REVISE**；采购与制造 **HOLD**。
同一SonoField-FPGA仓库、同一v5，本轮在codex/v5-hardware-design-20261011叠加PR4。
实际远端提交和Draft链接见shared/hardware_design/PUBLICATION_RECEIPT.json。
用户已授权自行同步GitHub，常规提交无需再批准；P0工程缺口使main提升不合格。

本轮实际交付：四源供电合同/功率计算和故障锁存模型，80触点及63/68GPIO候选，
237连接条目、C16原64pin合同和四颗关键IC针脚功能，136声学坐标、机械区域SVG，
101类型五表工作BOM和逐项差异，完整原生库/原理图建图任务、风险/后测清单。
这些资产都有明确候选和未验证字段，JSON/SVG没有冒称原生原理图。

| 验证 | 本轮结果 | 边界 |
|---|---|---|
| Python | 当前243/243，独立新克隆243/243 | 原203全部保留，新增40；模型不是电路 |
| 完整数字 | 3696帧×3Icarus+1XSim、C/AXI/校准/安全/等价PASS | 数字仿真 |
| C16 | 两工具64签名帧/32流水帧、5读回拒绝，2×1024capture及实际数字顶层PASS | 真实ADC模拟/电源未验证 |
| 温度/校准/GUI | 160maps/20480words；10fits×384holdouts；5运行时路径/375frames PASS | 合成输入/自动GUI，无实物跟踪 |
| 主机服务 | 1000/1000编译C进程PING、256寄存器mask、ARM对象PASS | 不是真实UART→PS→AXI→PL |
| Vivado2025.2 | 原生CLG400封装68GPIO，与手册80触点对账PASS；干净克隆报告一致 | 封装数据库；不证明实物等级、VCCO、外部时序或新综合 |
| BOM | 五表/101类型，404行公式及缓存独立检查PASS | 1205候选器件/聚合组条目，待原生逐网反标 |
| 可复现性 | 无硬链接稀疏clone、新锁定venv、12生成文件字节相同PASS | 同Windows/EDA；本轮全数字在当前clone重跑，clean本轮验证unit/合同/包数据库 |
| 保护/历史 | 4641原始当前文件审计、旧RTL/firmware/tests/goldens/BOM/evidence不变；3918历史Git身份不变 | 不读取冻结正文/旧沙盒 |
| CAD/实板 | EasyEDA实际0窗口，原生NOT_CREATED/ERC NOT_RUN；COM3Code0 | 未开UART、未烧录/复位、未超声/量功率/悬浮 |

功率不是完成项：64通道Cmax2.64nF/12V/40kHz的0.9732096W每板仅电容项。
上/下P_worst仍UNKNOWN。60W源在30%头寸下最大46.154W，40W为30.769W，
均须再按温度与保护/线束降额；中央15W源对应11.538W，6.8W仅设计分配。
CC3A未实测，4.75V低VBUS经线损可能低于ADC最低AVCC，升降压电路HOLD。

当前已确认缺口：RESET/SYNC、共享I2C与FAULT聚合尚未形成63IO运行wrapper；
安全模型没有独立TX电源截止的原生电路；AFE/TVS/fuse/FET/Pin1/EP/库UUID
未资格认证；346BRAM异步控制告警仍需P-20261010-001真实架构审查。
用户V2/V3兼容声明已经保存，但旧图内部REV1.0/2018及UART桥描述不一致
仍保留。用户表示会备份SD，当前没有哈希和恢复验证，不能宣称已备份。

失败未隐藏：首次保护审计拒绝新合同、缺VIVADO_BIN、Vivado未link设计、
短名字符串误判、clean缺临时目录/CC以及生成SVG/XDC换行复现失败均有记录。
没有删除失败测试、放宽35dB或替换golden。普通环境与换行修复后使用新标签。

详细入口：[设计审查](DESIGN_REVIEW.md)、[风险](RISKS.md)、[缺失事实与下一步](MISSING_FACTS_AND_NEXT_MEASUREMENTS.md)、
[复现](REPRODUCE.md)、[回退](ROLLBACK.md)。最终机器证据在
v5/evidence/hardware_design_20261011/FINAL_VERIFICATION.json；新检查点CP-20261011-001。
后续应先取得真实CAD连接和上述电气输入，再完成运行wrapper/安全电路/实板闭环。
