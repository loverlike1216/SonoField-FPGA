# ARRAY／05_SAFETY_TEMP逐步连接分册

本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。

<a id="page-array-05-safety-temp"></a>

## ARRAY板／05_SAFETY_TEMP图页

先放两路时钟二分频与独立单稳，再放许可/ARM逻辑和默认EN夹低晶体管，最后放故障上报和I2C温度。故障RC只滤报告，不串进本地EN关断。

<a id="array-u-oeinv"></a>

### 第001步：在ARRAY／05_SAFETY_TEMP放置 U_OEINV

在 **ARRAY板的05_SAFETY_TEMP图页**，先放置 **U_OEINV**，精确型号 **SN74LVC1G14DBVR**，封装 **DBV/SOT23-5**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_OEINV | SN74LVC1G14DBVR | 1 | NC | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| ARRAY | 05_SAFETY_TEMP | U_OEINV | SN74LVC1G14DBVR | 2 | A | OE_N | IN | 从此脚引线，标注精确网名`OE_N`；跨页使用同名板内标签。同网另有18个物理端点，逐个见[完整端点N0068](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0068)；例如01_LINK_BUFFERS/J_LINK.37（OE_N）；01_LINK_BUFFERS/R_DEF_OE_N.1（1）；02_595/U_SR00.13（OE_N）。 |
| ARRAY | 05_SAFETY_TEMP | U_OEINV | SN74LVC1G14DBVR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_OEINV | SN74LVC1G14DBVR | 4 | Y | OUTPUT_REQUEST | OUT | 从此脚引线，标注精确网名`OUTPUT_REQUEST`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G3.6（2B）。 [完整端点N0069](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0069)。 |
| ARRAY | 05_SAFETY_TEMP | U_OEINV | SN74LVC1G14DBVR | 5 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_OEINV.3→GND；U_OEINV.5→V3V3。 NC脚1逐个单独标记。

<a id="array-c-u-oeinv"></a>

### 第002步：在ARRAY／05_SAFETY_TEMP放置 C_U_OEINV

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_OEINV**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_OEINV的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_OEINV | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_OEINV | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_OEINV.1=`V3V3`，C_U_OEINV.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-wdiv-srclk"></a>

### 第003步：在ARRAY／05_SAFETY_TEMP放置 U_WDIV_SRCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_WDIV_SRCLK**，精确型号 **SN74LVC1G74DCUR**，封装 **DCU/VSSOP8**。

放在对应SRCLK/RCLK监测线上；74LVC1G74的D与反相输出构成二分频，PRE/CLR按表，不能用HB取代两路时钟监测。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_SRCLK | SN74LVC1G74DCUR | 1 | CLK | SRCLK_G0 | IN | 从此脚引线，标注精确网名`SRCLK_G0`；跨页使用同名板内标签。同网还接：02_595/U_SR00.11（SRCLK）；02_595/U_SR01.11（SRCLK）；02_595/U_SR02.11（SRCLK）；02_595/U_SR03.11（SRCLK）；01_LINK_BUFFERS/R_CLK_SRCLK0.2（2）。 [完整端点N0118](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0118)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_SRCLK | SN74LVC1G74DCUR | 2 | D | SRCLK_DIV_N | IN | 从此脚引线，标注精确网名`SRCLK_DIV_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDIV_SRCLK.3（Q_N）。 [完整端点N0117](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0117)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_SRCLK | SN74LVC1G74DCUR | 3 | Q_N | SRCLK_DIV_N | OUT | 从此脚引线，标注精确网名`SRCLK_DIV_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDIV_SRCLK.2（D）。 [完整端点N0117](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0117)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_SRCLK | SN74LVC1G74DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_SRCLK | SN74LVC1G74DCUR | 5 | Q | SRCLK_DIV | OUT | 从此脚引线，标注精确网名`SRCLK_DIV`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WD_SRCLK.1（TRIG）。 [完整端点N0116](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0116)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_SRCLK | SN74LVC1G74DCUR | 6 | CLR_N | POR_N | IN | 从此脚引线，标注精确网名`POR_N`；跨页使用同名板内标签。同网另有20个物理端点，逐个见[完整端点N0072](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0072)；例如02_595/U_SR00.10（SRCLR_N）；02_595/U_SR01.10（SRCLR_N）；02_595/U_SR02.10（SRCLR_N）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_SRCLK | SN74LVC1G74DCUR | 7 | PRE_N | V3V3 | IN | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_SRCLK | SN74LVC1G74DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_WDIV_SRCLK.4→GND；U_WDIV_SRCLK.7→V3V3；U_WDIV_SRCLK.8→V3V3。

<a id="array-c-u-wdiv-srclk"></a>

### 第004步：在ARRAY／05_SAFETY_TEMP放置 C_U_WDIV_SRCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_WDIV_SRCLK**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_WDIV_SRCLK的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_WDIV_SRCLK | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_WDIV_SRCLK | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_WDIV_SRCLK.1=`V3V3`，C_U_WDIV_SRCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-wd-srclk"></a>

### 第005步：在ARRAY／05_SAFETY_TEMP放置 U_WD_SRCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_WD_SRCLK**，精确型号 **LTC6993IS6-2#TRMPBF**，封装 **S6/TSOT23-6**。

放在对应时钟二分频器右侧；LTC6993IS6-2的1TRIG/2GND/3SET/4DIV/5V+/6OUT逐脚照表，RSET=100k，DIV接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_WD_SRCLK | LTC6993IS6-2#TRMPBF | 1 | TRIG | SRCLK_DIV | IN | 从此脚引线，标注精确网名`SRCLK_DIV`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDIV_SRCLK.5（Q）。 [完整端点N0116](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0116)。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_SRCLK | LTC6993IS6-2#TRMPBF | 2 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_SRCLK | LTC6993IS6-2#TRMPBF | 3 | SET | SRCLK_SET | IN | 从此脚引线，标注精确网名`SRCLK_SET`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_WD_SRCLK.1（1）。 [完整端点N0122](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0122)。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_SRCLK | LTC6993IS6-2#TRMPBF | 4 | DIV | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_SRCLK | LTC6993IS6-2#TRMPBF | 5 | V+ | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_SRCLK | LTC6993IS6-2#TRMPBF | 6 | OUT | SRCLK_ALIVE | OUT | 从此脚引线，标注精确网名`SRCLK_ALIVE`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDAND.1（A1）。 [完整端点N0111](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0111)。 |

接完确认：电源/地/参考为U_WD_SRCLK.2→GND；U_WD_SRCLK.4→GND；U_WD_SRCLK.5→V3V3。

