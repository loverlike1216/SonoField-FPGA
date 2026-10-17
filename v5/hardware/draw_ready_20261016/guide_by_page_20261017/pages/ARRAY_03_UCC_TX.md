# ARRAY／03_UCC_TX逐步连接分册

本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。

<a id="page-array-03-ucc-tx"></a>

## ARRAY板／03_UCC_TX图页

按U_DRV00→TX00/TX01，U_DRV01→TX02/TX03，直至U_DRV31→TX62/TX63排列。驱动后依次串150Ω、100nF、换能器；泄放并到换能器两端。

<a id="array-u-drv00"></a>

### 第001步：在ARRAY／03_UCC_TX放置 U_DRV00

在 **ARRAY板的03_UCC_TX图页**，先放置 **U_DRV00**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV00 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）；03_UCC_TX/U_DRV01.8（ENB）。 |
| ARRAY | 03_UCC_TX | U_DRV00 | UCC27624QDRQ1 | 2 | INA | TXLOG_00 | IN | 从此脚引线，标注精确网名`TXLOG_00`；跨页使用同名板内标签。同网还接：02_595/U_SR00.15（QA）；02_595/R_TX_PD00.1（1）。 [完整端点N0125](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0125)。 |
| ARRAY | 03_UCC_TX | U_DRV00 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV00 | UCC27624QDRQ1 | 4 | INB | TXLOG_01 | IN | 从此脚引线，标注精确网名`TXLOG_01`；跨页使用同名板内标签。同网还接：02_595/U_SR00.1（QB）；02_595/R_TX_PD01.1（1）。 [完整端点N0126](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0126)。 |
| ARRAY | 03_UCC_TX | U_DRV00 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_01 | OUT | 从此脚引线，标注精确网名`TXOUT_01`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX01.1（1）。 [完整端点N0190](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0190)。 |
| ARRAY | 03_UCC_TX | U_DRV00 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV00 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_00 | OUT | 从此脚引线，标注精确网名`TXOUT_00`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX00.1（1）。 [完整端点N0189](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0189)。 |
| ARRAY | 03_UCC_TX | U_DRV00 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV01.1（ENA）；03_UCC_TX/U_DRV01.8（ENB）。 |

接完确认：电源/地/参考为U_DRV00.3→GND；U_DRV00.6→VTX。

<a id="array-c-u-drv00"></a>

### 第002步：在ARRAY／03_UCC_TX放置 C_U_DRV00

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV00**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV00的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV00 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV00 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV00.1=`VTX`，C_U_DRV00.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-c-drv-bulk00"></a>

### 第003步：在ARRAY／03_UCC_TX放置 C_DRV_BULK00

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_DRV_BULK00**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_DRV00的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_DRV_BULK00 | C0603C105K3RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_DRV_BULK00 | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_DRV_BULK00.1=`VTX`，C_DRV_BULK00.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx00"></a>

### 第004步：在ARRAY／03_UCC_TX放置 R_TX00

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX00**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV00输出与C_TX_AC00之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX00 | CRCW2512150RFKEG | 1 | 1 | TXOUT_00 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_00`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV00.7（OUTA）。 [完整端点N0189](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0189)。 |
| ARRAY | 03_UCC_TX | R_TX00 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC00 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC00`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC00.1（1）。 [完整端点N0317](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0317)。 |

接完确认：R_TX00.1=`TXOUT_00`，R_TX00.2=`TX_AC_SRC00`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac00"></a>

### 第005步：在ARRAY／03_UCC_TX放置 C_TX_AC00

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC00**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX00之后、TX00之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC00 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC00 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC00`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX00.2（2）。 [完整端点N0317](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0317)。 |
| ARRAY | 03_UCC_TX | C_TX_AC00 | C1210C104J5GACTU | 2 | 2 | TXPLUS_00 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_00`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED00.1（1）；03_UCC_TX/TX00.1（PLUS）。 [完整端点N0253](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0253)。 |

接完确认：C_TX_AC00.1=`TX_AC_SRC00`，C_TX_AC00.2=`TXPLUS_00`；不可旁路该器件把两个网名短在一起。

<a id="array-tx00"></a>

### 第006步：在ARRAY／03_UCC_TX放置 TX00

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX00**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX00 | NU40C10T-2 | 1 | PLUS | TXPLUS_00 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_00`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC00.2（2）；03_UCC_TX/R_TX_BLEED00.1（1）。 [完整端点N0253](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0253)。 |
| ARRAY | 03_UCC_TX | TX00 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX00.2→GND。

<a id="array-r-tx-bleed00"></a>

### 第007步：在ARRAY／03_UCC_TX放置 R_TX_BLEED00

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED00**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX00.1与TX00.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED00 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_00 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_00`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC00.2（2）；03_UCC_TX/TX00.1（PLUS）。 [完整端点N0253](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0253)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED00 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED00.1=`TXPLUS_00`，R_TX_BLEED00.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx01"></a>

### 第008步：在ARRAY／03_UCC_TX放置 R_TX01

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX01**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV00输出与C_TX_AC01之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX01 | CRCW2512150RFKEG | 1 | 1 | TXOUT_01 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_01`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV00.5（OUTB）。 [完整端点N0190](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0190)。 |
| ARRAY | 03_UCC_TX | R_TX01 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC01 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC01`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC01.1（1）。 [完整端点N0318](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0318)。 |

接完确认：R_TX01.1=`TXOUT_01`，R_TX01.2=`TX_AC_SRC01`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac01"></a>

### 第009步：在ARRAY／03_UCC_TX放置 C_TX_AC01

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC01**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX01之后、TX01之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC01 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC01 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC01`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX01.2（2）。 [完整端点N0318](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0318)。 |
| ARRAY | 03_UCC_TX | C_TX_AC01 | C1210C104J5GACTU | 2 | 2 | TXPLUS_01 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_01`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED01.1（1）；03_UCC_TX/TX01.1（PLUS）。 [完整端点N0254](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0254)。 |

接完确认：C_TX_AC01.1=`TX_AC_SRC01`，C_TX_AC01.2=`TXPLUS_01`；不可旁路该器件把两个网名短在一起。

<a id="array-tx01"></a>

### 第010步：在ARRAY／03_UCC_TX放置 TX01

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX01**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX01 | NU40C10T-2 | 1 | PLUS | TXPLUS_01 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_01`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC01.2（2）；03_UCC_TX/R_TX_BLEED01.1（1）。 [完整端点N0254](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0254)。 |
| ARRAY | 03_UCC_TX | TX01 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX01.2→GND。

<a id="array-r-tx-bleed01"></a>

### 第011步：在ARRAY／03_UCC_TX放置 R_TX_BLEED01

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED01**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX01.1与TX01.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED01 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_01 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_01`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC01.2（2）；03_UCC_TX/TX01.1（PLUS）。 [完整端点N0254](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0254)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED01 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED01.1=`TXPLUS_01`，R_TX_BLEED01.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv01"></a>

### 第012步：在ARRAY／03_UCC_TX放置 U_DRV01

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV01**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV01 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.8（ENB）。 |
| ARRAY | 03_UCC_TX | U_DRV01 | UCC27624QDRQ1 | 2 | INA | TXLOG_02 | IN | 从此脚引线，标注精确网名`TXLOG_02`；跨页使用同名板内标签。同网还接：02_595/U_SR00.2（QC）；02_595/R_TX_PD02.1（1）。 [完整端点N0127](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0127)。 |
| ARRAY | 03_UCC_TX | U_DRV01 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV01 | UCC27624QDRQ1 | 4 | INB | TXLOG_03 | IN | 从此脚引线，标注精确网名`TXLOG_03`；跨页使用同名板内标签。同网还接：02_595/U_SR00.3（QD）；02_595/R_TX_PD03.1（1）。 [完整端点N0128](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0128)。 |
| ARRAY | 03_UCC_TX | U_DRV01 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_03 | OUT | 从此脚引线，标注精确网名`TXOUT_03`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX03.1（1）。 [完整端点N0192](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0192)。 |
| ARRAY | 03_UCC_TX | U_DRV01 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV01 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_02 | OUT | 从此脚引线，标注精确网名`TXOUT_02`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX02.1（1）。 [完整端点N0191](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0191)。 |
| ARRAY | 03_UCC_TX | U_DRV01 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV01.3→GND；U_DRV01.6→VTX。

<a id="array-c-u-drv01"></a>

### 第013步：在ARRAY／03_UCC_TX放置 C_U_DRV01

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV01**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV01的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV01 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV01 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV01.1=`VTX`，C_U_DRV01.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx02"></a>

### 第014步：在ARRAY／03_UCC_TX放置 R_TX02

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX02**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV01输出与C_TX_AC02之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX02 | CRCW2512150RFKEG | 1 | 1 | TXOUT_02 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_02`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV01.7（OUTA）。 [完整端点N0191](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0191)。 |
| ARRAY | 03_UCC_TX | R_TX02 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC02 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC02`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC02.1（1）。 [完整端点N0319](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0319)。 |

接完确认：R_TX02.1=`TXOUT_02`，R_TX02.2=`TX_AC_SRC02`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac02"></a>

### 第015步：在ARRAY／03_UCC_TX放置 C_TX_AC02

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC02**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX02之后、TX02之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC02 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC02 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC02`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX02.2（2）。 [完整端点N0319](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0319)。 |
| ARRAY | 03_UCC_TX | C_TX_AC02 | C1210C104J5GACTU | 2 | 2 | TXPLUS_02 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_02`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED02.1（1）；03_UCC_TX/TX02.1（PLUS）。 [完整端点N0255](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0255)。 |

接完确认：C_TX_AC02.1=`TX_AC_SRC02`，C_TX_AC02.2=`TXPLUS_02`；不可旁路该器件把两个网名短在一起。

<a id="array-tx02"></a>

### 第016步：在ARRAY／03_UCC_TX放置 TX02

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX02**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX02 | NU40C10T-2 | 1 | PLUS | TXPLUS_02 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_02`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC02.2（2）；03_UCC_TX/R_TX_BLEED02.1（1）。 [完整端点N0255](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0255)。 |
| ARRAY | 03_UCC_TX | TX02 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX02.2→GND。

<a id="array-r-tx-bleed02"></a>

### 第017步：在ARRAY／03_UCC_TX放置 R_TX_BLEED02

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED02**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX02.1与TX02.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED02 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_02 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_02`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC02.2（2）；03_UCC_TX/TX02.1（PLUS）。 [完整端点N0255](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0255)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED02 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED02.1=`TXPLUS_02`，R_TX_BLEED02.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx03"></a>

### 第018步：在ARRAY／03_UCC_TX放置 R_TX03

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX03**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV01输出与C_TX_AC03之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX03 | CRCW2512150RFKEG | 1 | 1 | TXOUT_03 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_03`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV01.5（OUTB）。 [完整端点N0192](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0192)。 |
| ARRAY | 03_UCC_TX | R_TX03 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC03 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC03`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC03.1（1）。 [完整端点N0320](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0320)。 |

接完确认：R_TX03.1=`TXOUT_03`，R_TX03.2=`TX_AC_SRC03`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac03"></a>

### 第019步：在ARRAY／03_UCC_TX放置 C_TX_AC03

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC03**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX03之后、TX03之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC03 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC03 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC03`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX03.2（2）。 [完整端点N0320](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0320)。 |
| ARRAY | 03_UCC_TX | C_TX_AC03 | C1210C104J5GACTU | 2 | 2 | TXPLUS_03 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_03`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED03.1（1）；03_UCC_TX/TX03.1（PLUS）。 [完整端点N0256](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0256)。 |

接完确认：C_TX_AC03.1=`TX_AC_SRC03`，C_TX_AC03.2=`TXPLUS_03`；不可旁路该器件把两个网名短在一起。

<a id="array-tx03"></a>

### 第020步：在ARRAY／03_UCC_TX放置 TX03

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX03**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX03 | NU40C10T-2 | 1 | PLUS | TXPLUS_03 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_03`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC03.2（2）；03_UCC_TX/R_TX_BLEED03.1（1）。 [完整端点N0256](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0256)。 |
| ARRAY | 03_UCC_TX | TX03 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX03.2→GND。

<a id="array-r-tx-bleed03"></a>

### 第021步：在ARRAY／03_UCC_TX放置 R_TX_BLEED03

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED03**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX03.1与TX03.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED03 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_03 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_03`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC03.2（2）；03_UCC_TX/TX03.1（PLUS）。 [完整端点N0256](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0256)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED03 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED03.1=`TXPLUS_03`，R_TX_BLEED03.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv02"></a>

### 第022步：在ARRAY／03_UCC_TX放置 U_DRV02

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV02**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV02 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV02 | UCC27624QDRQ1 | 2 | INA | TXLOG_04 | IN | 从此脚引线，标注精确网名`TXLOG_04`；跨页使用同名板内标签。同网还接：02_595/U_SR01.15（QA）；02_595/R_TX_PD04.1（1）。 [完整端点N0129](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0129)。 |
| ARRAY | 03_UCC_TX | U_DRV02 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV02 | UCC27624QDRQ1 | 4 | INB | TXLOG_05 | IN | 从此脚引线，标注精确网名`TXLOG_05`；跨页使用同名板内标签。同网还接：02_595/U_SR01.1（QB）；02_595/R_TX_PD05.1（1）。 [完整端点N0130](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0130)。 |
| ARRAY | 03_UCC_TX | U_DRV02 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_05 | OUT | 从此脚引线，标注精确网名`TXOUT_05`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX05.1（1）。 [完整端点N0194](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0194)。 |
| ARRAY | 03_UCC_TX | U_DRV02 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV02 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_04 | OUT | 从此脚引线，标注精确网名`TXOUT_04`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX04.1（1）。 [完整端点N0193](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0193)。 |
| ARRAY | 03_UCC_TX | U_DRV02 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV02.3→GND；U_DRV02.6→VTX。

<a id="array-c-u-drv02"></a>

### 第023步：在ARRAY／03_UCC_TX放置 C_U_DRV02

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV02**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV02的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV02 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV02 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV02.1=`VTX`，C_U_DRV02.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx04"></a>

### 第024步：在ARRAY／03_UCC_TX放置 R_TX04

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX04**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV02输出与C_TX_AC04之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX04 | CRCW2512150RFKEG | 1 | 1 | TXOUT_04 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_04`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV02.7（OUTA）。 [完整端点N0193](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0193)。 |
| ARRAY | 03_UCC_TX | R_TX04 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC04 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC04`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC04.1（1）。 [完整端点N0321](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0321)。 |

接完确认：R_TX04.1=`TXOUT_04`，R_TX04.2=`TX_AC_SRC04`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac04"></a>

### 第025步：在ARRAY／03_UCC_TX放置 C_TX_AC04

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC04**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX04之后、TX04之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC04 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC04 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC04`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX04.2（2）。 [完整端点N0321](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0321)。 |
| ARRAY | 03_UCC_TX | C_TX_AC04 | C1210C104J5GACTU | 2 | 2 | TXPLUS_04 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_04`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED04.1（1）；03_UCC_TX/TX04.1（PLUS）。 [完整端点N0257](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0257)。 |

接完确认：C_TX_AC04.1=`TX_AC_SRC04`，C_TX_AC04.2=`TXPLUS_04`；不可旁路该器件把两个网名短在一起。

<a id="array-tx04"></a>

### 第026步：在ARRAY／03_UCC_TX放置 TX04

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX04**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX04 | NU40C10T-2 | 1 | PLUS | TXPLUS_04 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_04`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC04.2（2）；03_UCC_TX/R_TX_BLEED04.1（1）。 [完整端点N0257](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0257)。 |
| ARRAY | 03_UCC_TX | TX04 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX04.2→GND。

<a id="array-r-tx-bleed04"></a>

### 第027步：在ARRAY／03_UCC_TX放置 R_TX_BLEED04

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED04**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX04.1与TX04.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED04 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_04 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_04`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC04.2（2）；03_UCC_TX/TX04.1（PLUS）。 [完整端点N0257](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0257)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED04 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED04.1=`TXPLUS_04`，R_TX_BLEED04.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx05"></a>

### 第028步：在ARRAY／03_UCC_TX放置 R_TX05

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX05**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV02输出与C_TX_AC05之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX05 | CRCW2512150RFKEG | 1 | 1 | TXOUT_05 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_05`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV02.5（OUTB）。 [完整端点N0194](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0194)。 |
| ARRAY | 03_UCC_TX | R_TX05 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC05 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC05`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC05.1（1）。 [完整端点N0322](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0322)。 |

接完确认：R_TX05.1=`TXOUT_05`，R_TX05.2=`TX_AC_SRC05`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac05"></a>

### 第029步：在ARRAY／03_UCC_TX放置 C_TX_AC05

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC05**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX05之后、TX05之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC05 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC05 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC05`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX05.2（2）。 [完整端点N0322](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0322)。 |
| ARRAY | 03_UCC_TX | C_TX_AC05 | C1210C104J5GACTU | 2 | 2 | TXPLUS_05 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_05`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED05.1（1）；03_UCC_TX/TX05.1（PLUS）。 [完整端点N0258](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0258)。 |

接完确认：C_TX_AC05.1=`TX_AC_SRC05`，C_TX_AC05.2=`TXPLUS_05`；不可旁路该器件把两个网名短在一起。

<a id="array-tx05"></a>

### 第030步：在ARRAY／03_UCC_TX放置 TX05

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX05**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX05 | NU40C10T-2 | 1 | PLUS | TXPLUS_05 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_05`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC05.2（2）；03_UCC_TX/R_TX_BLEED05.1（1）。 [完整端点N0258](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0258)。 |
| ARRAY | 03_UCC_TX | TX05 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX05.2→GND。

<a id="array-r-tx-bleed05"></a>

### 第031步：在ARRAY／03_UCC_TX放置 R_TX_BLEED05

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED05**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX05.1与TX05.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED05 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_05 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_05`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC05.2（2）；03_UCC_TX/TX05.1（PLUS）。 [完整端点N0258](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0258)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED05 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED05.1=`TXPLUS_05`，R_TX_BLEED05.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv03"></a>

### 第032步：在ARRAY／03_UCC_TX放置 U_DRV03

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV03**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV03 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV03 | UCC27624QDRQ1 | 2 | INA | TXLOG_06 | IN | 从此脚引线，标注精确网名`TXLOG_06`；跨页使用同名板内标签。同网还接：02_595/U_SR01.2（QC）；02_595/R_TX_PD06.1（1）。 [完整端点N0131](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0131)。 |
| ARRAY | 03_UCC_TX | U_DRV03 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV03 | UCC27624QDRQ1 | 4 | INB | TXLOG_07 | IN | 从此脚引线，标注精确网名`TXLOG_07`；跨页使用同名板内标签。同网还接：02_595/U_SR01.3（QD）；02_595/R_TX_PD07.1（1）。 [完整端点N0132](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0132)。 |
| ARRAY | 03_UCC_TX | U_DRV03 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_07 | OUT | 从此脚引线，标注精确网名`TXOUT_07`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX07.1（1）。 [完整端点N0196](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0196)。 |
| ARRAY | 03_UCC_TX | U_DRV03 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV03 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_06 | OUT | 从此脚引线，标注精确网名`TXOUT_06`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX06.1（1）。 [完整端点N0195](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0195)。 |
| ARRAY | 03_UCC_TX | U_DRV03 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV03.3→GND；U_DRV03.6→VTX。

<a id="array-c-u-drv03"></a>

### 第033步：在ARRAY／03_UCC_TX放置 C_U_DRV03

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV03**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV03的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV03 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV03 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV03.1=`VTX`，C_U_DRV03.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx06"></a>

### 第034步：在ARRAY／03_UCC_TX放置 R_TX06

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX06**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV03输出与C_TX_AC06之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX06 | CRCW2512150RFKEG | 1 | 1 | TXOUT_06 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_06`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV03.7（OUTA）。 [完整端点N0195](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0195)。 |
| ARRAY | 03_UCC_TX | R_TX06 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC06 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC06`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC06.1（1）。 [完整端点N0323](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0323)。 |

接完确认：R_TX06.1=`TXOUT_06`，R_TX06.2=`TX_AC_SRC06`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac06"></a>

### 第035步：在ARRAY／03_UCC_TX放置 C_TX_AC06

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC06**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX06之后、TX06之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC06 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC06 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC06`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX06.2（2）。 [完整端点N0323](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0323)。 |
| ARRAY | 03_UCC_TX | C_TX_AC06 | C1210C104J5GACTU | 2 | 2 | TXPLUS_06 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_06`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED06.1（1）；03_UCC_TX/TX06.1（PLUS）。 [完整端点N0259](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0259)。 |

接完确认：C_TX_AC06.1=`TX_AC_SRC06`，C_TX_AC06.2=`TXPLUS_06`；不可旁路该器件把两个网名短在一起。

<a id="array-tx06"></a>

### 第036步：在ARRAY／03_UCC_TX放置 TX06

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX06**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX06 | NU40C10T-2 | 1 | PLUS | TXPLUS_06 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_06`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC06.2（2）；03_UCC_TX/R_TX_BLEED06.1（1）。 [完整端点N0259](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0259)。 |
| ARRAY | 03_UCC_TX | TX06 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX06.2→GND。

<a id="array-r-tx-bleed06"></a>

### 第037步：在ARRAY／03_UCC_TX放置 R_TX_BLEED06

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED06**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX06.1与TX06.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED06 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_06 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_06`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC06.2（2）；03_UCC_TX/TX06.1（PLUS）。 [完整端点N0259](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0259)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED06 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED06.1=`TXPLUS_06`，R_TX_BLEED06.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx07"></a>

### 第038步：在ARRAY／03_UCC_TX放置 R_TX07

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX07**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV03输出与C_TX_AC07之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX07 | CRCW2512150RFKEG | 1 | 1 | TXOUT_07 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_07`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV03.5（OUTB）。 [完整端点N0196](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0196)。 |
| ARRAY | 03_UCC_TX | R_TX07 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC07 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC07`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC07.1（1）。 [完整端点N0324](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0324)。 |

接完确认：R_TX07.1=`TXOUT_07`，R_TX07.2=`TX_AC_SRC07`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac07"></a>

### 第039步：在ARRAY／03_UCC_TX放置 C_TX_AC07

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC07**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX07之后、TX07之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC07 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC07 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC07`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX07.2（2）。 [完整端点N0324](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0324)。 |
| ARRAY | 03_UCC_TX | C_TX_AC07 | C1210C104J5GACTU | 2 | 2 | TXPLUS_07 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_07`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED07.1（1）；03_UCC_TX/TX07.1（PLUS）。 [完整端点N0260](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0260)。 |

接完确认：C_TX_AC07.1=`TX_AC_SRC07`，C_TX_AC07.2=`TXPLUS_07`；不可旁路该器件把两个网名短在一起。

<a id="array-tx07"></a>

