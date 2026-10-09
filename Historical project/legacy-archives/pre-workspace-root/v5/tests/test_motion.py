"""MOTION-SW01..37 plus protocol, safety, model and register regression cases."""
import copy
import json
import tempfile
import threading
import unittest
from pathlib import Path
import numpy as np
from software.motion.workspace import load_profile,validate_target,validate_speed,mm_to_m,m_to_mm
from software.motion.trajectory import Planner,xyz
from software.motion.trap_solver import TrapSolver,digest
from software.motion.commands import encode,decode
from software.motion.motion_controller import MotionController
from software.motion.transport import RegisterTranscriptTransport,BoardTransport
from software.calibration.config import load
from software.control.host import Controller
from software.acoustic_model.transducer import Transducer
from software.acoustic_model.field_solver import pressure
from software.acoustic_model.visualize_field import potential_proxy

ROOT=Path(__file__).resolve().parents[1]
RECORD=ROOT/'simulation/fixtures/calibration_reference.json'


class MotionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile=load_profile();cls.planner=Planner(cls.profile)
        cls.record=json.loads(RECORD.read_text());cls.solver=TrapSolver(load(),cls.record,cls.profile)

    def target(self,p):return validate_target(p,self.profile)
    def speed(self,v,**kwargs):return validate_speed(v,self.profile,**kwargs)
    def shape(self,kind,params,**kwargs):return self.planner.planar(kind,params,**kwargs)
    def check_path(self,path,vertical=False):
        positions=np.array([xyz(r) for r in path]);dt=1/self.profile['update_rate_hz']
        for row in path:self.target(xyz(row))
        self.assertEqual(path[0]['velocity_mm_s'],0);self.assertEqual(path[-1]['velocity_mm_s'],0)
        np.testing.assert_allclose(np.diff([r['timestamp_target'] for r in path]),dt,atol=1e-12)
        velocity=np.diff(positions,axis=0)/dt
        acceleration=np.diff(np.vstack([np.zeros((1,3)),velocity,np.zeros((1,3))]),axis=0)/dt
        self.assertLessEqual(np.linalg.norm(acceleration,axis=1).max(),(10 if vertical else 20)*1.01)

    def test_MOTION_SW01_origin(self):np.testing.assert_array_equal(self.target([0,0,0]),[0,0,0])
    def test_MOTION_SW02_bounds(self):self.target([-10,10,-6])
    def test_MOTION_SW03_reject_x(self):
        with self.assertRaisesRegex(ValueError,'TARGET_OUT_OF_WORKSPACE'):self.target([10.001,0,0])
    def test_MOTION_SW04_reject_y(self):
        with self.assertRaises(ValueError):self.target([0,-10.001,0])
    def test_MOTION_SW05_reject_z(self):
        with self.assertRaises(ValueError):self.target([0,0,6.001])
    def test_MOTION_SW06_exact_boundary(self):
        for signs in np.array(np.meshgrid([-1,1],[-1,1],[-1,1])).reshape(3,-1).T:self.target(signs*[10,10,6])
    def test_MOTION_SW07_units(self):np.testing.assert_allclose(m_to_mm(mm_to_m([3,-2,6])),[3,-2,6])
    def test_MOTION_SW08_min_horizontal(self):self.assertEqual(self.speed(.5),.5)
    def test_MOTION_SW09_max_horizontal(self):self.assertEqual(self.speed(10),10)
    def test_MOTION_SW10_above_horizontal(self):
        with self.assertRaises(ValueError):self.speed(10.001)
    def test_MOTION_SW11_vertical_bounds(self):
        self.speed(.5,vertical=True);self.speed(5,vertical=True)
    def test_MOTION_SW12_above_vertical(self):
        with self.assertRaises(ValueError):self.speed(5.001,vertical=True)
    def test_MOTION_SW13_negative(self):
        with self.assertRaises(ValueError):self.speed(-1)
    def test_MOTION_SW14_zero_only_hold(self):
        with self.assertRaises(ValueError):self.speed(0)
        self.assertEqual(self.speed(0,hold=True),0)
    def test_MOTION_SW15_xy(self):self.check_path(self.planner.point_move([0,0,0],[5,4,0]))
    def test_MOTION_SW16_z(self):self.check_path(self.planner.point_move([0,0,0],[0,0,4]),vertical=True)
    def test_MOTION_SW17_xyz_decomposition(self):
        path=self.planner.point_move([0,0,0],[4,3,2]);pos=np.array([xyz(r) for r in path]);delta=np.diff(pos,axis=0)
        self.assertFalse(np.any((np.linalg.norm(delta[:,:2],axis=1)>1e-12)&(np.abs(delta[:,2])>1e-12)))
        np.testing.assert_allclose(pos[-1],[4,3,2])
    def test_MOTION_SW18_end_velocity(self):self.check_path(self.planner.line([0,0,0],[8,0,0]))
    def test_MOTION_SW19_all_in_workspace(self):self.check_path(self.planner.point_move([-10,-10,-6],[10,10,6]))
    def test_MOTION_SW20_line(self):self.check_path(self.shape('LINE',{'start':[-5,0],'end':[5,0]}))
    def test_MOTION_SW21_circle(self):self.check_path(self.shape('CIRCLE',{'radius':5}))
    def test_MOTION_SW22_semicircle(self):
        for start in (0,90,180,270):self.check_path(self.shape('SEMICIRCLE',{'radius':5,'start_angle_deg':start}))
    def test_MOTION_SW23_ellipse(self):self.check_path(self.shape('ELLIPSE',{'a':6,'b':3,'rotation_deg':30}))
    def test_MOTION_SW24_hyperbola(self):
        self.check_path(self.shape('HYPERBOLA_SEGMENT',{'a':2,'b':2,'interval':[-1,1],'branch':-1}))
        with self.assertRaises(ValueError):self.shape('HYPERBOLA_SEGMENT',{'a':2,'b':2,'interval':[-100,100]})
    def test_MOTION_SW25_triangle(self):self.check_path(self.shape('TRIANGLE',{'radius':5}))
    def test_MOTION_SW26_rectangle(self):self.check_path(self.shape('RECTANGLE',{'width':8,'height':6}))
    def test_MOTION_SW27_custom(self):
        self.check_path(self.shape('CUSTOM_WAYPOINTS',{'vertices':[[-5,-2],[5,-2],[5,2]]}))
        with self.assertRaisesRegex(ValueError,'SEGMENT_TOO_SHORT'):
            self.shape('CUSTOM_WAYPOINTS',{'vertices':[[0,0],[.01,0],[5,2]]})
    def test_MOTION_SW28_out_of_bounds_path(self):
        with self.assertRaisesRegex(ValueError,'TARGET_OUT_OF_WORKSPACE'):self.shape('CIRCLE',{'radius':11})
    def test_MOTION_SW29_corner_rounding(self):
        path=self.shape('RECTANGLE',{'width':8,'height':6},speed=10);self.check_path(path)
        positions=np.array([xyz(r) for r in path]);self.assertGreater(np.linalg.norm(positions-np.array([4,3,0]),axis=1).min(),.1)
    def test_MOTION_SW30_positive_z(self):self.check_path(self.planner.line([0,0,0],[0,0,4],2,vertical=True),True)
    def test_MOTION_SW31_negative_z(self):self.check_path(self.planner.line([0,0,4],[0,0,-4],2,vertical=True),True)
    def test_MOTION_SW32_xy_fixed(self):
        path=self.planner.line([2,3,-4],[2,3,4],2,vertical=True)
        for row in path:np.testing.assert_array_equal(xyz(row)[:2],[2,3])
    def test_MOTION_SW33_vertical_cap(self):
        with self.assertRaises(ValueError):self.planner.line([0,0,0],[0,0,4],10,vertical=True)
    def test_MOTION_SW34_center_z(self):
        path=self.planner.line([2,3,4],[2,3,0],2,vertical=True);np.testing.assert_array_equal(xyz(path[-1]),[2,3,0])
        with tempfile.TemporaryDirectory() as temp:
            controller=MotionController(load(),self.profile,None,Path(temp)/'unused.jsonl')
            controller.position=[2,3,4]
            path=controller.preview('RETURN_CENTER',{'target':[9,9,5]})
            np.testing.assert_array_equal(xyz(path[-1]),[0,0,0])
    def test_MOTION_SW35_full_maps(self):
        for p in ([0,0,0],[5,0,0],[0,0,4],[0,0,-4]):
            rows,report=self.solver.solve(p);self.assertEqual(len(rows),128);self.assertEqual(report['validity'],'TRAP_VALID')
    def test_MOTION_SW36_deterministic(self):
        solver=TrapSolver(load(),self.record,self.profile)
        self.assertEqual(digest(self.solver.solve([4,2,1])),digest(solver.solve([4,2,1])))
    def test_MOTION_SW37_calibration_constant(self):
        a,_=self.solver.solve([0,0,0]);b,_=self.solver.solve([5,2,4])
        self.assertEqual([r['calibration_phase'] for r in a],[r['calibration_phase'] for r in b])
        self.assertNotEqual([r['requested_phase'] for r in a],[r['requested_phase'] for r in b])

    def test_field_model_cross_check(self):
        rows,_=self.solver.solve([1,2,3]);elements=[]
        for i,(position,normal,c) in enumerate(zip(self.solver.tx,self.solver.normals,self.record['channels'])):
            elements.append(Transducer(c['channel_id'],i,tuple(position),tuple(normal),frequency=self.record['f_work'],
                                       relative_amplitude=self.solver.amplitude[i],
                                       calibration_phase=rows[i]['calibration_phase']*2*np.pi/256,intrinsic_phase=-self.solver.errors[i]))
        points=np.array([[.001,.002,.003],[-.004,.003,-.001]])
        phases=np.array([r['requested_phase'] for r in rows])*2*np.pi/256
        np.testing.assert_allclose(self.solver.pressure(points,rows),pressure(elements,points,phases,self.record['sound_speed']),atol=1e-10)
        np.testing.assert_allclose(self.solver.potential(points,rows),potential_proxy(elements,points,phases,self.record['sound_speed'],h=.000025),rtol=1e-10)

    def test_invalid_trap_no_acoustic_field(self):
        record=copy.deepcopy(self.record)
        for c in record['channels']:c['relative_amplitude']=0
        solver=TrapSolver(load(),record,self.profile)
        self.assertEqual(solver.solve([0,0,0])[1]['validity'],'TRAP_INVALID_MODEL')

    def test_protocol_integrity(self):
        packet=encode(42,'SET_TARGET',{'target':[1,2,3]})
        self.assertEqual(decode(packet),(42,'SET_TARGET',{'target':[1,2,3]}))
        with self.assertRaises(ValueError):decode(packet[:-1]+bytes([packet[-1]^1]))
        with self.assertRaises(ValueError):decode(packet[:-2])
        with self.assertRaises(ValueError):encode(0,'HOLD',{'data':'x'*20000})

    def test_invalid_nonfinite_and_bounded_inputs(self):
        for p in ([np.nan,0,0],[0,np.inf,0],[1,2]):
            with self.assertRaises(ValueError):self.target(p)
        with self.assertRaises(ValueError):self.shape('CIRCLE',{'radius':5},repeat=100000)
        with self.assertRaises(ValueError):self.shape('CUSTOM_WAYPOINTS',{'vertices':[[0,0]]*65})
        with self.assertRaises(ValueError):load_profile(hardware=True)
        with self.assertRaises(RuntimeError):BoardTransport()

    def test_controller_register_map(self):
        rows,_=self.solver.solve([0,0,0]);transport=RegisterTranscriptTransport();controller=Controller(transport.read32,transport.write32)
        controller.stream_map(rows)
        self.assertEqual(transport.write_count,385)
        self.assertEqual(transport.frames[0],[(r['enabled']<<16)|(r['calibration_phase']<<8)|r['requested_phase'] for r in rows])
        with self.assertRaises(ValueError):controller.stream_map(rows[:-1])
        with self.assertRaises(RuntimeError):transport.read32(4)

    def test_safety_state_and_stop(self):
        class UnitTransport:
            # Unit-test double only: this test makes no RTL execution claim.
            def __init__(self):self.cancelled=threading.Event();self.calls=0
            def stop(self):self.cancelled.set()
            def execute(self,transcript,frequency):self.calls+=1;return {'classification':'UNIT_TEST_DOUBLE'}
        with tempfile.TemporaryDirectory() as temp:
            t=UnitTransport();m=MotionController(load(),self.profile,t,Path(temp)/'commands.jsonl')
            self.assertEqual(m.state,'SAFE_DISABLED')
            with self.assertRaises(RuntimeError):m.dispatch(encode(0,'SET_TARGET',{'target':[1,0,0]}))
            m.dispatch(encode(1,'CONNECT'));self.assertEqual(t.calls,0)
            m.load_calibration(self.record)
            with self.assertRaises(RuntimeError):m.dispatch(encode(2,'SET_TARGET',{'target':[1,0,0]}))
            m.dispatch(encode(3,'APPLY_CENTER'));self.assertEqual(m.state,'WAIT_OPERATOR')
            m.dispatch(encode(4,'BALL_AT_CENTER_CONFIRMED'));self.assertEqual(m.state,'ARMED')
            preview=m.preview('SET_TARGET',{'target':[1,0,0]})
            m.dispatch(encode(5,'SET_TARGET',{'target':[1,0,0]}),prepared_path=preview)
            m.dispatch(encode(6,'STOP'));self.assertEqual(m.state,'SAFE_DISABLED');self.assertFalse(m.confirmed)
            with self.assertRaises(ValueError):m.dispatch(encode(6,'STOP'))


if __name__=='__main__':unittest.main()
