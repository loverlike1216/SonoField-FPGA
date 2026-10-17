# CENTRAL／05_RX_INPUT逐步连接分册

本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。

<a id="page-central-05-rx-input"></a>

## CENTRAL板／05_RX_INPUT图页

按UP四路在上、DN四路在下摆放掉电隔离开关、空白控制和499Ω/1nF ADC输入RC。每路终点是对应ADC正输入；负输入接GND。

<a id="central-u-blankinv-up"></a>

### 第001步：在CENTRAL／05_RX_INPUT放置 U_BLANKINV_UP

在 **CENTRAL板的05_RX_INPUT图页**，先放置 **U_BLANKINV_UP**，精确型号 **SN74LVC1G14DBVR**，封装 **DBV/SOT23-5**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_UP | SN74LVC1G14DBVR | 1 | NC | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_UP | SN74LVC1G14DBVR | 2 | A | UP_RX_BLANK_RAW | IN | 从此脚引线，标注精确网名`UP_RX_BLANK_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.24（EX_IO1_11P）；02_TX_BUFFERS/U_CBUF2.2（A0）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.1（1）；05_RX_INPUT/R_OFF_UP_RX_BLANK_RAW.1（1）。 [完整端点N0667](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0667)。 |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_UP | SN74LVC1G14DBVR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_UP | SN74LVC1G14DBVR | 4 | Y | RX_ALLOW_UP | OUT | 从此脚引线，标注精确网名`RX_ALLOW_UP`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_UP.2（1B）。 [完整端点N0576](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0576)。 |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_UP | SN74LVC1G14DBVR | 5 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_BLANKINV_UP.3→GND；U_BLANKINV_UP.5→V3V3。 NC脚1逐个单独标记。

<a id="central-c-u-blankinv-up"></a>

### 第002步：在CENTRAL／05_RX_INPUT放置 C_U_BLANKINV_UP

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_U_BLANKINV_UP**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_BLANKINV_UP的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_U_BLANKINV_UP | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 05_RX_INPUT | C_U_BLANKINV_UP | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_BLANKINV_UP.1=`V3V3`，C_U_BLANKINV_UP.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-def-up-rx-blank-raw"></a>

### 第003步：在CENTRAL／05_RX_INPUT放置 R_DEF_UP_RX_BLANK_RAW

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_DEF_UP_RX_BLANK_RAW**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_BLANKINV_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_DEF_UP_RX_BLANK_RAW | CRCW060310K0FKEA | 1 | 1 | UP_RX_BLANK_RAW | PASSIVE | 从此脚引线，标注精确网名`UP_RX_BLANK_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.24（EX_IO1_11P）；02_TX_BUFFERS/U_CBUF2.2（A0）；05_RX_INPUT/R_OFF_UP_RX_BLANK_RAW.1（1）；05_RX_INPUT/U_BLANKINV_UP.2（A）。 [完整端点N0667](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0667)。 |
| CENTRAL | 05_RX_INPUT | R_DEF_UP_RX_BLANK_RAW | CRCW060310K0FKEA | 2 | 2 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_DN_RX_BLANK_RAW.2（2）。 |

接完确认：R_DEF_UP_RX_BLANK_RAW.1=`UP_RX_BLANK_RAW`，R_DEF_UP_RX_BLANK_RAW.2=`AX_VIO_REF3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-off-up-rx-blank-raw"></a>

### 第004步：在CENTRAL／05_RX_INPUT放置 R_OFF_UP_RX_BLANK_RAW

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_OFF_UP_RX_BLANK_RAW**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_BLANKINV_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_OFF_UP_RX_BLANK_RAW | CRCW0603100KFKEA | 1 | 1 | UP_RX_BLANK_RAW | PASSIVE | 从此脚引线，标注精确网名`UP_RX_BLANK_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.24（EX_IO1_11P）；02_TX_BUFFERS/U_CBUF2.2（A0）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.1（1）；05_RX_INPUT/U_BLANKINV_UP.2（A）。 [完整端点N0667](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0667)。 |
| CENTRAL | 05_RX_INPUT | R_OFF_UP_RX_BLANK_RAW | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_OFF_UP_RX_BLANK_RAW.1=`UP_RX_BLANK_RAW`，R_OFF_UP_RX_BLANK_RAW.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-rxg-up"></a>

