# ARRAY／04_RX逐步连接分册

本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。

<a id="page-array-04-rx"></a>

## ARRAY板／04_RX图页

先生成本板VBIAS25，再放四运放及RX0–3四路。每路从接收器进入限流/隔直/钳位/偏置/反馈网络，输出到J_LINK对应RX针。

<a id="array-u-bias"></a>

### 第001步：在ARRAY／04_RX放置 U_BIAS

在 **ARRAY板的04_RX图页**，先放置 **U_BIAS**，精确型号 **REF3025AIDBZR**，封装 **DBZ/SOT23-3**。

在ARRAY/04_RX左侧放REF3025，给本阵列产生VBIAS25；输入/输出各自退耦，不能跨阵列并联偏置源。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | U_BIAS | REF3025AIDBZR | 1 | IN | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 04_RX | U_BIAS | REF3025AIDBZR | 2 | OUT | VBIAS25 | OUT | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_BIAS0.2（2）；04_RX/R_RX_GAIN0.2（2）。 |
| ARRAY | 04_RX | U_BIAS | REF3025AIDBZR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为U_BIAS.1→V3V3；U_BIAS.2→VBIAS25；U_BIAS.3→GND。

<a id="array-c-bias-in"></a>

### 第002步：在ARRAY／04_RX放置 C_BIAS_IN

在 **ARRAY板的04_RX图页**，接着放置 **C_BIAS_IN**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_BIAS的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | C_BIAS_IN | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 04_RX | C_BIAS_IN | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_BIAS_IN.1=`V3V3`，C_BIAS_IN.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-c-bias-out"></a>

### 第003步：在ARRAY／04_RX放置 C_BIAS_OUT

在 **ARRAY板的04_RX图页**，接着放置 **C_BIAS_OUT**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_BIAS的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | C_BIAS_OUT | C0603C105K3RACTU | 1 | 1 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/R_RX_BIAS0.2（2）；04_RX/R_RX_GAIN0.2（2）。 |
| ARRAY | 04_RX | C_BIAS_OUT | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_BIAS_OUT.1=`VBIAS25`，C_BIAS_OUT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-rx"></a>

### 第004步：在ARRAY／04_RX放置 U_RX

在 **ARRAY板的04_RX图页**，接着放置 **U_RX**，精确型号 **OPA4192IPWR**，封装 **PW/TSSOP14**。

在ARRAY/04_RX中部放四运放；四路IN+/IN−/OUT逐脚对应四个RX通道。反馈电阻跨OUT与IN−，不是串到GND；V+接V5A，V−接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 1 | OUT0 | RX0 | ANALOG_OUT | 从此脚引线，标注精确网名`RX0`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.55（RX0）；04_RX/R_RX_FB0.1（1）；04_RX/R_RX_BLEED0.1（1）。 [完整端点N0087](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0087)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 2 | -IN0 | RX_FB0 | IN | 从此脚引线，标注精确网名`RX_FB0`；跨页使用同名板内标签。同网还接：04_RX/R_RX_GAIN0.1（1）；04_RX/R_RX_FB0.2（2）。 [完整端点N0096](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0096)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 3 | +IN0 | RX_BIAS0 | IN | 从此脚引线，标注精确网名`RX_BIAS0`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC0.2（2）；04_RX/R_RX_BIAS0.1（1）；04_RX/D_RX0.3（K1/A2）。 [完整端点N0091](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0091)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 4 | V+ | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有11个物理端点，逐个见[完整端点N0391](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0391)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 5 | +IN1 | RX_BIAS1 | IN | 从此脚引线，标注精确网名`RX_BIAS1`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC1.2（2）；04_RX/R_RX_BIAS1.1（1）；04_RX/D_RX1.3（K1/A2）。 [完整端点N0092](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0092)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 6 | -IN1 | RX_FB1 | IN | 从此脚引线，标注精确网名`RX_FB1`；跨页使用同名板内标签。同网还接：04_RX/R_RX_GAIN1.1（1）；04_RX/R_RX_FB1.2（2）。 [完整端点N0097](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0097)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 7 | OUT1 | RX1 | ANALOG_OUT | 从此脚引线，标注精确网名`RX1`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.57（RX1）；04_RX/R_RX_FB1.1（1）；04_RX/R_RX_BLEED1.1（1）。 [完整端点N0088](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0088)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 8 | OUT2 | RX2 | ANALOG_OUT | 从此脚引线，标注精确网名`RX2`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.59（RX2）；04_RX/R_RX_FB2.1（1）；04_RX/R_RX_BLEED2.1（1）。 [完整端点N0089](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0089)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 9 | -IN2 | RX_FB2 | IN | 从此脚引线，标注精确网名`RX_FB2`；跨页使用同名板内标签。同网还接：04_RX/R_RX_GAIN2.1（1）；04_RX/R_RX_FB2.2（2）。 [完整端点N0098](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0098)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 10 | +IN2 | RX_BIAS2 | IN | 从此脚引线，标注精确网名`RX_BIAS2`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC2.2（2）；04_RX/R_RX_BIAS2.1（1）；04_RX/D_RX2.3（K1/A2）。 [完整端点N0093](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0093)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 11 | V- | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 12 | +IN3 | RX_BIAS3 | IN | 从此脚引线，标注精确网名`RX_BIAS3`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC3.2（2）；04_RX/R_RX_BIAS3.1（1）；04_RX/D_RX3.3（K1/A2）。 [完整端点N0094](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0094)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 13 | -IN3 | RX_FB3 | IN | 从此脚引线，标注精确网名`RX_FB3`；跨页使用同名板内标签。同网还接：04_RX/R_RX_GAIN3.1（1）；04_RX/R_RX_FB3.2（2）。 [完整端点N0099](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0099)。 |
| ARRAY | 04_RX | U_RX | OPA4192IPWR | 14 | OUT3 | RX3 | ANALOG_OUT | 从此脚引线，标注精确网名`RX3`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.61（RX3）；04_RX/R_RX_FB3.1（1）；04_RX/R_RX_BLEED3.1（1）。 [完整端点N0090](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0090)。 |

