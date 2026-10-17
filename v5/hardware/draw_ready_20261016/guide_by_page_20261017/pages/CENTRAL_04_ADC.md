# CENTRAL／04_ADC逐步连接分册

本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。

<a id="page-central-04-adc"></a>

## CENTRAL板／04_ADC图页

中央放ADC，左侧放控制AHCT，右侧放DOUT返回翻译器。ADC参考电容就近围绕相应脚，不能把REFCAP当2.5V偏置。

<a id="central-u-adc"></a>

### 第001步：在CENTRAL／04_ADC放置 U_ADC

在 **CENTRAL板的04_ADC图页**，先放置 **U_ADC**，精确型号 **AD7606C-16BSTZ**，封装 **ST-64-2/LQFP64**。

04_ADC中部放64脚ADC。AVCC/VDRIVE用V5A；所有AGND/REFGND接本地连续GND。REGCAP、REFIN/REFOUT、REFCAP电容按各自网络，不能混接。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 1 | AVCC | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 2 | AGND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 3 | OS0 | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 4 | OS1 | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 5 | OS2 | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 6 | PAR/SER_SEL | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 7 | STBY_N | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 8 | RANGE | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 9 | CONVST | ADC_CONVST | IN | 从此脚引线，标注精确网名`ADC_CONVST`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_CONVST.2（2）；04_ADC/R_ADC_SAFE_CONVST.1（1）。 [完整端点N0407](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0407)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 10 | WR_N | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 11 | RESET | ADC_RESET | IN | 从此脚引线，标注精确网名`ADC_RESET`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RESET.2（2）；04_ADC/R_ADC_SAFE_RESET.1（1）。 [完整端点N0441](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0441)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 12 | RD/SCLK | ADC_SCLK | IN | 从此脚引线，标注精确网名`ADC_SCLK`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SCLK.2（2）；04_ADC/R_ADC_SAFE_SCLK.1（1）。 [完整端点N0444](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0444)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 13 | CS_N | ADC_CS_N | IN | 从此脚引线，标注精确网名`ADC_CS_N`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_CS_N.2（2）；04_ADC/R_ADC_SAFE_CS_N.1（1）。 [完整端点N0410](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0410)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 14 | BUSY | ADC_BUSY | OUT | 从此脚引线，标注精确网名`ADC_BUSY`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_ADC_RETURN_PD_BUSY.1（1）；04_ADC/U_BUSYBUF.2（A）。 [完整端点N0404](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0404)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 15 | FRSTDATA | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 16 | DB0 | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 17 | DB1 | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 18 | DB2 | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 19 | DB3/DOUTE | ADC_DOUTE | OUT | 从此脚引线，标注精确网名`ADC_DOUTE`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_E.1（1）；04_ADC/U_RET0.17（B5）。 [完整端点N0421](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0421)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 20 | DB4/DOUTF | ADC_DOUTF | OUT | 从此脚引线，标注精确网名`ADC_DOUTF`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_F.1（1）；04_ADC/U_RET0.16（B6）。 [完整端点N0423](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0423)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 21 | DB5/DOUTG | ADC_DOUTG | OUT | 从此脚引线，标注精确网名`ADC_DOUTG`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_G.1（1）；04_ADC/U_RET0.15（B7）。 [完整端点N0425](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0425)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 22 | DB6/DOUTH | ADC_DOUTH | OUT | 从此脚引线，标注精确网名`ADC_DOUTH`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_H.1（1）；04_ADC/U_RET0.14（B8）。 [完整端点N0427](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0427)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 23 | VDRIVE | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 24 | DB7/DOUTA | ADC_DOUTA | OUT | 从此脚引线，标注精确网名`ADC_DOUTA`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_DOUTA.1（1）；04_ADC/U_RET0.21（B1）。 [完整端点N0413](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0413)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 25 | DB8/DOUTB | ADC_DOUTB | OUT | 从此脚引线，标注精确网名`ADC_DOUTB`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_DOUTB.1（1）；04_ADC/U_RET0.20（B2）。 [完整端点N0415](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0415)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 26 | AGND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 27 | DB9/DOUTC | ADC_DOUTC | OUT | 从此脚引线，标注精确网名`ADC_DOUTC`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_DOUTC.1（1）；04_ADC/U_RET0.19（B3）。 [完整端点N0417](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0417)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 28 | DB10/DOUTD | ADC_DOUTD | OUT | 从此脚引线，标注精确网名`ADC_DOUTD`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_DOUTD.1（1）；04_ADC/U_RET0.18（B4）。 [完整端点N0419](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0419)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 29 | DB11/SDI | ADC_SDI | IN | 从此脚引线，标注精确网名`ADC_SDI`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SDI.2（2）；04_ADC/R_ADC_SAFE_SDI.1（1）。 [完整端点N0447](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0447)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 30 | DB12 | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 31 | DB13 | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 32 | DB14 | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 33 | DB15 | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 34 | REF_SELECT | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 35 | AGND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 36 | REGCAP | ADC_REGCAP36 | IN | 从此脚引线，标注精确网名`ADC_REGCAP36`；跨页使用同名板内标签。同网还接：04_ADC/C_REG36.1（1）。 [完整端点N0439](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0439)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 37 | AVCC | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 38 | AVCC | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 39 | REGCAP | ADC_REGCAP39 | IN | 从此脚引线，标注精确网名`ADC_REGCAP39`；跨页使用同名板内标签。同网还接：04_ADC/C_REG39.1（1）。 [完整端点N0440](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0440)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 40 | AGND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 41 | AGND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 42 | REFIN/REFOUT | ADC_REF25 | IN | 从此脚引线，标注精确网名`ADC_REF25`；跨页使用同名板内标签。同网还接：04_ADC/C_ADC_REF.1（1）。 [完整端点N0437](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0437)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 43 | REFGND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 44 | REFCAPA | ADC_REFCAP | IN | 从此脚引线，标注精确网名`ADC_REFCAP`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.45（REFCAPB）；04_ADC/C_ADC_REFCAP.1（1）。 [完整端点N0438](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0438)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 45 | REFCAPB | ADC_REFCAP | IN | 从此脚引线，标注精确网名`ADC_REFCAP`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.44（REFCAPA）；04_ADC/C_ADC_REFCAP.1（1）。 [完整端点N0438](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0438)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 46 | REFGND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 47 | AGND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 48 | AVCC | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 49 | V1+ | ADC_IN0 | IN | 从此脚引线，标注精确网名`ADC_IN0`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN0.2（2）；05_RX_INPUT/C_ADC_IN0.1（1）；05_RX_INPUT/R_ADC_BLEED0.1（1）。 [完整端点N0429](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0429)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 50 | V1- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 51 | V2+ | ADC_IN1 | IN | 从此脚引线，标注精确网名`ADC_IN1`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN1.2（2）；05_RX_INPUT/C_ADC_IN1.1（1）；05_RX_INPUT/R_ADC_BLEED1.1（1）。 [完整端点N0430](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0430)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 52 | V2- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 53 | V3+ | ADC_IN2 | IN | 从此脚引线，标注精确网名`ADC_IN2`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN2.2（2）；05_RX_INPUT/C_ADC_IN2.1（1）；05_RX_INPUT/R_ADC_BLEED2.1（1）。 [完整端点N0431](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0431)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 54 | V3- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 55 | V4+ | ADC_IN3 | IN | 从此脚引线，标注精确网名`ADC_IN3`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN3.2（2）；05_RX_INPUT/C_ADC_IN3.1（1）；05_RX_INPUT/R_ADC_BLEED3.1（1）。 [完整端点N0432](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0432)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 56 | V4- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 57 | V5+ | ADC_IN4 | IN | 从此脚引线，标注精确网名`ADC_IN4`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN4.2（2）；05_RX_INPUT/C_ADC_IN4.1（1）；05_RX_INPUT/R_ADC_BLEED4.1（1）。 [完整端点N0433](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0433)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 58 | V5- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 59 | V6+ | ADC_IN5 | IN | 从此脚引线，标注精确网名`ADC_IN5`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN5.2（2）；05_RX_INPUT/C_ADC_IN5.1（1）；05_RX_INPUT/R_ADC_BLEED5.1（1）。 [完整端点N0434](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0434)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 60 | V6- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 61 | V7+ | ADC_IN6 | IN | 从此脚引线，标注精确网名`ADC_IN6`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN6.2（2）；05_RX_INPUT/C_ADC_IN6.1（1）；05_RX_INPUT/R_ADC_BLEED6.1（1）。 [完整端点N0435](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0435)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 62 | V7- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 63 | V8+ | ADC_IN7 | IN | 从此脚引线，标注精确网名`ADC_IN7`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN7.2（2）；05_RX_INPUT/C_ADC_IN7.1（1）；05_RX_INPUT/R_ADC_BLEED7.1（1）。 [完整端点N0436](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0436)。 |
| CENTRAL | 04_ADC | U_ADC | AD7606C-16BSTZ | 64 | V8- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为U_ADC.1→V5A；U_ADC.2→GND；U_ADC.3→V5A；U_ADC.4→V5A；U_ADC.5→V5A；U_ADC.6→V5A；U_ADC.7→V5A；U_ADC.8→GND；U_ADC.10→V5A；U_ADC.16→GND；U_ADC.17→GND；U_ADC.18→GND；U_ADC.23→V5A；U_ADC.26→GND；U_ADC.30→GND；U_ADC.31→GND；U_ADC.32→GND；U_ADC.33→GND；U_ADC.34→V5A；U_ADC.35→GND；U_ADC.37→V5A；U_ADC.38→V5A；U_ADC.40→GND；U_ADC.41→GND；U_ADC.43→GND；U_ADC.46→GND；U_ADC.47→GND；U_ADC.48→V5A；U_ADC.50→GND；U_ADC.52→GND；U_ADC.54→GND；U_ADC.56→GND；U_ADC.58→GND；U_ADC.60→GND；U_ADC.62→GND；U_ADC.64→GND。 NC脚15逐个单独标记。

