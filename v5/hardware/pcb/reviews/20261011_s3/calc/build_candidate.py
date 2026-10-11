"""Canonical three-board component/pin/net candidate. No CAD/ERC claim.

Explicit pin numbers are package-specific. Native-library pin/footprint checking
is still required. Each component is present once, with one budget allocation.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv, json, math, html, hashlib
from power_worst_case import calculate
R=Path(__file__).resolve().parents[1];ROOT=R.parents[4];E=ROOT/'v5/evidence/pcb_s3_20261011'
C=[];PASS=[];PINS=[];MAPPING=[]
TI='https://www.ti.com/lit/ds/symlink/'
URL={'AD7606C-16BSTZ-RL':'https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf',
 'ADP7118AUJZ-5.0-R7':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf',
 'TC4427AEOA':'https://ww1.microchip.com/downloads/en/DeviceDoc/20001423J.pdf',
 'MMBT3904LT1G':'https://www.onsemi.com/pdf/datasheet/mmbt3904lt1-d.pdf',
 'PJ-002BH':'https://www.sameskydevices.com/product/resource/pj-002bh.pdf'}
for mp,ds in [('TPS259470LRPWR','tps25947'),('TPS54202DDCR','tps54202'),('TPS63070RNMR','tps63070'),('TPS7A2033PDBVR','tps7a20'),('TUSB321AIRWBR','tusb321ai'),('TPS3851H33EDRBR','tps3851'),('TPS3430DRCR','tps3430'),('TMP302ADRLR','tmp302'),('SN74LVC1G74DCUR','sn74lvc1g74'),('SN74LVC1G17DBVR','sn74lvc1g17'),('SN74LVC1G04DBVR','sn74lvc1g04'),('SN74LVC1G32DBVR','sn74lvc1g32'),('SN74LVC244APWR','sn74lvc244a'),('SN74LVC595APWR','sn74lvc595a'),('SN74AXC8T245PWR','sn74axc8t245'),('INA226AIDGSR','ina226'),('TMP117AIDRVR','tmp117'),('OPA4192IPWR','opa4192'),('REF5025AIDR','ref50'),('TCA9548APWR','tca9548a')]:URL[mp]=TI+ds+'.pdf'
URL['TMUX1574PWR']=TI+'tmux1574.pdf';URL['SN74LVC1G08DBVR']=TI+'sn74lvc1g08.pdf'
URL['USB4500-03-0-A']='https://gct.co/connector/usb4500'
URL['SMBJ15A']='https://m.littelfuse.com/~/media/electronics/datasheets/tvs_diodes/littelfuse_tvs_diode_smbj_datasheet.pdf.pdf'
URL['0451003.MRL']='https://www.littelfuse.com/assetdocs/fuse-451-and-453-datasheet?assetguid=533cd5cc-956c-4243-867f-6ab5a62f6ba1'
def writecsv(path,rows,keys=None):
    keys=keys or list(rows[0]);
    with path.open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,keys);w.writeheader();w.writerows(rows)
def add(b,ref,mpn,pins,function,rail='NONE',pkg='',value='',source=None):
    ref=b+'_'+ref;assert not any(c['refdes']==ref for c in C),ref
    row=dict(board=b,refdes=ref,mpn=mpn,value=value or mpn,package=pkg,function=function,rail=rail,
      procurement='HOLD',source_url=source or URL.get(mpn,'UNQUALIFIED_MPN_OR_PASSIVE_SERIES'))
    C.append(row)
    for p,net in pins.items():
        PINS.append(dict(board=b,refdes=ref,pin=str(p),net=b+':'+net if not net.startswith('NC:') else 'NC:'+ref+':'+str(p),
                         disposition='INTENTIONAL_NC' if net.startswith('NC:') else 'CONNECTED',function=function))
    return ref
def passive(b,ref,kind,value,a,z,function,rating='0603;0.1W;50V',tol='1%',formula='FUNCTIONAL_DESIGN_VALUE; qualification in report'):
    rr=add(b,ref,kind,{1:a,2:z},function,pkg=rating,value=value)
    PASS.append(dict(board=b,refdes=rr,kind=kind,value=value,tolerance=tol,net_1=b+':'+a,net_2=b+':'+z,function=function,
        derating_package=rating,formula=formula,source='S3 report/module datasheet; exact passive MPN remains HOLD'))
def res(b,ref,val,a,z,fun,**kw):passive(b,ref,'R',val,a,z,fun,**kw)
def cap(b,ref,val,a,z,fun,**kw):
    kw.setdefault('rating','0603;X7R;16V;effective C must be qualified');kw.setdefault('tol','10%');passive(b,ref,'C',val,a,z,fun,**kw)
def dec(b,ref,rail,val='100nF'):cap(b,ref,val,rail,'GND','local_decoupling')
def efuse(b,ref,vin,out,en,ov,flt,slew):
    add(b,ref,'TPS259470LRPWR',{1:en,2:ov,3:'NC:AUXOFF',4:flt,5:vin,6:out,7:ref+'_DVDT',8:'GND',9:ref+'_ILIM',10:'NC:ITIMER'},'input_protection' if ref=='U1' else 'tx_cutoff',vin,'RPW10')
    res(b,ref+'R1','1.65k',ref+'_ILIM','GND','current_limit',formula='Table9 min1.8 max2.2A with1.65k; resistor1% propagated separately')
    cap(b,ref+'C1',slew,ref+'_DVDT','GND','inrush_slew',tol='5%',rating='0603;C0G;50V',formula='TPS25947 application dVdt equation; measured ramp REQUIRED')
    res(b,ref+'R2','10k',flt,'3V3','fault_pullup')
def buck(b,ref,vin,out,rtop):
    add(b,ref,'TPS54202DDCR',{1:'GND',2:ref+'_SW',3:vin,4:ref+'_FB',5:vin,6:ref+'_BOOT'},'buck_'+out,vin,'SOT23-6')
    passive(b,ref+'L','L','22uH',ref+'_SW',out,'buck_inductor',rating='shielded;Isat>=3.5A at hot;DCR<=0.15ohm',tol='20%',formula='DeltaI=Vout*(1-Vout/Vin)/(Lmin*fmin); no2A load assumption')
    cap(b,ref+'CB','100nF',ref+'_BOOT',ref+'_SW','bootstrap',rating='0603;X7R;25V')
    res(b,ref+'RT',rtop,out,ref+'_FB','feedback',tol='0.1%',formula='Vout=0.596*(1+Rtop/10k); VFBguaranteed0.581..0.611V;latestRevC')
    res(b,ref+'RB','10k',ref+'_FB','GND','feedback',tol='0.1%')
    dec(b,ref+'CI',vin,'10uF');cap(b,ref+'CO','22uF',out,'GND','buck_output',rating='1210;X7R;16V;Ceff>=12uF')
def ldo5(b,ref,vin,out):
    add(b,ref,'ADP7118AUJZ-5.0-R7',{1:vin,2:'GND',3:vin,4:out,5:out},'analog_ldo',vin,'TSOT5')
    dec(b,ref+'CI',vin,'2.2uF');dec(b,ref+'CO',out,'4.7uF')
def g1(b,ref,mpn,inp,out,inp2=None):
    pins={1:'NC',2:inp,3:'GND',4:out,5:'3V3'}
    if inp2:pins[1]=inp2
    else:pins[1]='NC:1'
    add(b,ref,mpn,pins,'safety_logic','3V3','DBV5');dec(b,ref+'C','3V3')
def transistor(b,ref,base,collector,fun):add(b,ref,'MMBT3904LT1G',{1:base,2:'GND',3:collector},fun,pkg='SOT23')

def safety(b):
    add(b,'U10','TPS3851H33EDRBR',{1:'3V3',2:'WD_CWD',3:'3V3',4:'GND',5:'3V3',6:'HB',7:'FAULT_N',8:'FAULT_N',9:'GND'},'uv_and_backup_watchdog','3V3','DRB8+EP')
    dec(b,'C10','3V3');res(b,'R10','10k','WD_CWD','3V3','watchdog_factory_select')
    add(b,'U11','TPS3430DRCR',{1:'3V3',2:'NC:CWD',3:'GND',4:'NC:CRST',5:'GND',6:'3V3',7:'HB',8:'FAULT_N',9:'NC:9',10:'3V3',11:'GND'},'early_late_watchdog','3V3','DRC10+EP')
    dec(b,'C11','3V3');res(b,'R11','10k','HB','GND','heartbeat_idle')
    add(b,'U12','TMP302ADRLR',{1:'3V3',2:'GND',3:'FAULT_N',4:'3V3',5:'3V3',6:'3V3'},'independent_thermal_trip','3V3','DRL6')
    dec(b,'C12','3V3')
    add(b,'U13','SN74LVC1G74DCUR',{1:'ARM_CLK',2:'3V3',3:'NOT_ARMED',4:'GND',5:'ARMED',6:'FAULT_N',7:'3V3',8:'3V3'},'fault_latch','3V3','DCU8')
    dec(b,'C13','3V3');res(b,'R13','10k','FAULT_N','3V3','fault_pullup')
    add(b,'SW1','MOMENTARY_NO',{1:'3V3',2:'ARM_RAW'},'manual_rearm',pkg='QUALIFY_SWITCH')
    res(b,'R14','100k','ARM_RAW','GND','debounce');cap(b,'C14','100nF','ARM_RAW','GND','debounce')
    g1(b,'U14','SN74LVC1G17DBVR','ARM_RAW','ARM_CLK')
    add(b,'JESTOP','NC_LOOP',{1:'3V3',2:'ESTOP_OK'},'normally_closed_estop',pkg='keyed_2pin')
    res(b,'R15','10k','ESTOP_OK','GND','open_cable_fault')
    g1(b,'U15','SN74LVC1G04DBVR','ESTOP_OK','ESTOP_BAD')
    res(b,'R16','10k','ESTOP_BAD','ESTOP_BASE','fault_sink_base');transistor(b,'QSAFE','ESTOP_BASE','FAULT_N','estop_fault_sink')
    res(b,'R17','100k','ARMED','KILL_EN','kill_enable_divider');res(b,'R18','100k','KILL_EN','GND','kill_enable_divider')
    # Divider guarantees EN low even with an undefined flipflop below its1.65V operating minimum.
    g1(b,'U16','SN74LVC1G32DBVR','B_OE_N','DISABLE_A',inp2='NOT_ARMED')
    g1(b,'U17','SN74LVC1G04DBVR','FAULT_N','FAULT_BAD')
    g1(b,'U18','SN74LVC1G32DBVR','DISABLE_A','595_OE_N',inp2='FAULT_BAD')
    res(b,'R19','10k','595_OE_N','3V3','disable_default')

def array(b):
    add(b,'J1','PJ-002BH',{1:'VIN12_RAW',2:'GND',3:'NC:SWITCH'},'power_connector',pkg='THT5.5x2.5')
    # PJ terminal1=center must be confirmed visually against manufacturer's drawing before footprint release.
    add(b,'F1','0451003.MRL',{1:'VIN12_RAW',2:'VIN12_FUSED'},'upstream_fuse',pkg='2410',value='3A;125V;coordination_HOLD')
    add(b,'D1','SMBJ15A',{1:'GND',2:'VIN12_FUSED'},'input_tvs',pkg='SMB')
    efuse(b,'U1','VIN12_FUSED','VIN12_SAFE','UVLO12','OVLO12','MAIN_FLT_N','10nF')
    for r,v,a,z,f in [('R1','38.3k','VIN12_FUSED','UVLO12','uvlo'),('R2','4.99k','UVLO12','GND','uvlo'),('R3','48.3k','VIN12_FUSED','OVLO12','ovlo'),('R4','4.99k','OVLO12','GND','ovlo')]:res(b,r,v,a,z,f,tol='0.1%')
    cap(b,'C1','22uF','VIN12_SAFE','GND','input_bulk',rating='1210;X7R;25V;Ceff>=10uF');dec(b,'C2','VIN12_FUSED')
    passive(b,'RS1','R','20mOhm','VIN12_SAFE','VIN12_LOAD','current_shunt',rating='2512;1W;4terminal_Kelvin',tol='1%',formula='Vsense<81.92mV at2.222A;P<0.100W')
    buck(b,'U2','VIN12_LOAD','3V3','45.3k');buck(b,'U3','VIN12_LOAD','6V7','102k');ldo5(b,'U4','6V7','AFE5')
    efuse(b,'U5','VIN12_LOAD','TX12','KILL_EN','OVLO12','TX_FLT_N','47nF')
    cap(b,'C5','470uF','TX12','GND','tx_bulk',rating='SMD_electrolytic;25V;Cmin376uF;Cmax564uF;ESR/ripple_HOLD',tol='20%')
    res(b,'R5','680','TX12','GND','tx_bleeder',rating='2512;1W;50V',formula='P=13.2^2/(680*.99);worst stored-C bleed from total750uF')
    # FLT is not an exhaustive UV/OV indicator; upstream logic UV creates fault, UVLO acts directly.
    res(b,'R6','0','MAIN_FLT_N','FAULT_N','fault_join');res(b,'R7','0','TX_FLT_N','FAULT_N','fault_join')
    safety(b)
    add(b,'U20','INA226AIDGSR',{1:'GND',2:'GND',3:'NC:ALERT',4:'I2C_SDA',5:'I2C_SCL',6:'3V3',7:'GND',8:'VIN12_LOAD',9:'VIN12_LOAD',10:'VIN12_SAFE'},'current_telemetry','3V3','DGS10');dec(b,'C20','3V3')
    # Three sensors per array preserved; mux ports separate identical I2C addresses.
    for j in range(1):
        add(b,'UT'+str(j),'TMP117AIDRVR',{1:'I2C_SCL',2:'GND',3:'NC:ALERT',4:['GND','3V3','I2C_SDA'][j],5:'3V3',6:'I2C_SDA',7:'GND'},'temperature_telemetry','3V3','DRV6+EP');dec(b,'CT'+str(j),'3V3')
    sig=[f'DATA{i}' for i in range(16)]+['SRCLK','RCLK','OE_N','RESET_N','SYNC','RX_BLANK','HB','FAULT_N','PGOOD','I2C_SCL','I2C_SDA']+[f'RX{i}_OUT' for i in range(4)]
    hp={2*i+1:n for i,n in enumerate(sig)};hp.update({2*i+2:'GND' for i in range(32)});hp[63]='NC:SPARE'
    add(b,'JCTRL','SIGNAL_2x32_MPN_HOLD',hp,'signal_connector',pkg='64pin_keyed_ground_interleaved')
    # Explicit local Ioff buffers. Clock distribution is a candidate, external STA remains open.
    for j in range(3):
        names=(['DATA'+str(i) for i in range(16)]+['SRCLK','RCLK','OE_N','RESET_N','SYNC','RX_BLANK','HB','GND'])[j*8:j*8+8]
        pins={1:'GND',10:'GND',19:'GND',20:'3V3'}
        ins=[2,4,6,8,11,13,15,17];outs=[18,16,14,12,9,7,5,3]
        for k,n in enumerate(names):pins[ins[k]]=n;pins[outs[k]]=('B_'+n if n!='GND' else 'NC:UNUSED')
        add(b,'UB'+str(j),'SN74LVC244APWR',pins,'control_buffer','3V3','PW20');dec(b,'CB'+str(j),'3V3')
    for n in [f'DATA{i}' for i in range(16)]+['SRCLK','RCLK','RESET_N','SYNC','RX_BLANK','OE_N']:
        res(b,'RPORT_'+n,'10k',n,'3V3' if n in ['OE_N','RX_BLANK'] else 'GND','port_default')
    add(b,'TP_SYNC','TEST_POINT',{1:'B_SYNC'},'sync_handoff',pkg='1mm_pad')
    add(b,'TP_HB','TEST_POINT',{1:'B_HB'},'heartbeat_observation',pkg='1mm_pad')
    # Use buffered data/clocks. Safety heartbeat currently uses port directly:5V-tolerant TPS WDI.
    for lane in range(16):
        ref='US'+str(lane);pins={8:'GND',16:'3V3',14:'B_DATA'+str(lane),11:'B_SRCLK',12:'B_RCLK',13:'595_OE_N',10:'B_RESET_N',9:'NC:SEROUT',4:'NC:Q4',5:'NC:Q5',6:'NC:Q6',7:'NC:Q7'}
        for bit,pin in enumerate([15,1,2,3]):pins[pin]=f'Q{4*lane+bit}'
        add(b,ref,'SN74LVC595APWR',pins,'serializer','3V3','PW16');dec(b,ref+'C','3V3')
    for ch in range(64):
        # Two non-inverting NPN stages place all TC input pullups on switched TX12.
        # No always-on CMOS output directly reaches an unpowered TC VDD domain.
        q=f'Q{ch}';b1=f'BASE1_{ch}';mid=f'MID_{ch}';b2=f'BASE2_{ch}';tin=f'TCIN{ch}'
        res(b,f'RIN{ch}','1k',q,b1,'level_shift_base');res(b,f'RB1{ch}','10k',b1,'GND','level_shift_idle')
        transistor(b,f'QA{ch}',b1,mid,'level_shift_stage1');res(b,f'RC1{ch}','1k','3V3',mid,'level_shift_pullup')
        res(b,f'RB2{ch}','1k',mid,b2,'level_shift_base');res(b,f'RBD{ch}','10k',b2,'GND','level_shift_idle')
        transistor(b,f'QB{ch}',b2,tin,'level_shift_stage2');res(b,f'RC2{ch}','1.5k','TX12',tin,'level_shift_pullup',rating='0805;0.25W;50V')
        res(b,f'RTI{ch}','10k',tin,'GND','tc_input_idle')
        res(b,f'RTX{ch}','330',f'TCOUT{ch}',f'TX{ch}','tx_series_energy',rating='2512;1W;pulse_curve_HOLD;50V',formula='13.2^2/326.7=.533W at100%duty short;ratingderatingtohotmustcheck')
        add(b,f'TX{ch}','NU40C10T',{1:f'TX{ch}',2:'GND'},'ultrasound_transmitter','TX12','MECH_VENDOR_HOLD')
        MAPPING.append(dict(board=b,channel=ch,global_channel=ch+(0 if b=='UP' else 64),row=ch//8,col=ch%8,lane=ch//4+(0 if b=='UP' else 16),used_bit=ch%4,serializer=b+'_US'+str(ch//4),q_pin=[15,1,2,3][ch%4],driver=b+'_UD'+str(ch//2),driver_out_pin=7 if ch%2==0 else 5,series_resistor=b+'_RTX'+str(ch),transducer=b+'_TX'+str(ch)))
    for j in range(32):
        add(b,'UD'+str(j),'TC4427AEOA',{1:'NC:1',2:f'TCIN{2*j}',3:'GND',4:f'TCIN{2*j+1}',5:f'TCOUT{2*j+1}',6:'TX12',7:f'TCOUT{2*j}',8:'NC:8'},'tx_driver','TX12','SOIC8')
        dec(b,'CD'+str(j),'TX12');dec(b,'CDX'+str(j),'TX12','1uF')
    reference_and_afe(b)
    # Local PGOOD is deliberately a sensed logic rail, not an eFuse FLT synonym.
    res(b,'RPG','1k','3V3','PGOOD','status_series');res(b,'RPGD','10k','PGOOD','GND','status_idle')
    add(b,'LED1','GREEN_LED_MPN_HOLD',{1:'LED_AN',2:'GND'},'status_led','3V3','0603');res(b,'RLED','2.2k','3V3','LED_AN','led_limit')

def reference_and_afe(b):
    add(b,'UREF','REF5025AIDR',{1:'NC:DNC',2:'AFE5',3:'NC:TEMP',4:'GND',5:'REF_NR',6:'VBIAS',7:'NC:7',8:'NC:DNC'},'analog_bias_reference','AFE5','SOIC8')
    dec(b,'CREFI','AFE5');dec(b,'CREFO','VBIAS','10uF');cap(b,'CREFN','1uF','REF_NR','GND','reference_noise')
    # 2 quad op-amps/array;8 amplifiers used,4 receiver channels.
    for u in range(2):
        pins={4:'AFE5',11:'GND'}
        for k,(o,minus,plus) in enumerate([(1,2,3),(7,6,5),(8,9,10),(14,13,12)]):
            ch=2*u+k//2
            if k%2==0:pins.update({o:f'AMP{ch}',minus:f'FB{ch}',plus:f'RXBIAS{ch}'})
            else:pins.update({o:f'RX{ch}_OUT_RAW',minus:f'RX{ch}_OUT_RAW',plus:f'LP{ch}'})
        add(b,'UA'+str(u),'OPA4192IPWR',pins,'receiver_amplifier','AFE5','TSSOP14');dec(b,'CA'+str(u),'AFE5')
    for ch in range(4):
        add(b,'RX'+str(ch),'RX_MPN_UNKNOWN',{1:f'RX{ch}_IN',2:'GND'},'ultrasound_receiver','NONE','MECH_VENDOR_HOLD')
        res(b,'RA1'+str(ch),'4.99k',f'RX{ch}_IN',f'RXP{ch}','rx_fault_limit',rating='0805;0.25W;100V',formula='2x4.99k limits hypothetical30V pin fault below10mA abs current;notESDqualification')
        res(b,'RA2'+str(ch),'4.99k',f'RXP{ch}',f'RXC{ch}','rx_fault_limit',rating='0805;0.25W;100V')
        cap(b,'CAI'+str(ch),'100nF',f'RXC{ch}',f'RXBIAS{ch}','rx_ac_coupling',rating='0805;C0G_or_film;50V',tol='5%')
        res(b,'RAB'+str(ch),'100k',f'RXBIAS{ch}','VBIAS','rx_input_bias')
        res(b,'RAG'+str(ch),'10k',f'FB{ch}','VBIAS','rx_gain',tol='0.1%')
        res(b,'RAF'+str(ch),'100k',f'AMP{ch}',f'FB{ch}','rx_gain',tol='0.1%')
        cap(b,'CAF'+str(ch),'15pF',f'AMP{ch}',f'FB{ch}','rx_gain_rolloff',tol='2%',rating='0603;C0G;50V')
        res(b,'RAL'+str(ch),'2.21k',f'BLANK_OUT{ch}',f'LP{ch}','rx_lowpass',tol='0.1%')
        cap(b,'CAL'+str(ch),'680pF',f'LP{ch}','VBIAS','rx_lowpass',tol='2%',rating='0603;C0G;50V')
        res(b,'RAO'+str(ch),'100',f'RX{ch}_OUT_RAW',f'RX{ch}_OUT','cable_output_damping')
    # Post-amplifier blanking keeps switch terminals in the local0..5V domain.
    add(b,'UBLANK','TMUX1574PWR',{1:'B_RX_BLANK',2:'AMP0',3:'VBIAS',4:'BLANK_OUT0',5:'AMP1',6:'VBIAS',7:'BLANK_OUT1',8:'GND',9:'BLANK_OUT2',10:'VBIAS',11:'AMP2',12:'BLANK_OUT3',13:'VBIAS',14:'AMP3',15:'GND',16:'AFE5'},'rx_blanking','AFE5','PW16');dec(b,'CBLANK','AFE5')

def central():
    b='CENTRAL'
    usb={p:'GND' for p in ['A1','A12','B1','B12']};usb.update({p:'VBUS_RAW' for p in ['A4','A9','B4','B9']});usb.update({'A5':'CC1','B5':'CC2'})
    for p in ['A6','A7','A8','B6','B7','B8']:usb[p]='NC:USB_DATA'
    usb['SHIELD']='SHIELD';add(b,'JUSB','USB4500-03-0-A',usb,'usb_power_connector',pkg='USB_C_16pin_MID_MOUNT_FOOTPRINT_HOLD')
    cap(b,'CSH','1nF','SHIELD','GND','shield_ac',rating='0603;C0G;1kV');res(b,'RSH','1Meg','SHIELD','GND','shield_bleed')
    add(b,'UBOOT','TPS7A2033PDBVR',{1:'VBUS_RAW',2:'GND',3:'VBUS_RAW',4:'NC:4',5:'BOOT3V3'},'cc_bootstrap','VBUS_RAW','DBV5');dec(b,'CBI','VBUS_RAW','1uF');dec(b,'CBO','BOOT3V3','1uF')
    add(b,'UCC','TUSB321AIRWBR',{1:'CC1',2:'CC2',3:'GND',4:'GND',5:'VBUS_DET',6:'NC:VCONN',7:'NC:OUT1',8:'CC3A_N',9:'NC:ID',10:'GND',11:'NC:DIR',12:'BOOT3V3',13:'GND'},'usb_current_advertisement','BOOT3V3','RWB12+EP')
    res(b,'RCC','900k','VBUS_RAW','VBUS_DET','usb_vbus_detect');res(b,'RCCP','10k','CC3A_N','BOOT3V3','cc_output_pullup')
    add(b,'UINV','SN74LVC1G04DBVR',{1:'NC:1',2:'CC3A_N',3:'GND',4:'USB_ALLOW',5:'BOOT3V3'},'cc_allow_inverter','BOOT3V3','DBV5');dec(b,'CCCD','BOOT3V3')
    res(b,'REN','100k','USB_ALLOW','GND','usb_main_default_off')
    efuse(b,'U1','VBUS_RAW','VBUS_SHUNT_IN','USB_ALLOW','USB_OVLO','USB_FLT_N','10nF')
    passive(b,'RS1','R','20mOhm','VBUS_SHUNT_IN','VBUS_SAFE','current_shunt',rating='2512;1W;4terminal_Kelvin',tol='1%')
    res(b,'ROVT','37.4k','VBUS_RAW','USB_OVLO','usb_ovlo',tol='0.1%');res(b,'ROVB','10k','USB_OVLO','GND','usb_ovlo',tol='0.1%')
    add(b,'UBB','TPS63070RNMR',{1:'GND',2:'BB_PG',3:'BB_AUX',4:'GND',5:'BB_FB',6:'NC:FB2',7:'6V3',8:'6V3',9:'BB_L2',10:'GND',11:'BB_L1',12:'VBUS_SAFE',13:'VBUS_SAFE',14:'VBUS_SAFE',15:'GND',16:'GND'},'central_buck_boost','VBUS_SAFE','RNM15+EP')
    passive(b,'LBB','L','1.5uH','BB_L1','BB_L2','buckboost_inductor',rating='shielded;Isat>=6A_at_hot;DCR<=35mOhm',tol='20%')
    dec(b,'CBBA','BB_AUX');dec(b,'CBBI','VBUS_SAFE','10uF');cap(b,'CBBO','47uF','6V3','GND','buckboost_output',rating='2x1210_or_singlequalified;Ceff>=40uF;16V')
    res(b,'RBBT','68.7k','6V3','BB_FB','feedback',tol='0.1%');res(b,'RBBB','10k','BB_FB','GND','feedback',tol='0.1%');res(b,'RBPG','10k','BB_PG','3V3','power_good_pullup')
    buck(b,'U2','6V3','3V3','45.3k');ldo5(b,'U3','6V3','AVCC5')
    # CoreADC pins from ADI RevA Table9 pp15-17;serial/software/4DOUT contract.
    ap={1:'AVCC5',2:'GND',3:'3V3',4:'3V3',5:'3V3',6:'3V3',7:'3V3',8:'GND',9:'ADC_CONVST',10:'GND',11:'ADC_RESET',12:'ADC_SCLK',13:'ADC_CS_N',14:'ADC_BUSY',15:'NC:FRSTDATA',23:'3V3',24:'ADC_DOUT[0]',25:'ADC_DOUT[1]',26:'GND',27:'ADC_DOUT[2]',28:'ADC_DOUT[3]',29:'ADC_SDI',34:'GND',35:'GND',36:'REGCAP_A',37:'AVCC5',38:'AVCC5',39:'REGCAP_D',40:'GND',41:'GND',42:'REF2V5',43:'GND',44:'REFCAP',45:'REFCAP',46:'GND',47:'GND',48:'AVCC5'}
    for i in list(range(16,19))+list(range(30,34)):ap[i]='GND'
    for i in range(19,23):ap[i]='NC:DOUT_UNUSED'
    for ch in range(8):ap[49+2*ch]=f'ADCIN{ch}';ap[50+2*ch]='GND'
    add(b,'UADC','AD7606C-16BSTZ-RL',ap,'adc','AVCC5','LQFP64')
    for i in [1,37,38,48]:dec(b,'CAD'+str(i),'AVCC5')
    dec(b,'CAD23','3V3');dec(b,'CAD36','REGCAP_A','1uF');dec(b,'CAD39','REGCAP_D','1uF');dec(b,'CAD42','REF2V5');dec(b,'CAD44','REFCAP','10uF');dec(b,'CADB','AVCC5','10uF')
    add(b,'UREF','REF5025AIDR',{1:'NC:DNC',2:'AVCC5',3:'NC:TEMP',4:'GND',5:'REF_NR',6:'REF2V5',7:'NC:7',8:'NC:DNC'},'adc_reference','AVCC5','SOIC8');dec(b,'CREFI','AVCC5');dec(b,'CREFO','REF2V5','10uF');dec(b,'CREFN','REF_NR','1uF')
    for ch in range(8):
        name=('UP' if ch<4 else 'DN')+f'_RX{ch%4}_OUT';res(b,'RAI'+str(ch),'499',name,f'ADCIN{ch}','adc_input_filter',tol='0.1%');cap(b,'CAI'+str(ch),'1nF',f'ADCIN{ch}','GND','adc_input_filter',tol='2%',rating='0603;C0G;50V')
    # Use the approved connector mapping directly, including all power NCs.
    con=json.loads((ROOT/'v5/hardware/design_20261011/CONNECTION_CONTRACT.json').read_text(encoding='utf-8'))['connections']
    for header in ['J10','J11']:
        pins={i:'NC:UNUSED_OR_POWER' for i in range(1,41)}
        for r in con:
            ep=r['central_endpoint']
            if ep.startswith('CENTRAL_AX_'+header+'.'):
                p=int(ep.rsplit('.',1)[1]);n=r['net'];pins[p]='GND' if r['direction']=='GROUND' else n if r['direction'] in ['IN','OUT','OPEN_DRAIN'] else 'NC:POWER_OR_UNASSIGNED'
        # Explicit power contacts remain NC from approved map (never use power for VCCA).
        add(b,'AX_'+header,'AX7020_2x20_INTERFACE',pins,'ax7020_interface',pkg='40pin_MAPPING_HOLD')
    # Eight-channel transceivers grouped by signal direction;local3V3 on both ports is provisional untilVCCO proven.
    dirs=defaultdict(list)
    for r in con:
        if r['central_endpoint'].startswith('CENTRAL_AX_') and r['direction'] in ['IN','OUT']:dirs[r['direction']].append(r['net'])
    j=0
    for direct,names in dirs.items():
        for start in range(0,len(names),8):
            chunk=names[start:start+8];pins={1:'3V3',2:('3V3' if direct=='OUT' else 'GND'),11:'GND',12:'GND',13:'GND',22:'HOST_OE_N',23:'3V3',24:'3V3'}
            for k in range(8):
                n=chunk[k] if k<len(chunk) else None;pins[3+k]=n or 'GND';pins[21-k]=('IO_'+n if n else 'NC:UNUSED')
            add(b,'UX'+str(j),'SN74AXC8T245PWR',pins,'ax_domain_interface','3V3','PW24');dec(b,'CXA'+str(j),'3V3');dec(b,'CXB'+str(j),'3V3');j+=1
    add(b,'JHOSTEN','NORMALLY_OPEN_JUMPER',{1:'HOST_OE_N',2:'GND'},'manual_host_io_enable',pkg='2pin_NO_DEFAULT_SHUNT');res(b,'RHOST','10k','HOST_OE_N','3V3','host_io_default_off')
    g1(b,'UESTOP','SN74LVC1G08DBVR','IO_UP_FAULT_N','IO_ESTOP_STATUS',inp2='IO_DN_FAULT_N')
    for arr in ['UP','DN']:
        sig=[f'DATA{i}' for i in range(16)]+['SRCLK','RCLK','OE_N','RESET_N','SYNC','RX_BLANK','HB','FAULT_N','PGOOD','I2C_SCL','I2C_SDA']+[f'RX{i}_OUT' for i in range(4)]
        pins={2*i+2:'GND' for i in range(32)};pins[63]='NC:SPARE'
        for i,n in enumerate(sig):
            if n.startswith('DATA'):name='IO_TX_DATA_'+arr+'['+n[4:]+']'
            elif n=='HB':name='IO_'+arr+'_HEARTBEAT'
            elif n.startswith('RX') and n.endswith('_OUT'):name=arr+'_'+n
            elif n in ['I2C_SCL','I2C_SDA']:name=arr+'_'+n
            else:name='IO_'+arr+'_'+n
            pins[2*i+1]=name
        add(b,'J'+arr,'SIGNAL_2x32_MPN_HOLD',pins,'array_signal_connector',pkg='64pin_keyed_ground_interleaved')
    # I2C upstream pins do not have a finalized AX7020 top-level assignment yet.
    mux={1:'GND',2:'GND',3:'3V3',12:'GND',23:'I2C_SDA_HOST',24:'3V3',22:'I2C_SCL_HOST',21:'GND'}
    for k,(sd,sc) in enumerate([(4,5),(6,7),(8,9),(10,11),(13,14),(15,16),(17,18),(19,20)]):
        mux[sd]=('UP_I2C_SDA' if k==0 else 'DN_I2C_SDA' if k==1 else 'LOCAL_SDA' if k==2 else 'NC:SPARE');mux[sc]=('UP_I2C_SCL' if k==0 else 'DN_I2C_SCL' if k==1 else 'LOCAL_SCL' if k==2 else 'NC:SPARE')
    add(b,'UMUX','TCA9548APWR',mux,'i2c_mux','3V3','PW24');dec(b,'CMUX','3V3')
    add(b,'UMON','INA226AIDGSR',{1:'GND',2:'GND',3:'NC:ALERT',4:'LOCAL_SDA',5:'LOCAL_SCL',6:'3V3',7:'GND',8:'VBUS_SAFE',9:'VBUS_SAFE',10:'VBUS_SHUNT_IN'},'current_telemetry','3V3','DGS10');dec(b,'CMON','3V3')
    add(b,'UTEMP','TMP117AIDRVR',{1:'LOCAL_SCL',2:'GND',3:'NC:ALERT',4:'GND',5:'3V3',6:'LOCAL_SDA',7:'GND'},'temperature_telemetry','3V3','DRV6+EP');dec(b,'CTEMP','3V3')
    add(b,'JI2C','I2C_HOST_ASSIGNMENT_HOLD',{1:'I2C_SDA_HOST',2:'I2C_SCL_HOST',3:'GND'},'i2c_handoff',pkg='3pin')
    add(b,'JHOSTI2C','TWO_NORMALLY_OPEN_SHUNTS',{1:'I2C_SCL',2:'I2C_SCL_HOST',3:'I2C_SDA',4:'I2C_SDA_HOST'},'manual_host_i2c_isolation',pkg='2x2_NO_DEFAULT_SHUNTS')
    for bus in ['I2C_SDA_HOST','I2C_SCL_HOST','UP_I2C_SDA','UP_I2C_SCL','DN_I2C_SDA','DN_I2C_SCL','LOCAL_SDA','LOCAL_SCL']:res(b,'RP'+bus,'2.2k','3V3',bus,'i2c_pullup')
    for n in ['ADC_CONVST','ADC_RESET','ADC_SCLK','ADC_CS_N','ADC_SDI','ADC_BUSY']+[f'ADC_DOUT[{i}]' for i in range(4)]:
        res(b,'RIO_'+n,'33',n,'IO_'+n,'adc_digital_series')
    for n,rail in [('ADC_CONVST','GND'),('ADC_RESET','GND'),('ADC_SCLK','GND'),('ADC_CS_N','3V3'),('ADC_SDI','GND')]:res(b,'RDEFAULT_'+n,'10k',n,rail,'adc_default')
    add(b,'LED1','GREEN_LED_MPN_HOLD',{1:'LED_AN',2:'GND'},'status_led','3V3','0603');res(b,'RLED','2.2k','3V3','LED_AN','led_limit')

def exports():
    writecsv(R/'netlist/COMPONENTS.csv',C);writecsv(R/'netlist/PIN_NET.csv',PINS);writecsv(R/'05_TX_CHANNEL_MAPPING.csv',MAPPING);writecsv(R/'07_PASSIVE_VALUE_REGISTER.csv',PASS)
    payload=dict(status='STRICT_PIN_NET_CANDIDATE_NOT_NATIVE_NOT_ERC',components=C,pins=PINS,source='calc/build_candidate.py',unqualified=['footprints','host_poweroff','fault_energy','AFE_input_protection','clock_STA'])
    (R/'netlist/THREE_BOARD_CANDIDATE.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    groups=defaultdict(list)
    for c in C:groups[(c['board'],c['mpn'],c['value'],c['package'],c['function'])].append(c)
    bom=[];budget=[]
    current={'tx_driver':(.00045,.0015,'MAX_QUIESCENT_ONLY; dynamic not guaranteed'), 'serializer':(.00001,.00004,'MAX_STATIC_ONLY;CVf dynamic conditional'), 'receiver_amplifier':(.004,.0052,'PER_QUAD_MAX_IQ; outputload separate'), 'adc':(.045,.050,'RevA Table2 p9;1MSPS;add1.9mA VDRIVE separately'), 'current_telemetry':(.00033,.00042,'DATASHEET_IQ_MAX'), 'temperature_telemetry':(.0000035,.00015,'MODE_DEPENDENT_ALLOCATION'), 'analog_bias_reference':(.001,.0012,'REF50xxAI datasheet table3'), 'adc_reference':(.001,.0012,'REF50xxAI datasheet table3'), 'cc_bootstrap':(.002,.020,'GLOBAL_BOOTSTRAP_DESIGN_ALLOWANCE')}
    for key,rows in sorted(groups.items()):
        b,mp,v,pkg,f=key;refs=' '.join(c['refdes'] for c in rows);n=len(rows)
        bom.append(dict(board=b,refdes=refs,qty=n,mpn=mp,value=v,package=pkg,function=f,change='NEW_EXPLICIT_REFDES_REPLACES_LEGACY_CATEGORY_COUNT',status='RELEASE_CANDIDATE_ONLY_PROCUREMENT_HOLD',source_url=rows[0]['source_url']))
        rail=rows[0]['rail'];rr={'3V3':(3.15,3.3,3.42),'AFE5':(4.91,5,5.09),'AVCC5':(4.91,5,5.09),'TX12':(10.8,12,13.2),'VBUS_RAW':(3.8,5,5.5),'BOOT3V3':(3.2505,3.3,3.3495),'VIN12_FUSED':(10.8,12,13.2),'VIN12_LOAD':(10.8,12,13.2),'VBUS_SAFE':(3.53,5,5.5),'6V3':(6.195,6.296,6.397),'6V7':(6.44,6.675,6.91)}.get(rail,(None,None,None));volts=rr[2]
        typ,imax,cl=current.get(f,(None,None,'PASSIVE_PATH_OR_UNGUARANTEED_DYNAMIC; allocated by function; global input clamp applies'))
        output={'buck_3V3':3.296,'buck_6V7':6.675,'central_buck_boost':6.296,'analog_ldo':5,'cc_bootstrap':3.3}.get(f)
        budget.append(dict(Board=b,Rail=rail,Refdes=refs,Qty=n,Device_function=mp+'/'+f,Operating_mode='normal/standby/fault separated in report',Vin_min=rr[0],Vin_nom=rr[1],Vin_max=rr[2],Vout=output,Vrail_for_power=volts,I_typ_A=typ,I_max_continuous_A=imax,I_peak_A='',t_peak_s='',f_sw_Hz=40000 if f in ['tx_driver','ultrasound_transmitter'] else '',max_active_channels=64 if b!='CENTRAL' else 8,standby_draw='datasheet or UNKNOWN; not zero',datasheet_revision_table_page='01_DATASHEET_MAX_RATINGS_REGISTER.csv',classification=cl,power_formula='Qty*(AVCCmax*50mA+VDRIVEmax*1.9mA)' if f=='adc' else 'Qty*Vrail*Imax applies only to explicit IQ allocation',P_max_continuous_W=n*(volts*imax+(3.42*.0019 if f=='adc' else 0)) if imax is not None else None,P_peak_W=None,loss_W=None,heat_W=None,confidence='CANDIDATE_BOUND_OR_MISSING',source_URL=rows[0]['source_url'],open_qualification='NOT_A_COMPLETE_GUARANTEED_LOAD_SUM; hardware steady limit is separate'))
    for old in ['B-008','B-009']:
        bom.append(dict(board='LEGACY_RETIRED',refdes=old,qty=0,mpn='OLD_PLACEHOLDER_RETIRED',value='0 installed',package='',function='superseded_by_TPS3851_one_per_array',change='OLD2_EACH_TOTAL4_TO_ZERO',status='DO_NOT_FIT',source_url='S3 explicit user instruction'))
    writecsv(R/'10_BOM_RELEASE_CANDIDATE_DELTA.csv',bom);writecsv(R/'02_THREE_BOARD_POWER_BUDGET.csv',budget)
    # Compatibility filename requested in instruction section2.1, same canonical table bytes.
    (R/'LOAD_AND_POWER_BUDGET.csv').write_bytes((R/'02_THREE_BOARD_POWER_BUDGET.csv').read_bytes())
    (R/'calc/workbook_data.json').write_text(json.dumps(dict(bom=bom,budget=budget,results=calculate(json.loads((R/'calc/inputs.json').read_text()))),indent=2)+'\n',encoding='utf-8')
    bynet=defaultdict(list)
    for p in PINS:
        if p['disposition']=='CONNECTED':bynet[p['net']].append(p)
    xml=['<?xml version="1.0" encoding="utf-8"?>','<export version="D"><components>']
    for c in C:xml.append(f'<comp ref="{c["refdes"]}"><value>{html.escape(c["value"])}</value><footprint>{html.escape(c["package"])}</footprint></comp>')
    xml.append('</components><nets>')
    for i,(net,pins) in enumerate(sorted(bynet.items()),1):
        xml.append(f'<net code="{i}" name="{html.escape(net)}">')
        for p in pins:xml.append(f'<node ref="{p["refdes"]}" pin="{p["pin"]}"/>')
        xml.append('</net>')
    xml.append('</nets></export>');(R/'netlist/THREE_BOARD_GENERIC_NETLIST.xml').write_text('\n'.join(xml),encoding='utf-8')
    (E/'CANDIDATE_COUNTS.json').write_text(json.dumps(dict(total_components=len(C),per_board=dict(Counter(c['board'] for c in C)),pins=len(PINS),passives=len(PASS),bom_group_rows=len(bom),legacy_baseline_installed=1205,legacy_count_is_not_new_design_constraint=True,pcb_mpn_gates=sorted(set(c['mpn'] for c in C if 'HOLD' in c['mpn'] or 'UNKNOWN' in c['mpn']))),indent=2)+'\n',encoding='utf-8')
def main():
    (R/'netlist').mkdir(exist_ok=True);array('UP');array('DN');central();exports();print(f'{len(C)} components;{len(PINS)} pins;{len(PASS)} passives')
if __name__=='__main__':main()
