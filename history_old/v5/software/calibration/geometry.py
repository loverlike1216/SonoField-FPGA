"""Lower-board local reference; upper pose = translation(m), xyz Euler(deg)."""
import numpy as np
from scipy.spatial.transform import Rotation
from scipy.optimize import least_squares


def local_geometry(config):
    xy = config['xy_m']
    tx = np.array([(x,y,0) for y in xy for x in xy])
    rx = np.c_[np.array(config['rx_xy_m']),np.zeros(4)]
    return tx, rx


def positions(config, pose=None, centered=False):
    tx, rx = local_geometry(config)
    pose = np.array(pose if pose is not None else [0,0,config['nominal_gap_m'],0,0,0])
    rot = Rotation.from_euler('xyz',pose[3:],degrees=True).as_matrix()
    txs=np.r_[tx@rot.T+pose[:3],tx]; rxs=np.r_[rx@rot.T+pose[:3],rx]
    if centered:
        center=txs.mean(axis=0);txs-=center;rxs-=center
    return txs,rxs


def paths(config):
    # Lower TX first, then upper. Preserve all four receiver paths independently.
    return [(tx,rx) for tx in list(range(64,128))+list(range(64))
            for rx in (range(4) if tx>=64 else range(4,8))]


def distances(config, pose, pairs):
    tx,rx=positions(config,pose)
    return np.linalg.norm(tx[np.array(pairs)[:,0]]-rx[np.array(pairs)[:,1]],axis=1)


def solve_pose(config, pairs, measured, sigma=None):
    measured=np.asarray(measured);pairs=np.asarray(pairs)
    sigma=np.broadcast_to(config['pose']['uncertainty_m'] if sigma is None else sigma,measured.shape)
    valid=np.isfinite(measured)&np.isfinite(sigma)&(sigma>0)
    if valid.sum()<12:raise ValueError('Insufficient valid geometric paths')
    initial=[0,0,config['nominal_gap_m'],0,0,0]
    a=config['pose']['max_angle_deg'];xy=config['pose']['bounds_translation_m'][0]
    bounds=([-xy,-xy,config['gap_range_m'][0],-a,-a,-a],[xy,xy,config['gap_range_m'][1],a,a,a])
    def fit(mask,x):
        return least_squares(lambda p:(distances(config,p,pairs[mask])-measured[mask])/sigma[mask],
                             x,bounds=bounds,loss='soft_l1',x_scale=[.001,.001,.1,1,1,1],max_nfev=300,
                             ftol=1e-11,xtol=1e-11,gtol=1e-11)
    first=fit(valid,initial); residual=distances(config,first.x,pairs)-measured
    accepted=valid&(abs(residual)<config['pose']['outlier_m'])
    if accepted.sum()<12:raise ValueError('No consistent rigid geometry')
    result=fit(accepted,first.x)
    rank=np.linalg.matrix_rank(result.jac)
    if not result.success or rank<6:raise ValueError('Unobservable or unconverged rigid pose')
    residual=distances(config,result.x,pairs)-measured
    return {'pose':result.x.tolist(),'residual_m':[float(v) if np.isfinite(v) else None for v in residual],'accepted':accepted.tolist(),
            'accepted_count':int(accepted.sum()),'rejected_count':int((~accepted).sum()),
            'rms_m':float(np.sqrt(np.mean(residual[accepted]**2))),
            'jacobian_condition':float(np.linalg.cond(result.jac)),'rank':int(rank)}