接完确认：电源/地/参考为U_RX.4→V5A；U_RX.11→GND。

<a id="array-c-u-rx"></a>

### 第005步：在ARRAY／04_RX放置 C_U_RX

在 **ARRAY板的04_RX图页**，接着放置 **C_U_RX**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RX的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | C_U_RX | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有11个物理端点，逐个见[完整端点N0391](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0391)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| ARRAY | 04_RX | C_U_RX | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RX.1=`V5A`，C_U_RX.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-c-rx-bulk"></a>

### 第006步：在ARRAY／04_RX放置 C_RX_BULK

在 **ARRAY板的04_RX图页**，接着放置 **C_RX_BULK**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_RX的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | C_RX_BULK | C0603C105K3RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有11个物理端点，逐个见[完整端点N0391](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0391)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| ARRAY | 04_RX | C_RX_BULK | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_BULK.1=`V5A`，C_RX_BULK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-rx0"></a>

### 第007步：在ARRAY／04_RX放置 RX0

在 **ARRAY板的04_RX图页**，接着放置 **RX0**，精确型号 **NU40C10R-2**，封装 **manufacturer receiver**。

放在对应接收通道最左侧；两脚按表，后接输入限流、交流耦合、偏置和运放；不要与发射驱动输出网络连接。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | RX0 | NU40C10R-2 | 1 | SENSE | RX_RAW0 | PASSIVE | 从此脚引线，标注精确网名`RX_RAW0`；跨页使用同名板内标签。同网还接：04_RX/R_RX_IN0.1（1）。 [完整端点N0104](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0104)。 |
| ARRAY | 04_RX | RX0 | NU40C10R-2 | 2 | RETURN | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为RX0.2→GND。

<a id="array-c-rx-ac0"></a>

### 第008步：在ARRAY／04_RX放置 C_RX_AC0

