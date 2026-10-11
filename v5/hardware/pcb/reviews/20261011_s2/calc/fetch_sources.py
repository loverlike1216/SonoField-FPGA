"""Fetch fixed public reference files; never import/execute third-party designs."""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, subprocess, urllib.request, urllib.parse, zipfile

ROOT = Path(__file__).resolve().parents[5]
EVIDENCE = ROOT / 'evidence/pcb_s2_20261011'
RAW = EVIDENCE / 'local_raw'
REPOS = {
 'sonicsurface': ('upnalab/SonicSurface','d254d69c2881c601be50e9e955a98438b94fc63a',[
  'Electronics/16x16 10mm transducers SMD PCB Gerbers/BOM.txt',
  'Electronics/16x16 10mm transducers SMD PCB Gerbers/SonicSurface1.2_2Layers_183x169.zip',
  'Firmware/FPGA primary/src/Counter.vhd','LICENSE']),
 'ultraino': ('asiermarzo/Ultraino','0d6d1f724f54ae9fdcbcc1e6d3527468f67f0715',[
  'DriverBoards/ArduinoMega64/driver board/ArduinoMEGA64-BOM.txt',
  'DriverBoards/ArduinoMega64/driver board/ArduinoMEGA64-PCB.zip',
  'DriverBoards/ArduinoMega64/firmware/DriverMEGA/DriverMEGA.ino','LICENSE']),
 'zynq': ('dylanmsu/Ultrasonic_Phased_Array','ffb8c6474fb21c2f68a00aa4c02841cf066babbc',[
  'hardware/PhasedArray5x5/PhasedArray.kicad_sch',
  'hardware/PhasedArray5x5/transducer.kicad_sch',
  'hardware/PhasedArray5x5/PhasedArray.kicad_pcb','LICENCE']),
 'homies': ('ultrasonic-homies/ultrasonic-holography','bdae32bb041f062373bf07495b261e929004a01f',[
  'pcb/rev1_altium_design_files.zip','pcb/fabrication_files.zip','final-report.pdf','LICENSE']),
 'array-v3': ('ultrasonic-phased-array/array-V3-hardware','b57070772249451d72bd629b138393ea744bb7df',['array.pdf','LICENSE']),
}
DATASHEETS = {
 'tps3851':'https://www.ti.com/lit/ds/symlink/tps3851.pdf',
 'tps54202':'https://www.ti.com/lit/ds/symlink/tps54202.pdf',
 'sn74lvc595a':'https://www.ti.com/lit/ds/symlink/sn74lvc595a.pdf',
 'tc4427a':'https://ww1.microchip.com/downloads/en/DeviceDoc/20001423J.pdf',
 'ad7606c-16':'https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf',
 'opa4192':'https://www.ti.com/lit/ds/symlink/opa4192.pdf',
 'tmux1574':'https://www.ti.com/lit/ds/symlink/tmux1574.pdf',
 'ref5025':'https://www.ti.com/lit/ds/symlink/ref50.pdf',
 'tps2663':'https://www.ti.com/lit/ds/symlink/tps2663.pdf',
 'adp7118':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf',
 'ina226':'https://www.ti.com/lit/ds/symlink/ina226.pdf',
 'tmp117':'https://www.ti.com/lit/ds/symlink/tmp117.pdf',
 'sn74axc8t245':'https://www.ti.com/lit/ds/symlink/sn74axc8t245.pdf',
 'tca9548a':'https://www.ti.com/lit/ds/symlink/tca9548a.pdf',
 'stusb4500l':'https://www.st.com/resource/en/datasheet/stusb4500l.pdf',
 'pj-002bh':'https://www.sameskydevices.com/product/resource/pj-002bh.pdf',
 'gst40a':'https://www.meanwell.com/Upload/PDF/GST40A/GST40A-SPEC.PDF',
 'gst60a':'https://www.meanwell.com/Upload/PDF/GST60A/GST60A-SPEC.PDF',
}

def fetch(job):
    label,url,dest = job
    rec = dict(id=label,url=url,queried_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'SonoField-Reference-Audit/1.0'})
        data=urllib.request.urlopen(req,timeout=25).read()
        if dest.suffix=='.pdf' and not data.startswith(b'%PDF'): raise ValueError('Not a PDF')
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        rec.update(status='FETCHED',sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),local=str(dest.relative_to(EVIDENCE)).replace('\\','/'))
        if dest.suffix=='.zip':
            with zipfile.ZipFile(dest) as z:
                rec['members']=[x.filename for x in z.infolist()]
                for member in z.infolist():
                    target=(dest.parent/(dest.stem+'_unpacked')/member.filename).resolve()
                    if not target.is_relative_to(dest.parent.resolve()) or member.is_dir():continue
                    if member.file_size>30_000_000:continue
                    target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(member))
        if dest.suffix=='.pdf':
            textpath=dest.with_suffix('.txt')
            try:
                from pypdf import PdfReader
                reader=PdfReader(dest)
                textpath.write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages)),encoding='utf-8')
                rec['text_extraction']='PYPDF_6.20.0';rec['pages']=len(reader.pages)
            except Exception as exc:
                rec['text_extraction']='FAILED';rec['extraction_error']=str(exc)
    except Exception as exc:rec.update(status='FAILED',error=str(exc))
    print(label,rec['status'],flush=True)
    return rec

def main():
    RAW.mkdir(parents=True,exist_ok=True)
    jobs=[]
    for slug,(repo,sha,paths) in REPOS.items():
        for i,path in enumerate(paths):
            url='https://raw.githubusercontent.com/'+repo+'/'+sha+'/'+urllib.parse.quote(path)
            jobs.append((slug+':'+path,url,RAW/slug/Path(path).name))
    jobs += [(name,url,RAW/'datasheets'/(name+'.pdf')) for name,url in DATASHEETS.items()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: records=list(pool.map(fetch,jobs))
    out=dict(scope='REFERENCE_ONLY_NO_THIRDPARTY_CODE_EXECUTION_OR_REUSE',repositories={k:dict(repository=v[0],commit=v[1]) for k,v in REPOS.items()},sources=records)
    (EVIDENCE/'SOURCE_FETCH_MANIFEST.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__': main()