<a id="array-c-u-wd-srclk"></a>

### 第006步：在ARRAY／05_SAFETY_TEMP放置 C_U_WD_SRCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_WD_SRCLK**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_WD_SRCLK的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_WD_SRCLK | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_WD_SRCLK | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_WD_SRCLK.1=`V3V3`，C_U_WD_SRCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-wd-srclk"></a>

### 第007步：在ARRAY／05_SAFETY_TEMP放置 R_WD_SRCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_WD_SRCLK**，精确型号 **RC0603FR-07100KL**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_WD_SRCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_WD_SRCLK | RC0603FR-07100KL | 1 | 1 | SRCLK_SET | PASSIVE | 从此脚引线，标注精确网名`SRCLK_SET`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WD_SRCLK.3（SET）。 [完整端点N0122](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0122)。 |
| ARRAY | 05_SAFETY_TEMP | R_WD_SRCLK | RC0603FR-07100KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_WD_SRCLK.1=`SRCLK_SET`，R_WD_SRCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-wdiv-rclk"></a>

### 第008步：在ARRAY／05_SAFETY_TEMP放置 U_WDIV_RCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_WDIV_RCLK**，精确型号 **SN74LVC1G74DCUR**，封装 **DCU/VSSOP8**。

放在对应SRCLK/RCLK监测线上；74LVC1G74的D与反相输出构成二分频，PRE/CLR按表，不能用HB取代两路时钟监测。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_RCLK | SN74LVC1G74DCUR | 1 | CLK | RCLK_G0 | IN | 从此脚引线，标注精确网名`RCLK_G0`；跨页使用同名板内标签。同网还接：02_595/U_SR00.12（RCLK）；02_595/U_SR01.12（RCLK）；02_595/U_SR02.12（RCLK）；02_595/U_SR03.12（RCLK）；01_LINK_BUFFERS/R_CLK_RCLK0.2（2）。 [完整端点N0082](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0082)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_RCLK | SN74LVC1G74DCUR | 2 | D | RCLK_DIV_N | IN | 从此脚引线，标注精确网名`RCLK_DIV_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDIV_RCLK.3（Q_N）。 [完整端点N0081](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0081)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_RCLK | SN74LVC1G74DCUR | 3 | Q_N | RCLK_DIV_N | OUT | 从此脚引线，标注精确网名`RCLK_DIV_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDIV_RCLK.2（D）。 [完整端点N0081](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0081)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_RCLK | SN74LVC1G74DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_RCLK | SN74LVC1G74DCUR | 5 | Q | RCLK_DIV | OUT | 从此脚引线，标注精确网名`RCLK_DIV`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WD_RCLK.1（TRIG）。 [完整端点N0080](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0080)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_RCLK | SN74LVC1G74DCUR | 6 | CLR_N | POR_N | IN | 从此脚引线，标注精确网名`POR_N`；跨页使用同名板内标签。同网另有20个物理端点，逐个见[完整端点N0072](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0072)；例如02_595/U_SR00.10（SRCLR_N）；02_595/U_SR01.10（SRCLR_N）；02_595/U_SR02.10（SRCLR_N）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_RCLK | SN74LVC1G74DCUR | 7 | PRE_N | V3V3 | IN | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDIV_RCLK | SN74LVC1G74DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_WDIV_RCLK.4→GND；U_WDIV_RCLK.7→V3V3；U_WDIV_RCLK.8→V3V3。

<a id="array-c-u-wdiv-rclk"></a>

### 第009步：在ARRAY／05_SAFETY_TEMP放置 C_U_WDIV_RCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_WDIV_RCLK**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_WDIV_RCLK的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_WDIV_RCLK | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_WDIV_RCLK | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_WDIV_RCLK.1=`V3V3`，C_U_WDIV_RCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-wd-rclk"></a>

### 第010步：在ARRAY／05_SAFETY_TEMP放置 U_WD_RCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_WD_RCLK**，精确型号 **LTC6993IS6-2#TRMPBF**，封装 **S6/TSOT23-6**。

放在对应时钟二分频器右侧；LTC6993IS6-2的1TRIG/2GND/3SET/4DIV/5V+/6OUT逐脚照表，RSET=100k，DIV接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_WD_RCLK | LTC6993IS6-2#TRMPBF | 1 | TRIG | RCLK_DIV | IN | 从此脚引线，标注精确网名`RCLK_DIV`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDIV_RCLK.5（Q）。 [完整端点N0080](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0080)。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_RCLK | LTC6993IS6-2#TRMPBF | 2 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_RCLK | LTC6993IS6-2#TRMPBF | 3 | SET | RCLK_SET | IN | 从此脚引线，标注精确网名`RCLK_SET`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_WD_RCLK.1（1）。 [完整端点N0086](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0086)。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_RCLK | LTC6993IS6-2#TRMPBF | 4 | DIV | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_RCLK | LTC6993IS6-2#TRMPBF | 5 | V+ | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | U_WD_RCLK | LTC6993IS6-2#TRMPBF | 6 | OUT | RCLK_ALIVE | OUT | 从此脚引线，标注精确网名`RCLK_ALIVE`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDAND.2（B1）。 [完整端点N0075](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0075)。 |

接完确认：电源/地/参考为U_WD_RCLK.2→GND；U_WD_RCLK.4→GND；U_WD_RCLK.5→V3V3。

<a id="array-c-u-wd-rclk"></a>

### 第011步：在ARRAY／05_SAFETY_TEMP放置 C_U_WD_RCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_WD_RCLK**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_WD_RCLK的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_WD_RCLK | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_WD_RCLK | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_WD_RCLK.1=`V3V3`，C_U_WD_RCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-wd-rclk"></a>

### 第012步：在ARRAY／05_SAFETY_TEMP放置 R_WD_RCLK

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_WD_RCLK**，精确型号 **RC0603FR-07100KL**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页U_WD_RCLK的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_WD_RCLK | RC0603FR-07100KL | 1 | 1 | RCLK_SET | PASSIVE | 从此脚引线，标注精确网名`RCLK_SET`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WD_RCLK.3（SET）。 [完整端点N0086](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0086)。 |
| ARRAY | 05_SAFETY_TEMP | R_WD_RCLK | RC0603FR-07100KL | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_WD_RCLK.1=`RCLK_SET`，R_WD_RCLK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-wdand"></a>

