# SonoField-FPGA v5 — AX7020 唯一活动工程空间迁移、旧仓库树封存与全链路回归：Codex 正式执行指令

> 指令性质：面向 Codex 的 **有门禁、可回滚、先验证后切换** 的工程重组任务。此文件是任务要求，不是已经执行迁移的证明。  
> 编制：2026-10-09；当前依据：GitHub `main` 在调研时 HEAD `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`，实际执行时 **必须重新获取最新 HEAD**。  
> PROJECT_ID：`SONOFIELD_FPGA` · Repository：`https://github.com/loverlike1216/SonoField-FPGA.git` · 唯一活动版本：`v5` · 板卡：`ALINX AX7020` · 开发工具：`Vivado/Vitis 2025.2`。  
> 当前执行模式：`CONTINUE_CURRENT_VERSION / WORKSPACE_MIGRATION_WITH_FREEZE_GATES`。**不产生 v6，不创造 v4，不迁移成另一 Repository。**

## 0. 最终目标和不可折衷原则

目标是在独立的新 Windows 沙盒中继续 **AX7020-only 的 SonoField-FPGA v5**，同时在同一 GitHub Repository 下将 **迁移基准时旧仓库根目录的全部已跟踪工程内容，按原相对路径封存到 `history_old/`**。迁移后仓库根只保留精简的活动恢复入口、活动状态文档、`v5/` 工程和只读 `history_old/`，为今后作品/论文/展示交付创造干净的基础。

不可折衷原则：

1. 旧本地沙盒 `E:\Codex_project\AMD-SonoField-FPGA` **原样保存**，不得剪切、删除、移动、覆盖、`git pull` 重置或以其为工作区开展新迁移实验。用户口中的“剪切到 GitHub”应安全解释为 **Git 跟踪树的受审阅路径迁移 + 旧本地物理副本不动**；GitHub 的 `.git` 历史本来由 Repository 保存，**绝不可嵌套上传 `.git/`**。 
2. 新独立工作区**建议候选**：`E:\Codex_project\SonoField-FPGA-AX7020-v5`。执行前先确认用户已批准/指定的实际新沙盒路径；若只有这个建议路径，可在确认为不存在且与原工作区不重叠时建立候选克隆，但在用户确认前不要擅自将其写成已批准的永久 `workspace_path`。所有构建/依赖/生成物必须留在新沙盒对应路径内。
3. **同一个 GitHub Repository 和其现有历史/`main`**。禁止 force push、rebase 历史、孤儿分支替换历史、`git reset --hard`、全局清理、`git clean -fdx`、删除旧物理目录和覆盖未追踪用户资料。
4. **`history_old/` 只读封存**：默认的 Codex 搜索、IDE 索引、构建、测试、打包、Vivado source list、Python import、CI 不访问它。仅本次迁移审计/证据对比、未来用户明确下令恢复/溯源时例外。不得把旧 Robei/EBAZ 板级文件当作 AX7020 引脚、电压、串口、PS/DDR 或 Timing 事实。
5. **必须维持原功能和既有 Acceptance**。不得为“迁移成功”删减测试、放宽断言、更换黄金参考去迎合实现，或以 stub/mock/fake 冒充真实板级结果。
6. 本任务允许对候选目录、迁移分支、当前文档、必要的路径/构建配置做**可恢复、可审计修改**；**合入远端 `main` 前必须提交完整证据并取得用户人工批准**。任何无法闭环的实质风险停在候选分支，不能声称已正式切换。
7. 根目录应只有 **一个活动生产实现**：`v5/`。`history_old/v5/` 是迁移前历史快照，并非第二个开发版本，不得被任何运行入口引用。

## 1. 当前 Repository 事实（必须刷新，不可用本文代替实时仓库）

截至本指令编制时已读取真实 Repository：

