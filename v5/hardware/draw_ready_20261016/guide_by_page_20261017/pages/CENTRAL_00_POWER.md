# CENTRAL／00_POWER逐步连接分册

本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。

<a id="page-central-00-power"></a>

## CENTRAL板／00_POWER图页

从左到右：J_PWR→F1→SW1→U_EF→V12_SW。下方分出3.3V与7.15V降压，再由7.15V经LDO得到V5A；监测输出送安全页。这里仅给中央板供电。

<a id="central-j-pwr"></a>

### 第001步：在CENTRAL／00_POWER放置 J_PWR

在 **CENTRAL板的00_POWER图页**，先放置 **J_PWR**，精确型号 **DC-050-20**，封装 **DC-050-20 THT supplier drawing**。

本页最左侧放DC入口。两处同编号1焊盘均属于同一CENTER正极；2接GND，3独立NC。匹配2.0mm中心针插头，中心正。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | J_PWR | DC-050-20 | 1 | CENTER | DC12_RAW | POWER | 接本板`DC12_RAW`电源/参考标签；来源：本板J_PWR.1输入正极，仅到本板保险丝输入。同网还接：00_POWER/F1.1（1）。 [完整端点N0460](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0460)。 |
| CENTRAL | 00_POWER | J_PWR | DC-050-20 | 2 | SLEEVE | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）；00_POWER/R_UV_BOT.2（2）。 |
| CENTRAL | 00_POWER | J_PWR | DC-050-20 | 3 | SWITCHED_SLEEVE | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |

接完确认：电源/地/参考为J_PWR.1→DC12_RAW；J_PWR.2→GND。 NC脚3逐个单独标记。

<a id="central-f1"></a>

### 第002步：在CENTRAL／00_POWER放置 F1

在 **CENTRAL板的00_POWER图页**，接着放置 **F1**，精确型号 **0451003.MRL**，封装 **2410**。其值为 **3A fast fuse**。

纸面位置：本页输入/输出位置。额定条件：3A; >=32VDC; Littelfuse0451003.MRL; normal budget<2.2A。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | F1 | 0451003.MRL | 1 | 1 | DC12_RAW | PASSIVE | 接本板`DC12_RAW`电源/参考标签；来源：本板J_PWR.1输入正极，仅到本板保险丝输入。同网还接：00_POWER/J_PWR.1（CENTER）。 [完整端点N0460](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0460)。 |
| CENTRAL | 00_POWER | F1 | 0451003.MRL | 2 | 2 | DC12_FUSED | PASSIVE | 接本板`DC12_FUSED`电源/参考标签；来源：本板F1.2保险丝后，到SW1.3。同网还接：00_POWER/SW1.3（ON_THROW）。 [完整端点N0459](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0459)。 |

接完确认：F1.1=`DC12_RAW`，F1.2=`DC12_FUSED`；不可旁路该器件把两个网名短在一起。

<a id="central-sw1"></a>

### 第003步：在CENTRAL／00_POWER放置 SW1

在 **CENTRAL板的00_POWER图页**，接着放置 **SW1**，精确型号 **7101MD9AV2QE**，封装 **C&K AV2 through-hole SPDT**。

放在保险丝之后。物理2是公共端，3是ON端，1为OFF端NC；图形旋转不改变物理脚号。开关状态由2与3接通定义。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | SW1 | 7101MD9AV2QE | 1 | OFF_THROW | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 00_POWER | SW1 | 7101MD9AV2QE | 2 | COMMON | DC12_AFTER_SWITCH | POWER | 接本板`DC12_AFTER_SWITCH`电源/参考标签；来源：本板SW1.2公共端输出，到eFuse输入。同网还接：00_POWER/U_EF.5（IN）；00_POWER/R_UV_TOP.1（1）；00_POWER/R_OV_TOP.1（1）；00_POWER/C_ENTRY_HF.1（1）。 [完整端点N0458](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0458)。 |
| CENTRAL | 00_POWER | SW1 | 7101MD9AV2QE | 3 | ON_THROW | DC12_FUSED | POWER | 接本板`DC12_FUSED`电源/参考标签；来源：本板F1.2保险丝后，到SW1.3。同网还接：00_POWER/F1.2（2）。 [完整端点N0459](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0459)。 |

接完确认：电源/地/参考为SW1.2→DC12_AFTER_SWITCH；SW1.3→DC12_FUSED。 NC脚1逐个单独标记。

<a id="central-c-entry-hf"></a>

### 第004步：在CENTRAL／00_POWER放置 C_ENTRY_HF

在 **CENTRAL板的00_POWER图页**，接着放置 **C_ENTRY_HF**，精确型号 **C1206C105K5RACTU**，封装 **1206**。其值为 **1uF**。

纸面位置：紧邻本页SW1的相应引脚区域。额定条件：50V X7R ±10%; nonpolar input hotplug capacitor。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_ENTRY_HF | C1206C105K5RACTU | 1 | 1 | DC12_AFTER_SWITCH | PASSIVE | 接本板`DC12_AFTER_SWITCH`电源/参考标签；来源：本板SW1.2公共端输出，到eFuse输入。同网还接：00_POWER/U_EF.5（IN）；00_POWER/R_UV_TOP.1（1）；00_POWER/R_OV_TOP.1（1）；00_POWER/SW1.2（COMMON）。 [完整端点N0458](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0458)。 |
| CENTRAL | 00_POWER | C_ENTRY_HF | C1206C105K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_ENTRY_HF.1=`DC12_AFTER_SWITCH`，C_ENTRY_HF.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-ef"></a>

### 第005步：在CENTRAL／00_POWER放置 U_EF

在 **CENTRAL板的00_POWER图页**，接着放置 **U_EF**，精确型号 **TPS259470LRPWR**，封装 **RPW/VQFN-HR10**。

放在开关右侧。按精确TPS259470L变体连接限流、欠压、过压和DVDT；AUXOFF/ITIMER按原表NC。它的供电启动与TX_PERMIT是不同功能。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 1 | EN/UVLO | EF_EN | IN | 从此脚引线，标注精确网名`EF_EN`；跨页使用同名板内标签。同网还接：00_POWER/R_UV_TOP.2（2）；00_POWER/R_UV_BOT.1（1）。 [完整端点N0556](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0556)。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 2 | OVLO | EF_OV | IN | 从此脚引线，标注精确网名`EF_OV`；跨页使用同名板内标签。同网还接：00_POWER/R_OV_TOP.2（2）；00_POWER/R_OV_BOT.1（1）。 [完整端点N0559](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0559)。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 3 | AUXOFF | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 4 | FLT_N | EF_FLT_N | OD | 从此脚引线，标注精确网名`EF_FLT_N`；跨页使用同名板内标签。同网还接：00_POWER/R_EF_FLT.1（1）。 [完整端点N0557](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0557)。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 5 | IN | DC12_AFTER_SWITCH | POWER | 接本板`DC12_AFTER_SWITCH`电源/参考标签；来源：本板SW1.2公共端输出，到eFuse输入。同网还接：00_POWER/R_UV_TOP.1（1）；00_POWER/R_OV_TOP.1（1）；00_POWER/SW1.2（COMMON）；00_POWER/C_ENTRY_HF.1（1）。 [完整端点N0458](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0458)。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 6 | OUT | V12_SW | POWER | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/D_TVS.1（1）；00_POWER/C_EF_OUT.1（1）；00_POWER/U_BUCK1.3（VIN）；00_POWER/C_B1_IN.1（1）；00_POWER/C_B1_HF.1（1）；00_POWER/U_BUCK2.3（VIN）；00_POWER/C_B2_IN.1（1）；00_POWER/C_B2_HF.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 7 | DVDT | EF_DVDT | PASSIVE | 从此脚引线，标注精确网名`EF_DVDT`；跨页使用同名板内标签。同网还接：00_POWER/C_DVDT.1（1）。 [完整端点N0555](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0555)。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 8 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/R_UV_BOT.2（2）。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 9 | ILM | EF_ILM | PASSIVE | 从此脚引线，标注精确网名`EF_ILM`；跨页使用同名板内标签。同网还接：00_POWER/R_ILM.1（1）。 [完整端点N0558](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0558)。 |
| CENTRAL | 00_POWER | U_EF | TPS259470LRPWR | 10 | ITIMER | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |

