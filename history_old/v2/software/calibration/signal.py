"""Real estimators operating on raw vectors, with no injected geometry/phase answers."""
import numpy as np
from scipy.signal import correlate
from scipy.optimize import minimize_scalar


def circular_residual(x,y=0):return np.angle(np.exp(1j*(np.asarray(x)-y)))


def circular_mean(x,weights=None):
    z=np.average(np.exp(1j*np.asarray(x)),weights=weights)
    return float(np.angle(z)),float(abs(z))


def envelope(time, duration, rise, fall):
    t=np.asarray(time)
    return np.where(t<0,0,np.where(t<=duration,1-np.exp(-np.maximum(t,0)/rise),
                    (1-np.exp(-duration/rise))*np.exp(-np.maximum(t-duration,0)/fall)))


def fit_carrier(samples, fs, frequency, indices=None):
    y=np.asarray(samples,dtype=float)
    idx=np.arange(len(y)) if indices is None else np.asarray(indices)
    if len(idx)<8:raise ValueError('Insufficient carrier window')
    angle=2*np.pi*frequency*idx/fs
    design=np.c_[np.cos(angle),np.sin(angle),np.ones(len(idx))]
    coeff=np.linalg.lstsq(design,y[idx],rcond=None)[0]
    residual=y[idx]-design@coeff
    amp=float(np.hypot(*coeff[:2]));noise=float(np.sqrt(np.mean(residual**2)))
    return {'phase_rad':float(np.arctan2(-coeff[1],coeff[0])), 'amplitude':amp,
            'dc':float(coeff[2]),'snr_db':float(20*np.log10(max(amp/np.sqrt(2),1e-12)/max(noise,1e-12)))}


def estimate_tof(samples, fs, frequency, cycles, rise, fall):
    y=np.asarray(samples,dtype=float); y=y-np.mean(y[:max(8,int(.00002*fs))])
    duration=cycles/frequency;nt=min(len(y),int((duration+6*fall)*fs))
    t=np.arange(nt)/fs;e=envelope(t,duration,rise,fall)
    # Quadrature matched filter avoids carrier phase changing the coarse peak.
    corr=np.hypot(correlate(y,e*np.cos(2*np.pi*frequency*t),mode='full',method='fft'),
                  correlate(y,e*np.sin(2*np.pi*frequency*t),mode='full',method='fft'))
    lags=np.arange(-nt+1,len(y)); good=(lags>=0)&(lags<len(y)-duration*fs)
    values=np.where(good,corr,-np.inf); peak=int(np.argmax(values));lag=float(lags[peak])
    if 0<peak<len(values)-1:
        a,b,c=values[peak-1:peak+2];den=a-2*b+c
        if np.isfinite(den) and den:lag+=float(np.clip(.5*(a-c)/den,-.5,.5))
    time=np.arange(len(y))/fs;cos=np.cos(2*np.pi*frequency*time);sin=np.sin(2*np.pi*frequency*time)
    def objective(delay):
        env=envelope(time-delay/fs,duration,rise,fall)
        x=np.c_[env*cos,env*sin,np.ones(len(y))]
        coef=np.linalg.lstsq(x,y,rcond=None)[0]
        return float(np.mean((y-x@coef)**2))
    refined=minimize_scalar(objective,bounds=(max(0,lag-fs/frequency),lag+fs/frequency),method='bounded',options={'xatol':1e-5})
    excluded=values.copy();excluded[abs(lags-lags[peak])<fs/frequency]=-np.inf
    second=float(np.max(excluded));quality=float(values[peak]/max(second,1e-12))
    return {'sample_delay':float(refined.x),'integer_delay':int(lags[peak]),'parabolic_delay':lag,
            'tof_s':float(refined.x/fs),'peak':float(values[peak]),'peak_ratio':quality,
            'fit_rms':float(np.sqrt(refined.fun))}


def fuse_distance(coarse_m, phase_rad, frequency, sound_speed, chain_phase_rad=0):
    # cos(+wt) phase: observed = chain - k*d. Never use unreferenced phase as absolute distance.
    wavelength=sound_speed/frequency
    fraction=((chain_phase_rad-phase_rad)%(2*np.pi))/(2*np.pi)*wavelength
    return float(fraction+np.round((coarse_m-fraction)/wavelength)*wavelength)


def capture_quality(codes):
    a=np.asarray(codes)
    return {'min_code':int(a.min()),'max_code':int(a.max()),'clipping_count':int(np.count_nonzero((a<=-32768)|(a>=32767))),
            'rms_code':float(np.sqrt(np.mean((a.astype(float)-a.mean())**2))),'peak_code':float(np.max(abs(a.astype(float)-a.mean())))}