### 第013步：在ARRAY／05_SAFETY_TEMP放置 U_WDAND

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_WDAND**，精确型号 **SN74LVC2G08DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_WDAND | SN74LVC2G08DCUR | 1 | A1 | SRCLK_ALIVE | IN | 从此脚引线，标注精确网名`SRCLK_ALIVE`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WD_SRCLK.6（OUT）。 [完整端点N0111](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0111)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDAND | SN74LVC2G08DCUR | 2 | B1 | RCLK_ALIVE | IN | 从此脚引线，标注精确网名`RCLK_ALIVE`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WD_RCLK.6（OUT）。 [完整端点N0075](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0075)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDAND | SN74LVC2G08DCUR | 3 | Y2 | ARM_CLEAR_N | OUT | 从此脚引线，标注精确网名`ARM_CLEAR_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_ARM.6（CLR_N）。 [完整端点N0001](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0001)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDAND | SN74LVC2G08DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDAND | SN74LVC2G08DCUR | 5 | A2 | RAIL_CENTRAL_OK | IN | 从此脚引线，标注精确网名`RAIL_CENTRAL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G2.7（1Y）；05_SAFETY_TEMP/U_G2.5（2A）。 [完整端点N0073](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0073)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDAND | SN74LVC2G08DCUR | 6 | B2 | WD_OK | IN | 从此脚引线，标注精确网名`WD_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDAND.7（Y1）。 [完整端点N0400](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0400)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDAND | SN74LVC2G08DCUR | 7 | Y1 | WD_OK | OUT | 从此脚引线，标注精确网名`WD_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDAND.6（B2）。 [完整端点N0400](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0400)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDAND | SN74LVC2G08DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_WDAND.4→GND；U_WDAND.8→V3V3。

<a id="array-c-u-wdand"></a>

### 第014步：在ARRAY／05_SAFETY_TEMP放置 C_U_WDAND

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_WDAND**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_WDAND的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_WDAND | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_WDAND | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_WDAND.1=`V3V3`，C_U_WDAND.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-permit-inv"></a>

### 第015步：在ARRAY／05_SAFETY_TEMP放置 U_PERMIT_INV

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_PERMIT_INV**，精确型号 **SN74LVC1G14DBVR**，封装 **DBV/SOT23-5**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_PERMIT_INV | SN74LVC1G14DBVR | 1 | NC | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| ARRAY | 05_SAFETY_TEMP | U_PERMIT_INV | SN74LVC1G14DBVR | 2 | A | TX_PERMIT | IN | 从此脚引线，标注精确网名`TX_PERMIT`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.39（TX_PERMIT）；01_LINK_BUFFERS/R_DEF_TX_PERMIT.1（1）；05_SAFETY_TEMP/U_ARM.1（CLK）；05_SAFETY_TEMP/U_G3.2（1B）。 [完整端点N0382](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0382)。 |
| ARRAY | 05_SAFETY_TEMP | U_PERMIT_INV | SN74LVC1G14DBVR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_PERMIT_INV | SN74LVC1G14DBVR | 4 | Y | PERMIT_N | OUT | 从此脚引线，标注精确网名`PERMIT_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDOR.2（B1）。 [完整端点N0070](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0070)。 |
| ARRAY | 05_SAFETY_TEMP | U_PERMIT_INV | SN74LVC1G14DBVR | 5 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_PERMIT_INV.3→GND；U_PERMIT_INV.5→V3V3。 NC脚1逐个单独标记。

<a id="array-c-u-permit-inv"></a>

### 第016步：在ARRAY／05_SAFETY_TEMP放置 C_U_PERMIT_INV

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_PERMIT_INV**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_PERMIT_INV的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_PERMIT_INV | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_PERMIT_INV | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_PERMIT_INV.1=`V3V3`，C_U_PERMIT_INV.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-wdor"></a>

### 第017步：在ARRAY／05_SAFETY_TEMP放置 U_WDOR

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_WDOR**，精确型号 **SN74LVC2G32DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_WDOR | SN74LVC2G32DCUR | 1 | A1 | ARM_SEEN | IN | 从此脚引线，标注精确网名`ARM_SEEN`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_ARM.5（Q）；05_SAFETY_TEMP/U_G2.6（2B）。 [完整端点N0002](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0002)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDOR | SN74LVC2G32DCUR | 2 | B1 | PERMIT_N | IN | 从此脚引线，标注精确网名`PERMIT_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_PERMIT_INV.4（Y）。 [完整端点N0070](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0070)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDOR | SN74LVC2G32DCUR | 3 | Y2 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| ARRAY | 05_SAFETY_TEMP | U_WDOR | SN74LVC2G32DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDOR | SN74LVC2G32DCUR | 5 | A2 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDOR | SN74LVC2G32DCUR | 6 | B2 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_WDOR | SN74LVC2G32DCUR | 7 | Y1 | WD_REPORT_OK | OUT | 从此脚引线，标注精确网名`WD_REPORT_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_FAULT_FILTER.1（1）。 [完整端点N0402](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0402)。 |
| ARRAY | 05_SAFETY_TEMP | U_WDOR | SN74LVC2G32DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_WDOR.4→GND；U_WDOR.8→V3V3；U_WDOR.5→GND；U_WDOR.6→GND。 NC脚3逐个单独标记。

<a id="array-c-u-wdor"></a>

### 第018步：在ARRAY／05_SAFETY_TEMP放置 C_U_WDOR

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_WDOR**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_WDOR的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_WDOR | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_WDOR | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_WDOR.1=`V3V3`，C_U_WDOR.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-g1"></a>

### 第019步：在ARRAY／05_SAFETY_TEMP放置 U_G1

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_G1**，精确型号 **SN74LVC2G08DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_G1 | SN74LVC2G08DCUR | 1 | 1A | POR_N | IN | 从此脚引线，标注精确网名`POR_N`；跨页使用同名板内标签。同网另有20个物理端点，逐个见[完整端点N0072](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0072)；例如02_595/U_SR00.10（SRCLR_N）；02_595/U_SR01.10（SRCLR_N）；02_595/U_SR02.10（SRCLR_N）。 |
| ARRAY | 05_SAFETY_TEMP | U_G1 | SN74LVC2G08DCUR | 2 | 1B | V5_GOOD | IN | 从此脚引线，标注精确网名`V5_GOOD`；跨页使用同名板内标签。同网还接：00_POWER/U_5MON.6（RESET_N）；00_POWER/R_5GOOD.1（1）。 [完整端点N0394](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0394)。 |
| ARRAY | 05_SAFETY_TEMP | U_G1 | SN74LVC2G08DCUR | 3 | 2Y | LOCAL_OK | OUT | 从此脚引线，标注精确网名`LOCAL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_PG.2（A）；05_SAFETY_TEMP/U_G2.1（1A）；05_SAFETY_TEMP/U_FAULTAND.1（A1）。 [完整端点N0067](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0067)。 |
| ARRAY | 05_SAFETY_TEMP | U_G1 | SN74LVC2G08DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_G1 | SN74LVC2G08DCUR | 5 | 2A | BASE_RAIL_OK | IN | 从此脚引线，标注精确网名`BASE_RAIL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_I2C.5（EN）；05_SAFETY_TEMP/U_G1.7（1Y）。 [完整端点N0003](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0003)。 |
| ARRAY | 05_SAFETY_TEMP | U_G1 | SN74LVC2G08DCUR | 6 | 2B | TX_PRE_GOOD | IN | 从此脚引线，标注精确网名`TX_PRE_GOOD`；跨页使用同名板内标签。同网还接：00_POWER/U_TXMON.6（RESET_N）；00_POWER/R_U_TXMON_PU.1（1）。 [完整端点N0383](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0383)。 |
| ARRAY | 05_SAFETY_TEMP | U_G1 | SN74LVC2G08DCUR | 7 | 1Y | BASE_RAIL_OK | OUT | 从此脚引线，标注精确网名`BASE_RAIL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_I2C.5（EN）；05_SAFETY_TEMP/U_G1.5（2A）。 [完整端点N0003](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0003)。 |
| ARRAY | 05_SAFETY_TEMP | U_G1 | SN74LVC2G08DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_G1.4→GND；U_G1.8→V3V3。

