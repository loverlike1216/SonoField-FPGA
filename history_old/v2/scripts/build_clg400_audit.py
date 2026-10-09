"""Compare source claims with the exported Vivado CLG400 package database.

Image transcriptions below were manually read from the local user references.
They remain secondary evidence; conflicts are retained, never auto-corrected.
"""
import csv
from collections import Counter,defaultdict
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parent
OUT=ROOT/'evidence/board_transport'

def save(name,value):
    (OUT/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def main():
    db={p['pin']:p for p in csv.DictReader((OUT/'clg400_package_pins.tsv').open(),delimiter='\t')}
    rows=[]
    def add(source,pin,signal,connector=None,number=None,confidence='DOCUMENTED_CANDIDATE',primary=False):
        pkg=db.get(pin)
        rows.append(dict(source_file='Zynq7020/'+source,logical_signal=signal,connector=connector,
            connector_pin=number,fpga_package_pin=pin,bank=pkg['bank'] if pkg else None,
            pin_func=pkg['pin_func'] if pkg else None,package_availability=bool(pkg),
            pl_user_io=bool(pkg and pkg['is_general_purpose']=='1' and pkg['is_bonded']=='1'),
            vivado_is_bonded=pkg['is_bonded'] if pkg else None,confidence=confidence,
            precedence='USER_SELECTED_CONST' if primary else 'SECONDARY_REFERENCE',
            board_route_verified=False,vcco='UNKNOWN',accepted_xdc=False))
    for file in sorted((REPO/'Zynq7020/constrain').glob('*.const')):
        for p in ET.parse(file).getroot().findall('Port'):
            signal=p.get('Function');m=re.fullmatch(r'(J[3-6]) Pin(\d*)',signal)
            add('constrain/'+file.name,p.get('Name'),signal,m[1] if m else None,
                int(m[2]) if m and m[2] else None,primary=True)
    numbers=[1,2,3,4,5,6,7,8,13,14,15,16,17,18,19,20]
    image_headers={
        'J3':'U14 U15 T14 T15 T16 U17 V17 V18 U18 U19 T17 R18 N17 P18 T20 U20',
        'J4':'F19 F20 D19 D20 C20 B20 B19 A20 E18 E19 E17 D18 F16 F17 H15 G15',
        'J5':'N20 P20 M17 M18 M19 M20 L19 L20 K19 J19 H16 H17 G17 G18 G19 G20',
        'J6':'T11 T10 U12 T12 W13 V12 V13 U13 Y14 W14 W15 V16 V15 Y17 W16 V16'}
    for con,pins in image_headers.items():
        for num,pin in zip(numbers,pins.split()):add('1.png' if con in ('J3','J4') else '2.png',pin,f'{con} Pin{num}',con,num)
    periph={
        'LED':dict(zip(['D'+str(i) for i in range(12,20)],'R19 T19 W20 V20 G14 J18 Y18 Y19'.split())),
        'SPI':dict(zip(['CS','SCK','SDI','SDO','WP','Hold'],'V5 T9 V7 W11 Y11 Y8'.split())),
        'NRF':dict(zip(['CSN','SCK','MOSI','MISO','IRQ','CE'],'Y13 V11 V10 V6 W6 Y12'.split())),
        'HDMI':dict(zip(['CEC','SCL','SDA','HPD','CLK-','CLK+','D0-','D0+','D1-','D1+','D2-','D2+'],'J15 J20 H20 M14 K18 K17 J14 K14 J16 K16 L15 L14'.split())),
        'SW5':{'1':'Y7','2':'Y6','3':'Y9'},'SW1':{'button':'W9'},'clock':{'33.333MHz':'N18'}}
    for group,pins in periph.items():
        for signal,pin in pins.items():
            add('396993c30e2d447db53dcf3b509222a1.png',pin,group+' '+signal)
            if group in ('LED','SPI'):add('2.png',pin,group+' '+signal)
            if group not in ('LED','SPI') or (group=='LED' and signal in ('D16','D17','D18','D19')) or (group=='SPI' and signal in ('WP','Hold')):
                add('3.png',pin,group+' '+signal)
    # The Robei screenshot displays the same 37 peripheral rows as hardware.const.
    for row in list(rows):
        if row['source_file'].endswith('hardware.const'):
            add('1ec52b807edd6cf0dddcf8ffc4109a82.png',row['fpga_package_pin'],row['logical_signal'])
    # Layout gives positions, NOT connector pin numbers; don't invent orientation.
    layout={
      'J4':['H15 F16 E17 E18 B19 C20 D19 F19','G15 F17 D18 E19 A20 B20 D20 F20'],
      'J3':['U15 T15 U17 V18 U19 R18 P18 U20','U14 T14 T16 V17 U18 T17 N17 T20'],
      'J6':['T11 T10 U12 T12 W13 V12 V13 U13 Y14 W14 W15 Y16 V15 Y17 W16 V16'],
      'J5':['G20 G19 G18 G17 H17 H16 J19 K19 L20 L19 M20 M19 M18 M17 P20 N20']}
    for con,groups in layout.items():
        for index,pin in enumerate(' '.join(groups).split()):
            add('9268ababf01f495387fe9e2705411573.png',pin,f'{con} diagram position {index} (not pin number)',con,None)
    primary=[r for r in rows if r['precedence']=='USER_SELECTED_CONST']
    conflicts=[]
    for r in primary:
        if not r['pl_user_io']:conflicts.append(dict(kind='NOT_PL_USER_IO',record=r))
        if r['connector'] and r['connector_pin'] is None:conflicts.append(dict(kind='MISSING_CONNECTOR_PIN',record=r))
    mapping=defaultdict(list)
    for r in rows:
        if r['connector_pin'] is not None:mapping[(r['connector'],r['connector_pin'])].append(r)
    for (con,num),items in mapping.items():
        if len({r['fpga_package_pin'] for r in items})>1:
            conflicts.append(dict(kind='CONNECTOR_MAPPING_CONFLICT',connector=con,pin=num,
                claims=[dict(source=r['source_file'],fpga_pin=r['fpga_package_pin'],precedence=r['precedence']) for r in items]))
    conflicts.extend([
      dict(kind='HDMI_CEC',claims=['hardware.const / EDA image: J5 = PS_DDR_BA2_502','peripheral images: J15 = IO_25_35'],resolution='OPEN; J5 forbidden as PL IO; no automatic substitution'),
      dict(kind='Y16_V16',claims=['gpio.const: Y16 = J6 Pin6; V16 = J6 Pin without number','2.png: V16 used for both J6 Pin16 and Pin20','layout image: Y16 and V16 at separate positions'],resolution='OPEN'),
      dict(kind='CLOCK_VALUE',claims=['hardware.const/EDA: N18 33 MHz','peripheral table: N18 33.333 MHz'],resolution='User-selected 33 MHz precedence, not measured frequency')])
    general=Counter(r['bank'] for r in db.values() if r['is_general_purpose']=='1')
    save('clg400_part_candidates.json',dict(classification='CANDIDATE_ANALYSIS_ONLY',canonical_part=None,
        tool='Vivado 2025.2',candidates=[dict(row,available=True) for row in csv.DictReader((OUT/'clg400_parts.tsv').open(),delimiter='\t')]))
    save('clg400_pin_audit.json',dict(package='CLG400',tool='Vivado 2025.2',package_balls=len(db),
        pl_io_by_bank=dict(general),primary_record_count=len(primary),all_claim_count=len(rows),records=rows,
        source_coverage='Both .const files; all readable pin tables, EDA screenshot and unnumbered layout. Board photos/intro contain no additional assignable FPGA-pin claims.',
        note='IS_BONDED=0 on supply/GND balls does not mean physically absent. Package existence and PL-user-IO legality are recorded separately.'))
    save('constraint_conflicts.json',dict(status='OPEN',conflicts=conflicts))
    summary=f'''# CLG400 pin audit

Vivado 2025.2: {len(db)} package balls, PL user IO {dict(general)} (125 total).
AMD UG865 v1.9 page 22 independently states bank 33 absent, bank 13 partial, PS banks fully bonded.
Source: https://docs.amd.com/v/u/en-US/ug865-Zynq-7000-Pkg-Pinout
No bank 33 PL pin exists in this package database. Bank 13 provides 25 PL user IO, banks 34/35 each 50.
PS banks 500/501/502 are present. This proves bonding, not board routing or voltage.

Audited {len(primary)} primary .const claims and {len(rows)} total source claims including secondary images.
Each JSON row records signal, connector/number where known, ball, bank, availability, source and confidence.
No generated XDC is accepted. All board-route and VCCO evidence remains unverified.

Critical finding: hardware.const HDMI CEC J5 is PS_DDR_BA2_502, not a PL IO.
Secondary J15 is a legal bank35 PL IO, but this does NOT establish board routing or authorize replacement.
J3/J4/J5/J6 numbering differences, J4 Pin1 H15 versus F19, duplicated J4 Pin6 D18/E18,
missing V16/J6 number and image Y16/V16 disagreement are all retained in constraint_conflicts.json.
User-selected .const precedence resolves source priority only; it cannot make an illegal pin legal.
N18 is IO_L13P_T2_MRCC_34, clock-capable; documented 33 MHz is not a measurement.
Bank33/CLG484 assumptions are prohibited; bank13 cannot be budgeted as 50 pins.
Unnumbered layout positions are intentionally not converted to connector pin numbers.
'''
    (OUT/'CLG400_PIN_AUDIT.md').write_text(summary,encoding='utf-8')
    print('CLG400_AUDIT',len(primary),len(rows),'records;',len(conflicts),'conflict groups; GPIO banks',dict(general))

if __name__=='__main__':main()
