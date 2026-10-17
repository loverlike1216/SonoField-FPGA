"""Auditable subset reader. NOT a compliant full IBIS transient engine."""
from pathlib import Path
import re,json,numpy as np
R=Path(__file__).resolve().parents[1]
def number(s):
 s=s.strip().split('|')[0].strip()
 if s.upper()=='NA':return None
 m=re.match(r'^([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)(.*)',s)
 if not m:raise ValueError(s)
 n=float(m[1]);suffix=m[2]
 if suffix:
  scale={'f':1e-15,'p':1e-12,'n':1e-9,'u':1e-6,'m':1e-3,'k':1e3,'M':1e6,'G':1e9}.get(suffix[0],1);n*=scale
 return n
def models(path):
 text=Path(path).read_text(encoding='utf-8',errors='replace')
 chunks=re.split(r'(?im)^\[Model\]\s+',text)[1:];out={}
 for c in chunks:
  name=c.splitlines()[0].split()[0];sections={};current='HEADER'
  for line in c.splitlines()[1:]:
   line=line.split('|')[0].strip()
   if not line:continue
   if line.startswith('['):
    m=re.match(r'\[([^]]+)\](.*)',line);current=m[1].lower().replace('_',' ');sections.setdefault(current,[])
    if m[2].strip():sections[current].append(m[2].strip())
   else:sections.setdefault(current,[]).append(line)
  out[name]=sections
 return out
def table(model,section,corner='typ'):
 index={'typ':1,'min':2,'max':3}[corner];rows=[]
 for line in model.get(section.lower(),[]):
  x=line.split()
  try:
   if len(x)>=4:
    a,b=number(x[0]),number(x[index]);b=number(x[1])if b is None else b
    rows.append([a,b])
  except ValueError:pass
 a=np.array(rows,dtype=float)
 if a.size:return a[np.argsort(a[:,0])]
 return np.empty((0,2))
def scalar(model,name,corner='typ',default=None):
 key=name.lower().replace(' ','')
 for sec,lines in model.items():
  if sec.lower().replace(' ','')==key and lines:
   x=lines[0].split();return number(x[{'typ':0,'min':1,'max':2}[corner]])
  for line in lines:
   m=re.match(r'([a-zA-Z_]+)\s*(?:=|\s)\s*(.*)',line)
   if m and m[1].lower()==key:
    x=m[2].split();ix={'typ':0,'min':1,'max':2}[corner];return number(x[min(ix,len(x)-1)])
 return default
def pwl_expr(expr,rows):
 # ngspice behavioral piecewise linear function. Preserve all OEM IV rows.
 return 'pwl('+expr+','+','.join(f'{x:.9g},{y:.9g}'for x,y in rows)+')'if len(rows)else'0'
def clamp_cards(prefix,node,vcc,model,corner):
 lines=[]
 for label,arg,section in [('g',f'v({node})','gnd clamp'),('p',f'v({vcc})-v({node})','power clamp')]:
  a=table(model,section,corner)
  if len(a):
   # GND clamp has negative sink current below0. Power-clamp IBIS current
   # is referenced from Vcc; reverse sign when expressed as pad->Vcc.
   if label=='p':a=a.copy();a[:,1]*=-1
   lines.append(f'B{prefix}{label} {node} '+('0'if label=='g'else vcc)+' I='+pwl_expr(arg,a))
 return lines
if __name__=='__main__':
 names={'AX':('sources/models/zynq.ibs','LVCMOS33_F_8_HR'),'AUC_IN':('sources/models/scem333/sn74auc244.ibs','AUC244_IN_25'),'AUC_OUT':('sources/models/scem333/sn74auc244.ibs','AUC244_OUT_25'),'LVC_IN':('sources/models/scam008/sn74lvc244a.ibs','LVC244A_IN_33'),'LVC_OUT':('sources/models/scam008/sn74lvc244a.ibs','LVC244A_OUT_33'),'ALVC_IN':('sources/models/scem386/SN74ALVC244_IBIS/sn74alvc244.ibs','ALVC244_IN_33'),'ALVC_OUT':('sources/models/scem386/SN74ALVC244_IBIS/sn74alvc244.ibs','ALVC244_OUT_33')}
 out={}
 for key,(path,name)in names.items():
  m=models(R/path)[name];d=dict(model=name,source=path,c_comp=scalar(m,'c_comp'),vcc=scalar(m,'voltage range'),sections={s:len(table(m,s))for s in['pullup','pulldown','gnd clamp','power clamp','rising waveform','falling waveform']})
  d['near_0p5_IV']={s:float(np.interp(.5,table(m,s)[:,0],table(m,s)[:,1]))for s in['pullup','pulldown']if len(table(m,s))}
  out[key]=d
 (R/'results/IBIS_AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