- `main` HEAD：`ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`，根目录当前包含 `v1/`、`v2/`、`v5/`、`PCB/`、`BOM/`、`shared/`、`archive/`、`AI-*`、`evidence/`、`parameter_detection/` 等。
- GitHub 树包含约 **3907 个普通已跟踪文件**、约 **97.6 MB 合计文件字节**。实际迁移前需重新生成精确清单；旧本地未跟踪/忽略的文件**不在上述数量中**。
- 版本状态：`v5 ACTIVE`；`v1/v2 FROZEN`；`v3` 为未完整发布的暂停本地历史；`v4` 不存在。
- v5 最新工程 stage：`AX7020_BOARD_DETECTION_BOM_REVISION_AND_INTEGRATION_PREFLIGHT`；最新 Checkpoint：`CP-20261009-001`，之后请核查是否出现新提交。
- 最新真实板级证据：实板标签 `AX701020.3.0 / PCB Revision 3.0`；JTAG 已识别 `XC7Z020` / `0x23727093`，封装 CLG400 有照片证据；当前 PS 两 Cortex-A9 Running、PL DONE=1、SD 启动。完整速度/温度等级、Rev3 匹配 PS/DDR/IO/VCCO/安全内存所有权依然待证。**不得覆写现有启动镜像、重新配置未知 PL、读写未经授权 DDR。**
- 最新 v5 全数字回归：115 个 Python tests、3696 帧 × 三次 Icarus + 一次 XSim；协议/C/AXI、安全/波形/校准等价回归 PASS。v5 原生 Vivado 2025.2 的现有 132MHz OOC 综合属于 **pre-route**，不是 AX7020 板级全约束 Timing PASS，更不是实板闭环。
- 发射器：用户明确 **NU40C10T**，128 TX，8 RX；RX 完整料号及 NU40C10T 供应商完整封装/电参尚待确认。上阵列、下阵列各独立 12V 外部电源输入与保护，**AX7020 只负责控制/数据，不通过 FPGA 供给发射功率**。
- 正式 ADC 仍 `AD7606BBSTZ-RL`；`AD7606C-16BSTZ-RL` 仅是候选，不得未经独立 Review + 用户正式批准切换。NU40C10T 新 BOM 是 `v5/hardware/bom/working/2026-10-09/` 的工作副本，尚未电气放行；旧 `v5/config/hardware_parts.json` 的 TCT40 是待清晰处理的历史数字/配置兼容项，**不能直接以它作为生产采购 authority**。
- 当前老 `shared/BLOCKERS.md` 与 `BLOCKERS_ENGINEERING.md` 存在大量 **v2/Robei** 叙述；当前 `PROJECT_STATE`、`CONTEXT_CHECKPOINT` 已切换 v5。迁移必须消除此类“当前事实入口错乱”，但保存历史原文及来源。

优先检查及重新确认：`README.md`、`AGENTS.md`、`shared/PROJECT_STATE.json/.md`、`shared/VERSION_STATE.json`、`shared/CONTEXT_CHECKPOINT.md/.json`、`shared/CURRENT_PLAN.md`、`shared/DECISIONS.md`、`shared/BLOCKERS*.md`、`shared/ACCEPTANCE.md`、`v5/README.md`、`v5/evidence/board_bringup/20261009/RESULT.md`、`v5/evidence/baseline/board_integration_20261009/summary.json`、`v5/hardware/integration_candidates/20261009/`、`AI-problem/problem/P-20261008-001*` 与 `P-20261009-001*`。找不到的文件须标记缺失，不能伪造。

## 2. Scope / Non-Goals

### Scope

- 审计远端、旧本地、未提交数据和当前 v5，建立有 SHA256 / Git blob SHA / 路径 / 来源 / 权限 / 作用域的完整清单。
- 新独立 clone 与迁移前后 baseline；原历史根内容完整 Git 路径封存到 `history_old/`；构建一个唯一 AX7020 生产树。
- 修复当前活动文档、代码加载路径、运行脚本、CI、IDE 搜索、EDA 工程引用和 metadata 中的旧路径/板卡混淆。
- 保留所有有效 v5 软件、RTL、FW、ADC/自校准、轨迹、BOM/PCB、测试、数据、产物复现入口；定义作品交付边界。
- 在候选分支做两类以上独立验证，并在用户批准后合并和 remote verification，形成恢复 checkpoint、冻结清单和 Rollback 方案。

### Non-Goals

- 不升级 v6；不重做或削减 128TX/8RX 架构；不自动改正式 ADC；不因目录整理重新选定 FPGA pin、DDR、时钟；不做生产 PCB/制造 Gerber；不改变 SD/Flash/启动模式；不主动碰板卡；不强行解决外部物理阻塞；不推翻稳定寄存器/协议/相位算法/验收标准。

## 3. 工作区/仓库目标组织

### 3.1 本地（两个彼此独立的 Git 工作目录）

```text
E:\Codex_project\
├── AMD-SonoField-FPGA\                  # 旧本地沙盒；完整原样只读保留
└── SonoField-FPGA-AX7020-v5\            # 新沙盒建议候选；独立 clone；此后唯一活动开发
    ├── .git\                            # 新沙盒自己的 Git 元数据（只在本地）
    ├── README.md / AGENTS.md
    ├── shared\                         # 仅当前正式事实
    ├── AI-problem\                     # 当前有效问题、决策接口
    ├── v5\                             # 唯一活动实现
    └── history_old\                    # 不作为源码/构建/搜索输入
```