### 第040步：在ARRAY／03_UCC_TX放置 TX07

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX07**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX07 | NU40C10T-2 | 1 | PLUS | TXPLUS_07 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_07`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC07.2（2）；03_UCC_TX/R_TX_BLEED07.1（1）。 [完整端点N0260](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0260)。 |
| ARRAY | 03_UCC_TX | TX07 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX07.2→GND。

<a id="array-r-tx-bleed07"></a>

### 第041步：在ARRAY／03_UCC_TX放置 R_TX_BLEED07

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED07**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX07.1与TX07.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED07 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_07 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_07`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC07.2（2）；03_UCC_TX/TX07.1（PLUS）。 [完整端点N0260](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0260)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED07 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED07.1=`TXPLUS_07`，R_TX_BLEED07.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv04"></a>

### 第042步：在ARRAY／03_UCC_TX放置 U_DRV04

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV04**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV04 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV04 | UCC27624QDRQ1 | 2 | INA | TXLOG_08 | IN | 从此脚引线，标注精确网名`TXLOG_08`；跨页使用同名板内标签。同网还接：02_595/U_SR02.15（QA）；02_595/R_TX_PD08.1（1）。 [完整端点N0133](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0133)。 |
| ARRAY | 03_UCC_TX | U_DRV04 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV04 | UCC27624QDRQ1 | 4 | INB | TXLOG_09 | IN | 从此脚引线，标注精确网名`TXLOG_09`；跨页使用同名板内标签。同网还接：02_595/U_SR02.1（QB）；02_595/R_TX_PD09.1（1）。 [完整端点N0134](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0134)。 |
| ARRAY | 03_UCC_TX | U_DRV04 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_09 | OUT | 从此脚引线，标注精确网名`TXOUT_09`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX09.1（1）。 [完整端点N0198](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0198)。 |
| ARRAY | 03_UCC_TX | U_DRV04 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV04 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_08 | OUT | 从此脚引线，标注精确网名`TXOUT_08`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX08.1（1）。 [完整端点N0197](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0197)。 |
| ARRAY | 03_UCC_TX | U_DRV04 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV04.3→GND；U_DRV04.6→VTX。

<a id="array-c-u-drv04"></a>

### 第043步：在ARRAY／03_UCC_TX放置 C_U_DRV04

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV04**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV04的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV04 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV04 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV04.1=`VTX`，C_U_DRV04.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx08"></a>

### 第044步：在ARRAY／03_UCC_TX放置 R_TX08

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX08**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV04输出与C_TX_AC08之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX08 | CRCW2512150RFKEG | 1 | 1 | TXOUT_08 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_08`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV04.7（OUTA）。 [完整端点N0197](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0197)。 |
| ARRAY | 03_UCC_TX | R_TX08 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC08 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC08`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC08.1（1）。 [完整端点N0325](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0325)。 |

接完确认：R_TX08.1=`TXOUT_08`，R_TX08.2=`TX_AC_SRC08`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac08"></a>

### 第045步：在ARRAY／03_UCC_TX放置 C_TX_AC08

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC08**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX08之后、TX08之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC08 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC08 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC08`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX08.2（2）。 [完整端点N0325](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0325)。 |
| ARRAY | 03_UCC_TX | C_TX_AC08 | C1210C104J5GACTU | 2 | 2 | TXPLUS_08 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_08`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED08.1（1）；03_UCC_TX/TX08.1（PLUS）。 [完整端点N0261](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0261)。 |

接完确认：C_TX_AC08.1=`TX_AC_SRC08`，C_TX_AC08.2=`TXPLUS_08`；不可旁路该器件把两个网名短在一起。

<a id="array-tx08"></a>

### 第046步：在ARRAY／03_UCC_TX放置 TX08

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX08**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX08 | NU40C10T-2 | 1 | PLUS | TXPLUS_08 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_08`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC08.2（2）；03_UCC_TX/R_TX_BLEED08.1（1）。 [完整端点N0261](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0261)。 |
| ARRAY | 03_UCC_TX | TX08 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX08.2→GND。

<a id="array-r-tx-bleed08"></a>

### 第047步：在ARRAY／03_UCC_TX放置 R_TX_BLEED08

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED08**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX08.1与TX08.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED08 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_08 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_08`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC08.2（2）；03_UCC_TX/TX08.1（PLUS）。 [完整端点N0261](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0261)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED08 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED08.1=`TXPLUS_08`，R_TX_BLEED08.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx09"></a>

### 第048步：在ARRAY／03_UCC_TX放置 R_TX09

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX09**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV04输出与C_TX_AC09之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX09 | CRCW2512150RFKEG | 1 | 1 | TXOUT_09 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_09`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV04.5（OUTB）。 [完整端点N0198](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0198)。 |
| ARRAY | 03_UCC_TX | R_TX09 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC09 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC09`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC09.1（1）。 [完整端点N0326](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0326)。 |

接完确认：R_TX09.1=`TXOUT_09`，R_TX09.2=`TX_AC_SRC09`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac09"></a>

### 第049步：在ARRAY／03_UCC_TX放置 C_TX_AC09

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC09**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX09之后、TX09之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC09 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC09 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC09`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX09.2（2）。 [完整端点N0326](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0326)。 |
| ARRAY | 03_UCC_TX | C_TX_AC09 | C1210C104J5GACTU | 2 | 2 | TXPLUS_09 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_09`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED09.1（1）；03_UCC_TX/TX09.1（PLUS）。 [完整端点N0262](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0262)。 |

接完确认：C_TX_AC09.1=`TX_AC_SRC09`，C_TX_AC09.2=`TXPLUS_09`；不可旁路该器件把两个网名短在一起。

<a id="array-tx09"></a>

### 第050步：在ARRAY／03_UCC_TX放置 TX09

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX09**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX09 | NU40C10T-2 | 1 | PLUS | TXPLUS_09 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_09`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC09.2（2）；03_UCC_TX/R_TX_BLEED09.1（1）。 [完整端点N0262](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0262)。 |
| ARRAY | 03_UCC_TX | TX09 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX09.2→GND。

<a id="array-r-tx-bleed09"></a>

### 第051步：在ARRAY／03_UCC_TX放置 R_TX_BLEED09

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED09**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX09.1与TX09.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED09 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_09 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_09`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC09.2（2）；03_UCC_TX/TX09.1（PLUS）。 [完整端点N0262](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0262)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED09 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED09.1=`TXPLUS_09`，R_TX_BLEED09.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv05"></a>

### 第052步：在ARRAY／03_UCC_TX放置 U_DRV05

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV05**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV05 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV05 | UCC27624QDRQ1 | 2 | INA | TXLOG_10 | IN | 从此脚引线，标注精确网名`TXLOG_10`；跨页使用同名板内标签。同网还接：02_595/U_SR02.2（QC）；02_595/R_TX_PD10.1（1）。 [完整端点N0135](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0135)。 |
| ARRAY | 03_UCC_TX | U_DRV05 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV05 | UCC27624QDRQ1 | 4 | INB | TXLOG_11 | IN | 从此脚引线，标注精确网名`TXLOG_11`；跨页使用同名板内标签。同网还接：02_595/U_SR02.3（QD）；02_595/R_TX_PD11.1（1）。 [完整端点N0136](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0136)。 |
| ARRAY | 03_UCC_TX | U_DRV05 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_11 | OUT | 从此脚引线，标注精确网名`TXOUT_11`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX11.1（1）。 [完整端点N0200](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0200)。 |
| ARRAY | 03_UCC_TX | U_DRV05 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV05 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_10 | OUT | 从此脚引线，标注精确网名`TXOUT_10`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX10.1（1）。 [完整端点N0199](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0199)。 |
| ARRAY | 03_UCC_TX | U_DRV05 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV05.3→GND；U_DRV05.6→VTX。

<a id="array-c-u-drv05"></a>

### 第053步：在ARRAY／03_UCC_TX放置 C_U_DRV05

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV05**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV05的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV05 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV05 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV05.1=`VTX`，C_U_DRV05.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx10"></a>

### 第054步：在ARRAY／03_UCC_TX放置 R_TX10

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX10**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV05输出与C_TX_AC10之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX10 | CRCW2512150RFKEG | 1 | 1 | TXOUT_10 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_10`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV05.7（OUTA）。 [完整端点N0199](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0199)。 |
| ARRAY | 03_UCC_TX | R_TX10 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC10 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC10`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC10.1（1）。 [完整端点N0327](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0327)。 |

接完确认：R_TX10.1=`TXOUT_10`，R_TX10.2=`TX_AC_SRC10`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac10"></a>

### 第055步：在ARRAY／03_UCC_TX放置 C_TX_AC10

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC10**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX10之后、TX10之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC10 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC10 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC10`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX10.2（2）。 [完整端点N0327](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0327)。 |
| ARRAY | 03_UCC_TX | C_TX_AC10 | C1210C104J5GACTU | 2 | 2 | TXPLUS_10 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_10`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED10.1（1）；03_UCC_TX/TX10.1（PLUS）。 [完整端点N0263](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0263)。 |

接完确认：C_TX_AC10.1=`TX_AC_SRC10`，C_TX_AC10.2=`TXPLUS_10`；不可旁路该器件把两个网名短在一起。

<a id="array-tx10"></a>

### 第056步：在ARRAY／03_UCC_TX放置 TX10

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX10**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX10 | NU40C10T-2 | 1 | PLUS | TXPLUS_10 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_10`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC10.2（2）；03_UCC_TX/R_TX_BLEED10.1（1）。 [完整端点N0263](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0263)。 |
| ARRAY | 03_UCC_TX | TX10 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX10.2→GND。

<a id="array-r-tx-bleed10"></a>

### 第057步：在ARRAY／03_UCC_TX放置 R_TX_BLEED10

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED10**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX10.1与TX10.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED10 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_10 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_10`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC10.2（2）；03_UCC_TX/TX10.1（PLUS）。 [完整端点N0263](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0263)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED10 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED10.1=`TXPLUS_10`，R_TX_BLEED10.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx11"></a>

### 第058步：在ARRAY／03_UCC_TX放置 R_TX11

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX11**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV05输出与C_TX_AC11之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX11 | CRCW2512150RFKEG | 1 | 1 | TXOUT_11 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_11`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV05.5（OUTB）。 [完整端点N0200](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0200)。 |
| ARRAY | 03_UCC_TX | R_TX11 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC11 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC11`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC11.1（1）。 [完整端点N0328](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0328)。 |

接完确认：R_TX11.1=`TXOUT_11`，R_TX11.2=`TX_AC_SRC11`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac11"></a>

### 第059步：在ARRAY／03_UCC_TX放置 C_TX_AC11

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC11**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX11之后、TX11之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC11 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC11 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC11`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX11.2（2）。 [完整端点N0328](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0328)。 |
| ARRAY | 03_UCC_TX | C_TX_AC11 | C1210C104J5GACTU | 2 | 2 | TXPLUS_11 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_11`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED11.1（1）；03_UCC_TX/TX11.1（PLUS）。 [完整端点N0264](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0264)。 |

接完确认：C_TX_AC11.1=`TX_AC_SRC11`，C_TX_AC11.2=`TXPLUS_11`；不可旁路该器件把两个网名短在一起。

<a id="array-tx11"></a>

### 第060步：在ARRAY／03_UCC_TX放置 TX11

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX11**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX11 | NU40C10T-2 | 1 | PLUS | TXPLUS_11 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_11`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC11.2（2）；03_UCC_TX/R_TX_BLEED11.1（1）。 [完整端点N0264](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0264)。 |
| ARRAY | 03_UCC_TX | TX11 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX11.2→GND。

<a id="array-r-tx-bleed11"></a>

### 第061步：在ARRAY／03_UCC_TX放置 R_TX_BLEED11

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED11**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX11.1与TX11.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED11 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_11 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_11`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC11.2（2）；03_UCC_TX/TX11.1（PLUS）。 [完整端点N0264](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0264)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED11 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED11.1=`TXPLUS_11`，R_TX_BLEED11.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv06"></a>

### 第062步：在ARRAY／03_UCC_TX放置 U_DRV06

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV06**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV06 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV06 | UCC27624QDRQ1 | 2 | INA | TXLOG_12 | IN | 从此脚引线，标注精确网名`TXLOG_12`；跨页使用同名板内标签。同网还接：02_595/U_SR03.15（QA）；02_595/R_TX_PD12.1（1）。 [完整端点N0137](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0137)。 |
| ARRAY | 03_UCC_TX | U_DRV06 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV06 | UCC27624QDRQ1 | 4 | INB | TXLOG_13 | IN | 从此脚引线，标注精确网名`TXLOG_13`；跨页使用同名板内标签。同网还接：02_595/U_SR03.1（QB）；02_595/R_TX_PD13.1（1）。 [完整端点N0138](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0138)。 |
| ARRAY | 03_UCC_TX | U_DRV06 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_13 | OUT | 从此脚引线，标注精确网名`TXOUT_13`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX13.1（1）。 [完整端点N0202](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0202)。 |
| ARRAY | 03_UCC_TX | U_DRV06 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV06 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_12 | OUT | 从此脚引线，标注精确网名`TXOUT_12`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX12.1（1）。 [完整端点N0201](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0201)。 |
| ARRAY | 03_UCC_TX | U_DRV06 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV06.3→GND；U_DRV06.6→VTX。

<a id="array-c-u-drv06"></a>

### 第063步：在ARRAY／03_UCC_TX放置 C_U_DRV06

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV06**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV06的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV06 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV06 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV06.1=`VTX`，C_U_DRV06.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx12"></a>

### 第064步：在ARRAY／03_UCC_TX放置 R_TX12

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX12**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV06输出与C_TX_AC12之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX12 | CRCW2512150RFKEG | 1 | 1 | TXOUT_12 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_12`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV06.7（OUTA）。 [完整端点N0201](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0201)。 |
| ARRAY | 03_UCC_TX | R_TX12 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC12 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC12`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC12.1（1）。 [完整端点N0329](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0329)。 |

接完确认：R_TX12.1=`TXOUT_12`，R_TX12.2=`TX_AC_SRC12`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac12"></a>

### 第065步：在ARRAY／03_UCC_TX放置 C_TX_AC12

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC12**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX12之后、TX12之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC12 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC12 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC12`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX12.2（2）。 [完整端点N0329](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0329)。 |
| ARRAY | 03_UCC_TX | C_TX_AC12 | C1210C104J5GACTU | 2 | 2 | TXPLUS_12 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_12`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED12.1（1）；03_UCC_TX/TX12.1（PLUS）。 [完整端点N0265](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0265)。 |

接完确认：C_TX_AC12.1=`TX_AC_SRC12`，C_TX_AC12.2=`TXPLUS_12`；不可旁路该器件把两个网名短在一起。

<a id="array-tx12"></a>

### 第066步：在ARRAY／03_UCC_TX放置 TX12

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX12**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX12 | NU40C10T-2 | 1 | PLUS | TXPLUS_12 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_12`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC12.2（2）；03_UCC_TX/R_TX_BLEED12.1（1）。 [完整端点N0265](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0265)。 |
| ARRAY | 03_UCC_TX | TX12 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX12.2→GND。

<a id="array-r-tx-bleed12"></a>

### 第067步：在ARRAY／03_UCC_TX放置 R_TX_BLEED12

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED12**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX12.1与TX12.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED12 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_12 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_12`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC12.2（2）；03_UCC_TX/TX12.1（PLUS）。 [完整端点N0265](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0265)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED12 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED12.1=`TXPLUS_12`，R_TX_BLEED12.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx13"></a>

### 第068步：在ARRAY／03_UCC_TX放置 R_TX13

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX13**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV06输出与C_TX_AC13之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX13 | CRCW2512150RFKEG | 1 | 1 | TXOUT_13 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_13`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV06.5（OUTB）。 [完整端点N0202](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0202)。 |
| ARRAY | 03_UCC_TX | R_TX13 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC13 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC13`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC13.1（1）。 [完整端点N0330](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0330)。 |

接完确认：R_TX13.1=`TXOUT_13`，R_TX13.2=`TX_AC_SRC13`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac13"></a>

### 第069步：在ARRAY／03_UCC_TX放置 C_TX_AC13

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC13**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX13之后、TX13之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC13 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC13 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC13`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX13.2（2）。 [完整端点N0330](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0330)。 |
| ARRAY | 03_UCC_TX | C_TX_AC13 | C1210C104J5GACTU | 2 | 2 | TXPLUS_13 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_13`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED13.1（1）；03_UCC_TX/TX13.1（PLUS）。 [完整端点N0266](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0266)。 |

接完确认：C_TX_AC13.1=`TX_AC_SRC13`，C_TX_AC13.2=`TXPLUS_13`；不可旁路该器件把两个网名短在一起。

<a id="array-tx13"></a>

### 第070步：在ARRAY／03_UCC_TX放置 TX13

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX13**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX13 | NU40C10T-2 | 1 | PLUS | TXPLUS_13 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_13`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC13.2（2）；03_UCC_TX/R_TX_BLEED13.1（1）。 [完整端点N0266](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0266)。 |
| ARRAY | 03_UCC_TX | TX13 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX13.2→GND。

<a id="array-r-tx-bleed13"></a>

### 第071步：在ARRAY／03_UCC_TX放置 R_TX_BLEED13

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED13**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX13.1与TX13.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED13 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_13 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_13`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC13.2（2）；03_UCC_TX/TX13.1（PLUS）。 [完整端点N0266](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0266)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED13 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED13.1=`TXPLUS_13`，R_TX_BLEED13.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv07"></a>

### 第072步：在ARRAY／03_UCC_TX放置 U_DRV07

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV07**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV07 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV07 | UCC27624QDRQ1 | 2 | INA | TXLOG_14 | IN | 从此脚引线，标注精确网名`TXLOG_14`；跨页使用同名板内标签。同网还接：02_595/U_SR03.2（QC）；02_595/R_TX_PD14.1（1）。 [完整端点N0139](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0139)。 |
| ARRAY | 03_UCC_TX | U_DRV07 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV07 | UCC27624QDRQ1 | 4 | INB | TXLOG_15 | IN | 从此脚引线，标注精确网名`TXLOG_15`；跨页使用同名板内标签。同网还接：02_595/U_SR03.3（QD）；02_595/R_TX_PD15.1（1）。 [完整端点N0140](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0140)。 |
| ARRAY | 03_UCC_TX | U_DRV07 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_15 | OUT | 从此脚引线，标注精确网名`TXOUT_15`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX15.1（1）。 [完整端点N0204](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0204)。 |
| ARRAY | 03_UCC_TX | U_DRV07 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV07 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_14 | OUT | 从此脚引线，标注精确网名`TXOUT_14`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX14.1（1）。 [完整端点N0203](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0203)。 |
| ARRAY | 03_UCC_TX | U_DRV07 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV07.3→GND；U_DRV07.6→VTX。

<a id="array-c-u-drv07"></a>

### 第073步：在ARRAY／03_UCC_TX放置 C_U_DRV07

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV07**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV07的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV07 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV07 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV07.1=`VTX`，C_U_DRV07.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx14"></a>

### 第074步：在ARRAY／03_UCC_TX放置 R_TX14

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX14**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV07输出与C_TX_AC14之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX14 | CRCW2512150RFKEG | 1 | 1 | TXOUT_14 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_14`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV07.7（OUTA）。 [完整端点N0203](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0203)。 |
| ARRAY | 03_UCC_TX | R_TX14 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC14 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC14`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC14.1（1）。 [完整端点N0331](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0331)。 |

接完确认：R_TX14.1=`TXOUT_14`，R_TX14.2=`TX_AC_SRC14`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac14"></a>

### 第075步：在ARRAY／03_UCC_TX放置 C_TX_AC14

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC14**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX14之后、TX14之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC14 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC14 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC14`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX14.2（2）。 [完整端点N0331](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0331)。 |
| ARRAY | 03_UCC_TX | C_TX_AC14 | C1210C104J5GACTU | 2 | 2 | TXPLUS_14 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_14`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED14.1（1）；03_UCC_TX/TX14.1（PLUS）。 [完整端点N0267](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0267)。 |

接完确认：C_TX_AC14.1=`TX_AC_SRC14`，C_TX_AC14.2=`TXPLUS_14`；不可旁路该器件把两个网名短在一起。

<a id="array-tx14"></a>

### 第076步：在ARRAY／03_UCC_TX放置 TX14

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX14**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX14 | NU40C10T-2 | 1 | PLUS | TXPLUS_14 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_14`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC14.2（2）；03_UCC_TX/R_TX_BLEED14.1（1）。 [完整端点N0267](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0267)。 |
| ARRAY | 03_UCC_TX | TX14 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX14.2→GND。

<a id="array-r-tx-bleed14"></a>

### 第077步：在ARRAY／03_UCC_TX放置 R_TX_BLEED14

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED14**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX14.1与TX14.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED14 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_14 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_14`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC14.2（2）；03_UCC_TX/TX14.1（PLUS）。 [完整端点N0267](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0267)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED14 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED14.1=`TXPLUS_14`，R_TX_BLEED14.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx15"></a>

### 第078步：在ARRAY／03_UCC_TX放置 R_TX15

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX15**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV07输出与C_TX_AC15之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX15 | CRCW2512150RFKEG | 1 | 1 | TXOUT_15 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_15`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV07.5（OUTB）。 [完整端点N0204](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0204)。 |
| ARRAY | 03_UCC_TX | R_TX15 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC15 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC15`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC15.1（1）。 [完整端点N0332](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0332)。 |

接完确认：R_TX15.1=`TXOUT_15`，R_TX15.2=`TX_AC_SRC15`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac15"></a>

### 第079步：在ARRAY／03_UCC_TX放置 C_TX_AC15

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC15**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX15之后、TX15之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC15 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC15 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC15`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX15.2（2）。 [完整端点N0332](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0332)。 |
| ARRAY | 03_UCC_TX | C_TX_AC15 | C1210C104J5GACTU | 2 | 2 | TXPLUS_15 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_15`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED15.1（1）；03_UCC_TX/TX15.1（PLUS）。 [完整端点N0268](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0268)。 |

接完确认：C_TX_AC15.1=`TX_AC_SRC15`，C_TX_AC15.2=`TXPLUS_15`；不可旁路该器件把两个网名短在一起。

<a id="array-tx15"></a>

### 第080步：在ARRAY／03_UCC_TX放置 TX15

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX15**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX15 | NU40C10T-2 | 1 | PLUS | TXPLUS_15 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_15`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC15.2（2）；03_UCC_TX/R_TX_BLEED15.1（1）。 [完整端点N0268](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0268)。 |
| ARRAY | 03_UCC_TX | TX15 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX15.2→GND。

<a id="array-r-tx-bleed15"></a>

### 第081步：在ARRAY／03_UCC_TX放置 R_TX_BLEED15

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED15**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX15.1与TX15.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED15 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_15 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_15`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC15.2（2）；03_UCC_TX/TX15.1（PLUS）。 [完整端点N0268](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0268)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED15 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED15.1=`TXPLUS_15`，R_TX_BLEED15.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv08"></a>

