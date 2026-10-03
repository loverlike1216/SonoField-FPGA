"""Read-only source extraction and candidate interface inventory; never emits XDC."""
from pathlib import Path
import csv
import hashlib
import json
import re
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
OUT=ROOT/'evidence/pre_pcb_board_ready'
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    source=ROOT/'hardware/board/references/20261003_user/7020-400引脚配置(2).xlsx'
    with zipfile.ZipFile(source) as z:
        strings=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',NS)]
        cells={}
        for cell in ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//m:c',NS):
            node=cell.find('m:v',NS)
            if node is not None:
                value=node.text
                if cell.get('t')=='s':value=strings[int(value)]
                cells[cell.get('r')]=value
    save(OUT/'connector_reference/excel_cells.json',{'classification':'ACTUAL_XLSX_XML_CELLS','cells':cells})
    db={r['pin']:r for r in csv.DictReader((OUT/'connector_reference/package_pins.tsv').open(),delimiter='\t')}
    maps={}
    for con,first,col in [('J3',3,'B'),('J4',3,'E'),('J5',25,'B'),('J6',25,'E')]:
        rows=[]
        for i in range(20):
            value=cells.get(f'{col}{first+i}','UNKNOWN').strip()
            pkg=db.get(value)
            rows.append({'connector_pin':i+1,'source_cell':f'{col}{first+i}',
                         'fpga_package_pin':value if pkg else None,'source_value':value,
                         'package_properties':pkg,'board_route':'USER_PROVIDED_DOCUMENT_NOT_CONTINUITY_TESTED',
                         'vcco_v':None,'iostandard':None})
        maps[con]=rows
        pins=[r['fpga_package_pin'] for r in rows if r['fpga_package_pin']]
        assert len(pins)==len(set(pins))==16,(con,pins)
        assert all(db[p]['is_general_purpose']=='1' and db[p]['is_bonded']=='1' for p in pins)
    assert cells['B71']=='N18' and cells['C71'].lower()=='33.333mhz'
    save(OUT/'connector_reference/connector_audit.json',{'status':'PASS_PACKAGE_LEGALITY_AND_DOCUMENT_MAPPING_ONLY',
        'source_precedence':'NEW_USER_EXCEL_IMAGE_OVER_LEGACY_CONST','part':'xc7z020clg400-1',
        'connectors':maps,'clock':db['N18'],'physical_voltage_and_continuity':'NOT_VERIFIED'})
    for con,side,offset in [('J3','upper',0),('J4','lower',64)]:
        data=[r for r in maps[con] if r['fpga_package_pin']]
        for i,r in enumerate(data):
            r.update(signal=f'{side.upper()}_TX_DATA_{i:02d}',direction='FPGA_TO_DRIVER',serializer_lane=i+offset//4,
                     channels=[f'{side.upper()}_TX_{4*i+j:02d}' for j in range(4)],
                     shift_order_local_channels=[4*i+3,4*i+2,4*i+1,4*i])
        save(ROOT/f'config/{con.lower()}_{side}_data_interface.json',{'status':'CANDIDATE_NOT_ELECTRICALLY_FROZEN',
          'connector':con,'side':side,'channels':64,'lanes':16,'used_bits_per_lane':4,'pins':data,
          'supply_pins':{'9':'UNUSED_AUX_5V','10':'GND','11':'GND','12':'UNUSED_AUX_5V'},
          'external_power_required':True,'full_board_xdc_emitted':False})
    # Single centralized eight-RX ADC is the existing BOM/RTL architecture.
    upper=['UPPER_SHIFT_CLK','UPPER_LATCH_CLK','UPPER_OE_N','UPPER_BOARD_ENABLE','UPPER_RX_BLANK',
           'ADC_RESET','ADC_CONVST','ADC_CS_N','ADC_SCLK','ADC_SDI','ADC_BUSY',
           'ADC_DOUT_A','ADC_DOUT_B','ADC_DOUT_C','ADC_DOUT_D','UPPER_FAULT_N']
    lower=['LOWER_SHIFT_CLK','LOWER_LATCH_CLK','LOWER_OE_N','LOWER_BOARD_ENABLE','LOWER_RX_BLANK','LOWER_FAULT_N']
    for con,side,signals in [('J5','upper',upper),('J6','lower',lower)]:
        pins=[dict(r) for r in maps[con] if r['fpga_package_pin']]
        for i,r in enumerate(pins):
            signal=signals[i] if i<len(signals) else f'RESERVED_{i-len(signals):02d}'
            r.update(signal=signal,direction=('ADC_OR_FAULT_TO_FPGA' if signal in ['ADC_BUSY','ADC_DOUT_A','ADC_DOUT_B','ADC_DOUT_C','ADC_DOUT_D','UPPER_FAULT_N','LOWER_FAULT_N'] else 'FPGA_TO_BOARD' if not signal.startswith('RESERVED') else 'UNASSIGNED'))
        budget={'status':'CANDIDATE_NOT_FROZEN','connector':con,'side':side,'capacity':16,'used':len(signals),
                'reserved':16-len(signals),'central_adc_count':1,'central_adc_rx_channels':8,
                'adc_topology':'ONE_SHARED_ADC_CONTROL_BUS_ON_J5; LOWER_ANALOG_RX_REACHES_SAME_ADC',
                'hardware_fault_inputs':'PROPOSED_NOT_IMPLEMENTED_OR_QUALIFIED',
                'independent_bank_disable':'REQUIRED_AT_INTEGRATION; CURRENT_CORE_HAS_GLOBAL_DISABLE',
                'pins':pins,'vcco_v':None,'iostandard':None}
        save(ROOT/f'config/{con.lower()}_{side}_signal_budget.json',budget)
        save(ROOT/f'config/{con.lower()}_{side}_control_adc_interface.json',budget)
    jtag=(OUT/'board_identity/local_raw/jtag.log').read_text(errors='replace')
    assert '23727093' in jtag and '4BA00477' in jtag
    sanitized=re.sub(r'1234-oj1A','[CABLE_ID_REDACTED]',jtag)
    (OUT/'board_identity/jtag_sanitized.log').write_text(sanitized,encoding='utf-8')
    save(OUT/'board_identity/jtag_identity.json',{'status':'HARDWARE_VERIFIED_IDENTITY_ONLY','tool':'Vivado 2025.2',
      'family':'Zynq-7000','silicon':'xc7z020','idcode':'0x23727093','arm_dap_idcode':'0x4BA00477',
      'device_count':2,'jtag_clock_hz':15000000,'jtag_clock_is_pl_clock':False,
      'programmed':False,'ps_memory_accessed':False,'ft2232_variant':'NOT_DISTINGUISHED_BY_VID_PID_ALONE'})
    manifest=[]
    sources=[(Path('G:/Users/loverlike/Desktop/26嵌入式比赛/BOM/constrain/7020-400引脚配置(2).xlsx'),source),
      (Path('G:/Users/loverlike/Desktop/26嵌入式比赛/BOM/constrain/bc4867a086eab388bd705e6cc4926b8f.png'),source.parent/'connector_layout.png'),
      (Path.home()/'.codex/attachments/6126fbc9-d7a4-4b66-9340-1de3c60b92ee/已粘贴的文本.txt',REPO/'AI-interaction-memory/codex/instructions/v2_final_pre_pcb_board_integration.md')]
    for src,dst in sources:
        sh=hashlib.sha256(src.read_bytes()).hexdigest();dh=hashlib.sha256(dst.read_bytes()).hexdigest()
        assert sh==dh
        manifest.append({'original':str(src),'classified_copy':dst.relative_to(REPO).as_posix(),'sha256':sh,
                         'bytes':dst.stat().st_size,'original_preserved':True})
    save(OUT/'repository_reconciliation/upload_manifest.json',{'status':'PASS','files':manifest,
      'scope':'Three latest supplied originals; previous imports remain in their canonical locations'})
    print('PASS source copies, workbook mapping, 64 legal unique connector pins, N18, public JTAG evidence')

if __name__=='__main__':main()
