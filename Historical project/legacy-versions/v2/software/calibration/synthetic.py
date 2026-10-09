"""Reproducible physical-source substitute; the estimator never receives this truth object."""
import numpy as np
from scipy.spatial.transform import Rotation
from .geometry import positions
from .sound_speed import sound_speed
from .signal import envelope


def truth(config, seed=None):
    rng=np.random.default_rng(config['synthetic']['seed'] if seed is None else seed)
    rxphase=rng.normal(0,.25,8);rxphase[[0,4]]=config['phase_reference']['rx_anchor_phase_rad']
    rxdelay=rng.uniform(-15e-9,15e-9,8);rxdelay[[0,4]]=0
    gain=rng.uniform(.8,1.2,128);gain[7]=.15
    return {'pose':config['synthetic']['pose'],'f0':rng.uniform(39300,40700,128),
            'bandwidth':rng.uniform(1000,1500,128),'tx_phase':rng.uniform(-1.2,1.2,128),
            'tx_gain':gain,'rx_phase':rxphase,'rx_gain':rng.uniform(.9,1.1,8),'rx_delay':rxdelay}


def generate(config, injected, frequency, snr_db=None, seed=7020, echo=0, gain_scale=1):
    fs=config['adc']['sample_rate_hz'];n=sum(config[k] for k in ['pretrigger_samples','main_samples','ringdown_samples'])
    time=np.arange(n)/fs;start=config['pretrigger_samples']/fs
    env=config['environment'];c=sound_speed(env['temperature_c'],env['humidity_percent'],env['pressure_pa'],env['co2_ppm'])
    txpos,rxpos=positions(config,injected['pose']);rng=np.random.default_rng(seed)
    noise=10**(-(config['synthetic']['snr_db'] if snr_db is None else snr_db)/20)/np.sqrt(2)
    data=np.empty((128,n,8),dtype=np.int16)
    normals=np.r_[np.tile(Rotation.from_euler('xyz',injected['pose'][3:],degrees=True).apply([0,0,-1]),(64,1)),np.tile([0,0,1],(64,1))]
    duration=config['burst_cycles']/frequency
    for tx in range(128):
        v=rxpos-txpos[tx];d=np.linalg.norm(v,axis=1);cos=np.clip(v@normals[tx]/np.maximum(d,1e-9),0,1)
        active=np.array([rx<4 if tx>=64 else rx>=4 for rx in range(8)])
        response=1/(1+1j*2*(frequency-injected['f0'][tx])/injected['bandwidth'][tx])
        amp=.65*gain_scale*injected['tx_gain'][tx]*injected['rx_gain']*abs(response)*(.1/np.maximum(d,.02))*cos**2*active
        delay=start+d/c+injected['rx_delay'];local=time[:,None]-delay
        shape=envelope(local,duration,config['ring_up_s'],config['ring_down_s'])
        phase=2*np.pi*frequency*local+injected['tx_phase'][tx]+injected['rx_phase']+np.angle(response)
        volts=2.5+amp*shape*np.cos(phase)
        if echo:
            volts+=echo*amp*envelope(local-45e-6,duration,config['ring_up_s'],config['ring_down_s'])*np.cos(phase-2*np.pi*frequency*45e-6)
        volts+=rng.normal(0,max(.65*noise,1e-6),volts.shape)
        data[tx]=np.clip(np.rint(volts/config['adc']['range_v']*32768),-32768,32767).astype(np.int16)
    return data
