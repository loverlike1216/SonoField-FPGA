"""Additive requirements and negative cases for the hardware review candidate."""
from pathlib import Path
import copy,itertools,json,math,unittest
from software.board.hardware_design import (capacitive_power,source_limit,array_power,
    usb_avcc,i2c_pullup_bounds,adc_serial_budget,InterlockModel,MuxPolicy)
ROOT=Path(__file__).resolve().parents[1]
H=ROOT/'hardware/design_20261011'


class Power(unittest.TestCase):
    def test_capacitive_independent_energy(self):
        # Two edges/cycle, one-half CV2 per edge.
        self.assertAlmostEqual(capacitive_power(),64*2*.5*2.64e-9*144*40000)
    def test_voltage_squared(self):self.assertAlmostEqual(capacitive_power(swing_v=24),4*capacitive_power())
    def test_off_zero(self):self.assertEqual(capacitive_power(active_fraction=0),0)
    def test_no_unknown_as_zero(self):self.assertIsNone(array_power()['total_w'])
    def test_unknown_status(self):self.assertEqual(array_power(motional_w=0)['status'],'HOLD')
    def test_cable_energy_balance(self):
        r=array_power(motional_w=10,driver_extra_w=1,auxiliary_w=2,cable_loop_ohm=.2,efficiency=.8)
        self.assertAlmostEqual(r['total_w'],r['load_w']+(r['total_w']/12)**2*.2)
    def test_unphysical_load_rejected(self):
        self.assertEqual(array_power(motional_w=1000,driver_extra_w=1,auxiliary_w=2,cable_loop_ohm=1,efficiency=.8)['status'],'INVALID_VOLTAGE_COLLAPSE')
    def test_headroom_definition(self):self.assertAlmostEqual(source_limit(40)*1.3,40)
    def test_derating(self):self.assertAlmostEqual(source_limit(60,derating=.8),48/1.3)
    def test_nonfinite_rejected(self):
        for v in (-1,0,float('nan'),float('inf')):
            with self.subTest(v=v),self.assertRaises(ValueError):capacitive_power(swing_v=v)
    def test_bad_duty_rejected(self):
        with self.assertRaises(ValueError):capacitive_power(active_fraction=1.1)
    def test_bad_efficiency_rejected(self):
        with self.assertRaises(ValueError):array_power(motional_w=0,driver_extra_w=0,auxiliary_w=1,cable_loop_ohm=0,efficiency=1.1)
    def test_usb_low_vbus_failure(self):self.assertFalse(usb_avcc(4.75,1,.1,.05)['direct_path_valid'])
    def test_usb_good_path(self):self.assertTrue(usb_avcc(5.1,1,.1,.05)['direct_path_valid'])
    def test_adc_data_rate_not_sequential_proof(self):
        r=adc_serial_budget();self.assertEqual(r['data_only_min_sclk_hz'],25600000);self.assertFalse(r['sequential_feasible'])
    def test_adc_slower_feasible(self):self.assertTrue(adc_serial_budget(sample_hz=400000)['sequential_feasible'])


class Safety(unittest.TestCase):
    def test_boot_default_off(self):self.assertFalse(InterlockModel().step(pl_request=True))
    def test_manual_rearm_only_when_request_off(self):
        m=InterlockModel();self.assertFalse(m.step(pl_request=True,manual_rearm_edge=True));self.assertTrue(m.latched)
    def test_faults_each_cut_and_latch(self):
        for fault in ('central_ok','local_ok','estop_closed','temperature_ok','watchdog_ok','efuse_ok','cable_ok'):
            with self.subTest(fault=fault):
                m=InterlockModel();m.step(manual_rearm_edge=True);self.assertTrue(m.step(pl_request=True))
                self.assertFalse(m.step(pl_request=True,**{fault:False}));self.assertFalse(m.step(pl_request=True))
    def test_fault_and_rearm_simultaneous_fault_wins(self):self.assertFalse(InterlockModel().step(estop_closed=False,manual_rearm_edge=True,pl_request=True))
    def test_recover_requires_explicit_edge(self):
        m=InterlockModel();m.step(manual_rearm_edge=True);m.step(watchdog_ok=False)
        self.assertFalse(m.step(pl_request=True));m.step(manual_rearm_edge=True);self.assertTrue(m.step(pl_request=True))
    def test_central_loss_independent_of_ps(self):
        m=InterlockModel();m.step(manual_rearm_edge=True);self.assertFalse(m.step(pl_request=True,central_ok=False))


