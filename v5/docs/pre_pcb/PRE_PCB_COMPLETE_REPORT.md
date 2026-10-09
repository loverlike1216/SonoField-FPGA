# SonoField-FPGA v5：PCB 落地前全系统候选交付报告

日期：2026-10-09。项目：SONOFIELD_FPGA；正式 Repository 仍为
https://github.com/loverlike1216/SonoField-FPGA.git 。版本保持 **v5 ACTIVE**，没有建立下一版本。

**候选离线阶段结论：ACCEPT WITH LIMITATIONS，供用户及独立 Reviewer 审核。**
**全平台/真实声学结论：REVISE；PCB、电气、采购及制造：NOT_RELEASED。**
可离线执行的最终门禁均通过，已知离线 Blocking=0、已知离线 Critical Bug=0。
仍有13项环境、电气、物理、资料及审核门禁；这不等于整机 Blocking=0。
独立克隆、第二仿真器和真实 Vivado 提供交叉证据，未伪造独立人工/ChatGPT Review。

## 1. 身份、边界与来源

工作沙盒为 `E:\Codex_project\AMD_Sonofield`，分支
`feat/v5-prepcb-full-system`，继承迁移候选提交
`d7f7b60ae8ed9ed8bdee34c8738ce68aacd81743`。最终运行源码提交为
`a43728870a06949e67b0604f4716f07419b3306c`。报告与证据提交在此之后，实际发布 SHA
由 `PUBLICATION_RECEIPT.json` 记录，避免把文档内的自身提交写成循环引用。

本次 Repository Reconciliation 确认远端 main 为
`ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`；迁移 PR #1 仍 OPEN/DRAFT/UNMERGED。
本开发候选建立在该迁移分支上，不能绕过其人工合并门禁。此次没有 force push、main 合并、
历史重写或板卡操作。旧物理沙盒保持完整；当前任务未读取封存历史正文，冻结检查仅使用 Git 元数据。

完整执行文件已保存至项目 AI-interaction-memory；两张 PCB 草图原样保留并记录 SHA256。
草图只确立功能区和连接意图，不提供真实管脚、电源能力、器件额定值或8×8 TX 的替代几何。
[来源与 Hash](SOURCES.json)、[执行合同](EXECUTION_CONTRACT.md)、
[初始对账](../../evidence/pre_pcb_20261009/REPOSITORY_RECONCILIATION.md) 均保留。ChatGPT 历史访问 BLOCKED，当前可观察
Codex 消息/工具记录 PARTIAL；没有推断旧聊天或私有内部推理。

## 2. S0–S7 交付及证据等级

| Stage | 实际完成 | 等级与限制 |
|---|---|---|
| S0 FACTS | 同仓库/沙盒/分支对账；完整指令、草图、来源；112项受保护文件初始 Hash | 实际文件/Git 证据；Rev3完整硬件身份仍待核验 |
| S1 HARDWARE CONTRACT | 三板接口、上下独立12V候选供电、中央仅AX7020受保护单源供电；67/68 GPIO预算；新工作BOM | 文档与候选配置；功率、电流、封装和真实互锁未实测 |
| S2 OFFLINE PS/PL | PS7 GP0、六个外设地址窗口、BRAM、控制/状态、五中断、三个IIC、132MHz时钟/复位；真实xpr/logicalXSA；PL综合和布局布线 | BUILT / SYNTHESIZED；DDR关闭，外部时序/板级实现/ARM目标部署受阻 |
| S3 TEMP/ADC | 三TMP117读取/校验模型、SHT45 CRC、温度积分、128相位映射、ADC特征/原始块协议和错误拒绝 | TESTED / ALTERNATIVE_VALIDATION；无实物温度或RAW_ADC采集 |
| S4 CALIBRATION | 双向16+16对角TX/对侧4RX，128有向路径；6DoF+6RX延迟、两个gauge、观测性/置信度、坏数据拒绝 |10次合成拟合与留出验证；128TX逐路响应仍UNMEASURED，未宣称FULL_CHANNEL |
| S5 PC UI | 用户运行时XYZ点/拖动/Bezier控制柄、闭合/撤销/重做/顺序编辑、JSON+Hash保存重载、速度/加速度/jerk校验、C任务与RTL回放 | 五组自动运行时GUI回调测试；真实人工操作验收、串口和粒子位置未测 |
| S6 INTEGRATION | 原数字全回归；新安全/邮箱/协议/温度/GUI测试；实际新顶层BRAM→原核心闭环；独立clone+venv | TESTED / SIMULATED；失电/断线/时钟停止的物理截止仍需实测 |
| S7 HANDOFF | 最终证据索引、风险/回滚、状态/检查点、正常开发分支发布、Draft审核包 | 候选交付；用户合并/独立Review待进行 |