<a id="array-c-u-g1"></a>

### 第020步：在ARRAY／05_SAFETY_TEMP放置 C_U_G1

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_G1**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_G1的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_G1 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_G1 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_G1.1=`V3V3`，C_U_G1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-g2"></a>

### 第021步：在ARRAY／05_SAFETY_TEMP放置 U_G2

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_G2**，精确型号 **SN74LVC2G08DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_G2 | SN74LVC2G08DCUR | 1 | 1A | LOCAL_OK | IN | 从此脚引线，标注精确网名`LOCAL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_PG.2（A）；05_SAFETY_TEMP/U_G1.3（2Y）；05_SAFETY_TEMP/U_FAULTAND.1（A1）。 [完整端点N0067](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0067)。 |
| ARRAY | 05_SAFETY_TEMP | U_G2 | SN74LVC2G08DCUR | 2 | 1B | CENTRAL_POWER_OK | IN | 从此脚引线，标注精确网名`CENTRAL_POWER_OK`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.41（CENTRAL_POWER_OK）；01_LINK_BUFFERS/R_DEF_CENTRAL_POWER_OK.1（1）。 [完整端点N0014](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0014)。 |
| ARRAY | 05_SAFETY_TEMP | U_G2 | SN74LVC2G08DCUR | 3 | 2Y | BOARD_OK | OUT | 从此脚引线，标注精确网名`BOARD_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G3.1（1A）。 [完整端点N0004](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0004)。 |
| ARRAY | 05_SAFETY_TEMP | U_G2 | SN74LVC2G08DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_G2 | SN74LVC2G08DCUR | 5 | 2A | RAIL_CENTRAL_OK | IN | 从此脚引线，标注精确网名`RAIL_CENTRAL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G2.7（1Y）；05_SAFETY_TEMP/U_WDAND.5（A2）。 [完整端点N0073](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0073)。 |
| ARRAY | 05_SAFETY_TEMP | U_G2 | SN74LVC2G08DCUR | 6 | 2B | ARM_SEEN | IN | 从此脚引线，标注精确网名`ARM_SEEN`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_ARM.5（Q）；05_SAFETY_TEMP/U_WDOR.1（A1）。 [完整端点N0002](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0002)。 |
| ARRAY | 05_SAFETY_TEMP | U_G2 | SN74LVC2G08DCUR | 7 | 1Y | RAIL_CENTRAL_OK | OUT | 从此脚引线，标注精确网名`RAIL_CENTRAL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G2.5（2A）；05_SAFETY_TEMP/U_WDAND.5（A2）。 [完整端点N0073](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0073)。 |
| ARRAY | 05_SAFETY_TEMP | U_G2 | SN74LVC2G08DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_G2.4→GND；U_G2.8→V3V3。

<a id="array-c-u-g2"></a>

### 第022步：在ARRAY／05_SAFETY_TEMP放置 C_U_G2

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_G2**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_G2的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_G2 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_G2 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_G2.1=`V3V3`，C_U_G2.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-g3"></a>

