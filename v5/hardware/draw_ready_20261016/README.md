# SonoField-FPGA v5最终理论交付

入口：00最终决策→FINAL_REVIEW→02完整指南→01_BOM→03–09针表/对账。所有CSV为UTF-8 BOM，XLSX六页含数量公式和逐针/无源/外部配件；无真实采购价格或库存承诺。

目录：inputs原始输入副本；backup正式源变更前备份；scripts实际执行代码；candidate_rtl独立testbench；sources原厂PDF/IBIS（本地研究、不自动再分发）；results实际工具结果；logs原始日志；AI-interaction-memory可观察原始记录（本地私有）。旧尝试保留在native01–20与相应日志，不是当前放行版本。当前Native标签见results/FINAL_NATIVE_LABEL.txt。

复现：PowerShell7执行REPRODUCE.ps1 -Mode Validate。完整重放用-Mode Full -RunVivado，创建新replay目录，绝不覆盖旧证据。免费工具路径/版本见requirements-lock.txt与ENVIRONMENT_FINAL.json，Vivado需要用户已有可用安装/license。本任务未收费、未采购、未修改硬件。

DRAW_READY只是原理图输入理论闭合；实际PCB、原生ERC、部署和声学性能没有通过认证。