接完确认：电源/地/参考为U_EF.5→DC12_AFTER_SWITCH；U_EF.6→V12_SW；U_EF.8→GND。 NC脚3,10逐个单独标记。

<a id="central-c-dvdt"></a>

### 第006步：在CENTRAL／00_POWER放置 C_DVDT

在 **CENTRAL板的00_POWER图页**，接着放置 **C_DVDT**，精确型号 **C0603C103K5RACTU**，封装 **0603**。其值为 **10nF**。

纸面位置：紧邻本页U_EF的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_DVDT | C0603C103K5RACTU | 1 | 1 | EF_DVDT | PASSIVE | 从此脚引线，标注精确网名`EF_DVDT`；跨页使用同名板内标签。同网还接：00_POWER/U_EF.7（DVDT）。 [完整端点N0555](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0555)。 |
| CENTRAL | 00_POWER | C_DVDT | C0603C103K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_DVDT.1=`EF_DVDT`，C_DVDT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-ef-out"></a>

### 第007步：在CENTRAL／00_POWER放置 C_EF_OUT

在 **CENTRAL板的00_POWER图页**，接着放置 **C_EF_OUT**，精确型号 **EEEFK1V470P**，封装 **Panasonic FK 6.3mm can**。其值为 **47uF**。

纸面位置：紧邻本页U_EF的相应引脚区域。额定条件：35V 47uF ±20%; positive=pin1; EEEFK1V470P。有极性：物理1为正端、2为负端，不能对调。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_EF_OUT | EEEFK1V470P | 1 | 1 | V12_SW | PASSIVE | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/D_TVS.1（1）；00_POWER/U_EF.6（OUT）；00_POWER/U_BUCK1.3（VIN）；00_POWER/C_B1_IN.1（1）；00_POWER/C_B1_HF.1（1）；00_POWER/U_BUCK2.3（VIN）；00_POWER/C_B2_IN.1（1）；00_POWER/C_B2_HF.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | C_EF_OUT | EEEFK1V470P | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_EF_OUT.1=`V12_SW`，C_EF_OUT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-ef-flt"></a>

### 第008步：在CENTRAL／00_POWER放置 R_EF_FLT

在 **CENTRAL板的00_POWER图页**，接着放置 **R_EF_FLT**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_EF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_EF_FLT | CRCW060310K0FKEA | 1 | 1 | EF_FLT_N | PASSIVE | 从此脚引线，标注精确网名`EF_FLT_N`；跨页使用同名板内标签。同网还接：00_POWER/U_EF.4（FLT_N）。 [完整端点N0557](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0557)。 |
| CENTRAL | 00_POWER | R_EF_FLT | CRCW060310K0FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）；00_POWER/C_B1_OUT2.1（1）。 |

接完确认：R_EF_FLT.1=`EF_FLT_N`，R_EF_FLT.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-ilm"></a>

### 第009步：在CENTRAL／00_POWER放置 R_ILM

在 **CENTRAL板的00_POWER图页**，接着放置 **R_ILM**，精确型号 **CRCW06031K30FKEA**，封装 **0603**。其值为 **1.3k**。

纸面位置：紧邻本页U_EF的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_ILM | CRCW06031K30FKEA | 1 | 1 | EF_ILM | PASSIVE | 从此脚引线，标注精确网名`EF_ILM`；跨页使用同名板内标签。同网还接：00_POWER/U_EF.9（ILM）。 [完整端点N0558](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0558)。 |
| CENTRAL | 00_POWER | R_ILM | CRCW06031K30FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_ILM.1=`EF_ILM`，R_ILM.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-ov-bot"></a>

### 第010步：在CENTRAL／00_POWER放置 R_OV_BOT

在 **CENTRAL板的00_POWER图页**，接着放置 **R_OV_BOT**，精确型号 **TNPW060338K3BEEA**，封装 **0603**。其值为 **38.3k**。

纸面位置：紧邻本页U_EF的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_OV_BOT | TNPW060338K3BEEA | 1 | 1 | EF_OV | PASSIVE | 从此脚引线，标注精确网名`EF_OV`；跨页使用同名板内标签。同网还接：00_POWER/U_EF.2（OVLO）；00_POWER/R_OV_TOP.2（2）。 [完整端点N0559](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0559)。 |
| CENTRAL | 00_POWER | R_OV_BOT | TNPW060338K3BEEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_OV_BOT.1=`EF_OV`，R_OV_BOT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-ov-top"></a>

### 第011步：在CENTRAL／00_POWER放置 R_OV_TOP

在 **CENTRAL板的00_POWER图页**，接着放置 **R_OV_TOP**，精确型号 **TNPW0805392KBEEA**，封装 **0805**。其值为 **392k**。

纸面位置：紧邻本页U_EF的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_OV_TOP | TNPW0805392KBEEA | 1 | 1 | DC12_AFTER_SWITCH | PASSIVE | 接本板`DC12_AFTER_SWITCH`电源/参考标签；来源：本板SW1.2公共端输出，到eFuse输入。同网还接：00_POWER/U_EF.5（IN）；00_POWER/R_UV_TOP.1（1）；00_POWER/SW1.2（COMMON）；00_POWER/C_ENTRY_HF.1（1）。 [完整端点N0458](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0458)。 |
| CENTRAL | 00_POWER | R_OV_TOP | TNPW0805392KBEEA | 2 | 2 | EF_OV | PASSIVE | 从此脚引线，标注精确网名`EF_OV`；跨页使用同名板内标签。同网还接：00_POWER/U_EF.2（OVLO）；00_POWER/R_OV_BOT.1（1）。 [完整端点N0559](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0559)。 |

接完确认：R_OV_TOP.1=`DC12_AFTER_SWITCH`，R_OV_TOP.2=`EF_OV`；不可旁路该器件把两个网名短在一起。

<a id="central-r-uv-bot"></a>

### 第012步：在CENTRAL／00_POWER放置 R_UV_BOT

在 **CENTRAL板的00_POWER图页**，接着放置 **R_UV_BOT**，精确型号 **TNPW060359K0BEEA**，封装 **0603**。其值为 **59k**。

纸面位置：紧邻本页U_EF的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_UV_BOT | TNPW060359K0BEEA | 1 | 1 | EF_EN | PASSIVE | 从此脚引线，标注精确网名`EF_EN`；跨页使用同名板内标签。同网还接：00_POWER/U_EF.1（EN/UVLO）；00_POWER/R_UV_TOP.2（2）。 [完整端点N0556](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0556)。 |
| CENTRAL | 00_POWER | R_UV_BOT | TNPW060359K0BEEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_UV_BOT.1=`EF_EN`，R_UV_BOT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-uv-top"></a>

### 第013步：在CENTRAL／00_POWER放置 R_UV_TOP

