# 发布回执：Draft PR 等待人工审核

[Draft PR #1](https://github.com/loverlike1216/SonoField-FPGA/pull/1) 已建立，保持OPEN/DRAFT，没有合并main。实际核对的候选证据提交为 `f014214fb8db554fb3df9ac971ac759d683447a5`，功能验证源码为 `0ab574f9e2ad422106655f3c827e89d262d93bb4`，原BASE及当前main仍为 `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`。候选完整远端Git树与本地路径/blob/mode一致；冻结原文件3907个、97559165字节、2032个唯一原blob，加2个冻结元数据，差异0。最新PR head和checks以GitHub实际页面为准。

观察时间 `2026-10-09T13:53:22.176049+08:00`。GitHub Ubuntu/Python3.10的 [push检查](https://github.com/loverlike1216/SonoField-FPGA/actions/runs/37890523156) 和 [PR检查](https://github.com/loverlike1216/SonoField-FPGA/actions/runs/37890525671) 均已实际success；仅为结构/继承/冻结元数据/当前路径验证，不冒充离线全功能、Vivado或硬件测试。三份完整离线回归及独立clone结果见PORTABILITY_AND_REGRESSION。

CP-20261009-003在上述证据提交中保存候选验证状态。当前CP-20261009-004记录本次真实发布与独立CI里程碑；其head/base是观察到的真实提交，包含本回执的新提交必须用Git文件历史定位，不伪造自引用SHA。本回执之后只补当前状态/交互/审计元数据，v5非evidence输入与已测试源码完全一致。

结论 **ACCEPT WITH LIMITATIONS — CANDIDATE ONLY**；正式main迁移尚未完成。用户需审查具体候选与永久路径 `E:\Codex_project\AMD_Sonofield`。获明确批准后才重新对账、普通合并、独立clone远端main进行冷启动与冻结清单验证，再正式提升workspace_path。旧物理沙盒完整保留且后续默认不读，history_old默认不读/不改。无新版本、无设备操作、无force push。