功能覆盖按上述边界逐项列出；原115项测试保留且全部执行，新增56项合计171项通过。
未测代码覆盖率，也不以一个任意百分比表示整机或真实悬浮完成度。

## 3. 数字、算法、GUI与可复现结果

最终机器可读事实入口：
[FINAL_VERIFICATION.json](../../evidence/pre_pcb_20261009/FINAL_VERIFICATION.json)。

| 门禁 | 实际结果 | 主要证据 |
|---|---|---|
| 原始保护 |112项初始受保护文件复核PASS；仅两份C适配器及继承manifest获准改变，原RTL/测试/golden/阈值不变 | FINAL_PROTECTED_FILES.json |
| 单元测试 |原115+新增56=171；干净环境最终171/171 PASS | clean_reproduction/all171_final.log |
| 原完整数字基线 |主沙盒与独立克隆均PASS；各3696帧×3 Icarus+1 XSim，canonical JSON/ACK Hash相同 | inherited_full1/summary.json；clean_reproduction/full1/summary.json |
| 新安全/邮箱 |Icarus+XSim PASS，包括默认OFF、长按/释放、故障锁存、STOP立即禁止、手动重新使能 | clean_reproduction/rtl_verified/summary.json |
| 新顶层闭环 |37帧经过真实新顶层BRAM/安全/原核心；两工具ACK SHA256均为84db46a42298ea8f89938a7a23dd7dd60a5eabd44b375d10471f583c84abac8f | clean_reproduction/top_verified/summary.json |
| 温度相位 |160完整map、20480 channel words；Python独立积分与C解析积分bit-exact，随机calibration字节保持独立 | clean_reproduction/system_verified/summary.json |
| 稀疏几何 |5 seeds×均匀/梯度温度=10 fits，每次5初值；每次384未扫描TX留出路径；秩12、SVD/condition/covariance保存；重跑pose Hash相同 | clean_reproduction/system_verified/sparse/ |
| 稀疏误差 |最大单分量平移误差0.002275191mm；最大角度分量0.003091530°；留出最大10.236394ns；3个异常路径剔除 | 同上；均为SYNTHETIC_REFERENCE |
| 动态GUI全链 |5组运行时输入分别37/40/113/111/74帧，总375；JSON重载Hash、模型陷阱/运动限制、实际C帧协议/50Hz tick、双RTL ACK全部通过 | clean_reproduction/system_verified/gui/case_1..5 |
| 源码/路径 |177份受跟踪活动源码在两个沙盒规范化字节相同；原始/规范化Hash均保留，实际加载路径位于各自clone的v5 | CLEAN_SOURCE_COMPARISON.json；platform_verified/loaded_sources.txt |

主沙盒 inherited_full1 的单元子门禁为166项，当时新增5项传输测试尚在补齐；随后完整171项通过。
独立克隆完整基线已包含171项，最终源码又执行171项、新安全/新顶层/GUI/平台门禁。
完整3696帧基线运行于 `263f06f943e343f56639fb0f08d1bb07aeef3c64`；其后仅新增wrapper/监督器/
测试整合及平台元数据修正，原核心、原115项测试及黄金数据未变，并由保护Hash核实。

独立环境为 `.portability/prepcb_clean`，采用 `git clone --no-hardlinks` 及新建锁定venv。
Python3.10.11/Tk8.6，锁定12个包，GCC9.2、Icarus、Vivado/XSim2025.2。
两个克隆共享本机OS、EDA安装和license；它不是第二台实板或另一台电脑。复现按分阶段命令真实执行，
[REPRODUCTION.md](REPRODUCTION.md) 提供统一runner及独立平台构建命令。

## 4. Vivado/Vitis真实结果与边界

最终平台源为2025.2，候选legal part `xc7z020clg400-2`，不是实际工业级身份的证明。
PS地址全部为64KiB窗口：core 0x40000000、BRAM 0x42000000、GPIO 0x41200000、
IIC center/up/down 0x41600000/0x41610000/0x41620000。每项offset/range/唯一映射及中断数5均有脚本断言。
最后平台日志无CRITICAL WARNING或ERROR。生成xpr和无bitstream的logicalXSA；未生成可下载板级bitstream。