在 **CENTRAL板的00_POWER图页**，接着放置 **R_UV_TOP**，精确型号 **TNPW0805383KBEEA**，封装 **0805**。其值为 **383k**。

纸面位置：紧邻本页U_EF的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_UV_TOP | TNPW0805383KBEEA | 1 | 1 | DC12_AFTER_SWITCH | PASSIVE | 接本板`DC12_AFTER_SWITCH`电源/参考标签；来源：本板SW1.2公共端输出，到eFuse输入。同网还接：00_POWER/U_EF.5（IN）；00_POWER/R_OV_TOP.1（1）；00_POWER/SW1.2（COMMON）；00_POWER/C_ENTRY_HF.1（1）。 [完整端点N0458](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0458)。 |
| CENTRAL | 00_POWER | R_UV_TOP | TNPW0805383KBEEA | 2 | 2 | EF_EN | PASSIVE | 从此脚引线，标注精确网名`EF_EN`；跨页使用同名板内标签。同网还接：00_POWER/U_EF.1（EN/UVLO）；00_POWER/R_UV_BOT.1（1）。 [完整端点N0556](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0556)。 |

接完确认：R_UV_TOP.1=`DC12_AFTER_SWITCH`，R_UV_TOP.2=`EF_EN`；不可旁路该器件把两个网名短在一起。

<a id="central-d-tvs"></a>

### 第014步：在CENTRAL／00_POWER放置 D_TVS

在 **CENTRAL板的00_POWER图页**，接着放置 **D_TVS**，精确型号 **SMBJ15CA**，封装 **DO-214AA**。其值为 **SMBJ15CA**。

纸面位置：本页输入/输出位置。额定条件：bidirectional 15V VRWM; clamp/source energy not certified。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | D_TVS | SMBJ15CA | 1 | 1 | V12_SW | PASSIVE | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/U_EF.6（OUT）；00_POWER/C_EF_OUT.1（1）；00_POWER/U_BUCK1.3（VIN）；00_POWER/C_B1_IN.1（1）；00_POWER/C_B1_HF.1（1）；00_POWER/U_BUCK2.3（VIN）；00_POWER/C_B2_IN.1（1）；00_POWER/C_B2_HF.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | D_TVS | SMBJ15CA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/U_EF.8（GND）；00_POWER/R_UV_BOT.2（2）。 |

接完确认：D_TVS.1=`V12_SW`，D_TVS.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-buck1"></a>

### 第015步：在CENTRAL／00_POWER放置 U_BUCK1

在 **CENTRAL板的00_POWER图页**，接着放置 **U_BUCK1**，精确型号 **TPS54202DDCR**，封装 **DDC/SOT23-6**。

本页对应电压区左放芯片，中间SW→电感，右放输出电容和负载标签；BOOT电容跨BOOT/SW，前馈220pF跨反馈上臂。5脚EN按原表独立NC，不因通用接线习惯擅自补接电源。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | U_BUCK1 | TPS54202DDCR | 1 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 00_POWER | U_BUCK1 | TPS54202DDCR | 2 | SW | BUCK1_SW | POWER | 从此脚引线，标注精确网名`BUCK1_SW`；跨页使用同名板内标签。同网还接：00_POWER/C_B1_BOOT.2（2）；00_POWER/L1.1（1）。 [完整端点N0453](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0453)。 |
| CENTRAL | 00_POWER | U_BUCK1 | TPS54202DDCR | 3 | VIN | V12_SW | POWER | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/D_TVS.1（1）；00_POWER/U_EF.6（OUT）；00_POWER/C_EF_OUT.1（1）；00_POWER/C_B1_IN.1（1）；00_POWER/C_B1_HF.1（1）；00_POWER/U_BUCK2.3（VIN）；00_POWER/C_B2_IN.1（1）；00_POWER/C_B2_HF.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | U_BUCK1 | TPS54202DDCR | 4 | FB | BUCK1_FB | IN | 从此脚引线，标注精确网名`BUCK1_FB`；跨页使用同名板内标签。同网还接：00_POWER/R_B1_TOP.2（2）；00_POWER/R_B1_BOT.1（1）；00_POWER/C_B1_FF.2（2）。 [完整端点N0452](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0452)。 |
| CENTRAL | 00_POWER | U_BUCK1 | TPS54202DDCR | 5 | EN | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 00_POWER | U_BUCK1 | TPS54202DDCR | 6 | BOOT | BUCK1_BOOT | PASSIVE | 从此脚引线，标注精确网名`BUCK1_BOOT`；跨页使用同名板内标签。同网还接：00_POWER/C_B1_BOOT.1（1）。 [完整端点N0451](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0451)。 |

接完确认：电源/地/参考为U_BUCK1.1→GND；U_BUCK1.3→V12_SW。 NC脚5逐个单独标记。

<a id="central-c-b1-boot"></a>

### 第016步：在CENTRAL／00_POWER放置 C_B1_BOOT

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B1_BOOT**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B1_BOOT | C0603C104K5RACTU | 1 | 1 | BUCK1_BOOT | PASSIVE | 从此脚引线，标注精确网名`BUCK1_BOOT`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK1.6（BOOT）。 [完整端点N0451](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0451)。 |
| CENTRAL | 00_POWER | C_B1_BOOT | C0603C104K5RACTU | 2 | 2 | BUCK1_SW | PASSIVE | 从此脚引线，标注精确网名`BUCK1_SW`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK1.2（SW）；00_POWER/L1.1（1）。 [完整端点N0453](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0453)。 |

接完确认：C_B1_BOOT.1=`BUCK1_BOOT`，C_B1_BOOT.2=`BUCK1_SW`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b1-bulk"></a>

### 第017步：在CENTRAL／00_POWER放置 C_B1_BULK

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B1_BULK**，精确型号 **25SVPF47M**，封装 **Panasonic C6 Ø6.3mm height6mm polar**。其值为 **47uF**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C。有极性：物理1为正端、2为负端，不能对调。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B1_BULK | 25SVPF47M | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | C_B1_BULK | 25SVPF47M | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B1_BULK.1=`V3V3`，C_B1_BULK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b1-ff"></a>

### 第018步：在CENTRAL／00_POWER放置 C_B1_FF

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B1_FF**，精确型号 **C0603C221J5GACTU**，封装 **0603**。其值为 **220pF**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：50V C0G ±5%; TPS54202equation16 feedforward。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B1_FF | C0603C221J5GACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | C_B1_FF | C0603C221J5GACTU | 2 | 2 | BUCK1_FB | PASSIVE | 从此脚引线，标注精确网名`BUCK1_FB`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK1.4（FB）；00_POWER/R_B1_TOP.2（2）；00_POWER/R_B1_BOT.1（1）。 [完整端点N0452](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0452)。 |

接完确认：C_B1_FF.1=`V3V3`，C_B1_FF.2=`BUCK1_FB`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b1-hf"></a>

### 第019步：在CENTRAL／00_POWER放置 C_B1_HF

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B1_HF**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B1_HF | C0603C104K5RACTU | 1 | 1 | V12_SW | PASSIVE | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/D_TVS.1（1）；00_POWER/U_EF.6（OUT）；00_POWER/C_EF_OUT.1（1）；00_POWER/U_BUCK1.3（VIN）；00_POWER/C_B1_IN.1（1）；00_POWER/U_BUCK2.3（VIN）；00_POWER/C_B2_IN.1（1）；00_POWER/C_B2_HF.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | C_B1_HF | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B1_HF.1=`V12_SW`，C_B1_HF.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b1-in"></a>

