# 8RX/AFE/C16/中央USB-C

每阵列4RX，型号仍RX_MPN_UNKNOWN；每阵列2×OPA4192四运放，合计4颗/16个放大器，每路两级，数量无虚增。每RX经2×4.99k0805、100nF50V耦合、100k偏置到本地REF5025的2.5V。第一级非反相增益11，Rg10k/Rf100k均0.1%，Rf并15pF2% C0G；TMUX1574后放大器域blank选择2.5V，之后2.21k/680pF2%低通及第二级跟随器，100Ω输出阻尼；中央每路499Ω/1nF2%对地滤波后到ADC正端，负端接AGND，保持既有单端接口。

线性模型见evidence/AFE_FREQUENCY_SWEEP.csv，包含给定RC角落；不把它当作真实RX/OPA/线缆/ADC内部滤波模型。2.5V单电源偏置后输入有效动态范围要保留OPA输出余量；C16软件配置建议与既有RTL约定保持±5V/高带宽220kHz/4DOUT，实际转换/配置读回未运行。AFE输出中心2.5V占用单端±5V量程的部分动态范围，需要核查DC偏置处理、饱和及噪声，未擅自切换差分量程或修改RTL。35dB校准验收门限保持，线性RC匹配不能证明35dB。

传感器±30V为输入保护分析的假设故障，不是供应商保证；2×4.99k只限制电流，不能证明上电/掉电内部钳位和反灌安全。当前未加入经完整验证的外部钳位/泄放网络，G3保持REVISE；ADC±21V和OPA±10mA是stress边界，不能宣称正常工作额定或ESD能力。blank在放大器之后有意限制TMUX信号范围0..5V，不能保护第一级过载，恢复时间须测。

中央USB-C UFP3A检测见03；TPS63070强制PWM、1.5uH、Rtop68.7k/Rbottom10k0.1%产生约6.296V。含FB±1%、阻值、漏电及20mV纹波分配得到6.195299–6.396943V；最低大于ADP7118的6.09V完整精度条件。ADP5V全温±1.8%给AVCC4.91–5.09V，满足4.75–5.25V静态条件。中央3V3另用TPS54202，从6V3供电。阵列模拟前级则TPS54202 Rtop102k/10k，VFB0.581..0.611传播得到约6.49–6.85V后再ADP5V；不是套用0.6V假精度。两个22uH buck磁件须按实际负载与390k最小频率验证峰值及热。

UADC全部64pin在严格表：AVCC1/37/38/48每pin100nF，VDRIVE23本地100nF；36/39REGCAP分别1uF，42REFIN100nF，44/45相连10uF；AGND2/26/35/40/41/47和REFGND43/46到连续地平面。OS0..2高进入软件模式；PAR/SER高；STBY高、RANGE低、WR低；RESET activehigh默认下拉；CS默认上拉，CONVST/SCLK/SDI默认下拉。DOUTA/B/C/D是pin24/25/27/28，SDI29。其余未用串行数据输出19..22NC，DB0..2/DB12..15按手册串行模式接地。

ADC RevA Table2p9正常1MSPS IAVCCmax50mA、IDRIVEmax1.9mA，分别算，不把1MSPS能力误作软件现有采样率。USB连接器GCTUSB4500-03-0-A16pin，power-only数据触点NC；原厂网页确认5A总VBUS额定，型号不再占位，准确封装/图纸版本待核。连接器48V额定不表示CC/LDO能承受48V。开机瞬态、buckboost效率/纹波/稳定性和USB ESD为G2/G3，未声称电源完整验证。
