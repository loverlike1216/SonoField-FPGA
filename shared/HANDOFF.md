# v5 候选迁移交接

目标是审阅同一仓库、同一v5的工作空间迁移。恢复顺序：README/AGENTS → PROJECT_STATE/VERSION_STATE/CONTEXT_CHECKPOINT → CURRENT_PLAN/DECISIONS/BLOCKERS/ACCEPTANCE → 当前迁移证据 → Git状态与远端。BASE `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`，实际验证源码 `0ab574f9e2ad422106655f3c827e89d262d93bb4`；本次Codex thread为01a11f01-ebbe-76f3-ac92-b3e04e67b27a。

旧物理/私有/忽略/Git资料复核未变；封存3907个原Git文件和2个元数据；当前1017个v5原文件保留、102个核心/测试/黄金/BOM blob不变。三份新运行各115项测试和3696帧×4及完整嵌套门禁通过；15项离线候选、ADC256帧双工具、2025.2 OOC与18源重开也通过。规范化Hash一致。真实日志、源码/运行路径、版本、失败和限制见PORTABILITY_AND_REGRESSION及对应evidence。

结论ACCEPT WITH LIMITATIONS — CANDIDATE ONLY。发布Draft PR及实际CI/远端回执后等待用户main合并和永久路径批准；批准后再对账、合并、独立clone远端main验证。原生v5原理图NOT_CREATED/ERC_NOT_RUN/制造HOLD，整机REVISE；两个ADC/Rev3问题仍OPEN。ChatGPT历史BLOCKED，当前Codex记录PARTIAL，无虚构独立Review。

保护原沙盒、冻结历史、核心实现和验收。首次候选路径门禁失败及冻结前Windows文件恢复错误保留，修复和完整重跑有独立证据。未来默认不读取封存历史；继续当前v5，不升级、不操作板卡。