<a id="central-c-adc-av1"></a>

### 第002步：在CENTRAL／04_ADC放置 C_ADC_AV1

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_AV1**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_AV1 | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_ADC_AV1 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_AV1.1=`V5A`，C_ADC_AV1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-av37"></a>

### 第003步：在CENTRAL／04_ADC放置 C_ADC_AV37

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_AV37**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_AV37 | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_ADC_AV37 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_AV37.1=`V5A`，C_ADC_AV37.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-av38"></a>

### 第004步：在CENTRAL／04_ADC放置 C_ADC_AV38

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_AV38**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_AV38 | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_ADC_AV38 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_AV38.1=`V5A`，C_ADC_AV38.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-av48"></a>

### 第005步：在CENTRAL／04_ADC放置 C_ADC_AV48

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_AV48**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_AV48 | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_ADC_AV48 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_AV48.1=`V5A`，C_ADC_AV48.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-av-bulk"></a>

### 第006步：在CENTRAL／04_ADC放置 C_ADC_AV_BULK

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_AV_BULK**，精确型号 **C1210C106K3RACTU**，封装 **1210**。其值为 **10uF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_AV_BULK | C1210C106K3RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_ADC_AV_BULK | C1210C106K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_AV_BULK.1=`V5A`，C_ADC_AV_BULK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-d"></a>

### 第007步：在CENTRAL／04_ADC放置 C_ADC_D

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_D**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_D | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_ADC_D | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_D.1=`V5A`，C_ADC_D.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-d-bulk"></a>

### 第008步：在CENTRAL／04_ADC放置 C_ADC_D_BULK

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_D_BULK**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_D_BULK | C0603C105K3RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_ADC_D_BULK | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_D_BULK.1=`V5A`，C_ADC_D_BULK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-ref"></a>

