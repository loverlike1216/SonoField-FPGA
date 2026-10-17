# CENTRAL／06_I2C_TEMP_SAFETY逐步连接分册

本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。

<a id="page-central-06-i2c-temp-safety"></a>

## CENTRAL板／06_I2C_TEMP_SAFETY图页

从左到右：AX I2C域转换→MUX→三条温度支路。下方放本板健康逻辑和返回AX的故障/PG翻译器。电源监测器本体在00_POWER。

<a id="central-u-i2c-main"></a>

### 第001步：在CENTRAL／06_I2C_TEMP_SAFETY放置 U_I2C_MAIN

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，先放置 **U_I2C_MAIN**，精确型号 **TCA9517DGKR**，封装 **DGK/VSSOP8**。

放在AX侧I2C与中央MUX之间，A侧供电AX_VIO_REF3V3、B侧本地V3V3；分域退耦及上拉不混接。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_I2C_MAIN | TCA9517DGKR | 1 | VCCA | AX_VIO_REF3V3 | POWER | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_I2C_MAIN | TCA9517DGKR | 2 | SCLA | FPGA_SCL | OD | 从此脚引线，标注精确网名`FPGA_SCL`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.29（EX_IO2_14N）；06_I2C_TEMP_SAFETY/R_FPGA_I2C_SCL.1（1）。 [完整端点N0560](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0560)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_I2C_MAIN | TCA9517DGKR | 3 | SDAA | FPGA_SDA | OD | 从此脚引线，标注精确网名`FPGA_SDA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.30（EX_IO2_14P）；06_I2C_TEMP_SAFETY/R_FPGA_I2C_SDA.1（1）。 [完整端点N0561](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0561)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_I2C_MAIN | TCA9517DGKR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_I2C_MAIN | TCA9517DGKR | 5 | EN | LOCAL_OK | IN | 从此脚引线，标注精确网名`LOCAL_OK`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_G1.7（1Y）；06_I2C_TEMP_SAFETY/U_G1.5（2A）。 [完整端点N0567](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0567)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_I2C_MAIN | TCA9517DGKR | 6 | SDAB | I2C_SDA | OD | 从此脚引线，标注精确网名`I2C_SDA`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_MUX_I2C_SDA.1（1）；06_I2C_TEMP_SAFETY/U_MUX.23（SDA）。 [完整端点N0565](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0565)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_I2C_MAIN | TCA9517DGKR | 7 | SCLB | I2C_SCL | OD | 从此脚引线，标注精确网名`I2C_SCL`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_MUX_I2C_SCL.1（1）；06_I2C_TEMP_SAFETY/U_MUX.22（SCL）。 [完整端点N0564](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0564)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_I2C_MAIN | TCA9517DGKR | 8 | VCCB | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_I2C_MAIN.1→AX_VIO_REF3V3；U_I2C_MAIN.4→GND；U_I2C_MAIN.8→V3V3。

<a id="central-c-u-i2c-main-a"></a>

### 第002步：在CENTRAL／06_I2C_TEMP_SAFETY放置 C_U_I2C_MAIN_A

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **C_U_I2C_MAIN_A**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_I2C_MAIN的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_I2C_MAIN_A | C0603C104K5RACTU | 1 | 1 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_I2C_MAIN_A | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_I2C_MAIN_A.1=`AX_VIO_REF3V3`，C_U_I2C_MAIN_A.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-u-i2c-main-b"></a>

### 第003步：在CENTRAL／06_I2C_TEMP_SAFETY放置 C_U_I2C_MAIN_B

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **C_U_I2C_MAIN_B**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_I2C_MAIN的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_I2C_MAIN_B | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_I2C_MAIN_B | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_I2C_MAIN_B.1=`V3V3`，C_U_I2C_MAIN_B.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-fpga-i2c-scl"></a>

### 第004步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_FPGA_I2C_SCL

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_FPGA_I2C_SCL**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_I2C_MAIN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_FPGA_I2C_SCL | CRCW06032K20FKEA | 1 | 1 | FPGA_SCL | PASSIVE | 从此脚引线，标注精确网名`FPGA_SCL`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.29（EX_IO2_14N）；06_I2C_TEMP_SAFETY/U_I2C_MAIN.2（SCLA）。 [完整端点N0560](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0560)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_FPGA_I2C_SCL | CRCW06032K20FKEA | 2 | 2 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |

接完确认：R_FPGA_I2C_SCL.1=`FPGA_SCL`，R_FPGA_I2C_SCL.2=`AX_VIO_REF3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-fpga-i2c-sda"></a>

