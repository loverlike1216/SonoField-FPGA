"""Read XLSX XML caches with stdlib; independent of artifact-tool calculation."""
from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,json,csv,math,hashlib
R=Path(__file__).resolve().parents[1];ROOT=R.parents[4];E=ROOT/'v5/evidence/pcb_s3_20261011';N={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def read(p):
    z=zipfile.ZipFile(p);shared=[]
    if 'xl/sharedStrings.xml' in z.namelist():shared=[''.join(e.itertext()) for e in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',N)]
    rels={r.attrib['Id']:r.attrib['Target'] for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))};out={};count=0
    for sh in ET.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',N):
        target=rels[sh.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']];target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
        cells={}
        for c in ET.fromstring(z.read(target)).findall('.//m:c',N):
            v=c.find('m:v',N);raw=v.text if v is not None else None;typ=c.attrib.get('t');f=c.find('m:f',N)
            assert typ!='e',(sh.attrib['name'],c.attrib['r'],raw)
            if typ=='s':value=shared[int(raw)]
            elif typ=='inlineStr':value=''.join(c.find('m:is',N).itertext())
            elif typ=='str':value=raw
            elif raw is not None:
                try:value=float(raw)
                except ValueError:value=raw
            else:value=None
            cells[c.attrib['r']]=value
            if f is not None:count+=1;assert raw is not None,(sh.attrib['name'],c.attrib['r'],'missing formula cache')
        out[sh.attrib['name']]=cells
    return out,count
def main():
    p,pc=read(R/'02_THREE_BOARD_POWER_BUDGET.xlsx');b,bc=read(R/'10_BOM_RELEASE_CANDIDATE_DELTA.xlsx')
    calc=json.loads((E/'POWER_RESULTS.json').read_text());data=json.loads((R/'calc/workbook_data.json').read_text());cnt=json.loads((E/'CANDIDATE_COUNTS.json').read_text());checks=[]
    def eq(a,z,msg):assert isinstance(a,(int,float)) and math.isclose(a,z,rel_tol=1e-9,abs_tol=1e-9),(msg,a,z);checks.append(msg)
    eq(p['Decision']['F5'],calc['central_steady_input_max_w'],'central independent numeric')
    for row in [6,7]:eq(p['Decision']['F'+str(row)],calc['array_steady_input_max_w'],'array independent numeric'+str(row))
    for i,board in enumerate(['UP','DN','CENTRAL'],5):eq(b['BOM Summary']['B'+str(i)],cnt['per_board'][board],board+' quantity')
    eq(b['BOM Summary']['B9'],cnt['total_components'],'total installed');eq(b['BOM Summary']['C9'],1205,'legacy baseline')
    for i,row in enumerate(data['bom'],5):eq(b['BOM Groups']['F'+str(i)],row['qty'],'BOM group'+str(i))
    for i,row in enumerate(data['budget'],5):
        val=p['Loads']['H'+str(i)]
        if row['P_max_continuous_W'] is None:assert val=='UNKNOWN',(i,val)
        else:eq(val,row['P_max_continuous_W'],'load allocation'+str(i))
    result=dict(status='PASS',formula_count_power=pc,formula_count_bom=bc,numeric_checks=len(checks),all_formula_caches_present=True,no_excel_error_cells=True,method='stdlib XLSX XML caches vs independent Python results/actualrefdes counts;not nativeExcel runtime',files=[dict(path=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in [R/'02_THREE_BOARD_POWER_BUDGET.xlsx',R/'10_BOM_RELEASE_CANDIDATE_DELTA.xlsx']])
    (E/'WORKBOOK_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
