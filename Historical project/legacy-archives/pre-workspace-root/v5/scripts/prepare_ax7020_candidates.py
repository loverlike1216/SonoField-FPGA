"""Extract documented candidates, never emit deployment XDC or execute vendor code."""
from pathlib import Path
import csv,json,re,hashlib,xml.etree.ElementTree as ET,datetime
R=Path(__file__).resolve().parents[2]; V=R/'v5'
RAW=V/'evidence/board_bringup/20261009/local_raw'
OUT=V/'hardware/integration_candidates/20261009'
def dump(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 manual=(V/'hardware/ax7020/local_raw/official_manual.rst').read_text(encoding='utf-8')
 rows=[]
 for conn,section,end in [('J10','**J10扩展口引脚分配**','7.5 扩展口J11'),('J11','**J11扩展口引脚分配**','7.6')]:
  text=manual.split(section,1)[1].split(end,1)[0]
  found=re.findall(r'\| PIN(\d+)\s*\|([^|]+)\|([^|]+)\|([^|]+)\|',text)
  assert len(found)==40,(conn,len(found))
  for number,signal,func,pin in found:
   n=int(number);bank=re.search(r'_(34|35)\s*$',func)
   rows.append(dict(connector=conn,pin=n,documented_net=signal.strip(),package_pin=pin.strip(),bank=bank[1] if bank else '',
    vcco='3.3V_DOCUMENTED_NOT_MEASURED' if bank else '',direction='POWER_OR_GROUND',v5_signal='',status='V2_DOCUMENT_CANDIDATE_REV3_MATCH_PENDING',series_resistor='33ohm documented' if bank else ''))
 directions={}; signals={}
 for conn,side in [('J10','UP'),('J11','DN')]:
  ns=[f'TX_DATA_{side}[{i}]' for i in range(16)]+[f'{side}_{s}' for s in ['SRCLK','RCLK','OE_N','RESET_N','RX_BLANK','HEARTBEAT','SYNC','PGOOD','FAULT_N']]
  for n,s in enumerate(ns,3):signals[(conn,n)]=s;directions[s]='IN' if s.endswith(('PGOOD','FAULT_N')) else 'OUT'
 adc=[('ADC_CONVST','OUT'),('ADC_SCLK','OUT'),('ADC_CS_N','OUT'),('ADC_SDI','OUT'),('ADC_RESET','OUT'),('ADC_BUSY','IN')]+[(f'ADC_DOUT[{i}]','IN') for i in range(4)]+[('MON_I2C_SCL','OPEN_DRAIN'),('MON_I2C_SDA','OPEN_DRAIN'),('ESTOP_OK','IN')]
 spare=[(r['connector'],r['pin']) for r in rows if r['bank'] and (r['connector'],r['pin']) not in signals]
 for key,(s,d) in zip(spare,adc):signals[key]=s;directions[s]=d
 for row in rows:
  key=row['connector'],row['pin']
  if row['bank']:
   row['v5_signal']=signals.get(key,'RESERVED');row['direction']=directions.get(row['v5_signal'],'HIGH_Z')
   row['central_path']='separate open-drain buffer' if row['direction']=='OPEN_DRAIN' else 'qualified 3.3V/Ioff buffering; no direct power'
   row['array_path']='local clock fanout' if row['v5_signal'].endswith(('SRCLK','RCLK')) else 'direction-qualified AXC candidate or central ADC'
  else:row['central_path']='GND reference only' if row['documented_net']=='GND' else 'NO_CONNECT_NO_ARRAY_POWER';row['array_path']=''
 assert len(signals)==63 and len({r['package_pin'] for r in rows if r['bank']})==68
 with (OUT/'connector_pinmap_candidate.csv').open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
 dump(OUT/'gpio_budget.json',dict(status='DOCUMENTED_CANDIDATE_NOT_XDC',available_documented=68,used=63,reserved=5,
   array_each={'tx_data':16,'clocks':2,'oe_reset':2,'blank_heartbeat_sync':3,'pgood_fault':2},adc=10,i2c=2,estop=1,
   axc_each_array={'nonclock_outputs':21,'returns':2,'four_bit_groups':7,'candidate_chips':4,'original_chips':3},
   power_pins='NC except grounds; AX7020 does not feed array/central supply'))
 tree=ET.parse(RAW/'xsa_design_1.hwh');ps=next(m for m in tree.iter('MODULE') if m.get('MODTYPE')=='processing_system7')
 params={p.get('NAME'):p.get('VALUE') for p in ps.iter('PARAMETER')}
 selected={k:v for k,v in params.items() if k.startswith('PCW_') and any(x in k for x in ['DDR','UART1','CRYSTAL','FCLK','FPGA0','EN_RST','USE_M_AXI_GP0','CPU_CPU'])}
 dump(OUT/'official_ps_reference.json',dict(source_commit='fcf1e4a239b0f47e8ee95dfde7c2eedc5685c327',source_path='course_s2_vitis/01_ps_hello/Vitis/design_1_wrapper.xsa',
   sha256=hashlib.sha256((RAW/'hello.xsa').read_bytes()).hexdigest(),status='EXTRACTED_NOT_EXECUTED_NOT_REVISION_MATCHED',parameters=selected,
   conflicts=['Manual names Hynix H5TQ4G63AFR-PBC; reference PCW_UIPARAM_DDR_PARTNO=MT41J256M16 RE-125. Vendor timing-compatible preset is possible, but actual Revision3 DDR identity must be matched.',
   'Reference FCLK0=50MHz, not core design target132MHz. No silent substitution or ps7_init execution.']))
 adcconfig=dict(status='ISOLATED_RECOMMENDATION_NOT_FORMAL_SELECTION',mpn='AD7606C-16BSTZ-RL',hardware_mode='software mode selected by OS[2:0]=111',
  registers={'0x02':16,'0x03':17,'0x04':17,'0x05':17,'0x06':17,'0x07':255},
  range='all +/-5V single-ended',bandwidth='all channels high bandwidth220kHz',sample_rate='retain current sample cadence; do not silently raise to1MSPS',
  serial='4 DOUT;16bit two-complement;32clocks per8channel frame;no status/CRC',
  verification=['read back CONFIG,RANGE1..4,BANDWIDTH','corrupt readback must prevent ready','check lane/channel ordering','remeasure phase/gain; no automatic LUT inheritance'],
  source='https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf',source_pages=[42,47,49,61,67])
 dump(OUT/'adc_candidate.json',adcconfig)
 commands=[0x4200,0x0210,0x0311,0x0411,0x0511,0x0611,0x07ff]
 for addr in range(2,8):commands.extend([(addr|0x40)<<8,0x4000])
 commands.append(0)
 rom='// Isolated configuration ROM only; not instantiated in the production ADC interface.\nmodule ad7606c_candidate_rom(input wire[4:0] index,output reg[15:0] command);\nalways @* case(index)\n'
 rom+=''.join(f"5'd{i}: command=16'h{word:04x};\n" for i,word in enumerate(commands))
 rom+="default: command=16'h0000;\nendcase\nendmodule\n"
 (OUT/'ad7606c_candidate_rom.sv').write_text(rom,encoding='utf-8')
 pinlist=' '.join(r['package_pin'] for r in rows if r['bank'])
 tcl=f'''# Device database review only. No board access or deployment constraints.
create_project -in_memory -part xc7z020clg400-2
report_property [get_parts xc7z020clg400-2]
set stub [open v5/evidence/board_bringup/20261009/local_raw/package_review.v w]
puts $stub "module package_review(input wire a, output wire b); assign b=a; endmodule"
close $stub
read_verilog v5/evidence/board_bringup/20261009/local_raw/package_review.v
synth_design -rtl -top package_review -part xc7z020clg400-2
set out [open v5/evidence/board_bringup/20261009/package_pin_database.csv w]
puts $out "pin,bank,pin_func"
foreach pin {{{pinlist}}} {{
 set obj [get_package_pins $pin]
 puts $out "$pin,[get_property BANK $obj],[get_property PIN_FUNC $obj]"
}}
close $out
close_project
'''
 (V/'scripts/ax7020_package_review.tcl').write_text(tcl,encoding='utf-8')
 print(json.dumps(dict(pin_rows=len(rows),gpio=63,reserved=5,reference_ddr=selected.get('PCW_UIPARAM_DDR_PARTNO'),rom_commands=len(commands))))
if __name__=='__main__':main()
