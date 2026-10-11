# PCB-S3工程审查与剩余门禁

**PCB-S3结果：REVISE。** 器件连接/可复算候选交付ACCEPT WITH LIMITATIONS；整板电气、原生原理图、独立Review和制造验收未通过。不是模型自我认证。电源推荐已确定，不再要求用户选择功率档。

| 模块 | 结果 | 依据/限制 |
|---|---|---|
| 工作区/版本/保护边界 | ACCEPT WITH LIMITATIONS | v5/独立工作树/原区保留/Draft链未合并 |
| 12V/USB电源选择和静态限流 | ACCEPT WITH LIMITATIONS | 29.36W/12.35W持续设计包络；2mA/20mA分配及阻值传播待真实资格确认 |
| 安全/切断 | REVISE | 45静态检查、256布尔状态；快速故障能量/储能泄放/单故障SOA未保证 |
| 64TX映射 | ACCEPT WITH LIMITATIONS | 128逐通道、双阵列完全对称；真实RLC和全温相位/热未验证 |
| 8AFE/C16 | REVISE | 64pin/RC模型/静态AVCC可审；poweredoff钳位、量程/偏置处理、噪声和35dB未验证 |
| 跨板/AX接口 | REVISE | 电源NC/groundinterleave；自动掉电隔离及真实VCCO/66MHz STA未闭环 |
| 原生CAD/ERC/BOMrelease | REVISE | 严格表/可视审图fallback交付；native NOT_CREATED/ERC NOT_RUN/采购HOLD |

S3-0对账完成；S3-1预算及上下界分层完成候选；S3-2电源选择完成候选；S3-3全TX/安全连接完成候选；S3-4全RX/ADC完成候选但保护/配置有关键门禁；S3-5信号/机械连接完成候选但具体线束和时序未冻结；S3-6按允许fallback交付，原生/ERC未完成；S3-7实位号候选BOM和Draft同步。所有“完成”只指指定候选资产，不表示电气合格。

| Gate | Owner | 可关闭门禁的具体动作 |
|---|---|---|
| G1 原生图纸与独立审查 | PCB/CAD reviewer | 按严格表建立嘉立创EDA原生图、符号/封装逐pin复核、真实ERC+导出差异签核；当前无连接客户端 |
| G2 电源/故障/热资格 | 电源及安全工程 | 确认限流R容差传播与支路分配；源线阻/启动/UVLO/OVLO/电容有效值/热/短路SOA/fastfault最大能量/泄放；先离线模型后受控样机，另获硬件操作授权 |
| G3 AFE和接口电气 | 模拟及接口工程 | 定型RX、外部钳位/掉电隔离；修复主机/阵列I2C反灌；证明自动off或受控连接边界；噪声/blank/增益相位35dB及线束热/ESD |
| G4 真实数字集成/约束 | 主RTL/PS任务线 | 实现progressHB，补63GPIO绑定，核对ADC单端量程/偏置；VCCO/外部STA/BRAM问题闭环，S3不替其改实现 |
| G5 机械/物料最终签核 | PCB机械/物料工程 | 确认NU/RX尺寸及辐射面、64pin连接器/线缆、USB封装、所有无源/保护具体SKU/降额，净表BOM交叉审查；随后再申请制造/采购/main批准 |

当前243测试PASS；S2帧级/综合继承，不是新硬件证据。失败记录、未取到的源、原始资料hash、工作簿公式与静态检查均保留。用户授权只到候选/Draft同步，制造/采购/板写/main仍HOLD。创新性NOVELTY_NOT_CONFIRMED；未复制开源电路冒称原创，S2参考保留为背景。

复核入口：03电源结论、04安全、05TX映射、06AFE、09图纸/ERC、10BOM对账、HW_SW_HANDOFF。当前候选仍有G1–G5，不能进入制造。
