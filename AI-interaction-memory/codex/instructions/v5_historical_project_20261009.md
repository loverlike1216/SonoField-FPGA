# SonoField-FPGA v5 — GitHub 历史板卡资料隔离与 `Historical project/` 迁移指令

> **执行者**：Codex（建议 GPT-6.1 Sol / Extra High）  
> **指令性质**：已指定 Repository 内的 **v5 同版本结构整理 / Git 路径迁移 / 质量门禁**；不是 v6 开发，不是软件架构重构，也不是删除历史。  
> **用户目标**：让 GitHub 访客第一眼看到以 **ALINX AX7020** 为核心的 SonoField-FPGA v5；将无关的 **Robei 八角板**、**EBAZ4205** 及它们专属的旧工程、状态、日志、约束、原理图等集中放入仓库根目录名称完全一致的 **`Historical project/`**。本次迁移操作允许读取待迁移的历史文件；迁移结束后，**未经用户明确授权**，日常开发、默认检索及构建均不得读取该目录。  
> **正式仓库**：`https://github.com/loverlike1216/SonoField-FPGA.git`  
> **当前版本**：`v5`（已获用户批准；保持不变）  
> **开发工具**：Windows PowerShell 7 (`pwsh`)；Vivado 2025.2；当前 v5 既有 Python、Icarus、XSim、C/AXI 检验工具。  
> **迁移授权范围**：允许在**独立迁移分支**整理、创建、审查、修复必要的文件路径、提交迁移候选和创建 PR；**禁止未经用户审查直接合并 main**。禁止 Git 历史改写或 force push。

---

## 0. 核心约束（先读）

1. **唯一活动版本仍为 `v5`**，不得创建 v6，也不得将旧 v1/v2/v3 误标成最新阶段。Repo 不变，默认分支仍为 main。
2. 仓库根目录应出现**精确名字** `Historical project/`（大写 H、小写 project、中间空格），不是 `history_old`、`Historical_project`、`Historical Project`。所有命令及路径必须正确处理空格、中文和 Windows 大小写不敏感特性。
3. 必须区分：**专属于旧板的内容**（归档）、**v5 当前运行所需内容**（保留）、**复用的板无关核心**（保留）、**混合历史/当前内容**（拆分、留当前摘要及可追溯历史）、**来源不明内容**（阻塞/待审）。禁止单凭文件名出现 `Zynq` / `7020` / `FPGA` / `TCT40` 就机械移走；AX7020 本身也是 Zynq-7020。
4. 迁移应以 `git mv` / 审核过的同效 Git 树更改为主，尽量保持历史字节不变。迁移文件需验证 **源路径、目标路径、Git blob SHA、模式、字节数、必要时 SHA256**；不可“先删除后凭记忆重建”。移动本身不要求修改旧报告正文及其版本号。
5. 旧本地沙盒、未知未跟踪文件、`.git/`、Vivado 本地工程/缓存、外部厂商未获再分发授权的资料全部保留原状；**不要把本地私有物件直接推送公开仓库**。当前 Repository 为 public，提交前必须做秘密、账号、序列号、许可和版权审查。
6. 不得通过降低测试阈值、禁用回归、替换黄金结果、mock/placeholder、忽略失败警告或虚构测试记录使迁移“通过”。本任务不变更声场核心算法、协议、RTL 行为、ADC 正式料号或运行镜像。
7. **本次是整理，不是硬件部署授权**：AX7020 Rev3 仍需匹配 PS/DDR/VCCO/引脚等；禁止改变 SD/Flash/Boot、驱动、复位、未知 GPIO，不下载 bitstream，不接入未验收驱动板、不改 PCB 制造文件。
8. 不能保证 GitHub 网站全文搜索永远不索引历史（目录仍在同一仓库）；要求可执行地保证 **Codex 默认搜索、脚本依赖和 v5 构建排除历史目录**，并用 README/AGENTS/忽略配置与自动审计验证。
9. `Historical project/` 不是垃圾箱：原始源码、决策、失败日志、原理图、许可证和来源需可追溯；禁止粗暴删除旧记录或把既有版本升级授权消除。
10. 若 `main` 在开始后更新，必须重新读取差异并重新验证；不允许基于过时 HEAD 直接覆盖别人更新。

