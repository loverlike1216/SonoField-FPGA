"""Bounded planar paths and staged XY/Z motion, sampled at a fixed logical cadence.

Quintic progress makes each segment start/end at zero velocity and acceleration.
Duration uses both tangential and curvature acceleration, then checks sampled motion.
"""
import math
import numpy as np
from scipy.interpolate import CubicSpline
from .workspace import validate_target, validate_speed


def quintic(t):
    return t**3 * (10 + t * (-15 + 6*t))


class Planner:
    def __init__(self, profile):
        self.profile = profile
        self.rate = profile['update_rate_hz']

    def _sample(self, curve, speed, mode, vertical=False):
        speed = validate_speed(speed, self.profile, vertical=vertical)
        acceleration = self.profile['vertical_acceleration_mm_s2' if vertical else 'horizontal_acceleration_mm_s2']
        # Dense, deterministic curvature inspection includes speed/acceleration along the full curve.
        u = np.linspace(0, 1, 4097)
        geometry = curve(u)
        if geometry.shape != (len(u), 3) or not np.all(np.isfinite(geometry)):
            raise ValueError('Invalid finite path')
        for p in geometry:
            validate_target(p, self.profile)
        composed = curve(quintic(u))
        du = u[1] - u[0]
        v = np.gradient(composed, du, axis=0, edge_order=2)
        a = np.gradient(v, du, axis=0, edge_order=2)
        duration = max(np.linalg.norm(v, axis=1).max()/speed,
                       math.sqrt(np.linalg.norm(a, axis=1).max()/acceleration), 1/self.rate)*1.01
        steps = math.ceil(duration*self.rate)
        if steps+1 > self.profile['max_frames'] or steps/self.rate > self.profile['max_duration_s']:
            raise ValueError('TRAJECTORY_TOO_LONG')
        positions = curve(quintic(np.linspace(0, 1, steps+1)))
        measured_v = np.diff(positions, axis=0)*self.rate
        measured_a = np.diff(np.vstack([np.zeros((1,3)), measured_v, np.zeros((1,3))]), axis=0)*self.rate
        if np.linalg.norm(measured_v, axis=1).max() > speed*1.001 or np.linalg.norm(measured_a, axis=1).max() > acceleration*1.001:
            raise ValueError('PROFILE_SAMPLING_LIMIT')
        result=[]
        for i, p in enumerate(positions):
            validate_target(p, self.profile)
            result.append(dict(sequence_id=i, timestamp_target=i/self.rate,
                               x_mm=float(p[0]), y_mm=float(p[1]), z_mm=float(p[2]),
                               velocity_mm_s=0.0 if i in (0,steps) else float(np.linalg.norm(measured_v[i-1])),
                               mode=mode, phase_map_reference=None, validity='NOT_EVALUATED', trap_score=None))
        return result

    def join(self, *segments):
        result=[]
        for segment in segments:
            if not segment:
                continue
            if result:
                if not np.allclose(xyz(result[-1]), xyz(segment[0]), atol=1e-9, rtol=0):
                    raise ValueError('DISCONTINUOUS_TRAJECTORY')
                segment=segment[1:]
            result.extend(dict(row) for row in segment)
        if len(result) > self.profile['max_frames'] or (len(result)-1)/self.rate > self.profile['max_duration_s']:
            raise ValueError('TRAJECTORY_TOO_LONG')
        for i, row in enumerate(result):
            row.update(sequence_id=i, timestamp_target=i/self.rate)
        return result

    def hold(self, position, duration=0.1):
        p=validate_target(position, self.profile)
        if not np.isfinite(duration) or not 0 <= duration <= self.profile['max_duration_s']:
            raise ValueError('Invalid hold duration')
        n=max(1, math.ceil(duration*self.rate)+1)
        if n > self.profile['max_frames']:
            raise ValueError('TRAJECTORY_TOO_LONG')
        return [dict(sequence_id=i, timestamp_target=i/self.rate, x_mm=float(p[0]), y_mm=float(p[1]),
                     z_mm=float(p[2]), velocity_mm_s=0.0, mode='HOLD', phase_map_reference=None,
                     validity='NOT_EVALUATED', trap_score=None) for i in range(n)]

    def line(self, start, end, speed=3, *, vertical=False):
        a=validate_target(start,self.profile); b=validate_target(end,self.profile)
        if vertical and not np.array_equal(a[:2], b[:2]):
            raise ValueError('Vertical motion must keep XY fixed')
        if not vertical and a[2] != b[2]:
            raise ValueError('Planar motion must keep Z fixed')
        return self._sample(lambda u:a[None,:]+u[:,None]*(b-a),speed,
                            'VERTICAL_MOVE' if vertical else 'PLANAR_LINE',vertical)

    def point_move(self, start, end, speed=3, vertical_speed=2):
        a=validate_target(start,self.profile); b=validate_target(end,self.profile)
        validate_speed(speed,self.profile); validate_speed(vertical_speed,self.profile,vertical=True)
        corner=np.array([b[0],b[1],a[2]])
        segments=[]
        if not np.array_equal(a,corner): segments.append(self.line(a,corner,speed))
        if not np.array_equal(corner,b): segments.append(self.line(corner,b,vertical_speed,vertical=True))
        return self.join(*segments) if segments else self.hold(a)

    def planar(self, kind, parameters, speed=3, z=0, repeat=1, clockwise=False):
        p=parameters
        if type(repeat) is not int or not 1 <= repeat <= self.profile['max_repeats']:
            raise ValueError('Invalid repeat count')
        if not isinstance(clockwise,bool): raise ValueError('Invalid direction')
        if kind=='LINE':
            return self.line([*p['start'],z],[*p['end'],z],speed)
        center=np.asarray(p.get('center',[0,0]),float)
        if center.shape != (2,) or not np.all(np.isfinite(center)): raise ValueError('Invalid center')
        rotation=math.radians(float(p.get('rotation_deg',0)))
        rot=np.array([[math.cos(rotation),-math.sin(rotation)],[math.sin(rotation),math.cos(rotation)]])
        if kind in ('CIRCLE','SEMICIRCLE','ELLIPSE'):
            a=float(p.get('a',p.get('radius',5))); b=float(p.get('b',a))
            if not (math.isfinite(a) and math.isfinite(b) and a>0 and b>0): raise ValueError('Invalid radius/axis')
            start=math.radians(float(p.get('start_angle_deg',0)))
            sweep=math.radians(float(p.get('sweep_deg',180 if kind=='SEMICIRCLE' else 360)))
            if not math.isfinite(start+sweep) or not 0 < sweep <= 2*math.pi: raise ValueError('Invalid arc angles')
            def xy(u):
                angle=start+(-1 if clockwise else 1)*sweep*u
                return np.c_[a*np.cos(angle),b*np.sin(angle)]@rot.T+center
        elif kind=='HYPERBOLA_SEGMENT':
            a=float(p['a']); b=float(p['b']); lo,hi=map(float,p['interval'])
            branch=p.get('branch',1)
            if not all(map(math.isfinite,[a,b,lo,hi])) or not (a>0 and b>0 and -3<=lo<hi<=3 and branch in (-1,1)):
                raise ValueError('Invalid bounded hyperbola')
            def xy(u):
                t=lo+(hi-lo)*(1-u if clockwise else u)
                return np.c_[branch*a*np.cosh(t),b*np.sinh(t)]@rot.T+center
        elif kind in ('TRIANGLE','RECTANGLE','CUSTOM_WAYPOINTS'):
            if kind=='RECTANGLE':
                w=float(p['width']); h=float(p['height'])
                if not math.isfinite(w+h) or w<=0 or h<=0: raise ValueError('Invalid rectangle')
                vertices=np.array([[-w/2,-h/2],[w/2,-h/2],[w/2,h/2],[-w/2,h/2]])@rot.T+center
            elif kind=='TRIANGLE' and 'vertices' not in p:
                size=float(p.get('radius',5))
                if not math.isfinite(size) or size<=0: raise ValueError('Invalid triangle')
                angle=np.arange(3)*2*np.pi/3+math.pi/2
                vertices=np.c_[size*np.cos(angle),size*np.sin(angle)]@rot.T+center
            else: vertices=np.asarray(p['vertices'],float)
            closed=kind!='CUSTOM_WAYPOINTS' or p.get('closed',False)
            if vertices.ndim!=2 or vertices.shape[1]!=2 or not 2<=len(vertices)<=self.profile['max_waypoints'] or not np.all(np.isfinite(vertices)):
                raise ValueError('Invalid bounded waypoints')
            if kind=='TRIANGLE' and len(vertices)!=3: raise ValueError('Triangle needs 3 vertices')
            if np.any(np.linalg.norm(np.diff(vertices,axis=0),axis=1)<.1):raise ValueError('SEGMENT_TOO_SHORT')
            if clockwise: vertices=vertices[::-1]
            # Stop-and-go quintic segments are the explicit safe corner policy for custom paths.
            # Polygons use tangent-continuous quadratic corner arcs, radius bounded by local edges.
            if not closed:
                if repeat!=1: raise ValueError('Open custom path cannot repeat without an explicit return')
                return self.join(*[self.line([*a,z],[*b,z],speed) for a,b in zip(vertices[:-1],vertices[1:])])
            edges=np.linalg.norm(np.roll(vertices,-1,axis=0)-vertices,axis=1)
            if np.any(edges<0.1): raise ValueError('SEGMENT_TOO_SHORT')
            dense=[]
            r=min(self.profile['corner_radius_mm'],float(edges.min())*.24)
            entries=[]; exits=[]
            for i,v in enumerate(vertices):
                prev=vertices[i-1]; nex=vertices[(i+1)%len(vertices)]
                entries.append(v+(prev-v)*r/np.linalg.norm(prev-v))
                exits.append(v+(nex-v)*r/np.linalg.norm(nex-v))
            for i,v in enumerate(vertices):
                t=np.linspace(0,1,65)[:,None]
                dense.extend(((1-t)**2*entries[i]+2*(1-t)*t*v+t**2*exits[i])[:-1])
                dense.extend(np.linspace(exits[i],entries[(i+1)%len(vertices)],65)[:-1])
            dense=np.asarray([*dense,dense[0]])
            lengths=np.r_[0,np.cumsum(np.linalg.norm(np.diff(dense,axis=0),axis=1))]
            spline=CubicSpline(lengths/lengths[-1],dense,bc_type='periodic')
            xy=lambda u:spline(u)
        else: raise ValueError('Unknown trajectory type')
        curve=lambda u:np.c_[xy(u),np.full(len(u),z)]
        path=self._sample(curve,speed,kind)
        if repeat>1 and not np.allclose(xyz(path[0]),xyz(path[-1]),atol=1e-9):
            raise ValueError('Open trajectory cannot repeat without an explicit return')
        return self.join(*[path for _ in range(repeat)])


def xyz(row):
    return np.array([row['x_mm'],row['y_mm'],row['z_mm']])