### 第005步：在CENTRAL／05_RX_INPUT放置 U_RXG_UP

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **U_RXG_UP**，精确型号 **SN74LVC2G08DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | U_RXG_UP | SN74LVC2G08DCUR | 1 | 1A | V5_GOOD | IN | 从此脚引线，标注精确网名`V5_GOOD`；跨页使用同名板内标签。同网还接：00_POWER/U_5MON.6（RESET_N）；00_POWER/R_5GOOD.1（1）；05_RX_INPUT/U_RXG_DN.1（1A）；06_I2C_TEMP_SAFETY/U_G1.2（1B）。 [完整端点N0683](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0683)。 |
| CENTRAL | 05_RX_INPUT | U_RXG_UP | SN74LVC2G08DCUR | 2 | 1B | RX_ALLOW_UP | IN | 从此脚引线，标注精确网名`RX_ALLOW_UP`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_BLANKINV_UP.4（Y）。 [完整端点N0576](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0576)。 |
| CENTRAL | 05_RX_INPUT | U_RXG_UP | SN74LVC2G08DCUR | 3 | 2Y | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 05_RX_INPUT | U_RXG_UP | SN74LVC2G08DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXG_UP | SN74LVC2G08DCUR | 5 | 2A | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXG_UP | SN74LVC2G08DCUR | 6 | 2B | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXG_UP | SN74LVC2G08DCUR | 7 | 1Y | RX_ENABLE_UP | OUT | 从此脚引线，标注精确网名`RX_ENABLE_UP`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_UP.1（IN1）；05_RX_INPUT/U_RXSW_UP.8（IN4）；05_RX_INPUT/U_RXSW_UP.9（IN3）；05_RX_INPUT/U_RXSW_UP.16（IN2）。 [完整端点N0578](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0578)。 |
| CENTRAL | 05_RX_INPUT | U_RXG_UP | SN74LVC2G08DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_RXG_UP.5→GND；U_RXG_UP.6→GND；U_RXG_UP.4→GND；U_RXG_UP.8→V3V3。 NC脚3逐个单独标记。

<a id="central-c-u-rxg-up"></a>

### 第006步：在CENTRAL／05_RX_INPUT放置 C_U_RXG_UP

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_U_RXG_UP**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RXG_UP的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_U_RXG_UP | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 05_RX_INPUT | C_U_RXG_UP | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RXG_UP.1=`V3V3`，C_U_RXG_UP.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-rxsw-up"></a>

### 第007步：在CENTRAL／05_RX_INPUT放置 U_RXSW_UP

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **U_RXSW_UP**，精确型号 **ADG4612BRUZ**，封装 **RU/TSSOP16**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 1 | IN1 | RX_ENABLE_UP | IN | 从此脚引线，标注精确网名`RX_ENABLE_UP`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_UP.7（1Y）；05_RX_INPUT/U_RXSW_UP.8（IN4）；05_RX_INPUT/U_RXSW_UP.9（IN3）；05_RX_INPUT/U_RXSW_UP.16（IN2）。 [完整端点N0578](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0578)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 2 | D1 | UP_RX0_SW | PASSIVE | 从此脚引线，标注精确网名`UP_RX0_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN0.1（1）。 [完整端点N0658](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0658)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 3 | S1 | UP_RX0 | PASSIVE | 从此脚引线，标注精确网名`UP_RX0`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.55（RX0）。 [完整端点N0657](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0657)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 4 | VSS | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 5 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 6 | S4 | UP_RX3 | PASSIVE | 从此脚引线，标注精确网名`UP_RX3`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.61（RX3）。 [完整端点N0663](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0663)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 7 | D4 | UP_RX3_SW | PASSIVE | 从此脚引线，标注精确网名`UP_RX3_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN3.1（1）。 [完整端点N0664](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0664)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 8 | IN4 | RX_ENABLE_UP | IN | 从此脚引线，标注精确网名`RX_ENABLE_UP`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_UP.7（1Y）；05_RX_INPUT/U_RXSW_UP.1（IN1）；05_RX_INPUT/U_RXSW_UP.9（IN3）；05_RX_INPUT/U_RXSW_UP.16（IN2）。 [完整端点N0578](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0578)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 9 | IN3 | RX_ENABLE_UP | IN | 从此脚引线，标注精确网名`RX_ENABLE_UP`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_UP.7（1Y）；05_RX_INPUT/U_RXSW_UP.1（IN1）；05_RX_INPUT/U_RXSW_UP.8（IN4）；05_RX_INPUT/U_RXSW_UP.16（IN2）。 [完整端点N0578](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0578)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 10 | D3 | UP_RX2_SW | PASSIVE | 从此脚引线，标注精确网名`UP_RX2_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN2.1（1）。 [完整端点N0662](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0662)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 11 | S3 | UP_RX2 | PASSIVE | 从此脚引线，标注精确网名`UP_RX2`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.59（RX2）。 [完整端点N0661](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0661)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 12 | NC | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 13 | VDD | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 14 | S2 | UP_RX1 | PASSIVE | 从此脚引线，标注精确网名`UP_RX1`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.57（RX1）。 [完整端点N0659](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0659)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 15 | D2 | UP_RX1_SW | PASSIVE | 从此脚引线，标注精确网名`UP_RX1_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN1.1（1）。 [完整端点N0660](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0660)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_UP | ADG4612BRUZ | 16 | IN2 | RX_ENABLE_UP | IN | 从此脚引线，标注精确网名`RX_ENABLE_UP`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_UP.7（1Y）；05_RX_INPUT/U_RXSW_UP.1（IN1）；05_RX_INPUT/U_RXSW_UP.8（IN4）；05_RX_INPUT/U_RXSW_UP.9（IN3）。 [完整端点N0578](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0578)。 |