### 第020步：在CENTRAL／00_POWER放置 C_B1_IN

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B1_IN**，精确型号 **C1210C106K3RACTU**，封装 **1210**。其值为 **10uF**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B1_IN | C1210C106K3RACTU | 1 | 1 | V12_SW | PASSIVE | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/D_TVS.1（1）；00_POWER/U_EF.6（OUT）；00_POWER/C_EF_OUT.1（1）；00_POWER/U_BUCK1.3（VIN）；00_POWER/C_B1_HF.1（1）；00_POWER/U_BUCK2.3（VIN）；00_POWER/C_B2_IN.1（1）；00_POWER/C_B2_HF.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | C_B1_IN | C1210C106K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B1_IN.1=`V12_SW`，C_B1_IN.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b1-out1"></a>

### 第021步：在CENTRAL／00_POWER放置 C_B1_OUT1

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B1_OUT1**，精确型号 **C1210C226K3RACTU**，封装 **1210**。其值为 **22uF**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B1_OUT1 | C1210C226K3RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT2.1（1）。 |
| CENTRAL | 00_POWER | C_B1_OUT1 | C1210C226K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B1_OUT1.1=`V3V3`，C_B1_OUT1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b1-out2"></a>

### 第022步：在CENTRAL／00_POWER放置 C_B1_OUT2

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B1_OUT2**，精确型号 **C1210C226K3RACTU**，封装 **1210**。其值为 **22uF**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B1_OUT2 | C1210C226K3RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | C_B1_OUT2 | C1210C226K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B1_OUT2.1=`V3V3`，C_B1_OUT2.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-l1"></a>

### 第023步：在CENTRAL／00_POWER放置 L1

在 **CENTRAL板的00_POWER图页**，接着放置 **L1**，精确型号 **XAL7070-223MEC**，封装 **XAL7070**。其值为 **XAL7070-223MEC 22uH**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | L1 | XAL7070-223MEC | 1 | 1 | BUCK1_SW | PASSIVE | 从此脚引线，标注精确网名`BUCK1_SW`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK1.2（SW）；00_POWER/C_B1_BOOT.2（2）。 [完整端点N0453](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0453)。 |
| CENTRAL | 00_POWER | L1 | XAL7070-223MEC | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/C_B1_OUT1.1（1）；00_POWER/C_B1_OUT2.1（1）。 |

接完确认：L1.1=`BUCK1_SW`，L1.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-b1-bot"></a>

### 第024步：在CENTRAL／00_POWER放置 R_B1_BOT

在 **CENTRAL板的00_POWER图页**，接着放置 **R_B1_BOT**，精确型号 **TNPW060310K0BEEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_B1_BOT | TNPW060310K0BEEA | 1 | 1 | BUCK1_FB | PASSIVE | 从此脚引线，标注精确网名`BUCK1_FB`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK1.4（FB）；00_POWER/R_B1_TOP.2（2）；00_POWER/C_B1_FF.2（2）。 [完整端点N0452](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0452)。 |
| CENTRAL | 00_POWER | R_B1_BOT | TNPW060310K0BEEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_B1_BOT.1=`BUCK1_FB`，R_B1_BOT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-b1-top"></a>

### 第025步：在CENTRAL／00_POWER放置 R_B1_TOP

在 **CENTRAL板的00_POWER图页**，接着放置 **R_B1_TOP**，精确型号 **TNPW060345K3BEEA**，封装 **0603**。其值为 **45.3k**。

纸面位置：紧邻本页U_BUCK1的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_B1_TOP | TNPW060345K3BEEA | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | R_B1_TOP | TNPW060345K3BEEA | 2 | 2 | BUCK1_FB | PASSIVE | 从此脚引线，标注精确网名`BUCK1_FB`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK1.4（FB）；00_POWER/R_B1_BOT.1（1）；00_POWER/C_B1_FF.2（2）。 [完整端点N0452](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0452)。 |

接完确认：R_B1_TOP.1=`V3V3`，R_B1_TOP.2=`BUCK1_FB`；不可旁路该器件把两个网名短在一起。

<a id="central-u-buck2"></a>

### 第026步：在CENTRAL／00_POWER放置 U_BUCK2

在 **CENTRAL板的00_POWER图页**，接着放置 **U_BUCK2**，精确型号 **TPS54202DDCR**，封装 **DDC/SOT23-6**。

本页对应电压区左放芯片，中间SW→电感，右放输出电容和负载标签；BOOT电容跨BOOT/SW，前馈220pF跨反馈上臂。5脚EN按原表独立NC，不因通用接线习惯擅自补接电源。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | U_BUCK2 | TPS54202DDCR | 1 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 00_POWER | U_BUCK2 | TPS54202DDCR | 2 | SW | BUCK2_SW | POWER | 从此脚引线，标注精确网名`BUCK2_SW`；跨页使用同名板内标签。同网还接：00_POWER/C_B2_BOOT.2（2）；00_POWER/L2.1（1）。 [完整端点N0456](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0456)。 |
| CENTRAL | 00_POWER | U_BUCK2 | TPS54202DDCR | 3 | VIN | V12_SW | POWER | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/D_TVS.1（1）；00_POWER/U_EF.6（OUT）；00_POWER/C_EF_OUT.1（1）；00_POWER/U_BUCK1.3（VIN）；00_POWER/C_B1_IN.1（1）；00_POWER/C_B1_HF.1（1）；00_POWER/C_B2_IN.1（1）；00_POWER/C_B2_HF.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | U_BUCK2 | TPS54202DDCR | 4 | FB | BUCK2_FB | IN | 从此脚引线，标注精确网名`BUCK2_FB`；跨页使用同名板内标签。同网还接：00_POWER/R_B2_TOP.2（2）；00_POWER/R_B2_BOT.1（1）；00_POWER/C_B2_FF.2（2）。 [完整端点N0455](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0455)。 |
| CENTRAL | 00_POWER | U_BUCK2 | TPS54202DDCR | 5 | EN | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 00_POWER | U_BUCK2 | TPS54202DDCR | 6 | BOOT | BUCK2_BOOT | PASSIVE | 从此脚引线，标注精确网名`BUCK2_BOOT`；跨页使用同名板内标签。同网还接：00_POWER/C_B2_BOOT.1（1）。 [完整端点N0454](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0454)。 |

接完确认：电源/地/参考为U_BUCK2.1→GND；U_BUCK2.3→V12_SW。 NC脚5逐个单独标记。

<a id="central-c-b2-boot"></a>

### 第027步：在CENTRAL／00_POWER放置 C_B2_BOOT

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B2_BOOT**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B2_BOOT | C0603C104K5RACTU | 1 | 1 | BUCK2_BOOT | PASSIVE | 从此脚引线，标注精确网名`BUCK2_BOOT`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK2.6（BOOT）。 [完整端点N0454](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0454)。 |
| CENTRAL | 00_POWER | C_B2_BOOT | C0603C104K5RACTU | 2 | 2 | BUCK2_SW | PASSIVE | 从此脚引线，标注精确网名`BUCK2_SW`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK2.2（SW）；00_POWER/L2.1（1）。 [完整端点N0456](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0456)。 |

接完确认：C_B2_BOOT.1=`BUCK2_BOOT`，C_B2_BOOT.2=`BUCK2_SW`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b2-bulk"></a>

