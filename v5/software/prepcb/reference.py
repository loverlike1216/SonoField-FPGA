"""Explicit numerical test inputs; never sensor/ADC hardware observations."""
import numpy as np
from ..calibration.config import load
from ..calibration.geometry import positions
from .sparse import scan_plan


def synthetic_observations(seed, environment, pose=None):
    pose=pose if pose is not None else [.0007,-.0005,.1008,.35,-.2,.15]
    tx,rx=positions(load(),pose,centered=True);rng=np.random.default_rng(seed)
    delays=np.array([0,.2,-.15,.1,0,-.1,.15,-.2])*1e-6
    result=[]
    for t,r in scan_plan():
        tau=environment.reference_time(tx[t],rx[r])+delays[r]
        fine=tau+rng.normal(0,8e-9)
        result.append(dict(tx_id=t,rx_id=r,board='upper' if t<64 else 'lower',
            cmd_start_tick=0,actual_tx_onset_tick=0,convst_first_tick=0,sample_period=165,
            raw_ref=None,carrier_frequency=40000,temperature_vector=environment.metadata(),humidity=None,
            quality_flags=[],SNR=35,amplitude=1,phase=float(fine*40000*2*np.pi)%(2*np.pi),
            TOF_candidate=float(tau+rng.normal(0,5e-7)),coarse_uncertainty_s=4e-6,
            coarse_ambiguity='INDEPENDENT_COARSE_REFERENCE',frontend_delay='RX0_RX4_FIXED_GAUGES',
            source_commit='RUNTIME_NUMERICAL_REFERENCE',provenance='SYNTHETIC_REFERENCE'))
    return result