### 3.2 GitHub `main` 目标树

```text
SonoField-FPGA/
├── .gitattributes / .gitignore / .ignore
├── README.md
├── AGENTS.md
├── CHANGELOG.md                      # 当前工作日志入口，内容清晰
├── shared/
│   ├── PROJECT_STATE.json / .md
│   ├── VERSION_STATE.json
│   ├── CONTEXT_CHECKPOINT.md / .json
│   ├── CURRENT_PLAN.md
│   ├── DECISIONS.md
│   ├── BLOCKERS.md
│   ├── ACCEPTANCE.md
│   └── migration/                     # 迁移 SHA/清单/回滚证据
├── AI-problem/                         # 当前开放 P 文件与有效决策，来源保留
├── AI-chat-memory/                     # 仅真实可读取内容/恢复索引，BLOCKED 必须显式
├── AI-interaction-memory/              # 新活动交互索引及此后的正式记录
├── v5/
│   ├── README.md
│   ├── rtl/  tb/  tests/
│   ├── software/  firmware/
│   ├── config/  simulation/
│   ├── scripts/
│   ├── hardware/                      # AX7020 + NU40C10T + 3 PCB 候选
│   ├── docs/
│   ├── evidence/
│   └── ...                            # 其余已验证所需输入照原结构保留
└── history_old/                      # 迁移前旧仓库根的完整已跟踪内容快照
    ├── README.md / AGENTS.md / shared/
    ├── v1/ / v2/ / v5/               # v5 为迁移前快照，永不作为活动源码
    ├── PCB/ / BOM/ / archive/
    ├── AI-chat-memory/ / AI-interaction-memory/ / AI-problem/
    ├── evidence/ / parameter_detection/
    ├── .gitignore / .gitattributes / ...
    └── ARCHIVE_INDEX.md + FREEZE_MANIFEST.*
```

`history_old/` 应包含 **迁移固定 BASE_COMMIT 的所有 Git 已跟踪根文件（除根本不存在于 Git 树的 `.git/`）**，包括旧根的 v5 完整快照。新根的 v5 可通过从 BASE_COMMIT 原样恢复来复用 blob，无需重新上传第三方大文件；尽量让 Git 内部相同 blob 共享，**但新 clone 工作目录将实际有两份路径，注意磁盘容量**。

若远端出现 Git LFS、submodule、symlink、GitHub 大文件限制或不可获得的 LFS 对象，**先停下并给出替代存档方案与差异清单**，不得跳过文件后宣称“旧内容完整封存”。避免把本地未跟踪私有文件、token、密钥、设备身份、照片原始元数据、第三方未授权资料上传 public Repository。

### 3.3 默认历史排除

- 新根 `.ignore`（给 ripgrep/同类工具）：排除 `history_old/**`、临时构建、原始大日志；**不要把已跟踪 `history_old/` 放进 `.gitignore` 当成防修改措施**。
- `AGENTS.md` 写明：默认 `CURRENT_SCOPE = v5/ + shared/ + current AI-problem/ + root docs`；`history_old/`、早期 v1/v2/Robei/EBAZ 仅允许按“用户显式点名或审计恢复任务”读取。
- `run_baseline`、Vivado Tcl、test discovery、Python import、CI、EDA library、打包脚本，必须使用**允许列表 / 确定源清单**，禁止 `glob("**/*.sv")` 一类把 `history_old` 重复加载进来。
- 若 `history_old/` 中存在嵌套旧 `AGENTS.md`/配置，其内容只解释旧历史，不得作为当前 root 的决策/执行说明。

## 4. 分阶段执行及停止门禁

### Phase 0 — 只读 Reconciliation 和风险建账（不得改文件）

1. 在用户指定 Repo 核验 `origin`、`main`、remote HEAD、`git status`、`git ls-tree`；检查新旧路径存在性/是否重叠、文件系统容量与大小写兼容、LF/CRLF、LFS/submodules。
2. 在旧本地沙盒**只读**识别 local HEAD、branch、staged/unstaged/untracked/ignored；若存在尚未同步的用户数据，制作 **单独私有的 manifest 和备份建议**。禁止用一个干净的远端 checkout 冒充旧本地所有资料已归档。
3. 冻结 `BASE_COMMIT=<执行时实际 main SHA>`；记录远端 HEAD 与旧本地 HEAD 是否一致、现有 v5 验证证据及历史来源冲突；生成待迁移文件完整列表（路径、mode、Git blob SHA、size、SHA256，适当时内容 Hash）。统计文件数/体积/孤儿引用、破损符号链接、疑似密钥、大文件。
4. 若当前主分支比本文件更新，按最新工程事实修订计划；若发现他人并行写入，使用新基准且重复差异审核，不能在旧 HEAD 上直接覆盖新 main。
5. **Gate 0**：必须有可恢复 SHA、旧环境记录、数据保护说明、路径冲突结果、用户自定义源文件去向；否则 `REVISE` 并停止候选迁移。

