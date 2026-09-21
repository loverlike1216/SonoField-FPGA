import copy,json,tempfile,unittest
from pathlib import Path
import numpy as np
from software.calibration.config import load
from software.calibration.geometry import paths,positions,distances,solve_pose
from software.calibration.sound_speed import sound_speed
from software.calibration.signal import estimate_tof,envelope,fit_carrier,circular_mean,circular_residual,fuse_distance,capture_quality
from software.characterization.response import resonance,common_frequency
from software.calibration.database import decode_frames,save
from software.calibration.synthetic import truth,generate
from software.calibration.pipeline import process,phase_lut
from software.control.host import Controller
from software.control import registers as r


class CalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg=load();cls.gt=truth(cls.cfg);cls.pairs=paths(cls.cfg)
        cls.raw=np.stack([generate(cls.cfg,cls.gt,f,seed=7020+i) for i,f in enumerate(cls.cfg['sweep_hz'])])
        cls.record,cls.diag=process(cls.cfg,cls.raw,cls.cfg['sweep_hz'],
            {'git_commit':'unit-test','timestamp':'SIMULATION','board_revision':'SIM','classification':'SIMULATION_ESTIMATE',
             'upper_board_id':'SIM_UPPER','lower_board_id':'SIM_LOWER','tx_batch':'SIM','rx_batch':'SIM'},[{'sha256':'unit-input'}])

    def test_SW01_coordinates(self):
        tx,rx=positions(self.cfg,centered=True)
        self.assertEqual(tx.shape,(128,3));self.assertEqual(rx.shape,(8,3))
        # 128-term binary64 summation error; this is < 10^-9 micrometres.
        np.testing.assert_allclose(tx.mean(axis=0),0,atol=1e-15)
        self.assertAlmostEqual(tx[1,0]-tx[0,0],.012);self.assertAlmostEqual(tx[0,2]-tx[64,2],.1)

    def test_SW02_paths(self):
        self.assertEqual(len(set(self.pairs)),512)
        self.assertEqual(self.pairs[0],(64,0));self.assertEqual(self.pairs[-1],(63,7))

    def test_SW03_sound_speed_reference(self):
        # Cramer-column values independently published in JPCRD, DOI 10.1063/5.0294663.
        for t,h,expected in [(0,40,331.575),(20,60,344.115),(30,80,351.008)]:
            self.assertAlmostEqual(sound_speed(t,h,101325,400),expected,delta=.015)
        self.assertGreater(sound_speed(25,80,101325),sound_speed(25,10,101325))

    def test_SW04_environment_limits(self):
        for t,h,p in [(-20,50,101325),(20,110,101325),(20,50,50000)]:
            with self.assertRaises(ValueError):sound_speed(t,h,p)

    def test_SW05_tof_fractional(self):
        fs=800000;f=40000;t=np.arange(1024)/fs;delay=263.37/fs
        y=12000+5000*envelope(t-delay,16/f,25e-6,35e-6)*np.cos(2*np.pi*f*t+1.4)
        got=estimate_tof(y,fs,f,16,25e-6,35e-6)
        self.assertAlmostEqual(got['sample_delay'],263.37,delta=.03)

    def test_SW06_phase_and_dc(self):
        t=np.arange(1000)/800000;y=10000+1000*np.cos(2*np.pi*40300*t+2.3)
        got=fit_carrier(y,800000,40300)
        self.assertAlmostEqual(got['phase_rad'],2.3,places=10);self.assertAlmostEqual(got['dc'],10000,places=6)

    def test_SW07_circular_wrap(self):
        mean,strength=circular_mean(np.deg2rad([179,-179]))
        self.assertAlmostEqual(abs(mean),np.pi);self.assertGreater(strength,.999)

    def test_SW08_coarse_fine(self):
        for length in [.09,.1,.115,.15]:
            phase=circular_residual(.7-2*np.pi*40000*length/346)
            self.assertAlmostEqual(fuse_distance(length+.0002,phase,40000,346,.7),length,places=10)

    def test_SW09_ten_pose_cases(self):
        rng=np.random.default_rng(42)
        cases=[[0,0,.1,0,0,0],[0,0,.092,0,0,0],[0,0,.113,0,0,0],
               [.002,0,.1,0,0,0],[0,-.002,.1,0,0,0],[0,0,.1,1,0,0],
               [0,0,.1,0,-1,0],[0,0,.1,0,0,1],[.001,-.001,.099,.4,-.3,.2],[-.001,.002,.102,-.5,.6,-.4]]
        for index,pose in enumerate(cases):
            with self.subTest(index=index):
                observed=distances(self.cfg,pose,self.pairs)
                if index>=8:observed+=rng.normal(0,30e-6,len(observed));observed[::31]+=.004;observed[3::37]=np.nan
                got=solve_pose(self.cfg,self.pairs,observed)
                self.assertLess(np.linalg.norm(np.array(got['pose'])[:3]-pose[:3]),.0001)
                self.assertLess(np.linalg.norm(np.array(got['pose'])[3:]-pose[3:]),.1)

    def test_SW10_geometry_rejects_unobservable(self):
        with self.assertRaises(ValueError):solve_pose(self.cfg,self.pairs,[np.nan]*512)

    def test_SW11_resonance(self):
        f=np.arange(38500,41501,100);a=1/np.sqrt(1+(2*(f-40237)/1100)**2)
        self.assertAlmostEqual(resonance(f,a)['f0_hz'],40237,delta=2)

    def test_SW12_common_carrier(self):
        selected=self.record['f_work'];self.assertIn(selected,self.cfg['sweep_hz'])
        self.assertGreaterEqual(selected,38500);self.assertLessEqual(selected,41500)

    def test_SW13_full_raw_pipeline(self):
        p=np.array(self.record['measured_pose']['pose'])-self.gt['pose']
        self.assertLess(np.linalg.norm(p[:3])*1000,.1);self.assertLess(np.linalg.norm(p[3:]),.1)
        self.assertEqual(len(self.record['channels']),128);self.assertEqual(len(self.diag['pairs']),512)

    def test_SW14_phase_accuracy(self):
        response=1/(1+1j*2*(self.record['f_work']-self.gt['f0'])/self.gt['bandwidth'])
        errors=circular_residual([x['phase_error_rad'] for x in self.record['channels']],self.gt['tx_phase']+np.angle(response))
        self.assertLess(np.rad2deg(np.sqrt(np.mean(errors**2))),2)

    def test_SW15_frequency_accuracy(self):
        errors=np.array([x['f0_hz'] for x in self.record['channels']])-self.gt['f0']
        self.assertLess(np.sqrt(np.mean(errors**2)),80)

    def test_SW16_health_and_mask_policy(self):
        self.assertEqual(self.record['channels'][7]['status'],'WEAK')
        self.assertFalse(self.record['channels'][7]['recommended_mask']);self.assertTrue(self.record['channels'][7]['active_mask'])

    def test_SW17_lut_separate_fields(self):
        rows=phase_lut(self.cfg,self.record)
        self.assertEqual(len(rows),128)
        for x in rows:self.assertEqual(x['effective_phase'],(x['requested_phase']+x['calibration_phase'])%256)
        nominal=phase_lut(self.cfg,self.record,geometry_mode='NOMINAL')
        self.assertNotEqual([x['requested_phase'] for x in rows],[x['requested_phase'] for x in nominal])

    def test_SW18_database_hash_archive(self):
        with tempfile.TemporaryDirectory() as d:
            a=save(Path(d),self.record);b=save(Path(d),self.record);self.assertEqual(a,b)
            self.assertEqual(len(list((Path(d)/'archive').glob('*.json'))),1)

    def test_SW19_signed_unpack_and_clip(self):
        data=np.array([[-32768,-1,0,1,32767,100,-100,23]],dtype='<i2')
        np.testing.assert_array_equal(decode_frames(data.tobytes()),data)
        self.assertEqual(capture_quality(data)['clipping_count'],2)

    def test_SW20_control_errors_disable(self):
        writes=[];c=Controller(lambda address:32 if address==r.STATUS else 7,lambda a,v:writes.append((a,v)))
        with self.assertRaises(RuntimeError):c.wait(lambda s:False)
        self.assertIn((r.CONTROL,4),writes)
        with self.assertRaises(ValueError):c.apply_map([])

    def test_SW21_rx_reference_is_explicit(self):
        self.assertEqual(self.record['phase_reference'],'EXPLICIT_RX_ANCHORS')
        self.assertIn('SIMULATION_REFERENCE_ONLY',self.record['phase_reference_provenance'])

    def test_SW22_fixed_seed(self):
        a=generate(self.cfg,self.gt,40000,seed=6);b=generate(self.cfg,self.gt,40000,seed=6)
        self.assertTrue(np.array_equal(a,b))

    def test_SW23_invalid_or_relative_lut_rejected(self):
        invalid=copy.deepcopy(self.record);invalid['channels'][3]['phase_error_rad']=None
        with self.assertRaises(ValueError):phase_lut(self.cfg,invalid)
        relative=copy.deepcopy(self.record);relative['phase_reference']='RELATIVE_PER_BANK_ONLY'
        with self.assertRaises(ValueError):phase_lut(self.cfg,relative)

    def test_SW24_noisy_integer_tof(self):
        fs=800000;f=40000;t=np.arange(1024)/fs
        y=12000+5000*envelope(t-260/fs,16/f,25e-6,35e-6)*np.cos(2*np.pi*f*t+.3)
        y+=np.random.default_rng(17).normal(0,80,len(y))
        self.assertAlmostEqual(estimate_tof(y,fs,f,16,25e-6,35e-6)['sample_delay'],260,delta=.3)

    def test_SW25_reject_synthetic_reference_for_real_capture(self):
        with self.assertRaises(ValueError):process(self.cfg,self.raw,self.cfg['sweep_hz'],{'classification':'HARDWARE_VERIFIED'},[])


if __name__=='__main__':unittest.main()