### 第082步：在ARRAY／03_UCC_TX放置 U_DRV08

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV08**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV08 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV08 | UCC27624QDRQ1 | 2 | INA | TXLOG_16 | IN | 从此脚引线，标注精确网名`TXLOG_16`；跨页使用同名板内标签。同网还接：02_595/U_SR04.15（QA）；02_595/R_TX_PD16.1（1）。 [完整端点N0141](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0141)。 |
| ARRAY | 03_UCC_TX | U_DRV08 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV08 | UCC27624QDRQ1 | 4 | INB | TXLOG_17 | IN | 从此脚引线，标注精确网名`TXLOG_17`；跨页使用同名板内标签。同网还接：02_595/U_SR04.1（QB）；02_595/R_TX_PD17.1（1）。 [完整端点N0142](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0142)。 |
| ARRAY | 03_UCC_TX | U_DRV08 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_17 | OUT | 从此脚引线，标注精确网名`TXOUT_17`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX17.1（1）。 [完整端点N0206](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0206)。 |
| ARRAY | 03_UCC_TX | U_DRV08 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV08 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_16 | OUT | 从此脚引线，标注精确网名`TXOUT_16`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX16.1（1）。 [完整端点N0205](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0205)。 |
| ARRAY | 03_UCC_TX | U_DRV08 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV08.3→GND；U_DRV08.6→VTX。

<a id="array-c-u-drv08"></a>

### 第083步：在ARRAY／03_UCC_TX放置 C_U_DRV08

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV08**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV08的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV08 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV08 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV08.1=`VTX`，C_U_DRV08.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-c-drv-bulk08"></a>

### 第084步：在ARRAY／03_UCC_TX放置 C_DRV_BULK08

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_DRV_BULK08**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_DRV08的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_DRV_BULK08 | C0603C105K3RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_DRV_BULK08 | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_DRV_BULK08.1=`VTX`，C_DRV_BULK08.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx16"></a>

### 第085步：在ARRAY／03_UCC_TX放置 R_TX16

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX16**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV08输出与C_TX_AC16之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX16 | CRCW2512150RFKEG | 1 | 1 | TXOUT_16 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_16`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV08.7（OUTA）。 [完整端点N0205](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0205)。 |
| ARRAY | 03_UCC_TX | R_TX16 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC16 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC16`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC16.1（1）。 [完整端点N0333](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0333)。 |

接完确认：R_TX16.1=`TXOUT_16`，R_TX16.2=`TX_AC_SRC16`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac16"></a>

### 第086步：在ARRAY／03_UCC_TX放置 C_TX_AC16

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC16**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX16之后、TX16之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC16 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC16 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC16`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX16.2（2）。 [完整端点N0333](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0333)。 |
| ARRAY | 03_UCC_TX | C_TX_AC16 | C1210C104J5GACTU | 2 | 2 | TXPLUS_16 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_16`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED16.1（1）；03_UCC_TX/TX16.1（PLUS）。 [完整端点N0269](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0269)。 |

接完确认：C_TX_AC16.1=`TX_AC_SRC16`，C_TX_AC16.2=`TXPLUS_16`；不可旁路该器件把两个网名短在一起。

<a id="array-tx16"></a>

### 第087步：在ARRAY／03_UCC_TX放置 TX16

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX16**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX16 | NU40C10T-2 | 1 | PLUS | TXPLUS_16 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_16`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC16.2（2）；03_UCC_TX/R_TX_BLEED16.1（1）。 [完整端点N0269](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0269)。 |
| ARRAY | 03_UCC_TX | TX16 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX16.2→GND。

<a id="array-r-tx-bleed16"></a>

### 第088步：在ARRAY／03_UCC_TX放置 R_TX_BLEED16

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED16**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX16.1与TX16.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED16 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_16 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_16`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC16.2（2）；03_UCC_TX/TX16.1（PLUS）。 [完整端点N0269](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0269)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED16 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED16.1=`TXPLUS_16`，R_TX_BLEED16.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx17"></a>

### 第089步：在ARRAY／03_UCC_TX放置 R_TX17

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX17**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV08输出与C_TX_AC17之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX17 | CRCW2512150RFKEG | 1 | 1 | TXOUT_17 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_17`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV08.5（OUTB）。 [完整端点N0206](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0206)。 |
| ARRAY | 03_UCC_TX | R_TX17 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC17 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC17`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC17.1（1）。 [完整端点N0334](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0334)。 |

接完确认：R_TX17.1=`TXOUT_17`，R_TX17.2=`TX_AC_SRC17`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac17"></a>

### 第090步：在ARRAY／03_UCC_TX放置 C_TX_AC17

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC17**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX17之后、TX17之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC17 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC17 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC17`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX17.2（2）。 [完整端点N0334](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0334)。 |
| ARRAY | 03_UCC_TX | C_TX_AC17 | C1210C104J5GACTU | 2 | 2 | TXPLUS_17 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_17`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED17.1（1）；03_UCC_TX/TX17.1（PLUS）。 [完整端点N0270](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0270)。 |

接完确认：C_TX_AC17.1=`TX_AC_SRC17`，C_TX_AC17.2=`TXPLUS_17`；不可旁路该器件把两个网名短在一起。

<a id="array-tx17"></a>

### 第091步：在ARRAY／03_UCC_TX放置 TX17

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX17**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX17 | NU40C10T-2 | 1 | PLUS | TXPLUS_17 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_17`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC17.2（2）；03_UCC_TX/R_TX_BLEED17.1（1）。 [完整端点N0270](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0270)。 |
| ARRAY | 03_UCC_TX | TX17 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX17.2→GND。

<a id="array-r-tx-bleed17"></a>

### 第092步：在ARRAY／03_UCC_TX放置 R_TX_BLEED17

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED17**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX17.1与TX17.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED17 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_17 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_17`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC17.2（2）；03_UCC_TX/TX17.1（PLUS）。 [完整端点N0270](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0270)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED17 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED17.1=`TXPLUS_17`，R_TX_BLEED17.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv09"></a>

### 第093步：在ARRAY／03_UCC_TX放置 U_DRV09

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV09**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV09 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV09 | UCC27624QDRQ1 | 2 | INA | TXLOG_18 | IN | 从此脚引线，标注精确网名`TXLOG_18`；跨页使用同名板内标签。同网还接：02_595/U_SR04.2（QC）；02_595/R_TX_PD18.1（1）。 [完整端点N0143](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0143)。 |
| ARRAY | 03_UCC_TX | U_DRV09 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV09 | UCC27624QDRQ1 | 4 | INB | TXLOG_19 | IN | 从此脚引线，标注精确网名`TXLOG_19`；跨页使用同名板内标签。同网还接：02_595/U_SR04.3（QD）；02_595/R_TX_PD19.1（1）。 [完整端点N0144](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0144)。 |
| ARRAY | 03_UCC_TX | U_DRV09 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_19 | OUT | 从此脚引线，标注精确网名`TXOUT_19`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX19.1（1）。 [完整端点N0208](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0208)。 |
| ARRAY | 03_UCC_TX | U_DRV09 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV09 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_18 | OUT | 从此脚引线，标注精确网名`TXOUT_18`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX18.1（1）。 [完整端点N0207](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0207)。 |
| ARRAY | 03_UCC_TX | U_DRV09 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV09.3→GND；U_DRV09.6→VTX。

<a id="array-c-u-drv09"></a>

### 第094步：在ARRAY／03_UCC_TX放置 C_U_DRV09

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV09**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV09的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV09 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV09 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV09.1=`VTX`，C_U_DRV09.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx18"></a>

### 第095步：在ARRAY／03_UCC_TX放置 R_TX18

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX18**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV09输出与C_TX_AC18之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX18 | CRCW2512150RFKEG | 1 | 1 | TXOUT_18 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_18`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV09.7（OUTA）。 [完整端点N0207](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0207)。 |
| ARRAY | 03_UCC_TX | R_TX18 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC18 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC18`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC18.1（1）。 [完整端点N0335](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0335)。 |

接完确认：R_TX18.1=`TXOUT_18`，R_TX18.2=`TX_AC_SRC18`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac18"></a>

### 第096步：在ARRAY／03_UCC_TX放置 C_TX_AC18

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC18**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX18之后、TX18之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC18 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC18 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC18`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX18.2（2）。 [完整端点N0335](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0335)。 |
| ARRAY | 03_UCC_TX | C_TX_AC18 | C1210C104J5GACTU | 2 | 2 | TXPLUS_18 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_18`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED18.1（1）；03_UCC_TX/TX18.1（PLUS）。 [完整端点N0271](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0271)。 |

接完确认：C_TX_AC18.1=`TX_AC_SRC18`，C_TX_AC18.2=`TXPLUS_18`；不可旁路该器件把两个网名短在一起。

<a id="array-tx18"></a>

### 第097步：在ARRAY／03_UCC_TX放置 TX18

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX18**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX18 | NU40C10T-2 | 1 | PLUS | TXPLUS_18 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_18`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC18.2（2）；03_UCC_TX/R_TX_BLEED18.1（1）。 [完整端点N0271](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0271)。 |
| ARRAY | 03_UCC_TX | TX18 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX18.2→GND。

<a id="array-r-tx-bleed18"></a>

### 第098步：在ARRAY／03_UCC_TX放置 R_TX_BLEED18

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED18**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX18.1与TX18.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED18 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_18 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_18`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC18.2（2）；03_UCC_TX/TX18.1（PLUS）。 [完整端点N0271](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0271)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED18 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED18.1=`TXPLUS_18`，R_TX_BLEED18.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx19"></a>

### 第099步：在ARRAY／03_UCC_TX放置 R_TX19

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX19**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV09输出与C_TX_AC19之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX19 | CRCW2512150RFKEG | 1 | 1 | TXOUT_19 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_19`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV09.5（OUTB）。 [完整端点N0208](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0208)。 |
| ARRAY | 03_UCC_TX | R_TX19 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC19 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC19`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC19.1（1）。 [完整端点N0336](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0336)。 |

接完确认：R_TX19.1=`TXOUT_19`，R_TX19.2=`TX_AC_SRC19`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac19"></a>

### 第100步：在ARRAY／03_UCC_TX放置 C_TX_AC19

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC19**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX19之后、TX19之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC19 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC19 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC19`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX19.2（2）。 [完整端点N0336](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0336)。 |
| ARRAY | 03_UCC_TX | C_TX_AC19 | C1210C104J5GACTU | 2 | 2 | TXPLUS_19 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_19`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED19.1（1）；03_UCC_TX/TX19.1（PLUS）。 [完整端点N0272](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0272)。 |

接完确认：C_TX_AC19.1=`TX_AC_SRC19`，C_TX_AC19.2=`TXPLUS_19`；不可旁路该器件把两个网名短在一起。

<a id="array-tx19"></a>

### 第101步：在ARRAY／03_UCC_TX放置 TX19

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX19**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX19 | NU40C10T-2 | 1 | PLUS | TXPLUS_19 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_19`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC19.2（2）；03_UCC_TX/R_TX_BLEED19.1（1）。 [完整端点N0272](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0272)。 |
| ARRAY | 03_UCC_TX | TX19 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX19.2→GND。

<a id="array-r-tx-bleed19"></a>

### 第102步：在ARRAY／03_UCC_TX放置 R_TX_BLEED19

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED19**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX19.1与TX19.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED19 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_19 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_19`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC19.2（2）；03_UCC_TX/TX19.1（PLUS）。 [完整端点N0272](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0272)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED19 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED19.1=`TXPLUS_19`，R_TX_BLEED19.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv10"></a>

### 第103步：在ARRAY／03_UCC_TX放置 U_DRV10

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV10**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV10 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV10 | UCC27624QDRQ1 | 2 | INA | TXLOG_20 | IN | 从此脚引线，标注精确网名`TXLOG_20`；跨页使用同名板内标签。同网还接：02_595/U_SR05.15（QA）；02_595/R_TX_PD20.1（1）。 [完整端点N0145](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0145)。 |
| ARRAY | 03_UCC_TX | U_DRV10 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV10 | UCC27624QDRQ1 | 4 | INB | TXLOG_21 | IN | 从此脚引线，标注精确网名`TXLOG_21`；跨页使用同名板内标签。同网还接：02_595/U_SR05.1（QB）；02_595/R_TX_PD21.1（1）。 [完整端点N0146](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0146)。 |
| ARRAY | 03_UCC_TX | U_DRV10 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_21 | OUT | 从此脚引线，标注精确网名`TXOUT_21`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX21.1（1）。 [完整端点N0210](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0210)。 |
| ARRAY | 03_UCC_TX | U_DRV10 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV10 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_20 | OUT | 从此脚引线，标注精确网名`TXOUT_20`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX20.1（1）。 [完整端点N0209](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0209)。 |
| ARRAY | 03_UCC_TX | U_DRV10 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV10.3→GND；U_DRV10.6→VTX。

<a id="array-c-u-drv10"></a>

### 第104步：在ARRAY／03_UCC_TX放置 C_U_DRV10

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV10**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV10的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV10 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV10 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV10.1=`VTX`，C_U_DRV10.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx20"></a>

### 第105步：在ARRAY／03_UCC_TX放置 R_TX20

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX20**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV10输出与C_TX_AC20之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX20 | CRCW2512150RFKEG | 1 | 1 | TXOUT_20 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_20`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV10.7（OUTA）。 [完整端点N0209](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0209)。 |
| ARRAY | 03_UCC_TX | R_TX20 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC20 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC20`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC20.1（1）。 [完整端点N0337](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0337)。 |

接完确认：R_TX20.1=`TXOUT_20`，R_TX20.2=`TX_AC_SRC20`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac20"></a>

### 第106步：在ARRAY／03_UCC_TX放置 C_TX_AC20

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC20**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX20之后、TX20之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC20 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC20 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC20`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX20.2（2）。 [完整端点N0337](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0337)。 |
| ARRAY | 03_UCC_TX | C_TX_AC20 | C1210C104J5GACTU | 2 | 2 | TXPLUS_20 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_20`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED20.1（1）；03_UCC_TX/TX20.1（PLUS）。 [完整端点N0273](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0273)。 |

接完确认：C_TX_AC20.1=`TX_AC_SRC20`，C_TX_AC20.2=`TXPLUS_20`；不可旁路该器件把两个网名短在一起。

<a id="array-tx20"></a>

### 第107步：在ARRAY／03_UCC_TX放置 TX20

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX20**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX20 | NU40C10T-2 | 1 | PLUS | TXPLUS_20 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_20`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC20.2（2）；03_UCC_TX/R_TX_BLEED20.1（1）。 [完整端点N0273](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0273)。 |
| ARRAY | 03_UCC_TX | TX20 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX20.2→GND。

<a id="array-r-tx-bleed20"></a>

### 第108步：在ARRAY／03_UCC_TX放置 R_TX_BLEED20

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED20**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX20.1与TX20.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED20 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_20 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_20`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC20.2（2）；03_UCC_TX/TX20.1（PLUS）。 [完整端点N0273](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0273)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED20 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED20.1=`TXPLUS_20`，R_TX_BLEED20.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx21"></a>

### 第109步：在ARRAY／03_UCC_TX放置 R_TX21

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX21**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV10输出与C_TX_AC21之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX21 | CRCW2512150RFKEG | 1 | 1 | TXOUT_21 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_21`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV10.5（OUTB）。 [完整端点N0210](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0210)。 |
| ARRAY | 03_UCC_TX | R_TX21 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC21 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC21`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC21.1（1）。 [完整端点N0338](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0338)。 |

接完确认：R_TX21.1=`TXOUT_21`，R_TX21.2=`TX_AC_SRC21`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac21"></a>

### 第110步：在ARRAY／03_UCC_TX放置 C_TX_AC21

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC21**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX21之后、TX21之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC21 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC21 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC21`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX21.2（2）。 [完整端点N0338](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0338)。 |
| ARRAY | 03_UCC_TX | C_TX_AC21 | C1210C104J5GACTU | 2 | 2 | TXPLUS_21 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_21`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED21.1（1）；03_UCC_TX/TX21.1（PLUS）。 [完整端点N0274](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0274)。 |

接完确认：C_TX_AC21.1=`TX_AC_SRC21`，C_TX_AC21.2=`TXPLUS_21`；不可旁路该器件把两个网名短在一起。

<a id="array-tx21"></a>

### 第111步：在ARRAY／03_UCC_TX放置 TX21

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX21**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX21 | NU40C10T-2 | 1 | PLUS | TXPLUS_21 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_21`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC21.2（2）；03_UCC_TX/R_TX_BLEED21.1（1）。 [完整端点N0274](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0274)。 |
| ARRAY | 03_UCC_TX | TX21 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX21.2→GND。

<a id="array-r-tx-bleed21"></a>

### 第112步：在ARRAY／03_UCC_TX放置 R_TX_BLEED21

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED21**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX21.1与TX21.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED21 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_21 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_21`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC21.2（2）；03_UCC_TX/TX21.1（PLUS）。 [完整端点N0274](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0274)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED21 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED21.1=`TXPLUS_21`，R_TX_BLEED21.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv11"></a>

### 第113步：在ARRAY／03_UCC_TX放置 U_DRV11

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV11**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV11 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV11 | UCC27624QDRQ1 | 2 | INA | TXLOG_22 | IN | 从此脚引线，标注精确网名`TXLOG_22`；跨页使用同名板内标签。同网还接：02_595/U_SR05.2（QC）；02_595/R_TX_PD22.1（1）。 [完整端点N0147](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0147)。 |
| ARRAY | 03_UCC_TX | U_DRV11 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV11 | UCC27624QDRQ1 | 4 | INB | TXLOG_23 | IN | 从此脚引线，标注精确网名`TXLOG_23`；跨页使用同名板内标签。同网还接：02_595/U_SR05.3（QD）；02_595/R_TX_PD23.1（1）。 [完整端点N0148](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0148)。 |
| ARRAY | 03_UCC_TX | U_DRV11 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_23 | OUT | 从此脚引线，标注精确网名`TXOUT_23`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX23.1（1）。 [完整端点N0212](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0212)。 |
| ARRAY | 03_UCC_TX | U_DRV11 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV11 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_22 | OUT | 从此脚引线，标注精确网名`TXOUT_22`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX22.1（1）。 [完整端点N0211](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0211)。 |
| ARRAY | 03_UCC_TX | U_DRV11 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV11.3→GND；U_DRV11.6→VTX。

<a id="array-c-u-drv11"></a>

### 第114步：在ARRAY／03_UCC_TX放置 C_U_DRV11

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV11**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV11的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV11 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV11 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV11.1=`VTX`，C_U_DRV11.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx22"></a>

### 第115步：在ARRAY／03_UCC_TX放置 R_TX22

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX22**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV11输出与C_TX_AC22之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX22 | CRCW2512150RFKEG | 1 | 1 | TXOUT_22 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_22`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV11.7（OUTA）。 [完整端点N0211](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0211)。 |
| ARRAY | 03_UCC_TX | R_TX22 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC22 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC22`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC22.1（1）。 [完整端点N0339](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0339)。 |

接完确认：R_TX22.1=`TXOUT_22`，R_TX22.2=`TX_AC_SRC22`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac22"></a>

### 第116步：在ARRAY／03_UCC_TX放置 C_TX_AC22

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC22**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX22之后、TX22之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC22 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC22 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC22`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX22.2（2）。 [完整端点N0339](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0339)。 |
| ARRAY | 03_UCC_TX | C_TX_AC22 | C1210C104J5GACTU | 2 | 2 | TXPLUS_22 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_22`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED22.1（1）；03_UCC_TX/TX22.1（PLUS）。 [完整端点N0275](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0275)。 |

接完确认：C_TX_AC22.1=`TX_AC_SRC22`，C_TX_AC22.2=`TXPLUS_22`；不可旁路该器件把两个网名短在一起。

<a id="array-tx22"></a>

### 第117步：在ARRAY／03_UCC_TX放置 TX22

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX22**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX22 | NU40C10T-2 | 1 | PLUS | TXPLUS_22 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_22`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC22.2（2）；03_UCC_TX/R_TX_BLEED22.1（1）。 [完整端点N0275](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0275)。 |
| ARRAY | 03_UCC_TX | TX22 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX22.2→GND。

<a id="array-r-tx-bleed22"></a>

### 第118步：在ARRAY／03_UCC_TX放置 R_TX_BLEED22

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED22**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX22.1与TX22.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED22 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_22 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_22`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC22.2（2）；03_UCC_TX/TX22.1（PLUS）。 [完整端点N0275](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0275)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED22 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED22.1=`TXPLUS_22`，R_TX_BLEED22.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx23"></a>

### 第119步：在ARRAY／03_UCC_TX放置 R_TX23

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX23**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV11输出与C_TX_AC23之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX23 | CRCW2512150RFKEG | 1 | 1 | TXOUT_23 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_23`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV11.5（OUTB）。 [完整端点N0212](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0212)。 |
| ARRAY | 03_UCC_TX | R_TX23 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC23 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC23`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC23.1（1）。 [完整端点N0340](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0340)。 |

接完确认：R_TX23.1=`TXOUT_23`，R_TX23.2=`TX_AC_SRC23`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac23"></a>

### 第120步：在ARRAY／03_UCC_TX放置 C_TX_AC23

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC23**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX23之后、TX23之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC23 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC23 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC23`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX23.2（2）。 [完整端点N0340](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0340)。 |
| ARRAY | 03_UCC_TX | C_TX_AC23 | C1210C104J5GACTU | 2 | 2 | TXPLUS_23 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_23`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED23.1（1）；03_UCC_TX/TX23.1（PLUS）。 [完整端点N0276](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0276)。 |

接完确认：C_TX_AC23.1=`TX_AC_SRC23`，C_TX_AC23.2=`TXPLUS_23`；不可旁路该器件把两个网名短在一起。

<a id="array-tx23"></a>

### 第121步：在ARRAY／03_UCC_TX放置 TX23

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX23**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX23 | NU40C10T-2 | 1 | PLUS | TXPLUS_23 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_23`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC23.2（2）；03_UCC_TX/R_TX_BLEED23.1（1）。 [完整端点N0276](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0276)。 |
| ARRAY | 03_UCC_TX | TX23 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX23.2→GND。

<a id="array-r-tx-bleed23"></a>

### 第122步：在ARRAY／03_UCC_TX放置 R_TX_BLEED23

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED23**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX23.1与TX23.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED23 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_23 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_23`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC23.2（2）；03_UCC_TX/TX23.1（PLUS）。 [完整端点N0276](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0276)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED23 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED23.1=`TXPLUS_23`，R_TX_BLEED23.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv12"></a>

