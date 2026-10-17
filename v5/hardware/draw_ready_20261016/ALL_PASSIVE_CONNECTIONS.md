# 所有必要无源双端连接

| board | refdes | mpn | value | pin1_net | pin2_net | package | rating | polarity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CENTRAL | F1 | 0451003.MRL | 3A fast fuse | DC12_RAW | DC12_FUSED | 2410 | 3A; >=32VDC; Littelfuse0451003.MRL; normal budget<2.2A | nonpolar/bidirectional |
| CENTRAL | D_TVS | SMBJ15CA | SMBJ15CA | V12_SW | GND | DO-214AA | bidirectional 15V VRWM; clamp/source energy not certified | nonpolar/bidirectional |
| CENTRAL | R_UV_TOP | TNPW0805383KBEEA | 383k | DC12_AFTER_SWITCH | EF_EN | 0805 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_UV_BOT | TNPW060359K0BEEA | 59k | EF_EN | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_OV_TOP | TNPW0805392KBEEA | 392k | DC12_AFTER_SWITCH | EF_OV | 0805 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_OV_BOT | TNPW060338K3BEEA | 38.3k | EF_OV | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ILM | CRCW06031K30FKEA | 1.3k | EF_ILM | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_DVDT | C0603C103K5RACTU | 10nF | EF_DVDT | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_EF_FLT | CRCW060310K0FKEA | 10k | EF_FLT_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_EF_OUT | EEEFK1V470P | 47uF | V12_SW | GND | Panasonic FK 6.3mm can | 35V 47uF ±20%; positive=pin1; EEEFK1V470P | pin1 positive |
| CENTRAL | C_B1_IN | C1210C106K3RACTU | 10uF | V12_SW | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V | nonpolar/bidirectional |
| CENTRAL | C_B1_HF | C0603C104K5RACTU | 100nF | V12_SW | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_B1_BOOT | C0603C104K5RACTU | 100nF | BUCK1_BOOT | BUCK1_SW | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | L1 | XAL7070-223MEC | XAL7070-223MEC 22uH | BUCK1_SW | V3V3 | XAL7070 | DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise | nonpolar/bidirectional |
| CENTRAL | C_B1_OUT1 | C1210C226K3RACTU | 22uF | V3V3 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| CENTRAL | C_B1_OUT2 | C1210C226K3RACTU | 22uF | V3V3 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| CENTRAL | R_B1_TOP | TNPW060345K3BEEA | 45.3k | V3V3 | BUCK1_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_B1_BOT | TNPW060310K0BEEA | 10k | BUCK1_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_B2_IN | C1210C106K3RACTU | 10uF | V12_SW | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V | nonpolar/bidirectional |
| CENTRAL | C_B2_HF | C0603C104K5RACTU | 100nF | V12_SW | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_B2_BOOT | C0603C104K5RACTU | 100nF | BUCK2_BOOT | BUCK2_SW | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | L2 | XAL7070-223MEC | XAL7070-223MEC 22uH | BUCK2_SW | V7V15 | XAL7070 | DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise | nonpolar/bidirectional |
| CENTRAL | C_B2_OUT1 | C1210C226K3RACTU | 22uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| CENTRAL | C_B2_OUT2 | C1210C226K3RACTU | 22uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| CENTRAL | R_B2_TOP | TNPW0603110KBEEA | 110k | V7V15 | BUCK2_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_B2_BOT | TNPW060310K0BEEA | 10k | BUCK2_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_LDO_IN | C1210C106K3RACTU | 10uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required | nonpolar/bidirectional |
| CENTRAL | C_LDO_OUT | C1210C106K3RACTU | 10uF | V5A | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective>=2.2uF | nonpolar/bidirectional |
| CENTRAL | R_LDO_TOP | TNPW060331K0BEEA | 31k | V5A | LDO_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_LDO_BOT | TNPW060310K0BEEA | 10k | LDO_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_V5_BLEED | CRCW06031K00FKEA | 1k | V5A | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_5MON | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_5M_TOP | TNPW060331K6BEEA | 31.6k | V5A | V5_DIV_MID | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_5M_BOT | TNPW060310K0BEEA | 10k | V5_SENSE | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_5M_CT | C0603C103K5RACTU | 10nF | V5_CT | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_5GOOD | CRCW060310K0FKEA | 10k | V5_GOOD | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | F1 | 0451003.MRL | 3A fast fuse | DC12_RAW | DC12_FUSED | 2410 | 3A; >=32VDC; Littelfuse0451003.MRL; normal budget<2.2A | nonpolar/bidirectional |
| DN | F1 | 0451003.MRL | 3A fast fuse | DC12_RAW | DC12_FUSED | 2410 | 3A; >=32VDC; Littelfuse0451003.MRL; normal budget<2.2A | nonpolar/bidirectional |
| UP | D_TVS | SMBJ15CA | SMBJ15CA | V12_SW | GND | DO-214AA | bidirectional 15V VRWM; clamp/source energy not certified | nonpolar/bidirectional |
| DN | D_TVS | SMBJ15CA | SMBJ15CA | V12_SW | GND | DO-214AA | bidirectional 15V VRWM; clamp/source energy not certified | nonpolar/bidirectional |
| UP | R_UV_TOP | TNPW0805383KBEEA | 383k | DC12_AFTER_SWITCH | EF_EN | 0805 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_UV_TOP | TNPW0805383KBEEA | 383k | DC12_AFTER_SWITCH | EF_EN | 0805 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_UV_BOT | TNPW060359K0BEEA | 59k | EF_EN | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_UV_BOT | TNPW060359K0BEEA | 59k | EF_EN | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_OV_TOP | TNPW0805392KBEEA | 392k | DC12_AFTER_SWITCH | EF_OV | 0805 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_OV_TOP | TNPW0805392KBEEA | 392k | DC12_AFTER_SWITCH | EF_OV | 0805 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_OV_BOT | TNPW060338K3BEEA | 38.3k | EF_OV | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_OV_BOT | TNPW060338K3BEEA | 38.3k | EF_OV | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_ILM | CRCW06031K30FKEA | 1.3k | EF_ILM | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_ILM | CRCW06031K30FKEA | 1.3k | EF_ILM | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_DVDT | C0603C103K5RACTU | 10nF | EF_DVDT | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_DVDT | C0603C103K5RACTU | 10nF | EF_DVDT | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_EF_FLT | CRCW060310K0FKEA | 10k | EF_FLT_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_EF_FLT | CRCW060310K0FKEA | 10k | EF_FLT_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_EF_OUT | EEEFK1V470P | 47uF | V12_SW | GND | Panasonic FK 6.3mm can | 35V 47uF ±20%; positive=pin1; EEEFK1V470P | pin1 positive |
| DN | C_EF_OUT | EEEFK1V470P | 47uF | V12_SW | GND | Panasonic FK 6.3mm can | 35V 47uF ±20%; positive=pin1; EEEFK1V470P | pin1 positive |
| UP | C_B1_IN | C1210C106K3RACTU | 10uF | V12_SW | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V | nonpolar/bidirectional |
| DN | C_B1_IN | C1210C106K3RACTU | 10uF | V12_SW | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V | nonpolar/bidirectional |
| UP | C_B1_HF | C0603C104K5RACTU | 100nF | V12_SW | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_B1_HF | C0603C104K5RACTU | 100nF | V12_SW | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_B1_BOOT | C0603C104K5RACTU | 100nF | BUCK1_BOOT | BUCK1_SW | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_B1_BOOT | C0603C104K5RACTU | 100nF | BUCK1_BOOT | BUCK1_SW | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | L1 | XAL7070-223MEC | XAL7070-223MEC 22uH | BUCK1_SW | V3V3 | XAL7070 | DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise | nonpolar/bidirectional |
| DN | L1 | XAL7070-223MEC | XAL7070-223MEC 22uH | BUCK1_SW | V3V3 | XAL7070 | DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise | nonpolar/bidirectional |
| UP | C_B1_OUT1 | C1210C226K3RACTU | 22uF | V3V3 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| DN | C_B1_OUT1 | C1210C226K3RACTU | 22uF | V3V3 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| UP | C_B1_OUT2 | C1210C226K3RACTU | 22uF | V3V3 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| DN | C_B1_OUT2 | C1210C226K3RACTU | 22uF | V3V3 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| UP | R_B1_TOP | TNPW060345K3BEEA | 45.3k | V3V3 | BUCK1_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_B1_TOP | TNPW060345K3BEEA | 45.3k | V3V3 | BUCK1_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_B1_BOT | TNPW060310K0BEEA | 10k | BUCK1_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_B1_BOT | TNPW060310K0BEEA | 10k | BUCK1_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | C_B2_IN | C1210C106K3RACTU | 10uF | V12_SW | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V | nonpolar/bidirectional |
| DN | C_B2_IN | C1210C106K3RACTU | 10uF | V12_SW | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V | nonpolar/bidirectional |
| UP | C_B2_HF | C0603C104K5RACTU | 100nF | V12_SW | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_B2_HF | C0603C104K5RACTU | 100nF | V12_SW | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_B2_BOOT | C0603C104K5RACTU | 100nF | BUCK2_BOOT | BUCK2_SW | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_B2_BOOT | C0603C104K5RACTU | 100nF | BUCK2_BOOT | BUCK2_SW | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | L2 | XAL7070-223MEC | XAL7070-223MEC 22uH | BUCK2_SW | V7V15 | XAL7070 | DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise | nonpolar/bidirectional |
| DN | L2 | XAL7070-223MEC | XAL7070-223MEC 22uH | BUCK2_SW | V7V15 | XAL7070 | DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise | nonpolar/bidirectional |
| UP | C_B2_OUT1 | C1210C226K3RACTU | 22uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| DN | C_B2_OUT1 | C1210C226K3RACTU | 22uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| UP | C_B2_OUT2 | C1210C226K3RACTU | 22uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| DN | C_B2_OUT2 | C1210C226K3RACTU | 22uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| UP | R_B2_TOP | TNPW0603110KBEEA | 110k | V7V15 | BUCK2_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_B2_TOP | TNPW0603110KBEEA | 110k | V7V15 | BUCK2_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_B2_BOT | TNPW060310K0BEEA | 10k | BUCK2_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_B2_BOT | TNPW060310K0BEEA | 10k | BUCK2_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | C_B3_IN | C1210C106K3RACTU | 10uF | V12_SW | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V | nonpolar/bidirectional |
| DN | C_B3_IN | C1210C106K3RACTU | 10uF | V12_SW | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective C >=4.7uF at 12V | nonpolar/bidirectional |
| UP | C_B3_HF | C0603C104K5RACTU | 100nF | V12_SW | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_B3_HF | C0603C104K5RACTU | 100nF | V12_SW | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_B3_BOOT | C0603C104K5RACTU | 100nF | BUCK3_BOOT | BUCK3_SW | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_B3_BOOT | C0603C104K5RACTU | 100nF | BUCK3_BOOT | BUCK3_SW | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | L3 | XAL7070-223MEC | XAL7070-223MEC 22uH | BUCK3_SW | VTX_PRE | XAL7070 | DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise | nonpolar/bidirectional |
| DN | L3 | XAL7070-223MEC | XAL7070-223MEC 22uH | BUCK3_SW | VTX_PRE | XAL7070 | DCRmax39.7mOhm; Isat5.6A@30% at25C; Irms4.7A@20C rise | nonpolar/bidirectional |
| UP | C_B3_OUT1 | C1210C226K3RACTU | 22uF | VTX_PRE | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| DN | C_B3_OUT1 | C1210C226K3RACTU | 22uF | VTX_PRE | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| UP | C_B3_OUT2 | C1210C226K3RACTU | 22uF | VTX_PRE | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| DN | C_B3_OUT2 | C1210C226K3RACTU | 22uF | VTX_PRE | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; pair effective C >=20uF at rail voltage | nonpolar/bidirectional |
| UP | R_B3_TOP | TNPW0603158KBEEA | 158k | VTX_PRE | BUCK3_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_B3_TOP | TNPW0603158KBEEA | 158k | VTX_PRE | BUCK3_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_B3_BOT | TNPW060310K0BEEA | 10k | BUCK3_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_B3_BOT | TNPW060310K0BEEA | 10k | BUCK3_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | C_LDO_IN | C1210C106K3RACTU | 10uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required | nonpolar/bidirectional |
| DN | C_LDO_IN | C1210C106K3RACTU | 10uF | V7V15 | GND | 1210 | 25V X7R ±10%; Ceff verification required | nonpolar/bidirectional |
| UP | C_LDO_OUT | C1210C106K3RACTU | 10uF | V5A | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective>=2.2uF | nonpolar/bidirectional |
| DN | C_LDO_OUT | C1210C106K3RACTU | 10uF | V5A | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective>=2.2uF | nonpolar/bidirectional |
| UP | R_LDO_TOP | TNPW060331K0BEEA | 31k | V5A | LDO_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_LDO_TOP | TNPW060331K0BEEA | 31k | V5A | LDO_FB | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_LDO_BOT | TNPW060310K0BEEA | 10k | LDO_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_LDO_BOT | TNPW060310K0BEEA | 10k | LDO_FB | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_V5_BLEED | CRCW06031K00FKEA | 1k | V5A | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_V5_BLEED | CRCW06031K00FKEA | 1k | V5A | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_U_5MON | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_5MON | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_5M_TOP | TNPW060331K6BEEA | 31.6k | V5A | V5_DIV_MID | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_5M_TOP | TNPW060331K6BEEA | 31.6k | V5A | V5_DIV_MID | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_5M_BOT | TNPW060310K0BEEA | 10k | V5_SENSE | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_5M_BOT | TNPW060310K0BEEA | 10k | V5_SENSE | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | C_5M_CT | C0603C103K5RACTU | 10nF | V5_CT | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_5M_CT | C0603C103K5RACTU | 10nF | V5_CT | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_5GOOD | CRCW060310K0FKEA | 10k | V5_GOOD | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_5GOOD | CRCW060310K0FKEA | 10k | V5_GOOD | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_CBUF1 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_CBUF2 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_DEF_MASTER_OE_N | CRCW060310K0FKEA | 10k | MASTER_OE_N | AX_VIO_REF3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_OFF_MASTER_OE_N | CRCW0603100KFKEA | 100k | MASTER_OE_N | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_DEF_UP_RX_BLANK_RAW | CRCW060310K0FKEA | 10k | UP_RX_BLANK_RAW | AX_VIO_REF3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_OFF_UP_RX_BLANK_RAW | CRCW0603100KFKEA | 100k | UP_RX_BLANK_RAW | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_DEF_DN_RX_BLANK_RAW | CRCW060310K0FKEA | 10k | DN_RX_BLANK_RAW | AX_VIO_REF3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_OFF_DN_RX_BLANK_RAW | CRCW0603100KFKEA | 100k | DN_RX_BLANK_RAW | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_UP_OE_N_B | CRCW060333R0FKEA | 33 | UP_OE_N_B | UP_OE_N | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_DN_OE_N_B | CRCW060333R0FKEA | 33 | DN_OE_N_B | DN_OE_N | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_UP_TX_PERMIT_B | CRCW060333R0FKEA | 33 | UP_TX_PERMIT_B | UP_TX_PERMIT | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_DN_TX_PERMIT_B | CRCW060333R0FKEA | 33 | DN_TX_PERMIT_B | DN_TX_PERMIT | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_UP_RX_BLANK_B | CRCW060333R0FKEA | 33 | UP_RX_BLANK_B | UP_RX_BLANK | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_DN_RX_BLANK_B | CRCW060333R0FKEA | 33 | DN_RX_BLANK_B | DN_RX_BLANK | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_UP_HB_B | CRCW060333R0FKEA | 33 | UP_HB_B | UP_HB | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_DN_HB_B | CRCW060333R0FKEA | 33 | DN_HB_B | DN_HB | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_UP_CENTRAL_POWER_OK_B | CRCW060333R0FKEA | 33 | UP_CENTRAL_POWER_OK_B | UP_CENTRAL_POWER_OK | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_SRC_DN_CENTRAL_POWER_OK_B | CRCW060333R0FKEA | 33 | DN_CENTRAL_POWER_OK_B | DN_CENTRAL_POWER_OK | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_PG_UP | CRCW060310K0FKEA | 10k | UP_PGOOD | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_FAULT_UP | CRCW060310K0FKEA | 10k | UP_FAULT_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_PG_DN | CRCW060310K0FKEA | 10k | DN_PGOOD | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_FAULT_DN | CRCW060310K0FKEA | 10k | DN_FAULT_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_ADCBUF | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_ADC_SCLK | CRCW060333R0FKEA | 33 | ADC_SCLK_B | ADC_SCLK | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_CONVST | CRCW060333R0FKEA | 33 | ADC_CONVST_B | ADC_CONVST | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_CS_N | CRCW060333R0FKEA | 33 | ADC_CS_N_B | ADC_CS_N | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_SDI | CRCW060333R0FKEA | 33 | ADC_SDI_B | ADC_SDI | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RESET | CRCW060333R0FKEA | 33 | ADC_RESET_B | ADC_RESET | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_PD_SCLK | CRCW060310K0FKEA | 10k | ADC_SCLK_FPGA | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_PD_CONVST | CRCW060310K0FKEA | 10k | ADC_CONVST_FPGA | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_PD_SDI | CRCW060310K0FKEA | 10k | ADC_SDI_FPGA | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_PU_CS_N | CRCW060310K0FKEA | 10k | ADC_CS_N_FPGA | AX_VIO_REF3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_OFF_CS_N | CRCW0603100KFKEA | 100k | ADC_CS_N_FPGA | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_PU_RESET | CRCW060310K0FKEA | 10k | ADC_RESET_FPGA | AX_VIO_REF3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_OFF_RESET | CRCW0603100KFKEA | 100k | ADC_RESET_FPGA | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_SAFE_SCLK | CRCW060310K0FKEA | 10k | ADC_SCLK | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_SAFE_CONVST | CRCW060310K0FKEA | 10k | ADC_CONVST | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_SAFE_CS_N | CRCW060310K0FKEA | 10k | ADC_CS_N | V5A | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_SAFE_SDI | CRCW060310K0FKEA | 10k | ADC_SDI | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_SAFE_RESET | CRCW060310K0FKEA | 10k | ADC_RESET | V5A | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_DOUTA | CRCW0603100KFKEA | 100k | ADC_DOUTA | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_DOUTB | CRCW0603100KFKEA | 100k | ADC_DOUTB | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_DOUTC | CRCW0603100KFKEA | 100k | ADC_DOUTC | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_DOUTD | CRCW0603100KFKEA | 100k | ADC_DOUTD | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_BUSY | CRCW0603100KFKEA | 100k | ADC_BUSY | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_AV1 | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_ADC_AV37 | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_ADC_AV38 | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_ADC_AV48 | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_ADC_AV_BULK | C1210C106K3RACTU | 10uF | V5A | GND | 1210 | 25V X7R ±10%; Ceff verification required | nonpolar/bidirectional |
| CENTRAL | C_ADC_D | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_ADC_D_BULK | C0603C105K3RACTU | 1uF | V5A | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_REG36 | C0603C105K3RACTU | 1uF | ADC_REGCAP36 | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_REG39 | C0603C105K3RACTU | 1uF | ADC_REGCAP39 | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_ADC_REF | C0603C104K5RACTU | 100nF | ADC_REF25 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_ADC_REFCAP | C1210C226K3RACTU | 22uF | ADC_REFCAP | GND | 1210 | 25V X7R ±10%; Ceff verification required; 25V X7R; effective>=10uF at4.4V | nonpolar/bidirectional |
| CENTRAL | C_U_BLANKINV_UP | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_RXG_UP | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_RXSW_UP | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_ADC_IN0 | CRCW0603499RFKEA | 499 | UP_RX0_SW | ADC_IN0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_IN0 | C0603C102J5GACTU | 1nF | ADC_IN0 | GND | 0603 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | R_ADC_BLEED0 | CRCW06031M00FKEA | 1M | ADC_IN0 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_IN1 | CRCW0603499RFKEA | 499 | UP_RX1_SW | ADC_IN1 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_IN1 | C0603C102J5GACTU | 1nF | ADC_IN1 | GND | 0603 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | R_ADC_BLEED1 | CRCW06031M00FKEA | 1M | ADC_IN1 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_IN2 | CRCW0603499RFKEA | 499 | UP_RX2_SW | ADC_IN2 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_IN2 | C0603C102J5GACTU | 1nF | ADC_IN2 | GND | 0603 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | R_ADC_BLEED2 | CRCW06031M00FKEA | 1M | ADC_IN2 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_IN3 | CRCW0603499RFKEA | 499 | UP_RX3_SW | ADC_IN3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_IN3 | C0603C102J5GACTU | 1nF | ADC_IN3 | GND | 0603 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | R_ADC_BLEED3 | CRCW06031M00FKEA | 1M | ADC_IN3 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_BLANKINV_DN | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_RXG_DN | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_RXSW_DN | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_ADC_IN4 | CRCW0603499RFKEA | 499 | DN_RX0_SW | ADC_IN4 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_IN4 | C0603C102J5GACTU | 1nF | ADC_IN4 | GND | 0603 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | R_ADC_BLEED4 | CRCW06031M00FKEA | 1M | ADC_IN4 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_IN5 | CRCW0603499RFKEA | 499 | DN_RX1_SW | ADC_IN5 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_IN5 | C0603C102J5GACTU | 1nF | ADC_IN5 | GND | 0603 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | R_ADC_BLEED5 | CRCW06031M00FKEA | 1M | ADC_IN5 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_IN6 | CRCW0603499RFKEA | 499 | DN_RX2_SW | ADC_IN6 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_IN6 | C0603C102J5GACTU | 1nF | ADC_IN6 | GND | 0603 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | R_ADC_BLEED6 | CRCW06031M00FKEA | 1M | ADC_IN6 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_IN7 | CRCW0603499RFKEA | 499 | DN_RX3_SW | ADC_IN7 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_ADC_IN7 | C0603C102J5GACTU | 1nF | ADC_IN7 | GND | 0603 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | R_ADC_BLEED7 | CRCW06031M00FKEA | 1M | ADC_IN7 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_I2C_MAIN_A | C0603C104K5RACTU | 100nF | AX_VIO_REF3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_I2C_MAIN_B | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_FPGA_I2C_SCL | CRCW06032K20FKEA | 2.2k | FPGA_SCL | AX_VIO_REF3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_MUX_I2C_SCL | CRCW06032K20FKEA | 2.2k | I2C_SCL | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_FPGA_I2C_SDA | CRCW06032K20FKEA | 2.2k | FPGA_SDA | AX_VIO_REF3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_MUX_I2C_SDA | CRCW06032K20FKEA | 2.2k | I2C_SDA | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_TEMP_C_SCL | CRCW06032K20FKEA | 2.2k | TEMP_C_SCL | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_TEMP_C_SDA | CRCW06032K20FKEA | 2.2k | TEMP_C_SDA | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_UP_SCL | CRCW06032K20FKEA | 2.2k | UP_SCL | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_UP_SDA | CRCW06032K20FKEA | 2.2k | UP_SDA | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_DN_SCL | CRCW06032K20FKEA | 2.2k | DN_SCL | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_DN_SDA | CRCW06032K20FKEA | 2.2k | DN_SDA | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_MUX | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_TEMP | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | R_U_TEMP_ALERT | CRCW060310K0FKEA | 10k | U_TEMP_ALERT_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD00 | CRCW0603100KFKEA | 100k | DATA_00 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD00 | CRCW0603100KFKEA | 100k | DATA_00 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD01 | CRCW0603100KFKEA | 100k | DATA_01 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD01 | CRCW0603100KFKEA | 100k | DATA_01 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD02 | CRCW0603100KFKEA | 100k | DATA_02 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD02 | CRCW0603100KFKEA | 100k | DATA_02 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD03 | CRCW0603100KFKEA | 100k | DATA_03 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD03 | CRCW0603100KFKEA | 100k | DATA_03 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD04 | CRCW0603100KFKEA | 100k | DATA_04 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD04 | CRCW0603100KFKEA | 100k | DATA_04 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD05 | CRCW0603100KFKEA | 100k | DATA_05 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD05 | CRCW0603100KFKEA | 100k | DATA_05 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD06 | CRCW0603100KFKEA | 100k | DATA_06 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD06 | CRCW0603100KFKEA | 100k | DATA_06 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD07 | CRCW0603100KFKEA | 100k | DATA_07 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD07 | CRCW0603100KFKEA | 100k | DATA_07 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD08 | CRCW0603100KFKEA | 100k | DATA_08 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD08 | CRCW0603100KFKEA | 100k | DATA_08 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD09 | CRCW0603100KFKEA | 100k | DATA_09 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD09 | CRCW0603100KFKEA | 100k | DATA_09 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD10 | CRCW0603100KFKEA | 100k | DATA_10 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD10 | CRCW0603100KFKEA | 100k | DATA_10 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD11 | CRCW0603100KFKEA | 100k | DATA_11 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD11 | CRCW0603100KFKEA | 100k | DATA_11 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD12 | CRCW0603100KFKEA | 100k | DATA_12 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD12 | CRCW0603100KFKEA | 100k | DATA_12 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD13 | CRCW0603100KFKEA | 100k | DATA_13 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD13 | CRCW0603100KFKEA | 100k | DATA_13 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD14 | CRCW0603100KFKEA | 100k | DATA_14 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD14 | CRCW0603100KFKEA | 100k | DATA_14 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DATA_PD15 | CRCW0603100KFKEA | 100k | DATA_15 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DATA_PD15 | CRCW0603100KFKEA | 100k | DATA_15 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DEF_TX_PERMIT | CRCW060310K0FKEA | 10k | TX_PERMIT | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DEF_TX_PERMIT | CRCW060310K0FKEA | 10k | TX_PERMIT | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DEF_CENTRAL_POWER_OK | CRCW060310K0FKEA | 10k | CENTRAL_POWER_OK | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DEF_CENTRAL_POWER_OK | CRCW060310K0FKEA | 10k | CENTRAL_POWER_OK | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DEF_OE_N | CRCW060310K0FKEA | 10k | OE_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DEF_OE_N | CRCW060310K0FKEA | 10k | OE_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_DEF_RX_BLANK | CRCW060310K0FKEA | 10k | RX_BLANK | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_DEF_RX_BLANK | CRCW060310K0FKEA | 10k | RX_BLANK | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_U_OEINV | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_OEINV | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_ARM | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_ARM | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_PG | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_PG | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_FLT | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_FLT | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_GATE_OFF | CRCW0603100KFKEA | 100k | TX_GATE | VTX_PRE | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_GATE_OFF | CRCW0603100KFKEA | 100k | TX_GATE | VTX_PRE | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_CUT_BASE | CRCW06032K20FKEA | 2.2k | CUT_PERMIT | CUT_BASE | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_CUT_BASE | CRCW06032K20FKEA | 2.2k | CUT_PERMIT | CUT_BASE | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_CUT_PD | CRCW0603100KFKEA | 100k | CUT_BASE | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_CUT_PD | CRCW0603100KFKEA | 100k | CUT_BASE | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_BLEED | CRCW12062K20FKEA | 2.2k | VTX | GND | 1206 | 1% 0.25W | nonpolar/bidirectional |
| DN | R_TX_BLEED | CRCW12062K20FKEA | 2.2k | VTX | GND | 1206 | 1% 0.25W | nonpolar/bidirectional |
| UP | C_U_SR00 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR00 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR01 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR01 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR02 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR02 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR03 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR03 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR04 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR04 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR05 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR05 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR06 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR06 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR07 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR07 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR08 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR08 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR09 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR09 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR10 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR10 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR11 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR11 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR12 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR12 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR13 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR13 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR14 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR14 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_SR15 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_SR15 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV00 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV00 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_DRV_BULK00 | C0603C105K3RACTU | 1uF | VTX | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| DN | C_DRV_BULK00 | C0603C105K3RACTU | 1uF | VTX | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV01 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV01 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV02 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV02 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV03 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV03 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV04 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV04 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV05 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV05 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV06 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV06 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV07 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV07 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV08 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV08 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_DRV_BULK08 | C0603C105K3RACTU | 1uF | VTX | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| DN | C_DRV_BULK08 | C0603C105K3RACTU | 1uF | VTX | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV09 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV09 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV10 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV10 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV11 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV11 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV12 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV12 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV13 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV13 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV14 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV14 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV15 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV15 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV16 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV16 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_DRV_BULK16 | C0603C105K3RACTU | 1uF | VTX | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| DN | C_DRV_BULK16 | C0603C105K3RACTU | 1uF | VTX | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV17 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV17 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV18 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV18 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV19 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV19 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV20 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV20 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV21 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV21 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV22 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV22 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV23 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV23 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV24 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV24 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_DRV_BULK24 | C0603C105K3RACTU | 1uF | VTX | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| DN | C_DRV_BULK24 | C0603C105K3RACTU | 1uF | VTX | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV25 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV25 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV26 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV26 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV27 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV27 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV28 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV28 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV29 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV29 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV30 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV30 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_DRV31 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_DRV31 | C0603C104K5RACTU | 100nF | VTX | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_TX_PD00 | CRCW060310K0FKEA | 10k | TXLOG_00 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD00 | CRCW060310K0FKEA | 10k | TXLOG_00 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX00 | CRCW2512150RFKEG | 150 | TXOUT_00 | TX_AC_SRC00 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX00 | CRCW2512150RFKEG | 150 | TXOUT_00 | TX_AC_SRC00 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC00 | C1210C104J5GACTU | 100nF | TX_AC_SRC00 | TXPLUS_00 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC00 | C1210C104J5GACTU | 100nF | TX_AC_SRC00 | TXPLUS_00 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED00 | CRCW06031M00FKEA | 1M | TXPLUS_00 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED00 | CRCW06031M00FKEA | 1M | TXPLUS_00 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD01 | CRCW060310K0FKEA | 10k | TXLOG_01 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD01 | CRCW060310K0FKEA | 10k | TXLOG_01 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX01 | CRCW2512150RFKEG | 150 | TXOUT_01 | TX_AC_SRC01 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX01 | CRCW2512150RFKEG | 150 | TXOUT_01 | TX_AC_SRC01 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC01 | C1210C104J5GACTU | 100nF | TX_AC_SRC01 | TXPLUS_01 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC01 | C1210C104J5GACTU | 100nF | TX_AC_SRC01 | TXPLUS_01 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED01 | CRCW06031M00FKEA | 1M | TXPLUS_01 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED01 | CRCW06031M00FKEA | 1M | TXPLUS_01 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD02 | CRCW060310K0FKEA | 10k | TXLOG_02 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD02 | CRCW060310K0FKEA | 10k | TXLOG_02 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX02 | CRCW2512150RFKEG | 150 | TXOUT_02 | TX_AC_SRC02 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX02 | CRCW2512150RFKEG | 150 | TXOUT_02 | TX_AC_SRC02 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC02 | C1210C104J5GACTU | 100nF | TX_AC_SRC02 | TXPLUS_02 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC02 | C1210C104J5GACTU | 100nF | TX_AC_SRC02 | TXPLUS_02 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED02 | CRCW06031M00FKEA | 1M | TXPLUS_02 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED02 | CRCW06031M00FKEA | 1M | TXPLUS_02 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD03 | CRCW060310K0FKEA | 10k | TXLOG_03 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD03 | CRCW060310K0FKEA | 10k | TXLOG_03 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX03 | CRCW2512150RFKEG | 150 | TXOUT_03 | TX_AC_SRC03 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX03 | CRCW2512150RFKEG | 150 | TXOUT_03 | TX_AC_SRC03 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC03 | C1210C104J5GACTU | 100nF | TX_AC_SRC03 | TXPLUS_03 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC03 | C1210C104J5GACTU | 100nF | TX_AC_SRC03 | TXPLUS_03 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED03 | CRCW06031M00FKEA | 1M | TXPLUS_03 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED03 | CRCW06031M00FKEA | 1M | TXPLUS_03 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD04 | CRCW060310K0FKEA | 10k | TXLOG_04 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD04 | CRCW060310K0FKEA | 10k | TXLOG_04 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX04 | CRCW2512150RFKEG | 150 | TXOUT_04 | TX_AC_SRC04 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX04 | CRCW2512150RFKEG | 150 | TXOUT_04 | TX_AC_SRC04 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC04 | C1210C104J5GACTU | 100nF | TX_AC_SRC04 | TXPLUS_04 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC04 | C1210C104J5GACTU | 100nF | TX_AC_SRC04 | TXPLUS_04 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED04 | CRCW06031M00FKEA | 1M | TXPLUS_04 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED04 | CRCW06031M00FKEA | 1M | TXPLUS_04 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD05 | CRCW060310K0FKEA | 10k | TXLOG_05 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD05 | CRCW060310K0FKEA | 10k | TXLOG_05 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX05 | CRCW2512150RFKEG | 150 | TXOUT_05 | TX_AC_SRC05 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX05 | CRCW2512150RFKEG | 150 | TXOUT_05 | TX_AC_SRC05 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC05 | C1210C104J5GACTU | 100nF | TX_AC_SRC05 | TXPLUS_05 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC05 | C1210C104J5GACTU | 100nF | TX_AC_SRC05 | TXPLUS_05 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED05 | CRCW06031M00FKEA | 1M | TXPLUS_05 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED05 | CRCW06031M00FKEA | 1M | TXPLUS_05 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD06 | CRCW060310K0FKEA | 10k | TXLOG_06 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD06 | CRCW060310K0FKEA | 10k | TXLOG_06 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX06 | CRCW2512150RFKEG | 150 | TXOUT_06 | TX_AC_SRC06 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX06 | CRCW2512150RFKEG | 150 | TXOUT_06 | TX_AC_SRC06 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC06 | C1210C104J5GACTU | 100nF | TX_AC_SRC06 | TXPLUS_06 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC06 | C1210C104J5GACTU | 100nF | TX_AC_SRC06 | TXPLUS_06 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED06 | CRCW06031M00FKEA | 1M | TXPLUS_06 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED06 | CRCW06031M00FKEA | 1M | TXPLUS_06 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD07 | CRCW060310K0FKEA | 10k | TXLOG_07 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD07 | CRCW060310K0FKEA | 10k | TXLOG_07 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX07 | CRCW2512150RFKEG | 150 | TXOUT_07 | TX_AC_SRC07 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX07 | CRCW2512150RFKEG | 150 | TXOUT_07 | TX_AC_SRC07 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC07 | C1210C104J5GACTU | 100nF | TX_AC_SRC07 | TXPLUS_07 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC07 | C1210C104J5GACTU | 100nF | TX_AC_SRC07 | TXPLUS_07 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED07 | CRCW06031M00FKEA | 1M | TXPLUS_07 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED07 | CRCW06031M00FKEA | 1M | TXPLUS_07 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD08 | CRCW060310K0FKEA | 10k | TXLOG_08 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD08 | CRCW060310K0FKEA | 10k | TXLOG_08 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX08 | CRCW2512150RFKEG | 150 | TXOUT_08 | TX_AC_SRC08 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX08 | CRCW2512150RFKEG | 150 | TXOUT_08 | TX_AC_SRC08 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC08 | C1210C104J5GACTU | 100nF | TX_AC_SRC08 | TXPLUS_08 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC08 | C1210C104J5GACTU | 100nF | TX_AC_SRC08 | TXPLUS_08 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED08 | CRCW06031M00FKEA | 1M | TXPLUS_08 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED08 | CRCW06031M00FKEA | 1M | TXPLUS_08 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD09 | CRCW060310K0FKEA | 10k | TXLOG_09 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD09 | CRCW060310K0FKEA | 10k | TXLOG_09 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX09 | CRCW2512150RFKEG | 150 | TXOUT_09 | TX_AC_SRC09 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX09 | CRCW2512150RFKEG | 150 | TXOUT_09 | TX_AC_SRC09 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC09 | C1210C104J5GACTU | 100nF | TX_AC_SRC09 | TXPLUS_09 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC09 | C1210C104J5GACTU | 100nF | TX_AC_SRC09 | TXPLUS_09 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED09 | CRCW06031M00FKEA | 1M | TXPLUS_09 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED09 | CRCW06031M00FKEA | 1M | TXPLUS_09 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD10 | CRCW060310K0FKEA | 10k | TXLOG_10 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD10 | CRCW060310K0FKEA | 10k | TXLOG_10 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX10 | CRCW2512150RFKEG | 150 | TXOUT_10 | TX_AC_SRC10 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX10 | CRCW2512150RFKEG | 150 | TXOUT_10 | TX_AC_SRC10 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC10 | C1210C104J5GACTU | 100nF | TX_AC_SRC10 | TXPLUS_10 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC10 | C1210C104J5GACTU | 100nF | TX_AC_SRC10 | TXPLUS_10 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED10 | CRCW06031M00FKEA | 1M | TXPLUS_10 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED10 | CRCW06031M00FKEA | 1M | TXPLUS_10 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD11 | CRCW060310K0FKEA | 10k | TXLOG_11 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD11 | CRCW060310K0FKEA | 10k | TXLOG_11 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX11 | CRCW2512150RFKEG | 150 | TXOUT_11 | TX_AC_SRC11 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX11 | CRCW2512150RFKEG | 150 | TXOUT_11 | TX_AC_SRC11 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC11 | C1210C104J5GACTU | 100nF | TX_AC_SRC11 | TXPLUS_11 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC11 | C1210C104J5GACTU | 100nF | TX_AC_SRC11 | TXPLUS_11 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED11 | CRCW06031M00FKEA | 1M | TXPLUS_11 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED11 | CRCW06031M00FKEA | 1M | TXPLUS_11 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD12 | CRCW060310K0FKEA | 10k | TXLOG_12 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD12 | CRCW060310K0FKEA | 10k | TXLOG_12 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX12 | CRCW2512150RFKEG | 150 | TXOUT_12 | TX_AC_SRC12 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX12 | CRCW2512150RFKEG | 150 | TXOUT_12 | TX_AC_SRC12 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC12 | C1210C104J5GACTU | 100nF | TX_AC_SRC12 | TXPLUS_12 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC12 | C1210C104J5GACTU | 100nF | TX_AC_SRC12 | TXPLUS_12 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED12 | CRCW06031M00FKEA | 1M | TXPLUS_12 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED12 | CRCW06031M00FKEA | 1M | TXPLUS_12 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD13 | CRCW060310K0FKEA | 10k | TXLOG_13 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD13 | CRCW060310K0FKEA | 10k | TXLOG_13 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX13 | CRCW2512150RFKEG | 150 | TXOUT_13 | TX_AC_SRC13 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX13 | CRCW2512150RFKEG | 150 | TXOUT_13 | TX_AC_SRC13 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC13 | C1210C104J5GACTU | 100nF | TX_AC_SRC13 | TXPLUS_13 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC13 | C1210C104J5GACTU | 100nF | TX_AC_SRC13 | TXPLUS_13 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED13 | CRCW06031M00FKEA | 1M | TXPLUS_13 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED13 | CRCW06031M00FKEA | 1M | TXPLUS_13 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD14 | CRCW060310K0FKEA | 10k | TXLOG_14 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD14 | CRCW060310K0FKEA | 10k | TXLOG_14 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX14 | CRCW2512150RFKEG | 150 | TXOUT_14 | TX_AC_SRC14 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX14 | CRCW2512150RFKEG | 150 | TXOUT_14 | TX_AC_SRC14 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC14 | C1210C104J5GACTU | 100nF | TX_AC_SRC14 | TXPLUS_14 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC14 | C1210C104J5GACTU | 100nF | TX_AC_SRC14 | TXPLUS_14 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED14 | CRCW06031M00FKEA | 1M | TXPLUS_14 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED14 | CRCW06031M00FKEA | 1M | TXPLUS_14 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD15 | CRCW060310K0FKEA | 10k | TXLOG_15 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD15 | CRCW060310K0FKEA | 10k | TXLOG_15 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX15 | CRCW2512150RFKEG | 150 | TXOUT_15 | TX_AC_SRC15 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX15 | CRCW2512150RFKEG | 150 | TXOUT_15 | TX_AC_SRC15 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC15 | C1210C104J5GACTU | 100nF | TX_AC_SRC15 | TXPLUS_15 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC15 | C1210C104J5GACTU | 100nF | TX_AC_SRC15 | TXPLUS_15 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED15 | CRCW06031M00FKEA | 1M | TXPLUS_15 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED15 | CRCW06031M00FKEA | 1M | TXPLUS_15 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD16 | CRCW060310K0FKEA | 10k | TXLOG_16 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD16 | CRCW060310K0FKEA | 10k | TXLOG_16 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX16 | CRCW2512150RFKEG | 150 | TXOUT_16 | TX_AC_SRC16 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX16 | CRCW2512150RFKEG | 150 | TXOUT_16 | TX_AC_SRC16 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC16 | C1210C104J5GACTU | 100nF | TX_AC_SRC16 | TXPLUS_16 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC16 | C1210C104J5GACTU | 100nF | TX_AC_SRC16 | TXPLUS_16 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED16 | CRCW06031M00FKEA | 1M | TXPLUS_16 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED16 | CRCW06031M00FKEA | 1M | TXPLUS_16 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD17 | CRCW060310K0FKEA | 10k | TXLOG_17 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD17 | CRCW060310K0FKEA | 10k | TXLOG_17 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX17 | CRCW2512150RFKEG | 150 | TXOUT_17 | TX_AC_SRC17 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX17 | CRCW2512150RFKEG | 150 | TXOUT_17 | TX_AC_SRC17 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC17 | C1210C104J5GACTU | 100nF | TX_AC_SRC17 | TXPLUS_17 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC17 | C1210C104J5GACTU | 100nF | TX_AC_SRC17 | TXPLUS_17 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED17 | CRCW06031M00FKEA | 1M | TXPLUS_17 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED17 | CRCW06031M00FKEA | 1M | TXPLUS_17 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD18 | CRCW060310K0FKEA | 10k | TXLOG_18 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD18 | CRCW060310K0FKEA | 10k | TXLOG_18 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX18 | CRCW2512150RFKEG | 150 | TXOUT_18 | TX_AC_SRC18 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX18 | CRCW2512150RFKEG | 150 | TXOUT_18 | TX_AC_SRC18 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC18 | C1210C104J5GACTU | 100nF | TX_AC_SRC18 | TXPLUS_18 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC18 | C1210C104J5GACTU | 100nF | TX_AC_SRC18 | TXPLUS_18 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED18 | CRCW06031M00FKEA | 1M | TXPLUS_18 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED18 | CRCW06031M00FKEA | 1M | TXPLUS_18 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD19 | CRCW060310K0FKEA | 10k | TXLOG_19 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD19 | CRCW060310K0FKEA | 10k | TXLOG_19 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX19 | CRCW2512150RFKEG | 150 | TXOUT_19 | TX_AC_SRC19 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX19 | CRCW2512150RFKEG | 150 | TXOUT_19 | TX_AC_SRC19 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC19 | C1210C104J5GACTU | 100nF | TX_AC_SRC19 | TXPLUS_19 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC19 | C1210C104J5GACTU | 100nF | TX_AC_SRC19 | TXPLUS_19 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED19 | CRCW06031M00FKEA | 1M | TXPLUS_19 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED19 | CRCW06031M00FKEA | 1M | TXPLUS_19 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD20 | CRCW060310K0FKEA | 10k | TXLOG_20 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD20 | CRCW060310K0FKEA | 10k | TXLOG_20 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX20 | CRCW2512150RFKEG | 150 | TXOUT_20 | TX_AC_SRC20 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX20 | CRCW2512150RFKEG | 150 | TXOUT_20 | TX_AC_SRC20 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC20 | C1210C104J5GACTU | 100nF | TX_AC_SRC20 | TXPLUS_20 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC20 | C1210C104J5GACTU | 100nF | TX_AC_SRC20 | TXPLUS_20 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED20 | CRCW06031M00FKEA | 1M | TXPLUS_20 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED20 | CRCW06031M00FKEA | 1M | TXPLUS_20 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD21 | CRCW060310K0FKEA | 10k | TXLOG_21 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD21 | CRCW060310K0FKEA | 10k | TXLOG_21 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX21 | CRCW2512150RFKEG | 150 | TXOUT_21 | TX_AC_SRC21 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX21 | CRCW2512150RFKEG | 150 | TXOUT_21 | TX_AC_SRC21 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC21 | C1210C104J5GACTU | 100nF | TX_AC_SRC21 | TXPLUS_21 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC21 | C1210C104J5GACTU | 100nF | TX_AC_SRC21 | TXPLUS_21 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED21 | CRCW06031M00FKEA | 1M | TXPLUS_21 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED21 | CRCW06031M00FKEA | 1M | TXPLUS_21 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD22 | CRCW060310K0FKEA | 10k | TXLOG_22 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD22 | CRCW060310K0FKEA | 10k | TXLOG_22 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX22 | CRCW2512150RFKEG | 150 | TXOUT_22 | TX_AC_SRC22 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX22 | CRCW2512150RFKEG | 150 | TXOUT_22 | TX_AC_SRC22 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC22 | C1210C104J5GACTU | 100nF | TX_AC_SRC22 | TXPLUS_22 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC22 | C1210C104J5GACTU | 100nF | TX_AC_SRC22 | TXPLUS_22 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED22 | CRCW06031M00FKEA | 1M | TXPLUS_22 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED22 | CRCW06031M00FKEA | 1M | TXPLUS_22 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD23 | CRCW060310K0FKEA | 10k | TXLOG_23 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD23 | CRCW060310K0FKEA | 10k | TXLOG_23 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX23 | CRCW2512150RFKEG | 150 | TXOUT_23 | TX_AC_SRC23 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX23 | CRCW2512150RFKEG | 150 | TXOUT_23 | TX_AC_SRC23 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC23 | C1210C104J5GACTU | 100nF | TX_AC_SRC23 | TXPLUS_23 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC23 | C1210C104J5GACTU | 100nF | TX_AC_SRC23 | TXPLUS_23 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED23 | CRCW06031M00FKEA | 1M | TXPLUS_23 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED23 | CRCW06031M00FKEA | 1M | TXPLUS_23 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD24 | CRCW060310K0FKEA | 10k | TXLOG_24 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD24 | CRCW060310K0FKEA | 10k | TXLOG_24 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX24 | CRCW2512150RFKEG | 150 | TXOUT_24 | TX_AC_SRC24 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX24 | CRCW2512150RFKEG | 150 | TXOUT_24 | TX_AC_SRC24 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC24 | C1210C104J5GACTU | 100nF | TX_AC_SRC24 | TXPLUS_24 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC24 | C1210C104J5GACTU | 100nF | TX_AC_SRC24 | TXPLUS_24 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED24 | CRCW06031M00FKEA | 1M | TXPLUS_24 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED24 | CRCW06031M00FKEA | 1M | TXPLUS_24 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD25 | CRCW060310K0FKEA | 10k | TXLOG_25 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD25 | CRCW060310K0FKEA | 10k | TXLOG_25 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX25 | CRCW2512150RFKEG | 150 | TXOUT_25 | TX_AC_SRC25 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX25 | CRCW2512150RFKEG | 150 | TXOUT_25 | TX_AC_SRC25 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC25 | C1210C104J5GACTU | 100nF | TX_AC_SRC25 | TXPLUS_25 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC25 | C1210C104J5GACTU | 100nF | TX_AC_SRC25 | TXPLUS_25 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED25 | CRCW06031M00FKEA | 1M | TXPLUS_25 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED25 | CRCW06031M00FKEA | 1M | TXPLUS_25 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD26 | CRCW060310K0FKEA | 10k | TXLOG_26 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD26 | CRCW060310K0FKEA | 10k | TXLOG_26 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX26 | CRCW2512150RFKEG | 150 | TXOUT_26 | TX_AC_SRC26 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX26 | CRCW2512150RFKEG | 150 | TXOUT_26 | TX_AC_SRC26 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC26 | C1210C104J5GACTU | 100nF | TX_AC_SRC26 | TXPLUS_26 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC26 | C1210C104J5GACTU | 100nF | TX_AC_SRC26 | TXPLUS_26 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED26 | CRCW06031M00FKEA | 1M | TXPLUS_26 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED26 | CRCW06031M00FKEA | 1M | TXPLUS_26 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD27 | CRCW060310K0FKEA | 10k | TXLOG_27 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD27 | CRCW060310K0FKEA | 10k | TXLOG_27 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX27 | CRCW2512150RFKEG | 150 | TXOUT_27 | TX_AC_SRC27 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX27 | CRCW2512150RFKEG | 150 | TXOUT_27 | TX_AC_SRC27 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC27 | C1210C104J5GACTU | 100nF | TX_AC_SRC27 | TXPLUS_27 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC27 | C1210C104J5GACTU | 100nF | TX_AC_SRC27 | TXPLUS_27 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED27 | CRCW06031M00FKEA | 1M | TXPLUS_27 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED27 | CRCW06031M00FKEA | 1M | TXPLUS_27 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD28 | CRCW060310K0FKEA | 10k | TXLOG_28 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD28 | CRCW060310K0FKEA | 10k | TXLOG_28 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX28 | CRCW2512150RFKEG | 150 | TXOUT_28 | TX_AC_SRC28 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX28 | CRCW2512150RFKEG | 150 | TXOUT_28 | TX_AC_SRC28 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC28 | C1210C104J5GACTU | 100nF | TX_AC_SRC28 | TXPLUS_28 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC28 | C1210C104J5GACTU | 100nF | TX_AC_SRC28 | TXPLUS_28 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED28 | CRCW06031M00FKEA | 1M | TXPLUS_28 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED28 | CRCW06031M00FKEA | 1M | TXPLUS_28 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD29 | CRCW060310K0FKEA | 10k | TXLOG_29 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD29 | CRCW060310K0FKEA | 10k | TXLOG_29 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX29 | CRCW2512150RFKEG | 150 | TXOUT_29 | TX_AC_SRC29 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX29 | CRCW2512150RFKEG | 150 | TXOUT_29 | TX_AC_SRC29 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC29 | C1210C104J5GACTU | 100nF | TX_AC_SRC29 | TXPLUS_29 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC29 | C1210C104J5GACTU | 100nF | TX_AC_SRC29 | TXPLUS_29 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED29 | CRCW06031M00FKEA | 1M | TXPLUS_29 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED29 | CRCW06031M00FKEA | 1M | TXPLUS_29 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD30 | CRCW060310K0FKEA | 10k | TXLOG_30 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD30 | CRCW060310K0FKEA | 10k | TXLOG_30 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX30 | CRCW2512150RFKEG | 150 | TXOUT_30 | TX_AC_SRC30 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX30 | CRCW2512150RFKEG | 150 | TXOUT_30 | TX_AC_SRC30 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC30 | C1210C104J5GACTU | 100nF | TX_AC_SRC30 | TXPLUS_30 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC30 | C1210C104J5GACTU | 100nF | TX_AC_SRC30 | TXPLUS_30 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED30 | CRCW06031M00FKEA | 1M | TXPLUS_30 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED30 | CRCW06031M00FKEA | 1M | TXPLUS_30 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD31 | CRCW060310K0FKEA | 10k | TXLOG_31 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD31 | CRCW060310K0FKEA | 10k | TXLOG_31 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX31 | CRCW2512150RFKEG | 150 | TXOUT_31 | TX_AC_SRC31 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX31 | CRCW2512150RFKEG | 150 | TXOUT_31 | TX_AC_SRC31 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC31 | C1210C104J5GACTU | 100nF | TX_AC_SRC31 | TXPLUS_31 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC31 | C1210C104J5GACTU | 100nF | TX_AC_SRC31 | TXPLUS_31 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED31 | CRCW06031M00FKEA | 1M | TXPLUS_31 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED31 | CRCW06031M00FKEA | 1M | TXPLUS_31 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD32 | CRCW060310K0FKEA | 10k | TXLOG_32 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD32 | CRCW060310K0FKEA | 10k | TXLOG_32 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX32 | CRCW2512150RFKEG | 150 | TXOUT_32 | TX_AC_SRC32 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX32 | CRCW2512150RFKEG | 150 | TXOUT_32 | TX_AC_SRC32 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC32 | C1210C104J5GACTU | 100nF | TX_AC_SRC32 | TXPLUS_32 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC32 | C1210C104J5GACTU | 100nF | TX_AC_SRC32 | TXPLUS_32 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED32 | CRCW06031M00FKEA | 1M | TXPLUS_32 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED32 | CRCW06031M00FKEA | 1M | TXPLUS_32 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD33 | CRCW060310K0FKEA | 10k | TXLOG_33 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD33 | CRCW060310K0FKEA | 10k | TXLOG_33 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX33 | CRCW2512150RFKEG | 150 | TXOUT_33 | TX_AC_SRC33 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX33 | CRCW2512150RFKEG | 150 | TXOUT_33 | TX_AC_SRC33 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC33 | C1210C104J5GACTU | 100nF | TX_AC_SRC33 | TXPLUS_33 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC33 | C1210C104J5GACTU | 100nF | TX_AC_SRC33 | TXPLUS_33 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED33 | CRCW06031M00FKEA | 1M | TXPLUS_33 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED33 | CRCW06031M00FKEA | 1M | TXPLUS_33 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD34 | CRCW060310K0FKEA | 10k | TXLOG_34 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD34 | CRCW060310K0FKEA | 10k | TXLOG_34 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX34 | CRCW2512150RFKEG | 150 | TXOUT_34 | TX_AC_SRC34 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX34 | CRCW2512150RFKEG | 150 | TXOUT_34 | TX_AC_SRC34 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC34 | C1210C104J5GACTU | 100nF | TX_AC_SRC34 | TXPLUS_34 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC34 | C1210C104J5GACTU | 100nF | TX_AC_SRC34 | TXPLUS_34 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED34 | CRCW06031M00FKEA | 1M | TXPLUS_34 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED34 | CRCW06031M00FKEA | 1M | TXPLUS_34 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD35 | CRCW060310K0FKEA | 10k | TXLOG_35 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD35 | CRCW060310K0FKEA | 10k | TXLOG_35 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX35 | CRCW2512150RFKEG | 150 | TXOUT_35 | TX_AC_SRC35 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX35 | CRCW2512150RFKEG | 150 | TXOUT_35 | TX_AC_SRC35 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC35 | C1210C104J5GACTU | 100nF | TX_AC_SRC35 | TXPLUS_35 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC35 | C1210C104J5GACTU | 100nF | TX_AC_SRC35 | TXPLUS_35 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED35 | CRCW06031M00FKEA | 1M | TXPLUS_35 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED35 | CRCW06031M00FKEA | 1M | TXPLUS_35 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD36 | CRCW060310K0FKEA | 10k | TXLOG_36 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD36 | CRCW060310K0FKEA | 10k | TXLOG_36 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX36 | CRCW2512150RFKEG | 150 | TXOUT_36 | TX_AC_SRC36 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX36 | CRCW2512150RFKEG | 150 | TXOUT_36 | TX_AC_SRC36 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC36 | C1210C104J5GACTU | 100nF | TX_AC_SRC36 | TXPLUS_36 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC36 | C1210C104J5GACTU | 100nF | TX_AC_SRC36 | TXPLUS_36 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED36 | CRCW06031M00FKEA | 1M | TXPLUS_36 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED36 | CRCW06031M00FKEA | 1M | TXPLUS_36 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD37 | CRCW060310K0FKEA | 10k | TXLOG_37 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD37 | CRCW060310K0FKEA | 10k | TXLOG_37 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX37 | CRCW2512150RFKEG | 150 | TXOUT_37 | TX_AC_SRC37 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX37 | CRCW2512150RFKEG | 150 | TXOUT_37 | TX_AC_SRC37 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC37 | C1210C104J5GACTU | 100nF | TX_AC_SRC37 | TXPLUS_37 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC37 | C1210C104J5GACTU | 100nF | TX_AC_SRC37 | TXPLUS_37 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED37 | CRCW06031M00FKEA | 1M | TXPLUS_37 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED37 | CRCW06031M00FKEA | 1M | TXPLUS_37 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD38 | CRCW060310K0FKEA | 10k | TXLOG_38 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD38 | CRCW060310K0FKEA | 10k | TXLOG_38 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX38 | CRCW2512150RFKEG | 150 | TXOUT_38 | TX_AC_SRC38 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX38 | CRCW2512150RFKEG | 150 | TXOUT_38 | TX_AC_SRC38 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC38 | C1210C104J5GACTU | 100nF | TX_AC_SRC38 | TXPLUS_38 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC38 | C1210C104J5GACTU | 100nF | TX_AC_SRC38 | TXPLUS_38 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED38 | CRCW06031M00FKEA | 1M | TXPLUS_38 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED38 | CRCW06031M00FKEA | 1M | TXPLUS_38 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD39 | CRCW060310K0FKEA | 10k | TXLOG_39 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD39 | CRCW060310K0FKEA | 10k | TXLOG_39 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX39 | CRCW2512150RFKEG | 150 | TXOUT_39 | TX_AC_SRC39 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX39 | CRCW2512150RFKEG | 150 | TXOUT_39 | TX_AC_SRC39 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC39 | C1210C104J5GACTU | 100nF | TX_AC_SRC39 | TXPLUS_39 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC39 | C1210C104J5GACTU | 100nF | TX_AC_SRC39 | TXPLUS_39 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED39 | CRCW06031M00FKEA | 1M | TXPLUS_39 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED39 | CRCW06031M00FKEA | 1M | TXPLUS_39 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD40 | CRCW060310K0FKEA | 10k | TXLOG_40 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD40 | CRCW060310K0FKEA | 10k | TXLOG_40 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX40 | CRCW2512150RFKEG | 150 | TXOUT_40 | TX_AC_SRC40 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX40 | CRCW2512150RFKEG | 150 | TXOUT_40 | TX_AC_SRC40 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC40 | C1210C104J5GACTU | 100nF | TX_AC_SRC40 | TXPLUS_40 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC40 | C1210C104J5GACTU | 100nF | TX_AC_SRC40 | TXPLUS_40 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED40 | CRCW06031M00FKEA | 1M | TXPLUS_40 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED40 | CRCW06031M00FKEA | 1M | TXPLUS_40 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD41 | CRCW060310K0FKEA | 10k | TXLOG_41 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD41 | CRCW060310K0FKEA | 10k | TXLOG_41 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX41 | CRCW2512150RFKEG | 150 | TXOUT_41 | TX_AC_SRC41 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX41 | CRCW2512150RFKEG | 150 | TXOUT_41 | TX_AC_SRC41 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC41 | C1210C104J5GACTU | 100nF | TX_AC_SRC41 | TXPLUS_41 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC41 | C1210C104J5GACTU | 100nF | TX_AC_SRC41 | TXPLUS_41 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED41 | CRCW06031M00FKEA | 1M | TXPLUS_41 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED41 | CRCW06031M00FKEA | 1M | TXPLUS_41 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD42 | CRCW060310K0FKEA | 10k | TXLOG_42 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD42 | CRCW060310K0FKEA | 10k | TXLOG_42 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX42 | CRCW2512150RFKEG | 150 | TXOUT_42 | TX_AC_SRC42 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX42 | CRCW2512150RFKEG | 150 | TXOUT_42 | TX_AC_SRC42 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC42 | C1210C104J5GACTU | 100nF | TX_AC_SRC42 | TXPLUS_42 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC42 | C1210C104J5GACTU | 100nF | TX_AC_SRC42 | TXPLUS_42 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED42 | CRCW06031M00FKEA | 1M | TXPLUS_42 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED42 | CRCW06031M00FKEA | 1M | TXPLUS_42 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD43 | CRCW060310K0FKEA | 10k | TXLOG_43 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD43 | CRCW060310K0FKEA | 10k | TXLOG_43 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX43 | CRCW2512150RFKEG | 150 | TXOUT_43 | TX_AC_SRC43 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX43 | CRCW2512150RFKEG | 150 | TXOUT_43 | TX_AC_SRC43 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC43 | C1210C104J5GACTU | 100nF | TX_AC_SRC43 | TXPLUS_43 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC43 | C1210C104J5GACTU | 100nF | TX_AC_SRC43 | TXPLUS_43 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED43 | CRCW06031M00FKEA | 1M | TXPLUS_43 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED43 | CRCW06031M00FKEA | 1M | TXPLUS_43 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD44 | CRCW060310K0FKEA | 10k | TXLOG_44 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD44 | CRCW060310K0FKEA | 10k | TXLOG_44 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX44 | CRCW2512150RFKEG | 150 | TXOUT_44 | TX_AC_SRC44 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX44 | CRCW2512150RFKEG | 150 | TXOUT_44 | TX_AC_SRC44 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC44 | C1210C104J5GACTU | 100nF | TX_AC_SRC44 | TXPLUS_44 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC44 | C1210C104J5GACTU | 100nF | TX_AC_SRC44 | TXPLUS_44 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED44 | CRCW06031M00FKEA | 1M | TXPLUS_44 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED44 | CRCW06031M00FKEA | 1M | TXPLUS_44 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD45 | CRCW060310K0FKEA | 10k | TXLOG_45 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD45 | CRCW060310K0FKEA | 10k | TXLOG_45 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX45 | CRCW2512150RFKEG | 150 | TXOUT_45 | TX_AC_SRC45 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX45 | CRCW2512150RFKEG | 150 | TXOUT_45 | TX_AC_SRC45 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC45 | C1210C104J5GACTU | 100nF | TX_AC_SRC45 | TXPLUS_45 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC45 | C1210C104J5GACTU | 100nF | TX_AC_SRC45 | TXPLUS_45 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED45 | CRCW06031M00FKEA | 1M | TXPLUS_45 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED45 | CRCW06031M00FKEA | 1M | TXPLUS_45 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD46 | CRCW060310K0FKEA | 10k | TXLOG_46 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD46 | CRCW060310K0FKEA | 10k | TXLOG_46 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX46 | CRCW2512150RFKEG | 150 | TXOUT_46 | TX_AC_SRC46 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX46 | CRCW2512150RFKEG | 150 | TXOUT_46 | TX_AC_SRC46 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC46 | C1210C104J5GACTU | 100nF | TX_AC_SRC46 | TXPLUS_46 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC46 | C1210C104J5GACTU | 100nF | TX_AC_SRC46 | TXPLUS_46 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED46 | CRCW06031M00FKEA | 1M | TXPLUS_46 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED46 | CRCW06031M00FKEA | 1M | TXPLUS_46 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD47 | CRCW060310K0FKEA | 10k | TXLOG_47 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD47 | CRCW060310K0FKEA | 10k | TXLOG_47 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX47 | CRCW2512150RFKEG | 150 | TXOUT_47 | TX_AC_SRC47 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX47 | CRCW2512150RFKEG | 150 | TXOUT_47 | TX_AC_SRC47 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC47 | C1210C104J5GACTU | 100nF | TX_AC_SRC47 | TXPLUS_47 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC47 | C1210C104J5GACTU | 100nF | TX_AC_SRC47 | TXPLUS_47 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED47 | CRCW06031M00FKEA | 1M | TXPLUS_47 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED47 | CRCW06031M00FKEA | 1M | TXPLUS_47 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD48 | CRCW060310K0FKEA | 10k | TXLOG_48 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD48 | CRCW060310K0FKEA | 10k | TXLOG_48 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX48 | CRCW2512150RFKEG | 150 | TXOUT_48 | TX_AC_SRC48 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX48 | CRCW2512150RFKEG | 150 | TXOUT_48 | TX_AC_SRC48 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC48 | C1210C104J5GACTU | 100nF | TX_AC_SRC48 | TXPLUS_48 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC48 | C1210C104J5GACTU | 100nF | TX_AC_SRC48 | TXPLUS_48 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED48 | CRCW06031M00FKEA | 1M | TXPLUS_48 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED48 | CRCW06031M00FKEA | 1M | TXPLUS_48 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD49 | CRCW060310K0FKEA | 10k | TXLOG_49 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD49 | CRCW060310K0FKEA | 10k | TXLOG_49 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX49 | CRCW2512150RFKEG | 150 | TXOUT_49 | TX_AC_SRC49 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX49 | CRCW2512150RFKEG | 150 | TXOUT_49 | TX_AC_SRC49 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC49 | C1210C104J5GACTU | 100nF | TX_AC_SRC49 | TXPLUS_49 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC49 | C1210C104J5GACTU | 100nF | TX_AC_SRC49 | TXPLUS_49 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED49 | CRCW06031M00FKEA | 1M | TXPLUS_49 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED49 | CRCW06031M00FKEA | 1M | TXPLUS_49 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD50 | CRCW060310K0FKEA | 10k | TXLOG_50 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD50 | CRCW060310K0FKEA | 10k | TXLOG_50 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX50 | CRCW2512150RFKEG | 150 | TXOUT_50 | TX_AC_SRC50 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX50 | CRCW2512150RFKEG | 150 | TXOUT_50 | TX_AC_SRC50 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC50 | C1210C104J5GACTU | 100nF | TX_AC_SRC50 | TXPLUS_50 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC50 | C1210C104J5GACTU | 100nF | TX_AC_SRC50 | TXPLUS_50 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED50 | CRCW06031M00FKEA | 1M | TXPLUS_50 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED50 | CRCW06031M00FKEA | 1M | TXPLUS_50 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD51 | CRCW060310K0FKEA | 10k | TXLOG_51 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD51 | CRCW060310K0FKEA | 10k | TXLOG_51 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX51 | CRCW2512150RFKEG | 150 | TXOUT_51 | TX_AC_SRC51 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX51 | CRCW2512150RFKEG | 150 | TXOUT_51 | TX_AC_SRC51 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC51 | C1210C104J5GACTU | 100nF | TX_AC_SRC51 | TXPLUS_51 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC51 | C1210C104J5GACTU | 100nF | TX_AC_SRC51 | TXPLUS_51 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED51 | CRCW06031M00FKEA | 1M | TXPLUS_51 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED51 | CRCW06031M00FKEA | 1M | TXPLUS_51 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD52 | CRCW060310K0FKEA | 10k | TXLOG_52 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD52 | CRCW060310K0FKEA | 10k | TXLOG_52 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX52 | CRCW2512150RFKEG | 150 | TXOUT_52 | TX_AC_SRC52 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX52 | CRCW2512150RFKEG | 150 | TXOUT_52 | TX_AC_SRC52 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC52 | C1210C104J5GACTU | 100nF | TX_AC_SRC52 | TXPLUS_52 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC52 | C1210C104J5GACTU | 100nF | TX_AC_SRC52 | TXPLUS_52 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED52 | CRCW06031M00FKEA | 1M | TXPLUS_52 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED52 | CRCW06031M00FKEA | 1M | TXPLUS_52 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD53 | CRCW060310K0FKEA | 10k | TXLOG_53 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD53 | CRCW060310K0FKEA | 10k | TXLOG_53 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX53 | CRCW2512150RFKEG | 150 | TXOUT_53 | TX_AC_SRC53 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX53 | CRCW2512150RFKEG | 150 | TXOUT_53 | TX_AC_SRC53 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC53 | C1210C104J5GACTU | 100nF | TX_AC_SRC53 | TXPLUS_53 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC53 | C1210C104J5GACTU | 100nF | TX_AC_SRC53 | TXPLUS_53 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED53 | CRCW06031M00FKEA | 1M | TXPLUS_53 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED53 | CRCW06031M00FKEA | 1M | TXPLUS_53 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD54 | CRCW060310K0FKEA | 10k | TXLOG_54 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD54 | CRCW060310K0FKEA | 10k | TXLOG_54 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX54 | CRCW2512150RFKEG | 150 | TXOUT_54 | TX_AC_SRC54 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX54 | CRCW2512150RFKEG | 150 | TXOUT_54 | TX_AC_SRC54 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC54 | C1210C104J5GACTU | 100nF | TX_AC_SRC54 | TXPLUS_54 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC54 | C1210C104J5GACTU | 100nF | TX_AC_SRC54 | TXPLUS_54 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED54 | CRCW06031M00FKEA | 1M | TXPLUS_54 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED54 | CRCW06031M00FKEA | 1M | TXPLUS_54 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD55 | CRCW060310K0FKEA | 10k | TXLOG_55 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD55 | CRCW060310K0FKEA | 10k | TXLOG_55 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX55 | CRCW2512150RFKEG | 150 | TXOUT_55 | TX_AC_SRC55 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX55 | CRCW2512150RFKEG | 150 | TXOUT_55 | TX_AC_SRC55 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC55 | C1210C104J5GACTU | 100nF | TX_AC_SRC55 | TXPLUS_55 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC55 | C1210C104J5GACTU | 100nF | TX_AC_SRC55 | TXPLUS_55 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED55 | CRCW06031M00FKEA | 1M | TXPLUS_55 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED55 | CRCW06031M00FKEA | 1M | TXPLUS_55 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD56 | CRCW060310K0FKEA | 10k | TXLOG_56 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD56 | CRCW060310K0FKEA | 10k | TXLOG_56 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX56 | CRCW2512150RFKEG | 150 | TXOUT_56 | TX_AC_SRC56 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX56 | CRCW2512150RFKEG | 150 | TXOUT_56 | TX_AC_SRC56 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC56 | C1210C104J5GACTU | 100nF | TX_AC_SRC56 | TXPLUS_56 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC56 | C1210C104J5GACTU | 100nF | TX_AC_SRC56 | TXPLUS_56 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED56 | CRCW06031M00FKEA | 1M | TXPLUS_56 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED56 | CRCW06031M00FKEA | 1M | TXPLUS_56 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD57 | CRCW060310K0FKEA | 10k | TXLOG_57 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD57 | CRCW060310K0FKEA | 10k | TXLOG_57 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX57 | CRCW2512150RFKEG | 150 | TXOUT_57 | TX_AC_SRC57 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX57 | CRCW2512150RFKEG | 150 | TXOUT_57 | TX_AC_SRC57 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC57 | C1210C104J5GACTU | 100nF | TX_AC_SRC57 | TXPLUS_57 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC57 | C1210C104J5GACTU | 100nF | TX_AC_SRC57 | TXPLUS_57 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED57 | CRCW06031M00FKEA | 1M | TXPLUS_57 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED57 | CRCW06031M00FKEA | 1M | TXPLUS_57 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD58 | CRCW060310K0FKEA | 10k | TXLOG_58 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD58 | CRCW060310K0FKEA | 10k | TXLOG_58 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX58 | CRCW2512150RFKEG | 150 | TXOUT_58 | TX_AC_SRC58 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX58 | CRCW2512150RFKEG | 150 | TXOUT_58 | TX_AC_SRC58 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC58 | C1210C104J5GACTU | 100nF | TX_AC_SRC58 | TXPLUS_58 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC58 | C1210C104J5GACTU | 100nF | TX_AC_SRC58 | TXPLUS_58 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED58 | CRCW06031M00FKEA | 1M | TXPLUS_58 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED58 | CRCW06031M00FKEA | 1M | TXPLUS_58 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD59 | CRCW060310K0FKEA | 10k | TXLOG_59 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD59 | CRCW060310K0FKEA | 10k | TXLOG_59 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX59 | CRCW2512150RFKEG | 150 | TXOUT_59 | TX_AC_SRC59 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX59 | CRCW2512150RFKEG | 150 | TXOUT_59 | TX_AC_SRC59 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC59 | C1210C104J5GACTU | 100nF | TX_AC_SRC59 | TXPLUS_59 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC59 | C1210C104J5GACTU | 100nF | TX_AC_SRC59 | TXPLUS_59 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED59 | CRCW06031M00FKEA | 1M | TXPLUS_59 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED59 | CRCW06031M00FKEA | 1M | TXPLUS_59 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD60 | CRCW060310K0FKEA | 10k | TXLOG_60 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD60 | CRCW060310K0FKEA | 10k | TXLOG_60 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX60 | CRCW2512150RFKEG | 150 | TXOUT_60 | TX_AC_SRC60 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX60 | CRCW2512150RFKEG | 150 | TXOUT_60 | TX_AC_SRC60 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC60 | C1210C104J5GACTU | 100nF | TX_AC_SRC60 | TXPLUS_60 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC60 | C1210C104J5GACTU | 100nF | TX_AC_SRC60 | TXPLUS_60 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED60 | CRCW06031M00FKEA | 1M | TXPLUS_60 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED60 | CRCW06031M00FKEA | 1M | TXPLUS_60 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD61 | CRCW060310K0FKEA | 10k | TXLOG_61 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD61 | CRCW060310K0FKEA | 10k | TXLOG_61 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX61 | CRCW2512150RFKEG | 150 | TXOUT_61 | TX_AC_SRC61 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX61 | CRCW2512150RFKEG | 150 | TXOUT_61 | TX_AC_SRC61 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC61 | C1210C104J5GACTU | 100nF | TX_AC_SRC61 | TXPLUS_61 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC61 | C1210C104J5GACTU | 100nF | TX_AC_SRC61 | TXPLUS_61 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED61 | CRCW06031M00FKEA | 1M | TXPLUS_61 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED61 | CRCW06031M00FKEA | 1M | TXPLUS_61 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD62 | CRCW060310K0FKEA | 10k | TXLOG_62 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD62 | CRCW060310K0FKEA | 10k | TXLOG_62 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX62 | CRCW2512150RFKEG | 150 | TXOUT_62 | TX_AC_SRC62 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX62 | CRCW2512150RFKEG | 150 | TXOUT_62 | TX_AC_SRC62 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC62 | C1210C104J5GACTU | 100nF | TX_AC_SRC62 | TXPLUS_62 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC62 | C1210C104J5GACTU | 100nF | TX_AC_SRC62 | TXPLUS_62 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED62 | CRCW06031M00FKEA | 1M | TXPLUS_62 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED62 | CRCW06031M00FKEA | 1M | TXPLUS_62 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX_PD63 | CRCW060310K0FKEA | 10k | TXLOG_63 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_PD63 | CRCW060310K0FKEA | 10k | TXLOG_63 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TX63 | CRCW2512150RFKEG | 150 | TXOUT_63 | TX_AC_SRC63 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| DN | R_TX63 | CRCW2512150RFKEG | 150 | TXOUT_63 | TX_AC_SRC63 | 2512 | 1% 1W at70C; derate per CRCW datasheet; pulse qualification HOLD | nonpolar/bidirectional |
| UP | C_TX_AC63 | C1210C104J5GACTU | 100nF | TX_AC_SRC63 | TXPLUS_63 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_TX_AC63 | C1210C104J5GACTU | 100nF | TX_AC_SRC63 | TXPLUS_63 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_TX_BLEED63 | CRCW06031M00FKEA | 1M | TXPLUS_63 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TX_BLEED63 | CRCW06031M00FKEA | 1M | TXPLUS_63 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_BIAS_IN | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_BIAS_IN | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_BIAS_OUT | C0603C105K3RACTU | 1uF | VBIAS25 | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| DN | C_BIAS_OUT | C0603C105K3RACTU | 1uF | VBIAS25 | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| UP | R_RX_IN0 | CRCW060310K0FKEA | 10k | RX_RAW0 | RX_LIMIT0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_IN0 | CRCW060310K0FKEA | 10k | RX_RAW0 | RX_LIMIT0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_RX_AC0 | C1210C104J5GACTU | 100nF | RX_LIMIT0 | RX_BIAS0 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_RX_AC0 | C1210C104J5GACTU | 100nF | RX_LIMIT0 | RX_BIAS0 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_RX_BIAS0 | CRCW0603100KFKEA | 100k | RX_BIAS0 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_BIAS0 | CRCW0603100KFKEA | 100k | RX_BIAS0 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_GAIN0 | CRCW060310K0FKEA | 10k | RX_FB0 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_GAIN0 | CRCW060310K0FKEA | 10k | RX_FB0 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_FB0 | CRCW0603100KFKEA | 100k | RX0 | RX_FB0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_FB0 | CRCW0603100KFKEA | 100k | RX0 | RX_FB0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_BLEED0 | CRCW0603100KFKEA | 100k | RX0 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_BLEED0 | CRCW0603100KFKEA | 100k | RX0 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_IN1 | CRCW060310K0FKEA | 10k | RX_RAW1 | RX_LIMIT1 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_IN1 | CRCW060310K0FKEA | 10k | RX_RAW1 | RX_LIMIT1 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_RX_AC1 | C1210C104J5GACTU | 100nF | RX_LIMIT1 | RX_BIAS1 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_RX_AC1 | C1210C104J5GACTU | 100nF | RX_LIMIT1 | RX_BIAS1 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_RX_BIAS1 | CRCW0603100KFKEA | 100k | RX_BIAS1 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_BIAS1 | CRCW0603100KFKEA | 100k | RX_BIAS1 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_GAIN1 | CRCW060310K0FKEA | 10k | RX_FB1 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_GAIN1 | CRCW060310K0FKEA | 10k | RX_FB1 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_FB1 | CRCW0603100KFKEA | 100k | RX1 | RX_FB1 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_FB1 | CRCW0603100KFKEA | 100k | RX1 | RX_FB1 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_BLEED1 | CRCW0603100KFKEA | 100k | RX1 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_BLEED1 | CRCW0603100KFKEA | 100k | RX1 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_IN2 | CRCW060310K0FKEA | 10k | RX_RAW2 | RX_LIMIT2 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_IN2 | CRCW060310K0FKEA | 10k | RX_RAW2 | RX_LIMIT2 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_RX_AC2 | C1210C104J5GACTU | 100nF | RX_LIMIT2 | RX_BIAS2 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_RX_AC2 | C1210C104J5GACTU | 100nF | RX_LIMIT2 | RX_BIAS2 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_RX_BIAS2 | CRCW0603100KFKEA | 100k | RX_BIAS2 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_BIAS2 | CRCW0603100KFKEA | 100k | RX_BIAS2 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_GAIN2 | CRCW060310K0FKEA | 10k | RX_FB2 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_GAIN2 | CRCW060310K0FKEA | 10k | RX_FB2 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_FB2 | CRCW0603100KFKEA | 100k | RX2 | RX_FB2 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_FB2 | CRCW0603100KFKEA | 100k | RX2 | RX_FB2 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_BLEED2 | CRCW0603100KFKEA | 100k | RX2 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_BLEED2 | CRCW0603100KFKEA | 100k | RX2 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_IN3 | CRCW060310K0FKEA | 10k | RX_RAW3 | RX_LIMIT3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_IN3 | CRCW060310K0FKEA | 10k | RX_RAW3 | RX_LIMIT3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_RX_AC3 | C1210C104J5GACTU | 100nF | RX_LIMIT3 | RX_BIAS3 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_RX_AC3 | C1210C104J5GACTU | 100nF | RX_LIMIT3 | RX_BIAS3 | 1210 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | R_RX_BIAS3 | CRCW0603100KFKEA | 100k | RX_BIAS3 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_BIAS3 | CRCW0603100KFKEA | 100k | RX_BIAS3 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_GAIN3 | CRCW060310K0FKEA | 10k | RX_FB3 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_GAIN3 | CRCW060310K0FKEA | 10k | RX_FB3 | VBIAS25 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_FB3 | CRCW0603100KFKEA | 100k | RX3 | RX_FB3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_FB3 | CRCW0603100KFKEA | 100k | RX3 | RX_FB3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_RX_BLEED3 | CRCW0603100KFKEA | 100k | RX3 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_RX_BLEED3 | CRCW0603100KFKEA | 100k | RX3 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_U_RX | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_RX | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_RX_BULK | C0603C105K3RACTU | 1uF | V5A | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| DN | C_RX_BULK | C0603C105K3RACTU | 1uF | V5A | GND | 0603 | 25V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_I2C_A | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_I2C_A | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_I2C_B | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_I2C_B | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_TEMP_SCL | CRCW06032K20FKEA | 2.2k | TEMP_SCL | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TEMP_SCL | CRCW06032K20FKEA | 2.2k | TEMP_SCL | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_TEMP_SDA | CRCW06032K20FKEA | 2.2k | TEMP_SDA | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_TEMP_SDA | CRCW06032K20FKEA | 2.2k | TEMP_SDA | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_U_TEMP | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_TEMP | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_U_TEMP_ALERT | CRCW060310K0FKEA | 10k | U_TEMP_ALERT_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_U_TEMP_ALERT | CRCW060310K0FKEA | 10k | U_TEMP_ALERT_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_5M_TOP_TRIM | TNPW0603402RBEEA | 402 | V5_DIV_MID | V5_SENSE | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_U_TXMON_TOP | TNPW060371K5BEEA | 71.5k | VTX_PRE | U_TXMON_SENSE | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_U_TXMON_TOP | TNPW060371K5BEEA | 71.5k | VTX_PRE | U_TXMON_SENSE | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_U_TXMON_BOT | TNPW060310K0BEEA | 10k | U_TXMON_SENSE | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_U_TXMON_BOT | TNPW060310K0BEEA | 10k | U_TXMON_SENSE | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_U_TXMON_PU | CRCW060310K0FKEA | 10k | TX_PRE_GOOD | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_U_TXMON_PU | CRCW060310K0FKEA | 10k | TX_PRE_GOOD | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_U_TXMON_CT | C0805C103J5GACTU | 10nF | U_TXMON_CT | GND | 0805 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_U_TXMON_CT | C0805C103J5GACTU | 10nF | U_TXMON_CT | GND | 0805 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | C_U_TXMON | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_TXMON | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_5M_TOP_TRIM | TNPW0603402RBEEA | 402 | V5_DIV_MID | V5_SENSE | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_5M_TOP_TRIM | TNPW0603402RBEEA | 402 | V5_DIV_MID | V5_SENSE | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_U_POR_TOP | TNPW060316K9BEEA | 16.9k | V3V3 | U_POR_SENSE | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_U_POR_BOT | TNPW060310K0BEEA | 10k | U_POR_SENSE | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_U_POR_PU | CRCW060310K0FKEA | 10k | POR_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_POR_CT | C0805C103J5GACTU | 10nF | U_POR_CT | GND | 0805 | 50V C0G ±5% | nonpolar/bidirectional |
| CENTRAL | C_U_POR | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_G1 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_U_POR_TOP | TNPW060316K9BEEA | 16.9k | V3V3 | U_POR_SENSE | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_U_POR_TOP | TNPW060316K9BEEA | 16.9k | V3V3 | U_POR_SENSE | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_U_POR_BOT | TNPW060310K0BEEA | 10k | U_POR_SENSE | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| DN | R_U_POR_BOT | TNPW060310K0BEEA | 10k | U_POR_SENSE | GND | 0603 | 0.1% 0.1W | nonpolar/bidirectional |
| UP | R_U_POR_PU | CRCW060310K0FKEA | 10k | POR_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_U_POR_PU | CRCW060310K0FKEA | 10k | POR_N | V3V3 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | C_U_POR_CT | C0805C103J5GACTU | 10nF | U_POR_CT | GND | 0805 | 50V C0G ±5% | nonpolar/bidirectional |
| DN | C_U_POR_CT | C0805C103J5GACTU | 10nF | U_POR_CT | GND | 0805 | 50V C0G ±5% | nonpolar/bidirectional |
| UP | C_U_POR | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_POR | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_G1 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_G1 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_G2 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_G2 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | C_U_G3 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| DN | C_U_G3 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_ENRELEASE0 | CRCW06031K00FKEA | 1k | EN_PERMIT | ENRELEASE_BASE_G0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_ENRELEASE0 | CRCW06031K00FKEA | 1k | EN_PERMIT | ENRELEASE_BASE_G0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_ENRELEASE_PD0 | CRCW0603100KFKEA | 100k | ENRELEASE_BASE_G0 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_ENRELEASE_PD0 | CRCW0603100KFKEA | 100k | ENRELEASE_BASE_G0 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_EN_PU0 | CRCW06034K70FKEA | 4.7k | VTX | DRIVER_EN_G0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_EN_PU0 | CRCW06034K70FKEA | 4.7k | VTX | DRIVER_EN_G0 | 0603 | 1% 0.1W | nonpolar/bidirectional |
| UP | R_EN_PD0 | CRCW0603100KFKEA | 100k | DRIVER_EN_G0 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| DN | R_EN_PD0 | CRCW0603100KFKEA | 100k | DRIVER_EN_G0 | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_RET1_A | C0603C104K5RACTU | 100nF | AX_VIO_REF3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_RET1_B | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| UP | R_CLK_SRCLK0 | RC0603FR-0715RL | 15 | SRCLK_B0 | SRCLK_G0 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| DN | R_CLK_SRCLK0 | RC0603FR-0715RL | 15 | SRCLK_B0 | SRCLK_G0 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| UP | R_CLK_SRCLK1 | RC0603FR-0715RL | 15 | SRCLK_B1 | SRCLK_G1 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| DN | R_CLK_SRCLK1 | RC0603FR-0715RL | 15 | SRCLK_B1 | SRCLK_G1 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| UP | R_CLK_SRCLK2 | RC0603FR-0715RL | 15 | SRCLK_B2 | SRCLK_G2 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| DN | R_CLK_SRCLK2 | RC0603FR-0715RL | 15 | SRCLK_B2 | SRCLK_G2 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| UP | R_CLK_SRCLK3 | RC0603FR-0715RL | 15 | SRCLK_B3 | SRCLK_G3 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| DN | R_CLK_SRCLK3 | RC0603FR-0715RL | 15 | SRCLK_B3 | SRCLK_G3 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| UP | R_CLK_RCLK0 | RC0603FR-0715RL | 15 | RCLK_B0 | RCLK_G0 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| DN | R_CLK_RCLK0 | RC0603FR-0715RL | 15 | RCLK_B0 | RCLK_G0 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| UP | R_CLK_RCLK1 | RC0603FR-0715RL | 15 | RCLK_B1 | RCLK_G1 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| DN | R_CLK_RCLK1 | RC0603FR-0715RL | 15 | RCLK_B1 | RCLK_G1 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| UP | R_CLK_RCLK2 | RC0603FR-0715RL | 15 | RCLK_B2 | RCLK_G2 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| DN | R_CLK_RCLK2 | RC0603FR-0715RL | 15 | RCLK_B2 | RCLK_G2 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| UP | R_CLK_RCLK3 | RC0603FR-0715RL | 15 | RCLK_B3 | RCLK_G3 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| DN | R_CLK_RCLK3 | RC0603FR-0715RL | 15 | RCLK_B3 | RCLK_G3 | 0603 | 0.1W ±1% | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_E | CRCW0603100KFKEA | 100k | ADC_DOUTE | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_F | CRCW0603100KFKEA | 100k | ADC_DOUTF | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_G | CRCW0603100KFKEA | 100k | ADC_DOUTG | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | R_ADC_RETURN_PD_H | CRCW0603100KFKEA | 100k | ADC_DOUTH | GND | 0603 | 1% 0.1W | nonpolar/bidirectional |
| CENTRAL | C_U_RET0_A | C0603C104K5RACTU | 100nF | AX_VIO_REF3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_RET0_B | C0603C104K5RACTU | 100nF | V5A | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_U_BUSYBUF | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar/bidirectional |
| CENTRAL | C_B1_BULK | 25SVPF47M | 47uF | V3V3 | GND | Panasonic C6 Ø6.3mm height6mm polar | 25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C | pin1positive;pin2negative |
| CENTRAL | C_B1_FF | C0603C221J5GACTU | 220pF | V3V3 | BUCK1_FB | 0603 | 50V C0G ±5%; TPS54202equation16 feedforward | nonpolar |
| CENTRAL | C_B2_BULK | 25SVPF47M | 47uF | V7V15 | GND | Panasonic C6 Ø6.3mm height6mm polar | 25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C | pin1positive;pin2negative |
| CENTRAL | C_B2_FF | C0603C221J5GACTU | 220pF | V7V15 | BUCK2_FB | 0603 | 50V C0G ±5%; TPS54202equation16 feedforward | nonpolar |
| UP | C_B1_BULK | 25SVPF47M | 47uF | V3V3 | GND | Panasonic C6 Ø6.3mm height6mm polar | 25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C | pin1positive;pin2negative |
| UP | C_B1_FF | C0603C221J5GACTU | 220pF | V3V3 | BUCK1_FB | 0603 | 50V C0G ±5%; TPS54202equation16 feedforward | nonpolar |
| UP | C_B2_BULK | 25SVPF47M | 47uF | V7V15 | GND | Panasonic C6 Ø6.3mm height6mm polar | 25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C | pin1positive;pin2negative |
| UP | C_B2_FF | C0603C221J5GACTU | 220pF | V7V15 | BUCK2_FB | 0603 | 50V C0G ±5%; TPS54202equation16 feedforward | nonpolar |
| UP | C_B3_FF | C0603C221J5GACTU | 220pF | VTX_PRE | BUCK3_FB | 0603 | 50V C0G ±5%; TPS54202equation16 feedforward | nonpolar |
| DN | C_B1_BULK | 25SVPF47M | 47uF | V3V3 | GND | Panasonic C6 Ø6.3mm height6mm polar | 25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C | pin1positive;pin2negative |
| DN | C_B1_FF | C0603C221J5GACTU | 220pF | V3V3 | BUCK1_FB | 0603 | 50V C0G ±5%; TPS54202equation16 feedforward | nonpolar |
| DN | C_B2_BULK | 25SVPF47M | 47uF | V7V15 | GND | Panasonic C6 Ø6.3mm height6mm polar | 25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C | pin1positive;pin2negative |
| DN | C_B2_FF | C0603C221J5GACTU | 220pF | V7V15 | BUCK2_FB | 0603 | 50V C0G ±5%; TPS54202equation16 feedforward | nonpolar |
| DN | C_B3_FF | C0603C221J5GACTU | 220pF | VTX_PRE | BUCK3_FB | 0603 | 50V C0G ±5%; TPS54202equation16 feedforward | nonpolar |
| CENTRAL | R_RX_UP00 | RC0603FR-0722RL | 22 | UP_DATA_RAW_00 | UP_DATA_FILT_00 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP00 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_00 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP00 | RC0603FR-0747RL | 47 | UP_DATA_DRV_00 | UP_DATA_00 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP01 | RC0603FR-0722RL | 22 | UP_DATA_RAW_01 | UP_DATA_FILT_01 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP01 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_01 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP01 | RC0603FR-0747RL | 47 | UP_DATA_DRV_01 | UP_DATA_01 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP02 | RC0603FR-0722RL | 22 | UP_DATA_RAW_02 | UP_DATA_FILT_02 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP02 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_02 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP02 | RC0603FR-0747RL | 47 | UP_DATA_DRV_02 | UP_DATA_02 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP03 | RC0603FR-0722RL | 22 | UP_DATA_RAW_03 | UP_DATA_FILT_03 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP03 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_03 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP03 | RC0603FR-0747RL | 47 | UP_DATA_DRV_03 | UP_DATA_03 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP04 | RC0603FR-0722RL | 22 | UP_DATA_RAW_04 | UP_DATA_FILT_04 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP04 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_04 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP04 | RC0603FR-0747RL | 47 | UP_DATA_DRV_04 | UP_DATA_04 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP05 | RC0603FR-0722RL | 22 | UP_DATA_RAW_05 | UP_DATA_FILT_05 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP05 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_05 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP05 | RC0603FR-0747RL | 47 | UP_DATA_DRV_05 | UP_DATA_05 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP06 | RC0603FR-0722RL | 22 | UP_DATA_RAW_06 | UP_DATA_FILT_06 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP06 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_06 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP06 | RC0603FR-0747RL | 47 | UP_DATA_DRV_06 | UP_DATA_06 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP07 | RC0603FR-0722RL | 22 | UP_DATA_RAW_07 | UP_DATA_FILT_07 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP07 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_07 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP07 | RC0603FR-0747RL | 47 | UP_DATA_DRV_07 | UP_DATA_07 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP08 | RC0603FR-0722RL | 22 | UP_DATA_RAW_08 | UP_DATA_FILT_08 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP08 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_08 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP08 | RC0603FR-0747RL | 47 | UP_DATA_DRV_08 | UP_DATA_08 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP09 | RC0603FR-0722RL | 22 | UP_DATA_RAW_09 | UP_DATA_FILT_09 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP09 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_09 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP09 | RC0603FR-0747RL | 47 | UP_DATA_DRV_09 | UP_DATA_09 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP10 | RC0603FR-0722RL | 22 | UP_DATA_RAW_10 | UP_DATA_FILT_10 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP10 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_10 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP10 | RC0603FR-0747RL | 47 | UP_DATA_DRV_10 | UP_DATA_10 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP11 | RC0603FR-0722RL | 22 | UP_DATA_RAW_11 | UP_DATA_FILT_11 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP11 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_11 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP11 | RC0603FR-0747RL | 47 | UP_DATA_DRV_11 | UP_DATA_11 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP12 | RC0603FR-0722RL | 22 | UP_DATA_RAW_12 | UP_DATA_FILT_12 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP12 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_12 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP12 | RC0603FR-0747RL | 47 | UP_DATA_DRV_12 | UP_DATA_12 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP13 | RC0603FR-0722RL | 22 | UP_DATA_RAW_13 | UP_DATA_FILT_13 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP13 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_13 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP13 | RC0603FR-0747RL | 47 | UP_DATA_DRV_13 | UP_DATA_13 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP14 | RC0603FR-0722RL | 22 | UP_DATA_RAW_14 | UP_DATA_FILT_14 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP14 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_14 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP14 | RC0603FR-0747RL | 47 | UP_DATA_DRV_14 | UP_DATA_14 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_UP15 | RC0603FR-0722RL | 22 | UP_DATA_RAW_15 | UP_DATA_FILT_15 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_UP15 | CC0603JRNPO9BN3R3 | 3.3pF | UP_DATA_FILT_15 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP15 | RC0603FR-0747RL | 47 | UP_DATA_DRV_15 | UP_DATA_15 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN00 | RC0603FR-0722RL | 22 | DN_DATA_RAW_00 | DN_DATA_FILT_00 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN00 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_00 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN00 | RC0603FR-0747RL | 47 | DN_DATA_DRV_00 | DN_DATA_00 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN01 | RC0603FR-0722RL | 22 | DN_DATA_RAW_01 | DN_DATA_FILT_01 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN01 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_01 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN01 | RC0603FR-0747RL | 47 | DN_DATA_DRV_01 | DN_DATA_01 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN02 | RC0603FR-0722RL | 22 | DN_DATA_RAW_02 | DN_DATA_FILT_02 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN02 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_02 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN02 | RC0603FR-0747RL | 47 | DN_DATA_DRV_02 | DN_DATA_02 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN03 | RC0603FR-0722RL | 22 | DN_DATA_RAW_03 | DN_DATA_FILT_03 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN03 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_03 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN03 | RC0603FR-0747RL | 47 | DN_DATA_DRV_03 | DN_DATA_03 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN04 | RC0603FR-0722RL | 22 | DN_DATA_RAW_04 | DN_DATA_FILT_04 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN04 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_04 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN04 | RC0603FR-0747RL | 47 | DN_DATA_DRV_04 | DN_DATA_04 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN05 | RC0603FR-0722RL | 22 | DN_DATA_RAW_05 | DN_DATA_FILT_05 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN05 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_05 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN05 | RC0603FR-0747RL | 47 | DN_DATA_DRV_05 | DN_DATA_05 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN06 | RC0603FR-0722RL | 22 | DN_DATA_RAW_06 | DN_DATA_FILT_06 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN06 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_06 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN06 | RC0603FR-0747RL | 47 | DN_DATA_DRV_06 | DN_DATA_06 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN07 | RC0603FR-0722RL | 22 | DN_DATA_RAW_07 | DN_DATA_FILT_07 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN07 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_07 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN07 | RC0603FR-0747RL | 47 | DN_DATA_DRV_07 | DN_DATA_07 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN08 | RC0603FR-0722RL | 22 | DN_DATA_RAW_08 | DN_DATA_FILT_08 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN08 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_08 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN08 | RC0603FR-0747RL | 47 | DN_DATA_DRV_08 | DN_DATA_08 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN09 | RC0603FR-0722RL | 22 | DN_DATA_RAW_09 | DN_DATA_FILT_09 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN09 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_09 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN09 | RC0603FR-0747RL | 47 | DN_DATA_DRV_09 | DN_DATA_09 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN10 | RC0603FR-0722RL | 22 | DN_DATA_RAW_10 | DN_DATA_FILT_10 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN10 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_10 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN10 | RC0603FR-0747RL | 47 | DN_DATA_DRV_10 | DN_DATA_10 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN11 | RC0603FR-0722RL | 22 | DN_DATA_RAW_11 | DN_DATA_FILT_11 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN11 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_11 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN11 | RC0603FR-0747RL | 47 | DN_DATA_DRV_11 | DN_DATA_11 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN12 | RC0603FR-0722RL | 22 | DN_DATA_RAW_12 | DN_DATA_FILT_12 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN12 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_12 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN12 | RC0603FR-0747RL | 47 | DN_DATA_DRV_12 | DN_DATA_12 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN13 | RC0603FR-0722RL | 22 | DN_DATA_RAW_13 | DN_DATA_FILT_13 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN13 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_13 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN13 | RC0603FR-0747RL | 47 | DN_DATA_DRV_13 | DN_DATA_13 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN14 | RC0603FR-0722RL | 22 | DN_DATA_RAW_14 | DN_DATA_FILT_14 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN14 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_14 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN14 | RC0603FR-0747RL | 47 | DN_DATA_DRV_14 | DN_DATA_14 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_DN15 | RC0603FR-0722RL | 22 | DN_DATA_RAW_15 | DN_DATA_FILT_15 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_DN15 | CC0603JRNPO9BN3R3 | 3.3pF | DN_DATA_FILT_15 | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_DN15 | RC0603FR-0747RL | 47 | DN_DATA_DRV_15 | DN_DATA_15 | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_U_TXB0 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| CENTRAL | C_U_TXB1 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| CENTRAL | C_U_TXB2 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| CENTRAL | C_U_TXB3 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| CENTRAL | R_RX_SRCLK | RC0603FR-0722RL | 22 | MASTER_SRCLK | MASTER_SRCLK_FILT | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_SRCLK | CC0603JRNPO9BN3R3 | 3.3pF | MASTER_SRCLK_FILT | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP_SRCLK | RC0603FR-0747RL | 47 | UP_SRCLK_DRV | UP_SRCLK | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_TX_DN_SRCLK | RC0603FR-0747RL | 47 | DN_SRCLK_DRV | DN_SRCLK | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RX_RCLK | RC0603FR-0722RL | 22 | MASTER_RCLK | MASTER_RCLK_FILT | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_RX_RCLK | CC0603JRNPO9BN3R3 | 3.3pF | MASTER_RCLK_FILT | GND | 0603 | 50V C0G ±5% | nonpolar |
| CENTRAL | R_TX_UP_RCLK | RC0603FR-0747RL | 47 | UP_RCLK_DRV | UP_RCLK | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_TX_DN_RCLK | RC0603FR-0747RL | 47 | DN_RCLK_DRV | DN_RCLK | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_U_TXCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_TX_LOCAL | 25SVPF47M | 47uF | VTX_PRE | GND | Panasonic C6 Ø6.3mm height6mm polar | 25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C | pin1positive;pin2negative |
| UP | R_GATE_DRIVE | RC0603FR-0710KL | 10k | TX_GATE | CUT_COLLECTOR | 0603 | 0.1W ±1% | nonpolar |
| UP | C_TX_MILLER | C1206C103J5GACTU | 10nF | TX_GATE | VTX | 1206 | 50V C0G ±5%; drain-to-gate softstart; notgate-to-source | nonpolar |
| UP | C_U_DBUF0 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_U_DBUF1 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_U_CLK_SRCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_U_CLK_RCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | R_ENCLAMP0 | RC0603FR-078K2L | 8.2k | VTX | ENCLAMP_BASE_G0 | 0603 | 0.1W ±1% | nonpolar |
| UP | C_U_WDIV_SRCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_U_WD_SRCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | R_WD_SRCLK | RC0603FR-07100KL | 100k | SRCLK_SET | GND | 0603 | 0.1W ±1% | nonpolar |
| UP | C_U_WDIV_RCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_U_WD_RCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | R_WD_RCLK | RC0603FR-07100KL | 100k | RCLK_SET | GND | 0603 | 0.1W ±1% | nonpolar |
| UP | C_U_WDAND | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_U_PERMIT_INV | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_U_WDOR | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | R_FAULT_FILTER | RC0603FR-071KL | 1k | WD_REPORT_OK | WD_REPORT_RC | 0603 | 0.1W ±1% | nonpolar |
| UP | C_FAULT_FILTER | C0603C102J5GACTU | 1nF | WD_REPORT_RC | GND | 0603 | 50V C0G ±5% | nonpolar |
| UP | C_U_FAULT_SCHMITT | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| UP | C_U_FAULTAND | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_TX_LOCAL | 25SVPF47M | 47uF | VTX_PRE | GND | Panasonic C6 Ø6.3mm height6mm polar | 25V ±20%; ESR≤30mΩ; ripple2.8Arms@100kHz;−55..105°C | pin1positive;pin2negative |
| DN | R_GATE_DRIVE | RC0603FR-0710KL | 10k | TX_GATE | CUT_COLLECTOR | 0603 | 0.1W ±1% | nonpolar |
| DN | C_TX_MILLER | C1206C103J5GACTU | 10nF | TX_GATE | VTX | 1206 | 50V C0G ±5%; drain-to-gate softstart; notgate-to-source | nonpolar |
| DN | C_U_DBUF0 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_U_DBUF1 | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_U_CLK_SRCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_U_CLK_RCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | R_ENCLAMP0 | RC0603FR-078K2L | 8.2k | VTX | ENCLAMP_BASE_G0 | 0603 | 0.1W ±1% | nonpolar |
| DN | C_U_WDIV_SRCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_U_WD_SRCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | R_WD_SRCLK | RC0603FR-07100KL | 100k | SRCLK_SET | GND | 0603 | 0.1W ±1% | nonpolar |
| DN | C_U_WDIV_RCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_U_WD_RCLK | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | R_WD_RCLK | RC0603FR-07100KL | 100k | RCLK_SET | GND | 0603 | 0.1W ±1% | nonpolar |
| DN | C_U_WDAND | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_U_PERMIT_INV | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_U_WDOR | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | R_FAULT_FILTER | RC0603FR-071KL | 1k | WD_REPORT_OK | WD_REPORT_RC | 0603 | 0.1W ±1% | nonpolar |
| DN | C_FAULT_FILTER | C0603C102J5GACTU | 1nF | WD_REPORT_RC | GND | 0603 | 50V C0G ±5% | nonpolar |
| DN | C_U_FAULT_SCHMITT | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| DN | C_U_FAULTAND | C0603C104K5RACTU | 100nF | V3V3 | GND | 0603 | 50V X7R ±10% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP00 | RC0603FR-0710KL | 10k | UP_DATA_RAW_00 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP01 | RC0603FR-0710KL | 10k | UP_DATA_RAW_01 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP02 | RC0603FR-0710KL | 10k | UP_DATA_RAW_02 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP03 | RC0603FR-0710KL | 10k | UP_DATA_RAW_03 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP04 | RC0603FR-0710KL | 10k | UP_DATA_RAW_04 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP05 | RC0603FR-0710KL | 10k | UP_DATA_RAW_05 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP06 | RC0603FR-0710KL | 10k | UP_DATA_RAW_06 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP07 | RC0603FR-0710KL | 10k | UP_DATA_RAW_07 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP08 | RC0603FR-0710KL | 10k | UP_DATA_RAW_08 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP09 | RC0603FR-0710KL | 10k | UP_DATA_RAW_09 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP10 | RC0603FR-0710KL | 10k | UP_DATA_RAW_10 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP11 | RC0603FR-0710KL | 10k | UP_DATA_RAW_11 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP12 | RC0603FR-0710KL | 10k | UP_DATA_RAW_12 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP13 | RC0603FR-0710KL | 10k | UP_DATA_RAW_13 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP14 | RC0603FR-0710KL | 10k | UP_DATA_RAW_14 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_UP15 | RC0603FR-0710KL | 10k | UP_DATA_RAW_15 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN00 | RC0603FR-0710KL | 10k | DN_DATA_RAW_00 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN01 | RC0603FR-0710KL | 10k | DN_DATA_RAW_01 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN02 | RC0603FR-0710KL | 10k | DN_DATA_RAW_02 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN03 | RC0603FR-0710KL | 10k | DN_DATA_RAW_03 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN04 | RC0603FR-0710KL | 10k | DN_DATA_RAW_04 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN05 | RC0603FR-0710KL | 10k | DN_DATA_RAW_05 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN06 | RC0603FR-0710KL | 10k | DN_DATA_RAW_06 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN07 | RC0603FR-0710KL | 10k | DN_DATA_RAW_07 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN08 | RC0603FR-0710KL | 10k | DN_DATA_RAW_08 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN09 | RC0603FR-0710KL | 10k | DN_DATA_RAW_09 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN10 | RC0603FR-0710KL | 10k | DN_DATA_RAW_10 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN11 | RC0603FR-0710KL | 10k | DN_DATA_RAW_11 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN12 | RC0603FR-0710KL | 10k | DN_DATA_RAW_12 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN13 | RC0603FR-0710KL | 10k | DN_DATA_RAW_13 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN14 | RC0603FR-0710KL | 10k | DN_DATA_RAW_14 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DATA_RAW_PD_DN15 | RC0603FR-0710KL | 10k | DN_DATA_RAW_15 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DEF_MASTER_SRCLK | RC0603FR-0710KL | 10k | MASTER_SRCLK | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DEF_MASTER_RCLK | RC0603FR-0710KL | 10k | MASTER_RCLK | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DEF_MASTER_HB | RC0603FR-0710KL | 10k | MASTER_HB | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DEF_UP_TX_PERMIT_RAW | RC0603FR-0710KL | 10k | UP_TX_PERMIT_RAW | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_DEF_DN_TX_PERMIT_RAW | RC0603FR-0710KL | 10k | DN_TX_PERMIT_RAW | GND | 0603 | 0.1W ±1% | nonpolar |
| UP | R_DEF_SRCLK | RC0603FR-0710KL | 10k | SRCLK | GND | 0603 | 0.1W ±1% | nonpolar |
| DN | R_DEF_SRCLK | RC0603FR-0710KL | 10k | SRCLK | GND | 0603 | 0.1W ±1% | nonpolar |
| UP | R_DEF_RCLK | RC0603FR-0710KL | 10k | RCLK | GND | 0603 | 0.1W ±1% | nonpolar |
| DN | R_DEF_RCLK | RC0603FR-0710KL | 10k | RCLK | GND | 0603 | 0.1W ±1% | nonpolar |
| UP | R_DEF_HB | RC0603FR-0710KL | 10k | HB | GND | 0603 | 0.1W ±1% | nonpolar |
| DN | R_DEF_HB | RC0603FR-0710KL | 10k | HB | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_AXVIO_BLEED | RC0603FR-071KL | 1k | AX_VIO_REF3V3 | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | C_ENTRY_HF | C1206C105K5RACTU | 1uF | DC12_AFTER_SWITCH | GND | 1206 | 50V X7R ±10%; nonpolar input hotplug capacitor | nonpolar |
| UP | C_ENTRY_HF | C1206C105K5RACTU | 1uF | DC12_AFTER_SWITCH | GND | 1206 | 50V X7R ±10%; nonpolar input hotplug capacitor | nonpolar |
| DN | C_ENTRY_HF | C1206C105K5RACTU | 1uF | DC12_AFTER_SWITCH | GND | 1206 | 50V X7R ±10%; nonpolar input hotplug capacitor | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET0_3 | RC0603FR-0710KL | 10k | ADC_DOUTA_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET0_4 | RC0603FR-0710KL | 10k | ADC_DOUTB_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET0_5 | RC0603FR-0710KL | 10k | ADC_DOUTC_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET0_6 | RC0603FR-0710KL | 10k | ADC_DOUTD_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET0_7 | RC0603FR-0710KL | 10k | ADC_DOUTE_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET0_8 | RC0603FR-0710KL | 10k | ADC_DOUTF_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET0_9 | RC0603FR-0710KL | 10k | ADC_DOUTG_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET0_10 | RC0603FR-0710KL | 10k | ADC_DOUTH_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET1_3 | RC0603FR-0710KL | 10k | UP_PGOOD_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET1_4 | RC0603FR-0710KL | 10k | DN_PGOOD_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET1_5 | RC0603FR-0710KL | 10k | UP_FAULT_N_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET1_6 | RC0603FR-0710KL | 10k | DN_FAULT_N_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET1_7 | RC0603FR-0710KL | 10k | GLOBAL_OK_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |
| CENTRAL | R_RETURN_PD_U_RET1_8 | RC0603FR-0710KL | 10k | ADC_BUSY_FPGA | GND | 0603 | 0.1W ±1% | nonpolar |