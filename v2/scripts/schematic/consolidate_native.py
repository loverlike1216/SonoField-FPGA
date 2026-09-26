"""Merge official exported EasyEDA source into one schematic, then require native import/audit.

Only schematic-page coordinates/IDs/presentation change. Library documents and circuit
properties are retained. This edits an interchange export, NEVER the live project database.
Format authority: easyeda-api skill format/{project,schematic}.
"""
import copy
import json
import uuid
import zipfile
from collections import Counter
from pathlib import Path
from tx_design import OUT

TITLE='SonoField-FPGA-v2-Schematic-V1-SingleSheet'
PAGE='9c868d72bd925c50'


def records(text):
    for line in text.splitlines():
        if not line.strip(): continue
        a,b=line.split('||',1); b=b.removesuffix('|')
        yield json.loads(a),json.loads(b) if b else None


def encode(items):
    return '\n'.join(json.dumps(h,ensure_ascii=False,separators=(',',':'))+'||'+
            (json.dumps(b,ensure_ascii=False,separators=(',',':')) if b is not None else '')+'|' for h,b in items)+'\n'


def build():
    designs=[json.loads((OUT/'project'/f).read_text(encoding='utf-8')) for f in
             ['tx_design.json','system_design.json','power_design.json']]
    sheets={s['name']:s for d in designs for s in d['sheets']}
    mapping=json.loads((OUT/'project/native_sheet_map.json').read_text(encoding='utf-8'))
    by_id={v:k for k,v in mapping.items()}
    z=zipfile.ZipFile(OUT/'log/review/SonoField_modular_checkpoint.epro2')
    source=z.read(next(n for n in z.namelist() if n.endswith('.epru'))).decode()
    docs=[]
    for h,b in records(source):
        if h['type']=='DOCHEAD':docs.append([])
        docs[-1].append((h,b))
    assert sum(d[0][1]['docType']=='SCH_PAGE' for d in docs)==len(sheets)==83
    assert not any(d[0][1]['docType']=='PCB' for d in docs)
    placement={}
    def grid(names,col,row,columns):
        for i,n in enumerate(names):placement[n]=(col+i%columns,row+i//columns)
    grid([f'TX_UPPER_{i:02d}' for i in range(16)],0,0,4)
    grid([f'TX_LOWER_{i:02d}' for i in range(16)],9,0,4)
    digital=[n for n in sheets if n.startswith(('SERIALIZER','CLOCK_ENABLE','LEVEL_'))]+['ADC_AD7606B']
    grid(digital,4,0,5)
    rx=[n for n in sheets if n.startswith(('REFERENCE_','RX_BLANK_','AFE_'))]
    grid(rx,0,4,6)
    power=[n for n in sheets if n.startswith('POWER_')]
    grid(power,6,4,5)
    grid([f'FPGA_CORE_INTERFACE_{i}' for i in range(4)]+['SYSTEM_REFERENCE_AND_ENVIRONMENT'],11,4,2)
    assert set(placement)==set(sheets)
    assert len(set(placement.values()))==len(placement)
    cw,ch=1200,900
    def tilexy(n):
        col,row=placement[n]
        return col*cw+50, row*ch+250+(150 if row>=4 else 0)
    merged=[];retained=[];audit=[]
    for d in docs:
        typ=d[0][1]['docType']
        if typ!='SCH_PAGE':
            if typ=='CONFIG':
                for h,b in d:
                    if h['type']=='META' and b:b['defaultSheet']=PAGE
            if typ in ['SCH','BOARD']:
                for h,b in d:
                    if h['type']=='META' and b:b['title']='SonoField 全系统原理图'
            # Keep library attributes and symbols, strip account identity metadata.
            for h,b in d:
                if b and h['type']=='DOCHEAD':b.pop('user',None)
                if h['type'] not in ['META_CREATE','META_MODIFY']:retained.append((h,b))
            continue
        pid=d[0][1]['uuid'];name=by_id[pid];sheet=sheets[name]
        alive=[(h,b) for h,b in d if b is not None]
        refs={b['parentId']:b['value'] for h,b in alive if h['type']=='ATTR' and b.get('key')=='Designator'}
        expected={p['ref'] for p in sheet['parts']}
        keep={i for i,r in refs.items() if r in expected}
        assert {refs[i] for i in keep}==expected,(name,'source missing parts')
        remove={h['id'] for h,b in alive if h['type']=='COMPONENT' and h['id'] not in keep}
        ids={h['id']:uuid.uuid5(uuid.NAMESPACE_URL,PAGE+'/'+pid+'/'+h['id']).hex[:16]
             for h,b in alive if h.get('id') and h['type'] not in ['DOCHEAD','META','CANVAS','ELE_PLACEHOLDER']}
        ox,oy=tilexy(name); dx=ox;dy=oy+850
        def change(value):
            if isinstance(value,str):
                if value in ids:return ids[value]
                if value[:16] in ids:return ids[value[:16]]+value[16:]
            if isinstance(value,list):return [change(x) for x in value]
            if isinstance(value,dict):return {k:change(v) for k,v in value.items()}
            return value
        count=0
        for h,b in alive:
            if h['type'] in ['DOCHEAD','META','META_CREATE','META_MODIFY','CANVAS','ELE_PLACEHOLDER','TEXT']:continue
            if h.get('id') in remove or b.get('parentId') in remove:continue
            # Discard stray page/global net-label annotations; electrical NET attrs remain on wires.
            if h['type']=='ATTR' and b.get('parentId')=='$$root':continue
            h,b=change(copy.deepcopy(h)),change(copy.deepcopy(b))
            h.pop('firstTicket',None)
            for k in ['x','startX','endX','positionX','dotX1','dotX2','centerX']:
                if isinstance(b.get(k),(int,float)):b[k]+=dx
            for k in ['y','startY','endY','positionY','dotY1','dotY2','centerY']:
                if isinstance(b.get(k),(int,float)):b[k]+=dy
            if h['type']=='POLY' and 'points' in b:
                b['points']=[v+(dx if i%2==0 else dy) for i,v in enumerate(b['points'])]
            if h['type']=='ATTR':
                key=b.get('key')
                if key=='NET':
                    if b.get('rotation')==90:
                        b['x']+=6;b['y']+=5;b['align']='LEFT_TOP'
                    b['rotation']=0;b['fontSize']=7
                    # Long ADC control labels must stop before pin numbers/body.
                    if name=='ADC_AD7606B' and b['x']==ox+395 and oy+225<=b['y']<=oy+545:
                        b['x']=ox+422;b['align']='RIGHT_BOTTOM'
                    if name.startswith('LEVEL_') and b['x']==ox+345:
                        b['x']=ox+370;b['align']='RIGHT_BOTTOM'
                elif key in ['Designator','Name'] and b.get('valueVisible'):
                    b['fontSize']=7 if key=='Designator' else 6;b['rotation']=0
                elif key=='Unique ID':b['value']='SF_'+b['parentId']
            if h['type']=='COMPONENT':count+=1
            merged.append((h,b))
        assert count==len(expected)
        audit.append({'module':name,'components':count,'column':placement[name][0],'row':placement[name][1]})
    def add(typ,body):
        identity=uuid.uuid5(uuid.NAMESPACE_URL,PAGE+typ+str(len(merged))).hex[:16]
        merged.append(({'type':typ,'id':identity},body))
    def text(x,y,value,size=16,color='#142C54',bold=False):
        add('TEXT',dict(partId='',groupId='',locked=True,zIndex=99999,x=x,y=y,
            rotation=0,value=value,color=color,fillColor='',fontFamily='Microsoft YaHei',fontSize=size,
            strikeout=False,underline=False,italic=False,fontWeight=bold,align='LEFT_TOP'))
    def rect(x,y,w,h,width=3):
        add('RECT',dict(partId='',groupId='',locked=True,zIndex=0,dotX1=x,dotY1=y,dotX2=x+w,dotY2=y+h,
            radiusX=0,radiusY=0,rotation=0,strokeColor='#244BC1',strokeStyle=0,fillColor='',strokeWidth=width,fillStyle=0))
    for name,sheet in sheets.items():
        ox,oy=tilexy(name)
        rect(ox,oy,cw,ch,1.5)
        text(ox+25,oy+18,name,19,bold=True)
        for i,note in enumerate(sheet['notes'][1:]):text(ox+25,oy+48+15*i,note,8)
    text(50,20,'SonoField-FPGA | 128 TX / 8 RX | 单张全系统原理图',55,bold=True)
    text(50,100,'项目 v2 · 原理图 V1 · 12 mm 辐射面中心间距 · 100 mm 上下面间距（90–115 mm 可调）',26)
    text(50,150,'设计草案 / DRAFT · 未确认 FPGA 引脚及 VCCO 不作分配 · B04 时序及独立失钟保护待闭环 · 仅原理图',22,'#A52A2A')
    for x,label in [(50,'上阵列：64 路发射'),(4*cw+50,'数字串行、电平转换与 ADC'),(9*cw+50,'下阵列：64 路发射')]:
        text(x,205,label,30,bold=True)
    bottom=4*ch+340
    for x,label in [(50,'8 路接收：放大、偏置与消隐'),(6*cw+50,'分域电源与电流／温度监测'),(11*cw+50,'核心板逻辑接口及环境')]:text(x,bottom,label,28,bold=True)
    x,y=tilexy('REFERENCE_U');legend_y=6*ch+430
    text(90,legend_y,'网络与安全边界',32,bold=True)
    for i,t in enumerate([
        '所有 128 个发射通道均展开：UPPER_TX_00…63 / LOWER_TX_00…63；不使用代表通道替代。',
        '同名网络电气相连；分区蓝色实线仅为图形边界，不是导线。网络名按 EDA 大写规范导出。',
        'SERIAL_DATA[0…31] 对应 RTL serial_data[0…31]；每 lane 按 bit3→bit0 移入 QA…QD。',
        '接收映射：上 RX0…3 → ADC0…3；下 RX0…3 → ADC4…7。',
        'TP_CORE_* 是逻辑端点，不是已确认的核心板连接器脚号。供电及 FPGA VCCO 必须先核实。',
        'KILL 与 LEVEL_OE_N 默认禁止输出；独立 watchdog / power-good 尚待决策，禁止直接投板。',
        '通用无源器件和换能器为符号模板；Value 有效，MPN_TBD 表示尚未完成采购料号资格确认。',
        '完整校核结果见 PCB/V1/log/review；仿真与网表核对不等于实物验证。']):text(90,legend_y+60+32*i,t,18)
    header=[({'type':'DOCHEAD'},{'docType':'SCH_PAGE','uuid':PAGE,'client':'SonoField','editVersion':'3.2.149.88089769'}),
            ({'type':'META','id':'META'},{'title':'SonoField 全系统原理图','schematic':'ac7ec8f12e696ab7','source':'','zIndex':1})]
    for i,(h,b) in enumerate(header+merged,1):h['ticket']=i
    header[0][0]['ticket']=len(header+merged)
    native=encode(retained+header+merged)
    result=OUT/'project'/f'{TITLE}.epro2'
    with zipfile.ZipFile(result,'w',zipfile.ZIP_DEFLATED) as out:
        meta=json.loads(z.read('project2.json'));meta['title']=TITLE
        out.writestr('project2.json',json.dumps(meta,ensure_ascii=False))
        out.writestr(TITLE+'.epru',native)
    report={'status':'INTERCHANGE_GENERATED_NATIVE_IMPORT_REQUIRED','page_uuid':PAGE,'modules':audit,
            'components':sum(a['components'] for a in audit),'sheet_count':1,'pcb_count':0,
            'source_snapshot':'SonoField_modular_checkpoint.epro2','output':result.name}
    (OUT/'log/review/consolidation_transform.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(result,len(native.encode()),'source bytes;',report['components'],'components')


if __name__=='__main__':build()