接完确认：电源/地/参考为U_RXSW_UP.4→GND；U_RXSW_UP.5→GND；U_RXSW_UP.13→V5A。 NC脚12逐个单独标记。

<a id="central-c-u-rxsw-up"></a>

### 第008步：在CENTRAL／05_RX_INPUT放置 C_U_RXSW_UP

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_U_RXSW_UP**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_U_RXSW_UP | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 05_RX_INPUT | C_U_RXSW_UP | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RXSW_UP.1=`V5A`，C_U_RXSW_UP.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-in0"></a>

### 第009步：在CENTRAL／05_RX_INPUT放置 C_ADC_IN0

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_ADC_IN0**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_ADC_IN0 | C0603C102J5GACTU | 1 | 1 | ADC_IN0 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN0`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.49（V1+）；05_RX_INPUT/R_ADC_IN0.2（2）；05_RX_INPUT/R_ADC_BLEED0.1（1）。 [完整端点N0429](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0429)。 |
| CENTRAL | 05_RX_INPUT | C_ADC_IN0 | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_IN0.1=`ADC_IN0`，C_ADC_IN0.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-in1"></a>

### 第010步：在CENTRAL／05_RX_INPUT放置 C_ADC_IN1

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_ADC_IN1**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_ADC_IN1 | C0603C102J5GACTU | 1 | 1 | ADC_IN1 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN1`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.51（V2+）；05_RX_INPUT/R_ADC_IN1.2（2）；05_RX_INPUT/R_ADC_BLEED1.1（1）。 [完整端点N0430](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0430)。 |
| CENTRAL | 05_RX_INPUT | C_ADC_IN1 | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_IN1.1=`ADC_IN1`，C_ADC_IN1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-in2"></a>

### 第011步：在CENTRAL／05_RX_INPUT放置 C_ADC_IN2

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_ADC_IN2**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_ADC_IN2 | C0603C102J5GACTU | 1 | 1 | ADC_IN2 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN2`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.53（V3+）；05_RX_INPUT/R_ADC_IN2.2（2）；05_RX_INPUT/R_ADC_BLEED2.1（1）。 [完整端点N0431](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0431)。 |
| CENTRAL | 05_RX_INPUT | C_ADC_IN2 | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_IN2.1=`ADC_IN2`，C_ADC_IN2.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-in3"></a>

### 第012步：在CENTRAL／05_RX_INPUT放置 C_ADC_IN3

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_ADC_IN3**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_ADC_IN3 | C0603C102J5GACTU | 1 | 1 | ADC_IN3 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN3`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.55（V4+）；05_RX_INPUT/R_ADC_IN3.2（2）；05_RX_INPUT/R_ADC_BLEED3.1（1）。 [完整端点N0432](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0432)。 |
| CENTRAL | 05_RX_INPUT | C_ADC_IN3 | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_IN3.1=`ADC_IN3`，C_ADC_IN3.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-bleed0"></a>

### 第013步：在CENTRAL／05_RX_INPUT放置 R_ADC_BLEED0

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_BLEED0**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED0 | CRCW06031M00FKEA | 1 | 1 | ADC_IN0 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN0`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.49（V1+）；05_RX_INPUT/R_ADC_IN0.2（2）；05_RX_INPUT/C_ADC_IN0.1（1）。 [完整端点N0429](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0429)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED0 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_BLEED0.1=`ADC_IN0`，R_ADC_BLEED0.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-bleed1"></a>

### 第014步：在CENTRAL／05_RX_INPUT放置 R_ADC_BLEED1

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_BLEED1**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED1 | CRCW06031M00FKEA | 1 | 1 | ADC_IN1 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN1`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.51（V2+）；05_RX_INPUT/R_ADC_IN1.2（2）；05_RX_INPUT/C_ADC_IN1.1（1）。 [完整端点N0430](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0430)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED1 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_BLEED1.1=`ADC_IN1`，R_ADC_BLEED1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-bleed2"></a>