### 第005步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_FPGA_I2C_SDA

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_FPGA_I2C_SDA**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_I2C_MAIN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_FPGA_I2C_SDA | CRCW06032K20FKEA | 1 | 1 | FPGA_SDA | PASSIVE | 从此脚引线，标注精确网名`FPGA_SDA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.30（EX_IO2_14P）；06_I2C_TEMP_SAFETY/U_I2C_MAIN.3（SDAA）。 [完整端点N0561](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0561)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_FPGA_I2C_SDA | CRCW06032K20FKEA | 2 | 2 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |

接完确认：R_FPGA_I2C_SDA.1=`FPGA_SDA`，R_FPGA_I2C_SDA.2=`AX_VIO_REF3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-mux-i2c-scl"></a>

### 第006步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_MUX_I2C_SCL

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_MUX_I2C_SCL**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_I2C_MAIN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_MUX_I2C_SCL | CRCW06032K20FKEA | 1 | 1 | I2C_SCL | PASSIVE | 从此脚引线，标注精确网名`I2C_SCL`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_I2C_MAIN.7（SCLB）；06_I2C_TEMP_SAFETY/U_MUX.22（SCL）。 [完整端点N0564](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0564)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_MUX_I2C_SCL | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_MUX_I2C_SCL.1=`I2C_SCL`，R_MUX_I2C_SCL.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-mux-i2c-sda"></a>

### 第007步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_MUX_I2C_SDA

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_MUX_I2C_SDA**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_I2C_MAIN的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_MUX_I2C_SDA | CRCW06032K20FKEA | 1 | 1 | I2C_SDA | PASSIVE | 从此脚引线，标注精确网名`I2C_SDA`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_I2C_MAIN.6（SDAB）；06_I2C_TEMP_SAFETY/U_MUX.23（SDA）。 [完整端点N0565](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0565)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_MUX_I2C_SDA | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_MUX_I2C_SDA.1=`I2C_SDA`，R_MUX_I2C_SDA.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-u-mux"></a>

### 第008步：在CENTRAL／06_I2C_TEMP_SAFETY放置 U_MUX

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **U_MUX**，精确型号 **TCA9548APWR**，封装 **PW/TSSOP24**。

放在中央I2C主侧与三支路之间；TCA9548A为0x70，通道0中央、1上阵列、2下阵列。一次只选一路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 1 | A0 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 2 | A1 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 3 | RESET_N | POR_N | IN | 从此脚引线，标注精确网名`POR_N`；跨页使用同名板内标签。同网还接：00_POWER/U_POR.6（RESET_N）；00_POWER/R_U_POR_PU.1（1）；06_I2C_TEMP_SAFETY/U_G1.1（1A）。 [完整端点N0574](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0574)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 4 | SDA0 | TEMP_C_SDA | OD | 从此脚引线，标注精确网名`TEMP_C_SDA`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_TEMP_C_SDA.1（1）；06_I2C_TEMP_SAFETY/U_TEMP.6（SDA）。 [完整端点N0580](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0580)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 5 | SCL0 | TEMP_C_SCL | OD | 从此脚引线，标注精确网名`TEMP_C_SCL`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_TEMP_C_SCL.1（1）；06_I2C_TEMP_SAFETY/U_TEMP.1（SCL）。 [完整端点N0579](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0579)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 6 | SDA1 | UP_SDA | OD | 从此脚引线，标注精确网名`UP_SDA`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.53（SDA）；06_I2C_TEMP_SAFETY/R_UP_SDA.1（1）。 [完整端点N0669](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0669)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 7 | SCL1 | UP_SCL | OD | 从此脚引线，标注精确网名`UP_SCL`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.51（SCL）；06_I2C_TEMP_SAFETY/R_UP_SCL.1（1）。 [完整端点N0668](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0668)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 8 | SDA2 | DN_SDA | OD | 从此脚引线，标注精确网名`DN_SDA`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.53（SDA）；06_I2C_TEMP_SAFETY/R_DN_SDA.1（1）。 [完整端点N0549](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0549)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 9 | SCL2 | DN_SCL | OD | 从此脚引线，标注精确网名`DN_SCL`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.51（SCL）；06_I2C_TEMP_SAFETY/R_DN_SCL.1（1）。 [完整端点N0548](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0548)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 10 | SDA3 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 11 | SCL3 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 12 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 13 | SDA4 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 14 | SCL4 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 15 | SDA5 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 16 | SCL5 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 17 | SDA6 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 18 | SCL6 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 19 | SDA7 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 20 | SCL7 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 21 | A2 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 22 | SCL | I2C_SCL | OD | 从此脚引线，标注精确网名`I2C_SCL`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_I2C_MAIN.7（SCLB）；06_I2C_TEMP_SAFETY/R_MUX_I2C_SCL.1（1）。 [完整端点N0564](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0564)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 23 | SDA | I2C_SDA | OD | 从此脚引线，标注精确网名`I2C_SDA`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_I2C_MAIN.6（SDAB）；06_I2C_TEMP_SAFETY/R_MUX_I2C_SDA.1（1）。 [完整端点N0565](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0565)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_MUX | TCA9548APWR | 24 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_MUX.1→GND；U_MUX.2→GND；U_MUX.12→GND；U_MUX.21→GND；U_MUX.24→V3V3。 NC脚10,11,13,14,15,16,17,18,19,20逐个单独标记。

