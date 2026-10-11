"""Fetch narrowly selected official S3 documents; never execute vendor code."""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, urllib.request, sys
from pypdf import PdfReader
sys.stdout.reconfigure(encoding='utf-8')
R=Path(__file__).resolve().parent.parent;ROOT=R.parents[4]
E=ROOT/'v5/evidence/pcb_s3_20261011';RAW=E/'local_raw'
TI=['tps25947','tps3430','tusb321ai','cd40109b','tmp302','sn74lvc1g74','sn74lvc1g17','sn74lvc1g08','sn74lvc1g04','tps63070','tps7a2033','tps54202','tps3851','sn74lvc595a','sn74axc8t245','ina226','tmp117','tca9548a','opa4192','ref50','tmux1574']
TI += ['tps7a20','sn74lvc244a','sn74lvc1g32']
URLS={n:'https://www.ti.com/lit/ds/symlink/'+n+'.pdf' for n in TI}
URLS.update(tc4427a='https://ww1.microchip.com/downloads/en/DeviceDoc/20001423J.pdf',ad7606c16='https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf',adp7118='https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf',gst36e='https://www.meanwell.com/Upload/PDF/GST36E/GST36E-SPEC.PDF',gst25e='https://www.meanwell.com/Upload/PDF/GST25E/GST25E-SPEC.PDF',pj002bh='https://www.sameskydevices.com/product/resource/pj-002bh.pdf',smbj='https://www.littelfuse.com/assetdocs/littelfuse-tvs-diode-smbj-datasheet?assetguid=4dd0748f-84c4-4089-9f9a-7cf1924241c5',bat54='https://assets.nexperia.com/documents/data-sheet/BAT54_SER.pdf',bss138='https://assets.nexperia.com/documents/data-sheet/BSS138.pdf',bc847='https://assets.nexperia.com/documents/data-sheet/BC847_SER.pdf')
def fetch(pair):
 name,url=pair;p=RAW/(name+'.pdf');out=dict(name=name,url=url)
 try:
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 SonoField engineering reference audit'})
   with urllib.request.urlopen(req,timeout=45) as f:b=f.read()
   if not b.startswith(b'%PDF'):raise ValueError('Not a PDF; response not retained as datasheet')
   p.write_bytes(b)
  out.update(status='DOWNLOADED',bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
  pdf=PdfReader(p);t='\n'.join('\n=== PDF PAGE '+str(i+1)+' ===\n'+(page.extract_text() or '') for i,page in enumerate(pdf.pages));(RAW/(name+'.txt')).write_text(t,encoding='utf-8');out.update(pages=len(pdf.pages),extraction='PYPDF_ACTUAL_TEXT')
 except Exception as exc:out.update(status='FAILED_RETAINED',error=type(exc).__name__+': '+str(exc))
 return out
def main():
 RAW.mkdir(parents=True,exist_ok=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(fetch,URLS.items()))
 j=dict(recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),classification='OFFICIAL_READ_ONLY_REFERENCE_NOT_HARDWARE',documents=rows)
 (E/'SOURCE_MANIFEST.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for x in rows:print(x['name'],x['status'],x.get('pages',''),x.get('error',''))
if __name__=='__main__':main()
