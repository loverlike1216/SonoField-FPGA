# CENTRAL／02_TX_BUFFERS逐步连接分册

本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。

<a id="page-central-02-tx-buffers"></a>

## CENTRAL板／02_TX_BUFFERS图页

左侧放DATA输入串阻/滤波，中央放4颗数据LVT和1颗时钟LVT，右侧放UP/DN输出串阻。控制信号使用原LVC缓冲。原AX7020板载33Ω不再新增进本板BOM。

<a id="central-u-txb0"></a>

### 第001步：在CENTRAL／02_TX_BUFFERS放置 U_TXB0

在 **CENTRAL板的02_TX_BUFFERS图页**，先放置 **U_TXB0**，精确型号 **SN74LVT244BPWR**，封装 **PW/TSSOP20**。

按信号从接口到输出的顺序摆放LVT缓冲，供电本地V3V3、地GND；PW20无EP。每个通道A/Y和两个OE_N按实际脚号，未用输入接表定网络、未用输出独立NC。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 1 | 1OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 2 | A0 | UP_DATA_FILT_00 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP00.2（2）；02_TX_BUFFERS/C_RX_UP00.1（1）。 [完整端点N0615](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0615)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 3 | Y7 | UP_DATA_DRV_07 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP07.1（1）。 [完整端点N0606](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0606)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 4 | A1 | UP_DATA_FILT_01 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP01.2（2）；02_TX_BUFFERS/C_RX_UP01.1（1）。 [完整端点N0616](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0616)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 5 | Y6 | UP_DATA_DRV_06 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP06.1（1）。 [完整端点N0605](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0605)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 6 | A2 | UP_DATA_FILT_02 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP02.2（2）；02_TX_BUFFERS/C_RX_UP02.1（1）。 [完整端点N0617](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0617)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 7 | Y5 | UP_DATA_DRV_05 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP05.1（1）。 [完整端点N0604](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0604)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 8 | A3 | UP_DATA_FILT_03 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP03.2（2）；02_TX_BUFFERS/C_RX_UP03.1（1）。 [完整端点N0618](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0618)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 9 | Y4 | UP_DATA_DRV_04 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP04.1（1）。 [完整端点N0603](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0603)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 10 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 11 | A4 | UP_DATA_FILT_04 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP04.2（2）；02_TX_BUFFERS/C_RX_UP04.1（1）。 [完整端点N0619](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0619)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 12 | Y3 | UP_DATA_DRV_03 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP03.1（1）。 [完整端点N0602](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0602)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 13 | A5 | UP_DATA_FILT_05 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP05.2（2）；02_TX_BUFFERS/C_RX_UP05.1（1）。 [完整端点N0620](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0620)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 14 | Y2 | UP_DATA_DRV_02 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP02.1（1）。 [完整端点N0601](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0601)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 15 | A6 | UP_DATA_FILT_06 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP06.2（2）；02_TX_BUFFERS/C_RX_UP06.1（1）。 [完整端点N0621](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0621)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 16 | Y1 | UP_DATA_DRV_01 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP01.1（1）。 [完整端点N0600](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0600)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 17 | A7 | UP_DATA_FILT_07 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP07.2（2）；02_TX_BUFFERS/C_RX_UP07.1（1）。 [完整端点N0622](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0622)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 18 | Y0 | UP_DATA_DRV_00 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP00.1（1）。 [完整端点N0599](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0599)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 19 | 2OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB0 | SN74LVT244BPWR | 20 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_TXB0.1→GND；U_TXB0.19→GND；U_TXB0.10→GND；U_TXB0.20→V3V3。

<a id="central-c-u-txb0"></a>

### 第002步：在CENTRAL／02_TX_BUFFERS放置 C_U_TXB0

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_U_TXB0**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_U_TXB0 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 02_TX_BUFFERS | C_U_TXB0 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_TXB0.1=`V3V3`，C_U_TXB0.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up00"></a>

### 第003步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP00

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP00**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP00 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_00 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP00.2（2）；02_TX_BUFFERS/U_TXB0.2（A0）。 [完整端点N0615](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0615)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP00 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP00.1=`UP_DATA_FILT_00`，C_RX_UP00.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up01"></a>

### 第004步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP01

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP01**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP01 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_01 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP01.2（2）；02_TX_BUFFERS/U_TXB0.4（A1）。 [完整端点N0616](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0616)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP01 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP01.1=`UP_DATA_FILT_01`，C_RX_UP01.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up02"></a>

### 第005步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP02

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP02**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP02 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_02 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP02.2（2）；02_TX_BUFFERS/U_TXB0.6（A2）。 [完整端点N0617](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0617)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP02 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP02.1=`UP_DATA_FILT_02`，C_RX_UP02.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up03"></a>

### 第006步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP03

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP03**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP03 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_03 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP03.2（2）；02_TX_BUFFERS/U_TXB0.8（A3）。 [完整端点N0618](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0618)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP03 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP03.1=`UP_DATA_FILT_03`，C_RX_UP03.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up04"></a>

### 第007步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP04

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP04**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP04 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_04 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP04.2（2）；02_TX_BUFFERS/U_TXB0.11（A4）。 [完整端点N0619](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0619)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP04 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP04.1=`UP_DATA_FILT_04`，C_RX_UP04.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up05"></a>

### 第008步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP05

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP05**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP05 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_05 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP05.2（2）；02_TX_BUFFERS/U_TXB0.13（A5）。 [完整端点N0620](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0620)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP05 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP05.1=`UP_DATA_FILT_05`，C_RX_UP05.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up06"></a>

### 第009步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP06

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP06**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP06 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_06 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP06.2（2）；02_TX_BUFFERS/U_TXB0.15（A6）。 [完整端点N0621](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0621)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP06 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP06.1=`UP_DATA_FILT_06`，C_RX_UP06.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up07"></a>

### 第010步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP07

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP07**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP07 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_07 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP07.2（2）；02_TX_BUFFERS/U_TXB0.17（A7）。 [完整端点N0622](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0622)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP07 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP07.1=`UP_DATA_FILT_07`，C_RX_UP07.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up00"></a>

### 第011步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP00

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP00**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP00 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_00 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_00`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.3（EX_IO1_1N）；02_TX_BUFFERS/R_RX_UP00.1（1）。 [完整端点N0631](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0631)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP00 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP00.1=`UP_DATA_RAW_00`，R_DATA_RAW_PD_UP00.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up01"></a>

### 第012步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP01

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP01**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP01 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_01 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_01`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.4（EX_IO1_1P）；02_TX_BUFFERS/R_RX_UP01.1（1）。 [完整端点N0632](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0632)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP01 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP01.1=`UP_DATA_RAW_01`，R_DATA_RAW_PD_UP01.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up02"></a>

### 第013步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP02

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP02**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP02 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_02 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_02`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.5（EX_IO1_2N）；02_TX_BUFFERS/R_RX_UP02.1（1）。 [完整端点N0633](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0633)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP02 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP02.1=`UP_DATA_RAW_02`，R_DATA_RAW_PD_UP02.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up03"></a>

### 第014步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP03

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP03**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP03 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_03 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_03`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.6（EX_IO1_2P）；02_TX_BUFFERS/R_RX_UP03.1（1）。 [完整端点N0634](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0634)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP03 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP03.1=`UP_DATA_RAW_03`，R_DATA_RAW_PD_UP03.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up04"></a>

### 第015步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP04

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP04**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP04 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_04 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_04`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.7（EX_IO1_3N）；02_TX_BUFFERS/R_RX_UP04.1（1）。 [完整端点N0635](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0635)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP04 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP04.1=`UP_DATA_RAW_04`，R_DATA_RAW_PD_UP04.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up05"></a>

### 第016步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP05

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP05**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP05 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_05 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_05`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.8（EX_IO1_3P）；02_TX_BUFFERS/R_RX_UP05.1（1）。 [完整端点N0636](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0636)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP05 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP05.1=`UP_DATA_RAW_05`，R_DATA_RAW_PD_UP05.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up06"></a>

### 第017步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP06

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP06**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP06 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_06 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_06`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.9（EX_IO1_4N）；02_TX_BUFFERS/R_RX_UP06.1（1）。 [完整端点N0637](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0637)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP06 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP06.1=`UP_DATA_RAW_06`，R_DATA_RAW_PD_UP06.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up07"></a>

### 第018步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP07

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP07**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP07 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_07 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_07`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.10（EX_IO1_4P）；02_TX_BUFFERS/R_RX_UP07.1（1）。 [完整端点N0638](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0638)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP07 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP07.1=`UP_DATA_RAW_07`，R_DATA_RAW_PD_UP07.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up00"></a>

### 第019步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP00

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP00**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP00 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_00 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_00`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.3（EX_IO1_1N）；02_TX_BUFFERS/R_DATA_RAW_PD_UP00.1（1）。 [完整端点N0631](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0631)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP00 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_00 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP00.1（1）；02_TX_BUFFERS/U_TXB0.2（A0）。 [完整端点N0615](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0615)。 |

接完确认：R_RX_UP00.1=`UP_DATA_RAW_00`，R_RX_UP00.2=`UP_DATA_FILT_00`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up01"></a>

### 第020步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP01

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP01**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP01 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_01 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_01`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.4（EX_IO1_1P）；02_TX_BUFFERS/R_DATA_RAW_PD_UP01.1（1）。 [完整端点N0632](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0632)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP01 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_01 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP01.1（1）；02_TX_BUFFERS/U_TXB0.4（A1）。 [完整端点N0616](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0616)。 |

接完确认：R_RX_UP01.1=`UP_DATA_RAW_01`，R_RX_UP01.2=`UP_DATA_FILT_01`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up02"></a>

### 第021步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP02

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP02**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP02 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_02 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_02`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.5（EX_IO1_2N）；02_TX_BUFFERS/R_DATA_RAW_PD_UP02.1（1）。 [完整端点N0633](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0633)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP02 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_02 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP02.1（1）；02_TX_BUFFERS/U_TXB0.6（A2）。 [完整端点N0617](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0617)。 |

接完确认：R_RX_UP02.1=`UP_DATA_RAW_02`，R_RX_UP02.2=`UP_DATA_FILT_02`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up03"></a>

### 第022步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP03

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP03**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP03 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_03 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_03`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.6（EX_IO1_2P）；02_TX_BUFFERS/R_DATA_RAW_PD_UP03.1（1）。 [完整端点N0634](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0634)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP03 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_03 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP03.1（1）；02_TX_BUFFERS/U_TXB0.8（A3）。 [完整端点N0618](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0618)。 |

接完确认：R_RX_UP03.1=`UP_DATA_RAW_03`，R_RX_UP03.2=`UP_DATA_FILT_03`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up04"></a>

### 第023步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP04

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP04**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP04 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_04 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_04`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.7（EX_IO1_3N）；02_TX_BUFFERS/R_DATA_RAW_PD_UP04.1（1）。 [完整端点N0635](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0635)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP04 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_04 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP04.1（1）；02_TX_BUFFERS/U_TXB0.11（A4）。 [完整端点N0619](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0619)。 |

接完确认：R_RX_UP04.1=`UP_DATA_RAW_04`，R_RX_UP04.2=`UP_DATA_FILT_04`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up05"></a>

### 第024步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP05

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP05**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP05 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_05 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_05`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.8（EX_IO1_3P）；02_TX_BUFFERS/R_DATA_RAW_PD_UP05.1（1）。 [完整端点N0636](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0636)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP05 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_05 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP05.1（1）；02_TX_BUFFERS/U_TXB0.13（A5）。 [完整端点N0620](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0620)。 |

接完确认：R_RX_UP05.1=`UP_DATA_RAW_05`，R_RX_UP05.2=`UP_DATA_FILT_05`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up06"></a>

### 第025步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP06

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP06**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP06 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_06 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_06`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.9（EX_IO1_4N）；02_TX_BUFFERS/R_DATA_RAW_PD_UP06.1（1）。 [完整端点N0637](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0637)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP06 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_06 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP06.1（1）；02_TX_BUFFERS/U_TXB0.15（A6）。 [完整端点N0621](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0621)。 |

接完确认：R_RX_UP06.1=`UP_DATA_RAW_06`，R_RX_UP06.2=`UP_DATA_FILT_06`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up07"></a>

### 第026步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP07

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP07**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP07 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_07 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_07`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.10（EX_IO1_4P）；02_TX_BUFFERS/R_DATA_RAW_PD_UP07.1（1）。 [完整端点N0638](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0638)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP07 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_07 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP07.1（1）；02_TX_BUFFERS/U_TXB0.17（A7）。 [完整端点N0622](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0622)。 |