### 第123步：在ARRAY／03_UCC_TX放置 U_DRV12

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV12**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV12 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV12 | UCC27624QDRQ1 | 2 | INA | TXLOG_24 | IN | 从此脚引线，标注精确网名`TXLOG_24`；跨页使用同名板内标签。同网还接：02_595/U_SR06.15（QA）；02_595/R_TX_PD24.1（1）。 [完整端点N0149](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0149)。 |
| ARRAY | 03_UCC_TX | U_DRV12 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV12 | UCC27624QDRQ1 | 4 | INB | TXLOG_25 | IN | 从此脚引线，标注精确网名`TXLOG_25`；跨页使用同名板内标签。同网还接：02_595/U_SR06.1（QB）；02_595/R_TX_PD25.1（1）。 [完整端点N0150](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0150)。 |
| ARRAY | 03_UCC_TX | U_DRV12 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_25 | OUT | 从此脚引线，标注精确网名`TXOUT_25`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX25.1（1）。 [完整端点N0214](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0214)。 |
| ARRAY | 03_UCC_TX | U_DRV12 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV12 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_24 | OUT | 从此脚引线，标注精确网名`TXOUT_24`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX24.1（1）。 [完整端点N0213](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0213)。 |
| ARRAY | 03_UCC_TX | U_DRV12 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV12.3→GND；U_DRV12.6→VTX。

<a id="array-c-u-drv12"></a>

### 第124步：在ARRAY／03_UCC_TX放置 C_U_DRV12

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV12**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV12的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV12 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV12 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV12.1=`VTX`，C_U_DRV12.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx24"></a>

### 第125步：在ARRAY／03_UCC_TX放置 R_TX24

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX24**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV12输出与C_TX_AC24之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX24 | CRCW2512150RFKEG | 1 | 1 | TXOUT_24 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_24`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV12.7（OUTA）。 [完整端点N0213](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0213)。 |
| ARRAY | 03_UCC_TX | R_TX24 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC24 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC24`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC24.1（1）。 [完整端点N0341](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0341)。 |

接完确认：R_TX24.1=`TXOUT_24`，R_TX24.2=`TX_AC_SRC24`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac24"></a>

### 第126步：在ARRAY／03_UCC_TX放置 C_TX_AC24

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC24**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX24之后、TX24之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC24 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC24 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC24`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX24.2（2）。 [完整端点N0341](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0341)。 |
| ARRAY | 03_UCC_TX | C_TX_AC24 | C1210C104J5GACTU | 2 | 2 | TXPLUS_24 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_24`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED24.1（1）；03_UCC_TX/TX24.1（PLUS）。 [完整端点N0277](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0277)。 |

接完确认：C_TX_AC24.1=`TX_AC_SRC24`，C_TX_AC24.2=`TXPLUS_24`；不可旁路该器件把两个网名短在一起。

<a id="array-tx24"></a>

### 第127步：在ARRAY／03_UCC_TX放置 TX24

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX24**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX24 | NU40C10T-2 | 1 | PLUS | TXPLUS_24 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_24`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC24.2（2）；03_UCC_TX/R_TX_BLEED24.1（1）。 [完整端点N0277](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0277)。 |
| ARRAY | 03_UCC_TX | TX24 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX24.2→GND。

<a id="array-r-tx-bleed24"></a>

### 第128步：在ARRAY／03_UCC_TX放置 R_TX_BLEED24

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED24**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX24.1与TX24.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED24 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_24 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_24`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC24.2（2）；03_UCC_TX/TX24.1（PLUS）。 [完整端点N0277](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0277)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED24 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED24.1=`TXPLUS_24`，R_TX_BLEED24.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx25"></a>

### 第129步：在ARRAY／03_UCC_TX放置 R_TX25

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX25**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV12输出与C_TX_AC25之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX25 | CRCW2512150RFKEG | 1 | 1 | TXOUT_25 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_25`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV12.5（OUTB）。 [完整端点N0214](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0214)。 |
| ARRAY | 03_UCC_TX | R_TX25 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC25 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC25`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC25.1（1）。 [完整端点N0342](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0342)。 |

接完确认：R_TX25.1=`TXOUT_25`，R_TX25.2=`TX_AC_SRC25`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac25"></a>

### 第130步：在ARRAY／03_UCC_TX放置 C_TX_AC25

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC25**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX25之后、TX25之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC25 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC25 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC25`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX25.2（2）。 [完整端点N0342](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0342)。 |
| ARRAY | 03_UCC_TX | C_TX_AC25 | C1210C104J5GACTU | 2 | 2 | TXPLUS_25 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_25`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED25.1（1）；03_UCC_TX/TX25.1（PLUS）。 [完整端点N0278](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0278)。 |

接完确认：C_TX_AC25.1=`TX_AC_SRC25`，C_TX_AC25.2=`TXPLUS_25`；不可旁路该器件把两个网名短在一起。

<a id="array-tx25"></a>

### 第131步：在ARRAY／03_UCC_TX放置 TX25

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX25**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX25 | NU40C10T-2 | 1 | PLUS | TXPLUS_25 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_25`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC25.2（2）；03_UCC_TX/R_TX_BLEED25.1（1）。 [完整端点N0278](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0278)。 |
| ARRAY | 03_UCC_TX | TX25 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX25.2→GND。

<a id="array-r-tx-bleed25"></a>

### 第132步：在ARRAY／03_UCC_TX放置 R_TX_BLEED25

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED25**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX25.1与TX25.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED25 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_25 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_25`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC25.2（2）；03_UCC_TX/TX25.1（PLUS）。 [完整端点N0278](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0278)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED25 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED25.1=`TXPLUS_25`，R_TX_BLEED25.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv13"></a>

### 第133步：在ARRAY／03_UCC_TX放置 U_DRV13

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV13**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV13 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV13 | UCC27624QDRQ1 | 2 | INA | TXLOG_26 | IN | 从此脚引线，标注精确网名`TXLOG_26`；跨页使用同名板内标签。同网还接：02_595/U_SR06.2（QC）；02_595/R_TX_PD26.1（1）。 [完整端点N0151](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0151)。 |
| ARRAY | 03_UCC_TX | U_DRV13 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV13 | UCC27624QDRQ1 | 4 | INB | TXLOG_27 | IN | 从此脚引线，标注精确网名`TXLOG_27`；跨页使用同名板内标签。同网还接：02_595/U_SR06.3（QD）；02_595/R_TX_PD27.1（1）。 [完整端点N0152](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0152)。 |
| ARRAY | 03_UCC_TX | U_DRV13 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_27 | OUT | 从此脚引线，标注精确网名`TXOUT_27`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX27.1（1）。 [完整端点N0216](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0216)。 |
| ARRAY | 03_UCC_TX | U_DRV13 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV13 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_26 | OUT | 从此脚引线，标注精确网名`TXOUT_26`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX26.1（1）。 [完整端点N0215](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0215)。 |
| ARRAY | 03_UCC_TX | U_DRV13 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV13.3→GND；U_DRV13.6→VTX。

<a id="array-c-u-drv13"></a>

### 第134步：在ARRAY／03_UCC_TX放置 C_U_DRV13

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV13**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV13的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV13 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV13 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV13.1=`VTX`，C_U_DRV13.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx26"></a>

### 第135步：在ARRAY／03_UCC_TX放置 R_TX26

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX26**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV13输出与C_TX_AC26之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX26 | CRCW2512150RFKEG | 1 | 1 | TXOUT_26 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_26`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV13.7（OUTA）。 [完整端点N0215](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0215)。 |
| ARRAY | 03_UCC_TX | R_TX26 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC26 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC26`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC26.1（1）。 [完整端点N0343](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0343)。 |

接完确认：R_TX26.1=`TXOUT_26`，R_TX26.2=`TX_AC_SRC26`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac26"></a>

### 第136步：在ARRAY／03_UCC_TX放置 C_TX_AC26

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC26**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX26之后、TX26之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC26 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC26 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC26`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX26.2（2）。 [完整端点N0343](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0343)。 |
| ARRAY | 03_UCC_TX | C_TX_AC26 | C1210C104J5GACTU | 2 | 2 | TXPLUS_26 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_26`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED26.1（1）；03_UCC_TX/TX26.1（PLUS）。 [完整端点N0279](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0279)。 |

接完确认：C_TX_AC26.1=`TX_AC_SRC26`，C_TX_AC26.2=`TXPLUS_26`；不可旁路该器件把两个网名短在一起。

<a id="array-tx26"></a>

### 第137步：在ARRAY／03_UCC_TX放置 TX26

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX26**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX26 | NU40C10T-2 | 1 | PLUS | TXPLUS_26 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_26`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC26.2（2）；03_UCC_TX/R_TX_BLEED26.1（1）。 [完整端点N0279](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0279)。 |
| ARRAY | 03_UCC_TX | TX26 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX26.2→GND。

<a id="array-r-tx-bleed26"></a>

### 第138步：在ARRAY／03_UCC_TX放置 R_TX_BLEED26

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED26**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX26.1与TX26.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED26 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_26 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_26`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC26.2（2）；03_UCC_TX/TX26.1（PLUS）。 [完整端点N0279](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0279)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED26 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED26.1=`TXPLUS_26`，R_TX_BLEED26.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx27"></a>

### 第139步：在ARRAY／03_UCC_TX放置 R_TX27

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX27**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV13输出与C_TX_AC27之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX27 | CRCW2512150RFKEG | 1 | 1 | TXOUT_27 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_27`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV13.5（OUTB）。 [完整端点N0216](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0216)。 |
| ARRAY | 03_UCC_TX | R_TX27 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC27 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC27`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC27.1（1）。 [完整端点N0344](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0344)。 |

接完确认：R_TX27.1=`TXOUT_27`，R_TX27.2=`TX_AC_SRC27`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac27"></a>

### 第140步：在ARRAY／03_UCC_TX放置 C_TX_AC27

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC27**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX27之后、TX27之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC27 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC27 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC27`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX27.2（2）。 [完整端点N0344](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0344)。 |
| ARRAY | 03_UCC_TX | C_TX_AC27 | C1210C104J5GACTU | 2 | 2 | TXPLUS_27 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_27`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED27.1（1）；03_UCC_TX/TX27.1（PLUS）。 [完整端点N0280](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0280)。 |

接完确认：C_TX_AC27.1=`TX_AC_SRC27`，C_TX_AC27.2=`TXPLUS_27`；不可旁路该器件把两个网名短在一起。

<a id="array-tx27"></a>

### 第141步：在ARRAY／03_UCC_TX放置 TX27

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX27**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX27 | NU40C10T-2 | 1 | PLUS | TXPLUS_27 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_27`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC27.2（2）；03_UCC_TX/R_TX_BLEED27.1（1）。 [完整端点N0280](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0280)。 |
| ARRAY | 03_UCC_TX | TX27 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX27.2→GND。

<a id="array-r-tx-bleed27"></a>

### 第142步：在ARRAY／03_UCC_TX放置 R_TX_BLEED27

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED27**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX27.1与TX27.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED27 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_27 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_27`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC27.2（2）；03_UCC_TX/TX27.1（PLUS）。 [完整端点N0280](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0280)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED27 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED27.1=`TXPLUS_27`，R_TX_BLEED27.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv14"></a>

### 第143步：在ARRAY／03_UCC_TX放置 U_DRV14

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV14**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV14 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV14 | UCC27624QDRQ1 | 2 | INA | TXLOG_28 | IN | 从此脚引线，标注精确网名`TXLOG_28`；跨页使用同名板内标签。同网还接：02_595/U_SR07.15（QA）；02_595/R_TX_PD28.1（1）。 [完整端点N0153](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0153)。 |
| ARRAY | 03_UCC_TX | U_DRV14 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV14 | UCC27624QDRQ1 | 4 | INB | TXLOG_29 | IN | 从此脚引线，标注精确网名`TXLOG_29`；跨页使用同名板内标签。同网还接：02_595/U_SR07.1（QB）；02_595/R_TX_PD29.1（1）。 [完整端点N0154](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0154)。 |
| ARRAY | 03_UCC_TX | U_DRV14 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_29 | OUT | 从此脚引线，标注精确网名`TXOUT_29`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX29.1（1）。 [完整端点N0218](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0218)。 |
| ARRAY | 03_UCC_TX | U_DRV14 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV14 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_28 | OUT | 从此脚引线，标注精确网名`TXOUT_28`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX28.1（1）。 [完整端点N0217](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0217)。 |
| ARRAY | 03_UCC_TX | U_DRV14 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV14.3→GND；U_DRV14.6→VTX。

<a id="array-c-u-drv14"></a>

### 第144步：在ARRAY／03_UCC_TX放置 C_U_DRV14

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV14**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV14的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV14 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV14 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV14.1=`VTX`，C_U_DRV14.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx28"></a>

### 第145步：在ARRAY／03_UCC_TX放置 R_TX28

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX28**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV14输出与C_TX_AC28之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX28 | CRCW2512150RFKEG | 1 | 1 | TXOUT_28 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_28`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV14.7（OUTA）。 [完整端点N0217](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0217)。 |
| ARRAY | 03_UCC_TX | R_TX28 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC28 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC28`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC28.1（1）。 [完整端点N0345](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0345)。 |

接完确认：R_TX28.1=`TXOUT_28`，R_TX28.2=`TX_AC_SRC28`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac28"></a>

### 第146步：在ARRAY／03_UCC_TX放置 C_TX_AC28

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC28**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX28之后、TX28之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC28 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC28 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC28`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX28.2（2）。 [完整端点N0345](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0345)。 |
| ARRAY | 03_UCC_TX | C_TX_AC28 | C1210C104J5GACTU | 2 | 2 | TXPLUS_28 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_28`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED28.1（1）；03_UCC_TX/TX28.1（PLUS）。 [完整端点N0281](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0281)。 |

接完确认：C_TX_AC28.1=`TX_AC_SRC28`，C_TX_AC28.2=`TXPLUS_28`；不可旁路该器件把两个网名短在一起。

<a id="array-tx28"></a>

### 第147步：在ARRAY／03_UCC_TX放置 TX28

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX28**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX28 | NU40C10T-2 | 1 | PLUS | TXPLUS_28 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_28`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC28.2（2）；03_UCC_TX/R_TX_BLEED28.1（1）。 [完整端点N0281](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0281)。 |
| ARRAY | 03_UCC_TX | TX28 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX28.2→GND。

<a id="array-r-tx-bleed28"></a>

### 第148步：在ARRAY／03_UCC_TX放置 R_TX_BLEED28

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED28**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX28.1与TX28.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED28 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_28 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_28`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC28.2（2）；03_UCC_TX/TX28.1（PLUS）。 [完整端点N0281](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0281)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED28 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED28.1=`TXPLUS_28`，R_TX_BLEED28.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx29"></a>

### 第149步：在ARRAY／03_UCC_TX放置 R_TX29

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX29**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV14输出与C_TX_AC29之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX29 | CRCW2512150RFKEG | 1 | 1 | TXOUT_29 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_29`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV14.5（OUTB）。 [完整端点N0218](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0218)。 |
| ARRAY | 03_UCC_TX | R_TX29 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC29 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC29`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC29.1（1）。 [完整端点N0346](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0346)。 |

接完确认：R_TX29.1=`TXOUT_29`，R_TX29.2=`TX_AC_SRC29`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac29"></a>

### 第150步：在ARRAY／03_UCC_TX放置 C_TX_AC29

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC29**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX29之后、TX29之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC29 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC29 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC29`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX29.2（2）。 [完整端点N0346](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0346)。 |
| ARRAY | 03_UCC_TX | C_TX_AC29 | C1210C104J5GACTU | 2 | 2 | TXPLUS_29 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_29`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED29.1（1）；03_UCC_TX/TX29.1（PLUS）。 [完整端点N0282](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0282)。 |

接完确认：C_TX_AC29.1=`TX_AC_SRC29`，C_TX_AC29.2=`TXPLUS_29`；不可旁路该器件把两个网名短在一起。

<a id="array-tx29"></a>

### 第151步：在ARRAY／03_UCC_TX放置 TX29

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX29**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX29 | NU40C10T-2 | 1 | PLUS | TXPLUS_29 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_29`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC29.2（2）；03_UCC_TX/R_TX_BLEED29.1（1）。 [完整端点N0282](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0282)。 |
| ARRAY | 03_UCC_TX | TX29 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX29.2→GND。

<a id="array-r-tx-bleed29"></a>

### 第152步：在ARRAY／03_UCC_TX放置 R_TX_BLEED29

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED29**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX29.1与TX29.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED29 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_29 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_29`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC29.2（2）；03_UCC_TX/TX29.1（PLUS）。 [完整端点N0282](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0282)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED29 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED29.1=`TXPLUS_29`，R_TX_BLEED29.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv15"></a>

### 第153步：在ARRAY／03_UCC_TX放置 U_DRV15

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV15**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV15 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV15 | UCC27624QDRQ1 | 2 | INA | TXLOG_30 | IN | 从此脚引线，标注精确网名`TXLOG_30`；跨页使用同名板内标签。同网还接：02_595/U_SR07.2（QC）；02_595/R_TX_PD30.1（1）。 [完整端点N0155](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0155)。 |
| ARRAY | 03_UCC_TX | U_DRV15 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV15 | UCC27624QDRQ1 | 4 | INB | TXLOG_31 | IN | 从此脚引线，标注精确网名`TXLOG_31`；跨页使用同名板内标签。同网还接：02_595/U_SR07.3（QD）；02_595/R_TX_PD31.1（1）。 [完整端点N0156](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0156)。 |
| ARRAY | 03_UCC_TX | U_DRV15 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_31 | OUT | 从此脚引线，标注精确网名`TXOUT_31`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX31.1（1）。 [完整端点N0220](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0220)。 |
| ARRAY | 03_UCC_TX | U_DRV15 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV15 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_30 | OUT | 从此脚引线，标注精确网名`TXOUT_30`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX30.1（1）。 [完整端点N0219](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0219)。 |
| ARRAY | 03_UCC_TX | U_DRV15 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV15.3→GND；U_DRV15.6→VTX。

<a id="array-c-u-drv15"></a>

### 第154步：在ARRAY／03_UCC_TX放置 C_U_DRV15

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV15**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV15的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV15 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV15 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV15.1=`VTX`，C_U_DRV15.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx30"></a>

### 第155步：在ARRAY／03_UCC_TX放置 R_TX30

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX30**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV15输出与C_TX_AC30之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX30 | CRCW2512150RFKEG | 1 | 1 | TXOUT_30 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_30`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV15.7（OUTA）。 [完整端点N0219](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0219)。 |
| ARRAY | 03_UCC_TX | R_TX30 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC30 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC30`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC30.1（1）。 [完整端点N0347](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0347)。 |

接完确认：R_TX30.1=`TXOUT_30`，R_TX30.2=`TX_AC_SRC30`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac30"></a>

### 第156步：在ARRAY／03_UCC_TX放置 C_TX_AC30

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC30**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX30之后、TX30之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC30 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC30 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC30`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX30.2（2）。 [完整端点N0347](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0347)。 |
| ARRAY | 03_UCC_TX | C_TX_AC30 | C1210C104J5GACTU | 2 | 2 | TXPLUS_30 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_30`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED30.1（1）；03_UCC_TX/TX30.1（PLUS）。 [完整端点N0283](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0283)。 |

接完确认：C_TX_AC30.1=`TX_AC_SRC30`，C_TX_AC30.2=`TXPLUS_30`；不可旁路该器件把两个网名短在一起。

<a id="array-tx30"></a>

### 第157步：在ARRAY／03_UCC_TX放置 TX30

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX30**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX30 | NU40C10T-2 | 1 | PLUS | TXPLUS_30 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_30`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC30.2（2）；03_UCC_TX/R_TX_BLEED30.1（1）。 [完整端点N0283](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0283)。 |
| ARRAY | 03_UCC_TX | TX30 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX30.2→GND。

<a id="array-r-tx-bleed30"></a>

### 第158步：在ARRAY／03_UCC_TX放置 R_TX_BLEED30

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED30**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX30.1与TX30.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED30 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_30 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_30`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC30.2（2）；03_UCC_TX/TX30.1（PLUS）。 [完整端点N0283](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0283)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED30 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED30.1=`TXPLUS_30`，R_TX_BLEED30.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx31"></a>

### 第159步：在ARRAY／03_UCC_TX放置 R_TX31

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX31**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV15输出与C_TX_AC31之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX31 | CRCW2512150RFKEG | 1 | 1 | TXOUT_31 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_31`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV15.5（OUTB）。 [完整端点N0220](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0220)。 |
| ARRAY | 03_UCC_TX | R_TX31 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC31 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC31`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC31.1（1）。 [完整端点N0348](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0348)。 |

接完确认：R_TX31.1=`TXOUT_31`，R_TX31.2=`TX_AC_SRC31`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac31"></a>

### 第160步：在ARRAY／03_UCC_TX放置 C_TX_AC31

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC31**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX31之后、TX31之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC31 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC31 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC31`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX31.2（2）。 [完整端点N0348](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0348)。 |
| ARRAY | 03_UCC_TX | C_TX_AC31 | C1210C104J5GACTU | 2 | 2 | TXPLUS_31 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_31`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED31.1（1）；03_UCC_TX/TX31.1（PLUS）。 [完整端点N0284](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0284)。 |

接完确认：C_TX_AC31.1=`TX_AC_SRC31`，C_TX_AC31.2=`TXPLUS_31`；不可旁路该器件把两个网名短在一起。

<a id="array-tx31"></a>

### 第161步：在ARRAY／03_UCC_TX放置 TX31

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX31**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX31 | NU40C10T-2 | 1 | PLUS | TXPLUS_31 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_31`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC31.2（2）；03_UCC_TX/R_TX_BLEED31.1（1）。 [完整端点N0284](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0284)。 |
| ARRAY | 03_UCC_TX | TX31 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX31.2→GND。

<a id="array-r-tx-bleed31"></a>

### 第162步：在ARRAY／03_UCC_TX放置 R_TX_BLEED31

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED31**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX31.1与TX31.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED31 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_31 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_31`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC31.2（2）；03_UCC_TX/TX31.1（PLUS）。 [完整端点N0284](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0284)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED31 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED31.1=`TXPLUS_31`，R_TX_BLEED31.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv16"></a>

### 第163步：在ARRAY／03_UCC_TX放置 U_DRV16

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV16**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV16 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV16 | UCC27624QDRQ1 | 2 | INA | TXLOG_32 | IN | 从此脚引线，标注精确网名`TXLOG_32`；跨页使用同名板内标签。同网还接：02_595/U_SR08.15（QA）；02_595/R_TX_PD32.1（1）。 [完整端点N0157](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0157)。 |
| ARRAY | 03_UCC_TX | U_DRV16 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV16 | UCC27624QDRQ1 | 4 | INB | TXLOG_33 | IN | 从此脚引线，标注精确网名`TXLOG_33`；跨页使用同名板内标签。同网还接：02_595/U_SR08.1（QB）；02_595/R_TX_PD33.1（1）。 [完整端点N0158](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0158)。 |
| ARRAY | 03_UCC_TX | U_DRV16 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_33 | OUT | 从此脚引线，标注精确网名`TXOUT_33`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX33.1（1）。 [完整端点N0222](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0222)。 |
| ARRAY | 03_UCC_TX | U_DRV16 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV16 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_32 | OUT | 从此脚引线，标注精确网名`TXOUT_32`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX32.1（1）。 [完整端点N0221](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0221)。 |
| ARRAY | 03_UCC_TX | U_DRV16 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV16.3→GND；U_DRV16.6→VTX。