产出：`PRE_MIGRATION_AUDIT.md/json`、`OLD_TRACKED_MANIFEST.json`、`LOCAL_UNTRACKED_PRIVATE_INVENTORY.json`（后者仅本地，不能公开设备序列/秘密）、`ROLLBACK_PLAN.md`。

### Phase 1 — 新沙盒独立冷启动（迁移前对照）

1. **在新候选目录执行独立 `git clone`**，确认 `origin` 完全等于现有 Repo，检出 `BASE_COMMIT` 并从该 Commit 创建 `chore/v5-ax7020-workspace-isolation` 候选分支。勿在旧沙盒上 `git mv`。
2. 新沙盒建立自己的 Python venv、依赖、输出目录；实际工具仍调用主机已安装 Python3.10、Icarus、Vivado2025.2、GCC，运行环境路径记录为机器事实而非板级事实。
3. 在干净 clone 执行当前已有 `v5/scripts/run_baseline.ps1`，数据输出到独立的新证据路径，不覆盖旧 summary；核对 Python/RTL/GUI/C/AXI/serializer/校准/安全/黄金等价测试，并保存真实 log 与 Hash。已有的 Vivado OOC 工程重建/重开应对照，但要清楚其 OOC 物理限制。
4. **Gate 1**：若未达到当前 BASE 的正式验证要求，不进入归档；先做 RCA 并保留失败 log。不能先搬迁再把原有失败归咎于目录结构。

### Phase 2 — GitHub 旧树封存 + 活动树抽取（仅候选分支）

1. 以 `BASE_COMMIT` 的 Git **已跟踪目录树**为唯一旧仓库快照来源，逐项移动到新分支的 `history_old/<原路径>`，保留旧对象、mode、Git blob SHA；这包括旧根的 `v5/`、`shared/`、`README`、`AGENTS`、BOM、PCB、evidence、archive 等。
2. 在仓库根从 `BASE_COMMIT` **重新建立当前 v5 完整源目录**，优先原样复制，所有 v5 继承文件先做 hash 对比；不要从旧本地未提交的散乱工作树无审查拷贝。
3. 从旧 `shared/` 提取**当前 v5 有效事实**形成精简新根 `shared/`，历史完整内容已经在 `history_old/shared/`，不要把旧 v2 阻塞叙述原封当成当前入口。
4. 新根生成 root README/AGENTS/当前 AI-problem/AI-interaction 索引、`.ignore`、适用的 `.gitignore`/`.gitattributes`、根 CHANGELOG 与 `shared/migration/`。当前打开的 P 问题保留 Problem ID、原内容 Hash 和 Repo 路径迁移映射；**历史的正式 Decision 一律保留原文，不允许改写成新批准**。
5. 以 `OLD_TRACKED_MANIFEST` 为机器核验依据，对每条 `<original-path>` 必须找到 `history_old/<original-path>`，比较 Git blob SHA/mode、按需逐字节 SHA；计数应一致，任何不一致必须明确列入 exception，而非自动忽略。保持旧 HEAD 可通过 `git show BASE:path` 单独还原。根本未被 Git 跟踪的 `.git/` 不属于要上传的目录。
6. 为 `history_old/` 生成只读索引，至少包含 BASE_COMMIT、归档时间、旧结构简述、个数/总字节数/树 Hash、路径映射、历史原件检查结果、访问规则、LICENSE/第三方限制与恢复方法。归档一旦冻结不得日常增改；增加 CI 检查阻止 PR 意外修改 `history_old` 的旧快照。
7. **Gate 2**：全量路径/Hash/mode 校验 PASS，新的 `v5/` 完整，未把任何 `local_raw` / 私密材料上传；否则停止。GitHub 的历史 commit 本身不要重写。

> 注意：本阶段是**创建独立候选分支并生成内容快照**，不是在旧本地执行不可恢复的物理剪切。只在单次可审查的 Git 迁移提交里调整跟踪路径；分开提交“旧树归档”和“新活动根清理”亦可，但两者必须共同通过后才能合并到 `main`。无需创建新 Repository。

### Phase 3 — 旧硬件噪声与事实入口整顿

实行“**按作用分类，不是按关键词粗暴删除**”：

