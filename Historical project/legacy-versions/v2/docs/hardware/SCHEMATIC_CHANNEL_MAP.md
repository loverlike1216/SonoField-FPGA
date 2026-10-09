# Schematic channel map — v2 / schematic V1

Native net names are uppercase. RTL identifiers remain case-sensitive. Logical mapping only; physical FPGA/connector pins and VCCO remain BLOCKED.

| Channel | RTL index | Lane / 595 output | Driver / pins in,out | x,y,z mm | Face net |
|---|---|---|---|---|---|
| UPPER_TX_00 | 0 | 0 / QA | U_DRV_U00 / 2,7 | (-42, -42, 50) | U_TX00_FACE |
| UPPER_TX_01 | 1 | 0 / QB | U_DRV_U00 / 4,5 | (-30, -42, 50) | U_TX01_FACE |
| UPPER_TX_02 | 2 | 0 / QC | U_DRV_U02 / 2,7 | (-18, -42, 50) | U_TX02_FACE |
| UPPER_TX_03 | 3 | 0 / QD | U_DRV_U02 / 4,5 | (-6, -42, 50) | U_TX03_FACE |
| UPPER_TX_04 | 4 | 1 / QA | U_DRV_U04 / 2,7 | (6, -42, 50) | U_TX04_FACE |
| UPPER_TX_05 | 5 | 1 / QB | U_DRV_U04 / 4,5 | (18, -42, 50) | U_TX05_FACE |
| UPPER_TX_06 | 6 | 1 / QC | U_DRV_U06 / 2,7 | (30, -42, 50) | U_TX06_FACE |
| UPPER_TX_07 | 7 | 1 / QD | U_DRV_U06 / 4,5 | (42, -42, 50) | U_TX07_FACE |
| UPPER_TX_08 | 8 | 2 / QA | U_DRV_U08 / 2,7 | (-42, -30, 50) | U_TX08_FACE |
| UPPER_TX_09 | 9 | 2 / QB | U_DRV_U08 / 4,5 | (-30, -30, 50) | U_TX09_FACE |
| UPPER_TX_10 | 10 | 2 / QC | U_DRV_U10 / 2,7 | (-18, -30, 50) | U_TX10_FACE |
| UPPER_TX_11 | 11 | 2 / QD | U_DRV_U10 / 4,5 | (-6, -30, 50) | U_TX11_FACE |
| UPPER_TX_12 | 12 | 3 / QA | U_DRV_U12 / 2,7 | (6, -30, 50) | U_TX12_FACE |
| UPPER_TX_13 | 13 | 3 / QB | U_DRV_U12 / 4,5 | (18, -30, 50) | U_TX13_FACE |
| UPPER_TX_14 | 14 | 3 / QC | U_DRV_U14 / 2,7 | (30, -30, 50) | U_TX14_FACE |
| UPPER_TX_15 | 15 | 3 / QD | U_DRV_U14 / 4,5 | (42, -30, 50) | U_TX15_FACE |
| UPPER_TX_16 | 16 | 4 / QA | U_DRV_U16 / 2,7 | (-42, -18, 50) | U_TX16_FACE |
| UPPER_TX_17 | 17 | 4 / QB | U_DRV_U16 / 4,5 | (-30, -18, 50) | U_TX17_FACE |
| UPPER_TX_18 | 18 | 4 / QC | U_DRV_U18 / 2,7 | (-18, -18, 50) | U_TX18_FACE |
| UPPER_TX_19 | 19 | 4 / QD | U_DRV_U18 / 4,5 | (-6, -18, 50) | U_TX19_FACE |
| UPPER_TX_20 | 20 | 5 / QA | U_DRV_U20 / 2,7 | (6, -18, 50) | U_TX20_FACE |
| UPPER_TX_21 | 21 | 5 / QB | U_DRV_U20 / 4,5 | (18, -18, 50) | U_TX21_FACE |
| UPPER_TX_22 | 22 | 5 / QC | U_DRV_U22 / 2,7 | (30, -18, 50) | U_TX22_FACE |
| UPPER_TX_23 | 23 | 5 / QD | U_DRV_U22 / 4,5 | (42, -18, 50) | U_TX23_FACE |
| UPPER_TX_24 | 24 | 6 / QA | U_DRV_U24 / 2,7 | (-42, -6, 50) | U_TX24_FACE |
| UPPER_TX_25 | 25 | 6 / QB | U_DRV_U24 / 4,5 | (-30, -6, 50) | U_TX25_FACE |
| UPPER_TX_26 | 26 | 6 / QC | U_DRV_U26 / 2,7 | (-18, -6, 50) | U_TX26_FACE |
| UPPER_TX_27 | 27 | 6 / QD | U_DRV_U26 / 4,5 | (-6, -6, 50) | U_TX27_FACE |
| UPPER_TX_28 | 28 | 7 / QA | U_DRV_U28 / 2,7 | (6, -6, 50) | U_TX28_FACE |
| UPPER_TX_29 | 29 | 7 / QB | U_DRV_U28 / 4,5 | (18, -6, 50) | U_TX29_FACE |
| UPPER_TX_30 | 30 | 7 / QC | U_DRV_U30 / 2,7 | (30, -6, 50) | U_TX30_FACE |
| UPPER_TX_31 | 31 | 7 / QD | U_DRV_U30 / 4,5 | (42, -6, 50) | U_TX31_FACE |
| UPPER_TX_32 | 32 | 8 / QA | U_DRV_U32 / 2,7 | (-42, 6, 50) | U_TX32_FACE |
| UPPER_TX_33 | 33 | 8 / QB | U_DRV_U32 / 4,5 | (-30, 6, 50) | U_TX33_FACE |
| UPPER_TX_34 | 34 | 8 / QC | U_DRV_U34 / 2,7 | (-18, 6, 50) | U_TX34_FACE |
| UPPER_TX_35 | 35 | 8 / QD | U_DRV_U34 / 4,5 | (-6, 6, 50) | U_TX35_FACE |
| UPPER_TX_36 | 36 | 9 / QA | U_DRV_U36 / 2,7 | (6, 6, 50) | U_TX36_FACE |
| UPPER_TX_37 | 37 | 9 / QB | U_DRV_U36 / 4,5 | (18, 6, 50) | U_TX37_FACE |
| UPPER_TX_38 | 38 | 9 / QC | U_DRV_U38 / 2,7 | (30, 6, 50) | U_TX38_FACE |
| UPPER_TX_39 | 39 | 9 / QD | U_DRV_U38 / 4,5 | (42, 6, 50) | U_TX39_FACE |
| UPPER_TX_40 | 40 | 10 / QA | U_DRV_U40 / 2,7 | (-42, 18, 50) | U_TX40_FACE |
| UPPER_TX_41 | 41 | 10 / QB | U_DRV_U40 / 4,5 | (-30, 18, 50) | U_TX41_FACE |
| UPPER_TX_42 | 42 | 10 / QC | U_DRV_U42 / 2,7 | (-18, 18, 50) | U_TX42_FACE |
| UPPER_TX_43 | 43 | 10 / QD | U_DRV_U42 / 4,5 | (-6, 18, 50) | U_TX43_FACE |
| UPPER_TX_44 | 44 | 11 / QA | U_DRV_U44 / 2,7 | (6, 18, 50) | U_TX44_FACE |
| UPPER_TX_45 | 45 | 11 / QB | U_DRV_U44 / 4,5 | (18, 18, 50) | U_TX45_FACE |
| UPPER_TX_46 | 46 | 11 / QC | U_DRV_U46 / 2,7 | (30, 18, 50) | U_TX46_FACE |
| UPPER_TX_47 | 47 | 11 / QD | U_DRV_U46 / 4,5 | (42, 18, 50) | U_TX47_FACE |
| UPPER_TX_48 | 48 | 12 / QA | U_DRV_U48 / 2,7 | (-42, 30, 50) | U_TX48_FACE |
| UPPER_TX_49 | 49 | 12 / QB | U_DRV_U48 / 4,5 | (-30, 30, 50) | U_TX49_FACE |
| UPPER_TX_50 | 50 | 12 / QC | U_DRV_U50 / 2,7 | (-18, 30, 50) | U_TX50_FACE |
| UPPER_TX_51 | 51 | 12 / QD | U_DRV_U50 / 4,5 | (-6, 30, 50) | U_TX51_FACE |
| UPPER_TX_52 | 52 | 13 / QA | U_DRV_U52 / 2,7 | (6, 30, 50) | U_TX52_FACE |
| UPPER_TX_53 | 53 | 13 / QB | U_DRV_U52 / 4,5 | (18, 30, 50) | U_TX53_FACE |
| UPPER_TX_54 | 54 | 13 / QC | U_DRV_U54 / 2,7 | (30, 30, 50) | U_TX54_FACE |
| UPPER_TX_55 | 55 | 13 / QD | U_DRV_U54 / 4,5 | (42, 30, 50) | U_TX55_FACE |
| UPPER_TX_56 | 56 | 14 / QA | U_DRV_U56 / 2,7 | (-42, 42, 50) | U_TX56_FACE |
| UPPER_TX_57 | 57 | 14 / QB | U_DRV_U56 / 4,5 | (-30, 42, 50) | U_TX57_FACE |
| UPPER_TX_58 | 58 | 14 / QC | U_DRV_U58 / 2,7 | (-18, 42, 50) | U_TX58_FACE |
| UPPER_TX_59 | 59 | 14 / QD | U_DRV_U58 / 4,5 | (-6, 42, 50) | U_TX59_FACE |
| UPPER_TX_60 | 60 | 15 / QA | U_DRV_U60 / 2,7 | (6, 42, 50) | U_TX60_FACE |
| UPPER_TX_61 | 61 | 15 / QB | U_DRV_U60 / 4,5 | (18, 42, 50) | U_TX61_FACE |
| UPPER_TX_62 | 62 | 15 / QC | U_DRV_U62 / 2,7 | (30, 42, 50) | U_TX62_FACE |
| UPPER_TX_63 | 63 | 15 / QD | U_DRV_U62 / 4,5 | (42, 42, 50) | U_TX63_FACE |
| LOWER_TX_00 | 64 | 16 / QA | U_DRV_L00 / 2,7 | (-42, -42, -50) | L_TX00_FACE |
| LOWER_TX_01 | 65 | 16 / QB | U_DRV_L00 / 4,5 | (-30, -42, -50) | L_TX01_FACE |
| LOWER_TX_02 | 66 | 16 / QC | U_DRV_L02 / 2,7 | (-18, -42, -50) | L_TX02_FACE |
| LOWER_TX_03 | 67 | 16 / QD | U_DRV_L02 / 4,5 | (-6, -42, -50) | L_TX03_FACE |
| LOWER_TX_04 | 68 | 17 / QA | U_DRV_L04 / 2,7 | (6, -42, -50) | L_TX04_FACE |
| LOWER_TX_05 | 69 | 17 / QB | U_DRV_L04 / 4,5 | (18, -42, -50) | L_TX05_FACE |
| LOWER_TX_06 | 70 | 17 / QC | U_DRV_L06 / 2,7 | (30, -42, -50) | L_TX06_FACE |
| LOWER_TX_07 | 71 | 17 / QD | U_DRV_L06 / 4,5 | (42, -42, -50) | L_TX07_FACE |
| LOWER_TX_08 | 72 | 18 / QA | U_DRV_L08 / 2,7 | (-42, -30, -50) | L_TX08_FACE |
| LOWER_TX_09 | 73 | 18 / QB | U_DRV_L08 / 4,5 | (-30, -30, -50) | L_TX09_FACE |
| LOWER_TX_10 | 74 | 18 / QC | U_DRV_L10 / 2,7 | (-18, -30, -50) | L_TX10_FACE |
| LOWER_TX_11 | 75 | 18 / QD | U_DRV_L10 / 4,5 | (-6, -30, -50) | L_TX11_FACE |
| LOWER_TX_12 | 76 | 19 / QA | U_DRV_L12 / 2,7 | (6, -30, -50) | L_TX12_FACE |
| LOWER_TX_13 | 77 | 19 / QB | U_DRV_L12 / 4,5 | (18, -30, -50) | L_TX13_FACE |
| LOWER_TX_14 | 78 | 19 / QC | U_DRV_L14 / 2,7 | (30, -30, -50) | L_TX14_FACE |
| LOWER_TX_15 | 79 | 19 / QD | U_DRV_L14 / 4,5 | (42, -30, -50) | L_TX15_FACE |
| LOWER_TX_16 | 80 | 20 / QA | U_DRV_L16 / 2,7 | (-42, -18, -50) | L_TX16_FACE |
| LOWER_TX_17 | 81 | 20 / QB | U_DRV_L16 / 4,5 | (-30, -18, -50) | L_TX17_FACE |
| LOWER_TX_18 | 82 | 20 / QC | U_DRV_L18 / 2,7 | (-18, -18, -50) | L_TX18_FACE |
| LOWER_TX_19 | 83 | 20 / QD | U_DRV_L18 / 4,5 | (-6, -18, -50) | L_TX19_FACE |
| LOWER_TX_20 | 84 | 21 / QA | U_DRV_L20 / 2,7 | (6, -18, -50) | L_TX20_FACE |
| LOWER_TX_21 | 85 | 21 / QB | U_DRV_L20 / 4,5 | (18, -18, -50) | L_TX21_FACE |
| LOWER_TX_22 | 86 | 21 / QC | U_DRV_L22 / 2,7 | (30, -18, -50) | L_TX22_FACE |
| LOWER_TX_23 | 87 | 21 / QD | U_DRV_L22 / 4,5 | (42, -18, -50) | L_TX23_FACE |
| LOWER_TX_24 | 88 | 22 / QA | U_DRV_L24 / 2,7 | (-42, -6, -50) | L_TX24_FACE |
| LOWER_TX_25 | 89 | 22 / QB | U_DRV_L24 / 4,5 | (-30, -6, -50) | L_TX25_FACE |
| LOWER_TX_26 | 90 | 22 / QC | U_DRV_L26 / 2,7 | (-18, -6, -50) | L_TX26_FACE |
| LOWER_TX_27 | 91 | 22 / QD | U_DRV_L26 / 4,5 | (-6, -6, -50) | L_TX27_FACE |
| LOWER_TX_28 | 92 | 23 / QA | U_DRV_L28 / 2,7 | (6, -6, -50) | L_TX28_FACE |
| LOWER_TX_29 | 93 | 23 / QB | U_DRV_L28 / 4,5 | (18, -6, -50) | L_TX29_FACE |
| LOWER_TX_30 | 94 | 23 / QC | U_DRV_L30 / 2,7 | (30, -6, -50) | L_TX30_FACE |
| LOWER_TX_31 | 95 | 23 / QD | U_DRV_L30 / 4,5 | (42, -6, -50) | L_TX31_FACE |
| LOWER_TX_32 | 96 | 24 / QA | U_DRV_L32 / 2,7 | (-42, 6, -50) | L_TX32_FACE |
| LOWER_TX_33 | 97 | 24 / QB | U_DRV_L32 / 4,5 | (-30, 6, -50) | L_TX33_FACE |
| LOWER_TX_34 | 98 | 24 / QC | U_DRV_L34 / 2,7 | (-18, 6, -50) | L_TX34_FACE |
| LOWER_TX_35 | 99 | 24 / QD | U_DRV_L34 / 4,5 | (-6, 6, -50) | L_TX35_FACE |
| LOWER_TX_36 | 100 | 25 / QA | U_DRV_L36 / 2,7 | (6, 6, -50) | L_TX36_FACE |
| LOWER_TX_37 | 101 | 25 / QB | U_DRV_L36 / 4,5 | (18, 6, -50) | L_TX37_FACE |
| LOWER_TX_38 | 102 | 25 / QC | U_DRV_L38 / 2,7 | (30, 6, -50) | L_TX38_FACE |
| LOWER_TX_39 | 103 | 25 / QD | U_DRV_L38 / 4,5 | (42, 6, -50) | L_TX39_FACE |
| LOWER_TX_40 | 104 | 26 / QA | U_DRV_L40 / 2,7 | (-42, 18, -50) | L_TX40_FACE |
| LOWER_TX_41 | 105 | 26 / QB | U_DRV_L40 / 4,5 | (-30, 18, -50) | L_TX41_FACE |
| LOWER_TX_42 | 106 | 26 / QC | U_DRV_L42 / 2,7 | (-18, 18, -50) | L_TX42_FACE |
| LOWER_TX_43 | 107 | 26 / QD | U_DRV_L42 / 4,5 | (-6, 18, -50) | L_TX43_FACE |
| LOWER_TX_44 | 108 | 27 / QA | U_DRV_L44 / 2,7 | (6, 18, -50) | L_TX44_FACE |
| LOWER_TX_45 | 109 | 27 / QB | U_DRV_L44 / 4,5 | (18, 18, -50) | L_TX45_FACE |
| LOWER_TX_46 | 110 | 27 / QC | U_DRV_L46 / 2,7 | (30, 18, -50) | L_TX46_FACE |
| LOWER_TX_47 | 111 | 27 / QD | U_DRV_L46 / 4,5 | (42, 18, -50) | L_TX47_FACE |
| LOWER_TX_48 | 112 | 28 / QA | U_DRV_L48 / 2,7 | (-42, 30, -50) | L_TX48_FACE |
| LOWER_TX_49 | 113 | 28 / QB | U_DRV_L48 / 4,5 | (-30, 30, -50) | L_TX49_FACE |
| LOWER_TX_50 | 114 | 28 / QC | U_DRV_L50 / 2,7 | (-18, 30, -50) | L_TX50_FACE |
| LOWER_TX_51 | 115 | 28 / QD | U_DRV_L50 / 4,5 | (-6, 30, -50) | L_TX51_FACE |
| LOWER_TX_52 | 116 | 29 / QA | U_DRV_L52 / 2,7 | (6, 30, -50) | L_TX52_FACE |
| LOWER_TX_53 | 117 | 29 / QB | U_DRV_L52 / 4,5 | (18, 30, -50) | L_TX53_FACE |
| LOWER_TX_54 | 118 | 29 / QC | U_DRV_L54 / 2,7 | (30, 30, -50) | L_TX54_FACE |
| LOWER_TX_55 | 119 | 29 / QD | U_DRV_L54 / 4,5 | (42, 30, -50) | L_TX55_FACE |
| LOWER_TX_56 | 120 | 30 / QA | U_DRV_L56 / 2,7 | (-42, 42, -50) | L_TX56_FACE |
| LOWER_TX_57 | 121 | 30 / QB | U_DRV_L56 / 4,5 | (-30, 42, -50) | L_TX57_FACE |
| LOWER_TX_58 | 122 | 30 / QC | U_DRV_L58 / 2,7 | (-18, 42, -50) | L_TX58_FACE |
| LOWER_TX_59 | 123 | 30 / QD | U_DRV_L58 / 4,5 | (-6, 42, -50) | L_TX59_FACE |
| LOWER_TX_60 | 124 | 31 / QA | U_DRV_L60 / 2,7 | (6, 42, -50) | L_TX60_FACE |
| LOWER_TX_61 | 125 | 31 / QB | U_DRV_L60 / 4,5 | (18, 42, -50) | L_TX61_FACE |
| LOWER_TX_62 | 126 | 31 / QC | U_DRV_L62 / 2,7 | (30, 42, -50) | L_TX62_FACE |
| LOWER_TX_63 | 127 | 31 / QD | U_DRV_L62 / 4,5 | (42, 42, -50) | L_TX63_FACE |