在 **ARRAY板的04_RX图页**，接着放置 **C_RX_AC0**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：紧邻本页RX0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | C_RX_AC0 | C1210C104J5GACTU | 1 | 1 | RX_LIMIT0 | PASSIVE | 从此脚引线，标注精确网名`RX_LIMIT0`；跨页使用同名板内标签。同网还接：04_RX/R_RX_IN0.2（2）。 [完整端点N0100](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0100)。 |
| ARRAY | 04_RX | C_RX_AC0 | C1210C104J5GACTU | 2 | 2 | RX_BIAS0 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS0`；跨页使用同名板内标签。同网还接：04_RX/R_RX_BIAS0.1（1）；04_RX/D_RX0.3（K1/A2）；04_RX/U_RX.3（+IN0）。 [完整端点N0091](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0091)。 |

接完确认：C_RX_AC0.1=`RX_LIMIT0`，C_RX_AC0.2=`RX_BIAS0`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-bias0"></a>

### 第009步：在ARRAY／04_RX放置 R_RX_BIAS0

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_BIAS0**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_BIAS0 | CRCW0603100KFKEA | 1 | 1 | RX_BIAS0 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS0`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC0.2（2）；04_RX/D_RX0.3（K1/A2）；04_RX/U_RX.3（+IN0）。 [完整端点N0091](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0091)。 |
| ARRAY | 04_RX | R_RX_BIAS0 | CRCW0603100KFKEA | 2 | 2 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_GAIN0.2（2）。 |

接完确认：R_RX_BIAS0.1=`RX_BIAS0`，R_RX_BIAS0.2=`VBIAS25`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-bleed0"></a>

### 第010步：在ARRAY／04_RX放置 R_RX_BLEED0

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_BLEED0**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_BLEED0 | CRCW0603100KFKEA | 1 | 1 | RX0 | PASSIVE | 从此脚引线，标注精确网名`RX0`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.55（RX0）；04_RX/R_RX_FB0.1（1）；04_RX/U_RX.1（OUT0）。 [完整端点N0087](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0087)。 |
| ARRAY | 04_RX | R_RX_BLEED0 | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RX_BLEED0.1=`RX0`，R_RX_BLEED0.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-fb0"></a>

### 第011步：在ARRAY／04_RX放置 R_RX_FB0

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_FB0**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_FB0 | CRCW0603100KFKEA | 1 | 1 | RX0 | PASSIVE | 从此脚引线，标注精确网名`RX0`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.55（RX0）；04_RX/R_RX_BLEED0.1（1）；04_RX/U_RX.1（OUT0）。 [完整端点N0087](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0087)。 |
| ARRAY | 04_RX | R_RX_FB0 | CRCW0603100KFKEA | 2 | 2 | RX_FB0 | PASSIVE | 从此脚引线，标注精确网名`RX_FB0`；跨页使用同名板内标签。同网还接：04_RX/R_RX_GAIN0.1（1）；04_RX/U_RX.2（-IN0）。 [完整端点N0096](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0096)。 |

接完确认：R_RX_FB0.1=`RX0`，R_RX_FB0.2=`RX_FB0`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-gain0"></a>

### 第012步：在ARRAY／04_RX放置 R_RX_GAIN0

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_GAIN0**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页RX0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_GAIN0 | CRCW060310K0FKEA | 1 | 1 | RX_FB0 | PASSIVE | 从此脚引线，标注精确网名`RX_FB0`；跨页使用同名板内标签。同网还接：04_RX/R_RX_FB0.2（2）；04_RX/U_RX.2（-IN0）。 [完整端点N0096](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0096)。 |
| ARRAY | 04_RX | R_RX_GAIN0 | CRCW060310K0FKEA | 2 | 2 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_BIAS0.2（2）。 |

接完确认：R_RX_GAIN0.1=`RX_FB0`，R_RX_GAIN0.2=`VBIAS25`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-in0"></a>

### 第013步：在ARRAY／04_RX放置 R_RX_IN0

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_IN0**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页RX0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_IN0 | CRCW060310K0FKEA | 1 | 1 | RX_RAW0 | PASSIVE | 从此脚引线，标注精确网名`RX_RAW0`；跨页使用同名板内标签。同网还接：04_RX/RX0.1（SENSE）。 [完整端点N0104](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0104)。 |
| ARRAY | 04_RX | R_RX_IN0 | CRCW060310K0FKEA | 2 | 2 | RX_LIMIT0 | PASSIVE | 从此脚引线，标注精确网名`RX_LIMIT0`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC0.1（1）。 [完整端点N0100](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0100)。 |

接完确认：R_RX_IN0.1=`RX_RAW0`，R_RX_IN0.2=`RX_LIMIT0`；不可旁路该器件把两个网名短在一起。

<a id="array-d-rx0"></a>

### 第014步：在ARRAY／04_RX放置 D_RX0

在 **ARRAY板的04_RX图页**，接着放置 **D_RX0**，精确型号 **BAS70-04,215**，封装 **SOT23**。