---

## 1. 已知仓库事实（仅作为本次任务的预检索线索，执行时必须刷新）

2026-10-09 ChatGPT 通过 GitHub 读取到：

- Repository `loverlike1216/SonoField-FPGA`，默认分支 `main`，public。
- 检索时 HEAD 为 `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`；约 3,907 个已跟踪文件、约 97.6 MB 文件内容，根目录有 `v1/`、`v2/`、`v5/`、`PCB/`、`BOM/`、`parameter_detection/`、`archive/`、`evidence/`、`shared/`、`AI-chat-memory/`、`AI-interaction-memory/`、`AI-problem/` 等。
- `shared/PROJECT_STATE.json`、`shared/VERSION_STATE.json` 以 **v5/AX7020** 为当前事实；`shared/BLOCKERS.md` 与 `shared/ACCEPTANCE.md` 文件开头却仍以 **v2** 为标题和主体，属于**活动状态入口冲突**，本次必须处置。
- 最新 AX7020 实板只读结果 `v5/evidence/board_bringup/20261009/RESULT.md`：PCB `AX701020.3.0` / Rev3，XC7Z020 JTAG ID `0x23727093`、CLG400 照片、现有 PL DONE、双 Cortex-A9 Running/SD 启动；完整物理料号/速度温度等级复核、DDR 实测、VCCO、UART/AXI 真机闭环仍未完成。不能把已上电/已编程误称为 SonoField 已部署。
- `v5/evidence/BASELINE_VALIDATION.md` 和最新数字回归记录：既有 **115 项 Python 测试 PASS、3 次 Icarus + 1 次 XSim、每组 3,696 帧一致**；文档器件 OOC 综合不等于 Rev3 整板布局布线通过。迁移后须真实重跑并对比。
- 当前硬件方向：128 TX / 8 RX、NU40C10T（真实批次/规格待确认）、AX7020、两块独立外部供电阵列 PCB、中央采样/控制 PCB、温度补偿、8-bit 相位、32 lanes × 每 lane 4 used、原子相位提交、PS/PL/UART、校准与运动上位机。新 BOM 工作副本及设计候选均在 `v5/hardware/`；**正式 ADC 仍为 AD7606B；AD7606C-16 只是待批准候选**。
- 如有与上文不同的实际 `main`/工作区事实，以**用户当前指令 + 批准决策 + 最新真实仓库代码/配置/工具证据**修正，并在报告中列差异。尤其不要把旧 Robei -1 实现结果套用到 AX7020 -2/I。

**先读指定文件，不执行通篇历史全文扫描：**

`README.md`、`AGENTS.md`、`shared/PROJECT_STATE.json`、`shared/VERSION_STATE.json`、`shared/CONTEXT_CHECKPOINT.*`、`shared/CURRENT_PLAN.md`、`shared/DECISIONS.md`、`shared/BLOCKERS.md`、`shared/BLOCKERS_ENGINEERING.md`、`shared/ACCEPTANCE.md`、`v5/README.md`、`v5/evidence/BASELINE_VALIDATION.md`、`v5/evidence/board_bringup/20261009/RESULT.md`、`v5/hardware/bom/working/2026-10-09/README.md`、当前 `AI-problem/` 中 v5 未决问题、以及已存在的旧沙盒迁移交接文档（若确实存在且可读取）。

如果上述文件路径已变化，用仓库实际路径；文档缺失必须写 `MISSING` 而非臆造内容。

---

## 2. 目标 GitHub 结构（示意，不要求所有文件一律挪走）

