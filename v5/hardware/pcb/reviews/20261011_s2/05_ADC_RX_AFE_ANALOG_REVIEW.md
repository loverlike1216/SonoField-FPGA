# RX/AFE/AD7606C-16及数字接口

**Gate D HOLD。** RX确切MPN、阻抗频谱、最大接收电压、TX泄漏、线缆寄生、目标增益、噪声和抗混叠指标缺失；不能给每路完整已定R/C。每板4RX、两OPA4192封装=8运放，整机16运放，能容纳每RX两级候选，不能把4封装当4路。

推荐功能链：RX→有明确故障额定的串阻/限幅→偏置+第一级高输入阻抗放大→滤波/第二级低阻缓冲→专用屏蔽对→中央ADC输入RC。传感器到前级的限幅需要在负半周/失电时不向3V3/5V倒灌；BAT54S不是完整保护方案。TMUX1574的powered-off protection不允许任意负压输入，单5V下未偏置双极RX不能直接接入；完整输入范围/钳位电流/电荷注入需核验。[TMUX1574 RevC](https://www.ti.com/lit/ds/symlink/tmux1574.pdf)

OPA4192单5V工作是方向候选，典型GBW10MHz、slew20V/µs不能替代闭环稳定性和全温轨到轨负载摆幅。理想闭环G=10的估算带宽1MHz，但实际G/负载/反馈C未知，不能据此定型。REF5025AIDR供2.5V偏置需缓冲/噪声/启动和输出cap核验；本轮使用REF50 RevO里AI等级参数，不把新E等级低噪声性能错用于A件。[OPA4192 RevE](https://www.ti.com/lit/ds/symlink/opa4192.pdf)、[REF50 RevO](https://www.ti.com/lit/ds/symlink/ref50.pdf)

**手工AC示例而非生产AFE**：两个由理想缓冲隔离的一阶网络，高通R100k/C10nF，低通R10k/C100pF；

`H(s)=G * (s/ωH)/(1+s/ωH) * 1/(1+s/ωL)`，`fH=159.155Hz`，`fL=159.155kHz`，此例G=1，只验证频率和相位，不宣称增益/噪声合格。完整数值Bode数据 `calc/AFE_EXAMPLE_AC.csv`，Python从复数传递函数算出。R±1%、C±5%独立角落，40k相位约−14.709°..−13.057°，两路最坏差约1.653°；35dB自校准门限不能由这个结果推断通过。一阶滚降在400kHz仅约−8.65dB，明显不能独自保证宽带抗混叠；必须给输入频谱、ADC实际OSR/采样率和滤波阶数要求。不能把ADC内部滤波器假造为这一阶模型。

AD7606C-16 RevA页6表2：低带宽25kHz，高带宽一般220kHz，但±2.5V/0–5V量程高带宽为150kHz，绝不能把所有量程都写220kHz。40kHz在低带宽的通带外；高带宽也不是40kHz严格0dB。内部真实滤波响应、group delay和校准必须参考实际选定量程。[ADI完整数据表](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf)

| 节点/模式 | 原厂要求/当前缺口 |
|---|---|
| AVCC |4.75–5.25V；中央USB低压4.60V直接供给不合格；四AVCC各100nF就近、供电源10µF，页58|
| VDRIVE |1.71–5.25V但必须匹配FPGA/缓冲IO；未测Bank VCCO，不能据芯片范围反推3.3V已合格|
| REGCAP pin36/39 |各独立1µF到AGND；禁止两REGCAP短接，页17|
| REFIN/REFOUT pin42 |100nF到参考地；内部/外部参考由REF SELECT决定，不能同时强驱|
| REFCAPA/B pin44/45 |必须彼此连接，公共10µF低ESR到AGND；不是各1µF，也不能遗漏，页17/58|
| RESET |高有效；电源稳定后复位；已有ADC_RESET_N命名纠正不得倒退|
| 软件模式 |OS[2:0]=111；串行模式PAR/SER高；每通道配置带宽/量程/接口并读回；当前数字模型通过不等于芯片寄存器实读|
| 未用串口并行脚 |按页16/17定义绑AGND，4 DOUT配置相关引脚不得误绑；按ADC64_PIN_CONTRACT逐脚审|
| 吞吐 |800kSPS分析工作点、每4 DOUT各32bit→至少25.6MHz有效传送；还需BUSY/CS间隙/setup/hold/转换周期；原始8×16×800k=12.8MB/s|
| UART |115200 8N1仅11.52kB/s，不能承载12.8MB/s连续raw；需当前获准BRAM/PS聚合策略，不能私改协议|

ADC同步采样只覆盖芯片内部同一次CONVST，不能消除8路AFE/线缆/传感器相位差；40kHz下1°相当69.44ns。正负输入接法、单端/差分和偏置是否消除直流必须明确，当前原生网表缺失。

66MHz的周期15.1515ns、半周期7.5758ns。SN74LVC595A RevA §5.7在3.3±0.3V规定fclock至少104MHz、SRCLK/RCLK最小高低脉宽4.5ns，仅证明裸芯片能承受该频率。系统约束需要 `T/2 − tco_FPGA − tlevel − tbuf − cable_skew − tsu_595 − jitter >0` 和独立hold检查，须带真实VCCO、温度、线/负载/缓冲角落；当前不足以宣称66MHz线束通过。[TI595](https://www.ti.com/lit/ds/symlink/sn74lvc595a.pdf)

串阻不是统一33Ω：理想源端匹配`Rseries≈Z0−Rdriver`，Z0/驱动阻抗/源负载实际未取。布线stub和16颗595时钟扇出须看负载/缓冲；开源20Ω无可迁移保证。

595 OE高时Q为高阻，100k下拉在15µA IOZ+10µA TC输入最坏漏电假设下可到2.5V，超过0.8V VIL。10k候选约0.25V但高态负载约0.33mA，不能套用100µA测试条件下VOH≥VCC−0.2V；12mA保证在3.0V仅2.4V，与TC输入门槛没有严格正余量。需选择有保证阈值余量的缓冲/默认低网络、核验实际负载或制造商保证，不能只用典型曲线放行。SN74AXC8T245的DIR/OE参考VCCA，双侧断电Ioff有条件；任一侧未供电/线断/控制脚失电的端到端网络仍未证明。[AXC8T245](https://www.ti.com/lit/ds/symlink/sn74axc8t245.pdf)

I2C100kHz一阶近似 `tr≈0.8473*Rp*Cb`，按1µs允许上升时间、3mA/VOL0.4V假设，Rp下限967Ω，Cb100/200/400pF上限11.80/5.90/2.95kΩ；4.7k在400pF约1.593µs不能满足该假设。数据表/I2C实际器件sink上限、mux与隔离器串阻、重复上拉必须进入计算；每域独立，不把上下域同时并联。当前TCA9548A reset未落实是系统P0。[TCA9548A](https://www.ti.com/lit/ds/symlink/tca9548a.pdf)
