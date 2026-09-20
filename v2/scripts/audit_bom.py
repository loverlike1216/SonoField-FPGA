"""Audit the documentary XLSX/CSV import with an independent standard-library reader.

This script is a provenance check, not a runtime dependency or an electrical BOM qualification.
"""
import csv
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def main():
    bom = ROOT / 'hardware/bom'
    manifest = json.loads((bom / 'import_manifest.json').read_text(encoding='utf-8'))
    source = bom / 'BOM_MASTER.xlsx'
    assert hashlib.sha256(source.read_bytes()).hexdigest() == manifest['sha256']
    counts = {}
    with zipfile.ZipFile(source) as z:
        assert not any('externalLink' in n or 'vbaProject' in n for n in z.namelist())
        shared = []
        if 'xl/sharedStrings.xml' in z.namelist():
            shared = [''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        rels = {e.attrib['Id']: e.attrib['Target'] for e in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        sheets = ET.fromstring(z.read('xl/workbook.xml')).find('s:sheets', NS)
        for sheet in sheets:
            name = sheet.attrib['name']
            rid = sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
            target = rels[rid]
            path = target.lstrip('/') if target.startswith('/') else 'xl/' + target
            cells = {}
            for cell in ET.fromstring(z.read(path)).findall('.//s:sheetData/s:row/s:c', NS):
                assert cell.find('s:f', NS) is None, 'Formula import requires explicit handling'
                kind = cell.get('t')
                if kind == 'inlineStr': value = ''.join(cell.find('s:is', NS).itertext())
                else:
                    v = cell.find('s:v', NS)
                    value = '' if v is None else v.text or ''
                    if kind == 's': value = shared[int(value)]
                if value: cells[cell.attrib['r']] = value
            rows = list(csv.reader((bom / 'source_sheets' / (name + '.csv')).open(encoding='utf-8', newline='')))
            exported = {}
            for y, row in enumerate(rows, 1):
                for x, value in enumerate(row, 1):
                    n, label = x, ''
                    while n:
                        n, r = divmod(n - 1, 26); label = chr(65 + r) + label
                    if value: exported[label + str(y)] = value
            assert cells == exported, 'Cell mismatch: ' + name
            counts[name] = len(cells)
    master = list(csv.DictReader((bom / 'BOM_MASTER.csv').open(encoding='utf-8', newline='')))
    assert len(master) == manifest['master_data_rows'] == 65
    for row in master:
        total = int(row['Qty/Array PCB']) * int(row['Array PCBs']) + sum(int(row[k]) for k in ('Qty/ADC PCB', 'Qty/Sensor PCB', 'Qty/External'))
        assert total == int(row['Installed Total']), row['MPN']
    print(json.dumps({'status': 'PASS', 'xlsx_sha256': manifest['sha256'], 'sheets': counts,
                      'master_rows': len(master), 'quantity_checks': len(master),
                      'scope': 'Exact nonempty source cells and arithmetic only; NOT electrical, price, stock or footprint validation'}, indent=2))


if __name__ == '__main__':
    main()