```text
SonoField-FPGA/
├── README.md                      # 对外展示：唯一当前版本 v5 / AX7020
├── AGENTS.md                      # Codex 当前开发范围与历史默认禁读规则
├── .gitignore / .gitattributes     # 实际当前路径维护
├── .ignore / .rgignore             # 搜索默认排除 Historical project（视工具支持）
├── v5/                            # 唯一活动实现：完整、自包含、可运行
│   ├── rtl/ software/ firmware/ tb/ tests/
│   ├── config/ hardware/ scripts/ simulation/ evidence/ docs/
│   └── ...
├── shared/                        # 只保留当前 v5 状态、正式有效决策、验收、恢复入口
├── AI-problem/                    # 保留当前未决问题 / 经过确认仍适用的决策入口
├── AI-interaction-memory/          # 当前 v5 所必需的索引 / 交互来源
├── AI-chat-memory/                 # 当前来源记录与访问状态，不伪造历史
├── docs/ 或 references/            # 可选：确需根目录共享的板无关规范、许可证、导航
└── Historical project/
    ├── README.md                  # 历史目录索引、冻结政策、对应原路径、来源
    ├── MIGRATION_MANIFEST.csv
    ├── MIGRATION_AUDIT.md
    ├── archived-boards/
    │   ├── Robei-Zynq7020/
    │   └── EBAZ4205/
    ├── legacy-versions/           # v1/v2及证据完整性审查后移动
    ├── legacy-pcb/                # 旧 Robei/EBAZ 原理图、PCB/V1等
    ├── legacy-bom/                # 仅不再作为当前v5采购依据的旧BOM
    ├── legacy-evidence/           # 旧 FPGA/旧板旧版本仿真/布局布线等
    ├── legacy-decisions/          # 旧阶段原始决策/Problem（需保持来源/Hash）
    └── legacy-archives/          # 如确有旧 archive 数据，允许继续嵌套索引
```

目录子分类可根据真实文件调整，但**顶层名称 `Historical project/` 不得更改**。根目录的 `v5/`、根级有效治理文件和必要共享资料不得因为“清爽”被整体移动。`Historical project/` 下不允许出现自己的 `.git/`，不能形成 Git submodule 或第二个 Repository。

---

## 3. 文件分流规则与优先级

逐路径形成清单（CSV/JSON）：`old_path | new_path | type | classification | reason | dependencies | sha256 | git_blob | decision_source | validation`。

**分类与动作：**

| Class | 触发条件 | 目标动作 |
|---|---|---|
| `ACTIVE_V5_KEEP` | v5 正在加载的 RTL、软件、固件、仿真、GUI、协议、BOM、工具、脚本、配置、测试、数据 | 留在 `v5/`；必要时修复真实依赖，禁止缩减功能 |
| `ACTIVE_GOVERNANCE_KEEP` | 当前主 README、AGENTS、PROJECT_STATE、VERSION_STATE、CURRENT_PLAN、v5 BLOCKERS/ACCEPTANCE、当前有效问题/决策 | 根目录保留并整理为 v5 唯一权威入口 |
| `GENERIC_REUSABLE_KEEP` | 与开发板无关且 v5 实际用到的文献、数学模型、文档、许可证、工具 | 保留在外部合适公共目录，或经过哈希追踪复制到 v5 |
| `BOARD_LEGACY_MOVE` | 只服务 Robei 八角板 / EBAZ4205 的引脚、XDC、约束、PL 时钟、PS preset、UART、GPIO、DDR、BSP、Bitstream、实验图、板卡说明、采购和专有 EDA 项目 | `git mv` 到 `Historical project/archived-boards/` 或对应历史类别 |
| `LEGACY_VERSION_MOVE` | v1/v2 或暂停旧方案的自包含历史版本及其工具证据，与 v5 运行无动态依赖 | 移到 `Historical project/legacy-versions/`，保留内部相对结构、哈希及来源 |
| `MIXED_SPLIT_REVIEW` | 一份文件既有旧板叙述又包含当前 v5 的有效决策/复用设计 | 当前入口**保留有效部分或新建清晰 v5 摘要**；原文完整、未经篡改地归档；修复路径和证据 |
| `UNKNOWN_HOLD` | 无来源、物理参数未确认、依赖复杂或可能涉及不可再分发文件 | 暂不移动，记录到 BLOCKERS，待审查后处理 |

**默认候选（必须逐项检查，不能无条件批量搬走）：**

