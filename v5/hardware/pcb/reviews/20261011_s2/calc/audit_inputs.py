"""Read-only workbook/contract and public native-KiCad audit; no CAD execution."""
from pathlib import Path
import collections, hashlib, json, re, sys, zipfile, xml.etree.ElementTree as ET
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[5]
OUT=ROOT/'evidence/pcb_s2_20261011'
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def workbook():
    p=ROOT/'hardware/bom/working/2026-10-11/BOM_V5_FOUR_SOURCE_20261011.xlsx'
    with zipfile.ZipFile(p) as z:
        strings=[''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',NS)] if 'xl/sharedStrings.xml' in z.namelist() else []
        sheets=[]
        for i,s in enumerate(ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',NS),1):
            rows=[]
            for row in ET.fromstring(z.read(f'xl/worksheets/sheet{i}.xml')).findall('s:sheetData/s:row',NS):
                cells={}
                for c in row:
                    v=c.find('s:v',NS);f=c.find('s:f',NS)
                    value=v.text if v is not None else ''
                    if c.get('t')=='s':value=strings[int(value)]
                    if c.get('t')=='inlineStr':value=''.join(c.find('s:is',NS).itertext())
                    cells[c.get('r')]=dict(value=value,formula=f.text if f is not None else None)
                rows.append(cells)
            sheets.append(dict(name=s.get('name'),rows=rows))
    data=dict(path=str(p.relative_to(ROOT)),sha256=sha(p),sheets=sheets)
    (OUT/'WORKBOOK_XML_AUDIT.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return data
def parse_sexp(text):
    toks=re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',text)
    stack=[[]]
    for tok in toks:
        if tok=='(':obj=[];stack[-1].append(obj);stack.append(obj)
        elif tok==')':stack.pop()
        else:stack[-1].append(tok[1:-1] if tok.startswith('"') else tok)
    return stack[0][0]
def children(node,key):return [x for x in node if isinstance(x,list) and x and x[0]==key]
def kicad():
    result=[]
    for p in (OUT/'local_raw/zynq').glob('*.kicad_sch'):
        tree=parse_sexp(p.read_text(encoding='utf-8'))
        symbols=[]
        for symbol in children(tree,'symbol'):
            props={x[1]:x[2] for x in children(symbol,'property')}
            symbols.append(props)
        result.append(dict(file=p.name,sha256=sha(p),symbols=symbols,
          labels=[x[1] for k in ['label','global_label','hierarchical_label'] for x in children(tree,k)],
          wires=len(children(tree,'wire')),sheets=[{x[1]:x[2] for x in children(s,'property')} for s in children(tree,'sheet')]))
    (OUT/'KICAD_REFERENCE_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result
if __name__=='__main__':
    w=workbook()
    print('WORKBOOK',w['sha256'])
    for s in w['sheets']:
        print(s['name'],len(s['rows']))
        print('first item',[(k,v['value']) for k,v in s['rows'][4].items() if k[0] in 'ACEG'])
    k=kicad()
    for x in k:print('KICAD',x['file'],'symbols',len(x['symbols']),'wires',x['wires'],'sheets',len(x['sheets']))
    items=json.loads((ROOT/'hardware/design_20261011/BOM_INPUTS.json').read_text(encoding='utf-8'))['items']
    print('ITEMS',len(items),'COUNTS',[sum(x['quantities'][i] for x in items) for i in range(5)])
    for x in items: print(x['id'],x['description'],x['mpn'],x['quantities'])
