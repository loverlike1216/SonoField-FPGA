"""Independent acceptance assertions over real saved outputs and current sources."""
from pathlib import Path
import json,csv,hashlib,re
R=Path(__file__).resolve().parents[1];V=Path('E:/Codex_project/AMD_Sonofield/v5')
def j(p):return json.loads((R/p).read_text(encoding='utf-8-sig'))
def test_connection_and_quantity_census():
 d=j('results/FINAL_CONNECTION_DATABASE.json');a=j('results/INDEPENDENT_CONSISTENCY_FINAL.json')
 assert a['status']=='PASS' and a['fpga_contacts']==80 and a['array_contacts']==128
 assert len(d['pins'])==len({(x['board'],x['refdes'],x['pin'])for x in d['pins']})==5205
 assert sum(x['system_quantity']for x in d['bom'])==len(d['instances'])==1611
 assert len(d['passives'])==1259
def test_all_selected_SI_corners_jointly_pass():
 a=j('results/SELECTED_FINAL_SI_INDEPENDENT.json');assert len(a)==90
 for x in a:
  assert x['independent_status']=='PASS' and x['model_joint_status']=='PASS'
  assert x['independent_setup_ns']>=3.2 and x['independent_hold_ns']>=2.2
  assert x['independent_pulse_ns']>=5.2 and x['independent_latch_ns']>=3.2
 assert all(x['status']=='PASS'for x in j('results/CONVERGENCE_FINAL.json'))
def test_actual_native_route_and_io_boundaries():
 label=(R/'results/FINAL_NATIVE_LABEL.txt').read_text().strip()
 text=(R/f'results/{label}/NATIVE_IMPLEMENTATION_STATUS.txt').read_text()
 assert float(re.search(r'SETUP ([-.\d]+)',text)[1])>=0
 assert float(re.search(r'HOLD ([-.\d]+)',text)[1])>=0
 assert 'Checks found: 0'in(R/f'results/{label}/NATIVE_ROUTED_DRC.rpt').read_text()
 assert 'xc7z020clg400-2'in(R/f'results/{label}/NATIVE_ROUTED_DRC.rpt').read_text()
 a=list(csv.DictReader((R/f'results/{label}_final/PAD_DELAY.csv').open()))
 for key in ['max_ns','min_ns']:assert max(float(x[key])for x in a)-min(float(x[key])for x in a)<=.5
def test_final_source_hash_matches_implementation_input():
 for rel,h in j('results/FINAL_NATIVE_SOURCE_MANIFEST.json').items():assert hashlib.sha256((V/rel).read_bytes().replace(b'\r\n',b'\n')).hexdigest()==h,rel
def test_physical_adc_and_atomic_production_profile():
 a=j('results/capture_adc_final/summary.json');assert a['status']=='PASS'
 assert all(x['signed_frames']==2048 for x in a['runs'])
 assert a['runs'][0]['trace_sha256']==a['runs'][1]['trace_sha256']
 a=j('results/production_profile_adc_final_fixed/summary.json');assert all(x['status']=='PASS'for x in a)
 assert a[0]['ack_sha256']==a[1]['ack_sha256']
 p=json.loads((V/'config/draw_ready_profile.json').read_text());assert (p['adc_sclk_divider'],p['adc_sample_period_core_cycles'],p['adc_sample_rate_hz'])==(16,320,400000)
def test_real_digital_and_electrical_checks():
 assert all(x['status']=='PASS'for x in j('results/final_digital_qualified_final/summary.json'))
 assert all(x['status']=='PASS'for x in j('results/ELECTRICAL_FINAL_CHECKS.json'))
 assert j('results/BVD_FINAL.json')['refined']['vpp_v']<20
 p=j('results/ADC_FINAL_TIMING_BUDGET.json');assert p['minimum_pulse_bound_ns']>=p['required_pulse_ns']+.5
 assert p['cs_hold_bound_ns']>=p['required_cs_hold_ns']+.5
def test_no_power_or_ground_contact_stolen():
 a=list(csv.DictReader((R/'03_AX7020_J10_J11_PINMAP.csv').open(encoding='utf-8-sig')))
 for x in a:
  p=int(x['pin'])
  if p in(1,37,38):assert x['net']=='GND'and not x['rtl_port']
  if p in(2,40)or(p==39 and x['connector']=='J10'):assert x['net']=='NC'and not x['rtl_port']
  if p==39 and x['connector']=='J11':assert x['net']=='AX_VIO_REF3V3'and not x['rtl_port']
 a=list(csv.DictReader((R/'04_CENTRAL_TO_ARRAY_2x32_PINMAP.csv').open(encoding='utf-8-sig')));assert len(a)==128
 assert all(x['central_net']==x['array_net']=='GND'for x in a if int(x['pin'])%2==0)
def test_native_erc_and_physical_claims_are_not_fabricated():
 a=j('results/INDEPENDENT_CONSISTENCY_FINAL.json');assert a['native_erc']=='NOT_CHECKED'and a['hardware']is False
 a=j('results/CHAT_ACCESS_CAPABILITY.json');assert not a['consultation_sent']and not a['decision_received']