- `v1/`、`v2/`：原则上属于冻结历史；移动前做全文件清单、依赖、对照基线和自动测试检查，若 `v5` 存在运行时引用，须先将必需且许可允许的副本移入 `v5/` 并验证独立性。
- `PCB/V1/`：过去八角板/旧版原理图与 EasyEDA 证据候选；不能把它当成 AX7020 新版原理图。对当前 v5 必要的器件思想/图纸来源只保留经核对的摘要和引用。
- `BOM/`：旧原始采购表/说明候选；**v5 当前的 NU40C10T BOM 在 `v5/hardware/bom/`，不得被移动或覆盖**。
- `parameter_detection/`、根 `evidence/`、`archive/`：区分旧板专属/一般可复用/当前版本状态后分类。严禁整目录移动导致 v5 的链接或工具路径损坏。
- `shared/`：整体必须保留在外层；只把确认为历史专属的旧资料归档，并处理 stale 状态冲突。当前最新的 `shared/BLOCKERS.md`、`shared/ACCEPTANCE.md` 需特别审查。
- `AI-problem/`、`AI-interaction-memory/`、`AI-chat-memory/`：当前 v5 open problems、批准来源、Model/Stage 授权、检查点索引必须保留；可归档旧版本记录，保留精确 ID/Hash/目标路径，不得改变批准事实。
- `v5/` 内的 `not_inherited`、`Robei`、`EBAZ4205` 等**历史排除说明或迁移来源元数据**不能机械删除，这些可能是重要的负向安全约束和溯源信息；但 v5 的**实际构建/运行**不得加载旧板文件。
- 同一文件同时服务旧板与 v5 时优先**留当前有效文件并在历史索引添加来源引用**，不要为满足“全移走”而割裂运行链路。

**不能移动的东西**：当前 v5 源、历史迁移后的真实 CURRENT_STATE 依赖、活动版本批准证明、有效阻塞及验收口径、许可证必留声明、真实 Vivado 2025.2 证据、当前 NU40C10T BOM 和 AX7020 Board Layer、安全/温度/校准接口合同。

---

## 4. Gate 0 — 冻结快照、审计 Git、建立恢复锚点（只读）

1. 在原/新工作区分别查明 `pwd`、`git remote -v`、`git branch --show-current`、`git rev-parse HEAD`、`git status --porcelain=v1 -z`、`git ls-files -z`、`git submodule status`、`git lfs ls-files`（若已安装/使用）、活动工作区真实路径，避免把不同沙盒混成一个。
2. 检查 tracked / untracked / ignored 文件；分别记录字节数、数量、绝对路径与敏感性。**不执行 `git clean`、`git reset --hard`、未经审批的 stash、强制删除、移动用户私有文件**。若原工作区有用户更改，单独干净克隆执行迁移，原地只读。
3. 记录 `main` 头、源树 SHA 和 Git refs；建议创建只新增的保护 tag 或固定 SHA 恢复清单（是否推送恢复 tag 先获批准）；核对是否有未推送本地提交。
4. 运行迁移前完整数字基线，单独目录保存原始日志/summary/hash。默认通过 `v5/scripts/run_baseline.ps1`，按 `v5/README.md` 真实用法传参；不能复用上次 PASS 当这次 PASS。
5. 若缺 Python/Tk/Icarus/XSim/Vivado 2025.2/GCC/授权工具，记录 `MISSING_ENV` 并阻止“完整验收”；不得改掉测试才继续。
6. 写出 `migration_preflight.json`、`tracked_manifest_before.csv`、`protected_refs.json`、`baseline_before/`，每条记录源 HEAD 和工具版本。

**Gate 0 完成条件**：可复现的固定源 HEAD + 完整追踪清单 + 用户未跟踪资产安全 + 测试前基线。若有不安全/无法识别仓库状态，停止。

---

## 5. Gate 1 — 审计依赖与编制迁移目录清单（只读）