<a id="central-c-u-mux"></a>

### 第009步：在CENTRAL／06_I2C_TEMP_SAFETY放置 C_U_MUX

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **C_U_MUX**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_MUX的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_MUX | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_MUX | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_MUX.1=`V3V3`，C_U_MUX.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-dn-scl"></a>

### 第010步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_DN_SCL

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_DN_SCL**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_MUX的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_DN_SCL | CRCW06032K20FKEA | 1 | 1 | DN_SCL | PASSIVE | 从此脚引线，标注精确网名`DN_SCL`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.51（SCL）；06_I2C_TEMP_SAFETY/U_MUX.9（SCL2）。 [完整端点N0548](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0548)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_DN_SCL | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_DN_SCL.1=`DN_SCL`，R_DN_SCL.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-dn-sda"></a>

### 第011步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_DN_SDA

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_DN_SDA**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_MUX的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_DN_SDA | CRCW06032K20FKEA | 1 | 1 | DN_SDA | PASSIVE | 从此脚引线，标注精确网名`DN_SDA`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.53（SDA）；06_I2C_TEMP_SAFETY/U_MUX.8（SDA2）。 [完整端点N0549](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0549)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_DN_SDA | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_DN_SDA.1=`DN_SDA`，R_DN_SDA.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-temp-c-scl"></a>

### 第012步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_TEMP_C_SCL

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_TEMP_C_SCL**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_MUX的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_TEMP_C_SCL | CRCW06032K20FKEA | 1 | 1 | TEMP_C_SCL | PASSIVE | 从此脚引线，标注精确网名`TEMP_C_SCL`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_MUX.5（SCL0）；06_I2C_TEMP_SAFETY/U_TEMP.1（SCL）。 [完整端点N0579](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0579)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_TEMP_C_SCL | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_TEMP_C_SCL.1=`TEMP_C_SCL`，R_TEMP_C_SCL.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-temp-c-sda"></a>

### 第013步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_TEMP_C_SDA

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_TEMP_C_SDA**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_MUX的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_TEMP_C_SDA | CRCW06032K20FKEA | 1 | 1 | TEMP_C_SDA | PASSIVE | 从此脚引线，标注精确网名`TEMP_C_SDA`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_MUX.4（SDA0）；06_I2C_TEMP_SAFETY/U_TEMP.6（SDA）。 [完整端点N0580](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0580)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_TEMP_C_SDA | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_TEMP_C_SDA.1=`TEMP_C_SDA`，R_TEMP_C_SDA.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-up-scl"></a>

### 第014步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_UP_SCL

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_UP_SCL**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_MUX的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_UP_SCL | CRCW06032K20FKEA | 1 | 1 | UP_SCL | PASSIVE | 从此脚引线，标注精确网名`UP_SCL`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.51（SCL）；06_I2C_TEMP_SAFETY/U_MUX.7（SCL1）。 [完整端点N0668](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0668)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_UP_SCL | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_UP_SCL.1=`UP_SCL`，R_UP_SCL.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-up-sda"></a>

