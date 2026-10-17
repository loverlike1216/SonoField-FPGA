"""Cross-check review contracts, real package report and exported XLSX caches."""
from pathlib import Path
import argparse,csv,hashlib,json,re,sys,zipfile,xml.etree.ElementTree as ET
from decimal import Decimal, ROUND_CEILING
ROOT=Path(__file__).resolve().parents[1]


def io_identity(value):
    """Manual omits native VREF/DQS/AD/SRCC/MRCC suffixes, not lane/side/tile/bank."""
    value=re.sub(r'\s+','',value)
    value=re.sub(r'(IO_L\d+)_([PN])',r'\1\2',value)
    match=re.fullmatch(r'(IO_L\d+[PN]_T\d)(?:_(?:VREF|DQS|AD\d+[PN]|SRCC|MRCC|PUDC|B))*_(\d+)',value)
    return match.groups() if match else None


def audit(data,package):
    errors=[];rows=data['pins']
    if len(rows)!=80 or len({(r['connector'],r['pin']) for r in rows})!=80:errors.append('80 unique contacts required')
    gpio=[r for r in rows if r['bank']]
    if len(gpio)!=68 or sum(r['direction']=='HIGH_Z' for r in gpio)!=5:errors.append('63/68 GPIO contract mismatch')
    if len({r['package_pin'] for r in gpio})!=68:errors.append('Duplicate package pin')
    for r in gpio:
        p=package.get(r['package_pin'])
        if p is None or p['bank']!=r['bank']:errors.append('Native package bank mismatch '+r['package_pin'])
        if p and (io_identity(r['fpga_name']) is None or io_identity(p['pin_function'])!=io_identity(r['fpga_name'])):
            errors.append('Manual/native function mismatch '+r['package_pin'])
    for r in rows:
        if r['pin'] in (2,39,40) and (r['direction']!='NC_POWER' or r['binding']!='NO_CONNECT'):errors.append('Power backfeed risk')
    reset=next((r for r in rows if r['net']=='ADC_RESET'),None)
    if not reset or reset['binding']!='ACTIVE_HIGH_RESET':errors.append('ADC reset polarity')
    return errors


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    args.output=args.output.resolve()
    if not args.output.is_relative_to(ROOT) or args.output.exists():
        raise ValueError('A fresh output inside this v5 clone is required; failed evidence must be retained')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    h=ROOT/'hardware/design_20261011';e=ROOT/'evidence/hardware_design_20261011'
    data=json.loads((h/'SIGNAL_CONTRACT.json').read_text())
    package={r['package_pin']:r for r in csv.DictReader((e/'VIVADO_PACKAGE_PINS.csv').open())}
    errors=audit(data,package)
    negative=[]
    for case in ('bank','duplicate','power','reset','lane','polarity','tile','unknown_suffix'):
        mutant=json.loads(json.dumps(data))
        if case=='bank':mutant['pins'][2]['bank']='35'
        elif case=='duplicate':mutant['pins'][3]['package_pin']=mutant['pins'][2]['package_pin']
        elif case=='power':mutant['pins'][1]['direction']='OUT'
        elif case=='reset':next(r for r in mutant['pins'] if r['net']=='ADC_RESET')['binding']='ACTIVE_LOW'
        elif case=='lane':mutant['pins'][2]['fpga_name']='IO_L21N_T3_34'
        elif case=='polarity':mutant['pins'][2]['fpga_name']='IO_L22P_T3_34'
        elif case=='tile':mutant['pins'][2]['fpga_name']='IO_L22N_T2_34'
        else:mutant['pins'][2]['fpga_name']='IO_L22N_T3_UNKNOWN_34'
        rejected=bool(audit(mutant,package));negative.append(dict(case=case,rejected=rejected))
        if not rejected:errors.append('Negative mutant accepted '+case)
    bom=json.loads((h/'BOM_INPUTS.json').read_text(encoding='utf-8'))
    refs=[r for x in bom['items'] for rs in x['references'].values() for r in rs]
    if len(refs)!=len(set(refs)):errors.append('Duplicate BOM reference')
    expected={name:sum(x['quantities'][idx] for x in bom['items']) for name,idx in [('Upper',0),('Lower',1),('Central',2),('External',4)]}
    path=ROOT/'hardware/bom/working/2026-10-11/BOM_V5_FOUR_SOURCE_20261011.xlsx'
    ns={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(path) as z:
        sheets=ET.fromstring(z.read('xl/workbook.xml')).findall('x:sheets/x:sheet',ns)
        if [s.attrib['name'] for s in sheets]!=['Summary','Central','Upper','Lower','External']:errors.append('Five-sheet contract')
        xml=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        cells={c.attrib['r']:c for c in xml.findall('.//x:c',ns)}
        row=len(bom['items'])+6
        for col,name in zip('CDEF',('Upper','Lower','Central','External')):
            cell=cells[f'{col}{row}']
            if cell.find('x:f',ns) is None or float(cell.find('x:v',ns).text)!=expected[name]:errors.append('Formula/cache mismatch '+name)
        # Check every cached quantity and spare formula independently, not just totals.
        for sheet_no,name,idx in ((2,'Central',2),(3,'Upper',0),(4,'Lower',1),(5,'External',4)):
            sheet=ET.fromstring(z.read(f'xl/worksheets/sheet{sheet_no}.xml'))
            part_cells={c.attrib['r']:c for c in sheet.findall('.//x:c',ns)}
            for i,item in enumerate(bom['items'],5):
                qty=item['quantities'][idx]
                wanted=int((Decimal(qty)*Decimal('1.1')).to_integral_value(rounding=ROUND_CEILING))
                installed=part_cells[f'E{i}'];spares=part_cells[f'G{i}']
                if float(installed.find('x:v',ns).text)!=qty:errors.append(f'Installed quantity {name}/{item["id"]}')
                if spares.find('x:f',ns).text!=f'ROUNDUP(E{i}*(1+F{i}),0)' or float(spares.find('x:v',ns).text)!=wanted:
                    errors.append(f'Spare formula/cache {name}/{item["id"]}')
    naming=[dict(package_pin=r['package_pin'],manual=r['fpga_name'],native=package[r['package_pin']]['pin_function'],
                 identity=io_identity(r['fpga_name'])) for r in data['pins'] if r['bank'] and r['fpga_name']!=package[r['package_pin']]['pin_function']]
    result=dict(status='FAIL' if errors else 'PASS',errors=errors,negative_cases=negative,
                manual_short_name_differences=naming,
                native_package_pins=len(package),contacts=len(data['pins']),used_gpio=63,spare_gpio=5,
                installed_counts=expected,component_references=len(refs),bom_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                source='Native Vivado2025.2 package CSV vs independently parsed manual80; XLSX XML formula caches vs Python JSON reduction',
                physical_pin_continuity='NOT_RUN',erc='NOT_RUN',production='HOLD')
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2));return bool(errors)


if __name__=='__main__':sys.exit(main())
