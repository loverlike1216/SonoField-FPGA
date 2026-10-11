# 验证矩阵与复算

本轮是文档/离线计算交付。数字基线 PASS 与 PCB 电气 REVISE 是不同结论。

| 模块 | 引用/计算 | 模型/仿真 | 实测 | Native/ERC/DRC | Review |
|---|---|---|---|---|---|
|公开项目|固定commit/文件/hash，实际BOM/Gerber/原生文本/PDF|未执行第三方代码|第三方报告，非我方|KiCad文本解析；Altium未原生打开；无ERC|Codex审查；外部未做|
|驱动/负载|理想C能量/电荷、边沿、1/16/64/128路|数值RC能量检查，ALTERNATIVE_VALIDATION|NOT_VERIFIED|NOT_CREATED/NOT_RUN|负载/反灌/热P0|
|电源/Buck/LDO|角落/FB/纹波/容量/浪涌/热表达式|数值电感积分；无SPICE loop|NOT_VERIFIED|NOT_CREATED/NOT_RUN|负载/补偿/η未接受|
|TPS3851/安全|原厂逻辑/时序/阈值、当前heartbeat源|数字测试不证明物理独立关断|NOT_VERIFIED|NOT_CREATED/NOT_RUN|window/失电/锁存P0|
|RX/ADC|引脚/带宽范围；显式H(s)/AC CSV|理想AFE例，非生产电路；C16数字模型|真实ADC读回未做|NOT_CREATED/NOT_RUN|RX/AVCC/抗混叠P0|
|66MHz/I2C|裸器件限制、预算/上拉公式|外部IBIS/STA未做|NOT_VERIFIED|NOT_CREATED/NOT_RUN|VCCO/线束未知|
|BOM|5sheet/101类型重算、1010公式检查、860无源引用|无Excel GUI审图声明|非库存/采购实核|真实net未分配|功能去重未闭合|
|原数字系统|243原有测试、本轮nextstage基线|3696帧×3Icarus+1XSim及C/AXI/校准/安全/C16/软件门禁|无板写/超声|原OOC不升级为板级通过|实际本轮状态见FINAL_VERIFICATION.json|

复算环境：PowerShell7；本工作树.venv/Python3.10.11；项目锁定依赖另加pypdf6.20.0/cryptography50.0.2只用于资料读取；Icarus C:\iverilog\bin\iverilog.exe，Vivado2025.2 D:\Vivado\2025.2\2025.2\Vivado\bin\vivado.bat，GCC D:\DevC++\Dev-Cpp\TDM-GCC-64\bin\gcc.exe。其他机器先探测实际路径。

```powershell
Set-Location -LiteralPath 'E:\Codex_project\AMD_Sonofield_PCB_v5'
$env:PYTHONUTF8='1'
.venv/Scripts/python.exe v5/hardware/pcb/reviews/20261011_s2/calc/audit_inputs.py
.venv/Scripts/python.exe v5/hardware/pcb/reviews/20261011_s2/calc/review_calculations.py
.venv/Scripts/python.exe v5/hardware/pcb/reviews/20261011_s2/calc/verify_review.py
```

audit_inputs读取本地ignored public references，重取固定资料用fetch_sources.py（网络）。首轮PDF提取工具缺失/后来AES依赖不足的失败保留SOURCE_FETCH_ATTEMPT1及日志；STUSB4500L本地HTTP失败，实际改用原厂web读取，manifest明确。文字pypdf读取，TPS3851 timing和homies waveform另用Poppler渲染查看；未声称原生EDA操作。

完整数字基线另运行 `prepare_nextstage_checkout.py`、243 unittest、`run_nextstage.py --output v5/evidence/pcb_s2_20261011/digital_full`。见BASELINE_UNIT.log、DIGITAL_RUN.log、digital_full/summary.json。原脚本需fresh output，不能覆盖旧日志。prepare把本工作树少数current文本恢复Git blob行尾以保持既有字节比较；没有读历史正文。最终行尾恢复/原工程保护见FINAL_VERIFICATION.json。

243项单元测试的完整环境如下；CC必须指向真实GCC，TMP/TEMP须在本clone的build scratch内，因配置门禁有意拒绝clone外临时配置。输出目录先用新名称，保留失败日志。

```powershell
Set-Location -LiteralPath 'E:\Codex_project\AMD_Sonofield_PCB_v5'
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf8'
$env:PYTHONPATH=(Join-Path $PWD 'v5')
$env:CC='D:/DevC++/Dev-Cpp/TDM-GCC-64/bin/gcc.exe'
$env:TMP=(Join-Path $PWD 'v5/build/unit_scratch')
$env:TEMP=$env:TMP
New-Item -ItemType Directory -Path $env:TMP -Force | Out-Null
& ./.venv/Scripts/python.exe -m unittest discover -s v5/tests -v
if ($LASTEXITCODE -ne 0) { throw 'Unit baseline failed; preserve log' }
$env:VIVADO_BIN='D:/Vivado/2025.2/2025.2/Vivado/bin/vivado.bat'
$env:IVERILOG_BIN='C:/iverilog/bin/iverilog.exe'
# Full replay also requires the existing protected-byte preparation contract.
& ./.venv/Scripts/python.exe v5/scripts/prepare_nextstage_checkout.py
if ($LASTEXITCODE -ne 0) { throw 'Checkout preparation failed' }
& ./.venv/Scripts/python.exe v5/scripts/run_nextstage.py --output v5/evidence/pcb_s2_replay_new/digital_full
if ($LASTEXITCODE -ne 0) { throw 'Full replay failed; preserve output' }
```

本轮初次243项/完整数字基线PASS后，收尾补跑曾漏设CC及TMP/TEMP：226项中9 failure/2 setUpClass error（两个C测试类未展开）。原因分别为clone外临时配置被拒及编译器路径缺失；原测试/门限未改。恢复上述环境后再次运行243项全部PASS，耗时5.947s。失败与修正日志同存published_baseline/post_docs_unit_environment_failure.txt和post_docs_unit_corrected.txt；失败日志已脱敏个人目录。此环境失败未被隐去或冒充硬件失败。

下一阶段测量计划（未执行）：各轨无TX负载上电/CC预算；逻辑/功率掉电组合；VCCO/Ioff；单/16/64路共相及随机相电流/VDD/输出/RX泄漏/热点；RESET/WDO/锁存/栅极/rail；NC断线、主控制停但clock正常、快喂狗、欠压、过温；ADC实读和8路同相40kHz校准。短路/反接/过驱须先评估限流及设备保护并正式授权，本轮未实操。

独立验收最短路径：主对话审核Problem→器件级保护/供电方案→原生电路/网表/ERC/DRC→布局/回流/热→获准分板测量。没有外部Reviewer实质结论前不自认证Quality Gate通过。