接完确认：R_RX_UP07.1=`UP_DATA_RAW_07`，R_RX_UP07.2=`UP_DATA_FILT_07`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up00"></a>

### 第027步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP00

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP00**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP00 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_00 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB0.18（Y0）。 [完整端点N0599](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0599)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP00 | RC0603FR-0747RL | 2 | 2 | UP_DATA_00 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_00`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.1（DATA_00）。 [完整端点N0583](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0583)。 |

接完确认：R_TX_UP00.1=`UP_DATA_DRV_00`，R_TX_UP00.2=`UP_DATA_00`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up01"></a>

### 第028步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP01

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP01**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP01 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_01 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB0.16（Y1）。 [完整端点N0600](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0600)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP01 | RC0603FR-0747RL | 2 | 2 | UP_DATA_01 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_01`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.3（DATA_01）。 [完整端点N0584](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0584)。 |

接完确认：R_TX_UP01.1=`UP_DATA_DRV_01`，R_TX_UP01.2=`UP_DATA_01`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up02"></a>

### 第029步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP02

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP02**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP02 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_02 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB0.14（Y2）。 [完整端点N0601](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0601)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP02 | RC0603FR-0747RL | 2 | 2 | UP_DATA_02 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_02`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.5（DATA_02）。 [完整端点N0585](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0585)。 |

接完确认：R_TX_UP02.1=`UP_DATA_DRV_02`，R_TX_UP02.2=`UP_DATA_02`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up03"></a>

### 第030步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP03

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP03**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP03 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_03 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB0.12（Y3）。 [完整端点N0602](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0602)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP03 | RC0603FR-0747RL | 2 | 2 | UP_DATA_03 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_03`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.7（DATA_03）。 [完整端点N0586](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0586)。 |

接完确认：R_TX_UP03.1=`UP_DATA_DRV_03`，R_TX_UP03.2=`UP_DATA_03`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up04"></a>

### 第031步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP04

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP04**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP04 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_04 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB0.9（Y4）。 [完整端点N0603](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0603)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP04 | RC0603FR-0747RL | 2 | 2 | UP_DATA_04 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_04`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.9（DATA_04）。 [完整端点N0587](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0587)。 |

接完确认：R_TX_UP04.1=`UP_DATA_DRV_04`，R_TX_UP04.2=`UP_DATA_04`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up05"></a>

### 第032步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP05

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP05**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP05 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_05 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB0.7（Y5）。 [完整端点N0604](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0604)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP05 | RC0603FR-0747RL | 2 | 2 | UP_DATA_05 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_05`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.11（DATA_05）。 [完整端点N0588](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0588)。 |

接完确认：R_TX_UP05.1=`UP_DATA_DRV_05`，R_TX_UP05.2=`UP_DATA_05`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up06"></a>

### 第033步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP06

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP06**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP06 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_06 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB0.5（Y6）。 [完整端点N0605](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0605)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP06 | RC0603FR-0747RL | 2 | 2 | UP_DATA_06 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_06`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.13（DATA_06）。 [完整端点N0589](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0589)。 |

接完确认：R_TX_UP06.1=`UP_DATA_DRV_06`，R_TX_UP06.2=`UP_DATA_06`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up07"></a>

### 第034步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP07

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP07**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP07 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_07 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB0.3（Y7）。 [完整端点N0606](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0606)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP07 | RC0603FR-0747RL | 2 | 2 | UP_DATA_07 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_07`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.15（DATA_07）。 [完整端点N0590](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0590)。 |

接完确认：R_TX_UP07.1=`UP_DATA_DRV_07`，R_TX_UP07.2=`UP_DATA_07`；不可旁路该器件把两个网名短在一起。

<a id="central-u-txb1"></a>

### 第035步：在CENTRAL／02_TX_BUFFERS放置 U_TXB1

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **U_TXB1**，精确型号 **SN74LVT244BPWR**，封装 **PW/TSSOP20**。

按信号从接口到输出的顺序摆放LVT缓冲，供电本地V3V3、地GND；PW20无EP。每个通道A/Y和两个OE_N按实际脚号，未用输入接表定网络、未用输出独立NC。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 1 | 1OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 2 | A0 | UP_DATA_FILT_08 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP08.2（2）；02_TX_BUFFERS/C_RX_UP08.1（1）。 [完整端点N0623](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0623)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 3 | Y7 | UP_DATA_DRV_15 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP15.1（1）。 [完整端点N0614](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0614)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 4 | A1 | UP_DATA_FILT_09 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP09.2（2）；02_TX_BUFFERS/C_RX_UP09.1（1）。 [完整端点N0624](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0624)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 5 | Y6 | UP_DATA_DRV_14 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP14.1（1）。 [完整端点N0613](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0613)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 6 | A2 | UP_DATA_FILT_10 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP10.2（2）；02_TX_BUFFERS/C_RX_UP10.1（1）。 [完整端点N0625](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0625)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 7 | Y5 | UP_DATA_DRV_13 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP13.1（1）。 [完整端点N0612](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0612)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 8 | A3 | UP_DATA_FILT_11 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP11.2（2）；02_TX_BUFFERS/C_RX_UP11.1（1）。 [完整端点N0626](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0626)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 9 | Y4 | UP_DATA_DRV_12 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP12.1（1）。 [完整端点N0611](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0611)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 10 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 11 | A4 | UP_DATA_FILT_12 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP12.2（2）；02_TX_BUFFERS/C_RX_UP12.1（1）。 [完整端点N0627](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0627)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 12 | Y3 | UP_DATA_DRV_11 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP11.1（1）。 [完整端点N0610](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0610)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 13 | A5 | UP_DATA_FILT_13 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP13.2（2）；02_TX_BUFFERS/C_RX_UP13.1（1）。 [完整端点N0628](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0628)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 14 | Y2 | UP_DATA_DRV_10 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP10.1（1）。 [完整端点N0609](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0609)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 15 | A6 | UP_DATA_FILT_14 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP14.2（2）；02_TX_BUFFERS/C_RX_UP14.1（1）。 [完整端点N0629](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0629)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 16 | Y1 | UP_DATA_DRV_09 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP09.1（1）。 [完整端点N0608](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0608)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 17 | A7 | UP_DATA_FILT_15 | IN | 从此脚引线，标注精确网名`UP_DATA_FILT_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP15.2（2）；02_TX_BUFFERS/C_RX_UP15.1（1）。 [完整端点N0630](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0630)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 18 | Y0 | UP_DATA_DRV_08 | OUT | 从此脚引线，标注精确网名`UP_DATA_DRV_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP08.1（1）。 [完整端点N0607](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0607)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 19 | 2OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB1 | SN74LVT244BPWR | 20 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_TXB1.1→GND；U_TXB1.19→GND；U_TXB1.10→GND；U_TXB1.20→V3V3。

<a id="central-c-u-txb1"></a>

### 第036步：在CENTRAL／02_TX_BUFFERS放置 C_U_TXB1

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_U_TXB1**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_U_TXB1 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 02_TX_BUFFERS | C_U_TXB1 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_TXB1.1=`V3V3`，C_U_TXB1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up08"></a>

### 第037步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP08

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP08**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP08 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_08 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP08.2（2）；02_TX_BUFFERS/U_TXB1.2（A0）。 [完整端点N0623](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0623)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP08 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP08.1=`UP_DATA_FILT_08`，C_RX_UP08.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up09"></a>

### 第038步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP09

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP09**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP09 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_09 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP09.2（2）；02_TX_BUFFERS/U_TXB1.4（A1）。 [完整端点N0624](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0624)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP09 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP09.1=`UP_DATA_FILT_09`，C_RX_UP09.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up10"></a>

### 第039步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP10

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP10**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP10 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_10 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP10.2（2）；02_TX_BUFFERS/U_TXB1.6（A2）。 [完整端点N0625](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0625)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP10 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP10.1=`UP_DATA_FILT_10`，C_RX_UP10.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up11"></a>

### 第040步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP11

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP11**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP11 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_11 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP11.2（2）；02_TX_BUFFERS/U_TXB1.8（A3）。 [完整端点N0626](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0626)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP11 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP11.1=`UP_DATA_FILT_11`，C_RX_UP11.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up12"></a>

### 第041步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP12

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP12**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP12 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_12 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP12.2（2）；02_TX_BUFFERS/U_TXB1.11（A4）。 [完整端点N0627](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0627)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP12 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP12.1=`UP_DATA_FILT_12`，C_RX_UP12.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up13"></a>

### 第042步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP13

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP13**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP13 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_13 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP13.2（2）；02_TX_BUFFERS/U_TXB1.13（A5）。 [完整端点N0628](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0628)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP13 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP13.1=`UP_DATA_FILT_13`，C_RX_UP13.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up14"></a>

### 第043步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP14

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP14**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP14 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_14 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP14.2（2）；02_TX_BUFFERS/U_TXB1.15（A6）。 [完整端点N0629](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0629)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP14 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP14.1=`UP_DATA_FILT_14`，C_RX_UP14.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-up15"></a>

### 第044步：在CENTRAL／02_TX_BUFFERS放置 C_RX_UP15

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_UP15**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP15 | CC0603JRNPO9BN3R3 | 1 | 1 | UP_DATA_FILT_15 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_UP15.2（2）；02_TX_BUFFERS/U_TXB1.17（A7）。 [完整端点N0630](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0630)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_UP15 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_UP15.1=`UP_DATA_FILT_15`，C_RX_UP15.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up08"></a>

### 第045步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP08

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP08**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP08 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_08 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_08`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.11（EX_IO1_5N）；02_TX_BUFFERS/R_RX_UP08.1（1）。 [完整端点N0639](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0639)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP08 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP08.1=`UP_DATA_RAW_08`，R_DATA_RAW_PD_UP08.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up09"></a>

### 第046步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP09

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP09**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP09 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_09 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_09`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.12（EX_IO1_5P）；02_TX_BUFFERS/R_RX_UP09.1（1）。 [完整端点N0640](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0640)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP09 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP09.1=`UP_DATA_RAW_09`，R_DATA_RAW_PD_UP09.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up10"></a>

### 第047步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP10

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP10**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP10 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_10 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_10`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.13（EX_IO1_6N）；02_TX_BUFFERS/R_RX_UP10.1（1）。 [完整端点N0641](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0641)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP10 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP10.1=`UP_DATA_RAW_10`，R_DATA_RAW_PD_UP10.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up11"></a>

### 第048步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP11

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP11**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP11 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_11 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_11`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.14（EX_IO1_6P）；02_TX_BUFFERS/R_RX_UP11.1（1）。 [完整端点N0642](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0642)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP11 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP11.1=`UP_DATA_RAW_11`，R_DATA_RAW_PD_UP11.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up12"></a>

### 第049步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP12

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP12**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP12 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_12 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_12`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.15（EX_IO1_7N）；02_TX_BUFFERS/R_RX_UP12.1（1）。 [完整端点N0643](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0643)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP12 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP12.1=`UP_DATA_RAW_12`，R_DATA_RAW_PD_UP12.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up13"></a>

### 第050步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP13

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP13**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP13 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_13 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_13`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.16（EX_IO1_7P）；02_TX_BUFFERS/R_RX_UP13.1（1）。 [完整端点N0644](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0644)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP13 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP13.1=`UP_DATA_RAW_13`，R_DATA_RAW_PD_UP13.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up14"></a>

### 第051步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP14

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP14**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP14 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_14 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_14`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.17（EX_IO1_8N）；02_TX_BUFFERS/R_RX_UP14.1（1）。 [完整端点N0645](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0645)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP14 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP14.1=`UP_DATA_RAW_14`，R_DATA_RAW_PD_UP14.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-up15"></a>

### 第052步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_UP15

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_UP15**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP15 | RC0603FR-0710KL | 1 | 1 | UP_DATA_RAW_15 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_15`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.18（EX_IO1_8P）；02_TX_BUFFERS/R_RX_UP15.1（1）。 [完整端点N0646](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0646)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_UP15 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_UP15.1=`UP_DATA_RAW_15`，R_DATA_RAW_PD_UP15.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up08"></a>

