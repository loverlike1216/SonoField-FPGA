"""Runtime-authored 3D polylines/Bezier curves, deterministic 50Hz planning."""
import copy
import json
import math
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
from ..motion.trap_solver import digest

DEFAULT_LIMITS = dict(bounds_mm=[10, 10, 6], speed_mm_s=3., acceleration_mm_s2=8.,
                      jerk_mm_s3=40., max_step_mm=.2, phase_step_codes=8, max_frames=12000)


class Document:
    def __init__(self):
        self.data = dict(schema='sonofield.user_path/1', version='v5',
                         created_at=datetime.now(timezone.utc).isoformat(),
                         vertices=[], segments=[], closed=False,
                         limits=copy.deepcopy(DEFAULT_LIMITS), calibration_snapshot=None)
        self.undo_stack, self.redo_stack = [], []

    def edit(self, operation):
        before = copy.deepcopy(self.data)
        try:
            operation(self.data)
            self.validate()
        except Exception:
            self.data = before
            raise
        self.undo_stack.append(before)
        self.redo_stack.clear()

    def add(self, xyz, index=None, dwell=0., speed=3.):
        xyz = [float(x) for x in xyz]
        def operation(d):
            d['vertices'].insert(len(d['vertices']) if index is None else index,
                                 dict(xyz=xyz, dwell_s=float(dwell), speed_mm_s=float(speed)))
            d['segments'] = []  # topology edits invalidate explicit curve handles
        self.edit(operation)

    def move(self, index, xyz):
        self.edit(lambda d: d['vertices'][index].update(xyz=list(map(float, xyz))))

    def delete(self, index):
        def operation(d):
            d['vertices'].pop(index)
            d['segments'] = []
        self.edit(operation)

    def reorder(self, index, destination):
        def operation(d):
            d['vertices'].insert(destination, d['vertices'].pop(index))
            d['segments'] = []
        self.edit(operation)

    def bezier(self, segment, control1, control2):
        def operation(d):
            d['segments'] = [s for s in d['segments'] if s['index'] != segment]
            d['segments'].append(dict(index=segment, control1=list(map(float, control1)),
                                       control2=list(map(float, control2))))
        self.edit(operation)

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(copy.deepcopy(self.data))
            self.data = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(copy.deepcopy(self.data))
            self.data = self.redo_stack.pop()

    def validate(self):
        d = self.data
        if d['schema'] != 'sonofield.user_path/1' or d['version'] != 'v5':
            raise ValueError('Incompatible path schema')
        limits = d['limits']
        if (len(limits['bounds_mm']) != 3 or not np.all(np.isfinite(limits['bounds_mm']))
                or any(x <= 0 or x > cap for x, cap in zip(limits['bounds_mm'], [10, 10, 6]))):
            raise ValueError('Bounds exceed inspected model workspace')
        for key, cap in [('speed_mm_s', 10), ('acceleration_mm_s2', 50), ('jerk_mm_s3', 300),
                         ('max_step_mm', .5), ('phase_step_codes', 32), ('max_frames', 12000)]:
            if not math.isfinite(limits[key]) or not 0 < limits[key] <= cap:
                raise ValueError('Invalid limit: '+key)
        if type(limits['max_frames']) is not int or len(d['vertices']) > 500:
            raise ValueError('Bounded task size required')
        for vertex in d['vertices']:
            p = np.asarray(vertex['xyz'])
            if p.shape != (3,) or not np.all(np.isfinite(p)) or np.any(abs(p) > limits['bounds_mm']):
                raise ValueError('Waypoint outside model bounds')
            if not 0 <= vertex['dwell_s'] <= 60 or not 0 < vertex['speed_mm_s'] <= limits['speed_mm_s']:
                raise ValueError('Invalid dwell/speed')
        seen = set()
        for segment in d['segments']:
            idx = segment['index']
            if idx in seen or not 0 <= idx < len(d['vertices'])-int(not d['closed']):
                raise ValueError('Invalid curve segment')
            seen.add(idx)
            for key in ('control1', 'control2'):
                p = np.asarray(segment[key])
                if p.shape != (3,) or not np.all(np.isfinite(p)) or np.any(abs(p) > limits['bounds_mm']):
                    raise ValueError('Bezier control outside bounds')
        return True

    def save(self, path):
        self.validate()
        Path(path).write_text(json.dumps(dict(payload=self.data, sha256=digest(self.data)),
                                        ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

    @classmethod
    def load(cls, path):
        value = json.loads(Path(path).read_text(encoding='utf-8'))
        if digest(value['payload']) != value['sha256']:
            raise ValueError('Path integrity error')
        doc = cls()
        doc.data = value['payload']
        doc.validate()
        return doc


def sample(document, phase_function=None):
    document.validate()
    d, points = document.data, document.data['vertices']
    if not points:
        raise ValueError('Draw at least one waypoint')
    limits = d['limits']
    controls = {s['index']: s for s in d['segments']}
    def curve(index, u):
        a = np.asarray(points[index]['xyz'])
        b = np.asarray(points[(index+1) % len(points)]['xyz'])
        if index not in controls:
            return a[None, :]*(1-u[:, None])+b[None, :]*u[:, None]
        c = controls[index]
        return ((1-u[:, None])**3*a+3*(1-u[:, None])**2*u[:, None]*np.array(c['control1'])
                +3*(1-u[:, None])*u[:, None]**2*np.array(c['control2'])+u[:, None]**3*b)
    segments = len(points)-1+int(d['closed'] and len(points) > 1)
    frames = [points[0]['xyz']]
    frames.extend([points[0]['xyz']]*math.ceil(points[0]['dwell_s']*50))
    for index in range(segments):
        dense = curve(index, np.linspace(0, 1, 129))
        length = float(np.sum(np.linalg.norm(np.diff(dense, axis=0), axis=1)))
        speed = min(points[index]['speed_mm_s'], points[(index+1) % len(points)]['speed_mm_s'])
        duration = max(.1, 2*length/speed, math.sqrt(8*length/limits['acceleration_mm_s2']),
                       (80*length/limits['jerk_mm_s3'])**(1/3))
        count = math.ceil(duration*50)
        while True:
            u = np.linspace(0, 1, count+1)
            # Rest-to-rest quintic on every user segment makes corners bounded.
            eased = 10*u**3-15*u**4+6*u**5
            candidate = curve(index, eased)
            v = np.diff(candidate, axis=0)*50
            a = np.diff(v, axis=0)*50
            j = np.diff(a, axis=0)*50
            valid = (np.max(np.linalg.norm(v, axis=1)) <= speed+1e-8
                     and np.max(np.linalg.norm(v, axis=1))/50 <= limits['max_step_mm']
                     and np.max(np.linalg.norm(a, axis=1), initial=0) <= limits['acceleration_mm_s2']
                     and np.max(np.linalg.norm(j, axis=1), initial=0) <= limits['jerk_mm_s3'])
            if valid and phase_function:
                maps = np.array([phase_function(p) for p in candidate])
                valid = np.max(abs((np.diff(maps, axis=0)+128) % 256-128), initial=0) <= limits['phase_step_codes']
            if valid:
                break
            count *= 2
            if count+len(frames) > limits['max_frames']:
                raise ValueError('Path cannot meet bounds within bounded task capacity')
        frames.extend(candidate[1:].tolist())
        frames.extend([points[(index+1) % len(points)]['xyz']]*math.ceil(points[(index+1) % len(points)]['dwell_s']*50))
    if len(frames) > limits['max_frames']:
        raise ValueError('Path exceeds bounded queue capacity')
    return [dict(t_s=i/50, x_mm=float(p[0]), y_mm=float(p[1]), z_mm=float(p[2]))
            for i, p in enumerate(frames)]
