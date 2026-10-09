"""Candidate power/monitor/interface capture. Qualification and safety gates remain open."""
import json
from system_design import Sheet
from tx_design import OUT


def build():
    sheets=[]
    def page(name,notes):
        s=Sheet(name,notes);sheets.append(s);return s
    for b in ['U','L','A']:
        pg,dg,ag=[f'{x}GND_{b}' for x in ['P','D','A']]
        vin,protected,rail=f'VIN_{b}',f'FUSED_{b}',f'VDRV_{b}'
        v=f'3V3_{b}'
        s=page(f'POWER_INPUT_{b}',[
            'Independent external 12 V input; 12-15 V characterization only. Never apply 18 V as normal setpoint.',
            'TPS259470L latch-off candidate; nominal UV=9.2 V, OV=16.8 V, current limit=2.02 A.',
            'Values/ratings are design candidates. Fault signal is NOT a complete independent watchdog.',
            'Input connector, fuse/TVS and cable selection remain OPEN; TP endpoints are NOT connector pin assignments.'])
        s.part('TPS259470LRPWR',f'U_EFUSE_{b}',430,530,
               {1:f'UV_{b}',2:f'OV_{b}',3:None,4:f'FAULT_N_{b}',5:vin,6:protected,
                7:f'DVDT_{b}',8:pg,9:f'ILM_{b}',10:f'ITIMER_{b}'})
        s.part('TP',f'TP_INPUT_{b}',120,670,{1:vin},'EXTERNAL_INPUT',True)
        s.part('TP',f'TP_RETURN_{b}',120,570,{1:pg},'EXTERNAL_RETURN',True)
        for i,(value,a,z) in enumerate([('100k 1%',vin,f'UV_{b}'),('15k 1%',f'UV_{b}',pg),
                ('130k 1%',vin,f'OV_{b}'),('10k 1%',f'OV_{b}',pg),('1.65k 1%',f'ILM_{b}',pg),
                ('10k',v,f'FAULT_N_{b}')]):
            s.passive('R',f'R_EFUSE_{b}{i}',value,200+350*(i%3),330-100*(i//3),a,z)
        s.cap(f'C_DVDT_{b}',870,620,f'DVDT_{b}',pg,'3.3nF 50V')
        s.cap(f'C_ITIMER_{b}',870,520,f'ITIMER_{b}',pg,'2.2nF')
        s.cap(f'C_INPUT_{b}',150,440,vin,pg,'10uF 35V')
        s.passive('R',f'R_SHUNT_{b}','20mR 2W KELVIN',520,120,protected,rail)
        s=page(f'POWER_MONITOR_{b}',[
            'Local I2C bus at local 3.3 V; host connection/level compatibility TBD.',
            'INA226 address0x40, TMP117 address0x48 on EACH SEPARATE bus.',
            'Kelvin shunt sense; signed current, alert limits and calibration must be configured/tested.'])
        s.part('INA226AIDGSR',f'U_CURRENT_{b}',270,530,{1:dg,2:dg,3:f'CURRENT_ALERT_N_{b}',
            4:f'I2C_{b}_SDA',5:f'I2C_{b}_SCL',6:v,7:dg,8:rail,9:rail,10:protected})
        s.part('TMP117MAIDRVR',f'U_TEMP_{b}',800,530,{1:f'I2C_{b}_SCL',2:dg,3:f'TEMP_ALERT_N_{b}',
            4:dg,5:v,6:f'I2C_{b}_SDA',7:dg})
        s.cap(f'C_CURRENT_{b}',220,690,v,dg);s.cap(f'C_TEMP_{b}',800,690,v,dg)
        for i,net in enumerate([f'I2C_{b}_SDA',f'I2C_{b}_SCL',f'CURRENT_ALERT_N_{b}',f'TEMP_ALERT_N_{b}']):
            s.passive('R',f'R_MON_PULL_{b}{i}','4.7k',220+530*(i%2),320-120*(i//2),v,net)
        for suffix,chip,target in [('D','AP63203WU-7',v),('P','AP63200WU-7',f'5V5_{b}')]:
            tag=b+suffix;sw=f'SW_{tag}';bst=f'BST_{tag}';fb=target if suffix=='D' else f'FB_{tag}'
            s=page(f'POWER_BUCK_{tag}',[
                'AP63203 fixed3.3 V / AP63200 adjustable5.52 V; 6.8uH is unqualified BOM candidate.',
                'Inductor Isat/DCR, ceramic DC bias, ripple/stability and startup must be checked.',
                'Input and switching currents return to local PGND; no layout created.'])
            s.part(chip,f'U_BUCK_{tag}',430,530,{1:fb,2:rail,3:rail,4:pg,5:sw,6:bst})
            s.passive('L',f'L_BUCK_{tag}','6.8uH ISAT_TBD',810,520,sw,target)
            s.cap(f'C_BUCK_IN_{tag}',180,660,rail,pg,'10uF 35V')
            s.passive('C',f'C_BOOT_{tag}','100nF',650,680,bst,sw)
            s.cap(f'C_BUCK_O1_{tag}',380,290,target,pg,'22uF 16V')
            s.cap(f'C_BUCK_O2_{tag}',820,290,target,pg,'22uF 16V')
            if suffix=='P':
                s.passive('R',f'R_FB_TOP_{tag}','590k 1%',270,160,target,fb)
                s.passive('R',f'R_FB_BOTTOM_{tag}','100k 1%',800,160,fb,pg)
        s=page(f'POWER_ANALOG_{b}',[
            'Fixed5.0 V ADP7118: SENSE to output, SS open; EP to AGND.',
            'Ferrite before LDO; effective capacitor >=2.2uF over DC bias/temp. 200mA LDO limit.',
            'Ground links express intended common reference; physical return-path review remains mandatory.'])
        filt=f'LDO_IN_{b}';out=f'5VA_{b}'
        s.part('BLM21PG221SN1D',f'FB_ANALOG_{b}',200,610,{1:f'5V5_{b}',2:filt})
        s.part('ADP7118ACPZN5.0-R7',f'U_LDO_{b}',650,550,{1:out,2:out,3:ag,4:filt,5:None,6:filt,7:ag})
        s.cap(f'C_LDO_IN_{b}',200,400,filt,ag,'4.7uF 16V')
        s.cap(f'C_LDO_OUT_{b}',840,400,out,ag,'4.7uF 16V')
        s.passive('R',f'R_GROUND_D_{b}','0R RETURN_LINK',250,230,dg,pg)
        s.passive('R',f'R_GROUND_A_{b}','0R RETURN_LINK',750,230,ag,pg)
    s=page('SYSTEM_REFERENCE_AND_ENVIRONMENT',[
        'System reference joins local returns. Cable return topology NOT frozen.',
        'SHT45 remote ambient measurement; keep away from drivers. Dedicated 3.3 V I2C bus.',
        'Do not connect unknown PS/PL voltage domains directly to these monitor buses.'])
    for i,b in enumerate(['U','L','A']):
        s.passive('R',f'R_SYSTEM_GND_{b}','0R STAR_INTENT',220+350*i,600,f'PGND_{b}','SYSTEM_GND')
    s.part('SHT45-AD1B-R2','U_ENV',400,350,{1:'I2C_ENV_SDA',2:'I2C_ENV_SCL',3:'3V3_A',4:'DGND_A',5:None})
    s.cap('C_ENV',180,470,'3V3_A','DGND_A')
    for i,net in enumerate(['I2C_ENV_SDA','I2C_ENV_SCL']):
        s.passive('R',f'R_ENV_PULL{i}','4.7k',850,410-120*i,'3V3_A',net)
    signals=[f'serial_data[{i}]' for i in range(32)]+['shift_clock','latch_clock','output_disable',
        'adc_reset','adc_convst','adc_cs_n','adc_sclk','adc_sdi','adc_busy']+[f'adc_dout[{i}]' for i in range(4)]+[
        'rx_blank[0]','rx_blank[1]','hardware_enable','rst_n','LEVEL_OE_N','VCCO_FPGA','SYSTEM_GND']
    for group in range((len(signals)+15)//16):
        s=page(f'FPGA_CORE_INTERFACE_{group}',[
            'LOGICAL INTERFACE ONLY: every physical FPGA/connector pin and VCCO remains TBD (B01/B03).',
            'TP symbols identify logical endpoints; they are NOT a proposed core-board pinout.',
            'Native net labels use UPPERCASE; explicit case-sensitive RTL mapping is in channel-map report.',
            'hardware_enable/rst_n policy and independent KILL/watchdog remain OPEN.'])
        for i,signal in enumerate(signals[group*16:(group+1)*16]):
            s.part('TP',f'TP_CORE_{group*16+i:02d}',180+270*(i%4),600-140*(i//4),{1:signal},signal+' / PIN_TBD',True)
    return {'status':'DRAFT_NOT_FOR_FABRICATION','sheets':[s.record() for s in sheets],
            'rtl_to_native_net':{x:x.upper() for x in signals},'physical_pin_assignment':'BLOCKED_B01_B03'}


if __name__=='__main__':
    design=build();refs=[p['ref'] for s in design['sheets'] for p in s['parts']]
    assert len(refs)==len(set(refs))
    (OUT/'project/power_design.json').write_text(json.dumps(design,indent=2)+'\n',encoding='utf-8')
    print(len(design['sheets']),'power/interface sheets;',len(refs),'components')
