# PCB-S3给数字/PS/PL任务线的合同；本轮没有修改该实现

1. 每板独立HB，**合格任务完成后才产生下降沿**，正常下降沿19–21ms；上电/错误/未完整commit/未ACK/temperature invalid/safety fail时停止喂狗。自由运行计数器或定时器翻转不合格。高低电平建议10/10ms，不能每20ms仅翻转一次导致40ms下降沿。
2. TPS3430选CWDNC/SET0low/SET1high：保证合法窗口2.22–23.375ms；早于1.48ms必违规；1.48–2.22ms处于容差不确定区不得使用；超31.625ms最迟触发watchdog逻辑，另外叠加未保证的传播和切断/泄放时间。启动忽略170–230ms期间不允许据“未故障”判定已有进度。
3. 完整map/phase/safety/calibration状态/轨迹命令校验+atomiccommit+帧/ACK完成形成progress token；总错误状态、安全锁存、failcapture应阻断token。保留8bit请求/校准分离、35dB、签名capture/ACK、50Hz轨迹、共同timebase。RTL原prepcb_supervisor自由计时HB未改，当前不能联机使能。
4. 安全硬件FAULT独立清锁存+OE+TX功率，PS只观察。人工重使能须电源/温度/进度/配置均合法；不能自动定时重试清除故障。PGOOD只报告本地3V3存在，不等于全部12V/AFE/声学健康；ESTOP_STATUS组合两阵列FAULT_N目前建议健康高，需数字任务线核查health[0]极性。
5. 原63GPIO的RESET/SYNC/FAULT/I2C尚未完整暴露的项照旧开门禁；S3给出端口和物理pin，没有伪称有相应RTL。AXVCCO/外部STA/BRAM异步reset问题保留原问题单。
6. ADC负端保持AGND，既有单端±5V/高带宽方向不变；AFE输出带2.5V偏置须核查既有估计器对DC和饱和的处理。未经正式接口决策不得改为差分或改golden。±5V HBW220kHz不能泛化到±2.5V。读回配置/校准/blank恢复合格才允许正常采集。