### 第023步：在ARRAY／05_SAFETY_TEMP放置 U_G3

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_G3**，精确型号 **SN74LVC2G08DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_G3 | SN74LVC2G08DCUR | 1 | 1A | BOARD_OK | IN | 从此脚引线，标注精确网名`BOARD_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G2.3（2Y）。 [完整端点N0004](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0004)。 |
| ARRAY | 05_SAFETY_TEMP | U_G3 | SN74LVC2G08DCUR | 2 | 1B | TX_PERMIT | IN | 从此脚引线，标注精确网名`TX_PERMIT`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.39（TX_PERMIT）；01_LINK_BUFFERS/R_DEF_TX_PERMIT.1（1）；05_SAFETY_TEMP/U_ARM.1（CLK）；05_SAFETY_TEMP/U_PERMIT_INV.2（A）。 [完整端点N0382](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0382)。 |
| ARRAY | 05_SAFETY_TEMP | U_G3 | SN74LVC2G08DCUR | 3 | 2Y | EN_PERMIT | OUT | 从此脚引线，标注精确网名`EN_PERMIT`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_ENRELEASE0.1（1）。 [完整端点N0061](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0061)。 |
| ARRAY | 05_SAFETY_TEMP | U_G3 | SN74LVC2G08DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_G3 | SN74LVC2G08DCUR | 5 | 2A | CUT_PERMIT | IN | 从此脚引线，标注精确网名`CUT_PERMIT`；跨页使用同名板内标签。同网还接：00_POWER/R_CUT_BASE.1（1）；05_SAFETY_TEMP/U_G3.7（1Y）。 [完整端点N0017](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0017)。 |
| ARRAY | 05_SAFETY_TEMP | U_G3 | SN74LVC2G08DCUR | 6 | 2B | OUTPUT_REQUEST | IN | 从此脚引线，标注精确网名`OUTPUT_REQUEST`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_OEINV.4（Y）。 [完整端点N0069](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0069)。 |
| ARRAY | 05_SAFETY_TEMP | U_G3 | SN74LVC2G08DCUR | 7 | 1Y | CUT_PERMIT | OUT | 从此脚引线，标注精确网名`CUT_PERMIT`；跨页使用同名板内标签。同网还接：00_POWER/R_CUT_BASE.1（1）；05_SAFETY_TEMP/U_G3.5（2A）。 [完整端点N0017](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0017)。 |
| ARRAY | 05_SAFETY_TEMP | U_G3 | SN74LVC2G08DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_G3.4→GND；U_G3.8→V3V3。

<a id="array-c-u-g3"></a>

### 第024步：在ARRAY／05_SAFETY_TEMP放置 C_U_G3

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_G3**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_G3的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_G3 | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_G3 | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_G3.1=`V3V3`，C_U_G3.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-arm"></a>

### 第025步：在ARRAY／05_SAFETY_TEMP放置 U_ARM

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_ARM**，精确型号 **SN74LVC1G74DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_ARM | SN74LVC1G74DCUR | 1 | CLK | TX_PERMIT | IN | 从此脚引线，标注精确网名`TX_PERMIT`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.39（TX_PERMIT）；01_LINK_BUFFERS/R_DEF_TX_PERMIT.1（1）；05_SAFETY_TEMP/U_G3.2（1B）；05_SAFETY_TEMP/U_PERMIT_INV.2（A）。 [完整端点N0382](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0382)。 |
| ARRAY | 05_SAFETY_TEMP | U_ARM | SN74LVC1G74DCUR | 2 | D | V3V3 | IN | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | U_ARM | SN74LVC1G74DCUR | 3 | Q_N | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| ARRAY | 05_SAFETY_TEMP | U_ARM | SN74LVC1G74DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_ARM | SN74LVC1G74DCUR | 5 | Q | ARM_SEEN | OUT | 从此脚引线，标注精确网名`ARM_SEEN`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G2.6（2B）；05_SAFETY_TEMP/U_WDOR.1（A1）。 [完整端点N0002](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0002)。 |
| ARRAY | 05_SAFETY_TEMP | U_ARM | SN74LVC1G74DCUR | 6 | CLR_N | ARM_CLEAR_N | IN | 从此脚引线，标注精确网名`ARM_CLEAR_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDAND.3（Y2）。 [完整端点N0001](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0001)。 |
| ARRAY | 05_SAFETY_TEMP | U_ARM | SN74LVC1G74DCUR | 7 | PRE_N | V3V3 | IN | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | U_ARM | SN74LVC1G74DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_ARM.2→V3V3；U_ARM.4→GND；U_ARM.7→V3V3；U_ARM.8→V3V3。 NC脚3逐个单独标记。

<a id="array-c-u-arm"></a>

### 第026步：在ARRAY／05_SAFETY_TEMP放置 C_U_ARM

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_ARM**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_ARM的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_ARM | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_ARM | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_ARM.1=`V3V3`，C_U_ARM.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-q-enclamp0"></a>

### 第027步：在ARRAY／05_SAFETY_TEMP放置 Q_ENCLAMP0

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **Q_ENCLAMP0**，精确型号 **MMBT3904,215**，封装 **SOT23**。

本地UCC使能默认夹低晶体管，放在05_SAFETY_TEMP许可链右侧。DRIVER_EN_G0同时连接32颗UCC的64个EN脚，完整端点必须全接。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | Q_ENCLAMP0 | MMBT3904,215 | 1 | B | ENCLAMP_BASE_G0 | PASSIVE | 从此脚引线，标注精确网名`ENCLAMP_BASE_G0`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/Q_ENRELEASE0.3（C）；05_SAFETY_TEMP/R_ENCLAMP0.2（2）。 [完整端点N0059](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0059)。 |
| ARRAY | 05_SAFETY_TEMP | Q_ENCLAMP0 | MMBT3904,215 | 2 | E | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | Q_ENCLAMP0 | MMBT3904,215 | 3 | C | DRIVER_EN_G0 | PASSIVE | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：电源/地/参考为Q_ENCLAMP0.2→GND。

<a id="array-r-enclamp0"></a>

### 第028步：在ARRAY／05_SAFETY_TEMP放置 R_ENCLAMP0

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_ENCLAMP0**，精确型号 **RC0603FR-078K2L**，封装 **0603**。其值为 **8.2k**。

纸面位置：紧邻本页Q_ENCLAMP0的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_ENCLAMP0 | RC0603FR-078K2L | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 05_SAFETY_TEMP | R_ENCLAMP0 | RC0603FR-078K2L | 2 | 2 | ENCLAMP_BASE_G0 | PASSIVE | 从此脚引线，标注精确网名`ENCLAMP_BASE_G0`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/Q_ENCLAMP0.1（B）；05_SAFETY_TEMP/Q_ENRELEASE0.3（C）。 [完整端点N0059](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0059)。 |

接完确认：R_ENCLAMP0.1=`VTX`，R_ENCLAMP0.2=`ENCLAMP_BASE_G0`；不可旁路该器件把两个网名短在一起。

<a id="array-r-en-pd0"></a>

### 第029步：在ARRAY／05_SAFETY_TEMP放置 R_EN_PD0

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_EN_PD0**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页Q_ENCLAMP0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_EN_PD0 | CRCW0603100KFKEA | 1 | 1 | DRIVER_EN_G0 | PASSIVE | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |
| ARRAY | 05_SAFETY_TEMP | R_EN_PD0 | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_EN_PD0.1=`DRIVER_EN_G0`，R_EN_PD0.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-en-pu0"></a>

### 第030步：在ARRAY／05_SAFETY_TEMP放置 R_EN_PU0

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_EN_PU0**，精确型号 **CRCW06034K70FKEA**，封装 **0603**。其值为 **4.7k**。

纸面位置：紧邻本页Q_ENCLAMP0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_EN_PU0 | CRCW06034K70FKEA | 1 | 1 | VTX | PASSIVE | 接本板`VTX`电源/参考标签；来源：本板Q_TX漏极5/6/7/8后的TX电源，只给本板驱动。同网另有75个物理端点，逐个见[完整端点N0398](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0398)；例如00_POWER/Q_TX.5（D）；00_POWER/Q_TX.6（D）；00_POWER/Q_TX.7（D）。 |
| ARRAY | 05_SAFETY_TEMP | R_EN_PU0 | CRCW06034K70FKEA | 2 | 2 | DRIVER_EN_G0 | PASSIVE | 从此脚引线，标注精确网名`DRIVER_EN_G0`；跨页使用同名板内标签。同网另有66个物理端点，逐个见[完整端点N0053](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0053)；例如03_UCC_TX/U_DRV00.1（ENA）；03_UCC_TX/U_DRV00.8（ENB）；03_UCC_TX/U_DRV01.1（ENA）。 |

接完确认：R_EN_PU0.1=`VTX`，R_EN_PU0.2=`DRIVER_EN_G0`；不可旁路该器件把两个网名短在一起。

