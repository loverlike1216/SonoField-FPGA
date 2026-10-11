# PCB-S3 execution contract / baseline

PROJECT_ID=SONOFIELD_FPGA;repository=https://github.com/loverlike1216/SonoField-FPGA.git;workspace=E:/Codex_project/AMD_Sonofield_PCB_v5;branch=feat/v5-pcb-design;active/highest=v5;S3 base=23f8d4cedb44536f8c35fd132171868a80f9ded7.

用户实际回复：“按 S3 文件完整执行，保持 v5、制造/采购/板写/main 合并 HOLD”。正式指令完整保存在 AI-interaction-memory/codex/instructions/v5_pcb_s3_engineering_20261011.md，SHA256=b3a33a2b0541e8626ea952f2c6c8288ae0a78b8133f024c1cd05c42036475e44。附件中的批准文字没有被当作独立授权；本轮依据真实用户回复执行。

Goal/Scope: 三板器件级候选、严格连接表、最大持续输入包络、条件负载模型、保护真值表、可复算工作簿、实位号BOM和Draft PR6同步。电源选择由Codex完成。未知真实RLC不再阻止画图。

Non-goals/Do not change: RTL/firmware/XDC/接口协议/goldens/35dB门限/128TX8RX/32lanes×4used/40kHz激励/50Hz运动/12mm pitch/100mm nominal90–115mm gap/AX7020Rev3/C16。无v6。无实板串口/JTAG/SD/Flash/DDR操作、采购制造、main合并。原工作区和Historical project正文不读写。

Architecture: 每阵列独立12V；中央5V3A USB-C只供电；AX7020电源触点NC；每阵列TPS3851×1另加独立窗口监测、温度、锁存、TX独立切断。外部ChatGPT读取BLOCKED，无独立审查伪称。

Validation: 原243测试；严格pin/net数量/实际端口/ADC物理pin/上下一致性/硬件禁能逻辑/功率角落计算；工作簿缓存与Python交叉计算。S2已有3696帧×3Icarus+1XSim为继承证据，本轮未重跑且不宣称新跑。原生CAD未连接时使用明确允许的严格连接表降级；ERC NOT_RUN。

Rollback: 独立工作树新增S3路径，保留S2、失败日志和原BOM；可通过revert S3提交撤销；不reset/forcepush。DoneWhen: 候选内容可审查可复算、未完成门禁明确、PR更新并确认远端；不等同制造验收。

Reproduce from worktree: `.venv/Scripts/python.exe v5/hardware/pcb/reviews/20261011_s3/calc/power_worst_case.py`, then `build_candidate.py`, `review_candidate.py`, `build_reports.py` in同一calc目录。设置PYTHONUTF8=1；输出限S3目录；脚本不访问硬件。工作簿命令见calc/build_workbooks.mjs。
