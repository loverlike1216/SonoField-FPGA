"""New pre-PCB invariants, fault rejection and runtime-created path behavior."""
import copy, json, math, tempfile, unittest
from pathlib import Path
import numpy as np
from software.prepcb.temperature import Reading, Environment, Sensors, tmp117_decode, sht45_decode, sht_crc, compensate, transition
from software.prepcb.sparse import scan_plan, refine_tof, solve
from software.prepcb.safety import Safety
from software.prepcb.user_path import Document, sample
from software.prepcb.protocol import Client
from software.calibration.config import load
from software.calibration.geometry import positions
ROOT = Path(__file__).resolve().parents[1]


def environment(values=(25, 25, 25)):
    return Environment([Reading('TMP117_'+k.upper(), k, 100., v, provenance='SYNTHETIC_REFERENCE')
                        for k, v in zip(('center', 'upper', 'lower'), values)], 100.)


def observations(seed, env, pose=None):
    config = load()
    pose = pose or [.0007, -.0005, .1008, .35, -.2, .15]
    tx, rx = positions(config, pose, centered=True)
    rng = np.random.default_rng(seed)
    delays = np.array([0, .2, -.15, .1, 0, -.1, .15, -.2])*1e-6
    result = []
    for t, r in scan_plan():
        tau = env.reference_time(tx[t], rx[r])+delays[r]
        fine = tau+rng.normal(0, 8e-9)
        result.append(dict(tx_id=t, rx_id=r, board='upper' if t < 64 else 'lower',
                           phase=(fine*40000*2*np.pi) % (2*np.pi), TOF_candidate=tau+rng.normal(0, 5e-7),
                           coarse_uncertainty_s=4e-6, carrier_frequency=40000, SNR=35,
                           quality_flags=[], provenance='SYNTHETIC_REFERENCE',
                           cmd_start_tick=0, actual_tx_onset_tick=0, convst_first_tick=0,
                           sample_period=165, raw_ref=None, temperature_vector=env.metadata(),
                           humidity=None, amplitude=1, coarse_ambiguity='INDEPENDENT_COARSE_TOF',
                           frontend_delay='EXPLICIT_RX0_RX4_GAUGES', source_commit='TEST_RUNTIME_INPUT'))
    return result


class TemperatureTests(unittest.TestCase):
    def test_signed_register(self):
        self.assertEqual(tmp117_decode(b'\xff\x80'), -1)
    def test_short_read(self):
        with self.assertRaises(ValueError): tmp117_decode(b'\x00')
    def test_sht_crc(self):
        data=b'\x80\x00'; good=data+bytes([sht_crc(data)])
        self.assertTrue(0 < sht45_decode(good+good)[1] < 100)
        with self.assertRaises(ValueError): sht45_decode(good+good[:-1]+b'\x00')
    def test_integral_reference(self):
        env=environment((24, 29, 20))
        for a,b in [([.04,.02,.05],[0,0,-.02]),([0,0,-.05],[.03,-.03,.05]),([0,0,0],[.001,.002,.003])]:
            self.assertLess(abs(env.travel_time(a,b)-env.reference_time(a,b)), 1e-12)
    def test_uniform(self):
        env=environment()
        self.assertAlmostEqual(env.travel_time([0,0,.05],[0,0,-.05]), .1/(331.3+.606*25), places=12)
    def test_center_participates(self):
        self.assertNotEqual(environment().travel_time([0,0,.05],[0,0,-.05]), environment((28,25,25)).travel_time([0,0,.05],[0,0,-.05]))
    def test_missing(self):
        with self.assertRaises(ValueError): Environment(environment().readings[:2],100)
    def test_stale(self):
        with self.assertRaises(ValueError): Environment(environment().readings,103)
    def test_future(self):
        with self.assertRaises(ValueError): Environment(environment().readings,99)
    def test_offline(self):
        def read(*args): raise OSError('NACK')
        values=Sensors(read).poll(100,'FAULT_INJECTION')
        with self.assertRaises(ValueError): Environment(values,100)
    def test_extreme(self):
        with self.assertRaises(ValueError): environment((90,25,25))
    def test_humidity_assumed(self):
        self.assertTrue(environment().metadata()['pressure_assumed'])
        self.assertFalse(environment().metadata()['humidity_applied'])
    def test_atomic_calibration(self):
        rows=[dict(channel=i,requested_phase=i,calibration_phase=3,enabled=1) for i in range(128)]
        tx,_=positions(load(), centered=True)
        wanted=compensate(rows,tx,np.zeros(3),40000,343,environment())
        self.assertEqual([r['calibration_phase'] for r in wanted],[3]*128)
        self.assertEqual([r['requested_phase'] for r in rows],list(range(128)))
    def test_transition_hold(self):
        a=[dict(requested_phase=0,calibration_phase=0) for _ in range(128)]
        b=[dict(requested_phase=100,calibration_phase=0) for _ in range(128)]
        self.assertEqual(transition(a,b)[0],'HOLD_REARM_REQUIRED')
    def test_transition_slew(self):
        a=[dict(requested_phase=255,calibration_phase=0) for _ in range(128)]
        b=[dict(requested_phase=2,calibration_phase=0) for _ in range(128)]
        self.assertEqual(transition(a,b)[1][0]['requested_phase'],1)


