"""Export reproducible calibration/field diagnostics; amplitudes are relative, not Pa."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation
from .geometry import positions,paths
from .pipeline import phase_lut


def render(config,record,diagnostics,output):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    def finish(fig,name):
        fig.tight_layout();fig.savefig(output/(name+'.png'),dpi=150);plt.close(fig)
    ch=record['channels'];freq=config['sweep_hz'];response=diagnostics['amplitude_response']
    fig,ax=plt.subplots(1,2,figsize=(11,4))
    ax[0].plot(freq,(response/np.nanmax(response,axis=1)[:,None]).T,alpha=.15);ax[0].axvline(record['f_work'],color='black')
    ax[0].set(xlabel='Frequency (Hz)',ylabel='Normalized received amplitude',title='128 TX resonance curves')
    ax[1].hist([x['f0_hz'] for x in ch if x['f0_hz'] is not None],bins=20);ax[1].set(xlabel='Estimated f0 (Hz)',ylabel='TX count')
    finish(fig,'resonance')
    fig,ax=plt.subplots(2,2,figsize=(9,7))
    for row,(key,title) in enumerate([('phase_error_rad','Phase error (rad)'),('relative_amplitude','Relative amplitude')]):
        for bank in range(2):
            values=np.array([x[key] for x in ch[bank*64:(bank+1)*64]],dtype=float).reshape(8,8)
            im=ax[row,bank].imshow(values,origin='lower',extent=(-48,48,-48,48));fig.colorbar(im,ax=ax[row,bank])
            ax[row,bank].set(title=('UPPER ' if bank==0 else 'LOWER ')+title,xlabel='x (mm)',ylabel='y (mm)')
    finish(fig,'channel_heatmaps')
    fig,ax=plt.subplots(1,2,figsize=(11,4));coarse=np.array(record['coarse_pose']['residual_m'],dtype=float)*1000
    fine=np.array(record['measured_pose']['residual_m'],dtype=float)*1000
    ax[0].plot(coarse,label='Envelope TOF',alpha=.7);ax[0].plot(fine,label='Conditional phase refinement',alpha=.7)
    ax[0].set(xlabel='Directed path index',ylabel='Pose residual (mm)');ax[0].legend(fontsize=8)
    ax[1].hist(coarse[np.isfinite(coarse)],bins=30,alpha=.6,label='Envelope');ax[1].hist(fine[np.isfinite(fine)],bins=30,alpha=.6,label='Phase')
    ax[1].set(xlabel='Residual (mm)',ylabel='Path count');ax[1].legend();finish(fig,'pose_residuals')
    # Evaluate both LUTs in the SAME estimated actual geometry, so model correction
    # is visible. No truth object, calibrated absolute pressure or force is supplied.
    tx,_=positions(config,record['measured_pose']['pose'],centered=True)
    normals=np.r_[np.tile(Rotation.from_euler('xyz',record['measured_pose']['pose'][3:],degrees=True).apply([0,0,-1]),(64,1)),np.tile([0,0,1],(64,1))]
    errors=np.array([x['phase_error_rad'] or 0 for x in ch]);amp=np.array([x['relative_amplitude'] or 0 for x in ch])
    axis=np.linspace(-.015,.015,101);a,b=np.meshgrid(axis,axis);metrics={}
    for field_mode in ['FOCUS','STANDING_WAVE']:
        fig,axes=plt.subplots(2,3,figsize=(12,7));images=[]
        for row,geometry_mode in enumerate(['NOMINAL','CALIBRATED']):
            lut=phase_lut(config,record,geometry_mode=geometry_mode,field_mode=field_mode)
            phase=2*np.pi*np.array([x['effective_phase'] for x in lut])/256
            for col,plane in enumerate(['XY','XZ','YZ']):
                points=np.c_[a.ravel(),b.ravel(),np.zeros(a.size)]
                if plane=='XZ':points=points[:,[0,2,1]]
                if plane=='YZ':points=points[:,[2,0,1]]
                delta=points[:,None,:]-tx;distance=np.linalg.norm(delta,axis=2)
                direct=np.maximum(0,np.einsum('ptc,tc->pt',delta,normals)/distance)**2
                p=np.abs(np.sum(amp*direct/distance*np.exp(1j*(2*np.pi*record['f_work']*distance/record['sound_speed']+phase-errors)),axis=1)).reshape(a.shape)
                images.append((axes[row,col],p));axes[row,col].set(title=geometry_mode+' '+plane,xlabel=plane[0]+' (mm)',ylabel=plane[1]+' (mm)')
                metrics[field_mode+'_'+geometry_mode+'_'+plane]={'central_relative_pressure':float(p[50,50]),'peak_relative_pressure':float(p.max())}
        scale=max(x.max() for _,x in images)
        for ax,p in images:im=ax.imshow(p,origin='lower',extent=(-15,15,-15,15),vmin=0,vmax=scale,cmap='magma');fig.colorbar(im,ax=ax)
        fig.suptitle(field_mode+' / SIMULATION_ESTIMATE / relative pressure (not force)',fontsize=11)
        finish(fig,'field_'+field_mode.lower())
    (output/'field_metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