class Bus(unittest.TestCase):
    def test_mux_start_none(self):self.assertEqual(MuxPolicy().mask,0)
    def test_mux_onehot(self):
        m=MuxPolicy()
        for c in (0,1,2,0):self.assertEqual(m.select(c),1<<c)
    def test_unpowered_segment_rejected(self):
        m=MuxPolicy()
        with self.assertRaises(RuntimeError):m.select(1,powered=False)
        self.assertEqual(m.mask,0)
    def test_stuck_bus_requires_reset(self):
        m=MuxPolicy();m.select(1);self.assertIn('RESET',m.bus_timeout())
        with self.assertRaises(RuntimeError):m.select(0)
        m.reset_observed();self.assertEqual(m.select(0),1)
    def test_wrong_channel_rejected(self):
        with self.assertRaises(ValueError):MuxPolicy().select(3)
    def test_pullup_long_cable_bounds(self):
        a=i2c_pullup_bounds(400);self.assertTrue(a['r_min_ohm']<2200<a['r_max_ohm'])
        self.assertFalse(i2c_pullup_bounds(4000)['feasible'])


class Contracts(unittest.TestCase):
    def setUp(self):self.d=json.loads((H/'SIGNAL_CONTRACT.json').read_text());self.p=self.d['pins']
    def test_all_contacts_unique(self):self.assertEqual(len({(r['connector'],r['pin']) for r in self.p}),80)
    def test_gpio_63_and_5(self):
        gpio=[r for r in self.p if r['bank']];self.assertEqual(len(gpio),68);self.assertEqual(sum(r['direction']=='HIGH_Z' for r in gpio),5)
    def test_package_no_collision(self):
        a=[r['package_pin'] for r in self.p if r['bank']];self.assertEqual(len(a),len(set(a)))
    def test_header_power_all_nc(self):
        for r in self.p:
            if r['pin'] in (2,39,40):self.assertEqual(r['direction'],'NC_POWER');self.assertEqual(r['binding'],'NO_CONNECT')
    def test_reset_is_active_high(self):
        r=next(r for r in self.p if r['connector']=='J11' and r['pin']==28)
        self.assertEqual((r['net'],r['rtl_port'],r['safe_level']),('ADC_RESET','adc_reset','HIGH_RESET'))
    def test_core_not_claimed_wired(self):self.assertEqual(self.d['rtl_integration'],'PARTIAL_CURRENT_TOP_BINDINGS_EXPLICIT_NO_63_IO_WRAPPER_CLAIM')
    def test_new_adc_four_dout_same_header(self):
        a=[r for r in self.p if r['net'].startswith('ADC_DOUT')];self.assertEqual([(r['connector'],r['pin']) for r in a],[('J10',i) for i in (28,29,30,31)])
    def test_bom_preserves_core_counts(self):
        b={r['id']:r for r in json.loads((H/'BOM_INPUTS.json').read_text(encoding='utf-8'))['items']}
        for id,q in [('B-001',128),('B-002',8),('B-003',64),('B-004',32),('B-014',1),('B-032',3),('B-021',3)]:self.assertEqual(sum(b[id]['quantities']),q)
    def test_superseded_power_not_double_counted(self):
        b={r['id']:r for r in json.loads((H/'BOM_INPUTS.json').read_text(encoding='utf-8'))['items']}
        for id in ('B-018','B-020','B-023','B-024','B-044','H-006','H-007','H-008'):self.assertEqual(sum(b[id]['quantities']),0)
    def test_geometry_exact(self):
        self.assertEqual(self.d['geometry']['tx_axis_mm'],[-42,-30,-18,-6,6,18,30,42]);self.assertEqual(self.d['geometry']['face_gap_mm'],100)
    def test_no_native_erc_claim(self):
        n=json.loads((H/'CONNECTION_CONTRACT.json').read_text());self.assertEqual(n['erc'],'NOT_RUN');self.assertEqual(n['native_schematic'],'NOT_CREATED')
    def test_xdc_refuses_execution(self):
        self.assertTrue((H/'ax7020_design_review_only.xdc').read_text().startswith('error {REVIEW_ONLY'))


if __name__=='__main__':unittest.main()