### 第028步：在CENTRAL／00_POWER放置 C_B2_BULK

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B2_BULK**，精确型号 **25SVPF47M**，封装 **Panasonic C6 Ø6.3mm height6mm polar**。其值为 **47uF**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C。有极性：物理1为正端、2为负端，不能对调。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B2_BULK | 25SVPF47M | 1 | 1 | V7V15 | PASSIVE | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/L2.2（2）；00_POWER/C_B2_OUT1.1（1）；00_POWER/C_B2_OUT2.1（1）；00_POWER/R_B2_TOP.1（1）；00_POWER/C_LDO_IN.1（1）；00_POWER/U_LDO.4（EN）；00_POWER/U_LDO.6（IN）；00_POWER/C_B2_FF.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |
| CENTRAL | 00_POWER | C_B2_BULK | 25SVPF47M | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B2_BULK.1=`V7V15`，C_B2_BULK.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b2-ff"></a>

### 第029步：在CENTRAL／00_POWER放置 C_B2_FF

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B2_FF**，精确型号 **C0603C221J5GACTU**，封装 **0603**。其值为 **220pF**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：50V C0G ±5%; TPS54202equation16 feedforward。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

此电容不是普通对地退耦；两端严格按下面两个不同网络接入，不能机械地把2脚改接GND。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B2_FF | C0603C221J5GACTU | 1 | 1 | V7V15 | PASSIVE | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/L2.2（2）；00_POWER/C_B2_OUT1.1（1）；00_POWER/C_B2_OUT2.1（1）；00_POWER/R_B2_TOP.1（1）；00_POWER/C_LDO_IN.1（1）；00_POWER/U_LDO.4（EN）；00_POWER/U_LDO.6（IN）；00_POWER/C_B2_BULK.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |
| CENTRAL | 00_POWER | C_B2_FF | C0603C221J5GACTU | 2 | 2 | BUCK2_FB | PASSIVE | 从此脚引线，标注精确网名`BUCK2_FB`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK2.4（FB）；00_POWER/R_B2_TOP.2（2）；00_POWER/R_B2_BOT.1（1）。 [完整端点N0455](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0455)。 |

接完确认：C_B2_FF.1=`V7V15`，C_B2_FF.2=`BUCK2_FB`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b2-hf"></a>

### 第030步：在CENTRAL／00_POWER放置 C_B2_HF

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B2_HF**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B2_HF | C0603C104K5RACTU | 1 | 1 | V12_SW | PASSIVE | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/D_TVS.1（1）；00_POWER/U_EF.6（OUT）；00_POWER/C_EF_OUT.1（1）；00_POWER/U_BUCK1.3（VIN）；00_POWER/C_B1_IN.1（1）；00_POWER/C_B1_HF.1（1）；00_POWER/U_BUCK2.3（VIN）；00_POWER/C_B2_IN.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | C_B2_HF | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B2_HF.1=`V12_SW`，C_B2_HF.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b2-in"></a>

### 第031步：在CENTRAL／00_POWER放置 C_B2_IN

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B2_IN**，精确型号 **C1210C106K3RACTU**，封装 **1210**。其值为 **10uF**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B2_IN | C1210C106K3RACTU | 1 | 1 | V12_SW | PASSIVE | 接本板`V12_SW`电源/参考标签；来源：本板U_EF.6保护输出，给本板各降压输入。同网还接：00_POWER/D_TVS.1（1）；00_POWER/U_EF.6（OUT）；00_POWER/C_EF_OUT.1（1）；00_POWER/U_BUCK1.3（VIN）；00_POWER/C_B1_IN.1（1）；00_POWER/C_B1_HF.1（1）；00_POWER/U_BUCK2.3（VIN）；00_POWER/C_B2_HF.1（1）。 [完整端点N0678](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0678)。 |
| CENTRAL | 00_POWER | C_B2_IN | C1210C106K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B2_IN.1=`V12_SW`，C_B2_IN.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b2-out1"></a>

### 第032步：在CENTRAL／00_POWER放置 C_B2_OUT1

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B2_OUT1**，精确型号 **C1210C226K3RACTU**，封装 **1210**。其值为 **22uF**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B2_OUT1 | C1210C226K3RACTU | 1 | 1 | V7V15 | PASSIVE | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/L2.2（2）；00_POWER/C_B2_OUT2.1（1）；00_POWER/R_B2_TOP.1（1）；00_POWER/C_LDO_IN.1（1）；00_POWER/U_LDO.4（EN）；00_POWER/U_LDO.6（IN）；00_POWER/C_B2_BULK.1（1）；00_POWER/C_B2_FF.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |
| CENTRAL | 00_POWER | C_B2_OUT1 | C1210C226K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B2_OUT1.1=`V7V15`，C_B2_OUT1.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-b2-out2"></a>

### 第033步：在CENTRAL／00_POWER放置 C_B2_OUT2

在 **CENTRAL板的00_POWER图页**，接着放置 **C_B2_OUT2**，精确型号 **C1210C226K3RACTU**，封装 **1210**。其值为 **22uF**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_B2_OUT2 | C1210C226K3RACTU | 1 | 1 | V7V15 | PASSIVE | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/L2.2（2）；00_POWER/C_B2_OUT1.1（1）；00_POWER/R_B2_TOP.1（1）；00_POWER/C_LDO_IN.1（1）；00_POWER/U_LDO.4（EN）；00_POWER/U_LDO.6（IN）；00_POWER/C_B2_BULK.1（1）；00_POWER/C_B2_FF.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |
| CENTRAL | 00_POWER | C_B2_OUT2 | C1210C226K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_B2_OUT2.1=`V7V15`，C_B2_OUT2.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-l2"></a>

### 第034步：在CENTRAL／00_POWER放置 L2

在 **CENTRAL板的00_POWER图页**，接着放置 **L2**，精确型号 **XAL7070-223MEC**，封装 **XAL7070**。其值为 **XAL7070-223MEC 22uH**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | L2 | XAL7070-223MEC | 1 | 1 | BUCK2_SW | PASSIVE | 从此脚引线，标注精确网名`BUCK2_SW`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK2.2（SW）；00_POWER/C_B2_BOOT.2（2）。 [完整端点N0456](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0456)。 |
| CENTRAL | 00_POWER | L2 | XAL7070-223MEC | 2 | 2 | V7V15 | PASSIVE | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/C_B2_OUT1.1（1）；00_POWER/C_B2_OUT2.1（1）；00_POWER/R_B2_TOP.1（1）；00_POWER/C_LDO_IN.1（1）；00_POWER/U_LDO.4（EN）；00_POWER/U_LDO.6（IN）；00_POWER/C_B2_BULK.1（1）；00_POWER/C_B2_FF.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |

接完确认：L2.1=`BUCK2_SW`，L2.2=`V7V15`；不可旁路该器件把两个网名短在一起。

<a id="central-r-b2-bot"></a>

### 第035步：在CENTRAL／00_POWER放置 R_B2_BOT

在 **CENTRAL板的00_POWER图页**，接着放置 **R_B2_BOT**，精确型号 **TNPW060310K0BEEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_B2_BOT | TNPW060310K0BEEA | 1 | 1 | BUCK2_FB | PASSIVE | 从此脚引线，标注精确网名`BUCK2_FB`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK2.4（FB）；00_POWER/R_B2_TOP.2（2）；00_POWER/C_B2_FF.2（2）。 [完整端点N0455](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0455)。 |
| CENTRAL | 00_POWER | R_B2_BOT | TNPW060310K0BEEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_B2_BOT.1=`BUCK2_FB`，R_B2_BOT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-b2-top"></a>

### 第036步：在CENTRAL／00_POWER放置 R_B2_TOP

在 **CENTRAL板的00_POWER图页**，接着放置 **R_B2_TOP**，精确型号 **TNPW0603110KBEEA**，封装 **0603**。其值为 **110k**。