### 第053步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP08

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP08**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP08 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_08 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_08`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.11（EX_IO1_5N）；02_TX_BUFFERS/R_DATA_RAW_PD_UP08.1（1）。 [完整端点N0639](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0639)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP08 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_08 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP08.1（1）；02_TX_BUFFERS/U_TXB1.2（A0）。 [完整端点N0623](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0623)。 |

接完确认：R_RX_UP08.1=`UP_DATA_RAW_08`，R_RX_UP08.2=`UP_DATA_FILT_08`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up09"></a>

### 第054步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP09

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP09**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP09 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_09 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_09`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.12（EX_IO1_5P）；02_TX_BUFFERS/R_DATA_RAW_PD_UP09.1（1）。 [完整端点N0640](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0640)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP09 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_09 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP09.1（1）；02_TX_BUFFERS/U_TXB1.4（A1）。 [完整端点N0624](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0624)。 |

接完确认：R_RX_UP09.1=`UP_DATA_RAW_09`，R_RX_UP09.2=`UP_DATA_FILT_09`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up10"></a>

### 第055步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP10

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP10**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP10 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_10 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_10`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.13（EX_IO1_6N）；02_TX_BUFFERS/R_DATA_RAW_PD_UP10.1（1）。 [完整端点N0641](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0641)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP10 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_10 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP10.1（1）；02_TX_BUFFERS/U_TXB1.6（A2）。 [完整端点N0625](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0625)。 |

接完确认：R_RX_UP10.1=`UP_DATA_RAW_10`，R_RX_UP10.2=`UP_DATA_FILT_10`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up11"></a>

### 第056步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP11

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP11**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP11 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_11 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_11`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.14（EX_IO1_6P）；02_TX_BUFFERS/R_DATA_RAW_PD_UP11.1（1）。 [完整端点N0642](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0642)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP11 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_11 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP11.1（1）；02_TX_BUFFERS/U_TXB1.8（A3）。 [完整端点N0626](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0626)。 |

接完确认：R_RX_UP11.1=`UP_DATA_RAW_11`，R_RX_UP11.2=`UP_DATA_FILT_11`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up12"></a>

### 第057步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP12

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP12**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP12 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_12 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_12`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.15（EX_IO1_7N）；02_TX_BUFFERS/R_DATA_RAW_PD_UP12.1（1）。 [完整端点N0643](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0643)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP12 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_12 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP12.1（1）；02_TX_BUFFERS/U_TXB1.11（A4）。 [完整端点N0627](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0627)。 |

接完确认：R_RX_UP12.1=`UP_DATA_RAW_12`，R_RX_UP12.2=`UP_DATA_FILT_12`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up13"></a>

### 第058步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP13

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP13**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP13 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_13 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_13`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.16（EX_IO1_7P）；02_TX_BUFFERS/R_DATA_RAW_PD_UP13.1（1）。 [完整端点N0644](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0644)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP13 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_13 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP13.1（1）；02_TX_BUFFERS/U_TXB1.13（A5）。 [完整端点N0628](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0628)。 |

接完确认：R_RX_UP13.1=`UP_DATA_RAW_13`，R_RX_UP13.2=`UP_DATA_FILT_13`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up14"></a>

### 第059步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP14

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP14**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP14 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_14 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_14`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.17（EX_IO1_8N）；02_TX_BUFFERS/R_DATA_RAW_PD_UP14.1（1）。 [完整端点N0645](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0645)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP14 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_14 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP14.1（1）；02_TX_BUFFERS/U_TXB1.15（A6）。 [完整端点N0629](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0629)。 |

接完确认：R_RX_UP14.1=`UP_DATA_RAW_14`，R_RX_UP14.2=`UP_DATA_FILT_14`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-up15"></a>

### 第060步：在CENTRAL／02_TX_BUFFERS放置 R_RX_UP15

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_UP15**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP15 | RC0603FR-0722RL | 1 | 1 | UP_DATA_RAW_15 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_RAW_15`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.18（EX_IO1_8P）；02_TX_BUFFERS/R_DATA_RAW_PD_UP15.1（1）。 [完整端点N0646](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0646)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_UP15 | RC0603FR-0722RL | 2 | 2 | UP_DATA_FILT_15 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_FILT_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_UP15.1（1）；02_TX_BUFFERS/U_TXB1.17（A7）。 [完整端点N0630](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0630)。 |

接完确认：R_RX_UP15.1=`UP_DATA_RAW_15`，R_RX_UP15.2=`UP_DATA_FILT_15`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up08"></a>

### 第061步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP08

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP08**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP08 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_08 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB1.18（Y0）。 [完整端点N0607](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0607)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP08 | RC0603FR-0747RL | 2 | 2 | UP_DATA_08 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_08`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.17（DATA_08）。 [完整端点N0591](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0591)。 |

接完确认：R_TX_UP08.1=`UP_DATA_DRV_08`，R_TX_UP08.2=`UP_DATA_08`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up09"></a>

### 第062步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP09

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP09**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP09 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_09 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB1.16（Y1）。 [完整端点N0608](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0608)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP09 | RC0603FR-0747RL | 2 | 2 | UP_DATA_09 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_09`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.19（DATA_09）。 [完整端点N0592](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0592)。 |

接完确认：R_TX_UP09.1=`UP_DATA_DRV_09`，R_TX_UP09.2=`UP_DATA_09`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up10"></a>

### 第063步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP10

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP10**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP10 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_10 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB1.14（Y2）。 [完整端点N0609](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0609)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP10 | RC0603FR-0747RL | 2 | 2 | UP_DATA_10 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_10`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.21（DATA_10）。 [完整端点N0593](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0593)。 |

接完确认：R_TX_UP10.1=`UP_DATA_DRV_10`，R_TX_UP10.2=`UP_DATA_10`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up11"></a>

### 第064步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP11

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP11**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP11 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_11 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB1.12（Y3）。 [完整端点N0610](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0610)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP11 | RC0603FR-0747RL | 2 | 2 | UP_DATA_11 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_11`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.23（DATA_11）。 [完整端点N0594](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0594)。 |

接完确认：R_TX_UP11.1=`UP_DATA_DRV_11`，R_TX_UP11.2=`UP_DATA_11`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up12"></a>

### 第065步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP12

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP12**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP12 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_12 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB1.9（Y4）。 [完整端点N0611](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0611)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP12 | RC0603FR-0747RL | 2 | 2 | UP_DATA_12 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_12`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.25（DATA_12）。 [完整端点N0595](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0595)。 |

接完确认：R_TX_UP12.1=`UP_DATA_DRV_12`，R_TX_UP12.2=`UP_DATA_12`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up13"></a>

### 第066步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP13

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP13**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP13 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_13 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB1.7（Y5）。 [完整端点N0612](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0612)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP13 | RC0603FR-0747RL | 2 | 2 | UP_DATA_13 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_13`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.27（DATA_13）。 [完整端点N0596](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0596)。 |

接完确认：R_TX_UP13.1=`UP_DATA_DRV_13`，R_TX_UP13.2=`UP_DATA_13`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up14"></a>

### 第067步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP14

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP14**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP14 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_14 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB1.5（Y6）。 [完整端点N0613](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0613)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP14 | RC0603FR-0747RL | 2 | 2 | UP_DATA_14 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_14`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.29（DATA_14）。 [完整端点N0597](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0597)。 |

接完确认：R_TX_UP14.1=`UP_DATA_DRV_14`，R_TX_UP14.2=`UP_DATA_14`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up15"></a>

### 第068步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP15

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP15**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP15 | RC0603FR-0747RL | 1 | 1 | UP_DATA_DRV_15 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_DRV_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB1.3（Y7）。 [完整端点N0614](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0614)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP15 | RC0603FR-0747RL | 2 | 2 | UP_DATA_15 | PASSIVE | 从此脚引线，标注精确网名`UP_DATA_15`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.31（DATA_15）。 [完整端点N0598](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0598)。 |

接完确认：R_TX_UP15.1=`UP_DATA_DRV_15`，R_TX_UP15.2=`UP_DATA_15`；不可旁路该器件把两个网名短在一起。

<a id="central-u-txb2"></a>

### 第069步：在CENTRAL／02_TX_BUFFERS放置 U_TXB2

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **U_TXB2**，精确型号 **SN74LVT244BPWR**，封装 **PW/TSSOP20**。

按信号从接口到输出的顺序摆放LVT缓冲，供电本地V3V3、地GND；PW20无EP。每个通道A/Y和两个OE_N按实际脚号，未用输入接表定网络、未用输出独立NC。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 1 | 1OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 2 | A0 | DN_DATA_FILT_00 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN00.2（2）；02_TX_BUFFERS/C_RX_DN00.1（1）。 [完整端点N0495](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0495)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 3 | Y7 | DN_DATA_DRV_07 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN07.1（1）。 [完整端点N0486](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0486)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 4 | A1 | DN_DATA_FILT_01 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN01.2（2）；02_TX_BUFFERS/C_RX_DN01.1（1）。 [完整端点N0496](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0496)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 5 | Y6 | DN_DATA_DRV_06 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN06.1（1）。 [完整端点N0485](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0485)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 6 | A2 | DN_DATA_FILT_02 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN02.2（2）；02_TX_BUFFERS/C_RX_DN02.1（1）。 [完整端点N0497](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0497)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 7 | Y5 | DN_DATA_DRV_05 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN05.1（1）。 [完整端点N0484](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0484)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 8 | A3 | DN_DATA_FILT_03 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN03.2（2）；02_TX_BUFFERS/C_RX_DN03.1（1）。 [完整端点N0498](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0498)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 9 | Y4 | DN_DATA_DRV_04 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN04.1（1）。 [完整端点N0483](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0483)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 10 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 11 | A4 | DN_DATA_FILT_04 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN04.2（2）；02_TX_BUFFERS/C_RX_DN04.1（1）。 [完整端点N0499](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0499)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 12 | Y3 | DN_DATA_DRV_03 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN03.1（1）。 [完整端点N0482](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0482)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 13 | A5 | DN_DATA_FILT_05 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN05.2（2）；02_TX_BUFFERS/C_RX_DN05.1（1）。 [完整端点N0500](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0500)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 14 | Y2 | DN_DATA_DRV_02 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN02.1（1）。 [完整端点N0481](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0481)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 15 | A6 | DN_DATA_FILT_06 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN06.2（2）；02_TX_BUFFERS/C_RX_DN06.1（1）。 [完整端点N0501](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0501)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 16 | Y1 | DN_DATA_DRV_01 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN01.1（1）。 [完整端点N0480](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0480)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 17 | A7 | DN_DATA_FILT_07 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN07.2（2）；02_TX_BUFFERS/C_RX_DN07.1（1）。 [完整端点N0502](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0502)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 18 | Y0 | DN_DATA_DRV_00 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN00.1（1）。 [完整端点N0479](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0479)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 19 | 2OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB2 | SN74LVT244BPWR | 20 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_TXB2.1→GND；U_TXB2.19→GND；U_TXB2.10→GND；U_TXB2.20→V3V3。

<a id="central-c-u-txb2"></a>

### 第070步：在CENTRAL／02_TX_BUFFERS放置 C_U_TXB2

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_U_TXB2**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_U_TXB2 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 02_TX_BUFFERS | C_U_TXB2 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_TXB2.1=`V3V3`，C_U_TXB2.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn00"></a>

### 第071步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN00

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN00**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN00 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_00 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN00.2（2）；02_TX_BUFFERS/U_TXB2.2（A0）。 [完整端点N0495](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0495)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN00 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN00.1=`DN_DATA_FILT_00`，C_RX_DN00.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn01"></a>

### 第072步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN01

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN01**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN01 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_01 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN01.2（2）；02_TX_BUFFERS/U_TXB2.4（A1）。 [完整端点N0496](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0496)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN01 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN01.1=`DN_DATA_FILT_01`，C_RX_DN01.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn02"></a>

### 第073步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN02

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN02**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN02 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_02 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN02.2（2）；02_TX_BUFFERS/U_TXB2.6（A2）。 [完整端点N0497](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0497)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN02 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN02.1=`DN_DATA_FILT_02`，C_RX_DN02.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn03"></a>

### 第074步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN03

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN03**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN03 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_03 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN03.2（2）；02_TX_BUFFERS/U_TXB2.8（A3）。 [完整端点N0498](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0498)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN03 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN03.1=`DN_DATA_FILT_03`，C_RX_DN03.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn04"></a>

### 第075步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN04

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN04**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN04 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_04 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN04.2（2）；02_TX_BUFFERS/U_TXB2.11（A4）。 [完整端点N0499](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0499)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN04 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN04.1=`DN_DATA_FILT_04`，C_RX_DN04.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn05"></a>

### 第076步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN05

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN05**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN05 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_05 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN05.2（2）；02_TX_BUFFERS/U_TXB2.13（A5）。 [完整端点N0500](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0500)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN05 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN05.1=`DN_DATA_FILT_05`，C_RX_DN05.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn06"></a>

### 第077步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN06

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN06**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN06 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_06 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN06.2（2）；02_TX_BUFFERS/U_TXB2.15（A6）。 [完整端点N0501](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0501)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN06 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN06.1=`DN_DATA_FILT_06`，C_RX_DN06.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn07"></a>

### 第078步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN07

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN07**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN07 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_07 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN07.2（2）；02_TX_BUFFERS/U_TXB2.17（A7）。 [完整端点N0502](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0502)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN07 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN07.1=`DN_DATA_FILT_07`，C_RX_DN07.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn00"></a>

### 第079步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN00

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN00**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN00 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_00 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_00`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.3（EX_IO2_1N）；02_TX_BUFFERS/R_RX_DN00.1（1）。 [完整端点N0511](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0511)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN00 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN00.1=`DN_DATA_RAW_00`，R_DATA_RAW_PD_DN00.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn01"></a>

