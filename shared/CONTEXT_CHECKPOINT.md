---
checkpoint_id: CP-20261009-004
project_id: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
branch: chore/v5-ax7020-workspace-isolation
base_commit: ecd32e76e9b6c08806eae30a3c75a9c3be5e7570
head_commit: f014214fb8db554fb3df9ac971ac759d683447a5
active_version: v5
version_status: ACTIVE
current_stage: AX7020_V5_MIGRATION_CANDIDATE_USER_REVIEW
created_at: 2026-10-09T13:53:22.176049+08:00
created_by: Codex
checkpoint_reason: draft_publication_remote_tree_and_independent_ci_pass
source_of_truth: repository_and_actual_tool_evidence
status: VALID
---

# 当前恢复检查点：候选迁移已验证，等待人工合并审查

## 1. Current Identity

PROJECT_ID 为 SONOFIELD_FPGA；Repository 保持不变；当前分支 chore/v5-ax7020-workspace-isolation；v5 ACTIVE。本次执行候选路径为 `E:\Codex_project\AMD_Sonofield`，正式 `workspace_path` 尚未提升。旧物理沙盒原样保留。上方 head_commit 是已发布并已核验远端树的真实证据提交；两份环境实际验证的功能源码为 `0ab574f9e2ad422106655f3c827e89d262d93bb4`，功能输入仍完全相同。本发布检查点及回执在随后提交保存，包含提交由Git文件历史定位，避免虚构自引用SHA。

## 2. Current Goal

完成同一 v5 的独立工作空间迁移、旧 Git 跟踪树完整封存、当前事实入口整顿及全链路离线回归，然后交付可审查候选。不是版本升级。正式 main 合并、合并后远端 main 冷启动以及永久工作区提升仍需用户批准。

## 3. Architecture

保留 Host 轨迹→PS C 服务/协议→AXI→PL 的数字链路；128TX/8RX，8bit requested/calibration 相位独立，共同时基、完整相位图 atomic commit、32 lanes×4 used、50Hz motion cadence、ADC/校准链路。TX 为 NU40C10T，RX 完整料号未知，正式 ADC 为 AD7606BBSTZ-RL，C-16 仅候选。上下各 64TX 阵列采用独立外部电源及保护/默认关断；AX7020 仅控制与数据。辐射面中心距12mm，上下 nominal100mm、可调90–115mm，几何中心为原点。物理链路尚未验收。

## 4. Completed

- IMPLEMENTED：精简当前根、唯一 v5 活动树、构建及搜索允许列表、当前状态和复现文档。
- TESTED：3907 个旧 Git 原文件及2个冻结元数据，路径/mode/blob/raw SHA256 一致；102个受保护核心/测试/黄金/BOM文件不变；旧沙盒101394个唯一文件（含额外忽略依赖及根Git）复核无变化。
- SIMULATED：BASE、MIGRATED retry1、CLEAN_CLONE 各115项Python测试、3696帧×4、全部嵌套C/AXI/安全/波形/校准/黄金等价；各15项离线候选检查及ADC256帧双仿真器检查。
- SYNTHESIZED：三份环境分别完成 Vivado2025.2 OOC 综合和工程重开，均加载自己 v5 下的18个RTL源。
- HARDWARE_VERIFIED：本次没有新增硬件功能验证，也没有执行设备操作。

## 5. Current Plan Position

Phase0–5 的候选门禁通过。Phase6 已建立Draft PR#1，远端候选树核对通过，push与PR的独立Linux结构/冻结检查均success；当前等待人工审查。main合并和合并后重新clone属于后续批准步骤。Phase7回滚方案已准备，未执行回滚。

## 6. Next Actions

1. 核对最新 publication receipt、候选提交及 Draft PR；若尚未发布，完成候选分支推送和在线CI。
2. 用户审查具体候选、证据与永久工作区路径；未批准前不合并main。
3. 获得明确批准后重新 Reconciliation；main若已变更，先分析差异并重跑受影响门禁。
4. 执行普通非强制合并，从远端main独立clone并验证冷启动及冻结清单，再提升用户认可的工作区。
5. 迁移达到候选交付点后停止低收益优化；物理工程另按已批准路线推进。

## 7. Active Decisions

ADR-035：原v5授权；ADR-036：历史只读板卡识别授权；ADR-037：当前用户明确迁移授权，保留原仓库和旧沙盒、main须人工审核。原文与来源在当前DECISIONS中保留；历史板卡授权不自动延续到本任务。没有伪造ChatGPT Decision。

## 8. Blockers / Critical Issues

