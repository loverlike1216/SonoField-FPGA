# 当前 v5 工作计划

Phase0只读对账/私有完整清单、Phase1独立新clone迁移前BASE、Phase2完整Git旧树封存/活动v5抽取、Phase3当前AX7020事实整顿、Phase4运行和搜索路径隔离、Phase5迁移后及第二份干净环境完整回归均已通过。首次路径修正失败与恢复日志保留。Phase6发布候选/Draft PR/真实CI/远端回执后，等待USER_APPROVAL_REQUIRED_FOR_MAIN_MERGE。Phase7回滚方案已准备，未执行。

下一最小动作：人工审阅具体候选、全部证据、Rollback和永久工作区路径。用户明确批准后，重新检查远端main，普通非强制合并，独立clone远端main完成冷启动及冻结清单核验，再提升批准的工作区。旧沙盒不pull、不清理、不改动；后续默认不读取旧沙盒或history_old。继续意味着继续v5，不开v6，不修改核心/黄金/阈值，不操作设备。

后续硬件工作需单独闭环Rev3等级/VCCO/PS DDR/IO/时钟/运行镜像所有权/UART/BSP、正式ADC带宽、电气评审、TX/RX资质、上下独立供电/杀停/AFE，随后原生原理图/ERC和另行授权的无负载及声学测量。迁移候选达到交付点后停止低收益优化，整机仍REVISE。