### 第015步：在CENTRAL／05_RX_INPUT放置 R_ADC_BLEED2

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_BLEED2**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED2 | CRCW06031M00FKEA | 1 | 1 | ADC_IN2 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN2`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.53（V3+）；05_RX_INPUT/R_ADC_IN2.2（2）；05_RX_INPUT/C_ADC_IN2.1（1）。 [完整端点N0431](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0431)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED2 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_BLEED2.1=`ADC_IN2`，R_ADC_BLEED2.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-bleed3"></a>

### 第016步：在CENTRAL／05_RX_INPUT放置 R_ADC_BLEED3

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_BLEED3**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED3 | CRCW06031M00FKEA | 1 | 1 | ADC_IN3 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN3`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.55（V4+）；05_RX_INPUT/R_ADC_IN3.2（2）；05_RX_INPUT/C_ADC_IN3.1（1）。 [完整端点N0432](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0432)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED3 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_BLEED3.1=`ADC_IN3`，R_ADC_BLEED3.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-in0"></a>

### 第017步：在CENTRAL／05_RX_INPUT放置 R_ADC_IN0

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_IN0**，精确型号 **CRCW0603499RFKEA**，封装 **0603**。其值为 **499**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_IN0 | CRCW0603499RFKEA | 1 | 1 | UP_RX0_SW | PASSIVE | 从此脚引线，标注精确网名`UP_RX0_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_UP.2（D1）。 [完整端点N0658](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0658)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_IN0 | CRCW0603499RFKEA | 2 | 2 | ADC_IN0 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN0`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.49（V1+）；05_RX_INPUT/C_ADC_IN0.1（1）；05_RX_INPUT/R_ADC_BLEED0.1（1）。 [完整端点N0429](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0429)。 |

接完确认：R_ADC_IN0.1=`UP_RX0_SW`，R_ADC_IN0.2=`ADC_IN0`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-in1"></a>

### 第018步：在CENTRAL／05_RX_INPUT放置 R_ADC_IN1

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_IN1**，精确型号 **CRCW0603499RFKEA**，封装 **0603**。其值为 **499**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_IN1 | CRCW0603499RFKEA | 1 | 1 | UP_RX1_SW | PASSIVE | 从此脚引线，标注精确网名`UP_RX1_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_UP.15（D2）。 [完整端点N0660](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0660)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_IN1 | CRCW0603499RFKEA | 2 | 2 | ADC_IN1 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN1`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.51（V2+）；05_RX_INPUT/C_ADC_IN1.1（1）；05_RX_INPUT/R_ADC_BLEED1.1（1）。 [完整端点N0430](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0430)。 |

接完确认：R_ADC_IN1.1=`UP_RX1_SW`，R_ADC_IN1.2=`ADC_IN1`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-in2"></a>

### 第019步：在CENTRAL／05_RX_INPUT放置 R_ADC_IN2

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_IN2**，精确型号 **CRCW0603499RFKEA**，封装 **0603**。其值为 **499**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_IN2 | CRCW0603499RFKEA | 1 | 1 | UP_RX2_SW | PASSIVE | 从此脚引线，标注精确网名`UP_RX2_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_UP.10（D3）。 [完整端点N0662](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0662)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_IN2 | CRCW0603499RFKEA | 2 | 2 | ADC_IN2 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN2`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.53（V3+）；05_RX_INPUT/C_ADC_IN2.1（1）；05_RX_INPUT/R_ADC_BLEED2.1（1）。 [完整端点N0431](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0431)。 |

接完确认：R_ADC_IN2.1=`UP_RX2_SW`，R_ADC_IN2.2=`ADC_IN2`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-in3"></a>

### 第020步：在CENTRAL／05_RX_INPUT放置 R_ADC_IN3

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_IN3**，精确型号 **CRCW0603499RFKEA**，封装 **0603**。其值为 **499**。

纸面位置：紧邻本页U_RXSW_UP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_IN3 | CRCW0603499RFKEA | 1 | 1 | UP_RX3_SW | PASSIVE | 从此脚引线，标注精确网名`UP_RX3_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_UP.7（D4）。 [完整端点N0664](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0664)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_IN3 | CRCW0603499RFKEA | 2 | 2 | ADC_IN3 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN3`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.55（V4+）；05_RX_INPUT/C_ADC_IN3.1（1）；05_RX_INPUT/R_ADC_BLEED3.1（1）。 [完整端点N0432](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0432)。 |

接完确认：R_ADC_IN3.1=`UP_RX3_SW`，R_ADC_IN3.2=`ADC_IN3`；不可旁路该器件把两个网名短在一起。

<a id="central-u-blankinv-dn"></a>