### 第015步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_UP_SDA

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_UP_SDA**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_MUX的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_UP_SDA | CRCW06032K20FKEA | 1 | 1 | UP_SDA | PASSIVE | 从此脚引线，标注精确网名`UP_SDA`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.53（SDA）；06_I2C_TEMP_SAFETY/U_MUX.6（SDA1）。 [完整端点N0669](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0669)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_UP_SDA | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_UP_SDA.1=`UP_SDA`，R_UP_SDA.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-u-temp"></a>

### 第016步：在CENTRAL／06_I2C_TEMP_SAFETY放置 U_TEMP

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **U_TEMP**，精确型号 **TMP117NAIDRVR**，封装 **DRV/WSON6**。

放在本页I2C支路末端；三个板上的TMP117均为0x48，ADD0接GND；EP接GND。ALERT及其上拉按原表保留。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_TEMP | TMP117NAIDRVR | 1 | SCL | TEMP_C_SCL | IN | 从此脚引线，标注精确网名`TEMP_C_SCL`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_TEMP_C_SCL.1（1）；06_I2C_TEMP_SAFETY/U_MUX.5（SCL0）。 [完整端点N0579](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0579)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_TEMP | TMP117NAIDRVR | 2 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_TEMP | TMP117NAIDRVR | 3 | ALERT | U_TEMP_ALERT_N | OD | 从此脚引线，标注精确网名`U_TEMP_ALERT_N`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_U_TEMP_ALERT.1（1）。 [完整端点N0677](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0677)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_TEMP | TMP117NAIDRVR | 4 | ADD0 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_TEMP | TMP117NAIDRVR | 5 | V+ | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_TEMP | TMP117NAIDRVR | 6 | SDA | TEMP_C_SDA | OD | 从此脚引线，标注精确网名`TEMP_C_SDA`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/R_TEMP_C_SDA.1（1）；06_I2C_TEMP_SAFETY/U_MUX.4（SDA0）。 [完整端点N0580](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0580)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_TEMP | TMP117NAIDRVR | EP | PAD | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为U_TEMP.2→GND；U_TEMP.4→GND；U_TEMP.5→V3V3；U_TEMP.EP→GND。

<a id="central-c-u-temp"></a>

### 第017步：在CENTRAL／06_I2C_TEMP_SAFETY放置 C_U_TEMP

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **C_U_TEMP**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_TEMP的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_TEMP | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_TEMP | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_TEMP.1=`V3V3`，C_U_TEMP.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-u-temp-alert"></a>

### 第018步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_U_TEMP_ALERT

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_U_TEMP_ALERT**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TEMP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_U_TEMP_ALERT | CRCW060310K0FKEA | 1 | 1 | U_TEMP_ALERT_N | PASSIVE | 从此脚引线，标注精确网名`U_TEMP_ALERT_N`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_TEMP.3（ALERT）。 [完整端点N0677](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0677)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_U_TEMP_ALERT | CRCW060310K0FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_U_TEMP_ALERT.1=`U_TEMP_ALERT_N`，R_U_TEMP_ALERT.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-u-g1"></a>

### 第019步：在CENTRAL／06_I2C_TEMP_SAFETY放置 U_G1

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **U_G1**，精确型号 **SN74LVC2G08DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_G1 | SN74LVC2G08DCUR | 1 | 1A | POR_N | IN | 从此脚引线，标注精确网名`POR_N`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_MUX.3（RESET_N）；00_POWER/U_POR.6（RESET_N）；00_POWER/R_U_POR_PU.1（1）。 [完整端点N0574](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0574)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_G1 | SN74LVC2G08DCUR | 2 | 1B | V5_GOOD | IN | 从此脚引线，标注精确网名`V5_GOOD`；跨页使用同名板内标签。同网还接：00_POWER/U_5MON.6（RESET_N）；00_POWER/R_5GOOD.1（1）；05_RX_INPUT/U_RXG_UP.1（1A）；05_RX_INPUT/U_RXG_DN.1（1A）。 [完整端点N0683](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0683)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_G1 | SN74LVC2G08DCUR | 3 | 2Y | CENTRAL_READY | OUT | 从此脚引线，标注精确网名`CENTRAL_READY`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.11（A4）；02_TX_BUFFERS/U_CBUF2.13（A5）；06_I2C_TEMP_SAFETY/U_RET1.17（B5）。 [完整端点N0457](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0457)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_G1 | SN74LVC2G08DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_G1 | SN74LVC2G08DCUR | 5 | 2A | LOCAL_OK | IN | 从此脚引线，标注精确网名`LOCAL_OK`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_I2C_MAIN.5（EN）；06_I2C_TEMP_SAFETY/U_G1.7（1Y）。 [完整端点N0567](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0567)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_G1 | SN74LVC2G08DCUR | 6 | 2B | AX_VIO_REF3V3 | IN | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_G1 | SN74LVC2G08DCUR | 7 | 1Y | LOCAL_OK | OUT | 从此脚引线，标注精确网名`LOCAL_OK`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_I2C_MAIN.5（EN）；06_I2C_TEMP_SAFETY/U_G1.5（2A）。 [完整端点N0567](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0567)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_G1 | SN74LVC2G08DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_G1.6→AX_VIO_REF3V3；U_G1.4→GND；U_G1.8→V3V3。