- `ACTIVE_AX7020`：v5 生产 RTL、testbench、software、firmware、PS/PL contracts、AX7020 board facts、Vivado2025.2、NU40C10T 设计输入、当前 BOM/PCB、活动测试/当前证据 —— 在 `v5/`/`shared/` 中保留。
- `HISTORICAL_READ_ONLY`：Robei J2/J3/J4/J5/J6、N18/33MHz、旧 FTDI/COM4、旧板旧 XDC、旧 v2 时序/测试、EBAZ4205 双板和 White Rabbit 方案、TCT40 旧候选、历史 PCB/V1、曾被拒绝的候选、旧版本日志/归档 —— 完整在 `history_old/`，默认不访问、不参与构建。
- `PROVENANCE_REFERENCE`：v5 `inheritance_manifest`、测试修复原因、历史决策引用等可以**保留指向历史快照的静态字符串和 Hash**；但运行路径不得依赖历史文件。必须区分“历史引用”与“运行依赖”。
- `CONFLICT_NEEDS_REVIEW`：例如 v5 `hardware_parts.json` 仍含 TCT40，而新用户正式 TX 选择 NU40C10T；正式 ADC 仍是 AD7606B，C-16 是候选；旧 shared/BLOCKERS 以 v2 命名；旧 board rev/PS preset 与真实 AX701020.3.0 不匹配。这些不能靠批量替换文字来解决，需以 **源/用途/有效范围/决策状态** 四字段记录冲突，必要时创建 `AI-problem/problem`。

#### 当前硬件活动真值不可弄错

- 仅 ALINX AX7020 是新活动硬件主线；**已 JTAG 只读识别不等于已完成硬件功能验证**。
- 8×8 上阵列 + 8×8 下阵列，总 **128 TX / 8 RX**；TX **NU40C10T**、10mm 级别、12mm 辐射面中心间距，上下阵列辐射面 nominal 100mm、约 90–115mm 可调。
- 上下阵列各独立外部电源输入、各自电源保护和安全失能；AX7020 仅信号控制与数据处理，不向 128 TX 输送功率。
- 32 lanes × 每 lane 4 个使用的 595 输出、8bit requested/calibration 独立相位、全图 atomic commit、共同时基、motion queue、Host→PS→AXI→PL 现有接口、现有 safety/error 约束。
- 中央单颗 8ch 同步 ADC；正式 AD7606B 未被批准换型；NU40C10T 完整参数、RX 完整料号、电源/AFE/原理图仍未硬件放行。
- 原始历史数字与物理证据必须分开声明 `TESTED / SIMULATED / SYNTHESIZED_OOC / ROUTED / HARDWARE_READONLY / NOT_VERIFIED`。
- 未经硬件证据不得把旧板 N18、Robei 连接器、旧 COM/DDR 或老芯片速度等级导入 AX7020。

#### 强制审计活动 shared

新 `shared/BLOCKERS.md` 从当前 `PROJECT_STATE`/v5 evidence 构建，建立 v5 当前阻塞 ID、Evidence path、Owner/Next Action、OPEN/RESOLVED 状态、Last Verified 日期。历史 `shared/BLOCKERS_ENGINEERING.md` 如无当前必要性则只在 history_old 保留，或替换为一个简短的“历史定位指引”，**不要并列保留两个互相矛盾的 ACTIVE 阻塞表**。

检查每个活动文件：`PROJECT_STATE.*`、`VERSION_STATE`、`ENGINEERING_STATE`、`CONTEXT_CHECKPOINT.*`、`CURRENT_PLAN`、`DECISIONS`、`ACCEPTANCE`、`BLOCKERS`、`HANDOFF`、`MODEL_ENVIRONMENT`、`CHANGELOG`、`AGENTS`、`README`，包括 `workspace_path`、`current_stage`、`active_version`、source/hash/provenance、最新实板板号、BOM 路径、旧承诺与工具实际证据。旧事实只留“历史路径 + 日期 + 不适用于当前平台”的引用，不删除历史事实。

### Phase 4 — 路径依赖 / 可复现性 / 工程整洁

进行**真实静态审计 + 工具回归**：