1. 从 **当前 `v5` 的实际编译/运行源入口**推导依赖闭包，不要只使用 grep 名称：检查 `create_project.tcl`、XDC/EDIF/IP、`run_baseline.ps1`、Python import/relative data、C 头文件、JSON/YAML fixture、GUI assets、requirements、CI、子脚本、JLCEDA/EasyEDA 项目引用、工作目录和外部工具路径。
2. 用 `git ls-files` + `rg`/Python 逐项扫描候选旧板资料、旧提交状态及所有活动引用，记录正反向引用。**本次用户指令明确授权专项迁移审计中的定向历史读取**；未来继续开发时未获用户再次明确授权则禁止读取。
3. 对每个移动候选标明 Class、原因、旧路径、新路径、Git blob/sha256、是否有活动引用。特别区分 AX7020 与 Robei 都含 `Zynq-7020`，不按型号字符串粗筛。
4. 形成 `MOVE_PLAN.csv`、`KEEP_PLAN.csv`、`SPLIT_PLAN.csv`、`UNRESOLVED.md`、`V5_DEPENDENCY_GRAPH.md`；给出新增文件/引用改动的最小化方案。
5. 确认是否已有 `Historical project/`、`history_old/` 或其他同名近似目录；如果存在冲突，停止并说明，不能覆盖或叠套重复归档。

**Gate 1 完成条件**：所有已跟踪文件被唯一归类，不存在无解释的删除/遗失；任何未知高风险文件为 HOLD，不强制迁移。

---

## 6. Gate 2 — 创建真实历史目录，在独立分支执行可追溯迁移

1. 从最新一致的 `main` HEAD 创建**独立分支**，建议 `chore/v5-historical-project-isolation-20261009`；有重名分支则核实后另命名，不覆盖旧分支。
2. 在分支创建 `Historical project/README.md` 和审计索引，说明只读历史、原目录映射、旧板适用范围、冻结原因、默认不检索、恢复方式、历史文件不会参与 AX7020 构建。
3. 按已审查 `MOVE_PLAN.csv` 使用 `git mv -- "<old>" "Historical project/<class>/<new>"`，保留二进制文件精确字节。Windows `pwsh` 所有含空格路径用引号，严禁根据文本模糊匹配直接执行批量删除。
4. 混合文件遵循“一份真实原始历史 + 一份经审查当前有效摘要”的原则；**不编辑已冻结的历史正文**。对 `shared/BLOCKERS.md`、`shared/BLOCKERS_ENGINEERING.md`、`shared/ACCEPTANCE.md` 的 v2 旧版本，先把原文完整归档，再在 root `shared/` 制作 **v5 当前事实**记录，标清日期、证据、OPEN/RESOLVED、历史路径。不要重置 v5 未决 Problem/Status。
5. 保留 `shared/DECISIONS.md` 已获用户批准的有效决定及来源。旧决策可以归档原始全文，但当前 `shared/DECISIONS` 应有明确 v5 适用清单、正式批准的 provenance，并标明不自动继承旧 Robei 配置。
6. 修复所有受影响的**活动**链接和逻辑路径：README、AGENTS、状态 JSON、索引、脚本、配置、CI、构建清单、证据定位、相对/绝对路径、许可引用。允许生成迁移 redirect/index，但不能修改旧算法、寄存器、协议和测试标准。
7. 当前 v5 测试引用若涉及旧历史 fixture，需复制真正必要的 fixture 到 `v5/` 并记来源 SHA/许可，调整活动相对路径；不允许将活动脚本改为自动进入 `Historical project/`。
8. 针对源数据输出 `MIGRATION_MANIFEST.csv`、`MIGRATION_REPORT.md`、`MIGRATION_CONFLICTS.md`、目录级 `README`，包含文件级哈希与 rename/copy/delete 说明。

**Gate 2 完成条件**：旧板内容已按清单迁移但可追溯；当前活动代码/状态文件仍在外层；无无法解释的 tracked file 丢失。

---

## 7. Gate 3 — 将“默认不读历史”变成实际工程规则

