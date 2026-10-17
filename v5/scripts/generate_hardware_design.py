"""Generate review-only v5 hardware assets from the reviewed manual facts.

No vendor executable, hardware API, frozen archive or old sandbox is accessed.
The exact active signal contract is updated only with --adopt. A different
--output writes an independent reproduction without altering current files.
"""
from pathlib import Path
import argparse,copy,csv,itertools,json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from software.board.hardware_design import capacitive_power,source_limit,array_power,usb_avcc,i2c_pullup_bounds,adc_serial_budget


def save(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')


def csv_save(path,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)


def mapping():
    rows=json.loads((ROOT/'hardware/design_20261011/MANUAL_PIN_ROWS.json').read_text())
    for r in rows:
        h,p=r['connector'],r['pin'];side='UP' if h=='J10' else 'DN'
        port=None;binding='MISSING_BOARD_WRAPPER';direction='OUT';safe='LOW'
        if p in (1,37,38):net='SIGNAL_GND';direction='GROUND';binding='CONTROLLED_REFERENCE_RETURN';safe='GROUND'
        elif p in (2,39,40):net='NC_AX7020_'+('5V' if p==2 else '3V3');direction='NC_POWER';binding='NO_CONNECT';safe='ISOLATED'
        elif 3<=p<=18:
            net=f'TX_DATA_{side}[{p-3}]';port=f'serial_data[{p-3+(0 if h=="J10" else 16)}]';binding='DIRECT_LOGICAL_PORT'
        elif 19<=p<=27:
            suffix=['SRCLK','RCLK','OE_N','RESET_N','SYNC','RX_BLANK','HEARTBEAT','PGOOD','FAULT_N'][p-19]
            net=f'{side}_{suffix}'
            port={'SRCLK':'shift_clock','RCLK':'latch_clock','OE_N':'output_disable','RX_BLANK':f'rx_blank[{0 if side=="UP" else 1}]','HEARTBEAT':'heartbeat','PGOOD':f'health[{1 if side=="UP" else 2}]'}.get(suffix)
            if suffix in ('PGOOD','FAULT_N'):direction='IN';safe='LOW_FAULT'
            if suffix in ('SRCLK','RCLK','HEARTBEAT'):binding='SHARED_PORT_FANOUT_BUFFER_REQUIRED'
            elif suffix=='OE_N':binding='SAME_LEVEL_ACTIVE_HIGH_DISABLE_NO_INVERSION';safe='HIGH_DISABLE'
            elif suffix=='PGOOD':binding='DIRECT_LOGICAL_PORT'
            elif suffix=='RX_BLANK':binding='DIRECT_LOGICAL_PORT';safe='HIGH_BLANK'
            elif suffix in ('RESET_N','SYNC'):binding='NOT_EXPOSED_BY_CURRENT_TOP_REVIEW_REQUIRED';safe='LOW'
            elif suffix=='FAULT_N':binding='HARDWARE_FAULT_AGGREGATION_TO_HEALTH_REQUIRED'
        elif h=='J10' and 28<=p<=31:
            net=f'ADC_DOUT[{p-28}]';direction='IN';port=f'adc_dout[{p-28}]';binding='DIRECT_LOGICAL_PORT'
        elif h=='J10':
            net=['ADC_BUSY','ADC_SCLK','ADC_CONVST','ADC_CS_N','ADC_SDI'][p-32]
            port=net.lower();binding='DIRECT_LOGICAL_PORT';direction='IN' if p==32 else 'OUT';safe='HIGH' if p==35 else 'LOW'
        elif p==28:net='ADC_RESET';port='adc_reset';binding='ACTIVE_HIGH_RESET';safe='HIGH_RESET'
        elif p in (29,30):net='I2C_'+('SCL' if p==29 else 'SDA');direction='OPEN_DRAIN';binding='NEW_MUX_CONTROLLER_NOT_CONNECTED_TO_CURRENT_TOP';safe='HIGH_Z'
        elif p==31:net='ESTOP_STATUS';port='health[0]';direction='IN';binding='DIRECT_LOGICAL_PORT_NOT_SAFETY_CUTOFF';safe='LOW_FAULT'
        else:net=f'SPARE[{p-32}]';direction='HIGH_Z';binding='UNCONNECTED';safe='HIGH_Z'
        r.update(net=net,direction=direction,rtl_port=port or '',binding=binding,safe_level=safe,
                 vcco='NOT_MEASURED_DEFAULT_3V3_MANUAL' if r['bank'] else 'N_A',
                 io_standard='LVCMOS33_REVIEW_ONLY' if r['bank'] else 'N_A',
                 harness=f'CENTRAL_{h}.{p}',deployment='HOLD')
    return rows


def build(output,adopt=False):
    rows=mapping();save(output/'SIGNAL_CONTRACT.json',dict(active_version='v5',status='NON_DEPLOYABLE',pins=rows,
        used_gpio=63,spare_gpio=5,power='CENTRAL_USB_C_ONLY_HEADER_POWER_NC',
        reset_correction='AD7606C-16 RESET is active high; ADC_RESET_N in incoming table corrected',
        rtl_integration='PARTIAL_CURRENT_TOP_BINDINGS_EXPLICIT_NO_63_IO_WRAPPER_CLAIM',
        mux=dict(part='TCA9548APWR',address='0x70',channels={'0':'CENTRAL','1':'UPPER','2':'LOWER'},frequency_hz=100000,
                 reset='INDEPENDENT_LOCAL_RESET_REQUIRED_NOT_ALLOCATED_TO_63_GPIO',
                 fault='ONE_HOT_ONLY; select NONE before switch; timeout requires hardware RESET'),
        geometry=dict(tx_pitch_mm=12,tx_axis_mm=[-42,-30,-18,-6,6,18,30,42],rx_corners_mm=[[-54,-54],[-54,54],[54,-54],[54,54]],
                      face_gap_mm=100,face_gap_range_mm=[90,115],target='EPS_DIAMETER_2_TO_5_MM_NOT_VERIFIED')))
    csv_save(output/'IO_PINMAP.csv',rows)
    if adopt:
        save(ROOT/'config/SIGNAL_CONTRACT.json',json.loads((output/'SIGNAL_CONTRACT.json').read_text()))
        for filename in ('AX7020_REV3_68GPIO_AUDIT.csv','AX7020_REV3_PROPOSED_PINMAP.csv'):
            csv_save(ROOT/'hardware/ax7020'/filename,rows)
    # Clock/IO review file must stop before executing any pin assignments.
    xdc='error {REVIEW_ONLY: no deployment, measured VCCO or external delay qualification}\n'
    for r in rows:
        if r['bank'] and r['direction']!='HIGH_Z':
            xdc+=f'# {r["connector"]}.{r["pin"]} Bank{r["bank"]}: set_property PACKAGE_PIN {r["package_pin"]} [get_ports {{{r["net"]}}}]\n'
    (output/'ax7020_design_review_only.xdc').write_text(xdc,encoding='utf-8',newline='\n')
    if adopt:(ROOT/'hardware/constraints/ax7020_design_review_only.xdc').write_text(xdc,encoding='utf-8',newline='\n')
    budgets=[]
    for rated in (40.,60.,15.):
        for margin in (.2,.3):
            for derating in (1.,.8):
                budgets.append(dict(source='CENTRAL_USB_5V3A' if rated==15 else f'ARRAY_12V_{rated:g}W',rated_w=rated,
                    headroom=margin,derating_assumption=derating,allowed_w=source_limit(rated,margin,derating),
                    total_w=None,motional_w=None,status='HOLD_MISSING_CONTINUOUS_LOAD_AND_TEMPERATURE_DERATING'))
    csv_save(output/'POWER_BUDGET.csv',budgets)
    sweep=[dict(C_nf=c,V=v,f_hz=f,active=active,capacitive_w=capacitive_power(c,v,f,64,active))
           for c,v,f,active in itertools.product((1.76,2.2,2.64),(10.8,12.,13.2),(39000.,40000.,41000.),(.25,.5,1.))]
    save(output/'POWER_BUDGET.json',dict(budgets=budgets,sensitivity=sweep,array_unknown=array_power(),
        connector_5a_loss_w_at_30mohm=5**2*.03,efuse_5a_nominal_loss_w=5**2*.031,
        limits='Loss estimates, not thermal proof; PJ5A and eFuse pulse/short coordination HOLD',
        usb_voltage_sweep=[usb_avcc(v,i,r,.05) for v,i,r in itertools.product((4.75,5.,5.25),(.5,1.,2.),(.05,.15))],
        i2c=[dict(capacitance_pf=c,**i2c_pullup_bounds(c)) for c in (100,200,400,800)],
        adc_serial=adc_serial_budget(),uart_raw_stream_bytes_per_second=800000*8*2,
        uart_115200_8n1_payload_ceiling_Bps=11520,
        central_allocations_w={'ADC_AVCC_design_cap':1.0,'ADC_digital_reference_design_cap':.3,'AFE8_design_cap':2.,
                               'buffers_clock_design_cap':1.5,'monitor_safety_design_cap':.5,'conversion_loss_reserve':1.5},
        central_allocations_status='ENGINEERING_ALLOCATION_6P8W_NOT_TYPICAL_OR_WORST_CASE_PROOF'))
    # Preserve all previous component types. Remove superseded power choices
    # explicitly with zero installed count, never silently discard them.
    bom=copy.deepcopy(json.loads((ROOT/'hardware/next_stage/20261010/BOM_INPUTS.json').read_text(encoding='utf-8')))
    bom.update(status='WORKING_20261011_FOUR_SOURCE_POWER_PURCHASE_HOLD',source='hardware/next_stage/20261010/BOM_INPUTS.json')
    old_by_id={x['id']:copy.deepcopy(x) for x in bom['items']}
    for x in bom['items']:
        x.update(qualification='INHERITED_CANDIDATE_REQUIRES_NATIVE_PIN_REVIEW',procurement='HOLD',manufacturer='UNKNOWN_VERIFY',
                 datasheet_revision='UNKNOWN_VERIFY',access_date='2026-10-11',approval_source='User v5 scope; no procurement permission')
        if x['id']=='B-023':x.update(quantities=[0,0,0,0,0],risk='Old SMBJ20A removed from installed candidate; replacement requires clamp/energy proof')
        if x['id']=='B-024':x.update(quantities=[0,0,0,0,0],risk='Old eFuse removed; TPS26631 path below is new candidate')
        if x['id']=='B-014':x.update(mpn='AD7606C-16BSTZ-RL',manufacturer='Analog Devices',datasheet_revision='Rev.A',qualification='DESIGN_SELECTED_DEVICE_DIRECTION_ELECTRICAL_HOLD')
        if x['id']=='B-032':x.update(mpn='TMP117AIDRVR',manufacturer='Texas Instruments',datasheet_revision='Rev.D',qualification='DESIGN_SELECTED_PACKAGE_PIN_REVIEW_HOLD')
        removed={'B-017','B-018','B-020','B-041','B-042','B-044','PC-002','PC-003','PC-004','NS-002','NS-003'}
        if x['id'] in removed:
            x.update(quantities=[0,0,0,0,0],risk='SUPERSEDED_OR_OPTIONAL_DNP: see new H entries; not installed twice')
        if x['id'] in ('B-027','B-028'):
            x.update(mpn='TPS54202DDCR',manufacturer='Texas Instruments',source='https://www.ti.com/lit/ds/symlink/tps54202.pdf',
                     package='SOT23_6_DDC',risk='12V to '+('3.3V digital' if x['id']=='B-027' else '5.5V then existing5V AFE LDO')+'; L/C/thermal/EMI design HOLD')
        if x['id']=='B-039':x.update(mpn='DC5P5x2P5_CENTER_POSITIVE_LEAD_TBD',risk='5A nominal path; wire/fuse/plug length/temperature verification HOLD')
        if x['id']=='B-069':x.update(mpn='200x180mm_COMMON_ARRAY_EXTENSION_CANDIDATE',risk='Electronics outside118.3mm acoustic projection; mechanical/routing/thermal proof HOLD')
        # Prior monitor is central-only 1; retain it and add local monitors below.
    def add(id,mpn,description,quantities,package,source,manufacturer='UNKNOWN_VERIFY',risk='Pin/native library/electrical review required'):
        bom['items'].append(dict(id=id,mpn=mpn,description=description,quantities=quantities,package=package,source=source,
            manufacturer=manufacturer,qualification='CANDIDATE',procurement='HOLD',datasheet_revision='SEE_SOURCE_REGISTER',
            access_date='2026-10-11',approval_source='User hardware design direction, electrical release pending',
            supply='SEE_POWER_DOMAIN_CONTRACT',current_A=None,unit_price=None,currency='CNY',native_footprint='UNVERIFIED',risk=risk))
    add('H-001','STUSB4500LQTR','中央 Type-C 5V Sink',[0,0,1,0,0],'QFN24_EP_VERIFY','https://www.st.com/resource/en/datasheet/stusb4500l.pdf','STMicroelectronics','CC default/1.5A/3A detection and load inhibit required')
    add('H-002','TYPE_C_RECEPTACLE_MPN_TBD','中央 Type-C 电源插座',[0,0,1,0,0],'NATIVE_FOOTPRINT_TBD','CANDIDATE','UNKNOWN_VERIFY')
    add('H-003','PJ-002BH','阵列 DC5.5x2.5 插座',[1,1,0,0,0],'THT3_SWITCH_CONTACT','https://www.sameskydevices.com/product/resource/pj-002bh.pdf','Same Sky','5A nominal/30mohm; switch lug not independent source; temperature derating HOLD')
    add('H-004','TPS26631RGER','阵列 eFuse',[1,1,0,0,0],'VQFN24_RGE_EP','https://www.ti.com/lit/ds/symlink/tps2663.pdf','Texas Instruments','2x pulse support; RILIM/UVLO/OVP/fuse coordination HOLD, not automatic5A setting')
    add('H-005','TCA9548APWR','中央 I2C 3域选择',[0,0,1,0,0],'TSSOP24_PW','https://www.ti.com/lit/ds/symlink/tca9548a.pdf','Texas Instruments','Independent RESET still required for selected stuck-low branch')
    add('H-006','INA226AIDGSR','已有B021覆盖三颗，无重复装配',[0,0,0,0,0],'VSSOP10_DGS','https://www.ti.com/lit/ds/symlink/ina226.pdf','Texas Instruments')
    add('H-007','TPS3431SDRBR','被拒绝的标准看门狗备选DNP',[0,0,0,0,0],'VSON8_DRB_EP','https://www.ti.com/lit/ds/symlink/tps3431.pdf','Texas Instruments','STANDARD watchdog; not a window watchdog. Retain window requirement and B009 pending qualification')
    add('H-008','TPS54202DDCR','B027/B028已计两颗Buck，无重复装配',[0,0,0,0,0],'SOT23_6_DDC','https://www.ti.com/lit/ds/symlink/tps54202.pdf','Texas Instruments','B027/B028 independent buck rails; not central5V LDO')
    for id,mpn,desc,q,pkg,risk in [
        ('H-009','BACK_TO_BACK_FET_AND_DRIVER_TBD','默认OFF TX电源切断及反灌阻断',[1,1,0,0,0],'PIN_REVIEW_TBD','Independent of PL; gate pulldown and power-off paths required'),
        ('H-010','TVS_FUSE_SET_TBD','阵列协调保护组',[1,1,0,0,0],'VALUES_TBD','No SMBJ20A assumption; eFuse67V and driver18V transient envelope separate'),
        ('H-011','HOTSPOT_COMPARATOR_LATCH_REARM_TBD','硬件过温及人工重启锁存',[1,1,0,0,0],'PIN_REVIEW_TBD','TMP117/I2C is not independent hard cutoff'),
        ('H-012','CENTRAL_USB_EFUSE_BUCKBOOST_TBD','中央5V保护及ADC供电调节',[0,0,1,0,0],'PIN_REVIEW_TBD','VBUSmin minus cable and switch may violate4.75V ADC AVCC'),
        ('H-013','IOFF_BUFFER_SET_TBD','双侧断电高阻信号缓冲',[1,1,1,0,0],'PIN_REVIEW_TBD','Every crossing needs Ioff, OE default-off and ground-return review'),
        ('H-014','NC_ESTOP_MANUAL_REARM_TBD','外部急停及人工重启，板座见NS001',[0,0,0,0,1],'KEYED_TBD','Break any wire forces local power-off; fault removal alone cannot restart'),
        ('H-015','SHIELDED_RX_HARNESS_TBD','八路接收屏蔽线束',[0,0,0,0,8],'KEYED_TBD','Local AFE outputs; no direct unprotected transducer toADC'),
        ('H-016','KEYED_SIGNAL_HARNESS_TBD','两阵列数据/时钟/状态线束',[0,0,0,0,2],'RETURN_GROUND_TBD','66MHz is unqualified; no ribbon guarantee'),
        ('H-017','GST60A12-P1M','12V60W电源候选',[0,0,0,0,2],'EXTERNAL_5P5x2P5','Manufacturer P1M plug+5A thermal/load proof and user procurement required'),
        ('H-018','GST40A12-P1M','12V40W备选不重复装配',[0,0,0,0,0],'EXTERNAL_5P5x2P5','Alternative only, <=30.77W/board at30% headroom before derating'),
        ('H-019','USB_C_5V_3A_SOURCE_TBD','中央独立USB-C电源',[0,0,0,0,1],'EXTERNAL','CC3A availability; no implicit draw3A'),
        ('H-020','DRIVER_INPUT_PULLDOWN_TBD','每路驱动输入默认低',[64,64,0,0,0],'R_VALUE_TBD','595OE high makes Q high-Z; pulldown must defeat leakage without load excess'),
        ('H-021','MUX_RESET_SUPERVISOR_TBD','I2C独立复位电路',[0,0,1,0,0],'PIN_REVIEW_TBD','No new PL GPIO claimed; supervisor/recovery method needs actual circuit'),
    ]:add(id,mpn,desc,q,pkg,'CANDIDATE_ENGINEERING_REQUIREMENT',risk=risk)
    for x in bom['items']:
        x['references']={board:[f'{prefix}_{x["id"].replace("-","")}_{i+1:03}' for i in range(x['quantities'][idx])]
                         for board,prefix,idx in [('Upper','UP',0),('Lower','DN',1),('Central','CE',2),('External','EX',4)]}
    save(output/'BOM_INPUTS.json',bom)
    changes=[dict(id=x['id'],before=old_by_id.get(x['id']),after=x) for x in bom['items']
             if x['id'] not in old_by_id or any(x.get(k)!=old_by_id[x['id']].get(k) for k in ('mpn','quantities','risk'))]
    save(output/'BOM_DIFF.json',changes)
    connections=[]
    for r in rows:
        if r['direction'] in ('NC_POWER','HIGH_Z'):continue
        connections.append(dict(net=r['net'],from_endpoint=f'AX7020_{r["connector"]}.{r["pin"]}',
            central_endpoint=f'CENTRAL_AX_{r["connector"]}.{r["pin"]}',direction=r['direction'],
            buffering='IOFF_QUALIFICATION_HOLD' if r['bank'] else 'GROUND_RETURN_REVIEW',rtl=r['rtl_port'],binding=r['binding']))
    for side in ('UP','DN'):
        for lane in range(16):
            connections.append(dict(net=f'TX_DATA_{side}[{lane}]',from_endpoint=f'CENTRAL_{side}.DATA{lane}',
                central_endpoint=f'{side}_595_{lane}.SER',direction='OUT',buffering='LOCAL_LOGIC_3V3',rtl=f'serial_data[{lane+(0 if side=="UP" else 16)}]',binding='DIRECT_LOGICAL_PORT'))
        for ch in range(64):
            connections.append(dict(net=f'{side}_TX{ch}',from_endpoint=f'{side}_595_{ch//4}.Q{ch%4}',
                central_endpoint=f'{side}_TC4427A_{ch//2}.IN{ch%2}',direction='OUT',buffering='PULLDOWN_REQUIRED',rtl='serializer4used',binding='CHANNEL_INDEX_NO_MIRROR'))
        for ch in range(4):
            connections.append(dict(net=f'RX_{ch+(0 if side=="UP" else 4)}_SIGNAL',from_endpoint=f'{side}_RX{ch}.AFE_OUTPUT',
                central_endpoint=f'ADC.V{ch+1+(0 if side=="UP" else 4)}P',direction='ANALOG',buffering='PROTECTION_RC_SHIELDED_RETURN_HOLD',rtl='8CHANNEL_SIGNED_CAPTURE',binding='ADC_ANALOG_CONTRACT'))
    save(output/'CONNECTION_CONTRACT.json',dict(status='NOT_NATIVE_NETLIST_NOT_ERC',connections=connections,
         adc_pins=json.loads((ROOT/'hardware/next_stage/20261010/ADC64_PIN_CONTRACT.json').read_text()),
         power_sources=['AX7020_FACTORY5V','CENTRAL_USB5V','UPPER_DC12V','LOWER_DC12V'],
         current_top_unconnected=[r['net'] for r in rows if r['binding'] in ('NOT_EXPOSED_BY_CURRENT_TOP_REVIEW_REQUIRED','NEW_MUX_CONTROLLER_NOT_CONNECTED_TO_CURRENT_TOP','HARDWARE_FAULT_AGGREGATION_TO_HEALTH_REQUIRED')],
         native_schematic='NOT_CREATED',erc='NOT_RUN',manufacturing='HOLD'))
    positions=[]
    for side,z,normal in [('UP',50,-1),('DN',-50,1)]:
        for i,(y,x) in enumerate(itertools.product((-42,-30,-18,-6,6,18,30,42),repeat=2)):
            positions.append(dict(side=side,kind='TX',channel=i+(0 if side=='UP' else 64),x_mm=x,y_mm=y,z_face_mm=z,normal_z=normal))
        for i,(x,y) in enumerate(((-54,-54),(-54,54),(54,-54),(54,54))):
            positions.append(dict(side=side,kind='RX',channel=i+(0 if side=='UP' else 4),x_mm=x,y_mm=y,z_face_mm=z,normal_z=normal))
    csv_save(output/'TRANSDUCER_POSITIONS.csv',positions)
    library=[]
    for x in bom['items']:
        library.append(dict(id=x['id'],mpn=x['mpn'],manufacturer=x['manufacturer'],package=x['package'],
            source=x['source'],symbol_uuid=None,footprint_uuid=None,pin1='UNVERIFIED',ep='UNVERIFIED',
            pin_to_pad='NOT_RUN',status='DNP_OR_SUPERSEDED' if not sum(x['quantities']) else 'NATIVE_LIBRARY_HOLD'))
    save(output/'LIBRARY_QUALIFICATION.json',library)
    critical={
        'AD7606C-16BSTZ-RL':dict(pins=json.loads((ROOT/'hardware/next_stage/20261010/ADC64_PIN_CONTRACT.json').read_text()),source='ADI Rev.A Table9',status='CURRENT_PIN_CONTRACT_PRESERVED'),
        'TPS26631RGER':dict(pins={1:'IN',2:'IN',3:'B_GATE',4:'DRV',5:'IN_SYS',6:'UVLO',7:'OVP',8:'GND',9:'dVdT',10:'ILIM',11:'MODE',12:'SHDN',13:'IMON',14:'FLT',15:'PGTH',16:'PGOOD',17:'OUT',18:'OUT',19:'NC',20:'NC',21:'NC',22:'NC',23:'NC',24:'NC','EP':'GND'},source='TI SLVSE94G Table5-1 pp3-4; RGE only',status='DATASHEET_FUNCTIONS_CIRCUIT_VALUES_UNQUALIFIED'),
        'TCA9548APWR':dict(pins={1:'A0',2:'A1',3:'RESET_N',4:'SD0',5:'SC0',6:'SD1',7:'SC1',8:'SD2',9:'SC2',10:'SD3',11:'SC3',12:'GND',13:'SD4',14:'SC4',15:'SD5',16:'SC5',17:'SD6',18:'SC6',19:'SD7',20:'SC7',21:'A2',22:'SCL',23:'SDA',24:'VCC'},source='TI SCPS207H Table4-1 p3 PW only',status='DATASHEET_FUNCTIONS_IOFF_RESET_UNQUALIFIED'),
        'STUSB4500LQTR':dict(pins={1:'CC1DB',2:'CC1',3:'NU_GROUND',4:'CC2',5:'CC2DB',6:'RESET_HIGH',7:'SCL',8:'SDA',9:'DISCH',10:'GND',11:'ATTACH_N',12:'ADDR0',13:'ADDR1',14:'RP_1A5_N',15:'GPIO',16:'VBUS_EN_SNK_N',17:'A_B_SIDE',18:'VBUS_VS_DISCH',19:'ALERT_N',20:'RP_3A_N',21:'VREG_1V2',22:'VSYS',23:'VREG_2V7',24:'VDD','EP':'GND'},source='ST DS13102 Rev6 Table1 p4; official web read, local download timed out',status='DATASHEET_FUNCTIONS_POWER_PERMISSION_UNQUALIFIED')}
    save(output/'CRITICAL_PIN_FUNCTIONS.json',critical)
    # Code-native mechanical region figure, not native PCB or a routed layout.
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="900" viewBox="-120 -112 240 225">',
         '<style>text{font-family:Arial;font-size:4px} .zone{fill:#e5edf5;stroke:#587085;stroke-width:.4}</style>',
         '<rect x="-100" y="-90" width="200" height="180" fill="white" stroke="#18364b" stroke-width="1"/>',
         '<rect x="-59.15" y="-59.15" width="118.3" height="118.3" fill="#fff8e6" stroke="#b18e2b" stroke-dasharray="2 2"/>',
         '<rect class="zone" x="-86" y="-84" width="172" height="19"/><text x="-80" y="-74">16 serializers / clock buffers (region only)</text>',
         '<rect class="zone" x="-86" y="65" width="172" height="19"/><text x="-80" y="75">32 dual drivers / 64 TX inputs (region only)</text>',
         '<rect class="zone" x="-96" y="-55" width="30" height="110"/><text x="-94" y="-42">DC / safety</text>',
         '<rect class="zone" x="66" y="-55" width="30" height="110"/><text x="68" y="-42">AFE / IO</text>']
    for r in positions[:68]:
        color='#285c7c' if r['kind']=='TX' else '#c84d3b'
        svg.append(f'<circle cx="{r["x_mm"]}" cy="{-r["y_mm"]}" r="5.15" fill="{color}" opacity=".7"/>')
    svg.extend(['<text x="-98" y="-99">v5 common array 200 x 180 mm candidate. Acoustic projection unchanged.</text>',
                '<text x="-98" y="98">Regions only. No native CAD / no routing / ERC NOT_RUN / manufacture HOLD.</text>','</svg>'])
    (output/'ARRAY_MECHANICAL_REGIONS.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(dict(status='GENERATED_REVIEW_CANDIDATE',pins=len(rows),connections=len(connections),bom_types=len(bom['items']),native_cad='NOT_CREATED')))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'hardware/design_20261011');p.add_argument('--adopt',action='store_true');a=p.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(ROOT):raise ValueError('Output must stay in this v5 clone')
    out.mkdir(parents=True,exist_ok=True);build(out,a.adopt)
