# SonoField-FPGA v5 历史隔离候选迁移报告

迁移专项结论：**ACCEPT WITH LIMITATIONS**，可供用户和独立 Reviewer 审核。整机结论仍为 **REVISE**，PCB/制造保持 HOLD。当前没有合并 main，没有进行任何实板编程、复位、DDR RAM、UART/GPIO 或 PCB 制造操作。

## 身份与 Repository Reconciliation

| 项目 | 核验事实 |
|---|---|
| PROJECT_ID / 正式仓库 | SONOFIELD_FPGA / https://github.com/loverlike1216/SonoField-FPGA.git |
| 活动版本 / 沙盒 | v5 / E:/Codex_project/AMD_Sonofield；不是版本升级 |
| main 基准 | ecd32e76e9b6c08806eae30a3c75a9c3be5e7570 |
| 迁移前完整 v5 | 7dda49f00983c57d06ac639ad70bdaff9696e900 |
| 实际独立环境测试代码 | 3e788f4a2763c0354ca66d3836d0709dcf9f0107 |
| 迁移分支 | codex/v5-historical-project-isolation-20261009 |
| 新历史根 | Historical project/，大小写与空格完全一致 |

指令中的 main 快照较旧：完整 v5 已位于未合并 PR #2，候选沙盒已有 history_old/，当前 BLOCKERS/ACCEPTANCE 已是 v5，测试已从 115 增至 171。本分支从最新 main 创建，再普通快进纳入完整 v5 候选；main 没有移动。新 PR 包含仍未合并的 #1/#2 祖先提交，审核时必须明确处理这些依赖。

## 实际移动与完整性

6,670 个源 tracked 文件逐项唯一分类：**3,911 移动、2,759 保留**。移动项包含既有冻结快照 3,909 项及两份 v2 专属指令副本，共 **99,317,849 字节**，逐项原始 SHA256、Git blob、mode、size 全部保持。另新增 7 份冻结索引文件；历史目标共 3,918 个 tracked 项。没有重复嵌套一份旧归档，没有删除历史数据或改写冻结正文。

当前 v5 的 **2,695 个原文件全部保留原路径**，其中 **2,693 个 blob/mode 不变**。两处审查过的修改是 README 导航及历史元数据检查器。核心 RTL、C/算法/协议、寄存器、测试、黄金结果、阈值、正式 ADC、所有 BOM 和已有证据均不变。根 shared/、有效批准来源和两个当前 open problems 未整体移动。

历史原始 .gitattributes 改名为惰性文本，内容不变，防止旧 Git 属性在新路径下生效。旧跨根目录链接保持冻结原文；通过逐文件映射或固定原始 checkout 恢复原树。Robei 内容保留在完整旧版本/资料上下文中；源树没有独立 tracked EBAZ4205 项目，未从私有沙盒猜测导入。暂停 v3 与原物理沙盒未访问、未移动。

## Gate 与真实验证

| Gate | 结果与证据 |
|---|---|
| 0 | 固定 refs/源树、tracked 清单、私有资产元数据清单；本次新执行迁移前完整基线，未复用旧 PASS |
| 1 | 全文件分类、MOVE/KEEP/SPLIT、依赖清单、无目标覆盖/大小写冲突；缺失 BLOCKERS_ENGINEERING 如实记为 MISSING |
| 2 | 审核清单驱动实际 Git 移动；原件字节/blob/mode/size 全部一致，无 tracked 数据遗失 |
| 3 | 根规则、rg/明确 git grep allowlist、IDE、仅展开当前目录的 CI；默认检查器 open 审计历史正文访问 0 |
| 4 基线 | 迁移前及独立克隆后各 **171 tests，3,696 frames × 3 Icarus + 1 XSim**；canonical 轨迹/map/trap/ACK Hash 前后一致，C/AXI/校准/安全/黄金等价通过 |
| 4 新增功能 | 新锁定环境完整 pre-PCB：supervisor/mailbox、实际新 top 双工具通过；5 组真实 GUI 回调共 375 帧；160 maps / 20,480 Python-C words；10 sparse fits / 5 seeds / 5 starts |
| 4 Vivado | 原生 2025.2 current create_project 综合并重开，before/after/clean 三组源列表、器件、时钟、资源、时序检查一致 |
| 5 | 当前硬件/BOM/合同/证据保留；正式 AD7606BBSTZ-RL、NU40C10T、128TX/8RX、32×4、几何及供电边界未变 |
| 6 | 公开范围/秘密/隐私/许可证及 Git diff 审查、普通分支推送和 Draft PR；实际 PR/远端/CI 状态单独记录在 publication receipt |
| 7 | **DEFERRED**：用户明确批准具体 PR 合并后，才执行正常合并及新远端 main 克隆核对 |

独立克隆使用 --no-hardlinks、新 Git 仓库和新安装的锁定 venv；工作树物理不含 Historical project/。它共享本机 OS 与 EDA 安装，不能称为另一台电脑。所有新增传感/校准数据仍是 SYNTHETIC / ALTERNATIVE_VALIDATION；GUI 为实际自动回调，未声称人工绘制验收或真实粒子位置。

## Vivado 与现有风险

三次 core OOC 均为 xc7z020clg400-2、18 个当前 v5 RTL、132 MHz 内部目标（7.576 ns），资源 **7,219 LUT / 17,918 FF / 4 BRAM**，综合态 **WNS +0.994 ns / WHS +0.157 ns / WPWS 3.288 ns**。no_clock 与 unconstrained_internal_endpoints 为 0。

三次各保留相同 **28 条综合 warning**，含原有 motion_queue 置位/复位优先级、RAM 推断及其他提示；无新增差异、critical warning 或 error。**2,324 个输入、256 个输出缺少外部延时**，没有被忽略或伪装成整板 PASS。本次 core OOC 与上一轮 pre-PCB routed top 的报告范围不同，均不能关闭 Rev3 全板约束/时序门禁。

原有 13 项 Rev3/电源/引脚/PS-DDR/UART/ARM-BSP/ADC/硬件安全/声学/原理图/ERC/独立 Review 门禁保留。外部 ChatGPT 读取仍 BLOCKED，当前可观察 Codex/工具记录 PARTIAL；没有伪造独立 Reviewer 结论。

## 公开审查、回滚与审核边界

移动候选中未发现凭据或私网 IP；一个 serial 字段匹配为 ADC 总线描述。ZIP 的 305 个 JSON 成员已检查。公开范围只含既有项目产物、当前代码/治理及本次证据；私有资产清单仅本地保存。保留实际工具/工作区路径用于复现，不导入私人资料或设备标识。没有新增厂商文件，不据“原先公开”推断第三方许可；未来导入需独立审查。GitHub 网站索引不受本地 ignore 控制。

主要审核风险是 PR 包含先前未合并候选、目录移动规模较大，以及历史原文跨目录链接需映射恢复。未合并时关闭/保留 Draft PR 即不影响 main；合并后通过正常、经审查的 git revert 回滚，不 reset/force push/改写历史。固定源 SHA 可在独立克隆中恢复。两个已解决的本地执行失败见 operation_failures.json，未为 PASS 改动测试或阈值。

复现步骤见 shared/repository_cleanup/RUNBOOK.md；回滚见根 ROLLBACK_PLAN.md；文件映射见 Historical project/MIGRATION_MANIFEST.csv 和活动副本 ARCHIVE_PATH_MAP.json。最终线上状态以 shared/repository_cleanup/PUBLICATION_RECEIPT.json 与 PR 为准。候选已完成离线验证，等待人工合并批准；不代表 main、实板或制造已经验收。
