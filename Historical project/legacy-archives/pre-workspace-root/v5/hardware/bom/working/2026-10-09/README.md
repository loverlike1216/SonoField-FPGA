# 2026-10-09 BOM 工作副本

这是对 2026-10-08 原始提交的单独工作修订，不是采购/电气/制造释放。原件位于 `../../submissions/2026-10-08/`，SHA256 decf6b026c0b5a48efb6800d27463246d61f62a9e2de01c75da5012d7fe69a35，保持字节不变。changes.json 给出逐格修改原因。工作副本推荐 C-16 ADC；生产 RTL 和正式选型仍为 AD7606B，换型待独立 Review 与用户批准。

新增安全/电源/I²C/驱动偏置是候选，不应直接叠加旧模糊总量采购。门逻辑/监控数量保留 UNKNOWN；环境板 DNP；复合 RC/参考行是设计组，不重复采购。所有主板必须仍有各自监测与独立供电。

72 行原件 M=SUM(H:L) 保留；工作副本采用 artifact-tool 2.8.89 重算、导出并对四个区域做 PNG 视觉检查。新增表六个总量 SUM 另行验证。preview/ 为本地生成物，inspection NDJSON 为轻量检查输出。

## 复现与查看

直接用 Excel 或兼容软件打开工作副本即可，不依赖 Codex。核验：从仓库根用 Python 3.10+ 运行 `python v5/hardware/integration_candidates/20261009/verify_candidates.py`；只用标准库读取 XLSX XML，无需 openpyxl。

生成脚本 `v5/scripts/revise_ax7020_bom.mjs` 使用 artifact-tool；在有该依赖的 Node 环境运行。Codex 环境可将 `ARTIFACT_TOOL_MODULE` 设为已安装包的 `dist/artifact_tool.mjs` 完整路径，再 `node v5/scripts/revise_ax7020_bom.mjs`。普通同事环境若无此内部依赖，可阅读脚本/changes.json 并人工按格修改；不要声称生成链可在没有该依赖的机器直接运行。脚本只改工作副本和预览，不改原件，也不操作板卡。xlsx 的 ZIP 元数据可能变化，验证内容/公式及原件 Hash，而非要求重导出二进制完全相同。

来源与电气限制见 `v5/hardware/integration_candidates/20261009/`；制造 HOLD。