<a id="central-c-u-g1"></a>

### 第020步：在CENTRAL／06_I2C_TEMP_SAFETY放置 C_U_G1

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **C_U_G1**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_G1的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_G1 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_G1 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_G1.1=`V3V3`，C_U_G1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-ret1"></a>

### 第021步：在CENTRAL／06_I2C_TEMP_SAFETY放置 U_RET1

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **U_RET1**，精确型号 **SN74LVC8T245PWR**，封装 **PW/TSSOP24**。

放在中央健康/故障返回信号旁；VCCA使用AX_VIO_REF3V3，VCCB使用本地V3V3。ADC_BUSY也经过本芯片返回AX。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 1 | VCCA | AX_VIO_REF3V3 | POWER | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 2 | DIR | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 3 | A1 | UP_PGOOD_FPGA | OUT | 从此脚引线，标注精确网名`UP_PGOOD_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.26（EX_IO1_12P）；06_I2C_TEMP_SAFETY/R_RETURN_PD_U_RET1_3.1（1）。 [完整端点N0654](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0654)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 4 | A2 | DN_PGOOD_FPGA | OUT | 从此脚引线，标注精确网名`DN_PGOOD_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.26（EX_IO2_12P）；06_I2C_TEMP_SAFETY/R_RETURN_PD_U_RET1_4.1（1）。 [完整端点N0534](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0534)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 5 | A3 | UP_FAULT_N_FPGA | OUT | 从此脚引线，标注精确网名`UP_FAULT_N_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.27（EX_IO1_13N）；06_I2C_TEMP_SAFETY/R_RETURN_PD_U_RET1_5.1（1）。 [完整端点N0648](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0648)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 6 | A4 | DN_FAULT_N_FPGA | OUT | 从此脚引线，标注精确网名`DN_FAULT_N_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.27（EX_IO2_13N）；06_I2C_TEMP_SAFETY/R_RETURN_PD_U_RET1_6.1（1）。 [完整端点N0528](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0528)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 7 | A5 | GLOBAL_OK_FPGA | OUT | 从此脚引线，标注精确网名`GLOBAL_OK_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.31（EX_IO2_15N）；06_I2C_TEMP_SAFETY/R_RETURN_PD_U_RET1_7.1（1）。 [完整端点N0562](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0562)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 8 | A6 | ADC_BUSY_FPGA | OUT | 从此脚引线，标注精确网名`ADC_BUSY_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.32（EX_IO1_15P）；06_I2C_TEMP_SAFETY/R_RETURN_PD_U_RET1_8.1（1）。 [完整端点N0406](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0406)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 9 | A7 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 10 | A8 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 11 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 12 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 13 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 14 | B8 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 15 | B7 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 16 | B6 | ADC_BUSY_3V3 | IN | 从此脚引线，标注精确网名`ADC_BUSY_3V3`；跨页使用同名板内标签。同网还接：04_ADC/U_BUSYBUF.4（Y）。 [完整端点N0405](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0405)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 17 | B5 | CENTRAL_READY | IN | 从此脚引线，标注精确网名`CENTRAL_READY`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.11（A4）；02_TX_BUFFERS/U_CBUF2.13（A5）；06_I2C_TEMP_SAFETY/U_G1.3（2Y）。 [完整端点N0457](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0457)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 18 | B4 | DN_FAULT_N | IN | 从此脚引线，标注精确网名`DN_FAULT_N`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.47（FAULT_N）；06_I2C_TEMP_SAFETY/R_FAULT_DN.1（1）。 [完整端点N0527](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0527)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 19 | B3 | UP_FAULT_N | IN | 从此脚引线，标注精确网名`UP_FAULT_N`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.47（FAULT_N）；06_I2C_TEMP_SAFETY/R_FAULT_UP.1（1）。 [完整端点N0647](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0647)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 20 | B2 | DN_PGOOD | IN | 从此脚引线，标注精确网名`DN_PGOOD`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.49（PGOOD）；06_I2C_TEMP_SAFETY/R_PG_DN.1（1）。 [完整端点N0533](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0533)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 21 | B1 | UP_PGOOD | IN | 从此脚引线，标注精确网名`UP_PGOOD`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.49（PGOOD）；06_I2C_TEMP_SAFETY/R_PG_UP.1（1）。 [完整端点N0653](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0653)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 22 | OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 23 | VCCB | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | U_RET1 | SN74LVC8T245PWR | 24 | VCCB | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_RET1.1→AX_VIO_REF3V3；U_RET1.2→GND；U_RET1.11→GND；U_RET1.12→GND；U_RET1.13→GND；U_RET1.22→GND；U_RET1.23→V3V3；U_RET1.24→V3V3；U_RET1.15→GND；U_RET1.14→GND。 NC脚9,10逐个单独标记。

