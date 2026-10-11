# BOM独立复核与差分

源为当前工作树 `v5/hardware/bom/working/2026-10-11/BOM_V5_FOUR_SOURCE_20261011.xlsx`，SHA256 `a55b38dab4ce6004ac542e2c5fc0a09a365616ebbe9b3ec2bdf603f7a1726b1c`。原文件未修改。没有从历史聊天复制1205结论：`calc/audit_inputs.py`重新解析ZIP/XML；`review_calculations.py`重新加总和检查公式缓存。原始XML证据、重算结果分别在WORKBOOK_XML_AUDIT.json、BOM_RECOUNT.json。

| 分区 | 装机 |
|---|---:|
|Upper|551|
|Lower|551|
|Central|83|
|External|20|
|合计|1205|

101种物料，5 sheets。逐板404个`ROUNDUP(q*(1+spare),0)`采购计划缓存，与Summary606个引用/合计共1010项公式检查；没有把备品计入装机。BOM_INPUTS quantities实际次序是Upper/Lower/Central/Spare/External。旧装机无源R554/C302/L4，磁珠另列。

本轮新增 `BOM_INPUTS_S2_CANDIDATE.json` 和 `07_BOM_DELTA_DRAFT.csv`，未覆写既有BOM生成器输入或工作簿。旧B008/B009两行在新候选中装机各0，保留previous_quantities及来源；S2-001 TPS3851H33EDRBR上下各1，整机2。若只有此变化，550+550+83+20=1203；这只是算术方向，不含尚未分解的保护网络，也未扣未证实的重复。

| 动作 | 数量意义 |
|---|---|
|删除旧监控占位|B0082+B0092=4物理IC，旧功能仍保留|
|新增批准方向|TPS3851总2；功能覆盖不完整|
|无源已冻结新增/删除|0/0，S2-C被P0阻塞|
|条件修改审查|B030电感4；B022电阻3、B062电阻3、H020电阻128，共R134；不是已确定134颗新规格|
|功能重复/用途疑点|B054100kΩ180颗可能含输入下拉；B0610Ω136颗可能与输出阻尼预留冲突，不能直接删|
|额外保护网络|H009/H010/H011/NS004等每“网络×1”不是单器件，需展开FET/锁存/比较器/门控/泄放/保险/TVS|

人工位号完全相同的重复检查为0，但位号由BOM ID生成，不能证明功能无重复。所有860个R/C/L引用已进入06 CSV，真实net均未核实；B067/B068等DNP行仍在差分，不凑装机数。

1.65kΩ、1.37MΩ、590kΩ旧参数不得默认为TPS26631正确。20mΩ在5A超过INA226量程，若目标为5A，考虑容差后需 `R≤81.92mV/(5A*1.01)=16.22mΩ`，例如10mΩ只作为下轮候选；中央5V不同电流需单独算。每路100k默认下拉的阈值也未闭合；4个电感不等于能提供5A的Buck。

**BOM采购/HW/ERC/制造全部HOLD。** 本轮不新增xlsx，避免旧文件看起来已获最终批准。正式RCL分配和保护电路接受后才生成下一次BOM_RELEASE_CANDIDATE。禁止把1203或本包建议值作为直接采购单。