纸面位置：紧邻本页U_BUCK2的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_B2_TOP | TNPW0603110KBEEA | 1 | 1 | V7V15 | PASSIVE | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/L2.2（2）；00_POWER/C_B2_OUT1.1（1）；00_POWER/C_B2_OUT2.1（1）；00_POWER/C_LDO_IN.1（1）；00_POWER/U_LDO.4（EN）；00_POWER/U_LDO.6（IN）；00_POWER/C_B2_BULK.1（1）；00_POWER/C_B2_FF.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |
| CENTRAL | 00_POWER | R_B2_TOP | TNPW0603110KBEEA | 2 | 2 | BUCK2_FB | PASSIVE | 从此脚引线，标注精确网名`BUCK2_FB`；跨页使用同名板内标签。同网还接：00_POWER/U_BUCK2.4（FB）；00_POWER/R_B2_BOT.1（1）；00_POWER/C_B2_FF.2（2）。 [完整端点N0455](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0455)。 |

接完确认：R_B2_TOP.1=`V7V15`，R_B2_TOP.2=`BUCK2_FB`；不可旁路该器件把两个网名短在一起。

<a id="central-u-ldo"></a>

### 第037步：在CENTRAL／00_POWER放置 U_LDO

在 **CENTRAL板的00_POWER图页**，接着放置 **U_LDO**，精确型号 **TPS7A2601DRVR**，封装 **DRV/WSON6 + EP**。

放在7.15V与V5A之间；EP接本板GND。反馈电阻一端接OUT、另一端接FB，不能把反馈全部接地。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | U_LDO | TPS7A2601DRVR | 1 | OUT | V5A | POWER | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 00_POWER | U_LDO | TPS7A2601DRVR | 2 | FB | LDO_FB | IN | 从此脚引线，标注精确网名`LDO_FB`；跨页使用同名板内标签。同网还接：00_POWER/R_LDO_TOP.2（2）；00_POWER/R_LDO_BOT.1（1）。 [完整端点N0566](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0566)。 |
| CENTRAL | 00_POWER | U_LDO | TPS7A2601DRVR | 3 | PG | NC | NC | 此脚在本板只放独立不连接标记；不接任何板内线路、不建立NC网络。 |
| CENTRAL | 00_POWER | U_LDO | TPS7A2601DRVR | 4 | EN | V7V15 | IN | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/L2.2（2）；00_POWER/C_B2_OUT1.1（1）；00_POWER/C_B2_OUT2.1（1）；00_POWER/R_B2_TOP.1（1）；00_POWER/C_LDO_IN.1（1）；00_POWER/U_LDO.6（IN）；00_POWER/C_B2_BULK.1（1）；00_POWER/C_B2_FF.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |
| CENTRAL | 00_POWER | U_LDO | TPS7A2601DRVR | 5 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 00_POWER | U_LDO | TPS7A2601DRVR | 6 | IN | V7V15 | POWER | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/L2.2（2）；00_POWER/C_B2_OUT1.1（1）；00_POWER/C_B2_OUT2.1（1）；00_POWER/R_B2_TOP.1（1）；00_POWER/C_LDO_IN.1（1）；00_POWER/U_LDO.4（EN）；00_POWER/C_B2_BULK.1（1）；00_POWER/C_B2_FF.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |
| CENTRAL | 00_POWER | U_LDO | TPS7A2601DRVR | EP | PAD | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为U_LDO.1→V5A；U_LDO.4→V7V15；U_LDO.5→GND；U_LDO.6→V7V15；U_LDO.EP→GND。 NC脚3逐个单独标记。

<a id="central-c-ldo-in"></a>

### 第038步：在CENTRAL／00_POWER放置 C_LDO_IN

在 **CENTRAL板的00_POWER图页**，接着放置 **C_LDO_IN**，精确型号 **C1210C106K3RACTU**，封装 **1210**。其值为 **10uF**。

纸面位置：紧邻本页U_LDO的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_LDO_IN | C1210C106K3RACTU | 1 | 1 | V7V15 | PASSIVE | 接本板`V7V15`电源/参考标签；来源：本板U_BUCK2经L2输出的约7.15V电源，给LDO输入。同网还接：00_POWER/L2.2（2）；00_POWER/C_B2_OUT1.1（1）；00_POWER/C_B2_OUT2.1（1）；00_POWER/R_B2_TOP.1（1）；00_POWER/U_LDO.4（EN）；00_POWER/U_LDO.6（IN）；00_POWER/C_B2_BULK.1（1）；00_POWER/C_B2_FF.1（1）。 [完整端点N0685](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0685)。 |
| CENTRAL | 00_POWER | C_LDO_IN | C1210C106K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_LDO_IN.1=`V7V15`，C_LDO_IN.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-ldo-out"></a>

### 第039步：在CENTRAL／00_POWER放置 C_LDO_OUT

在 **CENTRAL板的00_POWER图页**，接着放置 **C_LDO_OUT**，精确型号 **C1210C106K3RACTU**，封装 **1210**。其值为 **10uF**。

纸面位置：紧邻本页U_LDO的相应引脚区域。额定条件：25V X7R ±10%; Ceff verification required; 25V X7R; effective>=2.2uF。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_LDO_OUT | C1210C106K3RACTU | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）；00_POWER/R_5M_TOP.1（1）。 |
| CENTRAL | 00_POWER | C_LDO_OUT | C1210C106K3RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_LDO_OUT.1=`V5A`，C_LDO_OUT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-ldo-bot"></a>

### 第040步：在CENTRAL／00_POWER放置 R_LDO_BOT

在 **CENTRAL板的00_POWER图页**，接着放置 **R_LDO_BOT**，精确型号 **TNPW060310K0BEEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_LDO的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_LDO_BOT | TNPW060310K0BEEA | 1 | 1 | LDO_FB | PASSIVE | 从此脚引线，标注精确网名`LDO_FB`；跨页使用同名板内标签。同网还接：00_POWER/R_LDO_TOP.2（2）；00_POWER/U_LDO.2（FB）。 [完整端点N0566](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0566)。 |
| CENTRAL | 00_POWER | R_LDO_BOT | TNPW060310K0BEEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_LDO_BOT.1=`LDO_FB`，R_LDO_BOT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-ldo-top"></a>

### 第041步：在CENTRAL／00_POWER放置 R_LDO_TOP

在 **CENTRAL板的00_POWER图页**，接着放置 **R_LDO_TOP**，精确型号 **TNPW060331K0BEEA**，封装 **0603**。其值为 **31k**。

纸面位置：紧邻本页U_LDO的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_LDO_TOP | TNPW060331K0BEEA | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_V5_BLEED.1（1）；00_POWER/R_5M_TOP.1（1）。 |
| CENTRAL | 00_POWER | R_LDO_TOP | TNPW060331K0BEEA | 2 | 2 | LDO_FB | PASSIVE | 从此脚引线，标注精确网名`LDO_FB`；跨页使用同名板内标签。同网还接：00_POWER/R_LDO_BOT.1（1）；00_POWER/U_LDO.2（FB）。 [完整端点N0566](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0566)。 |

接完确认：R_LDO_TOP.1=`V5A`，R_LDO_TOP.2=`LDO_FB`；不可旁路该器件把两个网名短在一起。

<a id="central-r-v5-bleed"></a>

### 第042步：在CENTRAL／00_POWER放置 R_V5_BLEED

在 **CENTRAL板的00_POWER图页**，接着放置 **R_V5_BLEED**，精确型号 **CRCW06031K00FKEA**，封装 **0603**。其值为 **1k**。