## Interface case mapping

| RTL / logical identifier | Native electrical net |
|---|---|
| `serial_data[0]` | `SERIAL_DATA[0]` |
| `serial_data[1]` | `SERIAL_DATA[1]` |
| `serial_data[2]` | `SERIAL_DATA[2]` |
| `serial_data[3]` | `SERIAL_DATA[3]` |
| `serial_data[4]` | `SERIAL_DATA[4]` |
| `serial_data[5]` | `SERIAL_DATA[5]` |
| `serial_data[6]` | `SERIAL_DATA[6]` |
| `serial_data[7]` | `SERIAL_DATA[7]` |
| `serial_data[8]` | `SERIAL_DATA[8]` |
| `serial_data[9]` | `SERIAL_DATA[9]` |
| `serial_data[10]` | `SERIAL_DATA[10]` |
| `serial_data[11]` | `SERIAL_DATA[11]` |
| `serial_data[12]` | `SERIAL_DATA[12]` |
| `serial_data[13]` | `SERIAL_DATA[13]` |
| `serial_data[14]` | `SERIAL_DATA[14]` |
| `serial_data[15]` | `SERIAL_DATA[15]` |
| `serial_data[16]` | `SERIAL_DATA[16]` |
| `serial_data[17]` | `SERIAL_DATA[17]` |
| `serial_data[18]` | `SERIAL_DATA[18]` |
| `serial_data[19]` | `SERIAL_DATA[19]` |
| `serial_data[20]` | `SERIAL_DATA[20]` |
| `serial_data[21]` | `SERIAL_DATA[21]` |
| `serial_data[22]` | `SERIAL_DATA[22]` |
| `serial_data[23]` | `SERIAL_DATA[23]` |
| `serial_data[24]` | `SERIAL_DATA[24]` |
| `serial_data[25]` | `SERIAL_DATA[25]` |
| `serial_data[26]` | `SERIAL_DATA[26]` |
| `serial_data[27]` | `SERIAL_DATA[27]` |
| `serial_data[28]` | `SERIAL_DATA[28]` |
| `serial_data[29]` | `SERIAL_DATA[29]` |
| `serial_data[30]` | `SERIAL_DATA[30]` |
| `serial_data[31]` | `SERIAL_DATA[31]` |
| `shift_clock` | `SHIFT_CLOCK` |
| `latch_clock` | `LATCH_CLOCK` |
| `output_disable` | `OUTPUT_DISABLE` |
| `adc_reset` | `ADC_RESET` |
| `adc_convst` | `ADC_CONVST` |
| `adc_cs_n` | `ADC_CS_N` |
| `adc_sclk` | `ADC_SCLK` |
| `adc_sdi` | `ADC_SDI` |
| `adc_busy` | `ADC_BUSY` |
| `adc_dout[0]` | `ADC_DOUT[0]` |
| `adc_dout[1]` | `ADC_DOUT[1]` |
| `adc_dout[2]` | `ADC_DOUT[2]` |
| `adc_dout[3]` | `ADC_DOUT[3]` |
| `rx_blank[0]` | `RX_BLANK[0]` |
| `rx_blank[1]` | `RX_BLANK[1]` |
| `hardware_enable` | `HARDWARE_ENABLE` |
| `rst_n` | `RST_N` |
| `LEVEL_OE_N` | `LEVEL_OE_N` |
| `VCCO_FPGA` | `VCCO_FPGA` |
| `SYSTEM_GND` | `SYSTEM_GND` |

## RX and serial order

UPPER_RX0–3 map to ADC V1–V4 (software 0–3); LOWER_RX0–3 map to V5–V8 (4–7). Each lane shifts bit3 first and bit0 last, so QA/QB/QC/QD hold channels 4L+0/1/2/3. QH-prime is not cascaded. The audit proves named connectivity, not propagation delay, ADC settling or independent safety.