<a id="central-c-u-ret1-a"></a>

### 第022步：在CENTRAL／06_I2C_TEMP_SAFETY放置 C_U_RET1_A

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **C_U_RET1_A**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_RET1_A | C0603C104K5RACTU | 1 | 1 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.2（2）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_RET1_A | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RET1_A.1=`AX_VIO_REF3V3`，C_U_RET1_A.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-u-ret1-b"></a>

### 第023步：在CENTRAL／06_I2C_TEMP_SAFETY放置 C_U_RET1_B

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **C_U_RET1_B**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_RET1_B | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | C_U_RET1_B | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_RET1_B.1=`V3V3`，C_U_RET1_B.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-adc-return-pd-busy"></a>

### 第024步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_ADC_RETURN_PD_BUSY

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_ADC_RETURN_PD_BUSY**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_ADC_RETURN_PD_BUSY | CRCW0603100KFKEA | 1 | 1 | ADC_BUSY | PASSIVE | 从此脚引线，标注精确网名`ADC_BUSY`；跨页使用同名板内标签。同网还接：04_ADC/U_ADC.14（BUSY）；04_ADC/U_BUSYBUF.2（A）。 [完整端点N0404](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0404)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_ADC_RETURN_PD_BUSY | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ADC_RETURN_PD_BUSY.1=`ADC_BUSY`，R_ADC_RETURN_PD_BUSY.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-fault-dn"></a>

### 第025步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_FAULT_DN

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_FAULT_DN**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_FAULT_DN | CRCW060310K0FKEA | 1 | 1 | DN_FAULT_N | PASSIVE | 从此脚引线，标注精确网名`DN_FAULT_N`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.47（FAULT_N）；06_I2C_TEMP_SAFETY/U_RET1.18（B4）。 [完整端点N0527](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0527)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_FAULT_DN | CRCW060310K0FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_FAULT_DN.1=`DN_FAULT_N`，R_FAULT_DN.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-fault-up"></a>

### 第026步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_FAULT_UP

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_FAULT_UP**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_FAULT_UP | CRCW060310K0FKEA | 1 | 1 | UP_FAULT_N | PASSIVE | 从此脚引线，标注精确网名`UP_FAULT_N`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.47（FAULT_N）；06_I2C_TEMP_SAFETY/U_RET1.19（B3）。 [完整端点N0647](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0647)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_FAULT_UP | CRCW060310K0FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_FAULT_UP.1=`UP_FAULT_N`，R_FAULT_UP.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-pg-dn"></a>

### 第027步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_PG_DN

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_PG_DN**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_PG_DN | CRCW060310K0FKEA | 1 | 1 | DN_PGOOD | PASSIVE | 从此脚引线，标注精确网名`DN_PGOOD`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.49（PGOOD）；06_I2C_TEMP_SAFETY/U_RET1.20（B2）。 [完整端点N0533](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0533)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_PG_DN | CRCW060310K0FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_PG_DN.1=`DN_PGOOD`，R_PG_DN.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-pg-up"></a>

