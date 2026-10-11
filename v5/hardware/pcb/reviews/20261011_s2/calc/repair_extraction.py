"""Keep original failed attempt; extract downloaded PDFs, fetch missing primary files."""
from pathlib import Path
import datetime,hashlib,json,urllib.request
from pypdf import PdfReader
import fetch_sources as fs
def main():
    manifest=json.loads((fs.EVIDENCE/'SOURCE_FETCH_ATTEMPT1.json').read_text(encoding='utf-8'))
    for rec in manifest['sources']:
        if 'local' not in rec:continue
        p=fs.EVIDENCE/rec['local']
        if not p.exists():continue
        rec['download_status']='FETCHED';rec['status']='FETCHED'
        if p.suffix=='.pdf':
            r=PdfReader(p)
            p.with_suffix('.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+(page.extract_text() or '') for i,page in enumerate(r.pages)),encoding='utf-8')
            rec['text_extraction']='PYPDF_6.20.0';rec['pages']=len(r.pages)
            rec['initial_extraction_error']=rec.pop('error',None)
    jobs=[('ref5025',fs.DATASHEETS['ref5025'],fs.RAW/'datasheets/ref5025.pdf'),
          ('zynq:LICENCE','https://raw.githubusercontent.com/dylanmsu/Ultrasonic_Phased_Array/'+fs.REPOS['zynq'][1]+'/LICENCE',fs.RAW/'zynq/LICENCE')]
    manifest['sources'] += [fs.fetch(j) for j in jobs]
    manifest['extraction_tool']='pypdf==6.20.0';manifest['original_attempt']='SOURCE_FETCH_ATTEMPT1.json'
    (fs.EVIDENCE/'SOURCE_FETCH_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PDF extraction complete; initial failure preserved')
if __name__=='__main__':main()
