# SonoField-FPGA · v2

低成本 **10 mm 超声发射器、上下各 8×8 的 128 路 FPGA 驻波悬浮平台**。
本轮交付可运行的 Python 声场模型、SystemVerilog 相位核心、自动验证及硬件启动规程。
尚未上板、未完成目标器件综合、未制造驱动板、未进行实物悬浮。50 mg 是逐级验证后的目标。

| 项目 | 值 |
|---|---|
| PROJECT_ID | SONOFIELD_FPGA |
| Repository | https://github.com/loverlike1216/SonoField-FPGA |
| Workspace | E:\Codex-project\AMD-SonoField-FPGA |
| Branch / version | main / v2 |
| Stage | SELF_CALIBRATION_SOFTWARE_AND_DIGITAL_SYSTEM |
| Board / EDA | Robei Zynq-7020 / AMD Vivado 2025.2 |

当前几何由用户明确指定：辐射面中心点距 **12 mm**，上下辐射面间距默认 **100 mm**、
可调 **90–115 mm**；全局原点为两个阵列辐射面中心组成空间的几何中心。
默认上/下面 z=±50 mm，x/y 各为 −42、−30、−18、−6、6、18、30、42 mm。
中心跨度 84×84 mm，名义壳体外包络 94×94 mm，相邻壳体间隙 2 mm。**这些不是 PCB 间距或外形尺寸。**
详见 [机械坐标定义](hardware/mechanical/radiating_surface_geometry.md) 和
[128 路坐标表](hardware/mechanical/geometry_10mm/coordinates_nominal.csv)。

板卡资料按用户指定以 `../Zynq7020/constrain` 为准：时钟记录为 N18 / 33 MHz。
完整 FPGA 料号、I/O Bank 电压及 `.const` 内部少数引脚编号仍不完整，见
[板卡审计](docs/hardware/board_facts.md) 和 [阻塞项](../shared/BLOCKERS.md)。没有编造 XDC。

## 安装与运行

进入本项目 `v2` 目录后使用 PowerShell，Python 3.10；已安装 Icarus 和 Vivado 的路径可通过参数覆盖。

```powershell
python -m venv ..\.venv
..\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
..\.venv\Scripts\python.exe -m software.acoustic_model.visualize_field --output build/model_review
..\.venv\Scripts\python.exe -m software.acoustic_model.phase_lut_generator --output build/phase_map.csv
..\.venv\Scripts\python.exe -m software.acoustic_model.export_geometry --output build/geometry_review
..\.venv\Scripts\python.exe scripts/validate.py --output build/verification_review
```

成功标准：44 项 Python 测试通过；Icarus 多通道配置通过；XSim 通过；三次 128 路轨迹与
独立 Python 参考、另一模拟器一致；最终 JSON `status=PASS`。不要只根据退出码或波形图片判断。
`--skip-xsim` 只产生 PARTIAL，不能当完整验证通过。

从零手动复现、环境路径、预期输出、综合门禁及故障处理见 [操作指南](docs/OPERATING_GUIDE.md)。

## 已实现

- 共同 40 kHz 时间基准、8 位相位、独立请求与校准、逐通道使能。
- 全图写入检查、影子/活动寄存器组、周期边界原子提交、明确错误应答。
- 32 lane × 4 有效位序列输出候选、安全复位/硬件禁用/溢出保护。
- 2/8/16/32/72/128 阵元、平面/浅凹几何、方向性声场、固定种子误差扫描、参考相位图。
- 继承的 TCT40 测量模板；v2 正式 BOM 与后续校准路线见 hardware/bom/BOM_LOCK.md、docs/architecture/V2_REQUIREMENTS.md。

## 文件布局

| 目录 | 内容 |
|---|---|
| rtl/、tb/ | 数字核心、集成顶层及自检 testbench |
| software/acoustic_model/、tests/ | 声场/颗粒模型和解析检查 |
| scripts/、config/ | 自动验证、板卡审计、工程脚本、明确配置 |
| constraints/ | 上板约束的阻塞说明；当前无 XDC |
| docs/ | 架构、硬件接口、理论边界、实验及操作指南 |
| hardware/ | 测量模板和原型 BOM；没有最终 PCB 生产文件 |
| evidence/ | 小体积原始日志、摘要、CSV、图及审计证据 |
| ../shared/ | 计划、决策、验收、状态、交接与报告 |
| ../Zynq7020/ | 用户原始板卡资料，只保留本机，不自动再发布 |
| build/、../build/、../.venv/ | 可再生成的本地输出/环境，Git 忽略 |

## 结果与限制

最新结果以 [交接](../shared/HANDOFF.md)、[验收矩阵](../shared/ACCEPTANCE.md)、[当前报告](../shared/report_v2.md) 指向的证据为准。
声压是任意单位，几何与材料是假设；没有绝对力、实际工作体积或 50 mg 悬浮保证。
132 MHz 是序列器集成仿真配置，并未验证板上倍频和布线。PS/AXI 传输、硬件时钟丢失保护、
驱动电路与实际器件校准仍属后续集成任务。

## 当前软件/数字阶段

v1 保持冻结，继承的全部源码和测试仍在 v2。新增 AD7606B 四线采集、模式/扫描/缓冲/主机命令，
以及原始采样到几何、谐振、相位、数据库与独立请求/校准 LUT 的软件处理链。
当前完整验证入口是 scripts/validate.py；最新证据位于 evidence/self_calibration_stage/validation。
物理测量、板级时序、PS/AXI 适配和 PCB 制造未完成。
详见 [自校准架构](docs/architecture/SELF_CALIBRATION.md)、[软硬件接口](docs/hardware/PCB_SOFTWARE_INTERFACE.md)。