### 第080步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN01

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN01**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN01 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_01 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_01`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.4（EX_IO2_1P）；02_TX_BUFFERS/R_RX_DN01.1（1）。 [完整端点N0512](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0512)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN01 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN01.1=`DN_DATA_RAW_01`，R_DATA_RAW_PD_DN01.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn02"></a>

### 第081步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN02

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN02**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN02 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_02 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_02`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.5（EX_IO2_2N）；02_TX_BUFFERS/R_RX_DN02.1（1）。 [完整端点N0513](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0513)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN02 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN02.1=`DN_DATA_RAW_02`，R_DATA_RAW_PD_DN02.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn03"></a>

### 第082步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN03

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN03**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN03 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_03 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_03`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.6（EX_IO2_2P）；02_TX_BUFFERS/R_RX_DN03.1（1）。 [完整端点N0514](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0514)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN03 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN03.1=`DN_DATA_RAW_03`，R_DATA_RAW_PD_DN03.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn04"></a>

### 第083步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN04

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN04**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN04 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_04 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_04`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.7（EX_IO2_3N）；02_TX_BUFFERS/R_RX_DN04.1（1）。 [完整端点N0515](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0515)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN04 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN04.1=`DN_DATA_RAW_04`，R_DATA_RAW_PD_DN04.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn05"></a>

### 第084步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN05

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN05**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN05 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_05 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_05`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.8（EX_IO2_3P）；02_TX_BUFFERS/R_RX_DN05.1（1）。 [完整端点N0516](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0516)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN05 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN05.1=`DN_DATA_RAW_05`，R_DATA_RAW_PD_DN05.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn06"></a>

### 第085步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN06

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN06**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN06 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_06 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_06`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.9（EX_IO2_4N）；02_TX_BUFFERS/R_RX_DN06.1（1）。 [完整端点N0517](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0517)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN06 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN06.1=`DN_DATA_RAW_06`，R_DATA_RAW_PD_DN06.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn07"></a>

### 第086步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN07

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN07**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN07 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_07 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_07`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.10（EX_IO2_4P）；02_TX_BUFFERS/R_RX_DN07.1（1）。 [完整端点N0518](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0518)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN07 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN07.1=`DN_DATA_RAW_07`，R_DATA_RAW_PD_DN07.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn00"></a>

### 第087步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN00

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN00**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN00 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_00 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_00`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.3（EX_IO2_1N）；02_TX_BUFFERS/R_DATA_RAW_PD_DN00.1（1）。 [完整端点N0511](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0511)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN00 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_00 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN00.1（1）；02_TX_BUFFERS/U_TXB2.2（A0）。 [完整端点N0495](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0495)。 |

接完确认：R_RX_DN00.1=`DN_DATA_RAW_00`，R_RX_DN00.2=`DN_DATA_FILT_00`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn01"></a>

### 第088步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN01

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN01**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN01 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_01 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_01`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.4（EX_IO2_1P）；02_TX_BUFFERS/R_DATA_RAW_PD_DN01.1（1）。 [完整端点N0512](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0512)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN01 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_01 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN01.1（1）；02_TX_BUFFERS/U_TXB2.4（A1）。 [完整端点N0496](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0496)。 |

接完确认：R_RX_DN01.1=`DN_DATA_RAW_01`，R_RX_DN01.2=`DN_DATA_FILT_01`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn02"></a>

### 第089步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN02

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN02**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN02 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_02 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_02`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.5（EX_IO2_2N）；02_TX_BUFFERS/R_DATA_RAW_PD_DN02.1（1）。 [完整端点N0513](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0513)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN02 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_02 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN02.1（1）；02_TX_BUFFERS/U_TXB2.6（A2）。 [完整端点N0497](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0497)。 |

接完确认：R_RX_DN02.1=`DN_DATA_RAW_02`，R_RX_DN02.2=`DN_DATA_FILT_02`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn03"></a>

### 第090步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN03

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN03**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN03 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_03 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_03`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.6（EX_IO2_2P）；02_TX_BUFFERS/R_DATA_RAW_PD_DN03.1（1）。 [完整端点N0514](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0514)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN03 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_03 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN03.1（1）；02_TX_BUFFERS/U_TXB2.8（A3）。 [完整端点N0498](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0498)。 |

接完确认：R_RX_DN03.1=`DN_DATA_RAW_03`，R_RX_DN03.2=`DN_DATA_FILT_03`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn04"></a>

### 第091步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN04

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN04**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN04 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_04 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_04`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.7（EX_IO2_3N）；02_TX_BUFFERS/R_DATA_RAW_PD_DN04.1（1）。 [完整端点N0515](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0515)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN04 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_04 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN04.1（1）；02_TX_BUFFERS/U_TXB2.11（A4）。 [完整端点N0499](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0499)。 |

接完确认：R_RX_DN04.1=`DN_DATA_RAW_04`，R_RX_DN04.2=`DN_DATA_FILT_04`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn05"></a>

### 第092步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN05

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN05**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN05 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_05 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_05`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.8（EX_IO2_3P）；02_TX_BUFFERS/R_DATA_RAW_PD_DN05.1（1）。 [完整端点N0516](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0516)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN05 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_05 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN05.1（1）；02_TX_BUFFERS/U_TXB2.13（A5）。 [完整端点N0500](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0500)。 |

接完确认：R_RX_DN05.1=`DN_DATA_RAW_05`，R_RX_DN05.2=`DN_DATA_FILT_05`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn06"></a>

### 第093步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN06

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN06**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN06 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_06 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_06`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.9（EX_IO2_4N）；02_TX_BUFFERS/R_DATA_RAW_PD_DN06.1（1）。 [完整端点N0517](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0517)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN06 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_06 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN06.1（1）；02_TX_BUFFERS/U_TXB2.15（A6）。 [完整端点N0501](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0501)。 |

接完确认：R_RX_DN06.1=`DN_DATA_RAW_06`，R_RX_DN06.2=`DN_DATA_FILT_06`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn07"></a>

### 第094步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN07

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN07**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN07 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_07 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_07`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.10（EX_IO2_4P）；02_TX_BUFFERS/R_DATA_RAW_PD_DN07.1（1）。 [完整端点N0518](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0518)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN07 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_07 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN07.1（1）；02_TX_BUFFERS/U_TXB2.17（A7）。 [完整端点N0502](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0502)。 |

接完确认：R_RX_DN07.1=`DN_DATA_RAW_07`，R_RX_DN07.2=`DN_DATA_FILT_07`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn00"></a>

### 第095步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN00

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN00**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN00 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_00 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_00`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB2.18（Y0）。 [完整端点N0479](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0479)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN00 | RC0603FR-0747RL | 2 | 2 | DN_DATA_00 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_00`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.1（DATA_00）。 [完整端点N0463](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0463)。 |

接完确认：R_TX_DN00.1=`DN_DATA_DRV_00`，R_TX_DN00.2=`DN_DATA_00`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn01"></a>

### 第096步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN01

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN01**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN01 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_01 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_01`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB2.16（Y1）。 [完整端点N0480](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0480)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN01 | RC0603FR-0747RL | 2 | 2 | DN_DATA_01 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_01`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.3（DATA_01）。 [完整端点N0464](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0464)。 |

接完确认：R_TX_DN01.1=`DN_DATA_DRV_01`，R_TX_DN01.2=`DN_DATA_01`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn02"></a>

### 第097步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN02

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN02**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN02 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_02 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_02`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB2.14（Y2）。 [完整端点N0481](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0481)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN02 | RC0603FR-0747RL | 2 | 2 | DN_DATA_02 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_02`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.5（DATA_02）。 [完整端点N0465](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0465)。 |

接完确认：R_TX_DN02.1=`DN_DATA_DRV_02`，R_TX_DN02.2=`DN_DATA_02`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn03"></a>

### 第098步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN03

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN03**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN03 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_03 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_03`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB2.12（Y3）。 [完整端点N0482](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0482)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN03 | RC0603FR-0747RL | 2 | 2 | DN_DATA_03 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_03`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.7（DATA_03）。 [完整端点N0466](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0466)。 |

接完确认：R_TX_DN03.1=`DN_DATA_DRV_03`，R_TX_DN03.2=`DN_DATA_03`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn04"></a>

### 第099步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN04

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN04**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN04 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_04 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_04`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB2.9（Y4）。 [完整端点N0483](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0483)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN04 | RC0603FR-0747RL | 2 | 2 | DN_DATA_04 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_04`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.9（DATA_04）。 [完整端点N0467](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0467)。 |

接完确认：R_TX_DN04.1=`DN_DATA_DRV_04`，R_TX_DN04.2=`DN_DATA_04`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn05"></a>

### 第100步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN05

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN05**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN05 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_05 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_05`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB2.7（Y5）。 [完整端点N0484](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0484)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN05 | RC0603FR-0747RL | 2 | 2 | DN_DATA_05 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_05`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.11（DATA_05）。 [完整端点N0468](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0468)。 |

接完确认：R_TX_DN05.1=`DN_DATA_DRV_05`，R_TX_DN05.2=`DN_DATA_05`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn06"></a>

### 第101步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN06

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN06**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN06 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_06 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_06`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB2.5（Y6）。 [完整端点N0485](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0485)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN06 | RC0603FR-0747RL | 2 | 2 | DN_DATA_06 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_06`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.13（DATA_06）。 [完整端点N0469](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0469)。 |

接完确认：R_TX_DN06.1=`DN_DATA_DRV_06`，R_TX_DN06.2=`DN_DATA_06`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn07"></a>

### 第102步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN07

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN07**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN07 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_07 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_07`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB2.3（Y7）。 [完整端点N0486](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0486)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN07 | RC0603FR-0747RL | 2 | 2 | DN_DATA_07 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_07`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.15（DATA_07）。 [完整端点N0470](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0470)。 |

接完确认：R_TX_DN07.1=`DN_DATA_DRV_07`，R_TX_DN07.2=`DN_DATA_07`；不可旁路该器件把两个网名短在一起。

<a id="central-u-txb3"></a>

### 第103步：在CENTRAL／02_TX_BUFFERS放置 U_TXB3

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **U_TXB3**，精确型号 **SN74LVT244BPWR**，封装 **PW/TSSOP20**。

按信号从接口到输出的顺序摆放LVT缓冲，供电本地V3V3、地GND；PW20无EP。每个通道A/Y和两个OE_N按实际脚号，未用输入接表定网络、未用输出独立NC。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 1 | 1OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 2 | A0 | DN_DATA_FILT_08 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN08.2（2）；02_TX_BUFFERS/C_RX_DN08.1（1）。 [完整端点N0503](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0503)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 3 | Y7 | DN_DATA_DRV_15 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN15.1（1）。 [完整端点N0494](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0494)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 4 | A1 | DN_DATA_FILT_09 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN09.2（2）；02_TX_BUFFERS/C_RX_DN09.1（1）。 [完整端点N0504](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0504)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 5 | Y6 | DN_DATA_DRV_14 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN14.1（1）。 [完整端点N0493](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0493)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 6 | A2 | DN_DATA_FILT_10 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN10.2（2）；02_TX_BUFFERS/C_RX_DN10.1（1）。 [完整端点N0505](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0505)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 7 | Y5 | DN_DATA_DRV_13 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN13.1（1）。 [完整端点N0492](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0492)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 8 | A3 | DN_DATA_FILT_11 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN11.2（2）；02_TX_BUFFERS/C_RX_DN11.1（1）。 [完整端点N0506](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0506)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 9 | Y4 | DN_DATA_DRV_12 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN12.1（1）。 [完整端点N0491](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0491)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 10 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 11 | A4 | DN_DATA_FILT_12 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN12.2（2）；02_TX_BUFFERS/C_RX_DN12.1（1）。 [完整端点N0507](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0507)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 12 | Y3 | DN_DATA_DRV_11 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN11.1（1）。 [完整端点N0490](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0490)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 13 | A5 | DN_DATA_FILT_13 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN13.2（2）；02_TX_BUFFERS/C_RX_DN13.1（1）。 [完整端点N0508](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0508)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 14 | Y2 | DN_DATA_DRV_10 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN10.1（1）。 [完整端点N0489](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0489)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 15 | A6 | DN_DATA_FILT_14 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN14.2（2）；02_TX_BUFFERS/C_RX_DN14.1（1）。 [完整端点N0509](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0509)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 16 | Y1 | DN_DATA_DRV_09 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN09.1（1）。 [完整端点N0488](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0488)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 17 | A7 | DN_DATA_FILT_15 | IN | 从此脚引线，标注精确网名`DN_DATA_FILT_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN15.2（2）；02_TX_BUFFERS/C_RX_DN15.1（1）。 [完整端点N0510](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0510)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 18 | Y0 | DN_DATA_DRV_08 | OUT | 从此脚引线，标注精确网名`DN_DATA_DRV_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN08.1（1）。 [完整端点N0487](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0487)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 19 | 2OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXB3 | SN74LVT244BPWR | 20 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_TXB3.1→GND；U_TXB3.19→GND；U_TXB3.10→GND；U_TXB3.20→V3V3。

<a id="central-c-u-txb3"></a>

### 第104步：在CENTRAL／02_TX_BUFFERS放置 C_U_TXB3

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_U_TXB3**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_U_TXB3 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 02_TX_BUFFERS | C_U_TXB3 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_TXB3.1=`V3V3`，C_U_TXB3.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn08"></a>

### 第105步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN08

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN08**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN08 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_08 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN08.2（2）；02_TX_BUFFERS/U_TXB3.2（A0）。 [完整端点N0503](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0503)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN08 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN08.1=`DN_DATA_FILT_08`，C_RX_DN08.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn09"></a>

### 第106步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN09

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN09**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN09 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_09 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN09.2（2）；02_TX_BUFFERS/U_TXB3.4（A1）。 [完整端点N0504](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0504)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN09 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN09.1=`DN_DATA_FILT_09`，C_RX_DN09.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn10"></a>

### 第107步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN10

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN10**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN10 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_10 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN10.2（2）；02_TX_BUFFERS/U_TXB3.6（A2）。 [完整端点N0505](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0505)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN10 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN10.1=`DN_DATA_FILT_10`，C_RX_DN10.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn11"></a>

### 第108步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN11

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN11**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN11 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_11 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN11.2（2）；02_TX_BUFFERS/U_TXB3.8（A3）。 [完整端点N0506](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0506)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN11 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN11.1=`DN_DATA_FILT_11`，C_RX_DN11.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn12"></a>

### 第109步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN12

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN12**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN12 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_12 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN12.2（2）；02_TX_BUFFERS/U_TXB3.11（A4）。 [完整端点N0507](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0507)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN12 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN12.1=`DN_DATA_FILT_12`，C_RX_DN12.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn13"></a>

### 第110步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN13

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN13**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN13 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_13 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN13.2（2）；02_TX_BUFFERS/U_TXB3.13（A5）。 [完整端点N0508](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0508)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN13 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN13.1=`DN_DATA_FILT_13`，C_RX_DN13.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn14"></a>

### 第111步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN14

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN14**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN14 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_14 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN14.2（2）；02_TX_BUFFERS/U_TXB3.15（A6）。 [完整端点N0509](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0509)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN14 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN14.1=`DN_DATA_FILT_14`，C_RX_DN14.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-dn15"></a>

### 第112步：在CENTRAL／02_TX_BUFFERS放置 C_RX_DN15

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_DN15**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN15 | CC0603JRNPO9BN3R3 | 1 | 1 | DN_DATA_FILT_15 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_DN15.2（2）；02_TX_BUFFERS/U_TXB3.17（A7）。 [完整端点N0510](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0510)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_DN15 | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_DN15.1=`DN_DATA_FILT_15`，C_RX_DN15.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn08"></a>

### 第113步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN08

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN08**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN08 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_08 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_08`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.11（EX_IO2_5N）；02_TX_BUFFERS/R_RX_DN08.1（1）。 [完整端点N0519](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0519)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN08 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN08.1=`DN_DATA_RAW_08`，R_DATA_RAW_PD_DN08.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn09"></a>