### 第021步：在CENTRAL／05_RX_INPUT放置 U_BLANKINV_DN

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **U_BLANKINV_DN**，精确型号 **SN74LVC1G14DBVR**，封装 **DBV/SOT23-5**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_DN | SN74LVC1G14DBVR | 1 | NC | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_DN | SN74LVC1G14DBVR | 2 | A | DN_RX_BLANK_RAW | IN | 从此脚引线，标注精确网名`DN_RX_BLANK_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.24（EX_IO2_11P）；02_TX_BUFFERS/U_CBUF2.4（A1）；05_RX_INPUT/R_DEF_DN_RX_BLANK_RAW.1（1）；05_RX_INPUT/R_OFF_DN_RX_BLANK_RAW.1（1）。 [完整端点N0547](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0547)。 |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_DN | SN74LVC1G14DBVR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_DN | SN74LVC1G14DBVR | 4 | Y | RX_ALLOW_DN | OUT | 从此脚引线，标注精确网名`RX_ALLOW_DN`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_DN.2（1B）。 [完整端点N0575](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0575)。 |
| CENTRAL | 05_RX_INPUT | U_BLANKINV_DN | SN74LVC1G14DBVR | 5 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_BLANKINV_DN.3→GND；U_BLANKINV_DN.5→V3V3。 NC脚1逐个单独标记。

<a id="central-c-u-blankinv-dn"></a>

### 第022步：在CENTRAL／05_RX_INPUT放置 C_U_BLANKINV_DN

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_U_BLANKINV_DN**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_BLANKINV_DN的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_U_BLANKINV_DN | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 05_RX_INPUT | C_U_BLANKINV_DN | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_BLANKINV_DN.1=`V3V3`，C_U_BLANKINV_DN.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-def-dn-rx-blank-raw"></a>

### 第023步：在CENTRAL／05_RX_INPUT放置 R_DEF_DN_RX_BLANK_RAW

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_DEF_DN_RX_BLANK_RAW**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_BLANKINV_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_DEF_DN_RX_BLANK_RAW | CRCW060310K0FKEA | 1 | 1 | DN_RX_BLANK_RAW | PASSIVE | 从此脚引线，标注精确网名`DN_RX_BLANK_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.24（EX_IO2_11P）；02_TX_BUFFERS/U_CBUF2.4（A1）；05_RX_INPUT/R_OFF_DN_RX_BLANK_RAW.1（1）；05_RX_INPUT/U_BLANKINV_DN.2（A）。 [完整端点N0547](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0547)。 |
| CENTRAL | 05_RX_INPUT | R_DEF_DN_RX_BLANK_RAW | CRCW060310K0FKEA | 2 | 2 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |

接完确认：R_DEF_DN_RX_BLANK_RAW.1=`DN_RX_BLANK_RAW`，R_DEF_DN_RX_BLANK_RAW.2=`AX_VIO_REF3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-off-dn-rx-blank-raw"></a>

### 第024步：在CENTRAL／05_RX_INPUT放置 R_OFF_DN_RX_BLANK_RAW

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_OFF_DN_RX_BLANK_RAW**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_BLANKINV_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_OFF_DN_RX_BLANK_RAW | CRCW0603100KFKEA | 1 | 1 | DN_RX_BLANK_RAW | PASSIVE | 从此脚引线，标注精确网名`DN_RX_BLANK_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.24（EX_IO2_11P）；02_TX_BUFFERS/U_CBUF2.4（A1）；05_RX_INPUT/R_DEF_DN_RX_BLANK_RAW.1（1）；05_RX_INPUT/U_BLANKINV_DN.2（A）。 [完整端点N0547](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0547)。 |
| CENTRAL | 05_RX_INPUT | R_OFF_DN_RX_BLANK_RAW | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_OFF_DN_RX_BLANK_RAW.1=`DN_RX_BLANK_RAW`，R_OFF_DN_RX_BLANK_RAW.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-rxg-dn"></a>