### 第009步：在CENTRAL／04_ADC放置 C_ADC_REF

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_REF**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_REF | C0603C104K5RACTU | 1 | 1 | ADC_REF25 | PASSIVE | 从此脚引线，标注精确网名`ADC_REF25`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.42（REFIN/REFOUT）。 [完整端点N0437](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0437)。 |
| CENTRAL | 04_ADC | C_ADC_REF | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_REF.1=`ADC_REF25`，C_ADC_REF.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-refcap"></a>

### 第010步：在CENTRAL／04_ADC放置 C_ADC_REFCAP

在 **CENTRAL板的04_ADC图页**，接着放置 **C_ADC_REFCAP**，精确型号 **C1210C226K3RACTU**，封装 **1210**。其值为 **22uF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required; 25V X7R; effective>=10uF at4.4V。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_ADC_REFCAP | C1210C226K3RACTU | 1 | 1 | ADC_REFCAP | PASSIVE | 从此脚引线，标注精确网名`ADC_REFCAP`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.44（REFCAPA）；04_ADC/U_ADC.45（REFCAPB）。 [完整端点N0438](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0438)。 |
| CENTRAL | 04_ADC | C_ADC_REFCAP | C1210C226K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_REFCAP.1=`ADC_REFCAP`，C_ADC_REFCAP.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-reg36"></a>

### 第011步：在CENTRAL／04_ADC放置 C_REG36

在 **CENTRAL板的04_ADC图页**，接着放置 **C_REG36**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_REG36 | C0603C105K3RACTU | 1 | 1 | ADC_REGCAP36 | PASSIVE | 从此脚引线，标注精确网名`ADC_REGCAP36`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.36（REGCAP）。 [完整端点N0439](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0439)。 |
| CENTRAL | 04_ADC | C_REG36 | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_REG36.1=`ADC_REGCAP36`，C_REG36.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-reg39"></a>

### 第012步：在CENTRAL／04_ADC放置 C_REG39

在 **CENTRAL板的04_ADC图页**，接着放置 **C_REG39**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_ADC的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_REG39 | C0603C105K3RACTU | 1 | 1 | ADC_REGCAP39 | PASSIVE | 从此脚引线，标注精确网名`ADC_REGCAP39`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.39（REGCAP）。 [完整端点N0440](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0440)。 |
| CENTRAL | 04_ADC | C_REG39 | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_REG39.1=`ADC_REGCAP39`，C_REG39.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-adcbuf"></a>

### 第013步：在CENTRAL／04_ADC放置 U_ADCBUF

在 **CENTRAL板的04_ADC图页**，接着放置 **U_ADCBUF**，精确型号 **SN74AHCT244PWR**，封装 **PW/TSSOP20**。

