# 阵列电源切断和安全电路候选

精确连接以netlist/PIN_NET.csv为准，UP/DN逐位一致；svg/为由同一连接表输出的带pin/net标记审图页，非嘉立创EDA原生图纸。没有运行ERC。

路径：J1中心正12V→F1 3A→D1 SMBJ15A→U1 TPS259470LRPWR全板输入保护→RS1 20mΩ→常供逻辑/AFE及U5独立TX切断→TX12→32×TC4427A。U1的UVLO用38.3k/4.99k、OVLO48.3k/4.99k，均0.1%；用比较器min/max和漏电验证上下界。U5 EN由锁存ARMED经过100k/100k分压，默认接地；所有TC输入高侧上拉都由TX12供电。U1/U5各1.65k1%限流，ITIMER NC；不能解释为零延迟。

U10 TPS3851H33EDRBR：VDD=3V3，CWD经10k至3V3，SET1高，MR高；RESET和WDO为开漏汇入FAULT_N。每阵列1颗、总2颗。H33约3.069V±0.8%欠压监测；看门狗170–230ms，非窗口。U11 TPS3430DRCR是**补足过快检测**，不是旧TLV803组合；CWD/CRST NC、SET0低、SET1高，下降沿合法保证交集2.22–23.375ms。建议合格进度每20ms下降沿，19–21ms合同；低/高各5/15ms或10/10ms实现须与下降沿合同一致，不用40ms翻转误喂。

U12 TMP302A两TRIPSET高：65°C候选，HYST高10°C典型；独立于TMP117/I2C/PS。放在TC阵列热点邻近，需热点和响应滞后实测。JESTOP常闭回路，断线后10k下拉、U15反相、QSAFE拉低FAULT_N。U1/U5 FLT也经0Ω显式汇入FAULT_N，但FLT并不报告所有UV/OV，12V保护依靠eFuse直接比较器，逻辑欠压由TPS3851独立处理。

U13 SN74LVC1G74：/CLR=FAULT_N，D=/PRE=3V3，非反相Q是**pin5**，反相Q是pin3；手动按钮、RC、Schmitt送CLK。故障清零锁存；故障消失不产生CLK上升沿，所以不自动重启。按钮持续按下不能当作持续许可；按钮弹跳/释放时序仍须实测。启动RESET保持低期间不能正常解锁，初始化必须在进度合格后人工重使能。

分压处理POR盲区：FF VCC<1.65V输出未定义，按输出≤VCC及EN漏电分配，EN最大0.8383V<eFuse下降阈值min1.076V。健康3V3≥3.15V且小负载VOH≥VCC−.2V时，EN最小1.4552V>上升阈值max1.223V。其他引脚反灌破坏该供电边界的情形仍需电气验证，不能用布尔表证明。

U16/U17/U18把FPGA OE、NOT_ARMED、FAULT_BAD组合为595_OE_N，10k默认上拉。数据无效时强制595高阻，逐通道基极下拉使TX输入低；3V3完全掉电时TX可残留DC电压，依赖切断和680Ω泄放。总TX电容上限设计750uF时，储能≤0.06534J、降到1V被动泄放约1.329s；**不是瞬时归零或认证安全能量**。C/ESR/泄漏/声学单次瞬态必须在G2验证；若要求更快泄放，优先补独立主动泄放电路，当前未伪称已有。

已检256种布尔故障/锁存组合；任一UV/early/late/temp/estop/inputflt/txflt使能均为0。这只是静态ALTERNATIVE_VALIDATION。手册未给出最大fasttrip/传播/能量时，仍保留制造HOLD，不能虚构一个全故障瞬态上界。