### 第025步：在CENTRAL／05_RX_INPUT放置 U_RXG_DN

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **U_RXG_DN**，精确型号 **SN74LVC2G08DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | U_RXG_DN | SN74LVC2G08DCUR | 1 | 1A | V5_GOOD | IN | 从此脚引线，标注精确网名`V5_GOOD`；跨页使用同名板内标签。同网还接：00_POWER/U_5MON.6（RESET_N）；00_POWER/R_5GOOD.1（1）；05_RX_INPUT/U_RXG_UP.1（1A）；06_I2C_TEMP_SAFETY/U_G1.2（1B）。 [完整端点N0683](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0683)。 |
| CENTRAL | 05_RX_INPUT | U_RXG_DN | SN74LVC2G08DCUR | 2 | 1B | RX_ALLOW_DN | IN | 从此脚引线，标注精确网名`RX_ALLOW_DN`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_BLANKINV_DN.4（Y）。 [完整端点N0575](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0575)。 |
| CENTRAL | 05_RX_INPUT | U_RXG_DN | SN74LVC2G08DCUR | 3 | 2Y | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 05_RX_INPUT | U_RXG_DN | SN74LVC2G08DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXG_DN | SN74LVC2G08DCUR | 5 | 2A | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXG_DN | SN74LVC2G08DCUR | 6 | 2B | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXG_DN | SN74LVC2G08DCUR | 7 | 1Y | RX_ENABLE_DN | OUT | 从此脚引线，标注精确网名`RX_ENABLE_DN`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_DN.1（IN1）；05_RX_INPUT/U_RXSW_DN.8（IN4）；05_RX_INPUT/U_RXSW_DN.9（IN3）；05_RX_INPUT/U_RXSW_DN.16（IN2）。 [完整端点N0577](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0577)。 |
| CENTRAL | 05_RX_INPUT | U_RXG_DN | SN74LVC2G08DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_RXG_DN.5→GND；U_RXG_DN.6→GND；U_RXG_DN.4→GND；U_RXG_DN.8→V3V3。 NC脚3逐个单独标记。

<a id="central-c-u-rxg-dn"></a>

### 第026步：在CENTRAL／05_RX_INPUT放置 C_U_RXG_DN

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_U_RXG_DN**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RXG_DN的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_U_RXG_DN | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 05_RX_INPUT | C_U_RXG_DN | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RXG_DN.1=`V3V3`，C_U_RXG_DN.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-rxsw-dn"></a>

### 第027步：在CENTRAL／05_RX_INPUT放置 U_RXSW_DN

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **U_RXSW_DN**，精确型号 **ADG4612BRUZ**，封装 **RU/TSSOP16**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 1 | IN1 | RX_ENABLE_DN | IN | 从此脚引线，标注精确网名`RX_ENABLE_DN`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_DN.7（1Y）；05_RX_INPUT/U_RXSW_DN.8（IN4）；05_RX_INPUT/U_RXSW_DN.9（IN3）；05_RX_INPUT/U_RXSW_DN.16（IN2）。 [完整端点N0577](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0577)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 2 | D1 | DN_RX0_SW | PASSIVE | 从此脚引线，标注精确网名`DN_RX0_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN4.1（1）。 [完整端点N0538](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0538)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 3 | S1 | DN_RX0 | PASSIVE | 从此脚引线，标注精确网名`DN_RX0`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.55（RX0）。 [完整端点N0537](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0537)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 4 | VSS | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 5 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 6 | S4 | DN_RX3 | PASSIVE | 从此脚引线，标注精确网名`DN_RX3`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.61（RX3）。 [完整端点N0543](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0543)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 7 | D4 | DN_RX3_SW | PASSIVE | 从此脚引线，标注精确网名`DN_RX3_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN7.1（1）。 [完整端点N0544](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0544)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 8 | IN4 | RX_ENABLE_DN | IN | 从此脚引线，标注精确网名`RX_ENABLE_DN`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_DN.7（1Y）；05_RX_INPUT/U_RXSW_DN.1（IN1）；05_RX_INPUT/U_RXSW_DN.9（IN3）；05_RX_INPUT/U_RXSW_DN.16（IN2）。 [完整端点N0577](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0577)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 9 | IN3 | RX_ENABLE_DN | IN | 从此脚引线，标注精确网名`RX_ENABLE_DN`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_DN.7（1Y）；05_RX_INPUT/U_RXSW_DN.1（IN1）；05_RX_INPUT/U_RXSW_DN.8（IN4）；05_RX_INPUT/U_RXSW_DN.16（IN2）。 [完整端点N0577](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0577)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 10 | D3 | DN_RX2_SW | PASSIVE | 从此脚引线，标注精确网名`DN_RX2_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN6.1（1）。 [完整端点N0542](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0542)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 11 | S3 | DN_RX2 | PASSIVE | 从此脚引线，标注精确网名`DN_RX2`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.59（RX2）。 [完整端点N0541](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0541)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 12 | NC | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 13 | VDD | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 14 | S2 | DN_RX1 | PASSIVE | 从此脚引线，标注精确网名`DN_RX1`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.57（RX1）。 [完整端点N0539](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0539)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 15 | D2 | DN_RX1_SW | PASSIVE | 从此脚引线，标注精确网名`DN_RX1_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/R_ADC_IN5.1（1）。 [完整端点N0540](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0540)。 |
| CENTRAL | 05_RX_INPUT | U_RXSW_DN | ADG4612BRUZ | 16 | IN2 | RX_ENABLE_DN | IN | 从此脚引线，标注精确网名`RX_ENABLE_DN`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXG_DN.7（1Y）；05_RX_INPUT/U_RXSW_DN.1（IN1）；05_RX_INPUT/U_RXSW_DN.8（IN4）；05_RX_INPUT/U_RXSW_DN.9（IN3）。 [完整端点N0577](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0577)。 |

