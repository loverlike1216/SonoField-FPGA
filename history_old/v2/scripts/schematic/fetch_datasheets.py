"""Cache primary datasheets locally; retain provenance, never claim review from download."""
from pathlib import Path
import concurrent.futures, hashlib, json, urllib.request
import fitz

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / 'PCB/V1/log/datasheet/vendor_files'
DEST.mkdir(parents=True, exist_ok=True)
SOURCES = {n: f'https://www.ti.com/lit/ds/symlink/{n}.pdf' for n in
           ('sn74lvc595a', 'sn74axc8t245', 'sn74lvc244a', 'sn74lvc1g32',
            'tmux1574', 'opa4192', 'ref5025', 'tps25947', 'ina226', 'tmp117')}
SOURCES.update({
 'tc4427a':'https://ww1.microchip.com/downloads/en/DeviceDoc/20001423J.pdf',
 'ad7606b':'https://www.analog.com/media/en/technical-documentation/data-sheets/AD7606B.pdf',
 'adp7118':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf',
 'ap63200':'https://www.diodes.com/assets/Datasheets/AP63200-AP63201-AP63203-AP63205.pdf',
 'bat54s':'https://www.nexperia.com/assets/documents/data-sheet/BAT54_SER.pdf',
 'ug1225':'https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad7606bfmcz-ug-1225.pdf',
 'ug933':'https://docs.amd.com/api/khub/documents/emfVNNoDnc5paYCtwGzwPg/content',
 'cn0148':'https://www.analog.com/media/en/reference-design-documentation/reference-designs/CN0148.pdf',
})

def fetch(item):
    name, url = item
    row = dict(id=name, url=url, review='PENDING', source='MANUFACTURER')
    try:
        path = DEST / (name+'.pdf')
        if not path.exists():
            data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=35).read()
            if not data.startswith(b'%PDF'): raise ValueError('Not PDF')
            path.write_bytes(data)
        data = path.read_bytes()
        doc = fitz.open(path)
        (DEST/(name+'.txt')).write_text('\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)), encoding='utf-8')
        row.update(status='DOWNLOADED', sha256=hashlib.sha256(data).hexdigest(), pages=len(doc), bytes=len(data))
    except Exception as exc:
        row.update(status='DOWNLOAD_FAILED', error=str(exc))
    return row

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        rows = list(pool.map(fetch, SOURCES.items()))
    (DEST.parent/'sources.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
    print('\n'.join(r['id']+': '+r['status'] for r in rows))