放在ADC控制输入左侧；AHCT供电使用V5A，将3.3V控制送入ADC。不要把输出端直接回接AX引脚。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 1 | 1OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 2 | A0 | ADC_SCLK_FPGA | IN | 从此脚引线，标注精确网名`ADC_SCLK_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.33（EX_IO1_16N）；04_ADC/R_ADC_PD_SCLK.1（1）。 [完整端点N0446](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0446)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 3 | Y7 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 4 | A1 | ADC_CONVST_FPGA | IN | 从此脚引线，标注精确网名`ADC_CONVST_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.34（EX_IO1_16P）；04_ADC/R_ADC_PD_CONVST.1（1）。 [完整端点N0409](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0409)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 5 | Y6 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 6 | A2 | ADC_CS_N_FPGA | IN | 从此脚引线，标注精确网名`ADC_CS_N_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.35（EX_IO1_17N）；04_ADC/R_ADC_PU_CS_N.1（1）；04_ADC/R_ADC_OFF_CS_N.1（1）。 [完整端点N0412](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0412)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 7 | Y5 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 8 | A3 | ADC_SDI_FPGA | IN | 从此脚引线，标注精确网名`ADC_SDI_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.36（EX_IO1_17P）；04_ADC/R_ADC_PD_SDI.1（1）。 [完整端点N0449](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0449)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 9 | Y4 | ADC_RESET_B | OUT | 从此脚引线，标注精确网名`ADC_RESET_B`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RESET.1（1）。 [完整端点N0442](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0442)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 10 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 11 | A4 | ADC_RESET_FPGA | IN | 从此脚引线，标注精确网名`ADC_RESET_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.28（EX_IO2_13P）；04_ADC/R_ADC_PU_RESET.1（1）；04_ADC/R_ADC_OFF_RESET.1（1）。 [完整端点N0443](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0443)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 12 | Y3 | ADC_SDI_B | OUT | 从此脚引线，标注精确网名`ADC_SDI_B`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SDI.1（1）。 [完整端点N0448](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0448)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 13 | A5 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 14 | Y2 | ADC_CS_N_B | OUT | 从此脚引线，标注精确网名`ADC_CS_N_B`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_CS_N.1（1）。 [完整端点N0411](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0411)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 15 | A6 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 16 | Y1 | ADC_CONVST_B | OUT | 从此脚引线，标注精确网名`ADC_CONVST_B`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_CONVST.1（1）。 [完整端点N0408](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0408)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 17 | A7 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 18 | Y0 | ADC_SCLK_B | OUT | 从此脚引线，标注精确网名`ADC_SCLK_B`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SCLK.1（1）。 [完整端点N0445](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0445)。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 19 | 2OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_ADCBUF | SN74AHCT244PWR | 20 | VCC | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |

接完确认：电源/地/参考为U_ADCBUF.1→GND；U_ADCBUF.19→GND；U_ADCBUF.10→GND；U_ADCBUF.20→V5A；U_ADCBUF.13→GND；U_ADCBUF.15→GND；U_ADCBUF.17→GND。 NC脚7,5,3逐个单独标记。

<a id="central-c-u-adcbuf"></a>

### 第014步：在CENTRAL／04_ADC放置 C_U_ADCBUF

在 **CENTRAL板的04_ADC图页**，接着放置 **C_U_ADCBUF**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_U_ADCBUF | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_U_ADCBUF | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_ADCBUF.1=`V5A`，C_U_ADCBUF.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-convst"></a>

### 第015步：在CENTRAL／04_ADC放置 R_ADC_CONVST

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_CONVST**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_CONVST | CRCW060333R0FKEA | 1 | 1 | ADC_CONVST_B | PASSIVE | 从此脚引线，标注精确网名`ADC_CONVST_B`；跨页使用同名板内标签。同网还接：04_ADC/U_ADCBUF.16（Y1）。 [完整端点N0408](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0408)。 |
| CENTRAL | 04_ADC | R_ADC_CONVST | CRCW060333R0FKEA | 2 | 2 | ADC_CONVST | PASSIVE | 从此脚引线，标注精确网名`ADC_CONVST`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SAFE_CONVST.1（1）；04_ADC/U_ADC.9（CONVST）。 [完整端点N0407](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0407)。 |

接完确认：R_ADC_CONVST.1=`ADC_CONVST_B`，R_ADC_CONVST.2=`ADC_CONVST`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-cs-n"></a>

### 第016步：在CENTRAL／04_ADC放置 R_ADC_CS_N

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_CS_N**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_CS_N | CRCW060333R0FKEA | 1 | 1 | ADC_CS_N_B | PASSIVE | 从此脚引线，标注精确网名`ADC_CS_N_B`；跨页使用同名板内标签。同网还接：04_ADC/U_ADCBUF.14（Y2）。 [完整端点N0411](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0411)。 |
| CENTRAL | 04_ADC | R_ADC_CS_N | CRCW060333R0FKEA | 2 | 2 | ADC_CS_N | PASSIVE | 从此脚引线，标注精确网名`ADC_CS_N`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SAFE_CS_N.1（1）；04_ADC/U_ADC.13（CS_N）。 [完整端点N0410](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0410)。 |

接完确认：R_ADC_CS_N.1=`ADC_CS_N_B`，R_ADC_CS_N.2=`ADC_CS_N`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-off-cs-n"></a>

### 第017步：在CENTRAL／04_ADC放置 R_ADC_OFF_CS_N

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_OFF_CS_N**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_OFF_CS_N | CRCW0603100KFKEA | 1 | 1 | ADC_CS_N_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_CS_N_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.35（EX_IO1_17N）；04_ADC/U_ADCBUF.6（A2）；04_ADC/R_ADC_PU_CS_N.1（1）。 [完整端点N0412](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0412)。 |
| CENTRAL | 04_ADC | R_ADC_OFF_CS_N | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_OFF_CS_N.1=`ADC_CS_N_FPGA`，R_ADC_OFF_CS_N.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-off-reset"></a>

### 第018步：在CENTRAL／04_ADC放置 R_ADC_OFF_RESET

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_OFF_RESET**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_OFF_RESET | CRCW0603100KFKEA | 1 | 1 | ADC_RESET_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_RESET_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.28（EX_IO2_13P）；04_ADC/U_ADCBUF.11（A4）；04_ADC/R_ADC_PU_RESET.1（1）。 [完整端点N0443](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0443)。 |
| CENTRAL | 04_ADC | R_ADC_OFF_RESET | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_OFF_RESET.1=`ADC_RESET_FPGA`，R_ADC_OFF_RESET.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-pd-convst"></a>

### 第019步：在CENTRAL／04_ADC放置 R_ADC_PD_CONVST

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_PD_CONVST**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_PD_CONVST | CRCW060310K0FKEA | 1 | 1 | ADC_CONVST_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_CONVST_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.34（EX_IO1_16P）；04_ADC/U_ADCBUF.4（A1）。 [完整端点N0409](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0409)。 |
| CENTRAL | 04_ADC | R_ADC_PD_CONVST | CRCW060310K0FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_PD_CONVST.1=`ADC_CONVST_FPGA`，R_ADC_PD_CONVST.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-pd-sclk"></a>

### 第020步：在CENTRAL／04_ADC放置 R_ADC_PD_SCLK

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_PD_SCLK**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_PD_SCLK | CRCW060310K0FKEA | 1 | 1 | ADC_SCLK_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_SCLK_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.33（EX_IO1_16N）；04_ADC/U_ADCBUF.2（A0）。 [完整端点N0446](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0446)。 |
| CENTRAL | 04_ADC | R_ADC_PD_SCLK | CRCW060310K0FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_PD_SCLK.1=`ADC_SCLK_FPGA`，R_ADC_PD_SCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-pd-sdi"></a>

### 第021步：在CENTRAL／04_ADC放置 R_ADC_PD_SDI

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_PD_SDI**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_PD_SDI | CRCW060310K0FKEA | 1 | 1 | ADC_SDI_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_SDI_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.36（EX_IO1_17P）；04_ADC/U_ADCBUF.8（A3）。 [完整端点N0449](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0449)。 |
| CENTRAL | 04_ADC | R_ADC_PD_SDI | CRCW060310K0FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_PD_SDI.1=`ADC_SDI_FPGA`，R_ADC_PD_SDI.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-pu-cs-n"></a>

### 第022步：在CENTRAL／04_ADC放置 R_ADC_PU_CS_N

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_PU_CS_N**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_PU_CS_N | CRCW060310K0FKEA | 1 | 1 | ADC_CS_N_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_CS_N_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.35（EX_IO1_17N）；04_ADC/U_ADCBUF.6（A2）；04_ADC/R_ADC_OFF_CS_N.1（1）。 [完整端点N0412](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0412)。 |
| CENTRAL | 04_ADC | R_ADC_PU_CS_N | CRCW060310K0FKEA | 2 | 2 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |

接完确认：R_ADC_PU_CS_N.1=`ADC_CS_N_FPGA`，R_ADC_PU_CS_N.2=`AX_VIO_REF3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-pu-reset"></a>

