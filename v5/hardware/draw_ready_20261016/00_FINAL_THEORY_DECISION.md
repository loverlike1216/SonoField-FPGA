# 最终理论决策

**THEORY_DRAW_READY：YES。整体结论：ACCEPT WITH LIMITATIONS。**

项目SONOFIELD_FPGA，唯一活动版本v5，工作区E:/Codex_project/AMD_Sonofield，分支codex/v5-hardware-design-20261011，任务开始HEAD8c27b5841b5494c3761ab211881a3ea2be63e8c8。用户已明确授权必要正式RTL/XDC修改及同分支commit/push。用户当前确认器件XC7Z020-2CLG400I，原-1结果保留为历史保守试验；JTAG只确认Z020 ID，不确认速度/温度后缀。

唯一方案：三板各自12V输入；阵列固定降压10V单端TX；128TX、8RX、32lane×4bit、每阵列16×SN74LVC595APWR和32×UCC27624QDRQ1。中央5颗、每阵列4颗SN74LVT244BPWR本地3.3V再驱动。第一接收端22Ω/3.3pF，中央输出47Ω，阵列DATA47Ω，四组局部时钟各15Ω/4个595、≤27mm、≤50pF。40/64芯公公排线连接2.54mm排母，两段各≤150mm；阵列偶数针全GND。J11.32–35为ADC DOUTE–H；J11.39仅≤50mA接口参考，预算≤20mA，不供主板/阵列/端接。

F流水由128/256MHz同源时钟驱动，SRCLK42.666667MHz，每24微周期接收完整快照，锁存与下一帧重叠；40kHz256级10.24M更新/s，最高41.5kHz要求10.624M，容量10.6667M。保持8bit requested/calibration分离、原子完整map commit、50Hz运动、协议和全部旧golden/阈值。

ADC最终采用8MHz SCLK、8DOUT、400kSPS（320corecycles），CS末尾保持4corecycles。此前16MHz/748.538k及10.667MHz/533.333k为过程候选，已由缓冲最坏脉宽/输入阈值预算取代，不是终版。400kSPS在40kHz提供每周期10点，八路同时采样，配合1024点幅相估计；本轮未承诺1MSPS。以减少有效利用率换取现有AHCT244的明确时序裕量，不新增器件。

动态完整IBIS、真实PDN/SSO、生产BSP和实物声学验证未完成；本轮用户允许用厂家保证值/保守等效模型闭合原理图输入。未制作PCB不作为理论出图阻塞。此结论不批准PCB、采购、烧录、部署、量产或main合并。完成后停止，等待独立Review。
