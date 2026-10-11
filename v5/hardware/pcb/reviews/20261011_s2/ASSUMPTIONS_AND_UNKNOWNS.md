# 输入分类、轨预算与执行契约

查询2026-10-11；只将实际可见证据归类。无实板测量输入。

| 参数 | 分类 | 来源/界限 |
|---|---|---|
|128TX8RX/12mm pitch/100mm gap90–115/50Hz/35dB|从合约获取/用户约束|当前shared和SIGNAL_CONTRACT；不是声学实测|
|TPS3851H33EDRBR整机2颗|用户批准方向|实际回复+S2原文section0；不代表功能安全批准|
|2.2nF±20%、40kHz、12V|工程假设|S2 GateA指定先计算；NU40C完整原厂C/Q/ESR等未取得|
|10.8–13.2V Vin分析、Ta60°C、Buck0.5A/2A例|工程假设|角落扫描范围；不是适配器保证和实际轨最大负载|
|TPS54202 2A/fsw390–630k/VFB.581–.611|原厂保证工作/电气表|RevC§5.5；仍须实际PCB热/loop验证|
|TC4427A 7Ω、1.5A|原厂典型且条件相关|18V测试值，不能当12V保证|
|TPS3851阈值/固定tWD/tRST|原厂保证/表值|RevB§5.5/5.6/8.1.1；POR输出条件有例外|
|ADC AVCC4.75–5.25、输入脚去耦|原厂保证/设计建议|C16RevA页6/17/58；板级供应未知|
|OPA GBW/slew、LDO200mV压差|原厂典型|不能代替全温/实负载保证|
|接触阻抗30mΩ/插座5A|原厂额定/表值|PJ-002BH；实际插头/温升未知|
|RLC模型、供电效率、热/声学指标|未知|未提供或未测，不补写数值|
|ADC寄存器实读、BankVCCO、保护故障延迟|未知|数字仿真不是实板实读或电气证据|

| 输入/轨 | min/typ/max电流或负载 | 额定/纹波/时序/热约束 | 状态 |
|---|---|---|---|
|AX7020原独立输入|UNKNOWN/UNKNOWN/UNKNOWN|原配规范；不由中央/阵列回供|维持原域，未操作|
|中央USB5V|UNKNOWN/UNKNOWN/UNKNOWN|CC广告default/1.5A/3A，3A仅条件上限；浪涌/ESD/eFuse|未选完整稳压/预算电路|
|中央ADC AVCC5V|UNKNOWN/UNKNOWN/UNKNOWN|4.75–5.25V；纹波/动态预算待定|低VBUS不合格，HOLD|
|中央VDRIVE/3V3|UNKNOWN/UNKNOWN/UNKNOWN|跟随实际IO电平、Ioff/复位顺序|VCCO未测|
|各阵列12V输入|理想C模型64路约.0676A标称，其余UNKNOWN|输入电流不能由该值封顶；60W/40W容量候选|负载/反灌/保护/线阻HOLD|
|各阵列TX rail|UNKNOWN/UNKNOWN/UNKNOWN|默认OFF/独立kill；剩余C必须放电，低纹波目标待定|物理电路未画|
|各阵列3V3 Buck|UNKNOWN/UNKNOWN/UNKNOWN；0.5/2A仅例|芯片2A上限非实际负载；FB角落/噪声/热|候选|
|各阵列5V5 Buck→5V LDO|UNKNOWN/UNKNOWN/UNKNOWN|LDO≤200mA；完整dropout/纹波/热/启动|候选|
|各阵列AFE/偏置|UNKNOWN/UNKNOWN/UNKNOWN|2OPA封装=8运放；参考和线负载要计入|RX/增益/过驱参数缺失|

推荐的原厂依据及精确页/公式索引见SOURCE_REGISTER.md。未给出无依据的轨纹波上限、真实功耗、声功率、悬浮力或温升保证。`Ppath=I²R`、`Pldo=(Vin−Vo)I`、`Tj=Ta+Pθactual`保留变量；噪声/温升门限须在下轮Acceptance中具体化。

执行契约：Goal为PCB-S2审查及前置论证。Scope仅当前v5、current shared/AI记录及离线公开资料。Allowed为独立工作树、审查/计算/BOM候选/日志、正常Draft提交同步。Non-Goals为完整原理图/最终BOM/制造/板写/RTL修改。Invariants沿用128TX8RX/8bit请求校准分离/共时基/原子map/签名采集ACK/35dB/50Hz/几何。Validation为实际资料读取、库存复算、独立数值交叉检查、原243及fullnextstage。Rollback为保留原基线/旧BOM，不覆写旧证据；候选分支可独立审阅。DoneWhen为审查资料可复算、所有缺口显式、真实数字结果留证、Draft同步，不以模型自证硬件闭环。S2-B P0未闭环时不启动S2-C全量定型。