1. 在根 `AGENTS.md` 明文规定：**迁移完成后，除非用户明确授权读取历史目录，否则 Codex 不打开、不全文搜索、不扫描 `Historical project/`**。即使遇到回归或怀疑根因在旧代码中，也须先报告拟读取的历史文件及理由，获得用户授权后方可定向查看，并记录原因。
2. 根 `README.md`：清晰的当前项目简介、AX7020 主板、Vivado 2025.2、v5 快速启动、用户交互与声场/硬件范围、最新证据与限制；最后只给一个 `Historical project/README.md` 历史链接，避免首页被旧版铺满。
3. 在 `v5/README.md`、`shared/CURRENT_PLAN.md` 中指明当前可运行入口。将旧主板资料移走后更新所有 root 导航，确保外部访客一眼看到 v5 的核心功能和状态。
4. 可增加根 `.ignore` / `.rgignore` 等当前工具认可的忽略规则，写入 `Historical project/`。**这些文件不能保证所有 GitHub 网站搜索/第三方索引都忽略历史**，因此不要承诺它们控制 GitHub 平台全文索引。
5. 审计默认 `git grep` / `rg` / 脚本 / CI：以明确允许路径列表（例如 `v5/ shared/ AGENTS.md README.md`）代替“从根目录递归读取所有文件”；对历史访问可通过显式 `--no-ignore`/路径授权实现。
6. 加入防回归检查：正常 build/test/synth 的加载源列表中 `Historical project/`、`Robei` 旧约束、`EBAZ4205` 板级文件数量必须为 0；但注释、历史来源和 negative-exclusion 描述可以存在，不能用粗暴文本零匹配作为合格标准。

**Gate 3 完成条件**：默认开发路径清晰；不会误把旧 GPIO/XDC/PS preset 或旧版 DDR/UART 设置当 AX7020 事实。

---

## 8. Gate 4 — 迁移前后全量验证（不能用迁移自述代替证据）

### A. 内容与路径完整性

- 完整 tracked before/after 清单，除新索引/当前必要更改外，旧文件 blob SHA、mode、字节大小完全一致；异常逐项解释。禁止未列入 MOVE_PLAN 的删除。
- 根 `v5/` 的源、仿真输入、正式测试资产保留；`v5` 里需修复的运行路径/版本元数据有明确差异清单和 Review。非必要核心 RTL/算法零差异。
- `Historical project/` 不含 `.git/`、明文密钥、个人私有信息、许可证不允许公开的未审资料。
- 任何文档导航链接/证据路径/目录索引可解析；检查 GitHub 大小写路径与 Windows 空格路径，防止 breakages。

### B. 数字功能与确定性

- 新独立干净工作区重新安装锁定依赖，依照 v5 官方入口运行完整基线；Python **至少达到原基线 115/115**，实际如已新增则以当前基线总数为准；不得有 skipped 的核心测试。
- 三次 Icarus + 一次 Vivado XSim 的 **每次 3,696 帧**及固定 seed/canonical hashes，逐个与迁移前**同输入/同工具合同**对比；若 hash 差异必须分析来源，不能简单更新 golden。
- 测试包含波形/相位/calibration/ADC 数字链、C 服务、PS/PL 仿真、AXI、队列、atomic commit、serializer、安全故障处理、GUI/运动轨迹；实际以当前 suite 为准，报告任何遗漏。
- 检查 UI 可启动、用户生成轨迹的流程及使用的 JSON/fixture，不因文件清理变成 mock/dummy 演示。

### C. Vivado 2025.2 与工程独立性

- 以当前 `v5/scripts/create_project.tcl` 和 `v5/config/ax7020_ooc.tcl` 实际构建/重开 Vivado 工程并执行 native OOC synthesis；记录实际器件、source membership、Cell utilization、时钟报告、未约束 IO 警告。迁移前后同条件结果做对照。
- 任何存在的现行板级 XDC/PS/DDR/UART/时钟脚本，核对它是否经 AX7020 Rev3 来源证实；未核验的不自动发布为生产约束。
- 搜索并验证 v5 全部当前工具路径、包含文件、Tcl source、C include、Python sys.path、打包/CI；禁止历史目录成为暗中运行依赖。
- 如果当前仓库尚无**真实**整板 P&R/PS UART/实板运行证据，只报告 `NOT_RUN / BLOCKED`，不因 OOC PASS 写成目标板完全可运行。

### D. 独立环境证据（推荐 A+B）

