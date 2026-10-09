"""LEVITATION_TRAP_V1: calibrated opposing node, local Rayleigh potential inspection.

Relative units only, high-contrast f1=f2=1; ignores gravity, streaming and finite-size
scattering. A local minimum is a SIMULATION_ESTIMATE, never proof of mass support.
"""
import hashlib
import json
import copy
import numpy as np
from scipy.special import j1
from scipy.spatial.transform import Rotation
from .workspace import validate_target, mm_to_m
from ..calibration.geometry import positions
from ..calibration.pipeline import phase_lut


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


class TrapSolver:
    def __init__(self, config, record, profile, *, simulation=True):
        self.config=copy.deepcopy(config); self.record=copy.deepcopy(record); self.profile=copy.deepcopy(profile)
        if not simulation and record.get('classification')!='HARDWARE_VERIFIED':
            raise ValueError('CALIBRATION_NOT_HARDWARE_VERIFIED')
        if record.get('phase_reference')!='EXPLICIT_RX_ANCHORS':
            raise ValueError('Cross-bank phase reference required')
        if not 38500<=record['f_work']<=41500 or not 300<record['sound_speed']<380:
            raise ValueError('Invalid calibrated frequency/environment')
        channels=record['channels']
        if len(channels)!=128 or [c['channel'] for c in channels]!=list(range(128)):
            raise ValueError('Invalid calibrated channel order')
        for ch in channels:
            if ch['active_mask'] and (ch['phase_error_rad'] is None or ch['relative_amplitude'] is None or
                                     not np.isfinite(ch['phase_error_rad']) or not np.isfinite(ch['relative_amplitude']) or ch['relative_amplitude']<0):
                raise ValueError('Invalid active calibration')
        self.calibration_id=digest(record)
        self.tx,_=positions(config,record['measured_pose']['pose'],centered=True)
        upper=Rotation.from_euler('xyz',record['measured_pose']['pose'][3:],degrees=True).apply([0,0,-1])
        self.normals=np.array([upper]*64+[[0,0,1]]*64)
        self.amplitude=np.array([(c['relative_amplitude'] or 0)*bool(c['active_mask']) for c in channels])
        self.errors=np.array([c['phase_error_rad'] or 0 for c in channels])
        self.k=2*np.pi*record['f_work']/record['sound_speed']
        self._cache={}

    def pressure(self, points_m, rows):
        """Vectorized equivalent of acoustic_model.field_solver.pressure.

        RTL temporal lag is a positive phase under exp(-i wt). Intrinsic acoustic
        delay has the opposite sign. Quantized calibration is retained separately.
        """
        v=np.asarray(points_m)[:,None,:]-self.tx[None,:,:]
        r=np.linalg.norm(v,axis=2)
        if np.any(r<=.005): raise ValueError('Excluded near-source region')
        co=np.clip(np.sum(v*self.normals[None,:,:],axis=2)/r,-1,1)
        arg=self.k*.005*np.sqrt(1-co*co)
        direct=np.ones_like(arg)
        np.divide(2*j1(arg),arg,out=direct,where=np.abs(arg)>1e-12)
        direct[co<=0]=0
        phase=np.array([x['requested_phase']+x['calibration_phase'] for x in rows])*2*np.pi/256-self.errors
        return np.sum(self.amplitude*direct/r*np.exp(1j*(self.k*r+phase)),axis=1)

    def potential(self, points_m, rows):
        pts=np.atleast_2d(points_m); h=.000025
        samples=np.concatenate([pts,*[pts+d for d in np.eye(3)*h],*[pts-d for d in np.eye(3)*h]])
        p=self.pressure(samples,rows).reshape(7,len(pts))
        grad=(p[1:4]-p[4:7])/(2*h)
        return np.abs(p[0])**2-1.5/self.k**2*np.sum(np.abs(grad)**2,axis=0)

    def derivatives(self, x_mm, rows):
        # Derivatives with respect to mm improve numerical conditioning.
        h=.1; deltas=[np.zeros(3)]
        deltas.extend(np.eye(3)*h); deltas.extend(-np.eye(3)*h)
        for i in range(3):
            for j in range(i):
                for si,sj in ((1,1),(1,-1),(-1,1),(-1,-1)):
                    deltas.append(np.eye(3)[i]*h*si+np.eye(3)[j]*h*sj)
        values=self.potential((x_mm+np.asarray(deltas))*.001,rows)
        u=values[0]; gradient=(values[1:4]-values[4:7])/(2*h)
        hessian=np.diag((values[1:4]+values[4:7]-2*u)/h**2)
        offset=7
        for i in range(3):
            for j in range(i):
                a,b,c,d=values[offset:offset+4]; offset+=4
                hessian[i,j]=hessian[j,i]=(a-b-c+d)/(4*h*h)
        return u,gradient,hessian

    def solve(self, target_mm):
        target=validate_target(target_mm,self.profile)
        key=tuple(target)
        if key in self._cache:
            return self._cache[key]
        rows=phase_lut(self.config,self.record,target=mm_to_m(target),field_mode='STANDING_WAVE')
        candidate=target.copy(); valid=True
        # Newton search is bounded within the explicitly inspected local neighborhood.
        for _ in range(5):
            u,g,h=self.derivatives(candidate,rows)
            if not np.all(np.isfinite(h)) or np.linalg.eigvalsh(h).min()<=0:
                valid=False; break
            step=np.linalg.solve(h,g)
            if np.linalg.norm(step)<1e-5: break
            if np.linalg.norm(candidate-step-target)>self.profile['trap_neighborhood_mm']:
                valid=False; break
            candidate-=step
        u,g,h=self.derivatives(candidate,rows)
        eigen=np.linalg.eigvalsh(h)
        offsets=np.array(np.meshgrid([-1,0,1],[-1,0,1],[-1,0,1])).reshape(3,-1).T
        # Compare a surrounding shell, excluding the center itself.
        offsets=offsets[np.any(offsets,axis=1)]*self.profile['trap_neighborhood_mm']
        shell=self.potential((candidate+offsets)*.001,rows)
        error=float(np.linalg.norm(candidate-target))
        residual=float(np.linalg.norm(g)/(max(abs(u),1)))
        valid=bool(valid and np.all(np.isfinite([u,*g,*eigen,*shell])) and eigen.min()>0 and
                   residual<1e-3 and error<=self.profile['trap_max_error_mm'] and np.all(shell>u) and
                   np.all(np.abs(candidate)<=np.array(self.profile['model_workspace_mm'])))
        report={'field_mode':'LEVITATION_TRAP_V1','classification':'SIMULATION_ESTIMATE',
                'validity':'TRAP_VALID' if valid else 'TRAP_INVALID_MODEL',
                'predicted_trap_mm':candidate.tolist(),'target_error_mm':error,
                'normalized_gradient_residual':residual,'hessian_eigenvalues_au_per_mm2':eigen.tolist(),
                'trap_score':float(eigen.min()/max(abs(u),1)), 'pressure_au':float(abs(self.pressure(candidate[None,:]*.001,rows)[0])),
                'map_sha256':digest(rows),'calibration_id':self.calibration_id}
        result=(rows,report)
        if len(self._cache)>=self.profile['max_frames']: self._cache.clear()
        self._cache[key]=result
        return result