### 第028步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_PG_UP

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_PG_UP**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_PG_UP | CRCW060310K0FKEA | 1 | 1 | UP_PGOOD | PASSIVE | 从此脚引线，标注精确网名`UP_PGOOD`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.49（PGOOD）；06_I2C_TEMP_SAFETY/U_RET1.21（B1）。 [完整端点N0653](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0653)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_PG_UP | CRCW060310K0FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_PG_UP.1=`UP_PGOOD`，R_PG_UP.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret1-3"></a>

### 第029步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_RETURN_PD_U_RET1_3

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_RETURN_PD_U_RET1_3**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_3 | RC0603FR-0710KL | 1 | 1 | UP_PGOOD_FPGA | PASSIVE | 从此脚引线，标注精确网名`UP_PGOOD_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.26（EX_IO1_12P）；06_I2C_TEMP_SAFETY/U_RET1.3（A1）。 [完整端点N0654](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0654)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_3 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET1_3.1=`UP_PGOOD_FPGA`，R_RETURN_PD_U_RET1_3.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret1-4"></a>

### 第030步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_RETURN_PD_U_RET1_4

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_RETURN_PD_U_RET1_4**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_4 | RC0603FR-0710KL | 1 | 1 | DN_PGOOD_FPGA | PASSIVE | 从此脚引线，标注精确网名`DN_PGOOD_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.26（EX_IO2_12P）；06_I2C_TEMP_SAFETY/U_RET1.4（A2）。 [完整端点N0534](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0534)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_4 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET1_4.1=`DN_PGOOD_FPGA`，R_RETURN_PD_U_RET1_4.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret1-5"></a>

### 第031步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_RETURN_PD_U_RET1_5

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_RETURN_PD_U_RET1_5**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_5 | RC0603FR-0710KL | 1 | 1 | UP_FAULT_N_FPGA | PASSIVE | 从此脚引线，标注精确网名`UP_FAULT_N_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.27（EX_IO1_13N）；06_I2C_TEMP_SAFETY/U_RET1.5（A3）。 [完整端点N0648](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0648)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_5 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET1_5.1=`UP_FAULT_N_FPGA`，R_RETURN_PD_U_RET1_5.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret1-6"></a>

### 第032步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_RETURN_PD_U_RET1_6

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_RETURN_PD_U_RET1_6**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_6 | RC0603FR-0710KL | 1 | 1 | DN_FAULT_N_FPGA | PASSIVE | 从此脚引线，标注精确网名`DN_FAULT_N_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.27（EX_IO2_13N）；06_I2C_TEMP_SAFETY/U_RET1.6（A4）。 [完整端点N0528](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0528)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_6 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET1_6.1=`DN_FAULT_N_FPGA`，R_RETURN_PD_U_RET1_6.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret1-7"></a>

### 第033步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_RETURN_PD_U_RET1_7

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_RETURN_PD_U_RET1_7**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_7 | RC0603FR-0710KL | 1 | 1 | GLOBAL_OK_FPGA | PASSIVE | 从此脚引线，标注精确网名`GLOBAL_OK_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.31（EX_IO2_15N）；06_I2C_TEMP_SAFETY/U_RET1.7（A5）。 [完整端点N0562](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0562)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_7 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET1_7.1=`GLOBAL_OK_FPGA`，R_RETURN_PD_U_RET1_7.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-return-pd-u-ret1-8"></a>

### 第034步：在CENTRAL／06_I2C_TEMP_SAFETY放置 R_RETURN_PD_U_RET1_8

在 **CENTRAL板的06_I2C_TEMP_SAFETY图页**，接着放置 **R_RETURN_PD_U_RET1_8**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_RET1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_8 | RC0603FR-0710KL | 1 | 1 | ADC_BUSY_FPGA | PASSIVE | 从此脚引线，标注精确网名`ADC_BUSY_FPGA`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.32（EX_IO1_15P）；06_I2C_TEMP_SAFETY/U_RET1.8（A6）。 [完整端点N0406](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0406)。 |
| CENTRAL | 06_I2C_TEMP_SAFETY | R_RETURN_PD_U_RET1_8 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_RETURN_PD_U_RET1_8.1=`ADC_BUSY_FPGA`，R_RETURN_PD_U_RET1_8.2=`GND`；不可旁路该器件把两个网名短在一起。

本页完成核对：**34个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。