<a id="array-q-enrelease0"></a>

### 第031步：在ARRAY／05_SAFETY_TEMP放置 Q_ENRELEASE0

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **Q_ENRELEASE0**，精确型号 **MMBT3904,215**，封装 **SOT23**。

紧邻Q_ENCLAMP0，只有EN_PERMIT合格才解除夹低；不要将内部上拉或100k电阻当作主动关断。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | Q_ENRELEASE0 | MMBT3904,215 | 1 | B | ENRELEASE_BASE_G0 | PASSIVE | 从此脚引线，标注精确网名`ENRELEASE_BASE_G0`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_ENRELEASE0.2（2）；05_SAFETY_TEMP/R_ENRELEASE_PD0.1（1）。 [完整端点N0060](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0060)。 |
| ARRAY | 05_SAFETY_TEMP | Q_ENRELEASE0 | MMBT3904,215 | 2 | E | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | Q_ENRELEASE0 | MMBT3904,215 | 3 | C | ENCLAMP_BASE_G0 | PASSIVE | 从此脚引线，标注精确网名`ENCLAMP_BASE_G0`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/Q_ENCLAMP0.1（B）；05_SAFETY_TEMP/R_ENCLAMP0.2（2）。 [完整端点N0059](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0059)。 |

接完确认：电源/地/参考为Q_ENRELEASE0.2→GND。

<a id="array-r-enrelease0"></a>

### 第032步：在ARRAY／05_SAFETY_TEMP放置 R_ENRELEASE0

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_ENRELEASE0**，精确型号 **CRCW06031K00FKEA**，封装 **0603**。其值为 **1k**。

纸面位置：紧邻本页Q_ENRELEASE0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_ENRELEASE0 | CRCW06031K00FKEA | 1 | 1 | EN_PERMIT | PASSIVE | 从此脚引线，标注精确网名`EN_PERMIT`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G3.3（2Y）。 [完整端点N0061](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0061)。 |
| ARRAY | 05_SAFETY_TEMP | R_ENRELEASE0 | CRCW06031K00FKEA | 2 | 2 | ENRELEASE_BASE_G0 | PASSIVE | 从此脚引线，标注精确网名`ENRELEASE_BASE_G0`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/Q_ENRELEASE0.1（B）；05_SAFETY_TEMP/R_ENRELEASE_PD0.1（1）。 [完整端点N0060](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0060)。 |

接完确认：R_ENRELEASE0.1=`EN_PERMIT`，R_ENRELEASE0.2=`ENRELEASE_BASE_G0`；不可旁路该器件把两个网名短在一起。

<a id="array-r-enrelease-pd0"></a>

### 第033步：在ARRAY／05_SAFETY_TEMP放置 R_ENRELEASE_PD0

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_ENRELEASE_PD0**，精确型号 **CRCW0603100KFKEA**，封装 **0603**。其值为 **100k**。

纸面位置：紧邻本页Q_ENRELEASE0的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_ENRELEASE_PD0 | CRCW0603100KFKEA | 1 | 1 | ENRELEASE_BASE_G0 | PASSIVE | 从此脚引线，标注精确网名`ENRELEASE_BASE_G0`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/Q_ENRELEASE0.1（B）；05_SAFETY_TEMP/R_ENRELEASE0.2（2）。 [完整端点N0060](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0060)。 |
| ARRAY | 05_SAFETY_TEMP | R_ENRELEASE_PD0 | CRCW0603100KFKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ENRELEASE_PD0.1=`ENRELEASE_BASE_G0`，R_ENRELEASE_PD0.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-fault-schmitt"></a>

### 第034步：在ARRAY／05_SAFETY_TEMP放置 U_FAULT_SCHMITT

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_FAULT_SCHMITT**，精确型号 **SN74LVC1G17DBVR**，封装 **DBV/SOT23-5**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_FAULT_SCHMITT | SN74LVC1G17DBVR | 1 | NC | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULT_SCHMITT | SN74LVC1G17DBVR | 2 | A | WD_REPORT_RC | IN | 从此脚引线，标注精确网名`WD_REPORT_RC`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_FAULT_FILTER.2（2）；05_SAFETY_TEMP/C_FAULT_FILTER.1（1）。 [完整端点N0403](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0403)。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULT_SCHMITT | SN74LVC1G17DBVR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULT_SCHMITT | SN74LVC1G17DBVR | 4 | Y | WD_REPORT_CLEAN | OUT | 从此脚引线，标注精确网名`WD_REPORT_CLEAN`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_FAULTAND.2（B1）。 [完整端点N0401](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0401)。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULT_SCHMITT | SN74LVC1G17DBVR | 5 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_FAULT_SCHMITT.3→GND；U_FAULT_SCHMITT.5→V3V3。 NC脚1逐个单独标记。

<a id="array-c-u-fault-schmitt"></a>

### 第035步：在ARRAY／05_SAFETY_TEMP放置 C_U_FAULT_SCHMITT

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_FAULT_SCHMITT**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_FAULT_SCHMITT的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_FAULT_SCHMITT | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_FAULT_SCHMITT | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_FAULT_SCHMITT.1=`V3V3`，C_U_FAULT_SCHMITT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-c-fault-filter"></a>

### 第036步：在ARRAY／05_SAFETY_TEMP放置 C_FAULT_FILTER

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_FAULT_FILTER**，精确型号 **C0603C102J5GACTU**，封装 **0603**。其值为 **1nF**。

纸面位置：紧邻本页U_FAULT_SCHMITT的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_FAULT_FILTER | C0603C102J5GACTU | 1 | 1 | WD_REPORT_RC | PASSIVE | 从此脚引线，标注精确网名`WD_REPORT_RC`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_FAULT_FILTER.2（2）；05_SAFETY_TEMP/U_FAULT_SCHMITT.2（A）。 [完整端点N0403](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0403)。 |
| ARRAY | 05_SAFETY_TEMP | C_FAULT_FILTER | C0603C102J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_FAULT_FILTER.1=`WD_REPORT_RC`，C_FAULT_FILTER.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-fault-filter"></a>

### 第037步：在ARRAY／05_SAFETY_TEMP放置 R_FAULT_FILTER

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_FAULT_FILTER**，精确型号 **RC0603FR-071KL**，封装 **0603**。其值为 **1k**。