| PL OOC 132MHz | 数值 |
|---|---:|
| WNS / TNS |+0.081ns / 0ns |
| WHS / THS |+0.096ns / 0ns |
| WPWS |+3.288ns |
| Slice LUT / FF |7463 / 20185 |
| Block RAM Tile |4 |
| OOC BUFGCTRL / MMCM |0 / 0，时钟由OOC外部逻辑端口提供 |
| no_clock / 内部未约束endpoint |0 / 0 |
| 缺外部input/output delay |161 / 148 |

实际资源只覆盖PL OOC顶层，不代表完整PS7平台/封装/板卡资源结果。
默认DRC报告22个Warning：20条继承RAMB36异步控制检查、1条该规则的报告上限、1条OOC需要PS7警告。
报告在20条处截断，不能解释为总共仅20个风险。重新打开真实DCP复查保留；没有waive、降级或关闭规则。
单内部时钟无内部CDC路径；无约束外部端口被CDC排除，不能作为跨板CDC/SI资格证据。
**TIMING_HOLD_MISSING_BOARD_FACTS / BOARD_TIMING_HOLD**：缺真实线缆/器件min/max delay、VCCO、完整Rev3事实，
因此没有填造输入输出延时。生产XDC未启用，候选XDC故意拒绝直接用于生产。

Vitis实际报告2025.2 build6295257；Python API环境可运行。真实目标预检得到
`PS_TARGET_BUILD_BLOCKED`，无审定目标BSP/XSA、ARM gcc不在PATH，UART路线UNVERIFIED_AX7020。
启动器即使返回OS exit0仍包含Python traceback；按阻塞处理。已产生的logicalXSA不是已审定可启动平台。
主机GCC编译/调用真实C服务和特征代码的结果仅为host验证，尚无Cortex-A9目标固件成功构建或实际UART/IIC/IRQ适配证据。

可重建工程实际位置：
`E:\Codex_project\AMD_Sonofield\.portability\prepcb_clean\v5\build\platform_verified\platform.xpr`。
运行路径及logicalXSA/BD再建/报告复制在最终证据下；大型中间目录与DCP按生成物留在本地build，Git提交可复建源码/脚本/报告。

## 5. 硬件、算法与运行限制

三板正式接口仍为128TX/8RX、32lanes×4、独立requested/calibration 8bit、公共时基和完整128路原子发布。
TX NU40C10T、正式ADC AD7606BBSTZ-RL不变，C-16未获替换批准，RX确切MPN仍HOLD。
中央不新增外部12V入口或猜测转换能力；J10/J11每rail只选一路受保护来源。
上下阵列分别独立12V5A候选源；60W只是标称容量，不是测得负载。已有约2AeFuse不能视为5A通路已合格。

三TMP117均参与温度→c(z)→沿声线传播积分→phase map；地址/开漏/三IIC分段见合同。
SHT45湿度只记录，humidity_applied=false；压力是假设。板上温度不代表测得三维空气温场。
Python温度平滑候选辅助和C超阈值HOLD均已实现，但尚无在线物理热控制资格。
真实独立NC急停、硬件watchdog、热点比较器、掉电/短路/上电顺序/时钟停转截止均需电气及实板验证。

稀疏校准只得到几何与RX延迟的有界数值拟合，RX0/RX4为明确固定gauge。
载波周期解模糊必须依赖独立粗TOF不确定度；C包络起点估计不能自行证明这个界。
原始采集适配器拒绝缺少测得前端延迟/质量证明的RAW_ADC；此次无真实采集。
128路TX幅相/增益均保留UNMEASURED，实际悬浮范围和粒子位置null/NOT_MEASURED。

GUI具备自由编辑能力，当前可运行模式为显式SIMULATION/HOST_FIXTURE，不开放未资格化的物理驱动。
可选串口枚举不打开设备，不固定COM号。轨迹在PC生成/上传任务，C服务按逻辑20ms推进，载波和队列由本地PS/PL架构承担；
Windows GUI不充当40kHz调度器。115200 8N1理想16384B传输至少1.422s，另加帧头/CRC/重传。
规划器最多12000点而C任务容量协商512帧；超长任务明确拒绝上传。
模型只检查局部归一化辐射势趋势/曲率与邻域限制，尚无全工作区副陷阱穷举、声压标定、50mg承载或悬浮实测。

