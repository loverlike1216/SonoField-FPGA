# SonoField-FPGA — AX7020 v5

唯一活动工程版本。用户于2026-10-08明确批准使用已有v5目录；没有创建v4。复制来源和逐文件Hash见config/inheritance_manifest.json；旧本地沙盒原样保存；旧Git根树在history_old封存，仅显式历史调查可读取。历史来源模型记录：GPT-6.1 Sol High（当时用户声明）；本次运行模型身份未独立确认。

继承128通道/8bit相位、独立校准、原子提交、确定性共同时基、采集/校准调度、运动轨迹、PS协议/C服务/AXI桥和安全控制。算法、接口、寄存器、测试阈值不因目录整理改变。10mm换能器、12mm辐射面中心间距、100mm上下辐射面间距（90–115mm可调）、双8×8与中心原点保持不变。

2026-10-09历史板级/集成结果：[实板只读检测与BOM](evidence/board_bringup/20261009/RESULT.md)、[迁移前历史数字回归](evidence/baseline/board_integration_20261009/summary.json)、[BOM工作副本](hardware/bom/working/2026-10-09/README.md)、[三板原理图准备](hardware/integration_candidates/20261009/SCHEMATIC_PREPARATION.md)。确认实板AX701020.3.0、XC7Z020 JTAG、CLG400照片；DDR控制器32bit配置已读到，但容量/稳定性未知。现有SD/PL/PS程序保持原样；UART/DDR内存/PS-PL实测未运行。

原数字基线与OOC结果见[evidence/BASELINE_VALIDATION.md](evidence/BASELINE_VALIDATION.md)。制造商资料描述XC7Z020-2CLG400I、PL50MHz U18、PS33.333MHz E7、1GiB DDR；完整器件等级、Rev3匹配PS配置、VCCO仍待核验。132MHz是继承的内部设计目标，不是板载晶振。内部OOC时序报告不能作为整板时序验收。

## 从任意克隆路径运行

在仓库根目录使用PowerShell7，Python3.10及Tk。本次验证工具为Vivado2025.2、Icarus Verilog、GCC。机器安装路径需要自行设置，不要复制机器专属路径为板卡事实。

```powershell
pwsh
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r v5/requirements-lock.txt
$env:VIVADO_BIN='D:/Vivado/2025.2/2025.2/Vivado/bin' # 改为本机安装目录
$env:IVERILOG_BIN='C:/iverilog/bin'                  # 改为本机安装目录
$env:CC='D:/DevC++/Dev-Cpp/TDM-GCC-64/bin/gcc.exe'   # 改为本机C编译器
./v5/scripts/run_baseline.ps1 -Output evidence/migration/manual_run
```

输出目录必须没有已有summary.json，避免覆盖证据。成功标准：总summary PASS、115项Python测试、3696帧、3次Icarus和1次XSim固定输入Hash一致，以及协议/C/AXI、安全、黄金等价回归全部通过。测试有GUI自动化，需要可用的桌面/Tk，不能以无GUI跳过核心回归。

只验证Python：进入v5，运行`../.venv/Scripts/python.exe -m unittest discover -s tests -v`。完整基线采用上面的入口，不要将单项通过当成完整通过。

离线Vivado综合（从v5目录运行）：

```powershell
& "$env:VIVADO_BIN/vivado.bat" -mode batch -source scripts/create_project.tcl -tclargs config/ax7020_ooc.tcl evidence/migration/manual_ooc build/manual_ooc
```

输出build/manual_ooc/sonofield_v5.xpr和synthesized.dcp；当前源码加载清单和报告位于evidence/migration/manual_ooc；两个目录必须尚不存在。工程只包含v5自身RTL；hardware/constraints/core_ooc.xdc只约束内部时钟。没有生产XDC、板级引脚分配、PS preset或可下载bitstream。Vivado参数缺失/版本不符时应失败，不能换用旧板约束。

运动界面：从v5目录运行`../.venv/Scripts/python.exe -m software.ui.app`，默认读取simulation/fixtures/calibration_reference.json。该文件是原始SYNTHETIC校准输入，保留其历史metadata；禁止当作AX7020或真实换能器测量。新校准输出使用v5 metadata。

## 目录职责与下一步

rtl/software/firmware/tb/tests为当前源；config为配置及继承清单；simulation为显式测试输入；scripts为自包含工具；hardware/ax7020为官方来源与待核验事实；hardware/bom为未冻结的继承BOM；hardware/pcb只保留边界说明，无生产发布；build是可再生成本地工程；evidence是实际运行证据。依赖环境可位于仓库根.venv，也可用入口-Python传入绝对解释器路径。

下一步依据已确认的Rev3.0，获得厂家匹配PS/DDR/时钟/IO参考、完整器件等级与VCCO，说明当前运行镜像和可用内存范围；接板上UART口并资格确认ARM BSP/工具链，再做无外部负载的临时PS-PL测试。独立审核ADC/本地安全/浪涌候选，保持制造HOLD。不得下载OOC工程或驱动未知GPIO；本次只进行实板只读检测，没有程序下载、PCB修改或声学实测。

默认只检索v5/shared/当前有效决策；历史仅在回归或用户要求时查看。全工程验收仍未完成。

当前候选迁移结果与完整冷启动命令见仓库shared/migration/RUNBOOK.md及PORTABILITY_AND_REGRESSION.md；旧证据保留原日期，不作为本轮复跑结果。
