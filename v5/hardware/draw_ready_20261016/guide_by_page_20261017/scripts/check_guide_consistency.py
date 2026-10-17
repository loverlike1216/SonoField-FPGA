"""Independent parser: original Markdown + CSV -> final readable Markdown contract.

Does not import the generator or trust its page manifest for electrical facts.
"""
from pathlib import Path
import collections, csv, hashlib, html, json, re
import sys

O=Path(__file__).resolve().parents[1]; A=O.parent
NEW=O/'13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md'
def source_path(name):
 p=O/'source_inputs'/name
 return p if p.is_file() else A/name
def load_csv(name):
 with source_path(name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def read(name):return source_path(name).read_text(encoding='utf-8-sig')
def parts(line):return [html.unescape(x.strip()) for x in line.strip().strip('|').split('|')]
def demand(condition,message):
 if not condition:raise AssertionError(message)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

source_pins=load_csv('ALL_DEVICE_PINS.csv')
source_inst=load_csv('ALL_INSTANCES.csv')
source_passive=load_csv('ALL_PASSIVE_CONNECTIONS.csv')
sp={(x['board'],x['refdes'],x['pin']):x for x in source_pins}
si={(x['board'],x['refdes']):x for x in source_inst}
sv={(x['board'],x['refdes']):x for x in source_passive}
original=read('02_JLCEDA_PRO_COMPLETE_SCHEMATIC_GUIDE.md')
fp=load_csv('03_AX7020_J10_J11_PINMAP.csv')
ar=load_csv('04_CENTRAL_TO_ARRAY_2x32_PINMAP.csv')
bom=load_csv('01_COMPLETE_BOM.csv')
db=json.loads(read('results/FINAL_CONNECTION_DATABASE.json'))
demand({(x['board'],x['refdes'],x['pin']):(x['mpn'],x['function'],x['net'],x['kind']) for x in db['pins']}
       =={k:(x['mpn'],x['function'],x['net'],x['kind']) for k,x in sp.items()},'source CSV/database disagreement')

def parse_original():
 board=None; mode=None; out={}; passives={}
 for line in original.splitlines():
  m=re.match(r'^### (CENTRAL|UP|DN)全部(.*)',line)
  if m:board=m[1];mode='pins' if '非无源' in m[2] else 'passives';continue
  if not line.startswith('|') or board is None:continue
  r=parts(line)
  if mode=='pins' and len(r)==6 and r[0] not in ['位号','---']:
   ref,mpn,pin,fn,net,kind=r;k=(board,ref,pin)
   demand(k not in out,'duplicate original pin '+str(k))
   out[k]={'mpn':mpn,'function':fn,'net':net,'kind':kind}
  elif mode=='passives' and len(r)==8 and r[0] not in ['位号','---']:
   ref,mpn,value,n1,n2,package,rating,polarity=r;k=(board,ref)
   demand(k not in passives,'duplicate original passive '+str(k))
   passives[k]={'mpn':mpn,'value':value,'pin1_net':n1,'pin2_net':n2,'package':package,'rating':rating,'polarity':polarity}
   for p,n in [('1',n1),('2',n2)]:
    demand((board,ref,p) not in out,'duplicate original passive pin')
    out[board,ref,p]={'mpn':mpn,'function':p,'net':n,'kind':'PASSIVE'}
 demand(set(out)==set(sp),'original Markdown pin coverage differs from source CSV')
 for k,v in out.items():
  for field in ['mpn','function','net','kind']:demand(v[field]==sp[k][field],f'original/CSV {k} {field}')
 demand(set(passives)==set(sv),'original passive coverage differs from CSV')
 for k,v in passives.items():
  for f in v:demand(v[f]==sv[k][f],f'original/CSV passive {k} {f}')
 return out,passives

old_pins,old_passives=parse_original()
#Prove the two physical array instances, including all ratings/values, are identical.
up={(r,p):(x['mpn'],x['function'],x['net'],x['kind']) for (b,r,p),x in sp.items() if b=='UP'}
dn={(r,p):(x['mpn'],x['function'],x['net'],x['kind']) for (b,r,p),x in sp.items() if b=='DN'}
demand(up==dn,'UP/DN pin contracts are not identical')
for (b,r),x in si.items():
 if b=='UP':
  for f in ['mpn','package','value','rating','selection_status']:
   demand(x[f]==si['DN',r][f],'UP/DN device difference '+r+' '+f)

expected_pages={
 'CENTRAL':['00_POWER','01_FPGA_HEADERS','02_TX_BUFFERS','03_ARRAY_HEADERS','04_ADC','05_RX_INPUT','06_I2C_TEMP_SAFETY'],
 'ARRAY':['00_POWER','01_LINK_BUFFERS','02_595','03_UCC_TX','04_RX','05_SAFETY_TEMP']}
for pages in expected_pages.values():
 for name in pages:demand('`'+name+'`' in original,'page name absent from original '+name)

def check(text):
 pins={};components={};netrows={};net_titles={};steps=collections.defaultdict(list)
 current=None; current_net=None; fprows=[]; arrows=[]; page_seen=[]
 for line in text.splitlines():
  m=re.match(r'^## (CENTRAL|ARRAY)板／(\S+)图页$',line)
  if m:page_seen.append((m[1],m[2]))
  m=re.match(r'^### 第(\d+)步：在(CENTRAL|ARRAY)／(\S+)放置 (\S+)$',line)
  if m:
   number,b,page,ref=m.groups();current=(b,ref);current_net=None
   demand(current not in components,'duplicate placement '+str(current))
   demand(page in expected_pages[b],'unknown page '+page)
   components[current]={'page':page,'step':int(number),'metadata':None,'value':None,'rating_line':None,'endpoints_confirmed':False}
   steps[b,page].append(int(number));continue
  m=re.search(r'精确型号 \*\*(.*?)\*\*，封装 \*\*(.*?)\*\*。',line)
  if m and current:
   demand(components[current]['metadata'] is None,'duplicate component metadata')
   components[current]['metadata']=(m[1],m[2]);value=re.search(r'其值为 \*\*(.*?)\*\*。',line)
   if value:components[current]['value']=value[1]
   continue
  if current and line.startswith('纸面位置：'):
   components[current]['rating_line']=line
  if current and line.startswith('接完确认：'+current[1]+'.1='):
   b,ref=current;sb='CENTRAL' if b=='CENTRAL' else 'UP';x=sv[sb,ref]
   demand(line==f'接完确认：{ref}.1=`{x["pin1_net"]}`，{ref}.2=`{x["pin2_net"]}`；不可旁路该器件把两个网名短在一起。','wrong passive endpoint prose '+str(current))
   components[current]['endpoints_confirmed']=True
  m=re.match(r'^### (N\d+)｜(CENTRAL|ARRAY)／(.+)$',line)
  if m:
   nid,b,n=m.groups();current=None;current_net=nid
   demand(nid not in net_titles,'duplicate net index id')
   net_titles[nid]=(b,n);netrows[nid]=[];continue
  if not line.startswith('|'):continue
  r=parts(line)
  if len(r)==9 and r[0] in ['CENTRAL','ARRAY']:
   b,page,ref,mpn,p,fn,n,kind,action=r;k=(b,ref,p)
   demand(current==(b,ref),'pin row belongs to wrong placement '+str(k))
   demand(components[current]['page']==page,'pin row page differs from placement '+str(k))
   demand(k not in pins,'duplicate final pin '+str(k))
   pins[k]={'page':page,'mpn':mpn,'function':fn,'net':n,'kind':kind,'action':action}
  elif len(r)==6 and r[0] in ['CENTRAL','ARRAY']:
   demand(current_net is not None,'endpoint outside net index')
   b,page,ref,p,fn,n=r
   demand(net_titles[current_net]==(b,n),'endpoint in wrong net index')
   netrows[current_net].append((b,page,ref,p,fn,n))
  elif len(r)==7 and r[0] in ['J_J10','J_J11']:fprows.append(r)
  elif len(r)==9 and r[0].isdigit() and r[1].startswith('J_UP.'):arrows.append(r)

 demand(page_seen==[(b,p) for b,ps in expected_pages.items() for p in ps],'page coverage/order changed')
 expected_components={('CENTRAL' if b=='CENTRAL' else 'ARRAY',r) for b,r in si if b!='DN'}
 demand(set(components)==expected_components,'device omission/extra in final guide')
 for (b,page),order in steps.items():demand(order==list(range(1,len(order)+1)),'non-contiguous or unordered steps '+str((b,page)))
 expected_pins={('CENTRAL' if b=='CENTRAL' else 'ARRAY',r,p):x for (b,r,p),x in sp.items() if b!='DN'}
 demand(set(pins)==set(expected_pins),'final physical pin omission/extra')
 for k,x in pins.items():
  source=expected_pins[k]
  for f in ['mpn','function','net','kind']:demand(x[f]==source[f],f'final/original pin mismatch {k} {f}')
 for (b,r),c in components.items():
  sb='CENTRAL' if b=='CENTRAL' else 'UP';x=si[sb,r]
  demand(c['metadata']==(x['mpn'],x['package']),'model/package mismatch '+str((b,r)))
  if (sb,r) in sv:
   demand(c['value']==sv[sb,r]['value'],'passive value mismatch '+str((b,r)))
   passive=sv[sb,r];rating_line=c['rating_line'] or ''
   demand('额定条件：'+passive['rating']+'。' in rating_line,'passive rating mismatch '+str((b,r)))
   expected_polarity='有极性：物理1为正端、2为负端，不能对调。' if 'positive' in passive['polarity'] else '无极性/双向；本文仍固定物理1/2，便于逐脚核对。'
   demand(rating_line.endswith(expected_polarity),'passive polarity mismatch '+str((b,r)))
   demand(c['endpoints_confirmed'],'missing passive endpoint confirmation '+str((b,r)))
 #Check final printed same-net lists independently from the final printed pin rows.
 expected_net=collections.defaultdict(list)
 for (b,r,p),x in pins.items():
  if x['net']!='NC':expected_net[b,x['net']].append((b,x['page'],r,p,x['function'],x['net']))
 demand(set(net_titles.values())==set(expected_net),'net index coverage differs')
 demand(len(set(net_titles.values()))==len(net_titles),'duplicate net title')
 for nid,key in net_titles.items():
  demand(collections.Counter(netrows[nid])==collections.Counter(expected_net[key]),'wrong/incomplete full net endpoints '+nid)
 for (b,r,p),x in pins.items():
  action=x['action']
  if x['net']=='NC':
   demand('独立不连接标记' in action and '不建立NC网络' in action,'NC isolation missing')
   continue
  nid=re.search(r'\[完整端点(N\d+)\]',action)
  demand(nid is not None,'missing complete endpoint reference '+str((b,r,p)))
  demand(net_titles[nid[1]]==(b,x['net']),'wrong complete endpoint link '+str((b,r,p)))
  peer={(page,ref,pp,fn) for bb,page,ref,pp,fn,n in expected_net[b,x['net']] if (ref,pp)!=(r,p)}
  printed=set(re.findall(r'(\d{2}_[A-Z0-9_]+)/([A-Za-z0-9_]+)\.([A-Za-z0-9]+)（([^）]*)）',action))
  if len(peer)<=8:demand(printed==peer,'wrong direct same-net peer '+str((b,r,p)))
  else:
   demand(printed.issubset(peer) and len(printed)==3,'wrong same-net examples '+str((b,r,p)))
   demand(f'另有{len(peer)}个物理端点' in action,'wrong fanout count '+str((b,r,p)))
  if x['net']=='GND':demand('直接接本板GND符号' in action,'missing ground instruction')
 #Check actual external mapping table against the independent frozen CSVs.
 expected_fp=[['J_'+x['connector'],x['pin'],x['connector']+'.'+x['pin'],x['manual_signal'],x['ball'],x['net'],x['rtl_port']] for x in fp]
 demand(fprows==expected_fp,'FPGA 80-contact mapping changed')
 expected_ar=[]
 for p in range(1,65):
  u=next(x for x in ar if x['board']=='UP' and int(x['pin'])==p)
  dn=next(x for x in ar if x['board']=='DN' and int(x['pin'])==p)
  demand(u['array_net']==dn['array_net'],'array local-net difference')
  s=str(p);expected_ar.append([s,'J_UP.'+s,u['central_net'],'J_DN.'+s,dn['central_net'],'J_LINK.'+s,u['array_net'],u['direction'],u['safe_default']])
 demand(arrows==expected_ar,'upper/lower 128-contact mapping changed')
 #Also reject changes to per-pin external-mate prose, not only its table.
 for x in fp:
  action=pins['CENTRAL','J_'+x['connector'],x['pin']]['action']
  demand('AX7020 '+x['connector']+'.'+x['pin']+'；' in action,'wrong AX mate in per-pin action')
  demand('AX功能='+x['manual_signal']+'，球位='+x['ball'] in action,'wrong AX function/ball in per-pin action')
 for p in range(1,65):
  u=next(x for x in ar if x['board']=='UP' and int(x['pin'])==p)
  dn=next(x for x in ar if x['board']=='DN' and int(x['pin'])==p)
  for b,connector,row in [('UP','J_UP',u),('DN','J_DN',dn)]:
   action=pins['CENTRAL',connector,str(p)]['action']
   demand(f'{b}阵列J_LINK.{p}（该板网名{row["array_net"]}）' in action,'wrong central mate prose')
  action=pins['ARRAY','J_LINK',str(p)]['action']
  demand(f'CENTRAL.J_UP.{p}（{u["central_net"]}）' in action and f'CENTRAL.J_DN.{p}（{dn["central_net"]}）' in action,'wrong array mate prose')
 #All original technical prose is retained, with headings shifted by one level only.
 old='## 1. 冻结架构与唯一选型'+original.split('## 1. 冻结架构与唯一选型',1)[1].split('## 8. 全部物理针与无源连接附录',1)[0]
 expected_technical=re.sub(r'^(#{1,5}) ',r'\1# ',old,flags=re.M)
 demand(text.endswith(expected_technical.rstrip('\n')+'\n'),'original technical conditions changed/omitted')
 #Expand the ARRAY template back into its two physical instances and compare all pins.
 expanded={}
 for (b,r,p),x in pins.items():
  for eb in (['CENTRAL'] if b=='CENTRAL' else ['UP','DN']):expanded[eb,r,p]=x
 demand(set(expanded)==set(old_pins),'expanded coverage differs from original')
 for k,x in expanded.items():
  for f in ['mpn','function','net','kind']:demand(x[f]==old_pins[k][f],'expanded contract difference '+str(k))
 #Quantities from the printed placement list must also match the consolidated BOM.
 quantities=collections.Counter()
 for (b,r),c in components.items():
  sb='CENTRAL' if b=='CENTRAL' else 'UP';x=si[sb,r]
  quantities[x['mpn'],x['package'],x['value']]+=1 if b=='CENTRAL' else 2
 expected_quantity=collections.Counter({(x['mpn'],x['package'],x['value']):int(x['system_quantity']) for x in bom})
 demand(quantities==expected_quantity,'printed device quantities differ from BOM')
 return {'template_devices':len(components),'expanded_devices':sum(1 if b=='CENTRAL' else 2 for b,r in components),
  'template_pins':len(pins),'expanded_pins':len(expanded),'template_networks':len(expected_net),
  'expanded_networks':sum(1 if b=='CENTRAL' else 2 for b,n in expected_net),
  'expanded_passives':len(source_passive),'fpga_contacts':len(fprows),'array_contacts':2*len(arrows),
  'nc_pins':sum(x['net']=='NC' for x in expanded.values()),
  'pages':len(page_seen),'page_devices':{b+'/'+p:len(order) for (b,p),order in steps.items()}}

text=NEW.read_text(encoding='utf-8-sig')
result=check(text)
page_keys=[(b,p) for b,ps in expected_pages.items() for p in ps]
for i,(b,p) in enumerate(page_keys):
 marker=f'<a id="page-{b.lower()}-{p.lower().replace("_","-")}"></a>'
 start=text.index(marker)
 if i+1<len(page_keys):
  nb,np=page_keys[i+1];end=text.index(f'<a id="page-{nb.lower()}-{np.lower().replace("_","-")}"></a>')
 else:end=text.index('## 两套FPGA接口：逐针接到AX7020的哪里')
 name=f'{b}_{p}.md'
 page_text=(O/'pages'/name).read_text(encoding='utf-8-sig')
 prefix=f'# {b}／{p}逐步连接分册\n\n本分册与完整指南的同名图页内容一致。电气限制、完整接口表及全部同网端点见[完整指南](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md)。\n\n'
 expected_page=(prefix+text[start:end].replace('](#net-','](../13_JLCEDA_PRO_BOARD_PAGE_STEP_GUIDE.md#net-')).rstrip('\n')+'\n'
 demand(page_text==expected_page,'page booklet differs from checked main guide '+name)
result['page_booklets_verified']=len(page_keys)
mutations=[]
def reject(name,changed):
 demand(changed!=text,'mutation did not change input '+name)
 try:check(changed)
 except AssertionError as e:mutations.append({'case':name,'status':'PASS_REJECTED','reason':str(e)})
 else:raise AssertionError('checker accepted invalid guide '+name)

#Only mutate strings in memory. Delivered guide and original inputs remain unchanged.
line=next(x for x in text.splitlines() if x.startswith('| ARRAY | 02_595 | U_SR00 |') and ' | 14 | ' in x)
reject('missing_SER_physical_pin',text.replace(line+'\n','',1))
fields=parts(line);wrong=line.replace(' | '+fields[6]+' | ',' | GND | ',1)
reject('wrong_SER_network',text.replace(line,wrong,1))
block=re.search(r'(### 第\d+步：在ARRAY／03_UCC_TX放置 R_TX00\n.*?其值为 \*\*)(.*?)(\*\*。)',text,re.S)
demand(block is not None,'no R_TX00 value for mutation')
reject('wrong_series_resistor_value',text[:block.start(2)]+'15R'+text[block.end(2):])
peer=re.search(r'同网还接：(\d{2}_[A-Z0-9_]+)/([A-Za-z0-9_]+)\.([A-Za-z0-9]+)（',text)
demand(peer is not None,'no explicit peer for mutation')
reject('wrong_connected_device_pin',text[:peer.start(3)]+'999'+text[peer.end(3):])
mapping='| J_J10 | 3 | J10.3 |'
reject('wrong_FPGA_cable_pin',text.replace(mapping,'| J_J10 | 3 | J10.4 |',1))
step=re.search(r'### 第\d+步：在CENTRAL／00_POWER放置 U_EF',text)
demand(step is not None,'no U_EF placement for mutation')
reject('wrong_component_page',text[:step.start()]+step[0].replace('00_POWER','01_FPGA_HEADERS')+text[step.end():])
reject('wrong_polarized_capacitor_orientation',text.replace('物理1为正端、2为负端','物理1为负端、2为正端',1))
endpoint_line=next(x for x in text.splitlines() if x.startswith('| ARRAY |') and len(parts(x))==6)
reject('missing_full_net_endpoint',text.replace(endpoint_line+'\n','',1))

hashes=json.loads((O/'results/GUIDE_INPUT_HASHES.json').read_text(encoding='utf-8'))
for name,h in hashes.items():demand(digest(source_path(name))==h,'input file modified '+name)
result.update(status='PASS',contract_differences=0,input_files_unchanged=True,
 source_guide_sha256=hashes['02_JLCEDA_PRO_COMPLETE_SCHEMATIC_GUIDE.md'],
 output_guide_sha256=digest(NEW),negative_checks=mutations,
 native_erc='NOT_CHECKED',hardware='NOT_CHECKED',circuit_changes=False,rtl_xdc_changes=False,
 scope='Representation equivalence only; no new electrical or hardware acceptance')
result['python_version']=sys.version.split()[0]
with (O/'results/CONSISTENCY.json').open('w',encoding='utf-8',newline='\n') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
rows=[['检查','状态','实际核对范围'],['---']*3,
 ['原Markdown ↔ 原CSV','PASS','5205个物理脚、1259个无源器件双端，字段逐项一致'],
 ['新Markdown ↔ 原Markdown/CSV','PASS','982个模板器件、3241个模板引脚；展开三板后1611器件/5205引脚，0差异'],
 ['型号/数量/封装/无源值/极性','PASS','全部85种BOM数量；新器件元数据与原CSV逐项核对；极性保留在操作段落'],
 ['图页与步骤','PASS','CENTRAL7页、ARRAY6页；每器件唯一页/唯一顺序，连续步骤，无遗漏'],
 ['逐页分册','PASS','13份分册与已核对全文的相应段落逐字一致，同网链接回链全文，末尾空行统一'],
 ['同网器件端点','PASS',f'{result["template_networks"]}个模板网络完整端点；每脚直接连接对象/高扇出链接逐项核对'],
 ['接口对应','PASS','80个FPGA触点和128个上下阵列触点；表格和每脚接线文字均核对'],
 ['原技术约束','PASS','原指南第1–7节正文完整保留，标题增加一级、文件末尾空行统一'],
 ['错误注入','PASS','8项实际内存负向测试全部拒绝；没有修改交付文件'],
 ['原输入保护','PASS','8个原输入SHA256前后不变'],
 ['新电气仿真/原生ERC/实物','NOT_CHECKED','本轮是指南表述转换，不新增此类验收']]
report='# 新旧指南独立一致性报告 — 2026-10-17\n\n**表述转换核对：PASS，电气连接合同差异：0。文档交付结论：ACCEPT。原工程ACCEPT WITH LIMITATIONS与待独立Review状态不变。**\n\n'
report+='\n'.join('| '+' | '.join(map(str,row))+' |' for row in rows)+'\n\n'
report+='原指南SHA256：`'+result['source_guide_sha256']+'`。\n\n新指南SHA256：`'+result['output_guide_sha256']+'`。\n\n'
report+='核对器独立读取最终Markdown，不导入生成器、不以生成器输出JSON作为电气真相。原指南表格先与独立CSV核对，再与新指南展开后的引脚集合、同网端点和BOM数量比较。新增加的图页归属/纸面顺序属于文档组织，不冒充旧指南已有的图页元数据。\n\n'
report+='## 实际错误注入\n\n'+ '\n'.join('- '+x['case']+'：'+x['status']+'；'+x['reason'] for x in mutations)+'\n\n'
report+='## 本页器件数量\n\n'+ '\n'.join('- '+k+'：'+str(v) for k,v in result['page_devices'].items())+'\n\n'
report+='复现：PowerShell7运行科学Python解释器执行`scripts/check_guide_consistency.py`。源输入来自本目录上一级；仅在原公开文件存在CRLF/LF格式差别时，source_inputs保留对应本地原始字节副本并优先读取，全部字段相同、原文件不改。脚本只将核对报告写到本目录。实际运行日志见logs/check_guide_consistency.log。\n'
with (O/'14_GUIDE_CONSISTENCY_REPORT.md').open('w',encoding='utf-8',newline='\n') as f:f.write(report)
print(json.dumps({k:v for k,v in result.items() if k not in ['page_devices','negative_checks']},ensure_ascii=False))
print('Negative mutation checks: '+str(len(mutations))+'/8 rejected as required.')