接完确认：电源/地/参考为U_RXSW_DN.4→GND；U_RXSW_DN.5→GND；U_RXSW_DN.13→V5A。 NC脚12逐个单独标记。

<a id="central-c-u-rxsw-dn"></a>

### 第028步：在CENTRAL／05_RX_INPUT放置 C_U_RXSW_DN

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_U_RXSW_DN**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_U_RXSW_DN | C0603C104K5RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 05_RX_INPUT | C_U_RXSW_DN | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RXSW_DN.1=`V5A`，C_U_RXSW_DN.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-in4"></a>

### 第029步：在CENTRAL／05_RX_INPUT放置 C_ADC_IN4

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_ADC_IN4**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_ADC_IN4 | C0603C102J5GACTU | 1 | 1 | ADC_IN4 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN4`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.57（V5+）；05_RX_INPUT/R_ADC_IN4.2（2）；05_RX_INPUT/R_ADC_BLEED4.1（1）。 [完整端点N0433](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0433)。 |
| CENTRAL | 05_RX_INPUT | C_ADC_IN4 | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_IN4.1=`ADC_IN4`，C_ADC_IN4.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-in5"></a>

### 第030步：在CENTRAL／05_RX_INPUT放置 C_ADC_IN5

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_ADC_IN5**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_ADC_IN5 | C0603C102J5GACTU | 1 | 1 | ADC_IN5 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN5`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.59（V6+）；05_RX_INPUT/R_ADC_IN5.2（2）；05_RX_INPUT/R_ADC_BLEED5.1（1）。 [完整端点N0434](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0434)。 |
| CENTRAL | 05_RX_INPUT | C_ADC_IN5 | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_IN5.1=`ADC_IN5`，C_ADC_IN5.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-in6"></a>

### 第031步：在CENTRAL／05_RX_INPUT放置 C_ADC_IN6

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_ADC_IN6**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_ADC_IN6 | C0603C102J5GACTU | 1 | 1 | ADC_IN6 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN6`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.61（V7+）；05_RX_INPUT/R_ADC_IN6.2（2）；05_RX_INPUT/R_ADC_BLEED6.1（1）。 [完整端点N0435](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0435)。 |
| CENTRAL | 05_RX_INPUT | C_ADC_IN6 | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_IN6.1=`ADC_IN6`，C_ADC_IN6.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-adc-in7"></a>

### 第032步：在CENTRAL／05_RX_INPUT放置 C_ADC_IN7

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **C_ADC_IN7**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | C_ADC_IN7 | C0603C102J5GACTU | 1 | 1 | ADC_IN7 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN7`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.63（V8+）；05_RX_INPUT/R_ADC_IN7.2（2）；05_RX_INPUT/R_ADC_BLEED7.1（1）。 [完整端点N0436](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0436)。 |
| CENTRAL | 05_RX_INPUT | C_ADC_IN7 | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ADC_IN7.1=`ADC_IN7`，C_ADC_IN7.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-bleed4"></a>

### 第033步：在CENTRAL／05_RX_INPUT放置 R_ADC_BLEED4

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_BLEED4**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED4 | CRCW06031M00FKEA | 1 | 1 | ADC_IN4 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN4`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.57（V5+）；05_RX_INPUT/R_ADC_IN4.2（2）；05_RX_INPUT/C_ADC_IN4.1（1）。 [完整端点N0433](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0433)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED4 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_BLEED4.1=`ADC_IN4`，R_ADC_BLEED4.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-bleed5"></a>

### 第034步：在CENTRAL／05_RX_INPUT放置 R_ADC_BLEED5

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_BLEED5**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED5 | CRCW06031M00FKEA | 1 | 1 | ADC_IN5 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN5`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.59（V6+）；05_RX_INPUT/R_ADC_IN5.2（2）；05_RX_INPUT/C_ADC_IN5.1（1）。 [完整端点N0434](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0434)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED5 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_BLEED5.1=`ADC_IN5`，R_ADC_BLEED5.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-bleed6"></a>

