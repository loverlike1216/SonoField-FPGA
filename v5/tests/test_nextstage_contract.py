"""Cross-artifact contracts: catch dangerous pin ties and inconsistent assemblies."""
from pathlib import Path
import json,unittest,zipfile,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
H=ROOT/'hardware/next_stage/20261010'
class Contract(unittest.TestCase):
 def test_unused_adc_outputs_are_unconnected(self):
  pins=json.loads((H/'ADC64_PIN_CONTRACT.json').read_text());self.assertEqual([p['pin'] for p in pins],list(range(1,65)))
  for p in pins[18:22]:self.assertTrue(p['net'].startswith('NC_UNUSED_DOUT'))
  for n in [16,17,18,30,31,32,33]:self.assertEqual(pins[n-1]['net'],'AGND')
 def test_bom_and_network_references_match(self):
  bom=json.loads((H/'BOM_INPUTS.json').read_text());net=json.loads((H/'SCHEMATIC_CONTRACT.json').read_text())
  refs=[r for x in bom['items'] for rs in x['references'].values() for r in rs];self.assertEqual(len(refs),len(set(refs)));self.assertEqual(set(refs),{c['reference'] for c in net['components']})
  self.assertEqual(sum(x['quantities'][i] for x in bom['items'] if x['id']=='B-032' for i in [0,1,2]),3)
  self.assertEqual(next(x['quantities'] for x in bom['items'] if x['id']=='B-014'),[0,0,1,0,0])
  for x in bom['items']:self.assertEqual(x['quantities'][0],x['quantities'][1]);self.assertIsNone(x['unit_price'])
 def test_current_formal_adc_and_hold(self):
  current=json.loads((ROOT/'config/system_baseline.json').read_text());self.assertEqual(current['adc']['part'],'AD7606C-16BSTZ-RL');self.assertEqual(current['adc']['bandwidth_mask'],255)
  net=json.loads((H/'SCHEMATIC_CONTRACT.json').read_text());self.assertEqual(net['erc'],'NOT_RUN');self.assertEqual(net['manufacturing'],'HOLD')
  self.assertIn('.ADC_C16(1)',(ROOT/'rtl/board/nextstage_pl.v').read_text())
 def test_workbook_seven_sheets_and_formula_caches(self):
  p=ROOT/'hardware/bom/working/2026-10-10/BOM_AX7020_NU40C10T_AD7606C16_WORKING.xlsx';ns={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
  with zipfile.ZipFile(p) as z:
   w=ET.fromstring(z.read('xl/workbook.xml'));self.assertEqual([s.attrib['name'] for s in w.findall('x:sheets/x:sheet',ns)],['Review','Upper','Lower','Central','External','Source_References','Decisions'])
   s=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
   cache={c.attrib['r']:c.find('x:v',ns).text for c in s.findall('.//x:c',ns) if c.find('x:v',ns) is not None}
   self.assertEqual([int(cache[f'C{n}']) for n in range(16,20)],[488,488,83,13]);self.assertAlmostEqual(float(cache['B25']),.811008)
if __name__=='__main__':unittest.main()