1. 源码：SV/Verilog imports/includes、Python package/import、C include、register-map generator、fixture paths、version flags、board profiles、relative/absolute Windows paths、文件编码/大小写。
2. Vivado：`create_project.tcl`、XDC、IP 生成路径、PS presets、source fileset、sim fileset、bitstream/packaging scripts、`.xpr` 重新打开；证明无任何实际构建依赖 `history_old`，且无 Robei/EBAZ 物理约束加载。未证实板级 IO 不得用猜测 pin 让 bitstream 生成“PASS”。
3. 软件：Tk GUI、host protocol、PS C service、AXI/MMIO、UART transport profile、串口设备识别、校准 LUT、trajectory generator；无硬编码旧本地目录、旧 COM4 或旧 Rev 引脚。运行时找不到未验证 board facts 应 fail-closed，不得 silent fallback 到旧板数据。
4. 电子硬件：v5 BOM/NU40C10T、三个 PCB 当前提案、单中央 ADC、上下独立电源及硬件杀停，旧 `PCB/V1` 不得成为新生产工程的唯一实际来源；新增 v5 原生 EDA 工程前，保留 `NOT_CREATED / ERC_NOT_RUN / MANUFACTURING_HOLD`。
5. 工具/CI：Python3.10 的 venv、pytest/unittest、Icarus、Vivado/XSim 2025.2、GCC / 目标 ARM 工具链（如存在）、Windows PowerShell 7；扫描 GitHub Actions、`.vscode`、pre-commit、EDA 和构建路径。若 CI 暂不存在，可增加只读的结构/历史禁改/源列表核验，但**不可假装 CI 已在线 PASS**。
6. 搜索污染：检查 `rg` 默认命中旧文件比例，写 `.ignore` 后证明默认只命中当前 `v5`/shared；历史仅显式 `--no-ignore` + `history_old/` 可以检索。测试目录发现器必须排除 `history_old`。
7. 未来作品打包：定义 `DELIVERY_MANIFEST.md` 与可重复的 `package_submission` 候选边界（源码、必要脚本、版本说明、BOM、原理图、真实证据、LICENSE、文档），默认**不包含** `history_old/`、私有原始资料、构建缓存、未批准 PCB、旧板文件；当前阶段无需制造最终作品包或虚构硬件验收。

修复规则：优先更新小范围路径解析、allowlist、文档/metadata，不得为了整洁大范围改写 RTL/协议/时序。所有 `move/rename` 后独立检查 import、test、build、CI、Vivado/EDA 路径；任何 change 必须有受影响模块和验证证据。

### Phase 5 — 迁移后强制验证矩阵

| Gate | 必须验证的内容 | 验收 |
|---|---|---|
| MIG-01 Git事实 | 相同 Repo、`v5 ACTIVE`、新工作目录、已冻结 BASE SHA；远端仍允许溯源旧提交 | PASS |
| MIG-02 历史完整 | 旧 Git 树每一条受审计路径在 `history_old/` 找到；file mode、blob Hash 一致；例外显式 | PASS，无静默丢失 |
| MIG-03 私有数据 | 旧物理沙盒及 untracked 用户资料仍在原位；public 新 commit 无 secrets/private raw | PASS |
| MIG-04 源隔离 | 当前 RTL/Python/FW/Tcl/fixtures/board configs 只从新 v5 加载；历史搜索默认排除 | PASS |
| MIG-05 结构 | 新工作区没有旧开发板活动 XDC/串口/PS 配置；入口和状态只有 v5 当前真值 | PASS |
| MIG-06 Python/GUI | **至少维持原 115/115 Python 测试、3696 帧 ×4 回归**，依 BASE 最新 Acceptance 调整为不低于最新真实指标 | PASS |
| MIG-07 独立仿真 | Icarus 3 次 + XSim 1 次相同固定输入、Seed、canon Hash；与 BASE 行为等价 | PASS |
| MIG-08 C/RTL/AXI | 协议、C service、UART 边界 mock、AXI/MMIO、校准、队列、安全/原子提交/serializer 全部既有回归 | PASS |
| MIG-09 Vivado2025.2 | 用新工作区 Tcl 生成/打开 OOC 工程、重建综合并输出真实源清单；所有运行源来自 `v5/` | PASS（OOC 不代表实板） |
| MIG-10 可移植性 | **第二个干净临时克隆**只含新 Git 活动树（`history_old` 可物理存在但不被加载），重新安装或独立验证依赖，完成全部可用离线回归 | PASS 或限定依赖差异 |
| MIG-11 工程交付 | README/AGENTS/当前 Checkpoint/BLOCKERS/BOM/PCB/权限/隐私/打包清单一致，链接与 paths 无失效 | PASS |
| MIG-12 实板边界 | 原有 SD/运行镜像未动；未执行新的 bitstream、未知 GPIO/DDR 操作；无新增虚假功能声明 | PASS |

注：Git commit metadata、绝对路径、时间戳、报告头会合理变化；对于声明 bit-exact / deterministic 的功能，只对**规范化的有效输入与 canonical trace/hash**逐项比较；任何有实质数据差异必须 RCA，不得简单忽略或改黄金文件。