### 第035步：在CENTRAL／05_RX_INPUT放置 R_ADC_BLEED6

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_BLEED6**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED6 | CRCW06031M00FKEA | 1 | 1 | ADC_IN6 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN6`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.61（V7+）；05_RX_INPUT/R_ADC_IN6.2（2）；05_RX_INPUT/C_ADC_IN6.1（1）。 [完整端点N0435](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0435)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED6 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_BLEED6.1=`ADC_IN6`，R_ADC_BLEED6.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-bleed7"></a>

### 第036步：在CENTRAL／05_RX_INPUT放置 R_ADC_BLEED7

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_BLEED7**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED7 | CRCW06031M00FKEA | 1 | 1 | ADC_IN7 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN7`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.63（V8+）；05_RX_INPUT/R_ADC_IN7.2（2）；05_RX_INPUT/C_ADC_IN7.1（1）。 [完整端点N0436](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0436)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_BLEED7 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_BLEED7.1=`ADC_IN7`，R_ADC_BLEED7.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-in4"></a>

### 第037步：在CENTRAL／05_RX_INPUT放置 R_ADC_IN4

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_IN4**，精确型号 **CRCW0603499RFKEA**，封装 **0603**。其值为 **499**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_IN4 | CRCW0603499RFKEA | 1 | 1 | DN_RX0_SW | PASSIVE | 从此脚引线，标注精确网名`DN_RX0_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_DN.2（D1）。 [完整端点N0538](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0538)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_IN4 | CRCW0603499RFKEA | 2 | 2 | ADC_IN4 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN4`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.57（V5+）；05_RX_INPUT/C_ADC_IN4.1（1）；05_RX_INPUT/R_ADC_BLEED4.1（1）。 [完整端点N0433](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0433)。 |

接完确认：R_ADC_IN4.1=`DN_RX0_SW`，R_ADC_IN4.2=`ADC_IN4`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-in5"></a>

### 第038步：在CENTRAL／05_RX_INPUT放置 R_ADC_IN5

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_IN5**，精确型号 **CRCW0603499RFKEA**，封装 **0603**。其值为 **499**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_IN5 | CRCW0603499RFKEA | 1 | 1 | DN_RX1_SW | PASSIVE | 从此脚引线，标注精确网名`DN_RX1_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_DN.15（D2）。 [完整端点N0540](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0540)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_IN5 | CRCW0603499RFKEA | 2 | 2 | ADC_IN5 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN5`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.59（V6+）；05_RX_INPUT/C_ADC_IN5.1（1）；05_RX_INPUT/R_ADC_BLEED5.1（1）。 [完整端点N0434](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0434)。 |

接完确认：R_ADC_IN5.1=`DN_RX1_SW`，R_ADC_IN5.2=`ADC_IN5`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-in6"></a>

### 第039步：在CENTRAL／05_RX_INPUT放置 R_ADC_IN6

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_IN6**，精确型号 **CRCW0603499RFKEA**，封装 **0603**。其值为 **499**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_IN6 | CRCW0603499RFKEA | 1 | 1 | DN_RX2_SW | PASSIVE | 从此脚引线，标注精确网名`DN_RX2_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_DN.10（D3）。 [完整端点N0542](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0542)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_IN6 | CRCW0603499RFKEA | 2 | 2 | ADC_IN6 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN6`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.61（V7+）；05_RX_INPUT/C_ADC_IN6.1（1）；05_RX_INPUT/R_ADC_BLEED6.1（1）。 [完整端点N0435](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0435)。 |

接完确认：R_ADC_IN6.1=`DN_RX2_SW`，R_ADC_IN6.2=`ADC_IN6`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-in7"></a>

### 第040步：在CENTRAL／05_RX_INPUT放置 R_ADC_IN7

在 **CENTRAL板的05_RX_INPUT图页**，接着放置 **R_ADC_IN7**，精确型号 **CRCW0603499RFKEA**，封装 **0603**。其值为 **499**。

纸面位置：紧邻本页U_RXSW_DN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 05_RX_INPUT | R_ADC_IN7 | CRCW0603499RFKEA | 1 | 1 | DN_RX3_SW | PASSIVE | 从此脚引线，标注精确网名`DN_RX3_SW`；跨页使用同名板内标签。同网还接：05_RX_INPUT/U_RXSW_DN.7（D4）。 [完整端点N0544](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0544)。 |
| CENTRAL | 05_RX_INPUT | R_ADC_IN7 | CRCW0603499RFKEA | 2 | 2 | ADC_IN7 | PASSIVE | 从此脚引线，标注精确网名`ADC_IN7`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.63（V8+）；05_RX_INPUT/C_ADC_IN7.1（1）；05_RX_INPUT/R_ADC_BLEED7.1（1）。 [完整端点N0436](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0436)。 |

接完确认：R_ADC_IN7.1=`DN_RX3_SW`，R_ADC_IN7.2=`ADC_IN7`；不可旁路该器件把两个网名短在一起。

本页完成核对：**40个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。