放在对应RX输入钳位节点旁。BAS70-04为双二极管：1脚A1接GND，2脚K2接V5A，3脚K1/A2接本通道钳位节点；不能按两脚TVS接法处理。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | D_RX0 | BAS70-04,215 | 1 | A1 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 04_RX | D_RX0 | BAS70-04,215 | 2 | K2 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有11个物理端点，逐个见[完整端点N0391](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0391)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| ARRAY | 04_RX | D_RX0 | BAS70-04,215 | 3 | K1/A2 | RX_BIAS0 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS0`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC0.2（2）；04_RX/R_RX_BIAS0.1（1）；04_RX/U_RX.3（+IN0）。 [完整端点N0091](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0091)。 |

接完确认：电源/地/参考为D_RX0.1→GND；D_RX0.2→V5A。

<a id="array-rx1"></a>

### 第015步：在ARRAY／04_RX放置 RX1

在 **ARRAY板的04_RX图页**，接着放置 **RX1**，精确型号 **NU40C10R-2**，封装 **manufacturer receiver**。

放在对应接收通道最左侧；两脚按表，后接输入限流、交流耦合、偏置和运放；不要与发射驱动输出网络连接。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | RX1 | NU40C10R-2 | 1 | SENSE | RX_RAW1 | PASSIVE | 从此脚引线，标注精确网名`RX_RAW1`；跨页使用同名板内标签。同网还接：04_RX/R_RX_IN1.1（1）。 [完整端点N0105](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0105)。 |
| ARRAY | 04_RX | RX1 | NU40C10R-2 | 2 | RETURN | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为RX1.2→GND。

<a id="array-c-rx-ac1"></a>

### 第016步：在ARRAY／04_RX放置 C_RX_AC1

在 **ARRAY板的04_RX图页**，接着放置 **C_RX_AC1**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：紧邻本页RX1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | C_RX_AC1 | C1210C104J5GACTU | 1 | 1 | RX_LIMIT1 | PASSIVE | 从此脚引线，标注精确网名`RX_LIMIT1`；跨页使用同名板内标签。同网还接：04_RX/R_RX_IN1.2（2）。 [完整端点N0101](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0101)。 |
| ARRAY | 04_RX | C_RX_AC1 | C1210C104J5GACTU | 2 | 2 | RX_BIAS1 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS1`；跨页使用同名板内标签。同网还接：04_RX/R_RX_BIAS1.1（1）；04_RX/D_RX1.3（K1/A2）；04_RX/U_RX.5（+IN1）。 [完整端点N0092](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0092)。 |

接完确认：C_RX_AC1.1=`RX_LIMIT1`，C_RX_AC1.2=`RX_BIAS1`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-bias1"></a>