<a id="array-c-u-drv16"></a>

### 第164步：在ARRAY／03_UCC_TX放置 C_U_DRV16

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV16**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV16的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV16 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV16 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV16.1=`VTX`，C_U_DRV16.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-c-drv-bulk16"></a>

### 第165步：在ARRAY／03_UCC_TX放置 C_DRV_BULK16

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_DRV_BULK16**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_DRV16的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_DRV_BULK16 | C0603C105K3RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_DRV_BULK16 | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_DRV_BULK16.1=`VTX`，C_DRV_BULK16.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx32"></a>

### 第166步：在ARRAY／03_UCC_TX放置 R_TX32

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX32**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV16输出与C_TX_AC32之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX32 | CRCW2512150RFKEG | 1 | 1 | TXOUT_32 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_32`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV16.7（OUTA）。 [完整端点N0221](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0221)。 |
| ARRAY | 03_UCC_TX | R_TX32 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC32 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC32`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC32.1（1）。 [完整端点N0349](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0349)。 |

接完确认：R_TX32.1=`TXOUT_32`，R_TX32.2=`TX_AC_SRC32`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac32"></a>

### 第167步：在ARRAY／03_UCC_TX放置 C_TX_AC32

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC32**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX32之后、TX32之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC32 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC32 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC32`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX32.2（2）。 [完整端点N0349](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0349)。 |
| ARRAY | 03_UCC_TX | C_TX_AC32 | C1210C104J5GACTU | 2 | 2 | TXPLUS_32 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_32`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED32.1（1）；03_UCC_TX/TX32.1（PLUS）。 [完整端点N0285](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0285)。 |

接完确认：C_TX_AC32.1=`TX_AC_SRC32`，C_TX_AC32.2=`TXPLUS_32`；不可旁路该器件把两个网名短在一起。

<a id="array-tx32"></a>

### 第168步：在ARRAY／03_UCC_TX放置 TX32

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX32**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX32 | NU40C10T-2 | 1 | PLUS | TXPLUS_32 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_32`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC32.2（2）；03_UCC_TX/R_TX_BLEED32.1（1）。 [完整端点N0285](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0285)。 |
| ARRAY | 03_UCC_TX | TX32 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX32.2→GND。

<a id="array-r-tx-bleed32"></a>

### 第169步：在ARRAY／03_UCC_TX放置 R_TX_BLEED32

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED32**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX32.1与TX32.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED32 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_32 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_32`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC32.2（2）；03_UCC_TX/TX32.1（PLUS）。 [完整端点N0285](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0285)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED32 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED32.1=`TXPLUS_32`，R_TX_BLEED32.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx33"></a>

### 第170步：在ARRAY／03_UCC_TX放置 R_TX33

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX33**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV16输出与C_TX_AC33之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX33 | CRCW2512150RFKEG | 1 | 1 | TXOUT_33 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_33`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV16.5（OUTB）。 [完整端点N0222](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0222)。 |
| ARRAY | 03_UCC_TX | R_TX33 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC33 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC33`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC33.1（1）。 [完整端点N0350](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0350)。 |

接完确认：R_TX33.1=`TXOUT_33`，R_TX33.2=`TX_AC_SRC33`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac33"></a>

### 第171步：在ARRAY／03_UCC_TX放置 C_TX_AC33

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC33**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX33之后、TX33之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC33 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC33 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC33`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX33.2（2）。 [完整端点N0350](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0350)。 |
| ARRAY | 03_UCC_TX | C_TX_AC33 | C1210C104J5GACTU | 2 | 2 | TXPLUS_33 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_33`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED33.1（1）；03_UCC_TX/TX33.1（PLUS）。 [完整端点N0286](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0286)。 |

接完确认：C_TX_AC33.1=`TX_AC_SRC33`，C_TX_AC33.2=`TXPLUS_33`；不可旁路该器件把两个网名短在一起。

<a id="array-tx33"></a>

### 第172步：在ARRAY／03_UCC_TX放置 TX33

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX33**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX33 | NU40C10T-2 | 1 | PLUS | TXPLUS_33 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_33`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC33.2（2）；03_UCC_TX/R_TX_BLEED33.1（1）。 [完整端点N0286](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0286)。 |
| ARRAY | 03_UCC_TX | TX33 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX33.2→GND。

<a id="array-r-tx-bleed33"></a>

### 第173步：在ARRAY／03_UCC_TX放置 R_TX_BLEED33

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED33**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX33.1与TX33.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED33 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_33 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_33`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC33.2（2）；03_UCC_TX/TX33.1（PLUS）。 [完整端点N0286](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0286)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED33 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED33.1=`TXPLUS_33`，R_TX_BLEED33.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv17"></a>

### 第174步：在ARRAY／03_UCC_TX放置 U_DRV17

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV17**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV17 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV17 | UCC27624QDRQ1 | 2 | INA | TXLOG_34 | IN | 从此脚引线，标注精确网名`TXLOG_34`；跨页使用同名板内标签。同网还接：02_595/U_SR08.2（QC）；02_595/R_TX_PD34.1（1）。 [完整端点N0159](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0159)。 |
| ARRAY | 03_UCC_TX | U_DRV17 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV17 | UCC27624QDRQ1 | 4 | INB | TXLOG_35 | IN | 从此脚引线，标注精确网名`TXLOG_35`；跨页使用同名板内标签。同网还接：02_595/U_SR08.3（QD）；02_595/R_TX_PD35.1（1）。 [完整端点N0160](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0160)。 |
| ARRAY | 03_UCC_TX | U_DRV17 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_35 | OUT | 从此脚引线，标注精确网名`TXOUT_35`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX35.1（1）。 [完整端点N0224](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0224)。 |
| ARRAY | 03_UCC_TX | U_DRV17 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV17 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_34 | OUT | 从此脚引线，标注精确网名`TXOUT_34`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX34.1（1）。 [完整端点N0223](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0223)。 |
| ARRAY | 03_UCC_TX | U_DRV17 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV17.3→GND；U_DRV17.6→VTX。

<a id="array-c-u-drv17"></a>

### 第175步：在ARRAY／03_UCC_TX放置 C_U_DRV17

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV17**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV17的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV17 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV17 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV17.1=`VTX`，C_U_DRV17.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx34"></a>

### 第176步：在ARRAY／03_UCC_TX放置 R_TX34

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX34**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV17输出与C_TX_AC34之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX34 | CRCW2512150RFKEG | 1 | 1 | TXOUT_34 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_34`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV17.7（OUTA）。 [完整端点N0223](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0223)。 |
| ARRAY | 03_UCC_TX | R_TX34 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC34 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC34`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC34.1（1）。 [完整端点N0351](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0351)。 |

接完确认：R_TX34.1=`TXOUT_34`，R_TX34.2=`TX_AC_SRC34`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac34"></a>

### 第177步：在ARRAY／03_UCC_TX放置 C_TX_AC34

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC34**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX34之后、TX34之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC34 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC34 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC34`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX34.2（2）。 [完整端点N0351](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0351)。 |
| ARRAY | 03_UCC_TX | C_TX_AC34 | C1210C104J5GACTU | 2 | 2 | TXPLUS_34 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_34`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED34.1（1）；03_UCC_TX/TX34.1（PLUS）。 [完整端点N0287](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0287)。 |

接完确认：C_TX_AC34.1=`TX_AC_SRC34`，C_TX_AC34.2=`TXPLUS_34`；不可旁路该器件把两个网名短在一起。

<a id="array-tx34"></a>

### 第178步：在ARRAY／03_UCC_TX放置 TX34

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX34**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX34 | NU40C10T-2 | 1 | PLUS | TXPLUS_34 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_34`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC34.2（2）；03_UCC_TX/R_TX_BLEED34.1（1）。 [完整端点N0287](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0287)。 |
| ARRAY | 03_UCC_TX | TX34 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX34.2→GND。

<a id="array-r-tx-bleed34"></a>

### 第179步：在ARRAY／03_UCC_TX放置 R_TX_BLEED34

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED34**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX34.1与TX34.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED34 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_34 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_34`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC34.2（2）；03_UCC_TX/TX34.1（PLUS）。 [完整端点N0287](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0287)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED34 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED34.1=`TXPLUS_34`，R_TX_BLEED34.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx35"></a>

### 第180步：在ARRAY／03_UCC_TX放置 R_TX35

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX35**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV17输出与C_TX_AC35之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX35 | CRCW2512150RFKEG | 1 | 1 | TXOUT_35 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_35`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV17.5（OUTB）。 [完整端点N0224](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0224)。 |
| ARRAY | 03_UCC_TX | R_TX35 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC35 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC35`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC35.1（1）。 [完整端点N0352](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0352)。 |

接完确认：R_TX35.1=`TXOUT_35`，R_TX35.2=`TX_AC_SRC35`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac35"></a>

### 第181步：在ARRAY／03_UCC_TX放置 C_TX_AC35

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC35**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX35之后、TX35之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC35 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC35 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC35`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX35.2（2）。 [完整端点N0352](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0352)。 |
| ARRAY | 03_UCC_TX | C_TX_AC35 | C1210C104J5GACTU | 2 | 2 | TXPLUS_35 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_35`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED35.1（1）；03_UCC_TX/TX35.1（PLUS）。 [完整端点N0288](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0288)。 |

接完确认：C_TX_AC35.1=`TX_AC_SRC35`，C_TX_AC35.2=`TXPLUS_35`；不可旁路该器件把两个网名短在一起。

<a id="array-tx35"></a>

### 第182步：在ARRAY／03_UCC_TX放置 TX35

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX35**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX35 | NU40C10T-2 | 1 | PLUS | TXPLUS_35 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_35`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC35.2（2）；03_UCC_TX/R_TX_BLEED35.1（1）。 [完整端点N0288](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0288)。 |
| ARRAY | 03_UCC_TX | TX35 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX35.2→GND。

<a id="array-r-tx-bleed35"></a>

### 第183步：在ARRAY／03_UCC_TX放置 R_TX_BLEED35

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED35**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX35.1与TX35.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED35 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_35 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_35`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC35.2（2）；03_UCC_TX/TX35.1（PLUS）。 [完整端点N0288](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0288)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED35 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED35.1=`TXPLUS_35`，R_TX_BLEED35.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv18"></a>

### 第184步：在ARRAY／03_UCC_TX放置 U_DRV18

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV18**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV18 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV18 | UCC27624QDRQ1 | 2 | INA | TXLOG_36 | IN | 从此脚引线，标注精确网名`TXLOG_36`；跨页使用同名板内标签。同网还接：02_595/U_SR09.15（QA）；02_595/R_TX_PD36.1（1）。 [完整端点N0161](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0161)。 |
| ARRAY | 03_UCC_TX | U_DRV18 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV18 | UCC27624QDRQ1 | 4 | INB | TXLOG_37 | IN | 从此脚引线，标注精确网名`TXLOG_37`；跨页使用同名板内标签。同网还接：02_595/U_SR09.1（QB）；02_595/R_TX_PD37.1（1）。 [完整端点N0162](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0162)。 |
| ARRAY | 03_UCC_TX | U_DRV18 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_37 | OUT | 从此脚引线，标注精确网名`TXOUT_37`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX37.1（1）。 [完整端点N0226](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0226)。 |
| ARRAY | 03_UCC_TX | U_DRV18 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV18 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_36 | OUT | 从此脚引线，标注精确网名`TXOUT_36`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX36.1（1）。 [完整端点N0225](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0225)。 |
| ARRAY | 03_UCC_TX | U_DRV18 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV18.3→GND；U_DRV18.6→VTX。

<a id="array-c-u-drv18"></a>

### 第185步：在ARRAY／03_UCC_TX放置 C_U_DRV18

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV18**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV18的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV18 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV18 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV18.1=`VTX`，C_U_DRV18.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx36"></a>

### 第186步：在ARRAY／03_UCC_TX放置 R_TX36

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX36**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV18输出与C_TX_AC36之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX36 | CRCW2512150RFKEG | 1 | 1 | TXOUT_36 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_36`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV18.7（OUTA）。 [完整端点N0225](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0225)。 |
| ARRAY | 03_UCC_TX | R_TX36 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC36 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC36`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC36.1（1）。 [完整端点N0353](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0353)。 |

接完确认：R_TX36.1=`TXOUT_36`，R_TX36.2=`TX_AC_SRC36`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac36"></a>

### 第187步：在ARRAY／03_UCC_TX放置 C_TX_AC36

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC36**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX36之后、TX36之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC36 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC36 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC36`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX36.2（2）。 [完整端点N0353](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0353)。 |
| ARRAY | 03_UCC_TX | C_TX_AC36 | C1210C104J5GACTU | 2 | 2 | TXPLUS_36 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_36`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED36.1（1）；03_UCC_TX/TX36.1（PLUS）。 [完整端点N0289](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0289)。 |

接完确认：C_TX_AC36.1=`TX_AC_SRC36`，C_TX_AC36.2=`TXPLUS_36`；不可旁路该器件把两个网名短在一起。

<a id="array-tx36"></a>

### 第188步：在ARRAY／03_UCC_TX放置 TX36

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX36**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX36 | NU40C10T-2 | 1 | PLUS | TXPLUS_36 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_36`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC36.2（2）；03_UCC_TX/R_TX_BLEED36.1（1）。 [完整端点N0289](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0289)。 |
| ARRAY | 03_UCC_TX | TX36 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX36.2→GND。

<a id="array-r-tx-bleed36"></a>

### 第189步：在ARRAY／03_UCC_TX放置 R_TX_BLEED36

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED36**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX36.1与TX36.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED36 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_36 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_36`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC36.2（2）；03_UCC_TX/TX36.1（PLUS）。 [完整端点N0289](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0289)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED36 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED36.1=`TXPLUS_36`，R_TX_BLEED36.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx37"></a>

### 第190步：在ARRAY／03_UCC_TX放置 R_TX37

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX37**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV18输出与C_TX_AC37之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX37 | CRCW2512150RFKEG | 1 | 1 | TXOUT_37 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_37`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV18.5（OUTB）。 [完整端点N0226](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0226)。 |
| ARRAY | 03_UCC_TX | R_TX37 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC37 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC37`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC37.1（1）。 [完整端点N0354](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0354)。 |

接完确认：R_TX37.1=`TXOUT_37`，R_TX37.2=`TX_AC_SRC37`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac37"></a>

### 第191步：在ARRAY／03_UCC_TX放置 C_TX_AC37

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC37**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX37之后、TX37之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC37 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC37 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC37`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX37.2（2）。 [完整端点N0354](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0354)。 |
| ARRAY | 03_UCC_TX | C_TX_AC37 | C1210C104J5GACTU | 2 | 2 | TXPLUS_37 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_37`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED37.1（1）；03_UCC_TX/TX37.1（PLUS）。 [完整端点N0290](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0290)。 |

接完确认：C_TX_AC37.1=`TX_AC_SRC37`，C_TX_AC37.2=`TXPLUS_37`；不可旁路该器件把两个网名短在一起。

<a id="array-tx37"></a>

### 第192步：在ARRAY／03_UCC_TX放置 TX37

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX37**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX37 | NU40C10T-2 | 1 | PLUS | TXPLUS_37 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_37`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC37.2（2）；03_UCC_TX/R_TX_BLEED37.1（1）。 [完整端点N0290](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0290)。 |
| ARRAY | 03_UCC_TX | TX37 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX37.2→GND。

<a id="array-r-tx-bleed37"></a>

### 第193步：在ARRAY／03_UCC_TX放置 R_TX_BLEED37

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED37**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX37.1与TX37.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED37 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_37 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_37`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC37.2（2）；03_UCC_TX/TX37.1（PLUS）。 [完整端点N0290](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0290)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED37 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED37.1=`TXPLUS_37`，R_TX_BLEED37.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv19"></a>

### 第194步：在ARRAY／03_UCC_TX放置 U_DRV19

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV19**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV19 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV19 | UCC27624QDRQ1 | 2 | INA | TXLOG_38 | IN | 从此脚引线，标注精确网名`TXLOG_38`；跨页使用同名板内标签。同网还接：02_595/U_SR09.2（QC）；02_595/R_TX_PD38.1（1）。 [完整端点N0163](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0163)。 |
| ARRAY | 03_UCC_TX | U_DRV19 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV19 | UCC27624QDRQ1 | 4 | INB | TXLOG_39 | IN | 从此脚引线，标注精确网名`TXLOG_39`；跨页使用同名板内标签。同网还接：02_595/U_SR09.3（QD）；02_595/R_TX_PD39.1（1）。 [完整端点N0164](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0164)。 |
| ARRAY | 03_UCC_TX | U_DRV19 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_39 | OUT | 从此脚引线，标注精确网名`TXOUT_39`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX39.1（1）。 [完整端点N0228](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0228)。 |
| ARRAY | 03_UCC_TX | U_DRV19 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV19 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_38 | OUT | 从此脚引线，标注精确网名`TXOUT_38`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX38.1（1）。 [完整端点N0227](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0227)。 |
| ARRAY | 03_UCC_TX | U_DRV19 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV19.3→GND；U_DRV19.6→VTX。

<a id="array-c-u-drv19"></a>

### 第195步：在ARRAY／03_UCC_TX放置 C_U_DRV19

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV19**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV19的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV19 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV19 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV19.1=`VTX`，C_U_DRV19.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx38"></a>

### 第196步：在ARRAY／03_UCC_TX放置 R_TX38

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX38**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV19输出与C_TX_AC38之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX38 | CRCW2512150RFKEG | 1 | 1 | TXOUT_38 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_38`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV19.7（OUTA）。 [完整端点N0227](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0227)。 |
| ARRAY | 03_UCC_TX | R_TX38 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC38 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC38`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC38.1（1）。 [完整端点N0355](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0355)。 |

接完确认：R_TX38.1=`TXOUT_38`，R_TX38.2=`TX_AC_SRC38`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac38"></a>

### 第197步：在ARRAY／03_UCC_TX放置 C_TX_AC38

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC38**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX38之后、TX38之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC38 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC38 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC38`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX38.2（2）。 [完整端点N0355](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0355)。 |
| ARRAY | 03_UCC_TX | C_TX_AC38 | C1210C104J5GACTU | 2 | 2 | TXPLUS_38 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_38`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED38.1（1）；03_UCC_TX/TX38.1（PLUS）。 [完整端点N0291](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0291)。 |

接完确认：C_TX_AC38.1=`TX_AC_SRC38`，C_TX_AC38.2=`TXPLUS_38`；不可旁路该器件把两个网名短在一起。

<a id="array-tx38"></a>

### 第198步：在ARRAY／03_UCC_TX放置 TX38

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX38**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX38 | NU40C10T-2 | 1 | PLUS | TXPLUS_38 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_38`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC38.2（2）；03_UCC_TX/R_TX_BLEED38.1（1）。 [完整端点N0291](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0291)。 |
| ARRAY | 03_UCC_TX | TX38 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX38.2→GND。

<a id="array-r-tx-bleed38"></a>

### 第199步：在ARRAY／03_UCC_TX放置 R_TX_BLEED38

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED38**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX38.1与TX38.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED38 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_38 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_38`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC38.2（2）；03_UCC_TX/TX38.1（PLUS）。 [完整端点N0291](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0291)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED38 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED38.1=`TXPLUS_38`，R_TX_BLEED38.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx39"></a>

### 第200步：在ARRAY／03_UCC_TX放置 R_TX39

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX39**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV19输出与C_TX_AC39之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX39 | CRCW2512150RFKEG | 1 | 1 | TXOUT_39 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_39`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV19.5（OUTB）。 [完整端点N0228](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0228)。 |
| ARRAY | 03_UCC_TX | R_TX39 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC39 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC39`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC39.1（1）。 [完整端点N0356](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0356)。 |

接完确认：R_TX39.1=`TXOUT_39`，R_TX39.2=`TX_AC_SRC39`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac39"></a>

### 第201步：在ARRAY／03_UCC_TX放置 C_TX_AC39

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC39**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX39之后、TX39之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC39 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC39 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC39`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX39.2（2）。 [完整端点N0356](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0356)。 |
| ARRAY | 03_UCC_TX | C_TX_AC39 | C1210C104J5GACTU | 2 | 2 | TXPLUS_39 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_39`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED39.1（1）；03_UCC_TX/TX39.1（PLUS）。 [完整端点N0292](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0292)。 |

接完确认：C_TX_AC39.1=`TX_AC_SRC39`，C_TX_AC39.2=`TXPLUS_39`；不可旁路该器件把两个网名短在一起。

<a id="array-tx39"></a>

### 第202步：在ARRAY／03_UCC_TX放置 TX39

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX39**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX39 | NU40C10T-2 | 1 | PLUS | TXPLUS_39 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_39`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC39.2（2）；03_UCC_TX/R_TX_BLEED39.1（1）。 [完整端点N0292](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0292)。 |
| ARRAY | 03_UCC_TX | TX39 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX39.2→GND。

<a id="array-r-tx-bleed39"></a>

### 第203步：在ARRAY／03_UCC_TX放置 R_TX_BLEED39

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED39**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX39.1与TX39.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED39 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_39 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_39`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC39.2（2）；03_UCC_TX/TX39.1（PLUS）。 [完整端点N0292](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0292)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED39 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED39.1=`TXPLUS_39`，R_TX_BLEED39.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv20"></a>

### 第204步：在ARRAY／03_UCC_TX放置 U_DRV20

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV20**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV20 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV20 | UCC27624QDRQ1 | 2 | INA | TXLOG_40 | IN | 从此脚引线，标注精确网名`TXLOG_40`；跨页使用同名板内标签。同网还接：02_595/U_SR10.15（QA）；02_595/R_TX_PD40.1（1）。 [完整端点N0165](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0165)。 |
| ARRAY | 03_UCC_TX | U_DRV20 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV20 | UCC27624QDRQ1 | 4 | INB | TXLOG_41 | IN | 从此脚引线，标注精确网名`TXLOG_41`；跨页使用同名板内标签。同网还接：02_595/U_SR10.1（QB）；02_595/R_TX_PD41.1（1）。 [完整端点N0166](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0166)。 |
| ARRAY | 03_UCC_TX | U_DRV20 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_41 | OUT | 从此脚引线，标注精确网名`TXOUT_41`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX41.1（1）。 [完整端点N0230](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0230)。 |
| ARRAY | 03_UCC_TX | U_DRV20 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV20 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_40 | OUT | 从此脚引线，标注精确网名`TXOUT_40`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX40.1（1）。 [完整端点N0229](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0229)。 |
| ARRAY | 03_UCC_TX | U_DRV20 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV20.3→GND；U_DRV20.6→VTX。

<a id="array-c-u-drv20"></a>