### 第114步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN09

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN09**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN09 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_09 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_09`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.12（EX_IO2_5P）；02_TX_BUFFERS/R_RX_DN09.1（1）。 [完整端点N0520](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0520)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN09 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN09.1=`DN_DATA_RAW_09`，R_DATA_RAW_PD_DN09.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn10"></a>

### 第115步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN10

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN10**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN10 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_10 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_10`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.13（EX_IO2_6N）；02_TX_BUFFERS/R_RX_DN10.1（1）。 [完整端点N0521](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0521)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN10 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN10.1=`DN_DATA_RAW_10`，R_DATA_RAW_PD_DN10.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn11"></a>

### 第116步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN11

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN11**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN11 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_11 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_11`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.14（EX_IO2_6P）；02_TX_BUFFERS/R_RX_DN11.1（1）。 [完整端点N0522](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0522)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN11 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN11.1=`DN_DATA_RAW_11`，R_DATA_RAW_PD_DN11.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn12"></a>

### 第117步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN12

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN12**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN12 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_12 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_12`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.15（EX_IO2_7N）；02_TX_BUFFERS/R_RX_DN12.1（1）。 [完整端点N0523](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0523)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN12 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN12.1=`DN_DATA_RAW_12`，R_DATA_RAW_PD_DN12.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn13"></a>

### 第118步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN13

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN13**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN13 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_13 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_13`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.16（EX_IO2_7P）；02_TX_BUFFERS/R_RX_DN13.1（1）。 [完整端点N0524](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0524)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN13 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN13.1=`DN_DATA_RAW_13`，R_DATA_RAW_PD_DN13.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn14"></a>

### 第119步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN14

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN14**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN14 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_14 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_14`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.17（EX_IO2_8N）；02_TX_BUFFERS/R_RX_DN14.1（1）。 [完整端点N0525](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0525)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN14 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN14.1=`DN_DATA_RAW_14`，R_DATA_RAW_PD_DN14.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-data-raw-pd-dn15"></a>

### 第120步：在CENTRAL／02_TX_BUFFERS放置 R_DATA_RAW_PD_DN15

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DATA_RAW_PD_DN15**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN15 | RC0603FR-0710KL | 1 | 1 | DN_DATA_RAW_15 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_15`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.18（EX_IO2_8P）；02_TX_BUFFERS/R_RX_DN15.1（1）。 [完整端点N0526](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0526)。 |
| CENTRAL | 02_TX_BUFFERS | R_DATA_RAW_PD_DN15 | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DATA_RAW_PD_DN15.1=`DN_DATA_RAW_15`，R_DATA_RAW_PD_DN15.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn08"></a>

### 第121步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN08

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN08**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN08 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_08 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_08`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.11（EX_IO2_5N）；02_TX_BUFFERS/R_DATA_RAW_PD_DN08.1（1）。 [完整端点N0519](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0519)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN08 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_08 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN08.1（1）；02_TX_BUFFERS/U_TXB3.2（A0）。 [完整端点N0503](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0503)。 |

接完确认：R_RX_DN08.1=`DN_DATA_RAW_08`，R_RX_DN08.2=`DN_DATA_FILT_08`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn09"></a>

### 第122步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN09

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN09**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN09 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_09 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_09`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.12（EX_IO2_5P）；02_TX_BUFFERS/R_DATA_RAW_PD_DN09.1（1）。 [完整端点N0520](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0520)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN09 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_09 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN09.1（1）；02_TX_BUFFERS/U_TXB3.4（A1）。 [完整端点N0504](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0504)。 |

接完确认：R_RX_DN09.1=`DN_DATA_RAW_09`，R_RX_DN09.2=`DN_DATA_FILT_09`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn10"></a>

### 第123步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN10

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN10**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN10 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_10 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_10`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.13（EX_IO2_6N）；02_TX_BUFFERS/R_DATA_RAW_PD_DN10.1（1）。 [完整端点N0521](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0521)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN10 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_10 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN10.1（1）；02_TX_BUFFERS/U_TXB3.6（A2）。 [完整端点N0505](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0505)。 |

接完确认：R_RX_DN10.1=`DN_DATA_RAW_10`，R_RX_DN10.2=`DN_DATA_FILT_10`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn11"></a>

### 第124步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN11

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN11**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN11 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_11 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_11`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.14（EX_IO2_6P）；02_TX_BUFFERS/R_DATA_RAW_PD_DN11.1（1）。 [完整端点N0522](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0522)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN11 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_11 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN11.1（1）；02_TX_BUFFERS/U_TXB3.8（A3）。 [完整端点N0506](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0506)。 |

接完确认：R_RX_DN11.1=`DN_DATA_RAW_11`，R_RX_DN11.2=`DN_DATA_FILT_11`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn12"></a>

### 第125步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN12

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN12**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN12 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_12 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_12`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.15（EX_IO2_7N）；02_TX_BUFFERS/R_DATA_RAW_PD_DN12.1（1）。 [完整端点N0523](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0523)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN12 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_12 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN12.1（1）；02_TX_BUFFERS/U_TXB3.11（A4）。 [完整端点N0507](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0507)。 |

接完确认：R_RX_DN12.1=`DN_DATA_RAW_12`，R_RX_DN12.2=`DN_DATA_FILT_12`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn13"></a>

### 第126步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN13

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN13**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN13 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_13 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_13`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.16（EX_IO2_7P）；02_TX_BUFFERS/R_DATA_RAW_PD_DN13.1（1）。 [完整端点N0524](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0524)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN13 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_13 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN13.1（1）；02_TX_BUFFERS/U_TXB3.13（A5）。 [完整端点N0508](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0508)。 |

接完确认：R_RX_DN13.1=`DN_DATA_RAW_13`，R_RX_DN13.2=`DN_DATA_FILT_13`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn14"></a>

### 第127步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN14

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN14**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN14 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_14 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_14`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.17（EX_IO2_8N）；02_TX_BUFFERS/R_DATA_RAW_PD_DN14.1（1）。 [完整端点N0525](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0525)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN14 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_14 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN14.1（1）；02_TX_BUFFERS/U_TXB3.15（A6）。 [完整端点N0509](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0509)。 |

接完确认：R_RX_DN14.1=`DN_DATA_RAW_14`，R_RX_DN14.2=`DN_DATA_FILT_14`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-dn15"></a>

