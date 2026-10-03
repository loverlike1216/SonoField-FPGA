# 参数检测与资料交叉验证

这是用户指定的检测归档入口，属于当前 SonoField-FPGA v2，不创建新版本、不迁移工程源码。最新 [2026-10-04 DDR 检测报告](20261004_ddr/RESULT.md)、[机器结果](20261004_ddr/summary.json) 和 [候选配置](../v2/config/ddr_candidate.json) 是当前入口。

`20261004_ddr/` 保存真实公开查询、脱敏工具输出与检测脚本；其 `local_raw/` 仅留本地并被 Git 忽略。`inputs/` 接收未来提供的板型匹配工程/原理图，当前没有输入可作配置证明。文件路径应由接手同事根据自身安装目录调整。

## 安全复查命令

仅在同型号裸板、无外接负载、经过本报告边界审查时复查。默认 PowerShell 7；不打开 COM、不调用 ps7_init、不写寄存器、不访问 DDR RAM、不下载程序。出现多个 APU 时脚本退出，不能自动挑选一个。raw 输出可能含线缆标识，必须仅保存到忽略目录，公开前脱敏。

```powershell
Set-Location '<自身 SonoField-FPGA 克隆根目录>'
$vivadoBin = 'D:/Vivado/2025.2/2025.2/Vivado/bin' # 换为自身 Vivado2025.2 安装目录
New-Item -ItemType Directory -Force parameter_detection/20261004_ddr/local_raw | Out-Null
Get-NetTCPConnection -LocalPort 3121 -State Listen -ErrorAction SilentlyContinue
```

先确认已有 listener 确实是本机 Vivado hw_server，并检查绑定范围；不能将任意 3121 服务当成目标服务器。仅在不存在服务器时，本次采用如下隐藏的 localhost helper：

```powershell
$probeServer = Start-Process -FilePath "$vivadoBin/unwrapped/win64.o/hw_server.exe" -ArgumentList '-stcp:127.0.0.1:3121','-p0' -WindowStyle Hidden -PassThru -RedirectStandardOutput parameter_detection/20261004_ddr/local_raw/hw_server_stdout.log -RedirectStandardError parameter_detection/20261004_ddr/local_raw/hw_server_stderr.log
$probeServer.Id
```

确认 localhost listener 就绪后，以下分别为本次实际执行的只读检测入口；输出文件名使用新后缀避免覆盖已归档证据：

```powershell
& "$vivadoBin/xsdb.bat" parameter_detection/20261004_ddr/read_ddrc.tcl *> parameter_detection/20261004_ddr/local_raw/recheck_ddrc.log
& "$vivadoBin/vivado.bat" -mode batch -source parameter_detection/20261004_ddr/read_jtag.tcl -log parameter_detection/20261004_ddr/local_raw/recheck_jtag.log -journal parameter_detection/20261004_ddr/local_raw/recheck_jtag.jou
```

成功判据：真实 JTAG 设备/IDCODE 与 XSDB PROBE_READ 输出；再按 AMD 寄存器定义判断是否为有效配置。本次复位值不满足 DDR 配置确认门禁。停止新建的 helper 前核对 PID、映像和是否被现有 GUI 使用；不能关闭用户其他服务。不要在复查中替换驱动或改变 Boot/跳线。

## 资料提升门禁

要把 512 MiB / 32 bit 从 CANDIDATE 提升为 CONFIRMED，必须取得板型匹配来源并比对实际两颗器件与 DQ/rank/地址拓扑、PS 参数和容量地址映射。通用示例、重新填写候选值的工程和 DDRC 复位默认字段均不构成交叉验证。配置事实、初始化后寄存器、实际电压/频率和运行 memory test 分别记录证据状态。

官方来源：[Micron FBGA decoder](https://www.micron.com/sales-support/design-tools/fbga-parts-decoder)、[D9PSK 实际解码器件](https://www.micron.com/products/memory/dram-components/ddr3-sdram/part-catalog/part-detail/mt41k128m16jt-125-it-k)、[AMD DDRC 字段](https://docs.amd.com/r/en-US/ug585-zynq-7000-SoC-TRM/Register-ddrc_ctrl-Details)。
