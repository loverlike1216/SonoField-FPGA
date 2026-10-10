# 离线复现

在正式仓库的独立克隆中，先用sparse-checkout只物化v5、shared、当前AI索引、
.github和根文档，确认Historical project工作树不存在。不要以旧沙盒作数据源。
在PowerShell7仓库根执行，所有输出标签选择未使用过的名称：

```powershell
git config core.autocrlf false
python v5/scripts/prepare_nextstage_checkout.py
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r v5/requirements-lock.txt
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
$env:PYTHONPATH=(Join-Path (Get-Location) 'v5')
.venv/Scripts/python.exe -m unittest discover -s v5/tests -v
.venv/Scripts/python.exe v5/scripts/generate_hardware_design.py --output v5/build/reproduce_hardware_unique
.venv/Scripts/python.exe v5/scripts/validate_hardware_design.py --output v5/build/reproduce_contract_unique.json
.venv/Scripts/python.exe v5/scripts/check_nextstage_preservation.py
.venv/Scripts/python.exe v5/scripts/check_workspace_migration.py --freeze-base 618b6f1ffe3dae9b98c59bf1c981349e48644662
```

预期243项测试全部通过；再生12个JSON/CSV/SVG/XDC与hardware/design_20261011同名
原文件逐字节一致；合同/公式检查PASS，物理连通和ERC仍NOT_RUN。原生包数据库
CSV是本轮工具证据；复核时从IO_PINMAP.csv取68个GPIO PACKAGE_PIN，每行一个，
使用实际安装Vivado2025.2运行hardware_design_package_review.tcl，两个tclargs
依次是输入针脚文本和新输出CSV；命令必须显式-log且-nojournal，避免根目录产生日志。

完整数字门禁还需设置真实工具路径，不从当前GUI推断环境变量：

```powershell
$env:VIVADO_BIN='<actual Vivado2025.2>/Vivado/bin'
$env:IVERILOG_BIN='<actual Icarus>/bin'
$env:CC='<actual C compiler executable>'
.venv/Scripts/python.exe v5/scripts/run_nextstage.py --output v5/evidence/hardware_reproduction_unique
```

成功标准含3696帧×三Icarus+一XSim的原子map/ACK/轨迹Hash一致、原C/AXI/
校准/安全/等价、温度/稀疏/动态GUI/C16四DOUT实际顶层门禁全部PASS。
原生2025.2 OOC/ARM BSP历史构建保留其作用域；本轮没有新板级program证据。

XLSX由v5/scripts/build_hardware_design_bom.mjs通过@oai/artifact-tool生成，
在可用该运行库的Node环境中传入绝对v5目录及新输出目录。版本与运行库
来源见TOOLCHAIN.json；不把本机缓存路径当成可移植依赖。没有该库仍可用
Python标准库独立验证已提交XLSX的五表、404行装机/备件公式和全部缓存。
生成器保留UNKNOWN价格和采购HOLD；XLSX ZIP字节可含创建元数据，重建以
公式/单元格/数量一致作为判据，不宣称整工作簿每次bit-exact。

错误处理：保留失败输出，修正工具路径/合法普通错误后用新标签重跑；
不得复用旧结果冒称新PASS。输出已存在时合同审查拒绝覆盖。不要取消核心
测试、修改阈值、读取冻结代码或向硬件写入来绕过离线错误。