## 6. BOM、文档与失败证据

新工作版 `hardware/bom/working/2026-10-09/prepcb/BOM_AX7020_NU40C10T_PREPCB_WORKING.xlsx`
按Review/Upper/Lower/Central/External分表，线束列入External。两阵列各64颗NU40C10T，中央正式AD7606B、
三TMP117、推荐SHT45与独立电源/保护候选明确。未知电流/额定/封装资料保留空值/HOLD。
数量和采购余量公式重算并做敏感度检查，五表及详细列渲染逐项检查；原三份BOM字节不变。
未完成原生CAD/PCB布局/铺铜/Gerber，Native ERC NOT_RUN；不可据此下单。

关键文件：

- [候选管脚CSV](../../hardware/prepcb/AX7020_REV3_PINMAP.csv)、[Pin provenance](PIN_PROVENANCE.md)、[候选XDC](../../hardware/constraints/ax7020_candidate.xdc)。
- [三板/电源/保护/地/线束合同](CENTRAL_ARRAY_HARDWARE_CONTRACT.md)、[温度验证](TEMP_COMPENSATION_VALIDATION.md)、[稀疏校准验证](SPARSE_CALIBRATION_VALIDATION.md)。
- [GUI操作与启动指南](GUI_USER_DRAWN_TRAJECTORY_GUIDE.md)、[复现命令](REPRODUCTION.md)、[JSON schemas](schemas/user_path.schema.json)。
- [失败及修正](FAILURES_AND_CORRECTIONS.md)、[未闭环门禁](PRE_PCB_OPEN_BLOCKERS.md)。

早期失败日志全部保留；top1的ERROR+PASS标记、自动PS地址分配失败、负WNS版本均不计成功。
被其他窗口遮挡的初次GUI屏幕抓图因含无关桌面内容而删除，不发布；后续只用自有窗口PrintWindow捕获，最终图已目视检查。
这一隐私删除不改变测试判定。最终成功目录与旧失败/中间结果由EVIDENCE_QUALIFICATION.json明确区分。

## 7. 风险与Rollback

| 风险 | 影响与当前处理 | 下一阶段关闭方式 |
|---|---|---|
| Rev3/供电/引脚/线束不匹配 |禁止部署；中央电源预算HOLD，候选引脚NON_DEPLOYABLE |原厂匹配资料和安全的独立核验 |
| ADC/AFE/TOF周期/阵列相位误差 |数值参考不能替代实际自校准或trap |真实RAW_ADC、独立TOF界、前端和逐TX测量 |
| inherited BRAM异步控制与外部时序 |仿真PASS不关闭硬件DRC/SI/CDC风险 |有授权的后续修复/完整板级STA和故障实验 |
| ARM目标缺失、物理串口未测 |无法称PS板端功能已运行 |匹配2025.2目标工具/BSP/OCM/startup与真实适配 |
| PR堆叠依赖未合并 |main仍旧状态；开发候选不等于正式迁移生效 |先独立审核PR1，再审核本开发候选，按依赖顺序正常合并 |

合并前回滚：保留当前分支及全部证据，切回未改动的迁移候选分支/提交d7f7b60即可；
生成物可放在独立clone，不覆盖旧沙盒。无需删除历史或重置远端。
若用户之后批准并完成合并，回滚使用正常revert提交并再次跑门禁，不force push、不rewrite、不删证据。
当前没有配置或驱动实板，故没有需要执行的硬件恢复动作；以后任何带电实验必须先关闭驱动并遵守独立安全流程。

## 8. 审核与下一步

现阶段可减少的离线阻塞已闭环，执行STOP_OPTIMIZATION_AND_DELIVER。
PC-B01..PC-B13和两个原OPEN Problem继续保留；禁止生成虚构ChatGPT Decision。
用户/Reviewer审核具体Draft PR、FINAL_VERIFICATION、风险与原始日志后，再决定正式合并及后续硬件实验。
发布回执记录真实远端SHA、PR/CI和main不变的检查；CI只验证结构与保护门禁，不声称云端Vivado或板卡测试。

本报告结论不会自动解锁PCB制造、采购、板卡写入或物理悬浮声称。