### 第023步：在CENTRAL／04_ADC放置 R_ADC_PU_RESET

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_PU_RESET**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_PU_RESET | CRCW060310K0FKEA | 1 | 1 | ADC_RESET_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_RESET_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.28（EX_IO2_13P）；04_ADC/U_ADCBUF.11（A4）；04_ADC/R_ADC_OFF_RESET.1（1）。 [完整端点N0443](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0443)。 |
| CENTRAL | 04_ADC | R_ADC_PU_RESET | CRCW060310K0FKEA | 2 | 2 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |

接完确认：R_ADC_PU_RESET.1=`ADC_RESET_FPGA`，R_ADC_PU_RESET.2=`AX_VIO_REF3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-reset"></a>

### 第024步：在CENTRAL／04_ADC放置 R_ADC_RESET

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RESET**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RESET | CRCW060333R0FKEA | 1 | 1 | ADC_RESET_B | PASSIVE | 从此脚引线，标注精确网名`ADC_RESET_B`；跨页使用同名板内标签。同网还接：04_ADC/U_ADCBUF.9（Y4）。 [完整端点N0442](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0442)。 |
| CENTRAL | 04_ADC | R_ADC_RESET | CRCW060333R0FKEA | 2 | 2 | ADC_RESET | PASSIVE | 从此脚引线，标注精确网名`ADC_RESET`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SAFE_RESET.1（1）；04_ADC/U_ADC.11（RESET）。 [完整端点N0441](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0441)。 |

接完确认：R_ADC_RESET.1=`ADC_RESET_B`，R_ADC_RESET.2=`ADC_RESET`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-safe-convst"></a>

### 第025步：在CENTRAL／04_ADC放置 R_ADC_SAFE_CONVST

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_SAFE_CONVST**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_SAFE_CONVST | CRCW060310K0FKEA | 1 | 1 | ADC_CONVST | PASSIVE | 从此脚引线，标注精确网名`ADC_CONVST`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_CONVST.2（2）；04_ADC/U_ADC.9（CONVST）。 [完整端点N0407](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0407)。 |
| CENTRAL | 04_ADC | R_ADC_SAFE_CONVST | CRCW060310K0FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_SAFE_CONVST.1=`ADC_CONVST`，R_ADC_SAFE_CONVST.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-safe-cs-n"></a>

### 第026步：在CENTRAL／04_ADC放置 R_ADC_SAFE_CS_N

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_SAFE_CS_N**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_SAFE_CS_N | CRCW060310K0FKEA | 1 | 1 | ADC_CS_N | PASSIVE | 从此脚引线，标注精确网名`ADC_CS_N`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_CS_N.2（2）；04_ADC/U_ADC.13（CS_N）。 [完整端点N0410](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0410)。 |
| CENTRAL | 04_ADC | R_ADC_SAFE_CS_N | CRCW060310K0FKEA | 2 | 2 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |

接完确认：R_ADC_SAFE_CS_N.1=`ADC_CS_N`，R_ADC_SAFE_CS_N.2=`V5A`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-safe-reset"></a>

### 第027步：在CENTRAL／04_ADC放置 R_ADC_SAFE_RESET

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_SAFE_RESET**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_SAFE_RESET | CRCW060310K0FKEA | 1 | 1 | ADC_RESET | PASSIVE | 从此脚引线，标注精确网名`ADC_RESET`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RESET.2（2）；04_ADC/U_ADC.11（RESET）。 [完整端点N0441](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0441)。 |
| CENTRAL | 04_ADC | R_ADC_SAFE_RESET | CRCW060310K0FKEA | 2 | 2 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |

接完确认：R_ADC_SAFE_RESET.1=`ADC_RESET`，R_ADC_SAFE_RESET.2=`V5A`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-safe-sclk"></a>

### 第028步：在CENTRAL／04_ADC放置 R_ADC_SAFE_SCLK

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_SAFE_SCLK**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_SAFE_SCLK | CRCW060310K0FKEA | 1 | 1 | ADC_SCLK | PASSIVE | 从此脚引线，标注精确网名`ADC_SCLK`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SCLK.2（2）；04_ADC/U_ADC.12（RD/SCLK）。 [完整端点N0444](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0444)。 |
| CENTRAL | 04_ADC | R_ADC_SAFE_SCLK | CRCW060310K0FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_SAFE_SCLK.1=`ADC_SCLK`，R_ADC_SAFE_SCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-safe-sdi"></a>

### 第029步：在CENTRAL／04_ADC放置 R_ADC_SAFE_SDI

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_SAFE_SDI**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_SAFE_SDI | CRCW060310K0FKEA | 1 | 1 | ADC_SDI | PASSIVE | 从此脚引线，标注精确网名`ADC_SDI`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SDI.2（2）；04_ADC/U_ADC.29（DB11/SDI）。 [完整端点N0447](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0447)。 |
| CENTRAL | 04_ADC | R_ADC_SAFE_SDI | CRCW060310K0FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_SAFE_SDI.1=`ADC_SDI`，R_ADC_SAFE_SDI.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-sclk"></a>

### 第030步：在CENTRAL／04_ADC放置 R_ADC_SCLK

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_SCLK**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_SCLK | CRCW060333R0FKEA | 1 | 1 | ADC_SCLK_B | PASSIVE | 从此脚引线，标注精确网名`ADC_SCLK_B`；跨页使用同名板内标签。同网还接：04_ADC/U_ADCBUF.18（Y0）。 [完整端点N0445](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0445)。 |
| CENTRAL | 04_ADC | R_ADC_SCLK | CRCW060333R0FKEA | 2 | 2 | ADC_SCLK | PASSIVE | 从此脚引线，标注精确网名`ADC_SCLK`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SAFE_SCLK.1（1）；04_ADC/U_ADC.12（RD/SCLK）。 [完整端点N0444](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0444)。 |

接完确认：R_ADC_SCLK.1=`ADC_SCLK_B`，R_ADC_SCLK.2=`ADC_SCLK`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-sdi"></a>

### 第031步：在CENTRAL／04_ADC放置 R_ADC_SDI

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_SDI**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_ADCBUF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_SDI | CRCW060333R0FKEA | 1 | 1 | ADC_SDI_B | PASSIVE | 从此脚引线，标注精确网名`ADC_SDI_B`；跨页使用同名板内标签。同网还接：04_ADC/U_ADCBUF.12（Y3）。 [完整端点N0448](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0448)。 |
| CENTRAL | 04_ADC | R_ADC_SDI | CRCW060333R0FKEA | 2 | 2 | ADC_SDI | PASSIVE | 从此脚引线，标注精确网名`ADC_SDI`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_SAFE_SDI.1（1）；04_ADC/U_ADC.29（DB11/SDI）。 [完整端点N0447](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0447)。 |

接完确认：R_ADC_SDI.1=`ADC_SDI_B`，R_ADC_SDI.2=`ADC_SDI`；不可旁路该器件把两个网名短在一起。

<a id="central-u-ret0"></a>

### 第032步：在CENTRAL／04_ADC放置 U_RET0

在 **CENTRAL板的04_ADC图页**，接着放置 **U_RET0**，精确型号 **SN74LVC8T245PWR**，封装 **PW/TSSOP24**。

放在ADC八路输出与FPGA接口之间；VCCA使用AX_VIO_REF3V3，VCCB使用V5A，DIR与OE_N按表。未用输入和输出也逐脚处理。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 1 | VCCA | AX_VIO_REF3V3 | POWER | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 2 | DIR | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 3 | A1 | ADC_DOUTA_FPGA | OUT | 从此脚引线，标注精确网名`ADC_DOUTA_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.28（EX_IO1_13P）；04_ADC/R_RETURN_PD_U_RET0_3.1（1）。 [完整端点N0414](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0414)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 4 | A2 | ADC_DOUTB_FPGA | OUT | 从此脚引线，标注精确网名`ADC_DOUTB_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.29（EX_IO1_14N）；04_ADC/R_RETURN_PD_U_RET0_4.1（1）。 [完整端点N0416](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0416)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 5 | A3 | ADC_DOUTC_FPGA | OUT | 从此脚引线，标注精确网名`ADC_DOUTC_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.30（EX_IO1_14P）；04_ADC/R_RETURN_PD_U_RET0_5.1（1）。 [完整端点N0418](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0418)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 6 | A4 | ADC_DOUTD_FPGA | OUT | 从此脚引线，标注精确网名`ADC_DOUTD_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.31（EX_IO1_15N）；04_ADC/R_RETURN_PD_U_RET0_6.1（1）。 [完整端点N0420](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0420)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 7 | A5 | ADC_DOUTE_FPGA | OUT | 从此脚引线，标注精确网名`ADC_DOUTE_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.32（ADC_DOUTE）；04_ADC/R_RETURN_PD_U_RET0_7.1（1）。 [完整端点N0422](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0422)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 8 | A6 | ADC_DOUTF_FPGA | OUT | 从此脚引线，标注精确网名`ADC_DOUTF_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.33（ADC_DOUTF）；04_ADC/R_RETURN_PD_U_RET0_8.1（1）。 [完整端点N0424](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0424)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 9 | A7 | ADC_DOUTG_FPGA | OUT | 从此脚引线，标注精确网名`ADC_DOUTG_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.34（ADC_DOUTG）；04_ADC/R_RETURN_PD_U_RET0_9.1（1）。 [完整端点N0426](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0426)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 10 | A8 | ADC_DOUTH_FPGA | OUT | 从此脚引线，标注精确网名`ADC_DOUTH_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.35（ADC_DOUTH）；04_ADC/R_RETURN_PD_U_RET0_10.1（1）。 [完整端点N0428](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0428)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 11 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 12 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 13 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 14 | B8 | ADC_DOUTH | IN | 从此脚引线，标注精确网名`ADC_DOUTH`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.22（DB6/DOUTH）；04_ADC/R_ADC_RETURN_PD_H.1（1）。 [完整端点N0427](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0427)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 15 | B7 | ADC_DOUTG | IN | 从此脚引线，标注精确网名`ADC_DOUTG`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.21（DB5/DOUTG）；04_ADC/R_ADC_RETURN_PD_G.1（1）。 [完整端点N0425](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0425)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 16 | B6 | ADC_DOUTF | IN | 从此脚引线，标注精确网名`ADC_DOUTF`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.20（DB4/DOUTF）；04_ADC/R_ADC_RETURN_PD_F.1（1）。 [完整端点N0423](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0423)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 17 | B5 | ADC_DOUTE | IN | 从此脚引线，标注精确网名`ADC_DOUTE`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.19（DB3/DOUTE）；04_ADC/R_ADC_RETURN_PD_E.1（1）。 [完整端点N0421](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0421)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 18 | B4 | ADC_DOUTD | IN | 从此脚引线，标注精确网名`ADC_DOUTD`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_DOUTD.1（1）；04_ADC/U_ADC.28（DB10/DOUTD）。 [完整端点N0419](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0419)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 19 | B3 | ADC_DOUTC | IN | 从此脚引线，标注精确网名`ADC_DOUTC`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_DOUTC.1（1）；04_ADC/U_ADC.27（DB9/DOUTC）。 [完整端点N0417](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0417)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 20 | B2 | ADC_DOUTB | IN | 从此脚引线，标注精确网名`ADC_DOUTB`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_DOUTB.1（1）；04_ADC/U_ADC.25（DB8/DOUTB）。 [完整端点N0415](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0415)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 21 | B1 | ADC_DOUTA | IN | 从此脚引线，标注精确网名`ADC_DOUTA`；跨页使用同名板内标签。同网还接：04_ADC/R_ADC_RETURN_PD_DOUTA.1（1）；04_ADC/U_ADC.24（DB7/DOUTA）。 [完整端点N0413](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0413)。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 22 | OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 23 | VCCB | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | U_RET0 | SN74LVC8T245PWR | 24 | VCCB | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |

接完确认：电源/地/参考为U_RET0.1→AX_VIO_REF3V3；U_RET0.2→GND；U_RET0.11→GND；U_RET0.12→GND；U_RET0.13→GND；U_RET0.22→GND；U_RET0.23→V5A；U_RET0.24→V5A。

<a id="central-c-u-ret0-a"></a>

### 第033步：在CENTRAL／04_ADC放置 C_U_RET0_A

在 **CENTRAL板的04_ADC图页**，接着放置 **C_U_RET0_A**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_U_RET0_A | C0603C104K5RACTU | 1 | 1 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |
| CENTRAL | 04_ADC | C_U_RET0_A | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RET0_A.1=`AX_VIO_REF3V3`，C_U_RET0_A.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-u-ret0-b"></a>

### 第034步：在CENTRAL／04_ADC放置 C_U_RET0_B

在 **CENTRAL板的04_ADC图页**，接着放置 **C_U_RET0_B**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_U_RET0_B | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 04_ADC | C_U_RET0_B | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RET0_B.1=`V5A`，C_U_RET0_B.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-douta"></a>

### 第035步：在CENTRAL／04_ADC放置 R_ADC_RETURN_PD_DOUTA

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RETURN_PD_DOUTA**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_DOUTA | CRCW0603100KFKEA | 1 | 1 | ADC_DOUTA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTA`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.24（DB7/DOUTA）；04_ADC/U_RET0.21（B1）。 [完整端点N0413](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0413)。 |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_DOUTA | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_DOUTA.1=`ADC_DOUTA`，R_ADC_RETURN_PD_DOUTA.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-doutb"></a>