未发现尚未闭环的候选功能回归或关键错误。main合并、合并后远端冷启动、永久路径提升及独立最终Review待用户。物理V5-B01/B03/B04/B05、BOM/ADC问题、原生原理图/ERC和外部ChatGPT历史访问仍受阻；唯一当前阻塞表为BLOCKERS.md。整机结论REVISE，制造HOLD。

## 9. Latest Validation

实际结果见 PORTABILITY_AND_REGRESSION.json 及 v5/evidence/migration/20261009 下 base、migrated_retry1、clean_clone 的 summary、真实日志、loaded_sources及runtime_ownership。日期2026-10-09；源码提交 `0ab574f9e2ad422106655f3c827e89d262d93bb4`；BASE `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`。四类规范化功能Hash与历史BASE和三份新运行完全相同。OOC均WNS+0.994ns/WHS+0.157ns、7219LUT/17918寄存器/4RAMB36；18源与重开门禁通过。没有布局布线或实板Timing闭合声明。

## 10. Known Limitations

第二份Git和venv独立，但共享同一主机安装的Vivado/Icarus/GCC，不能称第二台机器或另一OS。ARM目标编译器/BSP及真实PS-PL/DDR/UART/ADC/AFE/驱动/供电/声学未验收。OOC尚无板级输入输出延迟约束，HD.CLK_SRC未设置，不能据此声称完整CDC或板级Timing通过。原生v5原理图NOT_CREATED、ERC_NOT_RUN、MANUFACTURING_HOLD。BOM生成器没有进行冷启动重建；原工作簿字节和15项只读检查已验证。ChatGPT完整历史读取BLOCKED，当前Codex记录PARTIAL，独立最终Review待办。

## 11. Do Not Change

保护旧物理沙盒及私有/未跟踪/忽略/Git元数据；保护冻结history_old字节/mode/blob；保护核心RTL/FW/software/tests/goldens/BOM/协议/寄存器/安全和Acceptance。无用户明确授权，不合并main、不开新版本、不操作板卡。后续日常任务不读取封存历史和旧沙盒；只有用户明确点名恢复/溯源才例外。

## 12. Invariants

保持第3节架构与几何、正式ADC、上下独立外部供电。保留35dB校准阈值：translation norm<0.1mm、angle norm<0.1deg、f0RMSE<80Hz、phaseRMSE<2deg。不得使用skip标记替代完整门禁，不得修改黄金数据或降低阈值。OOC、仿真、历史只读识别和物理验收严格区分。

## 13. Open AI Problems

P-20261008-001（ADC40kHz带宽）；P-20261009-001（AX7020 Rev3 PS平台）。当前路径、ID、正文Hash和v5版本均已核对，正文未改动，无虚构Decision。

## 14. Repository Delta Since Previous Checkpoint

旧树和当前根已提交；首次迁移Tcl配置路径门禁误拒绝本克隆临时测试夹具，保留9个失败断言和日志后修复为本克隆config/build范围，原测试及完整回归重跑通过。第二份独立Git/新venv完成全部离线回归、OOC与重开。旧沙盒完整性、源码/搜索隔离与隐私审计已通过。冻结历史和102个受保护文件没有变化。

## 15. Resume Instruction

先读取当前恢复文件、真实Git状态/HEAD/远端和publication receipt，再审阅Draft PR。等待用户main合并与路径提升批准；继续当前v5，不从旧历史重新推断状态，不创建v6。

## 16. Evidence References

shared/migration/QUALITY_GATE.json、PORTABILITY_AND_REGRESSION.json、OLD_TRACKED_MANIFEST.json、ARCHIVE_COVERAGE.json、ROLLBACK_PLAN.md；v5/evidence/migration/20261009/digital_behavior_comparison.json、ooc_comparison.json、old_sandbox_preservation.json、active_reuse_hashes.json、search_isolation.json及三份真实baseline目录。

## 17. Provenance / State Conflicts

依据当前Git BASE/源码/index、原正式Decision、当前实际用户Phase0–7文件及请求、真实工具输出和初始私有清单。旧shared中的v2/Robei阻塞叙述属于历史，当前v5事实优先。board_clock_candidate仍在继承的18文件清单中，但未被实际顶层实例化，不构成AX7020物理时钟依据。失败日志仍标失败，重跑结果独立保存；不推断隐藏思维或不可访问的ChatGPT消息。

## Publication Update

[Draft PR #1](https://github.com/loverlike1216/SonoField-FPGA/pull/1) 已实际发布；观察证据提交 `f014214fb8db554fb3df9ac971ac759d683447a5`；main仍为 `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`。在线push和PR结构检查均success，详细回执见shared/migration/PUBLICATION_RECEIPT.json。下一最小动作是用户审阅候选并决定main合并和永久路径；禁止自动合并。在线结构验证不等于全功能或实板验证。