- A：现有本机完整真实基线。
- B：独立克隆目录、只包含当前允许的根治理/v5 当前运行内容以及锁定环境；没有旧历史文件也能跑数字基线。建议按已有 `standalone` 运行资产采用同等验证；如本轮不能新建依赖环境，只能标 `SAME_INSTALLED_DEPENDENCIES` 而不是另一机器复现。
- 所有生成日志、summary、工具版本、Source SHA、输出 hash 和失败记录都归档，不能覆盖原日志或悄悄丢弃失败。

**Gate 4 完成条件**：全部当前可跑的核心测试通过，行为/哈希可对照，Vivado 文件集不含历史资料，核心功能无回归；无法完成时 `REVISE`，不进入 main。

---

## 9. Gate 5 — 核对当前硬件/PCB/BOM 与历史的界线

历史隔离后，外层必须仍能找到并正确识别：

- **ALINX AX7020** 板卡 Rev3 当前事实/未核验事实：芯片 CLG400、用户声明 -2/I 与工具只读发现的范围明确区分；生产 XDC、Bank VCCO、PS DDR preset 和 UART 尚需物理/厂商证据。
- 128 × **NU40C10T** TX、8 RX（最终接收器具体 MPN 待验证）、上/下各 8×8、12 mm pitch、100 mm 名义间距（90–115 mm 可调）、两阵列分别独立外置供电，AX7020 不供 TX 功率。
- 中央 PCB / AX7020 与 AD7606B 正式采样链；AD7606C-16 仍是建议/待审批替代，不得在目录迁移期间顺手替换。
- 温度与环境补偿需求：上/下/中央温度、声速修正和自校准相位模型；如尚属规划/候选，正确标注而不是伪称全部已完成。
- 32 lanes × 4 used、8 bit requested/calibration、atomic map、UART/PS/PL、上位机动态轨迹功能和全局安全默认关闭等数字不变量。
- 新 BOM 工作副本、原始提交 BOM、供应商 datasheet 来源与原生原理图实际状态；旧 PCB/V1 的 ERC 通过**不能**视为 AX7020 PCB ERC PASS。

这一步是确保“历史整理没有抹掉未来 PCB 落地输入”，不是本任务授权额外开发新的 PCB 功能。若发现核心设计问题，记录给后续独立 Stage/AI-problem，避免迁移工作范围无限扩大。

---

## 10. Gate 6 — Git 审核、分支交付与人工门禁

1. 迁移仅在新分支上完成。`git status`/`git diff --stat`/`git diff --summary`/源目标 SHA 清单必须与计划一致，尤其检查每个二进制原件未被重新导出改变。
2. 审查 `.gitattributes` 对原生 epro2/eprj2、PDF、SVG 等文件的 binary 属性；审查 `.gitignore`、新 `.ignore/.rgignore` 在移动后不会错误隐藏应跟踪内容。
3. 严格扫描秘密、内网地址、设备序列号、个人文件和第三方未授权资料；对不适合 public GitHub 的内容仅保留来源索引和本地保存声明，不要暗中上传。
4. 使用**少量、逻辑清晰的常规提交**（移动、修路径、文档门禁、验证证据分开），允许 push **迁移分支**，创建 Draft PR，列出 `main` 与目标 HEAD、文件数/体积、v5 完整性、功能回归、Vivado 结果、审核未决、回滚方法。
5. **停止并等待用户人工批准合并 `main`**；用户已批准实施迁移，尚不等于批准在无证据下直接发布大规模目录变更。绝不 force push、reset/rewite 既有提交或删除 Git 历史。
6. 如执行过程中 `main` 更新，重新 base/diff 与回归，不能把原有远端更新覆盖掉。

**Gate 6 完成条件**：具备完整可审查 PR + 真实证据 + 无未解释修改；未获用户合并批准则状态为 `READY_FOR_USER_REVIEW`，不是已迁移到 main。

---

## 11. Gate 7 — 用户批准合并后的只读核对（授权后执行）

