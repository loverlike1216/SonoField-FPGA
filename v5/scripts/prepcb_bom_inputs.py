"""Read existing active working workbook, preserve it, emit candidate input rows."""
from pathlib import Path
import zipfile, xml.etree.ElementTree as ET, json
ROOT=Path(__file__).resolve().parents[1]

def main():
    source=ROOT/'hardware/bom/working/2026-10-09/BOM_AX7020_NU40C10T_WORKING_2026-10-09.xlsx'
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(source) as z:
        shared=[''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',ns)]
        rows=[]
        for row in ET.fromstring(z.read('xl/worksheets/sheet2.xml')).findall('.//s:sheetData/s:row',ns):
            cells=['']*21
            for cell in row:
                col=0
                for char in cell.attrib['r'].rstrip('0123456789'):col=col*26+ord(char)-64
                v=cell.find('s:v',ns)
                if v is not None:cells[col-1]=shared[int(v.text)] if cell.get('t')=='s' else v.text
            if cells[0].startswith('B-'):rows.append(cells)
    items=[]
    for a in rows:
        qty=[int(float(x or 0)) for x in a[7:12]]
        mpn,source_url=a[4],a[19]
        reason='Inherited candidate quantity; netlist/thermal review pending'
        if a[0]=='B-014':mpn='AD7606BBSTZ-RL';source_url='https://www.analog.com/en/products/ad7606b.html';reason='FORMAL ADC unchanged; C-16 separate unapproved alternative'
        if a[0]=='B-017':qty=[0,0,1,0,0];reason='Recommended central RH sensor, heater OFF'
        if a[0] in ('B-019','B-040'):qty=[0]*5;reason='Removed central external power path; central AX7020-only source'
        if a[0] in ('B-027','B-028','B-029','B-030','B-051'):qty[2]=0;reason='No central12V supply/converter or5V-to5V LDO headroom; central header budget HOLD'
        if a[0]=='B-044':mpn='12V 5A supply candidate (each)';qty=[0,0,0,0,2];reason='Two independent60W-rated sources;2A protection baseline unchanged, not60W load authorization'
        if a[0]=='B-001':source_url='USER_NU40C10T_VENDOR_DATASHEET_REQUIRED'
        if a[0]=='B-032':qty=[1,1,1,0,0];reason='REQUIRED 3TMP117; center48/up49/down4B'
        if a[0]=='B-023':reason='SMBJ20A protection coordination OPEN; cannot release'
        items.append(dict(id=a[0],description=a[3],mpn=mpn,package=a[6],quantities=qty,
            supply=a[5],current_A=None,logic='3V3 ONLY if GPIO; other domains require review',
            measured='NOT_VERIFIED',package_evidence='Public source only; pin1/EP/native footprint UNVERIFIED',
            source=source_url,supplier='AUTHORIZED_VENDOR_NOT_SELECTED',approval='NOT_APPROVED_FOR_PROCUREMENT',risk=reason))
    for identity,description,mpn,package,qty,url in [
        ('PC-001','Remote I2C hot-swap isolation','TCA4307DGKR','VSSOP-8',[0,0,2,0,0],'https://www.ti.com/product/TCA4307'),
        ('PC-002','Driver hotspot independent comparator','PART_SELECTION_HOLD','HOLD',[1,1,0,0,0],'USER_SAFETY_REQUIREMENT'),
        ('PC-003','Central header reverse-blocking protection','PART_SELECTION_HOLD','HOLD',[0,0,2,0,0],'USER_AX7020_POWER_ONLY_REQUIREMENT'),
        ('PC-004','NC emergency stop independent contact','PART_SELECTION_HOLD','HOLD',[0,0,0,0,1],'USER_SAFETY_REQUIREMENT')]:
        items.append(dict(id=identity,description=description,mpn=mpn,package=package,quantities=qty,supply='CANDIDATE_REVIEW_REQUIRED',current_A=None,
            logic='OPEN_DRAIN_3V3' if 'I2C' in description else 'ELECTRICAL_REVIEW_REQUIRED', measured='NOT_VERIFIED',package_evidence='Native pin1/EP not verified',
            source=url,supplier='NOT_SELECTED',approval='NOT_APPROVED_FOR_PROCUREMENT',risk='Electrical/thermal qualification HOLD'))
    output=ROOT/'hardware/prepcb/bom_inputs.json';output.write_text(json.dumps(dict(source=source.relative_to(ROOT).as_posix(),items=items),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