### 第128步：在CENTRAL／02_TX_BUFFERS放置 R_RX_DN15

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_DN15**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN15 | RC0603FR-0722RL | 1 | 1 | DN_DATA_RAW_15 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_RAW_15`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.18（EX_IO2_8P）；02_TX_BUFFERS/R_DATA_RAW_PD_DN15.1（1）。 [完整端点N0526](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0526)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_DN15 | RC0603FR-0722RL | 2 | 2 | DN_DATA_FILT_15 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_FILT_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_DN15.1（1）；02_TX_BUFFERS/U_TXB3.17（A7）。 [完整端点N0510](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0510)。 |

接完确认：R_RX_DN15.1=`DN_DATA_RAW_15`，R_RX_DN15.2=`DN_DATA_FILT_15`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn08"></a>

### 第129步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN08

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN08**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN08 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_08 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_08`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB3.18（Y0）。 [完整端点N0487](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0487)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN08 | RC0603FR-0747RL | 2 | 2 | DN_DATA_08 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_08`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.17（DATA_08）。 [完整端点N0471](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0471)。 |

接完确认：R_TX_DN08.1=`DN_DATA_DRV_08`，R_TX_DN08.2=`DN_DATA_08`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn09"></a>

### 第130步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN09

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN09**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN09 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_09 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_09`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB3.16（Y1）。 [完整端点N0488](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0488)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN09 | RC0603FR-0747RL | 2 | 2 | DN_DATA_09 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_09`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.19（DATA_09）。 [完整端点N0472](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0472)。 |

接完确认：R_TX_DN09.1=`DN_DATA_DRV_09`，R_TX_DN09.2=`DN_DATA_09`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn10"></a>

### 第131步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN10

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN10**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN10 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_10 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_10`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB3.14（Y2）。 [完整端点N0489](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0489)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN10 | RC0603FR-0747RL | 2 | 2 | DN_DATA_10 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_10`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.21（DATA_10）。 [完整端点N0473](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0473)。 |

接完确认：R_TX_DN10.1=`DN_DATA_DRV_10`，R_TX_DN10.2=`DN_DATA_10`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn11"></a>

### 第132步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN11

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN11**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN11 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_11 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_11`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB3.12（Y3）。 [完整端点N0490](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0490)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN11 | RC0603FR-0747RL | 2 | 2 | DN_DATA_11 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_11`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.23（DATA_11）。 [完整端点N0474](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0474)。 |

接完确认：R_TX_DN11.1=`DN_DATA_DRV_11`，R_TX_DN11.2=`DN_DATA_11`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn12"></a>

### 第133步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN12

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN12**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN12 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_12 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_12`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB3.9（Y4）。 [完整端点N0491](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0491)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN12 | RC0603FR-0747RL | 2 | 2 | DN_DATA_12 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_12`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.25（DATA_12）。 [完整端点N0475](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0475)。 |

接完确认：R_TX_DN12.1=`DN_DATA_DRV_12`，R_TX_DN12.2=`DN_DATA_12`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn13"></a>

### 第134步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN13

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN13**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN13 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_13 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_13`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB3.7（Y5）。 [完整端点N0492](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0492)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN13 | RC0603FR-0747RL | 2 | 2 | DN_DATA_13 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_13`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.27（DATA_13）。 [完整端点N0476](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0476)。 |

接完确认：R_TX_DN13.1=`DN_DATA_DRV_13`，R_TX_DN13.2=`DN_DATA_13`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn14"></a>

### 第135步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN14

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN14**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN14 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_14 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_14`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB3.5（Y6）。 [完整端点N0493](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0493)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN14 | RC0603FR-0747RL | 2 | 2 | DN_DATA_14 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_14`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.29（DATA_14）。 [完整端点N0477](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0477)。 |

接完确认：R_TX_DN14.1=`DN_DATA_DRV_14`，R_TX_DN14.2=`DN_DATA_14`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn15"></a>

### 第136步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN15

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN15**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXB3的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN15 | RC0603FR-0747RL | 1 | 1 | DN_DATA_DRV_15 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_DRV_15`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXB3.3（Y7）。 [完整端点N0494](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0494)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN15 | RC0603FR-0747RL | 2 | 2 | DN_DATA_15 | PASSIVE | 从此脚引线，标注精确网名`DN_DATA_15`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.31（DATA_15）。 [完整端点N0478](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0478)。 |

接完确认：R_TX_DN15.1=`DN_DATA_DRV_15`，R_TX_DN15.2=`DN_DATA_15`；不可旁路该器件把两个网名短在一起。

<a id="central-u-txclk"></a>

### 第137步：在CENTRAL／02_TX_BUFFERS放置 U_TXCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **U_TXCLK**，精确型号 **SN74LVT244BPWR**，封装 **PW/TSSOP20**。

按信号从接口到输出的顺序摆放LVT缓冲，供电本地V3V3、地GND；PW20无EP。每个通道A/Y和两个OE_N按实际脚号，未用输入接表定网络、未用输出独立NC。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 1 | 1OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 2 | A0 | MASTER_SRCLK_FILT | IN | 从此脚引线，标注精确网名`MASTER_SRCLK_FILT`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_SRCLK.2（2）；02_TX_BUFFERS/C_RX_SRCLK.1（1）；02_TX_BUFFERS/U_TXCLK.4（A1）。 [完整端点N0573](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0573)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 3 | Y7 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 4 | A1 | MASTER_SRCLK_FILT | IN | 从此脚引线，标注精确网名`MASTER_SRCLK_FILT`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_SRCLK.2（2）；02_TX_BUFFERS/C_RX_SRCLK.1（1）；02_TX_BUFFERS/U_TXCLK.2（A0）。 [完整端点N0573](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0573)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 5 | Y6 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 6 | A2 | MASTER_RCLK_FILT | IN | 从此脚引线，标注精确网名`MASTER_RCLK_FILT`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_RCLK.2（2）；02_TX_BUFFERS/C_RX_RCLK.1（1）；02_TX_BUFFERS/U_TXCLK.8（A3）。 [完整端点N0571](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0571)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 7 | Y5 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 8 | A3 | MASTER_RCLK_FILT | IN | 从此脚引线，标注精确网名`MASTER_RCLK_FILT`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_RCLK.2（2）；02_TX_BUFFERS/C_RX_RCLK.1（1）；02_TX_BUFFERS/U_TXCLK.6（A2）。 [完整端点N0571](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0571)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 9 | Y4 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 10 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 11 | A4 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 12 | Y3 | DN_RCLK_DRV | OUT | 从此脚引线，标注精确网名`DN_RCLK_DRV`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN_RCLK.1（1）。 [完整端点N0536](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0536)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 13 | A5 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 14 | Y2 | UP_RCLK_DRV | OUT | 从此脚引线，标注精确网名`UP_RCLK_DRV`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP_RCLK.1（1）。 [完整端点N0656](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0656)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 15 | A6 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 16 | Y1 | DN_SRCLK_DRV | OUT | 从此脚引线，标注精确网名`DN_SRCLK_DRV`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_DN_SRCLK.1（1）。 [完整端点N0551](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0551)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 17 | A7 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 18 | Y0 | UP_SRCLK_DRV | OUT | 从此脚引线，标注精确网名`UP_SRCLK_DRV`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_TX_UP_SRCLK.1（1）。 [完整端点N0671](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0671)。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 19 | 2OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_TXCLK | SN74LVT244BPWR | 20 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_TXCLK.1→GND；U_TXCLK.19→GND；U_TXCLK.10→GND；U_TXCLK.20→V3V3；U_TXCLK.11→GND；U_TXCLK.13→GND；U_TXCLK.15→GND；U_TXCLK.17→GND。 NC脚9,7,5,3逐个单独标记。

<a id="central-c-u-txclk"></a>

### 第138步：在CENTRAL／02_TX_BUFFERS放置 C_U_TXCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_U_TXCLK**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_U_TXCLK | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 02_TX_BUFFERS | C_U_TXCLK | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_TXCLK.1=`V3V3`，C_U_TXCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-rclk"></a>

### 第139步：在CENTRAL／02_TX_BUFFERS放置 C_RX_RCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_RCLK**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_RCLK | CC0603JRNPO9BN3R3 | 1 | 1 | MASTER_RCLK_FILT | PASSIVE | 从此脚引线，标注精确网名`MASTER_RCLK_FILT`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_RCLK.2（2）；02_TX_BUFFERS/U_TXCLK.6（A2）；02_TX_BUFFERS/U_TXCLK.8（A3）。 [完整端点N0571](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0571)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_RCLK | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_RCLK.1=`MASTER_RCLK_FILT`，C_RX_RCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-rx-srclk"></a>

### 第140步：在CENTRAL／02_TX_BUFFERS放置 C_RX_SRCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_RX_SRCLK**，精确型号 **CC0603JRNPO9BN3R3**，封装 **0603**。其值为 **3.3pF**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_RX_SRCLK | CC0603JRNPO9BN3R3 | 1 | 1 | MASTER_SRCLK_FILT | PASSIVE | 从此脚引线，标注精确网名`MASTER_SRCLK_FILT`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_RX_SRCLK.2（2）；02_TX_BUFFERS/U_TXCLK.2（A0）；02_TX_BUFFERS/U_TXCLK.4（A1）。 [完整端点N0573](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0573)。 |
| CENTRAL | 02_TX_BUFFERS | C_RX_SRCLK | CC0603JRNPO9BN3R3 | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_RX_SRCLK.1=`MASTER_SRCLK_FILT`，C_RX_SRCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-def-master-rclk"></a>

### 第141步：在CENTRAL／02_TX_BUFFERS放置 R_DEF_MASTER_RCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DEF_MASTER_RCLK**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DEF_MASTER_RCLK | RC0603FR-0710KL | 1 | 1 | MASTER_RCLK | PASSIVE | 从此脚引线，标注精确网名`MASTER_RCLK`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.20（EX_IO1_9P）；02_TX_BUFFERS/R_RX_RCLK.1（1）。 [完整端点N0570](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0570)。 |
| CENTRAL | 02_TX_BUFFERS | R_DEF_MASTER_RCLK | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DEF_MASTER_RCLK.1=`MASTER_RCLK`，R_DEF_MASTER_RCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-def-master-srclk"></a>

### 第142步：在CENTRAL／02_TX_BUFFERS放置 R_DEF_MASTER_SRCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DEF_MASTER_SRCLK**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DEF_MASTER_SRCLK | RC0603FR-0710KL | 1 | 1 | MASTER_SRCLK | PASSIVE | 从此脚引线，标注精确网名`MASTER_SRCLK`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.19（EX_IO1_9N）；02_TX_BUFFERS/R_RX_SRCLK.1（1）。 [完整端点N0572](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0572)。 |
| CENTRAL | 02_TX_BUFFERS | R_DEF_MASTER_SRCLK | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DEF_MASTER_SRCLK.1=`MASTER_SRCLK`，R_DEF_MASTER_SRCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-rclk"></a>

### 第143步：在CENTRAL／02_TX_BUFFERS放置 R_RX_RCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_RCLK**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_RCLK | RC0603FR-0722RL | 1 | 1 | MASTER_RCLK | PASSIVE | 从此脚引线，标注精确网名`MASTER_RCLK`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.20（EX_IO1_9P）；02_TX_BUFFERS/R_DEF_MASTER_RCLK.1（1）。 [完整端点N0570](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0570)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_RCLK | RC0603FR-0722RL | 2 | 2 | MASTER_RCLK_FILT | PASSIVE | 从此脚引线，标注精确网名`MASTER_RCLK_FILT`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_RCLK.1（1）；02_TX_BUFFERS/U_TXCLK.6（A2）；02_TX_BUFFERS/U_TXCLK.8（A3）。 [完整端点N0571](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0571)。 |

接完确认：R_RX_RCLK.1=`MASTER_RCLK`，R_RX_RCLK.2=`MASTER_RCLK_FILT`；不可旁路该器件把两个网名短在一起。

<a id="central-r-rx-srclk"></a>

### 第144步：在CENTRAL／02_TX_BUFFERS放置 R_RX_SRCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_RX_SRCLK**，精确型号 **RC0603FR-0722RL**，封装 **0603**。其值为 **22**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_RX_SRCLK | RC0603FR-0722RL | 1 | 1 | MASTER_SRCLK | PASSIVE | 从此脚引线，标注精确网名`MASTER_SRCLK`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.19（EX_IO1_9N）；02_TX_BUFFERS/R_DEF_MASTER_SRCLK.1（1）。 [完整端点N0572](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0572)。 |
| CENTRAL | 02_TX_BUFFERS | R_RX_SRCLK | RC0603FR-0722RL | 2 | 2 | MASTER_SRCLK_FILT | PASSIVE | 从此脚引线，标注精确网名`MASTER_SRCLK_FILT`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/C_RX_SRCLK.1（1）；02_TX_BUFFERS/U_TXCLK.2（A0）；02_TX_BUFFERS/U_TXCLK.4（A1）。 [完整端点N0573](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0573)。 |

接完确认：R_RX_SRCLK.1=`MASTER_SRCLK`，R_RX_SRCLK.2=`MASTER_SRCLK_FILT`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn-rclk"></a>