### 第205步：在ARRAY／03_UCC_TX放置 C_U_DRV20

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV20**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV20的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV20 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV20 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV20.1=`VTX`，C_U_DRV20.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx40"></a>

### 第206步：在ARRAY／03_UCC_TX放置 R_TX40

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX40**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV20输出与C_TX_AC40之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX40 | CRCW2512150RFKEG | 1 | 1 | TXOUT_40 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_40`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV20.7（OUTA）。 [完整端点N0229](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0229)。 |
| ARRAY | 03_UCC_TX | R_TX40 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC40 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC40`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC40.1（1）。 [完整端点N0357](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0357)。 |

接完确认：R_TX40.1=`TXOUT_40`，R_TX40.2=`TX_AC_SRC40`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac40"></a>

### 第207步：在ARRAY／03_UCC_TX放置 C_TX_AC40

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC40**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX40之后、TX40之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC40 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC40 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC40`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX40.2（2）。 [完整端点N0357](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0357)。 |
| ARRAY | 03_UCC_TX | C_TX_AC40 | C1210C104J5GACTU | 2 | 2 | TXPLUS_40 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_40`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED40.1（1）；03_UCC_TX/TX40.1（PLUS）。 [完整端点N0293](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0293)。 |

接完确认：C_TX_AC40.1=`TX_AC_SRC40`，C_TX_AC40.2=`TXPLUS_40`；不可旁路该器件把两个网名短在一起。

<a id="array-tx40"></a>

### 第208步：在ARRAY／03_UCC_TX放置 TX40

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX40**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX40 | NU40C10T-2 | 1 | PLUS | TXPLUS_40 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_40`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC40.2（2）；03_UCC_TX/R_TX_BLEED40.1（1）。 [完整端点N0293](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0293)。 |
| ARRAY | 03_UCC_TX | TX40 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX40.2→GND。

<a id="array-r-tx-bleed40"></a>

### 第209步：在ARRAY／03_UCC_TX放置 R_TX_BLEED40

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED40**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX40.1与TX40.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED40 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_40 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_40`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC40.2（2）；03_UCC_TX/TX40.1（PLUS）。 [完整端点N0293](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0293)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED40 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED40.1=`TXPLUS_40`，R_TX_BLEED40.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx41"></a>

### 第210步：在ARRAY／03_UCC_TX放置 R_TX41

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX41**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV20输出与C_TX_AC41之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX41 | CRCW2512150RFKEG | 1 | 1 | TXOUT_41 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_41`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV20.5（OUTB）。 [完整端点N0230](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0230)。 |
| ARRAY | 03_UCC_TX | R_TX41 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC41 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC41`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC41.1（1）。 [完整端点N0358](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0358)。 |

接完确认：R_TX41.1=`TXOUT_41`，R_TX41.2=`TX_AC_SRC41`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac41"></a>

### 第211步：在ARRAY／03_UCC_TX放置 C_TX_AC41

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC41**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX41之后、TX41之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC41 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC41 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC41`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX41.2（2）。 [完整端点N0358](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0358)。 |
| ARRAY | 03_UCC_TX | C_TX_AC41 | C1210C104J5GACTU | 2 | 2 | TXPLUS_41 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_41`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED41.1（1）；03_UCC_TX/TX41.1（PLUS）。 [完整端点N0294](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0294)。 |

接完确认：C_TX_AC41.1=`TX_AC_SRC41`，C_TX_AC41.2=`TXPLUS_41`；不可旁路该器件把两个网名短在一起。

<a id="array-tx41"></a>

### 第212步：在ARRAY／03_UCC_TX放置 TX41

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX41**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX41 | NU40C10T-2 | 1 | PLUS | TXPLUS_41 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_41`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC41.2（2）；03_UCC_TX/R_TX_BLEED41.1（1）。 [完整端点N0294](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0294)。 |
| ARRAY | 03_UCC_TX | TX41 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX41.2→GND。

<a id="array-r-tx-bleed41"></a>

### 第213步：在ARRAY／03_UCC_TX放置 R_TX_BLEED41

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED41**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX41.1与TX41.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED41 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_41 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_41`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC41.2（2）；03_UCC_TX/TX41.1（PLUS）。 [完整端点N0294](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0294)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED41 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED41.1=`TXPLUS_41`，R_TX_BLEED41.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv21"></a>

### 第214步：在ARRAY／03_UCC_TX放置 U_DRV21

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV21**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV21 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV21 | UCC27624QDRQ1 | 2 | INA | TXLOG_42 | IN | 从此脚引线，标注精确网名`TXLOG_42`；跨页使用同名板内标签。同网还接：02_595/U_SR10.2（QC）；02_595/R_TX_PD42.1（1）。 [完整端点N0167](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0167)。 |
| ARRAY | 03_UCC_TX | U_DRV21 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV21 | UCC27624QDRQ1 | 4 | INB | TXLOG_43 | IN | 从此脚引线，标注精确网名`TXLOG_43`；跨页使用同名板内标签。同网还接：02_595/U_SR10.3（QD）；02_595/R_TX_PD43.1（1）。 [完整端点N0168](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0168)。 |
| ARRAY | 03_UCC_TX | U_DRV21 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_43 | OUT | 从此脚引线，标注精确网名`TXOUT_43`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX43.1（1）。 [完整端点N0232](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0232)。 |
| ARRAY | 03_UCC_TX | U_DRV21 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV21 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_42 | OUT | 从此脚引线，标注精确网名`TXOUT_42`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX42.1（1）。 [完整端点N0231](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0231)。 |
| ARRAY | 03_UCC_TX | U_DRV21 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV21.3→GND；U_DRV21.6→VTX。

<a id="array-c-u-drv21"></a>

### 第215步：在ARRAY／03_UCC_TX放置 C_U_DRV21

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV21**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV21的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV21 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV21 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV21.1=`VTX`，C_U_DRV21.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx42"></a>

### 第216步：在ARRAY／03_UCC_TX放置 R_TX42

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX42**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV21输出与C_TX_AC42之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX42 | CRCW2512150RFKEG | 1 | 1 | TXOUT_42 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_42`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV21.7（OUTA）。 [完整端点N0231](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0231)。 |
| ARRAY | 03_UCC_TX | R_TX42 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC42 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC42`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC42.1（1）。 [完整端点N0359](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0359)。 |

接完确认：R_TX42.1=`TXOUT_42`，R_TX42.2=`TX_AC_SRC42`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac42"></a>

### 第217步：在ARRAY／03_UCC_TX放置 C_TX_AC42

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC42**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX42之后、TX42之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC42 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC42 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC42`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX42.2（2）。 [完整端点N0359](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0359)。 |
| ARRAY | 03_UCC_TX | C_TX_AC42 | C1210C104J5GACTU | 2 | 2 | TXPLUS_42 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_42`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED42.1（1）；03_UCC_TX/TX42.1（PLUS）。 [完整端点N0295](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0295)。 |

接完确认：C_TX_AC42.1=`TX_AC_SRC42`，C_TX_AC42.2=`TXPLUS_42`；不可旁路该器件把两个网名短在一起。

<a id="array-tx42"></a>

### 第218步：在ARRAY／03_UCC_TX放置 TX42

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX42**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX42 | NU40C10T-2 | 1 | PLUS | TXPLUS_42 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_42`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC42.2（2）；03_UCC_TX/R_TX_BLEED42.1（1）。 [完整端点N0295](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0295)。 |
| ARRAY | 03_UCC_TX | TX42 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX42.2→GND。

<a id="array-r-tx-bleed42"></a>

### 第219步：在ARRAY／03_UCC_TX放置 R_TX_BLEED42

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED42**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX42.1与TX42.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED42 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_42 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_42`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC42.2（2）；03_UCC_TX/TX42.1（PLUS）。 [完整端点N0295](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0295)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED42 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED42.1=`TXPLUS_42`，R_TX_BLEED42.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx43"></a>

### 第220步：在ARRAY／03_UCC_TX放置 R_TX43

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX43**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV21输出与C_TX_AC43之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX43 | CRCW2512150RFKEG | 1 | 1 | TXOUT_43 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_43`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV21.5（OUTB）。 [完整端点N0232](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0232)。 |
| ARRAY | 03_UCC_TX | R_TX43 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC43 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC43`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC43.1（1）。 [完整端点N0360](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0360)。 |

接完确认：R_TX43.1=`TXOUT_43`，R_TX43.2=`TX_AC_SRC43`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac43"></a>

### 第221步：在ARRAY／03_UCC_TX放置 C_TX_AC43

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC43**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX43之后、TX43之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC43 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC43 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC43`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX43.2（2）。 [完整端点N0360](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0360)。 |
| ARRAY | 03_UCC_TX | C_TX_AC43 | C1210C104J5GACTU | 2 | 2 | TXPLUS_43 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_43`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED43.1（1）；03_UCC_TX/TX43.1（PLUS）。 [完整端点N0296](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0296)。 |

接完确认：C_TX_AC43.1=`TX_AC_SRC43`，C_TX_AC43.2=`TXPLUS_43`；不可旁路该器件把两个网名短在一起。

<a id="array-tx43"></a>

### 第222步：在ARRAY／03_UCC_TX放置 TX43

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX43**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX43 | NU40C10T-2 | 1 | PLUS | TXPLUS_43 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_43`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC43.2（2）；03_UCC_TX/R_TX_BLEED43.1（1）。 [完整端点N0296](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0296)。 |
| ARRAY | 03_UCC_TX | TX43 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX43.2→GND。

<a id="array-r-tx-bleed43"></a>

### 第223步：在ARRAY／03_UCC_TX放置 R_TX_BLEED43

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED43**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX43.1与TX43.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED43 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_43 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_43`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC43.2（2）；03_UCC_TX/TX43.1（PLUS）。 [完整端点N0296](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0296)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED43 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED43.1=`TXPLUS_43`，R_TX_BLEED43.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv22"></a>

### 第224步：在ARRAY／03_UCC_TX放置 U_DRV22

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV22**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV22 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV22 | UCC27624QDRQ1 | 2 | INA | TXLOG_44 | IN | 从此脚引线，标注精确网名`TXLOG_44`；跨页使用同名板内标签。同网还接：02_595/U_SR11.15（QA）；02_595/R_TX_PD44.1（1）。 [完整端点N0169](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0169)。 |
| ARRAY | 03_UCC_TX | U_DRV22 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV22 | UCC27624QDRQ1 | 4 | INB | TXLOG_45 | IN | 从此脚引线，标注精确网名`TXLOG_45`；跨页使用同名板内标签。同网还接：02_595/U_SR11.1（QB）；02_595/R_TX_PD45.1（1）。 [完整端点N0170](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0170)。 |
| ARRAY | 03_UCC_TX | U_DRV22 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_45 | OUT | 从此脚引线，标注精确网名`TXOUT_45`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX45.1（1）。 [完整端点N0234](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0234)。 |
| ARRAY | 03_UCC_TX | U_DRV22 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV22 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_44 | OUT | 从此脚引线，标注精确网名`TXOUT_44`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX44.1（1）。 [完整端点N0233](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0233)。 |
| ARRAY | 03_UCC_TX | U_DRV22 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV22.3→GND；U_DRV22.6→VTX。

<a id="array-c-u-drv22"></a>

### 第225步：在ARRAY／03_UCC_TX放置 C_U_DRV22

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV22**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV22的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV22 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV22 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV22.1=`VTX`，C_U_DRV22.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx44"></a>

### 第226步：在ARRAY／03_UCC_TX放置 R_TX44

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX44**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV22输出与C_TX_AC44之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX44 | CRCW2512150RFKEG | 1 | 1 | TXOUT_44 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_44`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV22.7（OUTA）。 [完整端点N0233](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0233)。 |
| ARRAY | 03_UCC_TX | R_TX44 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC44 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC44`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC44.1（1）。 [完整端点N0361](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0361)。 |

接完确认：R_TX44.1=`TXOUT_44`，R_TX44.2=`TX_AC_SRC44`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac44"></a>

### 第227步：在ARRAY／03_UCC_TX放置 C_TX_AC44

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC44**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX44之后、TX44之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC44 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC44 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC44`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX44.2（2）。 [完整端点N0361](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0361)。 |
| ARRAY | 03_UCC_TX | C_TX_AC44 | C1210C104J5GACTU | 2 | 2 | TXPLUS_44 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_44`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED44.1（1）；03_UCC_TX/TX44.1（PLUS）。 [完整端点N0297](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0297)。 |

接完确认：C_TX_AC44.1=`TX_AC_SRC44`，C_TX_AC44.2=`TXPLUS_44`；不可旁路该器件把两个网名短在一起。

<a id="array-tx44"></a>

### 第228步：在ARRAY／03_UCC_TX放置 TX44

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX44**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX44 | NU40C10T-2 | 1 | PLUS | TXPLUS_44 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_44`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC44.2（2）；03_UCC_TX/R_TX_BLEED44.1（1）。 [完整端点N0297](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0297)。 |
| ARRAY | 03_UCC_TX | TX44 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX44.2→GND。

<a id="array-r-tx-bleed44"></a>

### 第229步：在ARRAY／03_UCC_TX放置 R_TX_BLEED44

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED44**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX44.1与TX44.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED44 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_44 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_44`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC44.2（2）；03_UCC_TX/TX44.1（PLUS）。 [完整端点N0297](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0297)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED44 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED44.1=`TXPLUS_44`，R_TX_BLEED44.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx45"></a>

### 第230步：在ARRAY／03_UCC_TX放置 R_TX45

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX45**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV22输出与C_TX_AC45之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX45 | CRCW2512150RFKEG | 1 | 1 | TXOUT_45 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_45`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV22.5（OUTB）。 [完整端点N0234](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0234)。 |
| ARRAY | 03_UCC_TX | R_TX45 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC45 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC45`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC45.1（1）。 [完整端点N0362](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0362)。 |

接完确认：R_TX45.1=`TXOUT_45`，R_TX45.2=`TX_AC_SRC45`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac45"></a>

### 第231步：在ARRAY／03_UCC_TX放置 C_TX_AC45

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC45**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX45之后、TX45之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC45 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC45 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC45`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX45.2（2）。 [完整端点N0362](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0362)。 |
| ARRAY | 03_UCC_TX | C_TX_AC45 | C1210C104J5GACTU | 2 | 2 | TXPLUS_45 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_45`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED45.1（1）；03_UCC_TX/TX45.1（PLUS）。 [完整端点N0298](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0298)。 |

接完确认：C_TX_AC45.1=`TX_AC_SRC45`，C_TX_AC45.2=`TXPLUS_45`；不可旁路该器件把两个网名短在一起。

<a id="array-tx45"></a>

### 第232步：在ARRAY／03_UCC_TX放置 TX45

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX45**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX45 | NU40C10T-2 | 1 | PLUS | TXPLUS_45 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_45`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC45.2（2）；03_UCC_TX/R_TX_BLEED45.1（1）。 [完整端点N0298](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0298)。 |
| ARRAY | 03_UCC_TX | TX45 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX45.2→GND。

<a id="array-r-tx-bleed45"></a>

### 第233步：在ARRAY／03_UCC_TX放置 R_TX_BLEED45

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED45**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX45.1与TX45.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED45 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_45 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_45`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC45.2（2）；03_UCC_TX/TX45.1（PLUS）。 [完整端点N0298](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0298)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED45 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED45.1=`TXPLUS_45`，R_TX_BLEED45.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv23"></a>

### 第234步：在ARRAY／03_UCC_TX放置 U_DRV23

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV23**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV23 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV23 | UCC27624QDRQ1 | 2 | INA | TXLOG_46 | IN | 从此脚引线，标注精确网名`TXLOG_46`；跨页使用同名板内标签。同网还接：02_595/U_SR11.2（QC）；02_595/R_TX_PD46.1（1）。 [完整端点N0171](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0171)。 |
| ARRAY | 03_UCC_TX | U_DRV23 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV23 | UCC27624QDRQ1 | 4 | INB | TXLOG_47 | IN | 从此脚引线，标注精确网名`TXLOG_47`；跨页使用同名板内标签。同网还接：02_595/U_SR11.3（QD）；02_595/R_TX_PD47.1（1）。 [完整端点N0172](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0172)。 |
| ARRAY | 03_UCC_TX | U_DRV23 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_47 | OUT | 从此脚引线，标注精确网名`TXOUT_47`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX47.1（1）。 [完整端点N0236](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0236)。 |
| ARRAY | 03_UCC_TX | U_DRV23 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV23 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_46 | OUT | 从此脚引线，标注精确网名`TXOUT_46`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX46.1（1）。 [完整端点N0235](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0235)。 |
| ARRAY | 03_UCC_TX | U_DRV23 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV23.3→GND；U_DRV23.6→VTX。

<a id="array-c-u-drv23"></a>

### 第235步：在ARRAY／03_UCC_TX放置 C_U_DRV23

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV23**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV23的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV23 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV23 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV23.1=`VTX`，C_U_DRV23.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx46"></a>

### 第236步：在ARRAY／03_UCC_TX放置 R_TX46

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX46**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV23输出与C_TX_AC46之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX46 | CRCW2512150RFKEG | 1 | 1 | TXOUT_46 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_46`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV23.7（OUTA）。 [完整端点N0235](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0235)。 |
| ARRAY | 03_UCC_TX | R_TX46 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC46 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC46`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC46.1（1）。 [完整端点N0363](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0363)。 |

接完确认：R_TX46.1=`TXOUT_46`，R_TX46.2=`TX_AC_SRC46`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac46"></a>

### 第237步：在ARRAY／03_UCC_TX放置 C_TX_AC46

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC46**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX46之后、TX46之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC46 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC46 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC46`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX46.2（2）。 [完整端点N0363](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0363)。 |
| ARRAY | 03_UCC_TX | C_TX_AC46 | C1210C104J5GACTU | 2 | 2 | TXPLUS_46 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_46`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED46.1（1）；03_UCC_TX/TX46.1（PLUS）。 [完整端点N0299](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0299)。 |

接完确认：C_TX_AC46.1=`TX_AC_SRC46`，C_TX_AC46.2=`TXPLUS_46`；不可旁路该器件把两个网名短在一起。

<a id="array-tx46"></a>

### 第238步：在ARRAY／03_UCC_TX放置 TX46

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX46**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX46 | NU40C10T-2 | 1 | PLUS | TXPLUS_46 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_46`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC46.2（2）；03_UCC_TX/R_TX_BLEED46.1（1）。 [完整端点N0299](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0299)。 |
| ARRAY | 03_UCC_TX | TX46 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX46.2→GND。

<a id="array-r-tx-bleed46"></a>

### 第239步：在ARRAY／03_UCC_TX放置 R_TX_BLEED46

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED46**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX46.1与TX46.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED46 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_46 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_46`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC46.2（2）；03_UCC_TX/TX46.1（PLUS）。 [完整端点N0299](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0299)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED46 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED46.1=`TXPLUS_46`，R_TX_BLEED46.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx47"></a>

### 第240步：在ARRAY／03_UCC_TX放置 R_TX47

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX47**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV23输出与C_TX_AC47之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX47 | CRCW2512150RFKEG | 1 | 1 | TXOUT_47 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_47`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV23.5（OUTB）。 [完整端点N0236](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0236)。 |
| ARRAY | 03_UCC_TX | R_TX47 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC47 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC47`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC47.1（1）。 [完整端点N0364](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0364)。 |

接完确认：R_TX47.1=`TXOUT_47`，R_TX47.2=`TX_AC_SRC47`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac47"></a>

### 第241步：在ARRAY／03_UCC_TX放置 C_TX_AC47

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC47**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX47之后、TX47之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC47 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC47 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC47`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX47.2（2）。 [完整端点N0364](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0364)。 |
| ARRAY | 03_UCC_TX | C_TX_AC47 | C1210C104J5GACTU | 2 | 2 | TXPLUS_47 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_47`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED47.1（1）；03_UCC_TX/TX47.1（PLUS）。 [完整端点N0300](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0300)。 |

接完确认：C_TX_AC47.1=`TX_AC_SRC47`，C_TX_AC47.2=`TXPLUS_47`；不可旁路该器件把两个网名短在一起。

<a id="array-tx47"></a>

### 第242步：在ARRAY／03_UCC_TX放置 TX47

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX47**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX47 | NU40C10T-2 | 1 | PLUS | TXPLUS_47 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_47`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC47.2（2）；03_UCC_TX/R_TX_BLEED47.1（1）。 [完整端点N0300](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0300)。 |
| ARRAY | 03_UCC_TX | TX47 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX47.2→GND。

<a id="array-r-tx-bleed47"></a>

### 第243步：在ARRAY／03_UCC_TX放置 R_TX_BLEED47

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED47**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX47.1与TX47.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED47 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_47 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_47`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC47.2（2）；03_UCC_TX/TX47.1（PLUS）。 [完整端点N0300](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0300)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED47 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED47.1=`TXPLUS_47`，R_TX_BLEED47.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv24"></a>

### 第244步：在ARRAY／03_UCC_TX放置 U_DRV24

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV24**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV24 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV24 | UCC27624QDRQ1 | 2 | INA | TXLOG_48 | IN | 从此脚引线，标注精确网名`TXLOG_48`；跨页使用同名板内标签。同网还接：02_595/U_SR12.15（QA）；02_595/R_TX_PD48.1（1）。 [完整端点N0173](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0173)。 |
| ARRAY | 03_UCC_TX | U_DRV24 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV24 | UCC27624QDRQ1 | 4 | INB | TXLOG_49 | IN | 从此脚引线，标注精确网名`TXLOG_49`；跨页使用同名板内标签。同网还接：02_595/U_SR12.1（QB）；02_595/R_TX_PD49.1（1）。 [完整端点N0174](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0174)。 |
| ARRAY | 03_UCC_TX | U_DRV24 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_49 | OUT | 从此脚引线，标注精确网名`TXOUT_49`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX49.1（1）。 [完整端点N0238](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0238)。 |
| ARRAY | 03_UCC_TX | U_DRV24 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV24 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_48 | OUT | 从此脚引线，标注精确网名`TXOUT_48`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX48.1（1）。 [完整端点N0237](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0237)。 |
| ARRAY | 03_UCC_TX | U_DRV24 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV24.3→GND；U_DRV24.6→VTX。

<a id="array-c-u-drv24"></a>

### 第245步：在ARRAY／03_UCC_TX放置 C_U_DRV24

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV24**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV24的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV24 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV24 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV24.1=`VTX`，C_U_DRV24.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-c-drv-bulk24"></a>

### 第246步：在ARRAY／03_UCC_TX放置 C_DRV_BULK24

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_DRV_BULK24**，精确型号 **C0603C105K3RACTU**，封装 **0603**。其值为 **1uF**。

纸面位置：紧邻本页U_DRV24的相应引脚区域。额定条件：25V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_DRV_BULK24 | C0603C105K3RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_DRV_BULK24 | C0603C105K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_DRV_BULK24.1=`VTX`，C_DRV_BULK24.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx48"></a>

