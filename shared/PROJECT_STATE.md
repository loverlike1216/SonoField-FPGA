# SonoField-FPGA v5 当前候选状态

同一 SONOFIELD_FPGA Repository，v5 ACTIVE。本任务为工作空间迁移，不升级版本。BASE为 `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`，实际验证源码为 `0ab574f9e2ad422106655f3c827e89d262d93bb4`。候选执行路径 `E:\Codex_project\AMD_Sonofield`；正式workspace_path尚未提升，main尚未合并。旧物理沙盒完整保留。

BASE、MIGRATED retry1和第二份独立CLEAN_CLONE均完成115项Python测试、3696帧×4、全部C/AXI/安全/波形/校准/黄金等价、15项离线候选检查、ADC256帧双仿真器、Vivado2025.2 OOC及18源重开；规范化Hash完全一致。旧Git树3907个原文件及2个冻结元数据无Hash/mode差异，当前v5的1017个原文件保留，102个受保护核心/测试/黄金/BOM文件未改动。

结论 **ACCEPT WITH LIMITATIONS — CANDIDATE ONLY**。人工main合并审查、合并后远端冷启动和永久路径提升待办。整机仍REVISE，原生v5原理图NOT_CREATED/ERC_NOT_RUN/制造HOLD。NU40C10T、未知完整RX料号、正式AD7606B、未批准C-16候选和上下独立外部供电边界明确。机器事实入口为PROJECT_STATE.json，恢复入口为CONTEXT_CHECKPOINT，当前唯一阻塞表为BLOCKERS.md。

发布核对：Draft PR #1 `https://github.com/loverlike1216/SonoField-FPGA/pull/1` 已建立；远端证据提交 `f014214fb8db554fb3df9ac971ac759d683447a5`，main仍为BASE；独立Linux push/PR结构门禁均已实际通过。当前恢复检查点CP-20261009-004，回执PUBLICATION_RECEIPT.json。下一动作仅为用户审核，获批准后才合并和远端main冷启动。