- 用户批准后通过正常 PR 合并路径将候选带入 `main`，保留 Git history，不 squash 失去审计可读性（如合并策略有要求需用户确认）。
- 切回独立干净克隆，读远端 `main` HEAD、树、根目录、`Historical project/`、`README`、`AGENTS`、`shared/`、`v5/`；核对 CI/构建入口以及历史默认排除规则。
- 再次执行至少 smoke / hash / 文件依赖审计；如有完整回归条件，建议完整重跑。报告远端 commit 和测试日志。
- 更新 `shared/PROJECT_STATE`、`VERSION_STATE`、`CURRENT_PLAN`、`CONTEXT_CHECKPOINT`、`BLOCKERS`、`ACCEPTANCE` 及状态索引，标清**当前 v5 / 历史归档完成 / 原有硬件阻塞仍未关闭**。不要用目录迁移的 `ACCEPT` 自动替代整机 `REVISE`。
- 原本本地旧沙盒保留只读/冻结，不执行跨目录剪切、清空缓存或覆盖本地未跟踪资料；以后日常工作只使用用户已指定的 AX7020 工作区。

---

## 12. 最终交付和 Quality Gate

必须产出：

1. `Historical project/README.md`（来源说明、旧版/旧板索引及冻结/默认禁读声明）。
2. `Historical project/MIGRATION_MANIFEST.csv`（逐文件 old→new / class / Git blob / SHA256 / size / reason）。
3. `Historical project/MIGRATION_AUDIT.md`（迁移总览、按版本/板卡/文件类型计数、历史溯源、许可证/敏感信息处置）。
4. 根 `README.md` 与 `AGENTS.md` 的 AX7020-v5 可导航版；`shared/` 当前有效状态、BLOCKERS、ACCEPTANCE 冲突整理与当前 Checkpoint。
5. `v5/evidence/repository_cleanup/<date>/`（前后清单、测试 summary、Icarus/XSim traces/hashes、Vivado 综合与源列表、运行路径依赖审计、Git PR 信息、失败与限制；路径可按当前证据规范调整）。
6. `ROLLBACK_PLAN.md`（不通过历史改写回滚；通过取消/关闭未合并分支、或合并后 `git revert` 正常恢复；原始 commit SHA 可直接检出）。
7. `V5_ACTIVE_DEPENDENCY_REPORT.md`（证明日常运行/构建不依赖 `Historical project/`；不可“grep 0次”代替真实源列表和运行证据）。
8. 最终单条报告：`PROJECT_ID / Repository / old HEAD / migration branch / new HEAD / Version v5 / preserved & moved count / digital tests / Vivado / CI / unresolved blockers / PR URL / risk / user approval requested / decision = ACCEPT|ACCEPT WITH LIMITATIONS|REVISE`。

**验收判据**：

- `Blocking migration defects = 0`、关键功能回归 0、任何源文件丢失 0、重要 binary/hash 未解释变化 0、`v5` 运行依赖指向历史目录数量 0、历史资料索引可恢复、根 README 可迅速导航到 v5。
- 迁移专项若全部通过，可以给 **`ACCEPT WITH LIMITATIONS`**（硬件尚未实测的原有限制保留）；若发现关键迁移回归则 **`REVISE`**。
- **禁止**因为迁移整理达到高分而宣布真实 AX7020 UART、PS→PL、ADC、声场、悬浮、最终 PCB 已经通过；它们仍以真实工具和硬件证据为准。

## 13. Codex 启动与停止条件

收到本指令后：先读取 Gate 0 的有限有效文件，确认真实沙盒、仓库和当前 v5 状态；能独立安全执行的审计、计划、分支文件迁移、验证、候选提交由 Codex 完成。**不必每个小目录调整都问用户**；但凡遇到无法判定的旧/新混合资料、需要破坏当前核心、重要数据不可恢复、额外付费工具、历史/发布大范围不可逆操作、或待合并 `main` 时，必须停止请用户确认。

遇到测试回归，最多按项目规则做 2–3 轮有证据的局部修复；无新证据时停止并上报根因，不无限循环。**绝不通过改变验收标准来证明迁移成功**。

> 终点：同一个 GitHub Repository 中，AX7020 v5 是唯一清晰的活动工程，旧 Robei/EBAZ4205 工程集中于 `Historical project/`，历史可追溯且默认不读取，v5 的当前软件/数字实现仍可复现，硬件未通过的部分如实标记。等待用户批准 PR 合并后再发布到 `main`。
