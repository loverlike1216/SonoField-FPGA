# v5 PCB-S2 执行基线与对账

本轮结果 **REVISE**。S2-A 调查及 S2-B 候选论证已形成；S2-B 的默认关断、窗口监控、真实负载等 P0 未闭环，因此 **S2-C 全量 R/C/L 定型 BLOCKED**。随包提交的计算和 BOM 是可审查候选，不是采购放行。

| 项 | 本轮真实状态 |
|---|---|
| PROJECT_ID / version | SONOFIELD_FPGA / v5 ACTIVE，无升级 |
| Repository | https://github.com/loverlike1216/SonoField-FPGA.git，PUBLIC |
| PCB workspace / branch | E:\Codex_project\AMD_Sonofield_PCB_v5 / feat/v5-pcb-design |
| 基线 HEAD | 8c27b5841b5494c3761ab211881a3ea2be63e8c8 |
| 集成依赖 | Draft PR #5 → #4 → #3 → main；#1/#2 是早期候选，不作为本轮基线 |
| main 查询值 | ecd32e76e9b6c08806eae30a3c75a9c3be5e7570 |
| 原恢复点 | CP-20261011-001，checkpoint commit 09201d34d15b21c4956f2d2377cc4daea33b1f71 |
| 当前工程 | AX7020、AD7606C-16、128T/8R、32 lanes×4 used、50Hz motion |
| 几何 | 板内 TX pitch12mm；辐射面距100mm，允许90–115mm；几何中心原点；EPS2–5mm |
| 外部 ChatGPT | CHAT_MEMORY_ACCESS_BLOCKED；本包是 Codex 审查，未伪称外部 Review |
| CAD / ERC / DRC / hardware | NOT_CREATED / NOT_RUN / NOT_RUN / NOT_VERIFIED |

用户明确回复“按文件执行，并批准上述工作树路径”。正式输入位于 `AI-interaction-memory/codex/instructions/v5_pcb_architecture_parameter_review_20261011.md`，SHA256 `d14eb709d7b625158ba40af32b2b0c56166101dc6e4beeb68b485d5d2da35e2e`。保留启动原文及实际回复的 PARTIAL 交互记录。

本工作树只物化当前允许目录，`Historical project/` 未物化、未读取其正文。共享 Git 对象库不等于允许访问历史正文。原工程的 `BOM/` 未跟踪资产保持原样；本轮没有移动、覆盖或清理它。

读取了 README、AGENTS、PROJECT_STATE、VERSION_STATE、CONTEXT_CHECKPOINT、CURRENT_PLAN、DECISIONS、BLOCKERS、ACCEPTANCE、当前 AI-problem，以及 v5 的 design_20261011、next_stage/20261010、硬件审查文档、BOM 和当前 RTL。ADC 决定 P-20261008-001 的 ID/version/body hash 对齐；其授权只确定 C16 方向，未放行电气设计。BRAM 问题 P-20261010-001 仍开放。

| 冲突 | 当前处理 |
|---|---|
| B-008 TLV803/TPS3839、B-009 TPS3430 原占位共4颗 | 新候选旧两行装机0，新增 S2-001 TPS3851H33EDRBR 上下各1，总2颗；原行及数量保存追溯 |
| 旧文档要求独立窗口看门狗，TPS3851 只有超时检测 | 保持既有安全要求；开 P-20261011-001，不自行降低要求 |
| 旧 B-062 1.65kΩ 所带“约2.02A”说明 | 不能用于 TPS26631，需重新计算；中央保护 IC 未选定 |
| 旧 100kΩ180颗和新增输入下拉128颗 | 实际网络未分配；功能重复待查，不能因人工位号不同认定不重复 |
| 旧中央 header 取电 / XT30 | ADR042 为独立 USB-C 中央、上下独立 DC5.5×2.5 中心正；header 电源触点 NC |
| 文档提到工作簿名不一致 | 本轮找到并独立读取 FOUR_SOURCE 工作簿；没有冒称存在同名 C16_WORKING 工作簿 |

工作簿重新按 ZIP/XML 读出，101类型、5 sheets，上551/下551/中央83/外部20，总1205；R554/C302/L4只是旧库存行数量。完整明细和公式检查见 `BOM_RECOUNT.json`。S2 只落实监控 IC 合并时算术总数1203（550/550/83/20），新增保护电路和重复项尚未量化，1203不是最终 BOM。

验证命令、运行结果以 `09_VERIFICATION_MATRIX.md` 和 `v5/evidence/pcb_s2_20261011/FINAL_VERIFICATION.json` 为准。本轮不修改正式 RTL、PS/PL、XDC、golden、阈值，不生成制造文件，不操作板卡，不合并 PR。
