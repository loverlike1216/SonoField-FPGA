"""Capture bounded batches; fail closed on partial writes and retain each result."""
import argparse
import json
from pathlib import Path
from gateway import execute
from tx_design import ROOT, OUT


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--stop', type=int, default=1)
    parser.add_argument('--design', default='tx_design.json')
    args = parser.parse_args()
    design = json.loads((OUT/'project'/args.design).read_text(encoding='utf-8'))
    devices = json.loads((OUT/'device/selected_devices.json').read_text(encoding='utf-8'))
    mapping_path = OUT/'project/native_sheet_map.json'
    mapping = json.loads(mapping_path.read_text(encoding='utf-8')) if mapping_path.exists() else {'TX_UPPER_00':'d44f64bd1a3255a6'}
    capture = Path(__file__).with_name('capture_sheet.js').read_text(encoding='utf-8')
    for sheet in design['sheets'][args.start:args.stop]:
        name = sheet['name']
        if name not in mapping:
            page = execute("const id=await eda.dmt_Schematic.createSchematicPage('ac7ec8f12e696ab7');if(!id)throw new Error('Page create failed');return id;")
            mapping[name] = page
            write(mapping_path, mapping)
            execute('return await eda.dmt_Schematic.modifySchematicPageName('+json.dumps(page)+','+json.dumps(name)+');')
        opened = execute('return await eda.dmt_EditorControl.openDocument('+json.dumps(mapping[name])+');')
        if not opened:
            raise RuntimeError('Document open failed')
        for offset in range(0, len(sheet['parts']), 4):
            batch = dict(sheet, parts=sheet['parts'][offset:offset+4], notes=sheet['notes'] if offset==0 else [])
            selected = {p['key']: devices[p['key']] for p in batch['parts']}
            code = 'const sheet='+json.dumps(batch)+';const devices='+json.dumps(selected)+';'+capture
            write(OUT/f'log/review/{name}_batch_{offset:02d}_intent.json', batch)
            result = execute(code)
            write(OUT/f'log/review/{name}_batch_{offset:02d}_result.json', result)
            print(name, offset, result['componentCount'], 'saved', flush=True)
        execute('const doc=await eda.dmt_SelectControl.getCurrentDocumentInfo();await eda.dmt_EditorControl.closeDocument(doc.tabId);return await eda.dmt_EditorControl.openDocument(doc.uuid);')
        write(mapping_path, mapping)


if __name__ == '__main__':
    main()