### 第145步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN_RCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN_RCLK**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN_RCLK | RC0603FR-0747RL | 1 | 1 | DN_RCLK_DRV | PASSIVE | 从此脚引线，标注精确网名`DN_RCLK_DRV`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXCLK.12（Y3）。 [完整端点N0536](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0536)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN_RCLK | RC0603FR-0747RL | 2 | 2 | DN_RCLK | PASSIVE | 从此脚引线，标注精确网名`DN_RCLK`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.35（RCLK）。 [完整端点N0535](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0535)。 |

接完确认：R_TX_DN_RCLK.1=`DN_RCLK_DRV`，R_TX_DN_RCLK.2=`DN_RCLK`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-dn-srclk"></a>

### 第146步：在CENTRAL／02_TX_BUFFERS放置 R_TX_DN_SRCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_DN_SRCLK**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN_SRCLK | RC0603FR-0747RL | 1 | 1 | DN_SRCLK_DRV | PASSIVE | 从此脚引线，标注精确网名`DN_SRCLK_DRV`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXCLK.16（Y1）。 [完整端点N0551](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0551)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_DN_SRCLK | RC0603FR-0747RL | 2 | 2 | DN_SRCLK | PASSIVE | 从此脚引线，标注精确网名`DN_SRCLK`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.33（SRCLK）。 [完整端点N0550](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0550)。 |

接完确认：R_TX_DN_SRCLK.1=`DN_SRCLK_DRV`，R_TX_DN_SRCLK.2=`DN_SRCLK`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up-rclk"></a>

### 第147步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP_RCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP_RCLK**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP_RCLK | RC0603FR-0747RL | 1 | 1 | UP_RCLK_DRV | PASSIVE | 从此脚引线，标注精确网名`UP_RCLK_DRV`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXCLK.14（Y2）。 [完整端点N0656](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0656)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP_RCLK | RC0603FR-0747RL | 2 | 2 | UP_RCLK | PASSIVE | 从此脚引线，标注精确网名`UP_RCLK`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.35（RCLK）。 [完整端点N0655](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0655)。 |

接完确认：R_TX_UP_RCLK.1=`UP_RCLK_DRV`，R_TX_UP_RCLK.2=`UP_RCLK`；不可旁路该器件把两个网名短在一起。

<a id="central-r-tx-up-srclk"></a>

### 第148步：在CENTRAL／02_TX_BUFFERS放置 R_TX_UP_SRCLK

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_TX_UP_SRCLK**，精确型号 **RC0603FR-0747RL**，封装 **0603**。其值为 **47**。

纸面位置：紧邻本页U_TXCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP_SRCLK | RC0603FR-0747RL | 1 | 1 | UP_SRCLK_DRV | PASSIVE | 从此脚引线，标注精确网名`UP_SRCLK_DRV`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_TXCLK.18（Y0）。 [完整端点N0671](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0671)。 |
| CENTRAL | 02_TX_BUFFERS | R_TX_UP_SRCLK | RC0603FR-0747RL | 2 | 2 | UP_SRCLK | PASSIVE | 从此脚引线，标注精确网名`UP_SRCLK`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.33（SRCLK）。 [完整端点N0670](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0670)。 |

接完确认：R_TX_UP_SRCLK.1=`UP_SRCLK_DRV`，R_TX_UP_SRCLK.2=`UP_SRCLK`；不可旁路该器件把两个网名短在一起。

<a id="central-u-cbuf1"></a>

### 第149步：在CENTRAL／02_TX_BUFFERS放置 U_CBUF1

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **U_CBUF1**，精确型号 **SN74LVC244APWR**，封装 **PW/TSSOP20**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 1 | 1OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 2 | A0 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 3 | Y7 | DN_TX_PERMIT_B | OUT | 从此脚引线，标注精确网名`DN_TX_PERMIT_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_DN_TX_PERMIT_B.1（1）。 [完整端点N0553](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0553)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 4 | A1 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 5 | Y6 | UP_TX_PERMIT_B | OUT | 从此脚引线，标注精确网名`UP_TX_PERMIT_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_UP_TX_PERMIT_B.1（1）。 [完整端点N0673](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0673)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 6 | A2 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 7 | Y5 | DN_OE_N_B | OUT | 从此脚引线，标注精确网名`DN_OE_N_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_DN_OE_N_B.1（1）。 [完整端点N0532](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0532)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 8 | A3 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 9 | Y4 | UP_OE_N_B | OUT | 从此脚引线，标注精确网名`UP_OE_N_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_UP_OE_N_B.1（1）。 [完整端点N0652](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0652)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 10 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 11 | A4 | MASTER_OE_N | IN | 从此脚引线，标注精确网名`MASTER_OE_N`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.21（EX_IO1_10N）；02_TX_BUFFERS/U_CBUF1.13（A5）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.1（1）；02_TX_BUFFERS/R_OFF_MASTER_OE_N.1（1）。 [完整端点N0569](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0569)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 12 | Y3 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 13 | A5 | MASTER_OE_N | IN | 从此脚引线，标注精确网名`MASTER_OE_N`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.21（EX_IO1_10N）；02_TX_BUFFERS/U_CBUF1.11（A4）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.1（1）；02_TX_BUFFERS/R_OFF_MASTER_OE_N.1（1）。 [完整端点N0569](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0569)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 14 | Y2 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 15 | A6 | UP_TX_PERMIT_RAW | IN | 从此脚引线，标注精确网名`UP_TX_PERMIT_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.22（EX_IO1_10P）；02_TX_BUFFERS/R_DEF_UP_TX_PERMIT_RAW.1（1）。 [完整端点N0674](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0674)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 16 | Y1 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 17 | A7 | DN_TX_PERMIT_RAW | IN | 从此脚引线，标注精确网名`DN_TX_PERMIT_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.22（EX_IO2_10P）；02_TX_BUFFERS/R_DEF_DN_TX_PERMIT_RAW.1（1）。 [完整端点N0554](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0554)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 18 | Y0 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 19 | 2OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF1 | SN74LVC244APWR | 20 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_CBUF1.1→GND；U_CBUF1.19→GND；U_CBUF1.10→GND；U_CBUF1.20→V3V3；U_CBUF1.2→GND；U_CBUF1.4→GND；U_CBUF1.6→GND；U_CBUF1.8→GND。 NC脚18,16,14,12逐个单独标记。

<a id="central-c-u-cbuf1"></a>

### 第150步：在CENTRAL／02_TX_BUFFERS放置 C_U_CBUF1

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_U_CBUF1**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_U_CBUF1 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 02_TX_BUFFERS | C_U_CBUF1 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_CBUF1.1=`V3V3`，C_U_CBUF1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-def-dn-tx-permit-raw"></a>

### 第151步：在CENTRAL／02_TX_BUFFERS放置 R_DEF_DN_TX_PERMIT_RAW

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DEF_DN_TX_PERMIT_RAW**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DEF_DN_TX_PERMIT_RAW | RC0603FR-0710KL | 1 | 1 | DN_TX_PERMIT_RAW | PASSIVE | 从此脚引线，标注精确网名`DN_TX_PERMIT_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.22（EX_IO2_10P）；02_TX_BUFFERS/U_CBUF1.17（A7）。 [完整端点N0554](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0554)。 |
| CENTRAL | 02_TX_BUFFERS | R_DEF_DN_TX_PERMIT_RAW | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DEF_DN_TX_PERMIT_RAW.1=`DN_TX_PERMIT_RAW`，R_DEF_DN_TX_PERMIT_RAW.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-def-master-oe-n"></a>

### 第152步：在CENTRAL／02_TX_BUFFERS放置 R_DEF_MASTER_OE_N

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DEF_MASTER_OE_N**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DEF_MASTER_OE_N | CRCW060310K0FKEA | 1 | 1 | MASTER_OE_N | PASSIVE | 从此脚引线，标注精确网名`MASTER_OE_N`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.21（EX_IO1_10N）；02_TX_BUFFERS/U_CBUF1.11（A4）；02_TX_BUFFERS/U_CBUF1.13（A5）；02_TX_BUFFERS/R_OFF_MASTER_OE_N.1（1）。 [完整端点N0569](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0569)。 |
| CENTRAL | 02_TX_BUFFERS | R_DEF_MASTER_OE_N | CRCW060310K0FKEA | 2 | 2 | AX_VIO_REF3V3 | PASSIVE | 接本板`AX_VIO_REF3V3`电源/参考标签；来源：CENTRAL.J_J11.39引入的AX接口参考，不能与本地V3V3并联，预算≤50mA。同网另有15个物理端点，逐个见[完整端点N0450](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0450)；例如01_FPGA_HEADERS/J_J11.39（AX_INTERFACE_REFERENCE）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.2（2）；05_RX_INPUT/R_DEF_DN_RX_BLANK_RAW.2（2）。 |

接完确认：R_DEF_MASTER_OE_N.1=`MASTER_OE_N`，R_DEF_MASTER_OE_N.2=`AX_VIO_REF3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-def-up-tx-permit-raw"></a>

### 第153步：在CENTRAL／02_TX_BUFFERS放置 R_DEF_UP_TX_PERMIT_RAW

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DEF_UP_TX_PERMIT_RAW**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DEF_UP_TX_PERMIT_RAW | RC0603FR-0710KL | 1 | 1 | UP_TX_PERMIT_RAW | PASSIVE | 从此脚引线，标注精确网名`UP_TX_PERMIT_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.22（EX_IO1_10P）；02_TX_BUFFERS/U_CBUF1.15（A6）。 [完整端点N0674](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0674)。 |
| CENTRAL | 02_TX_BUFFERS | R_DEF_UP_TX_PERMIT_RAW | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DEF_UP_TX_PERMIT_RAW.1=`UP_TX_PERMIT_RAW`，R_DEF_UP_TX_PERMIT_RAW.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-off-master-oe-n"></a>

### 第154步：在CENTRAL／02_TX_BUFFERS放置 R_OFF_MASTER_OE_N

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_OFF_MASTER_OE_N**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_OFF_MASTER_OE_N | CRCW0603100KFKEA | 1 | 1 | MASTER_OE_N | PASSIVE | 从此脚引线，标注精确网名`MASTER_OE_N`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.21（EX_IO1_10N）；02_TX_BUFFERS/U_CBUF1.11（A4）；02_TX_BUFFERS/U_CBUF1.13（A5）；02_TX_BUFFERS/R_DEF_MASTER_OE_N.1（1）。 [完整端点N0569](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0569)。 |
| CENTRAL | 02_TX_BUFFERS | R_OFF_MASTER_OE_N | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_OFF_MASTER_OE_N.1=`MASTER_OE_N`，R_OFF_MASTER_OE_N.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-dn-oe-n-b"></a>

### 第155步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_DN_OE_N_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_DN_OE_N_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_OE_N_B | CRCW060333R0FKEA | 1 | 1 | DN_OE_N_B | PASSIVE | 从此脚引线，标注精确网名`DN_OE_N_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF1.7（Y5）。 [完整端点N0532](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0532)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_OE_N_B | CRCW060333R0FKEA | 2 | 2 | DN_OE_N | PASSIVE | 从此脚引线，标注精确网名`DN_OE_N`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.37（OE_N）。 [完整端点N0531](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0531)。 |

接完确认：R_SRC_DN_OE_N_B.1=`DN_OE_N_B`，R_SRC_DN_OE_N_B.2=`DN_OE_N`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-dn-tx-permit-b"></a>

### 第156步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_DN_TX_PERMIT_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_DN_TX_PERMIT_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_TX_PERMIT_B | CRCW060333R0FKEA | 1 | 1 | DN_TX_PERMIT_B | PASSIVE | 从此脚引线，标注精确网名`DN_TX_PERMIT_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF1.3（Y7）。 [完整端点N0553](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0553)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_TX_PERMIT_B | CRCW060333R0FKEA | 2 | 2 | DN_TX_PERMIT | PASSIVE | 从此脚引线，标注精确网名`DN_TX_PERMIT`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.39（TX_PERMIT）。 [完整端点N0552](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0552)。 |

接完确认：R_SRC_DN_TX_PERMIT_B.1=`DN_TX_PERMIT_B`，R_SRC_DN_TX_PERMIT_B.2=`DN_TX_PERMIT`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-up-oe-n-b"></a>

### 第157步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_UP_OE_N_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_UP_OE_N_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_OE_N_B | CRCW060333R0FKEA | 1 | 1 | UP_OE_N_B | PASSIVE | 从此脚引线，标注精确网名`UP_OE_N_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF1.9（Y4）。 [完整端点N0652](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0652)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_OE_N_B | CRCW060333R0FKEA | 2 | 2 | UP_OE_N | PASSIVE | 从此脚引线，标注精确网名`UP_OE_N`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.37（OE_N）。 [完整端点N0651](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0651)。 |

