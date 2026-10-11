# 原理图/连接表/ERC/审图状态

SCHEMATIC=NATIVE_NOT_CREATED；ERC=NOT_RUN；NATIVE_CAD_CONNECTION=NO_PROCESS_NO_BRIDGE_CLIENT_OBSERVED。工具条件检查见PREFLIGHT.json。按S3允许降级交付严格pin/net表，而非伪装成功导入嘉立创EDA。

netlist/COMPONENTS.csv：2126个明确装机位号；PIN_NET.csv：6390个pin处置；THREE_BOARD_CANDIDATE.json与GENERIC_NETLIST.xml为可解析严格连接候选，XML不是原生EDA项目。未提交无许可证第三方源码。svg/带物理pin/net标签，REVIEW.html可搜索位号/网名/浏览模块；图由规范表生成，独立核查仍以手册和外部Reviewer为准。

SEMANTIC_REVIEW.json：45项最终PASS，板内单端网络0；SAFETY_TRUTH_TABLE.csv：256种布尔状态。结果只证明所列静态关系，不证明类比电路瞬态/布局/制造。曾失败J11_NC检查：检查器把OPEN_DRAIN两根I2C误归未分配电源触点；依据已批准pinmap修正分类，不删除I2C、不放宽电源NC。SEMANTIC_REVIEW_FAILED_01.json保留原失败。前期237项连接合约中包括逻辑TX通道，现只取63实际信号GPIO建立中央缓冲器，防止虚增128条物理接口。

手工审查已覆盖：C16完整64pin及REGCAP/REFCAP、5954used/NC、TC两级非反相和12V域、TPS物理pin/OD/厂设timing、FF pin5非反相Q、TCA RESETpin3与A2pin21、USB OUT2、NC电源、三板BOM数量。所有结论来自当前连接表与原厂资料，**不是独立Reviewer签字**。

Native导入要求：创建正确符号/封装并逐pin对照；先导入电源/安全/TX一通道/AFE一通道、确认复制映射，再全板绘制；运行真实ERC，逐告警记录处理，产生导出网表与本表差异。可沿用当前位号，无需改RTL。完成前G1仍HOLD。

本轮243测试PASS；S2完整帧/综合证据继承，当前未做SPICE、IBIS、外部STA、PCB DRC、硬件验证。没有把45项脚本检查命名成ERC。