### 第247步：在ARRAY／03_UCC_TX放置 R_TX48

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX48**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV24输出与C_TX_AC48之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX48 | CRCW2512150RFKEG | 1 | 1 | TXOUT_48 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_48`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV24.7（OUTA）。 [完整端点N0237](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0237)。 |
| ARRAY | 03_UCC_TX | R_TX48 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC48 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC48`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC48.1（1）。 [完整端点N0365](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0365)。 |

接完确认：R_TX48.1=`TXOUT_48`，R_TX48.2=`TX_AC_SRC48`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac48"></a>

### 第248步：在ARRAY／03_UCC_TX放置 C_TX_AC48

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC48**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX48之后、TX48之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC48 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC48 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC48`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX48.2（2）。 [完整端点N0365](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0365)。 |
| ARRAY | 03_UCC_TX | C_TX_AC48 | C1210C104J5GACTU | 2 | 2 | TXPLUS_48 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_48`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED48.1（1）；03_UCC_TX/TX48.1（PLUS）。 [完整端点N0301](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0301)。 |

接完确认：C_TX_AC48.1=`TX_AC_SRC48`，C_TX_AC48.2=`TXPLUS_48`；不可旁路该器件把两个网名短在一起。

<a id="array-tx48"></a>

### 第249步：在ARRAY／03_UCC_TX放置 TX48

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX48**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX48 | NU40C10T-2 | 1 | PLUS | TXPLUS_48 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_48`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC48.2（2）；03_UCC_TX/R_TX_BLEED48.1（1）。 [完整端点N0301](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0301)。 |
| ARRAY | 03_UCC_TX | TX48 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX48.2→GND。

<a id="array-r-tx-bleed48"></a>

### 第250步：在ARRAY／03_UCC_TX放置 R_TX_BLEED48

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED48**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX48.1与TX48.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED48 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_48 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_48`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC48.2（2）；03_UCC_TX/TX48.1（PLUS）。 [完整端点N0301](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0301)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED48 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED48.1=`TXPLUS_48`，R_TX_BLEED48.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx49"></a>

### 第251步：在ARRAY／03_UCC_TX放置 R_TX49

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX49**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV24输出与C_TX_AC49之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX49 | CRCW2512150RFKEG | 1 | 1 | TXOUT_49 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_49`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV24.5（OUTB）。 [完整端点N0238](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0238)。 |
| ARRAY | 03_UCC_TX | R_TX49 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC49 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC49`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC49.1（1）。 [完整端点N0366](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0366)。 |

接完确认：R_TX49.1=`TXOUT_49`，R_TX49.2=`TX_AC_SRC49`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac49"></a>

### 第252步：在ARRAY／03_UCC_TX放置 C_TX_AC49

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC49**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX49之后、TX49之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC49 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC49 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC49`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX49.2（2）。 [完整端点N0366](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0366)。 |
| ARRAY | 03_UCC_TX | C_TX_AC49 | C1210C104J5GACTU | 2 | 2 | TXPLUS_49 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_49`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED49.1（1）；03_UCC_TX/TX49.1（PLUS）。 [完整端点N0302](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0302)。 |

接完确认：C_TX_AC49.1=`TX_AC_SRC49`，C_TX_AC49.2=`TXPLUS_49`；不可旁路该器件把两个网名短在一起。

<a id="array-tx49"></a>

### 第253步：在ARRAY／03_UCC_TX放置 TX49

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX49**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX49 | NU40C10T-2 | 1 | PLUS | TXPLUS_49 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_49`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC49.2（2）；03_UCC_TX/R_TX_BLEED49.1（1）。 [完整端点N0302](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0302)。 |
| ARRAY | 03_UCC_TX | TX49 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX49.2→GND。

<a id="array-r-tx-bleed49"></a>

### 第254步：在ARRAY／03_UCC_TX放置 R_TX_BLEED49

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED49**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX49.1与TX49.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED49 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_49 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_49`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC49.2（2）；03_UCC_TX/TX49.1（PLUS）。 [完整端点N0302](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0302)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED49 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED49.1=`TXPLUS_49`，R_TX_BLEED49.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv25"></a>

### 第255步：在ARRAY／03_UCC_TX放置 U_DRV25

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV25**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV25 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV25 | UCC27624QDRQ1 | 2 | INA | TXLOG_50 | IN | 从此脚引线，标注精确网名`TXLOG_50`；跨页使用同名板内标签。同网还接：02_595/U_SR12.2（QC）；02_595/R_TX_PD50.1（1）。 [完整端点N0175](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0175)。 |
| ARRAY | 03_UCC_TX | U_DRV25 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV25 | UCC27624QDRQ1 | 4 | INB | TXLOG_51 | IN | 从此脚引线，标注精确网名`TXLOG_51`；跨页使用同名板内标签。同网还接：02_595/U_SR12.3（QD）；02_595/R_TX_PD51.1（1）。 [完整端点N0176](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0176)。 |
| ARRAY | 03_UCC_TX | U_DRV25 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_51 | OUT | 从此脚引线，标注精确网名`TXOUT_51`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX51.1（1）。 [完整端点N0240](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0240)。 |
| ARRAY | 03_UCC_TX | U_DRV25 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV25 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_50 | OUT | 从此脚引线，标注精确网名`TXOUT_50`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX50.1（1）。 [完整端点N0239](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0239)。 |
| ARRAY | 03_UCC_TX | U_DRV25 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV25.3→GND；U_DRV25.6→VTX。

<a id="array-c-u-drv25"></a>

### 第256步：在ARRAY／03_UCC_TX放置 C_U_DRV25

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV25**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV25的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV25 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV25 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV25.1=`VTX`，C_U_DRV25.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx50"></a>

### 第257步：在ARRAY／03_UCC_TX放置 R_TX50

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX50**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV25输出与C_TX_AC50之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX50 | CRCW2512150RFKEG | 1 | 1 | TXOUT_50 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_50`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV25.7（OUTA）。 [完整端点N0239](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0239)。 |
| ARRAY | 03_UCC_TX | R_TX50 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC50 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC50`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC50.1（1）。 [完整端点N0367](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0367)。 |

接完确认：R_TX50.1=`TXOUT_50`，R_TX50.2=`TX_AC_SRC50`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac50"></a>

### 第258步：在ARRAY／03_UCC_TX放置 C_TX_AC50

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC50**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX50之后、TX50之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC50 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC50 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC50`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX50.2（2）。 [完整端点N0367](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0367)。 |
| ARRAY | 03_UCC_TX | C_TX_AC50 | C1210C104J5GACTU | 2 | 2 | TXPLUS_50 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_50`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED50.1（1）；03_UCC_TX/TX50.1（PLUS）。 [完整端点N0303](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0303)。 |

接完确认：C_TX_AC50.1=`TX_AC_SRC50`，C_TX_AC50.2=`TXPLUS_50`；不可旁路该器件把两个网名短在一起。

<a id="array-tx50"></a>

### 第259步：在ARRAY／03_UCC_TX放置 TX50

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX50**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX50 | NU40C10T-2 | 1 | PLUS | TXPLUS_50 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_50`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC50.2（2）；03_UCC_TX/R_TX_BLEED50.1（1）。 [完整端点N0303](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0303)。 |
| ARRAY | 03_UCC_TX | TX50 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX50.2→GND。

<a id="array-r-tx-bleed50"></a>

### 第260步：在ARRAY／03_UCC_TX放置 R_TX_BLEED50

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED50**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX50.1与TX50.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED50 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_50 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_50`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC50.2（2）；03_UCC_TX/TX50.1（PLUS）。 [完整端点N0303](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0303)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED50 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED50.1=`TXPLUS_50`，R_TX_BLEED50.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx51"></a>

### 第261步：在ARRAY／03_UCC_TX放置 R_TX51

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX51**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV25输出与C_TX_AC51之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX51 | CRCW2512150RFKEG | 1 | 1 | TXOUT_51 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_51`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV25.5（OUTB）。 [完整端点N0240](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0240)。 |
| ARRAY | 03_UCC_TX | R_TX51 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC51 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC51`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC51.1（1）。 [完整端点N0368](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0368)。 |

接完确认：R_TX51.1=`TXOUT_51`，R_TX51.2=`TX_AC_SRC51`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac51"></a>

### 第262步：在ARRAY／03_UCC_TX放置 C_TX_AC51

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC51**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX51之后、TX51之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC51 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC51 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC51`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX51.2（2）。 [完整端点N0368](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0368)。 |
| ARRAY | 03_UCC_TX | C_TX_AC51 | C1210C104J5GACTU | 2 | 2 | TXPLUS_51 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_51`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED51.1（1）；03_UCC_TX/TX51.1（PLUS）。 [完整端点N0304](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0304)。 |

接完确认：C_TX_AC51.1=`TX_AC_SRC51`，C_TX_AC51.2=`TXPLUS_51`；不可旁路该器件把两个网名短在一起。

<a id="array-tx51"></a>

### 第263步：在ARRAY／03_UCC_TX放置 TX51

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX51**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX51 | NU40C10T-2 | 1 | PLUS | TXPLUS_51 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_51`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC51.2（2）；03_UCC_TX/R_TX_BLEED51.1（1）。 [完整端点N0304](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0304)。 |
| ARRAY | 03_UCC_TX | TX51 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX51.2→GND。

<a id="array-r-tx-bleed51"></a>

### 第264步：在ARRAY／03_UCC_TX放置 R_TX_BLEED51

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED51**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX51.1与TX51.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED51 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_51 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_51`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC51.2（2）；03_UCC_TX/TX51.1（PLUS）。 [完整端点N0304](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0304)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED51 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED51.1=`TXPLUS_51`，R_TX_BLEED51.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv26"></a>

### 第265步：在ARRAY／03_UCC_TX放置 U_DRV26

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV26**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV26 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV26 | UCC27624QDRQ1 | 2 | INA | TXLOG_52 | IN | 从此脚引线，标注精确网名`TXLOG_52`；跨页使用同名板内标签。同网还接：02_595/U_SR13.15（QA）；02_595/R_TX_PD52.1（1）。 [完整端点N0177](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0177)。 |
| ARRAY | 03_UCC_TX | U_DRV26 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV26 | UCC27624QDRQ1 | 4 | INB | TXLOG_53 | IN | 从此脚引线，标注精确网名`TXLOG_53`；跨页使用同名板内标签。同网还接：02_595/U_SR13.1（QB）；02_595/R_TX_PD53.1（1）。 [完整端点N0178](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0178)。 |
| ARRAY | 03_UCC_TX | U_DRV26 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_53 | OUT | 从此脚引线，标注精确网名`TXOUT_53`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX53.1（1）。 [完整端点N0242](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0242)。 |
| ARRAY | 03_UCC_TX | U_DRV26 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV26 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_52 | OUT | 从此脚引线，标注精确网名`TXOUT_52`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX52.1（1）。 [完整端点N0241](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0241)。 |
| ARRAY | 03_UCC_TX | U_DRV26 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV26.3→GND；U_DRV26.6→VTX。

<a id="array-c-u-drv26"></a>

### 第266步：在ARRAY／03_UCC_TX放置 C_U_DRV26

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV26**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV26的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV26 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV26 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV26.1=`VTX`，C_U_DRV26.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx52"></a>

### 第267步：在ARRAY／03_UCC_TX放置 R_TX52

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX52**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV26输出与C_TX_AC52之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX52 | CRCW2512150RFKEG | 1 | 1 | TXOUT_52 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_52`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV26.7（OUTA）。 [完整端点N0241](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0241)。 |
| ARRAY | 03_UCC_TX | R_TX52 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC52 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC52`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC52.1（1）。 [完整端点N0369](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0369)。 |

接完确认：R_TX52.1=`TXOUT_52`，R_TX52.2=`TX_AC_SRC52`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac52"></a>

### 第268步：在ARRAY／03_UCC_TX放置 C_TX_AC52

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC52**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX52之后、TX52之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC52 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC52 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC52`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX52.2（2）。 [完整端点N0369](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0369)。 |
| ARRAY | 03_UCC_TX | C_TX_AC52 | C1210C104J5GACTU | 2 | 2 | TXPLUS_52 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_52`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED52.1（1）；03_UCC_TX/TX52.1（PLUS）。 [完整端点N0305](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0305)。 |

接完确认：C_TX_AC52.1=`TX_AC_SRC52`，C_TX_AC52.2=`TXPLUS_52`；不可旁路该器件把两个网名短在一起。

<a id="array-tx52"></a>

### 第269步：在ARRAY／03_UCC_TX放置 TX52

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX52**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX52 | NU40C10T-2 | 1 | PLUS | TXPLUS_52 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_52`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC52.2（2）；03_UCC_TX/R_TX_BLEED52.1（1）。 [完整端点N0305](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0305)。 |
| ARRAY | 03_UCC_TX | TX52 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX52.2→GND。

<a id="array-r-tx-bleed52"></a>

### 第270步：在ARRAY／03_UCC_TX放置 R_TX_BLEED52

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED52**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX52.1与TX52.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED52 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_52 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_52`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC52.2（2）；03_UCC_TX/TX52.1（PLUS）。 [完整端点N0305](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0305)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED52 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED52.1=`TXPLUS_52`，R_TX_BLEED52.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx53"></a>

### 第271步：在ARRAY／03_UCC_TX放置 R_TX53

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX53**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV26输出与C_TX_AC53之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX53 | CRCW2512150RFKEG | 1 | 1 | TXOUT_53 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_53`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV26.5（OUTB）。 [完整端点N0242](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0242)。 |
| ARRAY | 03_UCC_TX | R_TX53 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC53 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC53`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC53.1（1）。 [完整端点N0370](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0370)。 |

接完确认：R_TX53.1=`TXOUT_53`，R_TX53.2=`TX_AC_SRC53`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac53"></a>

### 第272步：在ARRAY／03_UCC_TX放置 C_TX_AC53

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC53**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX53之后、TX53之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC53 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC53 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC53`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX53.2（2）。 [完整端点N0370](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0370)。 |
| ARRAY | 03_UCC_TX | C_TX_AC53 | C1210C104J5GACTU | 2 | 2 | TXPLUS_53 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_53`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED53.1（1）；03_UCC_TX/TX53.1（PLUS）。 [完整端点N0306](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0306)。 |

接完确认：C_TX_AC53.1=`TX_AC_SRC53`，C_TX_AC53.2=`TXPLUS_53`；不可旁路该器件把两个网名短在一起。

<a id="array-tx53"></a>

### 第273步：在ARRAY／03_UCC_TX放置 TX53

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX53**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX53 | NU40C10T-2 | 1 | PLUS | TXPLUS_53 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_53`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC53.2（2）；03_UCC_TX/R_TX_BLEED53.1（1）。 [完整端点N0306](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0306)。 |
| ARRAY | 03_UCC_TX | TX53 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX53.2→GND。

<a id="array-r-tx-bleed53"></a>

### 第274步：在ARRAY／03_UCC_TX放置 R_TX_BLEED53

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED53**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX53.1与TX53.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED53 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_53 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_53`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC53.2（2）；03_UCC_TX/TX53.1（PLUS）。 [完整端点N0306](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0306)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED53 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED53.1=`TXPLUS_53`，R_TX_BLEED53.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv27"></a>

### 第275步：在ARRAY／03_UCC_TX放置 U_DRV27

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV27**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV27 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV27 | UCC27624QDRQ1 | 2 | INA | TXLOG_54 | IN | 从此脚引线，标注精确网名`TXLOG_54`；跨页使用同名板内标签。同网还接：02_595/U_SR13.2（QC）；02_595/R_TX_PD54.1（1）。 [完整端点N0179](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0179)。 |
| ARRAY | 03_UCC_TX | U_DRV27 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV27 | UCC27624QDRQ1 | 4 | INB | TXLOG_55 | IN | 从此脚引线，标注精确网名`TXLOG_55`；跨页使用同名板内标签。同网还接：02_595/U_SR13.3（QD）；02_595/R_TX_PD55.1（1）。 [完整端点N0180](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0180)。 |
| ARRAY | 03_UCC_TX | U_DRV27 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_55 | OUT | 从此脚引线，标注精确网名`TXOUT_55`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX55.1（1）。 [完整端点N0244](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0244)。 |
| ARRAY | 03_UCC_TX | U_DRV27 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV27 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_54 | OUT | 从此脚引线，标注精确网名`TXOUT_54`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX54.1（1）。 [完整端点N0243](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0243)。 |
| ARRAY | 03_UCC_TX | U_DRV27 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV27.3→GND；U_DRV27.6→VTX。

<a id="array-c-u-drv27"></a>

### 第276步：在ARRAY／03_UCC_TX放置 C_U_DRV27

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV27**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV27的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV27 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV27 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV27.1=`VTX`，C_U_DRV27.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx54"></a>

### 第277步：在ARRAY／03_UCC_TX放置 R_TX54

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX54**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV27输出与C_TX_AC54之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX54 | CRCW2512150RFKEG | 1 | 1 | TXOUT_54 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_54`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV27.7（OUTA）。 [完整端点N0243](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0243)。 |
| ARRAY | 03_UCC_TX | R_TX54 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC54 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC54`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC54.1（1）。 [完整端点N0371](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0371)。 |

接完确认：R_TX54.1=`TXOUT_54`，R_TX54.2=`TX_AC_SRC54`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac54"></a>

### 第278步：在ARRAY／03_UCC_TX放置 C_TX_AC54

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC54**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX54之后、TX54之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC54 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC54 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC54`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX54.2（2）。 [完整端点N0371](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0371)。 |
| ARRAY | 03_UCC_TX | C_TX_AC54 | C1210C104J5GACTU | 2 | 2 | TXPLUS_54 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_54`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED54.1（1）；03_UCC_TX/TX54.1（PLUS）。 [完整端点N0307](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0307)。 |

接完确认：C_TX_AC54.1=`TX_AC_SRC54`，C_TX_AC54.2=`TXPLUS_54`；不可旁路该器件把两个网名短在一起。

<a id="array-tx54"></a>

### 第279步：在ARRAY／03_UCC_TX放置 TX54

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX54**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX54 | NU40C10T-2 | 1 | PLUS | TXPLUS_54 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_54`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC54.2（2）；03_UCC_TX/R_TX_BLEED54.1（1）。 [完整端点N0307](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0307)。 |
| ARRAY | 03_UCC_TX | TX54 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX54.2→GND。

<a id="array-r-tx-bleed54"></a>

### 第280步：在ARRAY／03_UCC_TX放置 R_TX_BLEED54

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED54**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX54.1与TX54.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED54 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_54 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_54`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC54.2（2）；03_UCC_TX/TX54.1（PLUS）。 [完整端点N0307](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0307)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED54 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED54.1=`TXPLUS_54`，R_TX_BLEED54.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx55"></a>

### 第281步：在ARRAY／03_UCC_TX放置 R_TX55

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX55**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV27输出与C_TX_AC55之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX55 | CRCW2512150RFKEG | 1 | 1 | TXOUT_55 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_55`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV27.5（OUTB）。 [完整端点N0244](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0244)。 |
| ARRAY | 03_UCC_TX | R_TX55 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC55 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC55`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC55.1（1）。 [完整端点N0372](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0372)。 |

接完确认：R_TX55.1=`TXOUT_55`，R_TX55.2=`TX_AC_SRC55`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac55"></a>

### 第282步：在ARRAY／03_UCC_TX放置 C_TX_AC55

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC55**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX55之后、TX55之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC55 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC55 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC55`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX55.2（2）。 [完整端点N0372](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0372)。 |
| ARRAY | 03_UCC_TX | C_TX_AC55 | C1210C104J5GACTU | 2 | 2 | TXPLUS_55 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_55`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED55.1（1）；03_UCC_TX/TX55.1（PLUS）。 [完整端点N0308](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0308)。 |

接完确认：C_TX_AC55.1=`TX_AC_SRC55`，C_TX_AC55.2=`TXPLUS_55`；不可旁路该器件把两个网名短在一起。

<a id="array-tx55"></a>

### 第283步：在ARRAY／03_UCC_TX放置 TX55

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX55**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX55 | NU40C10T-2 | 1 | PLUS | TXPLUS_55 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_55`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC55.2（2）；03_UCC_TX/R_TX_BLEED55.1（1）。 [完整端点N0308](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0308)。 |
| ARRAY | 03_UCC_TX | TX55 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX55.2→GND。

<a id="array-r-tx-bleed55"></a>

### 第284步：在ARRAY／03_UCC_TX放置 R_TX_BLEED55

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED55**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX55.1与TX55.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED55 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_55 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_55`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC55.2（2）；03_UCC_TX/TX55.1（PLUS）。 [完整端点N0308](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0308)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED55 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED55.1=`TXPLUS_55`，R_TX_BLEED55.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv28"></a>

### 第285步：在ARRAY／03_UCC_TX放置 U_DRV28

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV28**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV28 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV28 | UCC27624QDRQ1 | 2 | INA | TXLOG_56 | IN | 从此脚引线，标注精确网名`TXLOG_56`；跨页使用同名板内标签。同网还接：02_595/U_SR14.15（QA）；02_595/R_TX_PD56.1（1）。 [完整端点N0181](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0181)。 |
| ARRAY | 03_UCC_TX | U_DRV28 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV28 | UCC27624QDRQ1 | 4 | INB | TXLOG_57 | IN | 从此脚引线，标注精确网名`TXLOG_57`；跨页使用同名板内标签。同网还接：02_595/U_SR14.1（QB）；02_595/R_TX_PD57.1（1）。 [完整端点N0182](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0182)。 |
| ARRAY | 03_UCC_TX | U_DRV28 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_57 | OUT | 从此脚引线，标注精确网名`TXOUT_57`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX57.1（1）。 [完整端点N0246](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0246)。 |
| ARRAY | 03_UCC_TX | U_DRV28 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV28 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_56 | OUT | 从此脚引线，标注精确网名`TXOUT_56`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX56.1（1）。 [完整端点N0245](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0245)。 |
| ARRAY | 03_UCC_TX | U_DRV28 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV28.3→GND；U_DRV28.6→VTX。

<a id="array-c-u-drv28"></a>

### 第286步：在ARRAY／03_UCC_TX放置 C_U_DRV28

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV28**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV28的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV28 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV28 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV28.1=`VTX`，C_U_DRV28.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx56"></a>

### 第287步：在ARRAY／03_UCC_TX放置 R_TX56

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX56**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV28输出与C_TX_AC56之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX56 | CRCW2512150RFKEG | 1 | 1 | TXOUT_56 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_56`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV28.7（OUTA）。 [完整端点N0245](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0245)。 |
| ARRAY | 03_UCC_TX | R_TX56 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC56 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC56`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC56.1（1）。 [完整端点N0373](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0373)。 |

接完确认：R_TX56.1=`TXOUT_56`，R_TX56.2=`TX_AC_SRC56`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac56"></a>