接完确认：R_SRC_UP_OE_N_B.1=`UP_OE_N_B`，R_SRC_UP_OE_N_B.2=`UP_OE_N`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-up-tx-permit-b"></a>

### 第158步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_UP_TX_PERMIT_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_UP_TX_PERMIT_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF1的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_TX_PERMIT_B | CRCW060333R0FKEA | 1 | 1 | UP_TX_PERMIT_B | PASSIVE | 从此脚引线，标注精确网名`UP_TX_PERMIT_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF1.5（Y6）。 [完整端点N0673](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0673)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_TX_PERMIT_B | CRCW060333R0FKEA | 2 | 2 | UP_TX_PERMIT | PASSIVE | 从此脚引线，标注精确网名`UP_TX_PERMIT`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.39（TX_PERMIT）。 [完整端点N0672](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0672)。 |

接完确认：R_SRC_UP_TX_PERMIT_B.1=`UP_TX_PERMIT_B`，R_SRC_UP_TX_PERMIT_B.2=`UP_TX_PERMIT`；不可旁路该器件把两个网名短在一起。

<a id="central-u-cbuf2"></a>

### 第159步：在CENTRAL／02_TX_BUFFERS放置 U_CBUF2

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **U_CBUF2**，精确型号 **SN74LVC244APWR**，封装 **PW/TSSOP20**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 1 | 1OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 2 | A0 | UP_RX_BLANK_RAW | IN | 从此脚引线，标注精确网名`UP_RX_BLANK_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.24（EX_IO1_11P）；05_RX_INPUT/R_DEF_UP_RX_BLANK_RAW.1（1）；05_RX_INPUT/R_OFF_UP_RX_BLANK_RAW.1（1）；05_RX_INPUT/U_BLANKINV_UP.2（A）。 [完整端点N0667](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0667)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 3 | Y7 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 4 | A1 | DN_RX_BLANK_RAW | IN | 从此脚引线，标注精确网名`DN_RX_BLANK_RAW`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J11.24（EX_IO2_11P）；05_RX_INPUT/R_DEF_DN_RX_BLANK_RAW.1（1）；05_RX_INPUT/R_OFF_DN_RX_BLANK_RAW.1（1）；05_RX_INPUT/U_BLANKINV_DN.2（A）。 [完整端点N0547](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0547)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 5 | Y6 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 6 | A2 | MASTER_HB | IN | 从此脚引线，标注精确网名`MASTER_HB`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.25（EX_IO1_12N）；02_TX_BUFFERS/U_CBUF2.8（A3）；02_TX_BUFFERS/R_DEF_MASTER_HB.1（1）。 [完整端点N0568](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0568)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 7 | Y5 | DN_CENTRAL_POWER_OK_B | OUT | 从此脚引线，标注精确网名`DN_CENTRAL_POWER_OK_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_DN_CENTRAL_POWER_OK_B.1（1）。 [完整端点N0462](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0462)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 8 | A3 | MASTER_HB | IN | 从此脚引线，标注精确网名`MASTER_HB`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.25（EX_IO1_12N）；02_TX_BUFFERS/U_CBUF2.6（A2）；02_TX_BUFFERS/R_DEF_MASTER_HB.1（1）。 [完整端点N0568](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0568)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 9 | Y4 | UP_CENTRAL_POWER_OK_B | OUT | 从此脚引线，标注精确网名`UP_CENTRAL_POWER_OK_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_UP_CENTRAL_POWER_OK_B.1（1）。 [完整端点N0582](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0582)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 10 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 11 | A4 | CENTRAL_READY | IN | 从此脚引线，标注精确网名`CENTRAL_READY`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.13（A5）；06_I2C_TEMP_SAFETY/U_G1.3（2Y）；06_I2C_TEMP_SAFETY/U_RET1.17（B5）。 [完整端点N0457](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0457)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 12 | Y3 | DN_HB_B | OUT | 从此脚引线，标注精确网名`DN_HB_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_DN_HB_B.1（1）。 [完整端点N0530](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0530)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 13 | A5 | CENTRAL_READY | IN | 从此脚引线，标注精确网名`CENTRAL_READY`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.11（A4）；06_I2C_TEMP_SAFETY/U_G1.3（2Y）；06_I2C_TEMP_SAFETY/U_RET1.17（B5）。 [完整端点N0457](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0457)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 14 | Y2 | UP_HB_B | OUT | 从此脚引线，标注精确网名`UP_HB_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_UP_HB_B.1（1）。 [完整端点N0650](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0650)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 15 | A6 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 16 | Y1 | DN_RX_BLANK_B | OUT | 从此脚引线，标注精确网名`DN_RX_BLANK_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_DN_RX_BLANK_B.1（1）。 [完整端点N0546](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0546)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 17 | A7 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 18 | Y0 | UP_RX_BLANK_B | OUT | 从此脚引线，标注精确网名`UP_RX_BLANK_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/R_SRC_UP_RX_BLANK_B.1（1）。 [完整端点N0666](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0666)。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 19 | 2OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 02_TX_BUFFERS | U_CBUF2 | SN74LVC244APWR | 20 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_CBUF2.1→GND；U_CBUF2.19→GND；U_CBUF2.10→GND；U_CBUF2.20→V3V3；U_CBUF2.15→GND；U_CBUF2.17→GND。 NC脚5,3逐个单独标记。

<a id="central-c-u-cbuf2"></a>

### 第160步：在CENTRAL／02_TX_BUFFERS放置 C_U_CBUF2

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **C_U_CBUF2**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_CBUF2的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | C_U_CBUF2 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 02_TX_BUFFERS | C_U_CBUF2 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_CBUF2.1=`V3V3`，C_U_CBUF2.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-def-master-hb"></a>

### 第161步：在CENTRAL／02_TX_BUFFERS放置 R_DEF_MASTER_HB

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_DEF_MASTER_HB**，精确型号 **RC0603FR-0710KL**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_CBUF2的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_DEF_MASTER_HB | RC0603FR-0710KL | 1 | 1 | MASTER_HB | PASSIVE | 从此脚引线，标注精确网名`MASTER_HB`；跨页使用同名板内标签。同网还接：01_FPGA_HEADERS/J_J10.25（EX_IO1_12N）；02_TX_BUFFERS/U_CBUF2.6（A2）；02_TX_BUFFERS/U_CBUF2.8（A3）。 [完整端点N0568](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0568)。 |
| CENTRAL | 02_TX_BUFFERS | R_DEF_MASTER_HB | RC0603FR-0710KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_DEF_MASTER_HB.1=`MASTER_HB`，R_DEF_MASTER_HB.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-dn-central-power-ok-b"></a>

### 第162步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_DN_CENTRAL_POWER_OK_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_DN_CENTRAL_POWER_OK_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_CENTRAL_POWER_OK_B | CRCW060333R0FKEA | 1 | 1 | DN_CENTRAL_POWER_OK_B | PASSIVE | 从此脚引线，标注精确网名`DN_CENTRAL_POWER_OK_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.7（Y5）。 [完整端点N0462](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0462)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_CENTRAL_POWER_OK_B | CRCW060333R0FKEA | 2 | 2 | DN_CENTRAL_POWER_OK | PASSIVE | 从此脚引线，标注精确网名`DN_CENTRAL_POWER_OK`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.41（CENTRAL_POWER_OK）。 [完整端点N0461](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0461)。 |

接完确认：R_SRC_DN_CENTRAL_POWER_OK_B.1=`DN_CENTRAL_POWER_OK_B`，R_SRC_DN_CENTRAL_POWER_OK_B.2=`DN_CENTRAL_POWER_OK`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-dn-hb-b"></a>

### 第163步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_DN_HB_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_DN_HB_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_HB_B | CRCW060333R0FKEA | 1 | 1 | DN_HB_B | PASSIVE | 从此脚引线，标注精确网名`DN_HB_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.12（Y3）。 [完整端点N0530](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0530)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_HB_B | CRCW060333R0FKEA | 2 | 2 | DN_HB | PASSIVE | 从此脚引线，标注精确网名`DN_HB`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.45（HB）。 [完整端点N0529](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0529)。 |

接完确认：R_SRC_DN_HB_B.1=`DN_HB_B`，R_SRC_DN_HB_B.2=`DN_HB`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-dn-rx-blank-b"></a>

### 第164步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_DN_RX_BLANK_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_DN_RX_BLANK_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_RX_BLANK_B | CRCW060333R0FKEA | 1 | 1 | DN_RX_BLANK_B | PASSIVE | 从此脚引线，标注精确网名`DN_RX_BLANK_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.16（Y1）。 [完整端点N0546](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0546)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_DN_RX_BLANK_B | CRCW060333R0FKEA | 2 | 2 | DN_RX_BLANK | PASSIVE | 从此脚引线，标注精确网名`DN_RX_BLANK`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_DN.43（RX_BLANK）。 [完整端点N0545](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0545)。 |

接完确认：R_SRC_DN_RX_BLANK_B.1=`DN_RX_BLANK_B`，R_SRC_DN_RX_BLANK_B.2=`DN_RX_BLANK`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-up-central-power-ok-b"></a>

### 第165步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_UP_CENTRAL_POWER_OK_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_UP_CENTRAL_POWER_OK_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_CENTRAL_POWER_OK_B | CRCW060333R0FKEA | 1 | 1 | UP_CENTRAL_POWER_OK_B | PASSIVE | 从此脚引线，标注精确网名`UP_CENTRAL_POWER_OK_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.9（Y4）。 [完整端点N0582](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0582)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_CENTRAL_POWER_OK_B | CRCW060333R0FKEA | 2 | 2 | UP_CENTRAL_POWER_OK | PASSIVE | 从此脚引线，标注精确网名`UP_CENTRAL_POWER_OK`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.41（CENTRAL_POWER_OK）。 [完整端点N0581](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0581)。 |

接完确认：R_SRC_UP_CENTRAL_POWER_OK_B.1=`UP_CENTRAL_POWER_OK_B`，R_SRC_UP_CENTRAL_POWER_OK_B.2=`UP_CENTRAL_POWER_OK`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-up-hb-b"></a>

### 第166步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_UP_HB_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_UP_HB_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_HB_B | CRCW060333R0FKEA | 1 | 1 | UP_HB_B | PASSIVE | 从此脚引线，标注精确网名`UP_HB_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.14（Y2）。 [完整端点N0650](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0650)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_HB_B | CRCW060333R0FKEA | 2 | 2 | UP_HB | PASSIVE | 从此脚引线，标注精确网名`UP_HB`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.45（HB）。 [完整端点N0649](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0649)。 |

接完确认：R_SRC_UP_HB_B.1=`UP_HB_B`，R_SRC_UP_HB_B.2=`UP_HB`；不可旁路该器件把两个网名短在一起。

<a id="central-r-src-up-rx-blank-b"></a>

### 第167步：在CENTRAL／02_TX_BUFFERS放置 R_SRC_UP_RX_BLANK_B

在 **CENTRAL板的02_TX_BUFFERS图页**，接着放置 **R_SRC_UP_RX_BLANK_B**，精确型号 **CRCW060333R0FKEA**，封装 **0603**。其值为 **33**。

纸面位置：紧邻本页U_CBUF2的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_RX_BLANK_B | CRCW060333R0FKEA | 1 | 1 | UP_RX_BLANK_B | PASSIVE | 从此脚引线，标注精确网名`UP_RX_BLANK_B`；跨页使用同名板内标签。同网还接：02_TX_BUFFERS/U_CBUF2.18（Y0）。 [完整端点N0666](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0666)。 |
| CENTRAL | 02_TX_BUFFERS | R_SRC_UP_RX_BLANK_B | CRCW060333R0FKEA | 2 | 2 | UP_RX_BLANK | PASSIVE | 从此脚引线，标注精确网名`UP_RX_BLANK`；跨页使用同名板内标签。同网还接：03_ARRAY_HEADERS/J_UP.43（RX_BLANK）。 [完整端点N0665](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0665)。 |

接完确认：R_SRC_UP_RX_BLANK_B.1=`UP_RX_BLANK_B`，R_SRC_UP_RX_BLANK_B.2=`UP_RX_BLANK`；不可旁路该器件把两个网名短在一起。

本页完成核对：**167个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。