纸面位置：紧邻本页U_LDO的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_V5_BLEED | CRCW06031K00FKEA | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_5M_TOP.1（1）。 |
| CENTRAL | 00_POWER | R_V5_BLEED | CRCW06031K00FKEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_V5_BLEED.1=`V5A`，R_V5_BLEED.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-u-5mon"></a>

### 第043步：在CENTRAL／00_POWER放置 U_5MON

在 **CENTRAL板的00_POWER图页**，接着放置 **U_5MON**，精确型号 **TPS389001DSER**，封装 **DSE/WSON6**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | U_5MON | TPS389001DSER | 1 | SENSE | V5_SENSE | IN | 从此脚引线，标注精确网名`V5_SENSE`；跨页使用同名板内标签。同网还接：00_POWER/R_5M_BOT.1（1）；00_POWER/R_5M_TOP_TRIM.2（2）。 [完整端点N0684](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0684)。 |
| CENTRAL | 00_POWER | U_5MON | TPS389001DSER | 2 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 00_POWER | U_5MON | TPS389001DSER | 3 | MR_N | V3V3 | IN | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | U_5MON | TPS389001DSER | 4 | VDD | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | U_5MON | TPS389001DSER | 5 | CT | V5_CT | PASSIVE | 从此脚引线，标注精确网名`V5_CT`；跨页使用同名板内标签。同网还接：00_POWER/C_5M_CT.1（1）。 [完整端点N0681](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0681)。 |
| CENTRAL | 00_POWER | U_5MON | TPS389001DSER | 6 | RESET_N | V5_GOOD | OD | 从此脚引线，标注精确网名`V5_GOOD`；跨页使用同名板内标签。同网还接：00_POWER/R_5GOOD.1（1）；05_RX_INPUT/U_RXG_UP.1（1A）；05_RX_INPUT/U_RXG_DN.1（1A）；06_I2C_TEMP_SAFETY/U_G1.2（1B）。 [完整端点N0683](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0683)。 |
| CENTRAL | 00_POWER | U_5MON | TPS389001DSER | EP | PAD | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为U_5MON.2→GND；U_5MON.3→V3V3；U_5MON.4→V3V3；U_5MON.EP→GND。

<a id="central-c-u-5mon"></a>

### 第044步：在CENTRAL／00_POWER放置 C_U_5MON

在 **CENTRAL板的00_POWER图页**，接着放置 **C_U_5MON**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_5MON的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_U_5MON | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | C_U_5MON | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_5MON.1=`V3V3`，C_U_5MON.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-5m-ct"></a>

### 第045步：在CENTRAL／00_POWER放置 C_5M_CT

在 **CENTRAL板的00_POWER图页**，接着放置 **C_5M_CT**，精确型号 **C0603C103K5RACTU**，封装 **0603**。其值为 **10nF**。

纸面位置：紧邻本页U_5MON的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_5M_CT | C0603C103K5RACTU | 1 | 1 | V5_CT | PASSIVE | 从此脚引线，标注精确网名`V5_CT`；跨页使用同名板内标签。同网还接：00_POWER/U_5MON.5（CT）。 [完整端点N0681](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0681)。 |
| CENTRAL | 00_POWER | C_5M_CT | C0603C103K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_5M_CT.1=`V5_CT`，C_5M_CT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-5good"></a>

### 第046步：在CENTRAL／00_POWER放置 R_5GOOD

在 **CENTRAL板的00_POWER图页**，接着放置 **R_5GOOD**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_5MON的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_5GOOD | CRCW060310K0FKEA | 1 | 1 | V5_GOOD | PASSIVE | 从此脚引线，标注精确网名`V5_GOOD`；跨页使用同名板内标签。同网还接：00_POWER/U_5MON.6（RESET_N）；05_RX_INPUT/U_RXG_UP.1（1A）；05_RX_INPUT/U_RXG_DN.1（1A）；06_I2C_TEMP_SAFETY/U_G1.2（1B）。 [完整端点N0683](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0683)。 |
| CENTRAL | 00_POWER | R_5GOOD | CRCW060310K0FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_5GOOD.1=`V5_GOOD`，R_5GOOD.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-5m-bot"></a>

### 第047步：在CENTRAL／00_POWER放置 R_5M_BOT

在 **CENTRAL板的00_POWER图页**，接着放置 **R_5M_BOT**，精确型号 **TNPW060310K0BEEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_5MON的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_5M_BOT | TNPW060310K0BEEA | 1 | 1 | V5_SENSE | PASSIVE | 从此脚引线，标注精确网名`V5_SENSE`；跨页使用同名板内标签。同网还接：00_POWER/U_5MON.1（SENSE）；00_POWER/R_5M_TOP_TRIM.2（2）。 [完整端点N0684](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0684)。 |
| CENTRAL | 00_POWER | R_5M_BOT | TNPW060310K0BEEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_5M_BOT.1=`V5_SENSE`，R_5M_BOT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-5m-top"></a>

### 第048步：在CENTRAL／00_POWER放置 R_5M_TOP

在 **CENTRAL板的00_POWER图页**，接着放置 **R_5M_TOP**，精确型号 **TNPW060331K6BEEA**，封装 **0603**。其值为 **31.6k**。

纸面位置：紧邻本页U_5MON的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_5M_TOP | TNPW060331K6BEEA | 1 | 1 | V5A | PASSIVE | 接本板`V5A`电源/参考标签；来源：本板U_LDO.1输出的约5.084V模拟电源。同网另有34个物理端点，逐个见[完整端点N0680](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0680)；例如00_POWER/C_LDO_OUT.1（1）；00_POWER/R_LDO_TOP.1（1）；00_POWER/R_V5_BLEED.1（1）。 |
| CENTRAL | 00_POWER | R_5M_TOP | TNPW060331K6BEEA | 2 | 2 | V5_DIV_MID | PASSIVE | 从此脚引线，标注精确网名`V5_DIV_MID`；跨页使用同名板内标签。同网还接：00_POWER/R_5M_TOP_TRIM.1（1）。 [完整端点N0682](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0682)。 |

接完确认：R_5M_TOP.1=`V5A`，R_5M_TOP.2=`V5_DIV_MID`；不可旁路该器件把两个网名短在一起。

<a id="central-r-5m-top-trim"></a>

### 第049步：在CENTRAL／00_POWER放置 R_5M_TOP_TRIM

在 **CENTRAL板的00_POWER图页**，接着放置 **R_5M_TOP_TRIM**，精确型号 **TNPW0603402RBEEA**，封装 **0603**。其值为 **402**。

纸面位置：紧邻本页U_5MON的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_5M_TOP_TRIM | TNPW0603402RBEEA | 1 | 1 | V5_DIV_MID | PASSIVE | 从此脚引线，标注精确网名`V5_DIV_MID`；跨页使用同名板内标签。同网还接：00_POWER/R_5M_TOP.2（2）。 [完整端点N0682](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0682)。 |
| CENTRAL | 00_POWER | R_5M_TOP_TRIM | TNPW0603402RBEEA | 2 | 2 | V5_SENSE | PASSIVE | 从此脚引线，标注精确网名`V5_SENSE`；跨页使用同名板内标签。同网还接：00_POWER/U_5MON.1（SENSE）；00_POWER/R_5M_BOT.1（1）。 [完整端点N0684](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0684)。 |

接完确认：R_5M_TOP_TRIM.1=`V5_DIV_MID`，R_5M_TOP_TRIM.2=`V5_SENSE`；不可旁路该器件把两个网名短在一起。