证据要求最低 **A+B**：A=新沙盒真实本地工具基线；B=第二独立 clone 或隔离环境复验；C=静态审阅/独立 Reviewer 作为额外证据。不能将同一日志复制两份冒充独立验证。

### Phase 6 — PR、人工审查、合并与封存

1. 把“归档路径迁移”和“新活动状态/构建修复”整理为可审查的候选 Git commits；push 到 `chore/v5-ax7020-workspace-isolation`（push 前再次审阅 secret scan），优先开 Draft PR 到 `main`。
2. 输出：`BASE_COMMIT`、`CANDIDATE_HEAD`、PR URL、完整差异统计、旧树与 archive file/blob 数量、ACTIVE 文件列表、失败/通过回归、主要风险、回滚方法。**不要在最终审查前自动合并**。
3. 将候选整体作为 **USER_APPROVAL_REQUIRED_FOR_MAIN_MERGE** 等待用户明确批准；这并不构成版本升级申请，始终是 v5 结构迁移。若用户已明确对候选提交及审查结果批准合并，才允许普通非强制 merge；远端 HEAD 发生变化时重新对齐、重跑关键 Gate。
4. 合并后从远端 `main` **重新 clone 到独立临时目录**，核验远端 commit、目录树、current state、冷启动测试、历史冻结清单。旧本地目录仍不得自动 pull。仅在远端结果确认成功后将新沙盒设为正式 `workspace_path`（需与用户认可的路径一致）。
5. 更新最新 `shared/CONTEXT_CHECKPOINT.*`、`PROJECT_STATE`、`CURRENT_PLAN`、`ACCEPTANCE`、`BLOCKERS`、`CHANGELOG`，记录 PR/merge SHA、完成时间、可复现运行指令；核对 GitHub 远端实际内容。确保 `history_old` 后续没有被修改（可增加只读校验 CI）。

### Phase 7 — 失败处理与回滚

- 候选失败：保留旧本地原状、保留迁移分支及失败日志，不合并、不升级。Codex 可以在**候选分支**修复路径/环境小缺陷并重测，若 2–3 次无法闭环则 RCA/停机并汇报。
- 合并后发现严重回归：提交新的 **revert commit** 恢复此前树，或将活动目录按归档 manifest 逐项恢复；**禁止 force push/重写旧提交**。迁移前 BASE tag/commit 应可直接访问。使用恢复 commit 须由用户批准其影响范围。
- 发现历史对象丢失或备份缺项：停止归档“成功”声明，并报告缺失具体 Git path / Blob SHA / 本地未跟踪文件；根据真实证据修复。
- 若不能创建新沙盒或文件容量不足：不要转而在原沙盒直接移动文件；先给出空间预算和安全替代方案供用户决定。

## 5. 最终交付文件（名称可按现有规范协调，职责不得缺失）

在**新候选沙盒**中准备并更新到活动树：

- `shared/migration/PRE_MIGRATION_AUDIT.md` 与清单 JSON（含 BASE_COMMIT、原目录哈希、tracked/untracked 边界）。
- `shared/migration/ARCHIVE_COVERAGE.json`（每个原 Git path -> `history_old/...` 的模式/Blob SHA/验证结果）。
- `history_old/ARCHIVE_INDEX.md`、`history_old/FREEZE_MANIFEST.json`（封存时生成，随后严格只读）。
- `shared/migration/ACTIVE_TREE_ALLOWLIST.json` 和搜寻/加载隔离报告。
- `shared/migration/PORTABILITY_AND_REGRESSION.md`（原/新/clean clone 测试矩阵和日志 Hash）。
- `shared/migration/ROLLBACK_PLAN.md`、`shared/migration/DELIVERY_MANIFEST.md`。
- 新根 `README.md`、`AGENTS.md`、`shared/PROJECT_STATE.*`、`VERSION_STATE.json`、`CONTEXT_CHECKPOINT.*`、`CURRENT_PLAN.md`、`BLOCKERS.md`、`DECISIONS.md`、`ACCEPTANCE.md` 和必要的当前 AI-problem 索引。
- 如有必要，更新 `v5/scripts/*` 的路径 allowlist/封存保护审计脚本、GitHub CI 配置，但保持功能源码稳定；日志分类到 `v5/evidence/migration/<date>/`。
- Git 提交 SHA、Draft PR / reviewed PR、用户批准来源、最终 main SHA、远端实际核对回执。

如果外部 ChatGPT 历史读取仍受阻，保留 `CHAT_MEMORY_ACCESS_BLOCKED`，仅依据本次明确消息和真实仓库内容工作；不得宣称已经读取不存在的完整历史。历史的 AI-problem/decision 要连同其 Problem Hash 与 Version 保存，任何旧问题决策不自动变成 AX7020 新版本决策。