### 第036步：在CENTRAL／04_ADC放置 R_ADC_RETURN_PD_DOUTB

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RETURN_PD_DOUTB**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_DOUTB | CRCW0603100KFKEA | 1 | 1 | ADC_DOUTB | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTB`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.25（DB8/DOUTB）；04_ADC/U_RET0.20（B2）。 [完整端点N0415](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0415)。 |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_DOUTB | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_DOUTB.1=`ADC_DOUTB`，R_ADC_RETURN_PD_DOUTB.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-doutc"></a>

### 第037步：在CENTRAL／04_ADC放置 R_ADC_RETURN_PD_DOUTC

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RETURN_PD_DOUTC**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_DOUTC | CRCW0603100KFKEA | 1 | 1 | ADC_DOUTC | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTC`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.27（DB9/DOUTC）；04_ADC/U_RET0.19（B3）。 [完整端点N0417](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0417)。 |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_DOUTC | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_DOUTC.1=`ADC_DOUTC`，R_ADC_RETURN_PD_DOUTC.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-doutd"></a>

### 第038步：在CENTRAL／04_ADC放置 R_ADC_RETURN_PD_DOUTD

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RETURN_PD_DOUTD**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_DOUTD | CRCW0603100KFKEA | 1 | 1 | ADC_DOUTD | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTD`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.28（DB10/DOUTD）；04_ADC/U_RET0.18（B4）。 [完整端点N0419](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0419)。 |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_DOUTD | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_DOUTD.1=`ADC_DOUTD`，R_ADC_RETURN_PD_DOUTD.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-e"></a>

### 第039步：在CENTRAL／04_ADC放置 R_ADC_RETURN_PD_E

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RETURN_PD_E**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_E | CRCW0603100KFKEA | 1 | 1 | ADC_DOUTE | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTE`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.19（DB3/DOUTE）；04_ADC/U_RET0.17（B5）。 [完整端点N0421](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0421)。 |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_E | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_E.1=`ADC_DOUTE`，R_ADC_RETURN_PD_E.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-f"></a>