纸面位置：紧邻本页U_FAULT_SCHMITT的相应引脚区域。额定条件：0.1W ±1%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_FAULT_FILTER | RC0603FR-071KL | 1 | 1 | WD_REPORT_OK | PASSIVE | 从此脚引线，标注精确网名`WD_REPORT_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_WDOR.7（Y1）。 [完整端点N0402](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0402)。 |
| ARRAY | 05_SAFETY_TEMP | R_FAULT_FILTER | RC0603FR-071KL | 2 | 2 | WD_REPORT_RC | PASSIVE | 从此脚引线，标注精确网名`WD_REPORT_RC`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/C_FAULT_FILTER.1（1）；05_SAFETY_TEMP/U_FAULT_SCHMITT.2（A）。 [完整端点N0403](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0403)。 |

接完确认：R_FAULT_FILTER.1=`WD_REPORT_OK`，R_FAULT_FILTER.2=`WD_REPORT_RC`；不可旁路该器件把两个网名短在一起。

<a id="array-u-faultand"></a>

### 第038步：在ARRAY／05_SAFETY_TEMP放置 U_FAULTAND

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_FAULTAND**，精确型号 **SN74LVC2G08DCUR**，封装 **DCU/VSSOP8**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_FAULTAND | SN74LVC2G08DCUR | 1 | A1 | LOCAL_OK | IN | 从此脚引线，标注精确网名`LOCAL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_PG.2（A）；05_SAFETY_TEMP/U_G1.3（2Y）；05_SAFETY_TEMP/U_G2.1（1A）。 [完整端点N0067](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0067)。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULTAND | SN74LVC2G08DCUR | 2 | B1 | WD_REPORT_CLEAN | IN | 从此脚引线，标注精确网名`WD_REPORT_CLEAN`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_FAULT_SCHMITT.4（Y）。 [完整端点N0401](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0401)。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULTAND | SN74LVC2G08DCUR | 3 | Y2 | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULTAND | SN74LVC2G08DCUR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULTAND | SN74LVC2G08DCUR | 5 | A2 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULTAND | SN74LVC2G08DCUR | 6 | B2 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULTAND | SN74LVC2G08DCUR | 7 | Y1 | FAULT_OK | OUT | 从此脚引线，标注精确网名`FAULT_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_FLT.2（A）。 [完整端点N0063](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0063)。 |
| ARRAY | 05_SAFETY_TEMP | U_FAULTAND | SN74LVC2G08DCUR | 8 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_FAULTAND.4→GND；U_FAULTAND.8→V3V3；U_FAULTAND.5→GND；U_FAULTAND.6→GND。 NC脚3逐个单独标记。

<a id="array-c-u-faultand"></a>

### 第039步：在ARRAY／05_SAFETY_TEMP放置 C_U_FAULTAND

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_FAULTAND**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_FAULTAND的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_FAULTAND | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_FAULTAND | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_FAULTAND.1=`V3V3`，C_U_FAULTAND.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-pg"></a>

### 第040步：在ARRAY／05_SAFETY_TEMP放置 U_PG

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_PG**，精确型号 **SN74LVC1G125DBVR**，封装 **DBV/SOT23-5**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_PG | SN74LVC1G125DBVR | 1 | OE_N | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_PG | SN74LVC1G125DBVR | 2 | A | LOCAL_OK | IN | 从此脚引线，标注精确网名`LOCAL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G1.3（2Y）；05_SAFETY_TEMP/U_G2.1（1A）；05_SAFETY_TEMP/U_FAULTAND.1（A1）。 [完整端点N0067](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0067)。 |
| ARRAY | 05_SAFETY_TEMP | U_PG | SN74LVC1G125DBVR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_PG | SN74LVC1G125DBVR | 4 | Y | PGOOD | OUT | 从此脚引线，标注精确网名`PGOOD`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.49（PGOOD）。 [完整端点N0071](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0071)。 |
| ARRAY | 05_SAFETY_TEMP | U_PG | SN74LVC1G125DBVR | 5 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_PG.1→GND；U_PG.3→GND；U_PG.5→V3V3。

<a id="array-c-u-pg"></a>

### 第041步：在ARRAY／05_SAFETY_TEMP放置 C_U_PG

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_PG**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_PG的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_PG | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_PG | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_PG.1=`V3V3`，C_U_PG.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-flt"></a>