### 第017步：在ARRAY／04_RX放置 R_RX_BIAS1

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_BIAS1**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_BIAS1 | CRCW0603100KFKEA | 1 | 1 | RX_BIAS1 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS1`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC1.2（2）；04_RX/D_RX1.3（K1/A2）；04_RX/U_RX.5（+IN1）。 [完整端点N0092](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0092)。 |
| ARRAY | 04_RX | R_RX_BIAS1 | CRCW0603100KFKEA | 2 | 2 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_BIAS0.2（2）。 |

接完确认：R_RX_BIAS1.1=`RX_BIAS1`，R_RX_BIAS1.2=`VBIAS25`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-bleed1"></a>

### 第018步：在ARRAY／04_RX放置 R_RX_BLEED1

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_BLEED1**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_BLEED1 | CRCW0603100KFKEA | 1 | 1 | RX1 | PASSIVE | 从此脚引线，标注精确网名`RX1`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.57（RX1）；04_RX/R_RX_FB1.1（1）；04_RX/U_RX.7（OUT1）。 [完整端点N0088](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0088)。 |
| ARRAY | 04_RX | R_RX_BLEED1 | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RX_BLEED1.1=`RX1`，R_RX_BLEED1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-fb1"></a>

### 第019步：在ARRAY／04_RX放置 R_RX_FB1

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_FB1**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_FB1 | CRCW0603100KFKEA | 1 | 1 | RX1 | PASSIVE | 从此脚引线，标注精确网名`RX1`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.57（RX1）；04_RX/R_RX_BLEED1.1（1）；04_RX/U_RX.7（OUT1）。 [完整端点N0088](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0088)。 |
| ARRAY | 04_RX | R_RX_FB1 | CRCW0603100KFKEA | 2 | 2 | RX_FB1 | PASSIVE | 从此脚引线，标注精确网名`RX_FB1`；跨页使用同名板内标签。同网还接：04_RX/R_RX_GAIN1.1（1）；04_RX/U_RX.6（-IN1）。 [完整端点N0097](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0097)。 |

接完确认：R_RX_FB1.1=`RX1`，R_RX_FB1.2=`RX_FB1`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-gain1"></a>

### 第020步：在ARRAY／04_RX放置 R_RX_GAIN1

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_GAIN1**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页RX1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_GAIN1 | CRCW060310K0FKEA | 1 | 1 | RX_FB1 | PASSIVE | 从此脚引线，标注精确网名`RX_FB1`；跨页使用同名板内标签。同网还接：04_RX/R_RX_FB1.2（2）；04_RX/U_RX.6（-IN1）。 [完整端点N0097](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0097)。 |
| ARRAY | 04_RX | R_RX_GAIN1 | CRCW060310K0FKEA | 2 | 2 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_BIAS0.2（2）。 |

接完确认：R_RX_GAIN1.1=`RX_FB1`，R_RX_GAIN1.2=`VBIAS25`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-in1"></a>

### 第021步：在ARRAY／04_RX放置 R_RX_IN1

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_IN1**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页RX1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_IN1 | CRCW060310K0FKEA | 1 | 1 | RX_RAW1 | PASSIVE | 从此脚引线，标注精确网名`RX_RAW1`；跨页使用同名板内标签。同网还接：04_RX/RX1.1（SENSE）。 [完整端点N0105](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0105)。 |
| ARRAY | 04_RX | R_RX_IN1 | CRCW060310K0FKEA | 2 | 2 | RX_LIMIT1 | PASSIVE | 从此脚引线，标注精确网名`RX_LIMIT1`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC1.1（1）。 [完整端点N0101](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0101)。 |

接完确认：R_RX_IN1.1=`RX_RAW1`，R_RX_IN1.2=`RX_LIMIT1`；不可旁路该器件把两个网名短在一起。

<a id="array-d-rx1"></a>

### 第022步：在ARRAY／04_RX放置 D_RX1

在 **ARRAY板的04_RX图页**，接着放置 **D_RX1**，精确型号 **BAS70-04,215**，封装 **SOT23**。

放在对应RX输入钳位节点旁。BAS70-04为双二极管：1脚A1接GND，2脚K2接V5A，3脚K1/A2接本通道钳位节点；不能按两脚TVS接法处理。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | D_RX1 | BAS70-04,215 | 1 | A1 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 04_RX | D_RX1 | BAS70-04,215 | 2 | K2 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有11个物理端点，逐个见[完整端点N0391](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0391)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| ARRAY | 04_RX | D_RX1 | BAS70-04,215 | 3 | K1/A2 | RX_BIAS1 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS1`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC1.2（2）；04_RX/R_RX_BIAS1.1（1）；04_RX/U_RX.5（+IN1）。 [完整端点N0092](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0092)。 |

接完确认：电源/地/参考为D_RX1.1→GND；D_RX1.2→V5A。

<a id="array-rx2"></a>

### 第023步：在ARRAY／04_RX放置 RX2

在 **ARRAY板的04_RX图页**，接着放置 **RX2**，精确型号 **NU40C10R-2**，封装 **manufacturer receiver**。

放在对应接收通道最左侧；两脚按表，后接输入限流、交流耦合、偏置和运放；不要与发射驱动输出网络连接。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | RX2 | NU40C10R-2 | 1 | SENSE | RX_RAW2 | PASSIVE | 从此脚引线，标注精确网名`RX_RAW2`；跨页使用同名板内标签。同网还接：04_RX/R_RX_IN2.1（1）。 [完整端点N0106](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0106)。 |
| ARRAY | 04_RX | RX2 | NU40C10R-2 | 2 | RETURN | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为RX2.2→GND。

<a id="array-c-rx-ac2"></a>

### 第024步：在ARRAY／04_RX放置 C_RX_AC2

