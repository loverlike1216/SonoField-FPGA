import numpy as np


def resonance(frequencies, amplitudes):
    f=np.asarray(frequencies);a=np.asarray(amplitudes);valid=np.isfinite(a)&(a>0)
    if valid.sum()<3:return {'f0_hz':None,'quality':'INVALID','bandwidth_hz':None}
    i=int(np.nanargmax(np.where(valid,a,np.nan)));peak=float(f[i]);quality='EDGE'
    if 0<i<len(f)-1 and valid[i-1:i+2].all():
        poly=np.polyfit(f[i-1:i+2]-f[i],np.log(a[i-1:i+2]),2)
        if poly[0]<0:peak+=float(np.clip(-poly[1]/(2*poly[0]),f[i-1]-f[i],f[i+1]-f[i]));quality='GOOD'
    half=np.flatnonzero(valid&(a>=a[i]/np.sqrt(2)))
    bw=float(f[half[-1]]-f[half[0]]) if len(half)>1 and half[0]>0 and half[-1]<len(f)-1 else None
    return {'f0_hz':peak,'peak_amplitude':float(a[i]),'quality':quality,'bandwidth_hz':bw}


def common_frequency(frequencies, amplitudes, weak_fraction=.4):
    a=np.asarray(amplitudes);valid=np.sum(np.isfinite(a)&(a>0),axis=1)>=len(frequencies)*.8
    if valid.sum()<2:raise ValueError('Too few characterized TX channels')
    n=a[valid]/np.nanmax(a[valid],axis=1)[:,None]
    objective=np.nanmedian(n,axis=0)-.2*np.mean(n<weak_fraction,axis=0)
    i=int(np.nanargmax(objective))
    return {'f_work_hz':float(frequencies[i]),'selected_bin':i,'objective_curve':objective.tolist(),
            'selected_channel_count':int(valid.sum()),'rejected_channels':np.flatnonzero(~valid).tolist(),
            'justification':'Maximum median per-channel normalized amplitude minus 0.2 weak fraction'}
