# OPEN_BLOCKERS

P0_THEORY_BLOCKERS = 0。

| ID | 状态 | 内容 | 是否阻止本轮理论原理图输入 |
|---|---|---|---|
| REVIEW-01 | HOLD | 原frozen_parent源码hash FAIL；新用户授权差异需独立Review，原报告保留 | 否，禁止自动main推广 |
| MODEL-01 | HOLD | 完整动态IBIS、595 OEM模型、真实SSO/PDN/EMI未验证，采用公开说明的保守替代模型 | 否，必须遵守线长/负载/地参考条件 |
| CAD-01 | NOT_CHECKED | 原理图未创建、原生ERC未运行，采购/封装库精确映射未完成 | 否，绘图后制板前关闭 |
| RUNTIME-01 | HOLD | 实际PS/BSP完整运行镜像与真实UART/温度/ADC尚未部署；safe-status ELF不能当生产系统 | 否，下一阶段需实现/验证 |
| PHYSICAL-01 | NOT_CHECKED | 上电、连续NU端电压、声压/悬浮、实际热/ADC/线缆尚未测试 | 否，用户本轮只要求理论 |
| CHAT-01 | HOLD | 指定ChatGPT聊天无法直接read/send；0交互，不伪造决策 | 否，已给独立Review咨询包 |

所有未来工作保持v5，不自动进入原理图绘制或PCB。

## BOM中保留的两项HOLD

85种MPN中静态选型状态83PASS/2HOLD，未悄悄全部改为PASS。7101MD9AV2QE的5A/28VDC与针序已核对，HOLD对应实际接点反弹/浪涌资格；输入已精简为1µF并由后级eFuse缓启动，按本轮受控12V源条件可绘图。NU40C10R-2按用户T/R合并原厂资料作为接收候选，2脚/电容/前端连接已定义，HOLD对应采购机械极性确认、实际灵敏度离散/增益与声学SNR资格；没有把这些实物未验证项冒充PASS。两项均非本轮已知针位冲突或额定计算FAIL，制板/采购/实物验收前仍须关闭。