## 6. Done When / 最终判定

必须同时满足：

1. 旧本地沙盒与原有未跟踪/私有资料 **0 不明丢失**，旧仓库 Git 历史完整且可通过原 SHA 恢复。
2. `history_old/` 的旧 root 跟踪树 **文件/mode/blob SHA 覆盖完整**；默认检索/测试/构建绝不读取 history_old。
3. 新工作空间经真实 clean clone、重新建环境后，在 **不需要旧沙盒** 的条件下运行所有既有 v5 核心回归。
4. 当前唯一工程 `v5/` 仅按 AX7020 平台组织；BOM/NU40C10T/独立供电的事实、候选与阻塞不混淆；不存在多个互相矛盾的当前状态入口。
5. Python/GUI、Icarus、XSim、C/AXI/安全、Vivado OOC 的要求全部满足；无测试降级、mock 冒充硬件、旧板约束误加载。
6. root 文件结构简洁、证据位置明确、当前 `shared` 一致，后续可制作无需旧板文件的交付包。
7. 所有变更经候选分支 Review、用户批准后合入 `main`，远端 HEAD 和最终 fresh clone 均验证，Checkpoint 真实可恢复。

**独立最终评价只使用：** `ACCEPT / ACCEPT WITH LIMITATIONS / REVISE`。如果只完成候选分支准备且未获合并批准，结论必须明确为 `ACCEPT WITH LIMITATIONS — CANDIDATE ONLY` 或 `REVISE`，不得称 GitHub main 已迁移。

达到所有关键门禁后 **STOP_OPTIMIZATION_AND_DELIVER**；不要继续低收益代码重写或旧资料美化。物理板级/PCB/声学尚未通过的事项只作为明确限制造成的未完成范围，不能拖成无限迁移优化，也不得伪造整机 ACCEPT。

## 7. Codex 回报格式（严格）

```text
PROJECT_ID:
Repository / Branch / BASE_COMMIT / Candidate SHA / Remote HEAD:
Current Version: v5 (unchanged)
Old Local Workspace / New Local Workspace:
Migration Stage:
User Approval for main merge: NOT_REQUESTED / PENDING / APPROVED (source)
History Coverage: files / bytes / blob-mode mismatches / exceptions
Untracked and Private Asset Protection:
Active AX7020-only Build and Search Isolation:
Shared State Reconciliation:
Current PCB/BOM Boundary: NU40C10T / independent UP/DN power / ADC formal vs candidate
Tests: BASE / MIGRATED / CLEAN_CLONE with actual logs and canonical hashes
Vivado 2025.2: OOC / Place-Route / Board Hardware (separate truthful statuses)
Conflicts & BLOCKERS:
Unexpected Changes / Risk:
Changed Files and Git Commit URLs:
Rollback Point and Procedure:
Conclusion: ACCEPT / ACCEPT WITH LIMITATIONS / REVISE
Next Minimal Action:
```

---

## 8. 本次指令来源（可直接点击核对）

- Repo: https://github.com/loverlike1216/SonoField-FPGA
- 活动状态: https://github.com/loverlike1216/SonoField-FPGA/blob/main/shared/PROJECT_STATE.json
- 版本门禁: https://github.com/loverlike1216/SonoField-FPGA/blob/main/shared/VERSION_STATE.json
- 最新 Checkpoint: https://github.com/loverlike1216/SonoField-FPGA/blob/main/shared/CONTEXT_CHECKPOINT.md
- 最新计划: https://github.com/loverlike1216/SonoField-FPGA/blob/main/shared/CURRENT_PLAN.md
- 实板只读检测: https://github.com/loverlike1216/SonoField-FPGA/blob/main/v5/evidence/board_bringup/20261009/RESULT.md
- v5 完整数字基线: https://github.com/loverlike1216/SonoField-FPGA/blob/main/v5/evidence/BASELINE_VALIDATION.md
- BOM 工作副本: https://github.com/loverlike1216/SonoField-FPGA/tree/main/v5/hardware/bom/working/2026-10-09
- 当前三板设计准备: https://github.com/loverlike1216/SonoField-FPGA/blob/main/v5/hardware/integration_candidates/20261009/SCHEMATIC_PREPARATION.md
- 当前活动 AGENTS: https://github.com/loverlike1216/SonoField-FPGA/blob/main/AGENTS.md

**请从 Phase 0 开始。首先输出真实 Repository/工作区 Reconciliation 与候选新路径冲突结果；只有 Gate 0 通过才能继续迁移。所有过程以实际工具结果为准。**