<a id="central-u-por"></a>

### 第050步：在CENTRAL／00_POWER放置 U_POR

在 **CENTRAL板的00_POWER图页**，接着放置 **U_POR**，精确型号 **TPS389001DSER**，封装 **DSE/WSON6**。

按本页信号从左至右的流程摆放；以下物理脚号与网络是唯一连接依据，旋转符号不能改变脚号。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | U_POR | TPS389001DSER | 1 | SENSE | U_POR_SENSE | IN | 从此脚引线，标注精确网名`U_POR_SENSE`；跨页使用同名板内标签。同网还接：00_POWER/R_U_POR_TOP.2（2）；00_POWER/R_U_POR_BOT.1（1）。 [完整端点N0676](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0676)。 |
| CENTRAL | 00_POWER | U_POR | TPS389001DSER | 2 | GND | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |
| CENTRAL | 00_POWER | U_POR | TPS389001DSER | 3 | MR_N | V3V3 | IN | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | U_POR | TPS389001DSER | 4 | VDD | V3V3 | POWER | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | U_POR | TPS389001DSER | 5 | CT | U_POR_CT | PASSIVE | 从此脚引线，标注精确网名`U_POR_CT`；跨页使用同名板内标签。同网还接：00_POWER/C_U_POR_CT.1（1）。 [完整端点N0675](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0675)。 |
| CENTRAL | 00_POWER | U_POR | TPS389001DSER | 6 | RESET_N | POR_N | OD | 从此脚引线，标注精确网名`POR_N`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_MUX.3（RESET_N）；00_POWER/R_U_POR_PU.1（1）；06_I2C_TEMP_SAFETY/U_G1.1（1A）。 [完整端点N0574](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0574)。 |
| CENTRAL | 00_POWER | U_POR | TPS389001DSER | EP | PAD | GND | POWER | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：电源/地/参考为U_POR.2→GND；U_POR.3→V3V3；U_POR.4→V3V3；U_POR.EP→GND。

<a id="central-c-u-por"></a>

### 第051步：在CENTRAL／00_POWER放置 C_U_POR

在 **CENTRAL板的00_POWER图页**，接着放置 **C_U_POR**，精确型号 **C0603C104K5RACTU**，封装 **0603**。其值为 **100nF**。

纸面位置：紧邻本页U_POR的相应引脚区域。额定条件：50V X7R ±10%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_U_POR | C0603C104K5RACTU | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | C_U_POR | C0603C104K5RACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_POR.1=`V3V3`，C_U_POR.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-c-u-por-ct"></a>

### 第052步：在CENTRAL／00_POWER放置 C_U_POR_CT

在 **CENTRAL板的00_POWER图页**，接着放置 **C_U_POR_CT**，精确型号 **C0805C103J5GACTU**，封装 **0805**。其值为 **10nF**。

纸面位置：紧邻本页U_POR的相应引脚区域。额定条件：50V C0G ±5%。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | C_U_POR_CT | C0805C103J5GACTU | 1 | 1 | U_POR_CT | PASSIVE | 从此脚引线，标注精确网名`U_POR_CT`；跨页使用同名板内标签。同网还接：00_POWER/U_POR.5（CT）。 [完整端点N0675](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0675)。 |
| CENTRAL | 00_POWER | C_U_POR_CT | C0805C103J5GACTU | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：C_U_POR_CT.1=`U_POR_CT`，C_U_POR_CT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-u-por-bot"></a>

### 第053步：在CENTRAL／00_POWER放置 R_U_POR_BOT

在 **CENTRAL板的00_POWER图页**，接着放置 **R_U_POR_BOT**，精确型号 **TNPW060310K0BEEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_POR的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_U_POR_BOT | TNPW060310K0BEEA | 1 | 1 | U_POR_SENSE | PASSIVE | 从此脚引线，标注精确网名`U_POR_SENSE`；跨页使用同名板内标签。同网还接：00_POWER/U_POR.1（SENSE）；00_POWER/R_U_POR_TOP.2（2）。 [完整端点N0676](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0676)。 |
| CENTRAL | 00_POWER | R_U_POR_BOT | TNPW060310K0BEEA | 2 | 2 | GND | PASSIVE | 直接接本板GND符号；所有本板GND同网。同网另有363个物理端点，逐个见[完整端点N0563](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0563)；例如00_POWER/J_PWR.2（SLEEVE）；00_POWER/D_TVS.2（2）；00_POWER/U_EF.8（GND）。 |

接完确认：R_U_POR_BOT.1=`U_POR_SENSE`，R_U_POR_BOT.2=`GND`；不可旁路该器件把两个网名短在一起。

<a id="central-r-u-por-pu"></a>

### 第054步：在CENTRAL／00_POWER放置 R_U_POR_PU

在 **CENTRAL板的00_POWER图页**，接着放置 **R_U_POR_PU**，精确型号 **CRCW060310K0FKEA**，封装 **0603**。其值为 **10k**。

纸面位置：紧邻本页U_POR的相应引脚区域。额定条件：1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_U_POR_PU | CRCW060310K0FKEA | 1 | 1 | POR_N | PASSIVE | 从此脚引线，标注精确网名`POR_N`；跨页使用同名板内标签。同网还接：06_I2C_TEMP_SAFETY/U_MUX.3（RESET_N）；00_POWER/U_POR.6（RESET_N）；06_I2C_TEMP_SAFETY/U_G1.1（1A）。 [完整端点N0574](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0574)。 |
| CENTRAL | 00_POWER | R_U_POR_PU | CRCW060310K0FKEA | 2 | 2 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |

接完确认：R_U_POR_PU.1=`POR_N`，R_U_POR_PU.2=`V3V3`；不可旁路该器件把两个网名短在一起。

<a id="central-r-u-por-top"></a>

### 第055步：在CENTRAL／00_POWER放置 R_U_POR_TOP

在 **CENTRAL板的00_POWER图页**，接着放置 **R_U_POR_TOP**，精确型号 **TNPW060316K9BEEA**，封装 **0603**。其值为 **16.9k**。

纸面位置：紧邻本页U_POR的相应引脚区域。额定条件：0.1% 0.1W。无极性/双向；本文仍固定物理1/2，便于逐脚核对。

| 板卡 | 图页 | 位号 | 型号 | 物理脚 | 功能 | 网络 | 原表类型 | 具体接法／同网器件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | 00_POWER | R_U_POR_TOP | TNPW060316K9BEEA | 1 | 1 | V3V3 | PASSIVE | 接本板`V3V3`电源/参考标签；来源：本板U_BUCK1经L1输出的3.3V数字电源。同网另有61个物理端点，逐个见[完整端点N0679](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0679)；例如00_POWER/R_EF_FLT.2（2）；00_POWER/L1.2（2）；00_POWER/C_B1_OUT1.1（1）。 |
| CENTRAL | 00_POWER | R_U_POR_TOP | TNPW060316K9BEEA | 2 | 2 | U_POR_SENSE | PASSIVE | 从此脚引线，标注精确网名`U_POR_SENSE`；跨页使用同名板内标签。同网还接：00_POWER/U_POR.1（SENSE）；00_POWER/R_U_POR_BOT.1（1）。 [完整端点N0676](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-n0676)。 |

接完确认：R_U_POR_TOP.1=`V3V3`，R_U_POR_TOP.2=`U_POR_SENSE`；不可旁路该器件把两个网名短在一起。

本页完成核对：**55个器件**各只放置一次；所有上表物理脚已接对应标签或独立NC。跨页的对端位置可沿完整端点链接回查，之后进入下一图页。