### 第288步：在ARRAY／03_UCC_TX放置 C_TX_AC56

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC56**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX56之后、TX56之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC56 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC56 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC56`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX56.2（2）。 [完整端点N0373](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0373)。 |
| ARRAY | 03_UCC_TX | C_TX_AC56 | C1210C104J5GACTU | 2 | 2 | TXPLUS_56 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_56`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED56.1（1）；03_UCC_TX/TX56.1（PLUS）。 [完整端点N0309](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0309)。 |

接完确认：C_TX_AC56.1=`TX_AC_SRC56`，C_TX_AC56.2=`TXPLUS_56`；不可旁路该器件把两个网名短在一起。

<a id="array-tx56"></a>

### 第289步：在ARRAY／03_UCC_TX放置 TX56

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX56**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX56 | NU40C10T-2 | 1 | PLUS | TXPLUS_56 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_56`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC56.2（2）；03_UCC_TX/R_TX_BLEED56.1（1）。 [完整端点N0309](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0309)。 |
| ARRAY | 03_UCC_TX | TX56 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX56.2→GND。

<a id="array-r-tx-bleed56"></a>

### 第290步：在ARRAY／03_UCC_TX放置 R_TX_BLEED56

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED56**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX56.1与TX56.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED56 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_56 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_56`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC56.2（2）；03_UCC_TX/TX56.1（PLUS）。 [完整端点N0309](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0309)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED56 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED56.1=`TXPLUS_56`，R_TX_BLEED56.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx57"></a>

### 第291步：在ARRAY／03_UCC_TX放置 R_TX57

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX57**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV28输出与C_TX_AC57之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX57 | CRCW2512150RFKEG | 1 | 1 | TXOUT_57 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_57`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV28.5（OUTB）。 [完整端点N0246](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0246)。 |
| ARRAY | 03_UCC_TX | R_TX57 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC57 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC57`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC57.1（1）。 [完整端点N0374](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0374)。 |

接完确认：R_TX57.1=`TXOUT_57`，R_TX57.2=`TX_AC_SRC57`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac57"></a>

### 第292步：在ARRAY／03_UCC_TX放置 C_TX_AC57

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC57**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX57之后、TX57之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC57 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC57 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC57`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX57.2（2）。 [完整端点N0374](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0374)。 |
| ARRAY | 03_UCC_TX | C_TX_AC57 | C1210C104J5GACTU | 2 | 2 | TXPLUS_57 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_57`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED57.1（1）；03_UCC_TX/TX57.1（PLUS）。 [完整端点N0310](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0310)。 |

接完确认：C_TX_AC57.1=`TX_AC_SRC57`，C_TX_AC57.2=`TXPLUS_57`；不可旁路该器件把两个网名短在一起。

<a id="array-tx57"></a>

### 第293步：在ARRAY／03_UCC_TX放置 TX57

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX57**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX57 | NU40C10T-2 | 1 | PLUS | TXPLUS_57 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_57`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC57.2（2）；03_UCC_TX/R_TX_BLEED57.1（1）。 [完整端点N0310](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0310)。 |
| ARRAY | 03_UCC_TX | TX57 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX57.2→GND。

<a id="array-r-tx-bleed57"></a>

### 第294步：在ARRAY／03_UCC_TX放置 R_TX_BLEED57

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED57**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX57.1与TX57.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED57 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_57 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_57`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC57.2（2）；03_UCC_TX/TX57.1（PLUS）。 [完整端点N0310](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0310)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED57 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED57.1=`TXPLUS_57`，R_TX_BLEED57.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv29"></a>

### 第295步：在ARRAY／03_UCC_TX放置 U_DRV29

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV29**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV29 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV29 | UCC27624QDRQ1 | 2 | INA | TXLOG_58 | IN | 从此脚引线，标注精确网名`TXLOG_58`；跨页使用同名板内标签。同网还接：02_595/U_SR14.2（QC）；02_595/R_TX_PD58.1（1）。 [完整端点N0183](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0183)。 |
| ARRAY | 03_UCC_TX | U_DRV29 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV29 | UCC27624QDRQ1 | 4 | INB | TXLOG_59 | IN | 从此脚引线，标注精确网名`TXLOG_59`；跨页使用同名板内标签。同网还接：02_595/U_SR14.3（QD）；02_595/R_TX_PD59.1（1）。 [完整端点N0184](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0184)。 |
| ARRAY | 03_UCC_TX | U_DRV29 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_59 | OUT | 从此脚引线，标注精确网名`TXOUT_59`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX59.1（1）。 [完整端点N0248](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0248)。 |
| ARRAY | 03_UCC_TX | U_DRV29 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV29 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_58 | OUT | 从此脚引线，标注精确网名`TXOUT_58`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX58.1（1）。 [完整端点N0247](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0247)。 |
| ARRAY | 03_UCC_TX | U_DRV29 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV29.3→GND；U_DRV29.6→VTX。

<a id="array-c-u-drv29"></a>

### 第296步：在ARRAY／03_UCC_TX放置 C_U_DRV29

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV29**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV29的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV29 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV29 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV29.1=`VTX`，C_U_DRV29.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx58"></a>

### 第297步：在ARRAY／03_UCC_TX放置 R_TX58

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX58**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV29输出与C_TX_AC58之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX58 | CRCW2512150RFKEG | 1 | 1 | TXOUT_58 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_58`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV29.7（OUTA）。 [完整端点N0247](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0247)。 |
| ARRAY | 03_UCC_TX | R_TX58 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC58 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC58`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC58.1（1）。 [完整端点N0375](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0375)。 |

接完确认：R_TX58.1=`TXOUT_58`，R_TX58.2=`TX_AC_SRC58`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac58"></a>

### 第298步：在ARRAY／03_UCC_TX放置 C_TX_AC58

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC58**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX58之后、TX58之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC58 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC58 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC58`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX58.2（2）。 [完整端点N0375](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0375)。 |
| ARRAY | 03_UCC_TX | C_TX_AC58 | C1210C104J5GACTU | 2 | 2 | TXPLUS_58 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_58`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED58.1（1）；03_UCC_TX/TX58.1（PLUS）。 [完整端点N0311](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0311)。 |

接完确认：C_TX_AC58.1=`TX_AC_SRC58`，C_TX_AC58.2=`TXPLUS_58`；不可旁路该器件把两个网名短在一起。

<a id="array-tx58"></a>

### 第299步：在ARRAY／03_UCC_TX放置 TX58

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX58**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX58 | NU40C10T-2 | 1 | PLUS | TXPLUS_58 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_58`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC58.2（2）；03_UCC_TX/R_TX_BLEED58.1（1）。 [完整端点N0311](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0311)。 |
| ARRAY | 03_UCC_TX | TX58 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX58.2→GND。

<a id="array-r-tx-bleed58"></a>

### 第300步：在ARRAY／03_UCC_TX放置 R_TX_BLEED58

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED58**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX58.1与TX58.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED58 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_58 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_58`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC58.2（2）；03_UCC_TX/TX58.1（PLUS）。 [完整端点N0311](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0311)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED58 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED58.1=`TXPLUS_58`，R_TX_BLEED58.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx59"></a>

### 第301步：在ARRAY／03_UCC_TX放置 R_TX59

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX59**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV29输出与C_TX_AC59之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX59 | CRCW2512150RFKEG | 1 | 1 | TXOUT_59 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_59`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV29.5（OUTB）。 [完整端点N0248](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0248)。 |
| ARRAY | 03_UCC_TX | R_TX59 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC59 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC59`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC59.1（1）。 [完整端点N0376](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0376)。 |

接完确认：R_TX59.1=`TXOUT_59`，R_TX59.2=`TX_AC_SRC59`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac59"></a>

### 第302步：在ARRAY／03_UCC_TX放置 C_TX_AC59

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC59**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX59之后、TX59之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC59 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC59 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC59`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX59.2（2）。 [完整端点N0376](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0376)。 |
| ARRAY | 03_UCC_TX | C_TX_AC59 | C1210C104J5GACTU | 2 | 2 | TXPLUS_59 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_59`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED59.1（1）；03_UCC_TX/TX59.1（PLUS）。 [完整端点N0312](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0312)。 |

接完确认：C_TX_AC59.1=`TX_AC_SRC59`，C_TX_AC59.2=`TXPLUS_59`；不可旁路该器件把两个网名短在一起。

<a id="array-tx59"></a>

### 第303步：在ARRAY／03_UCC_TX放置 TX59

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX59**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX59 | NU40C10T-2 | 1 | PLUS | TXPLUS_59 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_59`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC59.2（2）；03_UCC_TX/R_TX_BLEED59.1（1）。 [完整端点N0312](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0312)。 |
| ARRAY | 03_UCC_TX | TX59 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX59.2→GND。

<a id="array-r-tx-bleed59"></a>

### 第304步：在ARRAY／03_UCC_TX放置 R_TX_BLEED59

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED59**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX59.1与TX59.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED59 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_59 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_59`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC59.2（2）；03_UCC_TX/TX59.1（PLUS）。 [完整端点N0312](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0312)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED59 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED59.1=`TXPLUS_59`，R_TX_BLEED59.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv30"></a>

### 第305步：在ARRAY／03_UCC_TX放置 U_DRV30

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV30**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV30 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV30 | UCC27624QDRQ1 | 2 | INA | TXLOG_60 | IN | 从此脚引线，标注精确网名`TXLOG_60`；跨页使用同名板内标签。同网还接：02_595/U_SR15.15（QA）；02_595/R_TX_PD60.1（1）。 [完整端点N0185](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0185)。 |
| ARRAY | 03_UCC_TX | U_DRV30 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV30 | UCC27624QDRQ1 | 4 | INB | TXLOG_61 | IN | 从此脚引线，标注精确网名`TXLOG_61`；跨页使用同名板内标签。同网还接：02_595/U_SR15.1（QB）；02_595/R_TX_PD61.1（1）。 [完整端点N0186](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0186)。 |
| ARRAY | 03_UCC_TX | U_DRV30 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_61 | OUT | 从此脚引线，标注精确网名`TXOUT_61`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX61.1（1）。 [完整端点N0250](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0250)。 |
| ARRAY | 03_UCC_TX | U_DRV30 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV30 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_60 | OUT | 从此脚引线，标注精确网名`TXOUT_60`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX60.1（1）。 [完整端点N0249](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0249)。 |
| ARRAY | 03_UCC_TX | U_DRV30 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV30.3→GND；U_DRV30.6→VTX。

<a id="array-c-u-drv30"></a>

### 第306步：在ARRAY／03_UCC_TX放置 C_U_DRV30

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV30**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV30的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV30 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV30 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV30.1=`VTX`，C_U_DRV30.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx60"></a>

### 第307步：在ARRAY／03_UCC_TX放置 R_TX60

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX60**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV30输出与C_TX_AC60之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX60 | CRCW2512150RFKEG | 1 | 1 | TXOUT_60 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_60`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV30.7（OUTA）。 [完整端点N0249](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0249)。 |
| ARRAY | 03_UCC_TX | R_TX60 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC60 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC60`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC60.1（1）。 [完整端点N0377](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0377)。 |

接完确认：R_TX60.1=`TXOUT_60`，R_TX60.2=`TX_AC_SRC60`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac60"></a>

### 第308步：在ARRAY／03_UCC_TX放置 C_TX_AC60

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC60**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX60之后、TX60之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC60 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC60 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC60`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX60.2（2）。 [完整端点N0377](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0377)。 |
| ARRAY | 03_UCC_TX | C_TX_AC60 | C1210C104J5GACTU | 2 | 2 | TXPLUS_60 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_60`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED60.1（1）；03_UCC_TX/TX60.1（PLUS）。 [完整端点N0313](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0313)。 |

接完确认：C_TX_AC60.1=`TX_AC_SRC60`，C_TX_AC60.2=`TXPLUS_60`；不可旁路该器件把两个网名短在一起。

<a id="array-tx60"></a>

### 第309步：在ARRAY／03_UCC_TX放置 TX60

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX60**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX60 | NU40C10T-2 | 1 | PLUS | TXPLUS_60 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_60`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC60.2（2）；03_UCC_TX/R_TX_BLEED60.1（1）。 [完整端点N0313](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0313)。 |
| ARRAY | 03_UCC_TX | TX60 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX60.2→GND。

<a id="array-r-tx-bleed60"></a>

### 第310步：在ARRAY／03_UCC_TX放置 R_TX_BLEED60

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED60**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX60.1与TX60.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED60 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_60 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_60`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC60.2（2）；03_UCC_TX/TX60.1（PLUS）。 [完整端点N0313](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0313)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED60 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED60.1=`TXPLUS_60`，R_TX_BLEED60.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx61"></a>

### 第311步：在ARRAY／03_UCC_TX放置 R_TX61

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX61**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV30输出与C_TX_AC61之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX61 | CRCW2512150RFKEG | 1 | 1 | TXOUT_61 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_61`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV30.5（OUTB）。 [完整端点N0250](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0250)。 |
| ARRAY | 03_UCC_TX | R_TX61 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC61 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC61`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC61.1（1）。 [完整端点N0378](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0378)。 |

接完确认：R_TX61.1=`TXOUT_61`，R_TX61.2=`TX_AC_SRC61`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac61"></a>

### 第312步：在ARRAY／03_UCC_TX放置 C_TX_AC61

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC61**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX61之后、TX61之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC61 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC61 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC61`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX61.2（2）。 [完整端点N0378](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0378)。 |
| ARRAY | 03_UCC_TX | C_TX_AC61 | C1210C104J5GACTU | 2 | 2 | TXPLUS_61 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_61`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED61.1（1）；03_UCC_TX/TX61.1（PLUS）。 [完整端点N0314](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0314)。 |

接完确认：C_TX_AC61.1=`TX_AC_SRC61`，C_TX_AC61.2=`TXPLUS_61`；不可旁路该器件把两个网名短在一起。

<a id="array-tx61"></a>

### 第313步：在ARRAY／03_UCC_TX放置 TX61

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX61**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX61 | NU40C10T-2 | 1 | PLUS | TXPLUS_61 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_61`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC61.2（2）；03_UCC_TX/R_TX_BLEED61.1（1）。 [完整端点N0314](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0314)。 |
| ARRAY | 03_UCC_TX | TX61 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX61.2→GND。

<a id="array-r-tx-bleed61"></a>

### 第314步：在ARRAY／03_UCC_TX放置 R_TX_BLEED61

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED61**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX61.1与TX61.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED61 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_61 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_61`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC61.2（2）；03_UCC_TX/TX61.1（PLUS）。 [完整端点N0314](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0314)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED61 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED61.1=`TXPLUS_61`，R_TX_BLEED61.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-drv31"></a>

### 第315步：在ARRAY／03_UCC_TX放置 U_DRV31

在 **ARRAY板的03_UCC_TX图页**，接着放置 **U_DRV31**，精确型号 **UCC27624QDRQ1**，封装 **D/SOIC8**。

放在对应两路TX支路左侧。精确D/SOIC8，无EP；VDD6接VTX，GND3接GND，ENA1/ENB8均接DRIVER_EN_G0。每个OUT按下表连接自己的150Ω支路。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | U_DRV31 | UCC27624QDRQ1 | 1 | ENA | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 03_UCC_TX | U_DRV31 | UCC27624QDRQ1 | 2 | INA | TXLOG_62 | IN | 从此脚引线，标注精确网名`TXLOG_62`；跨页使用同名板内标签。同网还接：02_595/U_SR15.2（QC）；02_595/R_TX_PD62.1（1）。 [完整端点N0187](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0187)。 |
| ARRAY | 03_UCC_TX | U_DRV31 | UCC27624QDRQ1 | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 03_UCC_TX | U_DRV31 | UCC27624QDRQ1 | 4 | INB | TXLOG_63 | IN | 从此脚引线，标注精确网名`TXLOG_63`；跨页使用同名板内标签。同网还接：02_595/U_SR15.3（QD）；02_595/R_TX_PD63.1（1）。 [完整端点N0188](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0188)。 |
| ARRAY | 03_UCC_TX | U_DRV31 | UCC27624QDRQ1 | 5 | OUTB | TXOUT_63 | OUT | 从此脚引线，标注精确网名`TXOUT_63`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX63.1（1）。 [完整端点N0252](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0252)。 |
| ARRAY | 03_UCC_TX | U_DRV31 | UCC27624QDRQ1 | 6 | VDD | VTX | POWER | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | U_DRV31 | UCC27624QDRQ1 | 7 | OUTA | TXOUT_62 | OUT | 从此脚引线，标注精确网名`TXOUT_62`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX62.1（1）。 [完整端点N0251](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0251)。 |
| ARRAY | 03_UCC_TX | U_DRV31 | UCC27624QDRQ1 | 8 | ENB | DRIVER_EN_G0 | IN | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为U_DRV31.3→GND；U_DRV31.6→VTX。

<a id="array-c-u-drv31"></a>

### 第316步：在ARRAY／03_UCC_TX放置 C_U_DRV31

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_U_DRV31**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_DRV31的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_U_DRV31 | C0603C104K5RACTU | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 03_UCC_TX | C_U_DRV31 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_DRV31.1=`VTX`，C_U_DRV31.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx62"></a>

### 第317步：在ARRAY／03_UCC_TX放置 R_TX62

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX62**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV31输出与C_TX_AC62之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX62 | CRCW2512150RFKEG | 1 | 1 | TXOUT_62 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_62`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV31.7（OUTA）。 [完整端点N0251](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0251)。 |
| ARRAY | 03_UCC_TX | R_TX62 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC62 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC62`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC62.1（1）。 [完整端点N0379](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0379)。 |

接完确认：R_TX62.1=`TXOUT_62`，R_TX62.2=`TX_AC_SRC62`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac62"></a>

### 第318步：在ARRAY／03_UCC_TX放置 C_TX_AC62

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC62**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX62之后、TX62之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC62 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC62 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC62`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX62.2（2）。 [完整端点N0379](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0379)。 |
| ARRAY | 03_UCC_TX | C_TX_AC62 | C1210C104J5GACTU | 2 | 2 | TXPLUS_62 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_62`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED62.1（1）；03_UCC_TX/TX62.1（PLUS）。 [完整端点N0315](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0315)。 |

接完确认：C_TX_AC62.1=`TX_AC_SRC62`，C_TX_AC62.2=`TXPLUS_62`；不可旁路该器件把两个网名短在一起。

<a id="array-tx62"></a>

### 第319步：在ARRAY／03_UCC_TX放置 TX62

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX62**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX62 | NU40C10T-2 | 1 | PLUS | TXPLUS_62 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_62`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC62.2（2）；03_UCC_TX/R_TX_BLEED62.1（1）。 [完整端点N0315](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0315)。 |
| ARRAY | 03_UCC_TX | TX62 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX62.2→GND。

<a id="array-r-tx-bleed62"></a>

### 第320步：在ARRAY／03_UCC_TX放置 R_TX_BLEED62

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED62**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX62.1与TX62.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED62 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_62 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_62`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC62.2（2）；03_UCC_TX/TX62.1（PLUS）。 [完整端点N0315](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0315)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED62 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED62.1=`TXPLUS_62`，R_TX_BLEED62.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-tx63"></a>

### 第321步：在ARRAY／03_UCC_TX放置 R_TX63

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX63**，精确型号 **CRCW2512150RFKEG**，封装 **2512**。其值为 **150**。

纸面位置：本通道U_DRV31输出与C_TX_AC63之间。额定条件：1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX63 | CRCW2512150RFKEG | 1 | 1 | TXOUT_63 | PASSIVE | 从此脚引线，标注精确网名`TXOUT_63`；跨页使用同名板内标签。同网还接：03_UCC_TX/U_DRV31.5（OUTB）。 [完整端点N0252](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0252)。 |
| ARRAY | 03_UCC_TX | R_TX63 | CRCW2512150RFKEG | 2 | 2 | TX_AC_SRC63 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC63`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC63.1（1）。 [完整端点N0380](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0380)。 |

接完确认：R_TX63.1=`TXOUT_63`，R_TX63.2=`TX_AC_SRC63`；不可旁路该器件把两个网名短在一起。

<a id="array-c-tx-ac63"></a>

### 第322步：在ARRAY／03_UCC_TX放置 C_TX_AC63

在 **ARRAY板的03_UCC_TX图页**，接着放置 **C_TX_AC63**，精确型号 **C1210C104J5GACTU**，封装 **1210**。其值为 **100nF**。

纸面位置：R_TX63之后、TX63之前，作为串联隔直元件。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | C_TX_AC63 | C1210C104J5GACTU | 1 | 1 | TX_AC_SRC63 | PASSIVE | 从此脚引线，标注精确网名`TX_AC_SRC63`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX63.2（2）。 [完整端点N0380](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0380)。 |
| ARRAY | 03_UCC_TX | C_TX_AC63 | C1210C104J5GACTU | 2 | 2 | TXPLUS_63 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_63`；跨页使用同名板内标签。同网还接：03_UCC_TX/R_TX_BLEED63.1（1）；03_UCC_TX/TX63.1（PLUS）。 [完整端点N0316](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0316)。 |

接完确认：C_TX_AC63.1=`TX_AC_SRC63`，C_TX_AC63.2=`TXPLUS_63`；不可旁路该器件把两个网名短在一起。

<a id="array-tx63"></a>

### 第323步：在ARRAY／03_UCC_TX放置 TX63

在 **ARRAY板的03_UCC_TX图页**，接着放置 **TX63**，精确型号 **NU40C10T-2**，封装 **manufacturer 10mm can, 12mm pitch target**。

放在本通道150Ω串联电阻及100nF串联隔直电容之后；1脚接TX_AC，2脚接GND，1M泄放跨换能器两端，连续端电压设计限制<20Vpp。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | TX63 | NU40C10T-2 | 1 | PLUS | TXPLUS_63 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_63`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC63.2（2）；03_UCC_TX/R_TX_BLEED63.1（1）。 [完整端点N0316](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0316)。 |
| ARRAY | 03_UCC_TX | TX63 | NU40C10T-2 | 2 | MINUS | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为TX63.2→GND。

<a id="array-r-tx-bleed63"></a>

### 第324步：在ARRAY／03_UCC_TX放置 R_TX_BLEED63

在 **ARRAY板的03_UCC_TX图页**，接着放置 **R_TX_BLEED63**，精确型号 **CRCW06031M00FKEA**，封装 **0603**。其值为 **1M**。

纸面位置：跨TX63.1与TX63.2的并联位置。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 03_UCC_TX | R_TX_BLEED63 | CRCW06031M00FKEA | 1 | 1 | TXPLUS_63 | PASSIVE | 从此脚引线，标注精确网名`TXPLUS_63`；跨页使用同名板内标签。同网还接：03_UCC_TX/C_TX_AC63.2（2）；03_UCC_TX/TX63.1（PLUS）。 [完整端点N0316](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0316)。 |
| ARRAY | 03_UCC_TX | R_TX_BLEED63 | CRCW06031M00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_TX_BLEED63.1=`TXPLUS_63`，R_TX_BLEED63.2=`GND`；不可旁路该器件把两个网名短在一起。

本页完成核对：**324个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。