在 **ARRAY板的04_RX图页**，接着放置 **C_RX_AC2**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：紧邻本页RX2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | C_RX_AC2 | C1210C104J5GACTU | 1 | 1 | RX_LIMIT2 | PASSIVE | 从此脚引线，标注精确网名`RX_LIMIT2`；跨页使用同名板内标签。同网还接：04_RX/R_RX_IN2.2（2）。 [完整端点N0102](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0102)。 |
| ARRAY | 04_RX | C_RX_AC2 | C1210C104J5GACTU | 2 | 2 | RX_BIAS2 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS2`；跨页使用同名板内标签。同网还接：04_RX/R_RX_BIAS2.1（1）；04_RX/D_RX2.3（K1/A2）；04_RX/U_RX.10（+IN2）。 [完整端点N0093](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0093)。 |

接完确认：C_RX_AC2.1=`RX_LIMIT2`，C_RX_AC2.2=`RX_BIAS2`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-bias2"></a>

### 第025步：在ARRAY／04_RX放置 R_RX_BIAS2

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_BIAS2**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_BIAS2 | CRCW0603100KFKEA | 1 | 1 | RX_BIAS2 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS2`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC2.2（2）；04_RX/D_RX2.3（K1/A2）；04_RX/U_RX.10（+IN2）。 [完整端点N0093](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0093)。 |
| ARRAY | 04_RX | R_RX_BIAS2 | CRCW0603100KFKEA | 2 | 2 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_BIAS0.2（2）。 |

接完确认：R_RX_BIAS2.1=`RX_BIAS2`，R_RX_BIAS2.2=`VBIAS25`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-bleed2"></a>

### 第026步：在ARRAY／04_RX放置 R_RX_BLEED2

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_BLEED2**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_BLEED2 | CRCW0603100KFKEA | 1 | 1 | RX2 | PASSIVE | 从此脚引线，标注精确网名`RX2`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.59（RX2）；04_RX/R_RX_FB2.1（1）；04_RX/U_RX.8（OUT2）。 [完整端点N0089](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0089)。 |
| ARRAY | 04_RX | R_RX_BLEED2 | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RX_BLEED2.1=`RX2`，R_RX_BLEED2.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-fb2"></a>

### 第027步：在ARRAY／04_RX放置 R_RX_FB2

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_FB2**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_FB2 | CRCW0603100KFKEA | 1 | 1 | RX2 | PASSIVE | 从此脚引线，标注精确网名`RX2`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.59（RX2）；04_RX/R_RX_BLEED2.1（1）；04_RX/U_RX.8（OUT2）。 [完整端点N0089](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0089)。 |
| ARRAY | 04_RX | R_RX_FB2 | CRCW0603100KFKEA | 2 | 2 | RX_FB2 | PASSIVE | 从此脚引线，标注精确网名`RX_FB2`；跨页使用同名板内标签。同网还接：04_RX/R_RX_GAIN2.1（1）；04_RX/U_RX.9（-IN2）。 [完整端点N0098](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0098)。 |

接完确认：R_RX_FB2.1=`RX2`，R_RX_FB2.2=`RX_FB2`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-gain2"></a>

### 第028步：在ARRAY／04_RX放置 R_RX_GAIN2

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_GAIN2**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页RX2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_GAIN2 | CRCW060310K0FKEA | 1 | 1 | RX_FB2 | PASSIVE | 从此脚引线，标注精确网名`RX_FB2`；跨页使用同名板内标签。同网还接：04_RX/R_RX_FB2.2（2）；04_RX/U_RX.9（-IN2）。 [完整端点N0098](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0098)。 |
| ARRAY | 04_RX | R_RX_GAIN2 | CRCW060310K0FKEA | 2 | 2 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_BIAS0.2（2）。 |

接完确认：R_RX_GAIN2.1=`RX_FB2`，R_RX_GAIN2.2=`VBIAS25`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-in2"></a>

### 第029步：在ARRAY／04_RX放置 R_RX_IN2

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_IN2**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页RX2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_IN2 | CRCW060310K0FKEA | 1 | 1 | RX_RAW2 | PASSIVE | 从此脚引线，标注精确网名`RX_RAW2`；跨页使用同名板内标签。同网还接：04_RX/RX2.1（SENSE）。 [完整端点N0106](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0106)。 |
| ARRAY | 04_RX | R_RX_IN2 | CRCW060310K0FKEA | 2 | 2 | RX_LIMIT2 | PASSIVE | 从此脚引线，标注精确网名`RX_LIMIT2`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC2.1（1）。 [完整端点N0102](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0102)。 |