### 第042步：在ARRAY／05_SAFETY_TEMP放置 U_FLT

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_FLT**，精确型号 **SN74LVC1G07DBVR**，封装 **DBV/SOT23-5**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_FLT | SN74LVC1G07DBVR | 1 | NC | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| ARRAY | 05_SAFETY_TEMP | U_FLT | SN74LVC1G07DBVR | 2 | A | FAULT_OK | IN | 从此脚引线，标注精确网名`FAULT_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_FAULTAND.7（Y1）。 [完整端点N0063](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0063)。 |
| ARRAY | 05_SAFETY_TEMP | U_FLT | SN74LVC1G07DBVR | 3 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_FLT | SN74LVC1G07DBVR | 4 | Y | FAULT_N | OD | 从此脚引线，标注精确网名`FAULT_N`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.47（FAULT_N）。 [完整端点N0062](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0062)。 |
| ARRAY | 05_SAFETY_TEMP | U_FLT | SN74LVC1G07DBVR | 5 | VCC | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_FLT.3→GND；U_FLT.5→V3V3。 NC脚1逐个单独标记。

<a id="array-c-u-flt"></a>

### 第043步：在ARRAY／05_SAFETY_TEMP放置 C_U_FLT

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_FLT**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_FLT的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_FLT | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_FLT | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_FLT.1=`V3V3`，C_U_FLT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-u-i2c"></a>

### 第044步：在ARRAY／05_SAFETY_TEMP放置 U_I2C

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_I2C**，精确型号 **TCA9517DGKR**，封装 **DGK/VSSOP8**。

放在ARRAY排线I2C与本地传感器之间；A侧是排线侧、B侧是本地侧，禁止B侧直接连另一TCA9517的B侧。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_I2C | TCA9517DGKR | 1 | VCCA | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | U_I2C | TCA9517DGKR | 2 | SCLA | SCL | OD | 从此脚引线，标注精确网名`SCL`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.51（SCL）。 [完整端点N0108](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0108)。 |
| ARRAY | 05_SAFETY_TEMP | U_I2C | TCA9517DGKR | 3 | SDAA | SDA | OD | 从此脚引线，标注精确网名`SDA`；跨页使用同名板内标签。同网还接：01_LINK_BUFFERS/J_LINK.53（SDA）。 [完整端点N0109](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0109)。 |
| ARRAY | 05_SAFETY_TEMP | U_I2C | TCA9517DGKR | 4 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_I2C | TCA9517DGKR | 5 | EN | BASE_RAIL_OK | IN | 从此脚引线，标注精确网名`BASE_RAIL_OK`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_G1.7（1Y）；05_SAFETY_TEMP/U_G1.5（2A）。 [完整端点N0003](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0003)。 |
| ARRAY | 05_SAFETY_TEMP | U_I2C | TCA9517DGKR | 6 | SDAB | TEMP_SDA | OD | 从此脚引线，标注精确网名`TEMP_SDA`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_TEMP_SDA.1（1）；05_SAFETY_TEMP/U_TEMP.6（SDA）。 [完整端点N0124](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0124)。 |
| ARRAY | 05_SAFETY_TEMP | U_I2C | TCA9517DGKR | 7 | SCLB | TEMP_SCL | OD | 从此脚引线，标注精确网名`TEMP_SCL`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_TEMP_SCL.1（1）；05_SAFETY_TEMP/U_TEMP.1（SCL）。 [完整端点N0123](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0123)。 |
| ARRAY | 05_SAFETY_TEMP | U_I2C | TCA9517DGKR | 8 | VCCB | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：电源/地/参考为U_I2C.1→V3V3；U_I2C.4→GND；U_I2C.8→V3V3。

<a id="array-c-u-i2c-a"></a>

### 第045步：在ARRAY／05_SAFETY_TEMP放置 C_U_I2C_A

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_I2C_A**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_I2C的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_I2C_A | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_I2C_A | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_I2C_A.1=`V3V3`，C_U_I2C_A.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-c-u-i2c-b"></a>

### 第046步：在ARRAY／05_SAFETY_TEMP放置 C_U_I2C_B

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_I2C_B**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_I2C的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_I2C_B | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_I2C_B | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_I2C_B.1=`V3V3`，C_U_I2C_B.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-temp-scl"></a>

### 第047步：在ARRAY／05_SAFETY_TEMP放置 R_TEMP_SCL

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_TEMP_SCL**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_I2C的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_TEMP_SCL | CRCW06032K20FKEA | 1 | 1 | TEMP_SCL | PASSIVE | 从此脚引线，标注精确网名`TEMP_SCL`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_I2C.7（SCLB）；05_SAFETY_TEMP/U_TEMP.1（SCL）。 [完整端点N0123](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0123)。 |
| ARRAY | 05_SAFETY_TEMP | R_TEMP_SCL | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_TEMP_SCL.1=`TEMP_SCL`，R_TEMP_SCL.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="array-r-temp-sda"></a>

### 第048步：在ARRAY／05_SAFETY_TEMP放置 R_TEMP_SDA

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_TEMP_SDA**，精确型号 **CRCW06032K20FKEA**，封装 **0603**。其值为 **2.2k**。

纸面位置：紧邻本页U_I2C的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_TEMP_SDA | CRCW06032K20FKEA | 1 | 1 | TEMP_SDA | PASSIVE | 从此脚引线，标注精确网名`TEMP_SDA`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_I2C.6（SDAB）；05_SAFETY_TEMP/U_TEMP.6（SDA）。 [完整端点N0124](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0124)。 |
| ARRAY | 05_SAFETY_TEMP | R_TEMP_SDA | CRCW06032K20FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_TEMP_SDA.1=`TEMP_SDA`，R_TEMP_SDA.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="array-u-temp"></a>

### 第049步：在ARRAY／05_SAFETY_TEMP放置 U_TEMP

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **U_TEMP**，精确型号 **TMP117NAIDRVR**，封装 **DRV/WSON6**。

放在本页I2C支路末端；三个板上的TMP117均为0x48，ADD0接GND；EP接GND。ALERT及其上拉按原表保留。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | U_TEMP | TMP117NAIDRVR | 1 | SCL | TEMP_SCL | IN | 从此脚引线，标注精确网名`TEMP_SCL`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_I2C.7（SCLB）；05_SAFETY_TEMP/R_TEMP_SCL.1（1）。 [完整端点N0123](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0123)。 |
| ARRAY | 05_SAFETY_TEMP | U_TEMP | TMP117NAIDRVR | 2 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_TEMP | TMP117NAIDRVR | 3 | ALERT | U_TEMP_ALERT_N | OD | 从此脚引线，标注精确网名`U_TEMP_ALERT_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/R_U_TEMP_ALERT.1（1）。 [完整端点N0386](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0386)。 |
| ARRAY | 05_SAFETY_TEMP | U_TEMP | TMP117NAIDRVR | 4 | ADD0 | GND | IN | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| ARRAY | 05_SAFETY_TEMP | U_TEMP | TMP117NAIDRVR | 5 | V+ | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | U_TEMP | TMP117NAIDRVR | 6 | SDA | TEMP_SDA | OD | 从此脚引线，标注精确网名`TEMP_SDA`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_I2C.6（SDAB）；05_SAFETY_TEMP/R_TEMP_SDA.1（1）。 [完整端点N0124](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0124)。 |
| ARRAY | 05_SAFETY_TEMP | U_TEMP | TMP117NAIDRVR | EP | PAD | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为U_TEMP.2→GND；U_TEMP.4→GND；U_TEMP.5→V3V3；U_TEMP.EP→GND。

<a id="array-c-u-temp"></a>

### 第050步：在ARRAY／05_SAFETY_TEMP放置 C_U_TEMP

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **C_U_TEMP**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_TEMP的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | C_U_TEMP | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| ARRAY | 05_SAFETY_TEMP | C_U_TEMP | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有493个物理端点，逐个见[完整端点N0064](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0064)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_TEMP.1=`V3V3`，C_U_TEMP.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="array-r-u-temp-alert"></a>

### 第051步：在ARRAY／05_SAFETY_TEMP放置 R_U_TEMP_ALERT

在 **ARRAY板的05_SAFETY_TEMP图页**，接着放置 **R_U_TEMP_ALERT**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_TEMP的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARRAY | 05_SAFETY_TEMP | R_U_TEMP_ALERT | CRCW060310K0FKEA | 1 | 1 | U_TEMP_ALERT_N | PASSIVE | 从此脚引线，标注精确网名`U_TEMP_ALERT_N`；跨页使用同名板内标签。同网还接：05_SAFETY_TEMP/U_TEMP.3（ALERT）。 [完整端点N0386](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0386)。 |
| ARRAY | 05_SAFETY_TEMP | R_U_TEMP_ALERT | CRCW060310K0FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有108个物理端点，逐个见[完整端点N0390](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0390)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_U_TEMP_ALERT.1=`U_TEMP_ALERT_N`，R_U_TEMP_ALERT.2=`V3V3`；不可旁路该器件把两个网名短在一起。

本页完成核对：**51个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。