### 第040步：在CENTRAL／04_ADC放置 R_ADC_RETURN_PD_F

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RETURN_PD_F**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_F | CRCW0603100KFKEA | 1 | 1 | ADC_DOUTF | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTF`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.20（DB4/DOUTF）；04_ADC/U_RET0.16（B6）。 [完整端点N0423](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0423)。 |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_F | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_F.1=`ADC_DOUTF`，R_ADC_RETURN_PD_F.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-g"></a>

### 第041步：在CENTRAL／04_ADC放置 R_ADC_RETURN_PD_G

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RETURN_PD_G**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_G | CRCW0603100KFKEA | 1 | 1 | ADC_DOUTG | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTG`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.21（DB5/DOUTG）；04_ADC/U_RET0.15（B7）。 [完整端点N0425](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0425)。 |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_G | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_G.1=`ADC_DOUTG`，R_ADC_RETURN_PD_G.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-h"></a>

### 第042步：在CENTRAL／04_ADC放置 R_ADC_RETURN_PD_H

在 **CENTRAL板的04_ADC图页**，接着放置 **R_ADC_RETURN_PD_H**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_H | CRCW0603100KFKEA | 1 | 1 | ADC_DOUTH | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTH`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.22（DB6/DOUTH）；04_ADC/U_RET0.14（B8）。 [完整端点N0427](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0427)。 |
| CENTRAL | 04_ADC | R_ADC_RETURN_PD_H | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_H.1=`ADC_DOUTH`，R_ADC_RETURN_PD_H.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret0-3"></a>

### 第043步：在CENTRAL／04_ADC放置 R_RETURN_PD_U_RET0_3

在 **CENTRAL板的04_ADC图页**，接着放置 **R_RETURN_PD_U_RET0_3**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_3 | RC0603FR-0710KL | 1 | 1 | ADC_DOUTA_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTA_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.28（EX_IO1_13P）；04_ADC/U_RET0.3（A1）。 [完整端点N0414](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0414)。 |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_3 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET0_3.1=`ADC_DOUTA_FPGA`，R_RETURN_PD_U_RET0_3.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret0-4"></a>

### 第044步：在CENTRAL／04_ADC放置 R_RETURN_PD_U_RET0_4

在 **CENTRAL板的04_ADC图页**，接着放置 **R_RETURN_PD_U_RET0_4**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_4 | RC0603FR-0710KL | 1 | 1 | ADC_DOUTB_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTB_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.29（EX_IO1_14N）；04_ADC/U_RET0.4（A2）。 [完整端点N0416](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0416)。 |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_4 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET0_4.1=`ADC_DOUTB_FPGA`，R_RETURN_PD_U_RET0_4.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret0-5"></a>

### 第045步：在CENTRAL／04_ADC放置 R_RETURN_PD_U_RET0_5

在 **CENTRAL板的04_ADC图页**，接着放置 **R_RETURN_PD_U_RET0_5**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_5 | RC0603FR-0710KL | 1 | 1 | ADC_DOUTC_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTC_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.30（EX_IO1_14P）；04_ADC/U_RET0.5（A3）。 [完整端点N0418](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0418)。 |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_5 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET0_5.1=`ADC_DOUTC_FPGA`，R_RETURN_PD_U_RET0_5.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret0-6"></a>

### 第046步：在CENTRAL／04_ADC放置 R_RETURN_PD_U_RET0_6

在 **CENTRAL板的04_ADC图页**，接着放置 **R_RETURN_PD_U_RET0_6**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_6 | RC0603FR-0710KL | 1 | 1 | ADC_DOUTD_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTD_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.31（EX_IO1_15N）；04_ADC/U_RET0.6（A4）。 [完整端点N0420](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0420)。 |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_6 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET0_6.1=`ADC_DOUTD_FPGA`，R_RETURN_PD_U_RET0_6.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret0-7"></a>

### 第047步：在CENTRAL／04_ADC放置 R_RETURN_PD_U_RET0_7

在 **CENTRAL板的04_ADC图页**，接着放置 **R_RETURN_PD_U_RET0_7**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_7 | RC0603FR-0710KL | 1 | 1 | ADC_DOUTE_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTE_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.32（ADC_DOUTE）；04_ADC/U_RET0.7（A5）。 [完整端点N0422](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0422)。 |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_7 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET0_7.1=`ADC_DOUTE_FPGA`，R_RETURN_PD_U_RET0_7.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret0-8"></a>

### 第048步：在CENTRAL／04_ADC放置 R_RETURN_PD_U_RET0_8

在 **CENTRAL板的04_ADC图页**，接着放置 **R_RETURN_PD_U_RET0_8**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_8 | RC0603FR-0710KL | 1 | 1 | ADC_DOUTF_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTF_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.33（ADC_DOUTF）；04_ADC/U_RET0.8（A6）。 [完整端点N0424](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0424)。 |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_8 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET0_8.1=`ADC_DOUTF_FPGA`，R_RETURN_PD_U_RET0_8.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret0-9"></a>

### 第049步：在CENTRAL／04_ADC放置 R_RETURN_PD_U_RET0_9

在 **CENTRAL板的04_ADC图页**，接着放置 **R_RETURN_PD_U_RET0_9**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_9 | RC0603FR-0710KL | 1 | 1 | ADC_DOUTG_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTG_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.34（ADC_DOUTG）；04_ADC/U_RET0.9（A7）。 [完整端点N0426](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0426)。 |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_9 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET0_9.1=`ADC_DOUTG_FPGA`，R_RETURN_PD_U_RET0_9.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret0-10"></a>

### 第050步：在CENTRAL／04_ADC放置 R_RETURN_PD_U_RET0_10

在 **CENTRAL板的04_ADC图页**，接着放置 **R_RETURN_PD_U_RET0_10**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_10 | RC0603FR-0710KL | 1 | 1 | ADC_DOUTH_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_DOUTH_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.35（ADC_DOUTH）；04_ADC/U_RET0.10（A8）。 [完整端点N0428](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0428)。 |
| CENTRAL | 04_ADC | R_RETURN_PD_U_RET0_10 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET0_10.1=`ADC_DOUTH_FPGA`，R_RETURN_PD_U_RET0_10.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-busybuf"></a>

### 第051步：在CENTRAL／04_ADC放置 U_BUSYBUF

在 **CENTRAL板的04_ADC图页**，接着放置 **U_BUSYBUF**，精确型号 **SN74LVC1G125DBVR**，封装 **DBV/SOT23-5**。

放在ADC BUSY与返回翻译器之间，V5A侧输入、本地3.3V输出网络按表。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | U_BUSYBUF | SN74LVC1G125DBVR | 1 | OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_BUSYBUF | SN74LVC1G125DBVR | 2 | A | ADC_BUSY | IN | 从此脚引线，标注精确网名`ADC_BUSY`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_ADC_RETURN_PD_BUSY.1（1）；04_ADC/U_ADC.14（BUSY）。 [完整端点N0404](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0404)。 |
| CENTRAL | 04_ADC | U_BUSYBUF | SN74LVC1G125DBVR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 04_ADC | U_BUSYBUF | SN74LVC1G125DBVR | 4 | Y | ADC_BUSY_3V3 | OUT | 从此脚引线，标注精确网名`ADC_BUSY_3V3`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_RET1.16（B6）。 [完整端点N0405](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0405)。 |
| CENTRAL | 04_ADC | U_BUSYBUF | SN74LVC1G125DBVR | 5 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_BUSYBUF.1→GND；U_BUSYBUF.3→GND；U_BUSYBUF.5→V3V3。

<a id="central-c-u-busybuf"></a>

### 第052步：在CENTRAL／04_ADC放置 C_U_BUSYBUF

在 **CENTRAL板的04_ADC图页**，接着放置 **C_U_BUSYBUF**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_BUSYBUF的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 04_ADC | C_U_BUSYBUF | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 04_ADC | C_U_BUSYBUF | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_BUSYBUF.1=`V3V3`，C_U_BUSYBUF.2=`GND`；不可旁路该器件把两个网名短在一起。

本页完成核对：**52个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。
