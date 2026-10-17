from pathlib import Path
import json,csv,hashlib,shutil,re,requests
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parents[1];d=json.loads((R/'results/FINAL_CONNECTION_DATABASE.json').read_text(encoding='utf-8'))
dest=R/'sources/user_attachments';dest.mkdir(exist_ok=True)
base=Path('E:/Codex_project/AMD_Sonofield/BOM')
for p in base.glob('*.pdf'):
 if any(s in p.name.lower()for s in ['22435680','nu40','6731413']):shutil.copy2(p,dest/p.name)
urls=sorted({x['source_url']for x in d['bom']if x['source_url'].lower().endswith('.pdf')}|{'https://industrial.panasonic.com/cdbs/www-data/pdf/AAB8000/AAB8000C177.pdf','https://www.ti.com/lit/ds/symlink/tmp117.pdf','https://www.ti.com/lit/ds/symlink/tps25947.pdf','https://www.ti.com/lit/ds/symlink/ucc27624-q1.pdf'})
rows=[]
def get(url):
 p=(R/'sources/user_attachments'/url.rsplit('/',1)[-1]) if url.startswith('inputs/') else R/'sources/final_primary'/url.rsplit('/',1)[-1];p.parent.mkdir(exist_ok=True)
 try:
  if not p.exists():
   q=requests.get(url,timeout=35);q.raise_for_status();assert q.content.startswith(b'%PDF');p.write_bytes(q.content)
  return dict(url=url,path=str(p.relative_to(R)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),status='AVAILABLE_PDF')
 except Exception as e:return dict(url=url,path='',sha256='',status='HOLD_RETRIEVAL:'+str(e)[:120])
with ThreadPoolExecutor(max_workers=6)as pool:rows=list(pool.map(get,urls))
(R/'results/FINAL_PRIMARY_RETRIEVAL.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
files=[]
for p in(R/'sources').rglob('*'):
 if p.is_file():files.append(dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),redistribution='LOCAL_RESEARCH_ONLY_OEM_LICENSE_NOT_ASSUMED'))
with(R/'SOURCE_FILE_MANIFEST.csv').open('w',encoding='utf-8-sig',newline='')as f:w=csv.DictWriter(f,fieldnames=list(files[0]));w.writeheader();w.writerows(files)
mapping={x['url']:x for x in rows};parts=[]
for x in d['bom']:
 ev=mapping.get(x['source_url'],{})
 parts.append(dict(mpn=x['mpn'],manufacturer=x['manufacturer'],package=x['package'],rating=x['rating'],primary_url=x['source_url'],download=ev.get('path','See SOURCE_FILE_MANIFEST / prior_primary / user_attachments; manufacturer catalog for passive series'),retrieval_status=ev.get('status','PRIMARY_REFERENCE_INDEXED; exactprocurementmapping_notchecked'),sha256=ev.get('sha256',''),evidence_scope='Datasheet/catalog/physicalpin contract; simulation limits stated separately'))
with(R/'COMPONENT_DATASHEET_INDEX.csv').open('w',encoding='utf-8-sig',newline='')as f:w=csv.DictWriter(f,fieldnames=list(parts[0]));w.writeheader();w.writerows(parts)
text='# 原厂资料、模型与证据索引\n\n逐型号见COMPONENT_DATASHEET_INDEX.csv，所有本地源文件的SHA256见SOURCE_FILE_MANIFEST.csv；工具原始证据见results和logs。PDF/IBIS保存在本地审核目录，公开仓库只放来源、hash和审查结论，不自动再分发厂家模型。\n\n'
text+='## 每个BOM型号\n\n| MPN | 封装 | 依据 | 本地文件/状态 |\n|---|---|---|---|\n'
for x in parts:text+=f"| {x['mpn']} | {x['package']} | {x['primary_url']} | {x['download']} / {x['retrieval_status']} |\n"
text+='\n## AX7020与开源参考\n\nAX7010_AX7020管脚.xlsx由用户提供，rawXML保存在results/VENDOR_XLSX_CELLS.json；手册V3.0第9、29–32页用于供电、排阻与接口。当前用户补充型号XC7Z020-2CLG400I，JTAG仅验证Z020 ID，不验证后缀。\n\nVDATP参考 https://github.com/danfoisy/vdatp ，此前已独立解析638个元件、2131节点；来源commit58a278fbe77dea22ac073acab2e36f4782a046b3，CERN-OHL-Pv2，原始License和errata保留在上一审核目录。仅用作结构、退耦和驱动对照，未复制其RTL作为本项目实现，也不继承其器件驱动电压。细节追溯上一目录results/VDATP_PROVENANCE.json与VDATP_*导出。\n\n嘉立创EDA专业版操作参考 https://prodocs.lceda.cn/ 。本次不调用EDA画图或修改已有工程。\n\n## 模型级别\n\nZynq、LVT等OEM IBIS文件的I/V、C_comp与封装RLC经脚本提取；有限边沿权重为工程近似，未完成全动态多夹具IBIS拟合、实际SSO/板PDN/EMI验证。595无已取得OEM IBIS，使用10pF/输入及数据手册判据。ADC为独立数字行为模型，BUCK是数据手册静态/补偿核算，PMOS为通用等效SPICE，NU为未拟合BVD。全部均非实物测试。\n'
(R/'12_DATASHEET_EVIDENCE_INDEX.md').write_text(text,encoding='utf-8')
print(json.dumps(dict(source_files=len(files),bom_models=len(parts),downloaded=sum(x['status']=='AVAILABLE_PDF'for x in rows),retrieval_hold=[x['url']for x in rows if x['status']!='AVAILABLE_PDF'])))