class SparseTests(unittest.TestCase):
    def test_points(self):
        pairs=scan_plan()
        self.assertEqual(len(pairs),128)
        self.assertEqual(len(set(t for t,r in pairs)),32)
        self.assertTrue(all((t<64)!=(r<4) for t,r in pairs))
    def test_supplements(self):
        self.assertEqual(len(scan_plan([1])),136)
    def test_ambiguity(self):
        with self.assertRaises(ValueError): refine_tof(.0003,1,40000,15e-6)
    def test_missing(self):
        with self.assertRaises(ValueError): solve(load(),observations(1,environment())[:20],environment())
    def test_bad_quality(self):
        obs=observations(1,environment())
        for o in obs:o['SNR']=5
        with self.assertRaises(ValueError): solve(load(),obs,environment())
    def test_unique_measurements(self):
        obs=observations(1,environment())
        with self.assertRaises(ValueError): solve(load(),obs+obs[:1],environment())


class PathTests(unittest.TestCase):
    def doc(self):
        d=Document();d.add([0,0,0]);d.add([.5,.2,.1]);return d
    def test_runtime_input(self):
        d=self.doc();d.add([-.3,.4,-.2]);self.assertEqual(sample(d)[-1]['z_mm'],-.2)
    def test_bezier(self):
        d=self.doc();d.bezier(0,[0,.8,0],[.5,.8,.1]);p=sample(d)
        self.assertGreater(max(r['y_mm'] for r in p),.2)
    def test_save_reload(self):
        d=self.doc();d.bezier(0,[.1,.4,0],[.3,.3,.1])
        with tempfile.TemporaryDirectory(dir=ROOT/'build') as tmp:
            p=Path(tmp)/'user.json';d.save(p);self.assertEqual(sample(d),sample(Document.load(p)))
    def test_integrity(self):
        d=self.doc()
        with tempfile.TemporaryDirectory(dir=ROOT/'build') as tmp:
            p=Path(tmp)/'user.json';d.save(p);v=json.loads(p.read_text());v['payload']['closed']=True;p.write_text(json.dumps(v))
            with self.assertRaises(ValueError):Document.load(p)
    def test_undo_redo(self):
        d=self.doc();d.move(1,[.2,.3,.4]);d.undo();self.assertEqual(d.data['vertices'][1]['xyz'],[.5,.2,.1]);d.redo();self.assertEqual(d.data['vertices'][1]['xyz'],[.2,.3,.4])
    def test_order_delete_insert(self):
        d=self.doc();d.add([.1,0,0],index=1);d.reorder(2,1);d.delete(2);self.assertEqual(len(d.data['vertices']),2)
    def test_closed(self):
        d=self.doc();d.edit(lambda x:x.update(closed=True));p=sample(d);self.assertEqual(p[0]['x_mm'],p[-1]['x_mm'])
    def test_bounds(self):
        d=self.doc()
        with self.assertRaises(ValueError):d.move(1,[11,0,0])
    def test_nan(self):
        d=self.doc()
        with self.assertRaises(ValueError):d.add([float('nan'),0,0])
    def test_accel_jerk(self):
        p=sample(self.doc());a=np.array([[r[k] for k in ('x_mm','y_mm','z_mm')] for r in p]);v=np.diff(a,axis=0)*50;acc=np.diff(v,axis=0)*50;j=np.diff(acc,axis=0)*50
        self.assertLessEqual(np.max(np.linalg.norm(v,axis=1)),3)
        self.assertLessEqual(np.max(np.linalg.norm(acc,axis=1)),8)
        self.assertLessEqual(np.max(np.linalg.norm(j,axis=1)),40)
    def test_negotiate_required(self):
        with self.assertRaises(ValueError):Client(lambda c,p:b'').upload(sample(self.doc()))