接完确认：R_RX_IN2.1=`RX_RAW2`，R_RX_IN2.2=`RX_LIMIT2`；不可旁路该器件把两个网名短在一起。

<a id="array-d-rx2"></a>

### 第030步：在ARRAY／04_RX放置 D_RX2

在 **ARRAY板的04_RX图页**，接着放置 **D_RX2**，精确型号 **BAS70-04,215**，封装 **SOT23**。

放在对应RX输入钳位节点旁。BAS70-04为双二极管：1脚A1接GND，2脚K2接V5A，3脚K1/A2接本通道钳位节点；不能按两脚TVS接法处理。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | D_RX2 | BAS70-04,215 | 1 | A1 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 04_RX | D_RX2 | BAS70-04,215 | 2 | K2 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有11个物理端点，逐个见[完整端点N0391](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0391)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| ARRAY | 04_RX | D_RX2 | BAS70-04,215 | 3 | K1/A2 | RX_BIAS2 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS2`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC2.2（2）；04_RX/R_RX_BIAS2.1（1）；04_RX/U_RX.10（+IN2）。 [完整端点N0093](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0093)。 |

接完确认：电源/地/参考为D_RX2.1→GND；D_RX2.2→V5A。

<a id="array-rx3"></a>

### 第031步：在ARRAY／04_RX放置 RX3

在 **ARRAY板的04_RX图页**，接着放置 **RX3**，精确型号 **NU40C10R-2**，封装 **manufacturer receiver**。

放在对应接收通道最左侧；两脚按表，后接输入限流、交流耦合、偏置和运放；不要与发射驱动输出网络连接。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | RX3 | NU40C10R-2 | 1 | SENSE | RX_RAW3 | PASSIVE | 从此脚引线，标注精确网名`RX_RAW3`；跨页使用同名板内标签。同网还接：04_RX/R_RX_IN3.1（1）。 [完整端点N0107](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0107)。 |
| ARRAY | 04_RX | RX3 | NU40C10R-2 | 2 | RETURN | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为RX3.2→GND。

<a id="array-c-rx-ac3"></a>

### 第032步：在ARRAY／04_RX放置 C_RX_AC3

在 **ARRAY板的04_RX图页**，接着放置 **C_RX_AC3**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：紧邻本页RX3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | C_RX_AC3 | C1210C104J5GACTU | 1 | 1 | RX_LIMIT3 | PASSIVE | 从此脚引线，标注精确网名`RX_LIMIT3`；跨页使用同名板内标签。同网还接：04_RX/R_RX_IN3.2（2）。 [完整端点N0103](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0103)。 |
| ARRAY | 04_RX | C_RX_AC3 | C1210C104J5GACTU | 2 | 2 | RX_BIAS3 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS3`；跨页使用同名板内标签。同网还接：04_RX/R_RX_BIAS3.1（1）；04_RX/D_RX3.3（K1/A2）；04_RX/U_RX.12（+IN3）。 [完整端点N0094](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0094)。 |

接完确认：C_RX_AC3.1=`RX_LIMIT3`，C_RX_AC3.2=`RX_BIAS3`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-bias3"></a>

