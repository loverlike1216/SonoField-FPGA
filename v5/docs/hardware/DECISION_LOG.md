# 2026-10-11 当前决策来源

来源为实际用户请求及完整指令文件SHA256
`8b1fdbfe351b789241afc8abb644179f19b9075b5152f4953a0555545a8d22d4`。
正式跨版本记录见shared/DECISIONS.md的ADR042；未编造外部ChatGPT决策。

| 决策 | 状态 | 执行边界 |
|---|---|---|
| 保持v5/原仓库/128TX8RX/数字核心及验收 | ADOPTED | 不新建版本、不改历史 |
| 四独立电源入口，中央USB-C5V，主板电源触点NC | ADOPTED_CURRENT_ARCHITECTURE | 替代旧中央header供电要求；电气实现HOLD |
| 上下各12V中心正极5.5×2.5、60W容量候选、40W备选 | ADOPTED_DESIGN_CANDIDATE | 最坏实功率未知；不采购 |
| 最低20%/目标30%源头寸 | ADOPTED | 温度/路径额定必须另降额 |
| 单2线I2C/TCA9548A三域，63GPIO+5备用 | ADOPTED_CANDIDATE | wrapper/局部复位/Ioff/外部时序未完成 |
| 单C16/3TMP117、12mm/固定坐标/EPS2–5mm | ADOPTED | 模拟、空气场与悬浮未验证 |
| ADC_RESET高有效更正 | DATASHEET_CORRECTION | 原RTL极性保持 |
| TPS3431作窗口看门狗 | REJECTED | 保留窗口要求和TPS3430候选审查 |
| CV²f代替整机功率，假5V3A/假ERC/假硬件PASS | REJECTED | 未知保持UNKNOWN/HOLD |
| 自主正常commit/push/GitHub同步 | USER_AUTHORIZED | 不重复询问常规同步 |
| 当前关键缺陷下main提升、采购、制造 | HOLD_QUALITY_GATE | 权限不代替电气和系统验收 |

BRAM架构Problem保持OPEN；未经真实来源和body-hash/版本匹配的Decision
不实施。输入文档的“已独立审核”是该文档的来源声明，本轮没有工具取得
独立Reviewer身份/审查记录，不另行认证为真实独立电气签核。