class SafetyTests(unittest.TestCase):
    def arm(self):
        s=Safety(3);s.step()
        for _ in range(5):s.step(arm=True)
        self.assertEqual(s.state,'ARMED_SAFE');return s
    def test_no_automatic_enable(self):
        s=Safety(3)
        for _ in range(10):s.step()
        self.assertFalse(s.emit)
    def test_held_at_start(self):
        s=Safety(3)
        for _ in range(10):s.step(arm=True)
        self.assertEqual(s.state,'BOARD_CHECK')
    def test_qualified_cal(self):
        s=self.arm()
        for _ in range(5):s.step(cal=True)
        self.assertTrue(s.emit)
    def test_fault_latches(self):
        s=self.arm();s.step(healthy=False);s.step();self.assertEqual(s.state,'FAULT_LATCHED');self.assertFalse(s.emit)
    def test_estop_clear_rearm(self):
        s=self.arm();s.step(estop_ok=False);s.step(clear=True);s.step();self.assertEqual(s.state,'BOARD_CHECK');self.assertFalse(s.emit)
    def test_timeout(self):
        s=Safety(3,4)
        for _ in range(7):s.step()
        self.assertEqual(s.state,'FAULT_LATCHED')
    def test_quality_failure(self):
        s=self.arm()
        for _ in range(5):s.step(cal=True)
        s.step(complete=True);s.step(quality=False);self.assertEqual(s.state,'FAULT_LATCHED')


class CExtensionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from software.prepcb.c_session import build
        cls.library=build(ROOT/'build/prepcb_unit_c')

    def session(self,flags=7):
        from software.prepcb.c_session import Session
        return Session(self.library,flags=flags)

    def path(self):
        d=Document();d.add([0,0,0]);d.add([.1,.1,.1]);return sample(d)

    def test_real_negotiation(self):
        s=self.session();self.assertEqual(s.client.capabilities['capacity'],512)
        self.assertFalse(s.client.capabilities['flags']&8)
    def test_actual_temp_bytes(self):
        import struct
        s=self.session();self.assertEqual(s.client.command('GET_TEMP'),struct.pack('<hhh',25*128,26*128,24*128))
    def test_upload_pause_resume(self):
        s=self.session();p=self.path();s.client.upload(p);s.client.command('MOTION_START');s.tick()
        s.client.command('MOTION_PAUSE');s.tick();self.assertEqual(s.lib.fixture_cursor(),1)
        s.client.command('MOTION_RESUME');s.tick();self.assertEqual(s.lib.fixture_cursor(),2)
        s.client.command('MOTION_STOP');s.tick();self.assertEqual(s.lib.fixture_cursor(),2)
    def test_fault_both_off(self):
        s=self.session();s.client.upload(self.path());s.client.command('MOTION_START');s.tick();s.lib.fixture_fault(1);s.tick()
        self.assertGreater(s.lib.fixture_disables(),0);self.assertEqual(s.lib.fixture_cursor(),1)
    def test_missing_temp_denied(self):
        s=self.session(flags=6)
        with self.assertRaises(ValueError):s.client.command('GET_TEMP')
    def test_unqualified_cal_denied(self):
        s=self.session(flags=3);s.client.upload(self.path())
        with self.assertRaises(ValueError):s.client.command('MOTION_START')
    def test_watchdog_no_auto_resume(self):
        s=self.session();s.client.upload(self.path());s.client.command('MOTION_START');s.tick();s.tick(1000,False)
        self.assertEqual(s.lib.fixture_connected(),0);self.assertEqual(s.lib.fixture_cursor(),1)
    def test_jump_denied(self):
        s=self.session();s.client.upload([dict(x_mm=0,y_mm=0,z_mm=0),dict(x_mm=5,y_mm=0,z_mm=0)])
        with self.assertRaises(ValueError):s.client.command('MOTION_START')
    def test_crc_fail_safe(self):
        from software.board.protocol import encode
        s=self.session();p=bytearray(encode(33,s.sequence+1));p[-1]^=1
        s.lib.fixture_feed(bytes(p),len(p));self.assertEqual(s.lib.fixture_connected(),0)
    def test_sequence_fail_safe(self):
        from software.board.protocol import encode
        s=self.session();p=encode(33,s.sequence)
        s.lib.fixture_feed(p,len(p));self.assertEqual(s.lib.fixture_connected(),0)
    def test_no_fabricated_cal_result(self):
        s=self.session(flags=3);self.assertEqual(s.client.command('CAL_RESULT'),b'\x00')
    def test_unknown_command(self):
        s=self.session()
        with self.assertRaises(ValueError):s.request(75)


if __name__=='__main__':unittest.main()
