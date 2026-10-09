"""Temperature-aware normalized acoustic model, no calibrated Pa/mass claims."""
import copy
import numpy as np
from scipy.special import j1
from ..motion.trap_solver import TrapSolver, digest
from ..motion.workspace import mm_to_m, validate_target
from ..calibration.pipeline import phase_lut
from .temperature import compensate


class TemperatureTrapSolver(TrapSolver):
    def __init__(self,config,record,profile,environment):
        super().__init__(config,record,profile,simulation=True)
        self.environment=environment
        self.k=2*np.pi*self.record['f_work']/float(environment.speed(0))

    def pressure(self,points_m,rows):
        points=np.asarray(points_m)
        v=points[:,None,:]-self.tx[None,:,:];r=np.linalg.norm(v,axis=2)
        if np.any(r<=.005):raise ValueError('Excluded near-source region')
        co=np.clip(np.sum(v*self.normals[None,:,:],axis=2)/r,-1,1)
        arg=self.k*.005*np.sqrt(1-co*co);direct=np.ones_like(arg)
        np.divide(2*j1(arg),arg,out=direct,where=abs(arg)>1e-12);direct[co<=0]=0
        tau=self.environment.travel_times(self.tx[None,:,:],points[:,None,:])
        phase=np.array([row['requested_phase']+row['calibration_phase'] for row in rows])*2*np.pi/256-self.errors
        return np.sum(self.amplitude*direct/r*np.exp(1j*(2*np.pi*self.record['f_work']*tau+phase)),axis=1)

    def solve(self,target_mm):
        target=validate_target(target_mm,self.profile)
        rows=phase_lut(self.config,self.record,target=mm_to_m(target),field_mode='STANDING_WAVE')
        rows=compensate(rows,self.tx,mm_to_m(target),self.record['f_work'],self.record['sound_speed'],self.environment)
        candidate=target.copy();valid=True
        for _ in range(5):
            u,g,h=self.derivatives(candidate,rows)
            if not np.all(np.isfinite(h)) or np.linalg.eigvalsh(h).min()<=0:valid=False;break
            step=np.linalg.solve(h,g)
            if np.linalg.norm(step)<1e-5:break
            if np.linalg.norm(candidate-step-target)>self.profile['trap_neighborhood_mm']:valid=False;break
            candidate-=step
        u,g,h=self.derivatives(candidate,rows);eigen=np.linalg.eigvalsh(h)
        offsets=np.array(np.meshgrid([-1,0,1],[-1,0,1],[-1,0,1])).reshape(3,-1).T
        offsets=offsets[np.any(offsets,axis=1)]*self.profile['trap_neighborhood_mm']
        shell=self.potential((candidate+offsets)*.001,rows)
        error=float(np.linalg.norm(candidate-target));residual=float(np.linalg.norm(g)/max(abs(u),1))
        valid=bool(valid and np.all(np.isfinite([u,*g,*eigen,*shell])) and eigen.min()>0 and residual<1e-3
                   and error<=self.profile['trap_max_error_mm'] and np.all(shell>u))
        return rows,dict(classification='SIMULATION_ESTIMATE',validity='TRAP_VALID' if valid else 'TRAP_INVALID_MODEL',
                         target_error_mm=error,normalized_gradient_residual=residual,hessian_eigenvalues_au_per_mm2=eigen.tolist(),
                         trap_score=float(eigen.min()/max(abs(u),1)),map_sha256=digest(rows),
                         temperature=self.environment.metadata(),max_supported_mass_mg=None,
                         global_sidelobes='NOT_EXHAUSTIVELY_SEARCHED_WORKSPACE_RESTRICTED')


def nominal_reference(record):
    result=copy.deepcopy(record)
    result['measured_pose']['pose']=[0,0,.1,0,0,0]
    result['classification']='SYNTHETIC_REFERENCE'
    result['calibration_id']='NOMINAL_ZERO_ERROR_REFERENCE_NOT_HARDWARE'
    result['f_work']=40000.
    result['sound_speed']=331.3+.606*25
    for ch in result['channels']:
        ch.update(phase_error_rad=0.,relative_amplitude=1.,active_mask=True)
    return result