### 第033步：在ARRAY／04_RX放置 R_RX_BIAS3

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_BIAS3**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX3的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_BIAS3 | CRCW0603100KFKEA | 1 | 1 | RX_BIAS3 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS3`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC3.2（2）；04_RX/D_RX3.3（K1/A2）；04_RX/U_RX.12（+IN3）。 [完整端点N0094](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0094)。 |
| ARRAY | 04_RX | R_RX_BIAS3 | CRCW0603100KFKEA | 2 | 2 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_BIAS0.2（2）。 |

接完确认：R_RX_BIAS3.1=`RX_BIAS3`，R_RX_BIAS3.2=`VBIAS25`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-bleed3"></a>

### 第034步：在ARRAY／04_RX放置 R_RX_BLEED3

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_BLEED3**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX3的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_BLEED3 | CRCW0603100KFKEA | 1 | 1 | RX3 | PASSIVE | 从此脚引线，标注精确网名`RX3`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.61（RX3）；04_RX/R_RX_FB3.1（1）；04_RX/U_RX.14（OUT3）。 [完整端点N0090](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0090)。 |
| ARRAY | 04_RX | R_RX_BLEED3 | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RX_BLEED3.1=`RX3`，R_RX_BLEED3.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-fb3"></a>

### 第035步：在ARRAY／04_RX放置 R_RX_FB3

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_FB3**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页RX3的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_FB3 | CRCW0603100KFKEA | 1 | 1 | RX3 | PASSIVE | 从此脚引线，标注精确网名`RX3`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.61（RX3）；04_RX/R_RX_BLEED3.1（1）；04_RX/U_RX.14（OUT3）。 [完整端点N0090](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0090)。 |
| ARRAY | 04_RX | R_RX_FB3 | CRCW0603100KFKEA | 2 | 2 | RX_FB3 | PASSIVE | 从此脚引线，标注精确网名`RX_FB3`；跨页使用同名板内标签。同网还接：04_RX/R_RX_GAIN3.1（1）；04_RX/U_RX.13（-IN3）。 [完整端点N0099](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0099)。 |

接完确认：R_RX_FB3.1=`RX3`，R_RX_FB3.2=`RX_FB3`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-gain3"></a>

### 第036步：在ARRAY／04_RX放置 R_RX_GAIN3

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_GAIN3**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页RX3的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_GAIN3 | CRCW060310K0FKEA | 1 | 1 | RX_FB3 | PASSIVE | 从此脚引线，标注精确网名`RX_FB3`；跨页使用同名板内标签。同网还接：04_RX/R_RX_FB3.2（2）；04_RX/U_RX.13（-IN3）。 [完整端点N0099](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0099)。 |
| ARRAY | 04_RX | R_RX_GAIN3 | CRCW060310K0FKEA | 2 | 2 | VBIAS25 | PASSIVE | 接本板`VBIAS25`电源/参考标签；来源：本板U_BIAS.2产生的接收2.5V偏置，不能与另一阵列偏置并联。同网另有9个物理端点，逐个见[完整端点N0397](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0397)；例如04_RX/U_BIAS.2（OUT）；04_RX/C_BIAS_OUT.1（1）；04_RX/R_RX_BIAS0.2（2）。 |

接完确认：R_RX_GAIN3.1=`RX_FB3`，R_RX_GAIN3.2=`VBIAS25`；不可旁路该器件把两个网名短在一起。

<a id="array-r-rx-in3"></a>

### 第037步：在ARRAY／04_RX放置 R_RX_IN3

在 **ARRAY板的04_RX图页**，接着放置 **R_RX_IN3**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页RX3的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | R_RX_IN3 | CRCW060310K0FKEA | 1 | 1 | RX_RAW3 | PASSIVE | 从此脚引线，标注精确网名`RX_RAW3`；跨页使用同名板内标签。同网还接：04_RX/RX3.1（SENSE）。 [完整端点N0107](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0107)。 |
| ARRAY | 04_RX | R_RX_IN3 | CRCW060310K0FKEA | 2 | 2 | RX_LIMIT3 | PASSIVE | 从此脚引线，标注精确网名`RX_LIMIT3`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC3.1（1）。 [完整端点N0103](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0103)。 |

接完确认：R_RX_IN3.1=`RX_RAW3`，R_RX_IN3.2=`RX_LIMIT3`；不可旁路该器件把两个网名短在一起。

<a id="array-d-rx3"></a>

### 第038步：在ARRAY／04_RX放置 D_RX3

在 **ARRAY板的04_RX图页**，接着放置 **D_RX3**，精确型号 **BAS70-04,215**，封装 **SOT23**。

放在对应RX输入钳位节点旁。BAS70-04为双二极管：1脚A1接GND，2脚K2接V5A，3脚K1/A2接本通道钳位节点；不能按两脚TVS接法处理。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 04_RX | D_RX3 | BAS70-04,215 | 1 | A1 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 04_RX | D_RX3 | BAS70-04,215 | 2 | K2 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有11个物理端点，逐个见[完整端点N0391](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0391)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| ARRAY | 04_RX | D_RX3 | BAS70-04,215 | 3 | K1/A2 | RX_BIAS3 | PASSIVE | 从此脚引线，标注精确网名`RX_BIAS3`；跨页使用同名板内标签。同网还接：04_RX/C_RX_AC3.2（2）；04_RX/R_RX_BIAS3.1（1）；04_RX/U_RX.12（+IN3）。 [完整端点N0094](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0094)。 |

接完确认：电源/地/参考为D_RX3.1→GND；D_RX3.2→V5A。

本页完成核对：**38个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。
