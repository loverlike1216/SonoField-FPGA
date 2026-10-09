"""Raw ADC -> geometry -> response -> relative phase -> database and separate LUT fields."""
import numpy as np
from .geometry import paths, positions, distances, solve_pose
from .signal import estimate_tof, fit_carrier, circular_mean, circular_residual, capture_quality, fuse_distance
from .sound_speed import sound_speed
from ..characterization.response import resonance, common_frequency
from ..acoustic_model.phase_solver import quantize_phase


def process(config, captures, frequencies, metadata, raw_sources):
    if metadata.get('classification')!='SIMULATION_ESTIMATE' and 'SIMULATION' in config['phase_reference']['reference_provenance']:
        raise ValueError('A real capture cannot use a simulated RX phase reference')
    fs=config['adc']['sample_rate_hz'];env=config['environment']
    c=sound_speed(env['temperature_c'],env['humidity_percent'],env['pressure_pa'],env['co2_ppm'])
    pairs=paths(config);base=int(np.argmin(abs(np.array(frequencies)-config['carrier_hz'])))
    f=frequencies[base];coarse=[];tof_reports=[];quality=[]
    for tx,rx in pairs:
        codes=captures[base,tx,:,rx];q=capture_quality(codes);quality.append(q)
        if q['clipping_count']:
            coarse.append(np.nan);tof_reports.append(None);continue
        est=estimate_tof(codes,fs,f,config['burst_cycles'],config['ring_up_s'],config['ring_down_s'])
        coarse.append((est['tof_s']-config['pretrigger_samples']/fs)*c);tof_reports.append(est)
    pose=solve_pose(config,pairs,coarse);d=distances(config,pose['pose'],pairs)
    amplitudes=np.full((128,len(frequencies),4),np.nan);phases=amplitudes.copy();snrs=amplitudes.copy()
    for fi,f in enumerate(frequencies):
        for pi,(tx,rx) in enumerate(pairs):
            if not pose['accepted'][pi]:continue
            codes=captures[fi,tx,:,rx]
            if capture_quality(codes)['clipping_count']:continue
            arrival=config['pretrigger_samples']/fs+d[pi]/c
            idx=np.arange(int((arrival+6/f)*fs),min(len(codes),int((arrival+(config['burst_cycles']-2)/f)*fs)))
            fitted=fit_carrier(codes,fs,f,idx)
            if fitted['snr_db']<config['health']['min_snr_db']:continue
            # Normalize directional/inverse-distance measurement for TX health comparison.
            amplitudes[tx,fi,rx%4]=fitted['amplitude']
            phases[tx,fi,rx%4]=circular_residual(fitted['phase_rad']+2*np.pi*f*(config['pretrigger_samples']/fs+d[pi]/c))
            snrs[tx,fi,rx%4]=fitted['snr_db']
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore',RuntimeWarning);response=np.nanmedian(amplitudes,axis=2)
    common=common_frequency(frequencies,response,config['health']['weak_fraction']);fi=common['selected_bin'];f=common['f_work_hz']
    y=phases[:,fi,:];errors=np.full(128,np.nan);agreement=np.zeros(128);rx_errors=np.zeros(8)
    anchors=config['phase_reference'].get('rx_anchor_phase_rad')
    # Each directional graph has its own phase gauge. Explicit external anchors are optional.
    for group,ids in [(0,np.arange(64,128)),(1,np.arange(64))]:
        local=y[ids];anchor=0 if anchors is None else anchors[group]
        rx_errors[4*group]=anchor
        for j in range(1,4):
            ok=np.isfinite(local[:,j])&np.isfinite(local[:,0])
            if ok.sum()<4:raise ValueError('Unconnected RX phase calibration graph')
            rx_errors[4*group+j]=circular_mean(local[ok,j]-local[ok,0])[0]+anchor
        for tx in ids:
            ok=np.isfinite(y[tx]);
            if ok.any():errors[tx],agreement[tx]=circular_mean(y[tx,ok]-rx_errors[4*group:4*group+4][ok])
    # Conditional phase refinement: coarse TOF selects the wavelength branch; fitted
    # TX/RX nuisance phases remove chain phase. This is NOT an independent absolute
    # ruler. Keep both solutions and the identifiable-reference statement in the DB.
    fine=[]
    for pi,(tx,rx) in enumerate(pairs):
        observed=y[tx,rx%4]-2*np.pi*f*d[pi]/c
        fine.append(fuse_distance(coarse[pi],observed,f,c,errors[tx]+rx_errors[rx])
                    if np.isfinite(observed) and np.isfinite(coarse[pi]) else np.nan)
    refined=solve_pose(config,pairs,fine)
    coarse_pose=pose
    # Reject a conditional refinement inconsistent with the envelope measurement.
    if np.linalg.norm(np.array(refined['pose'])[:3]-np.array(pose['pose'])[:3])>.0005:
        raise ValueError('Phase refinement conflicts with coarse geometry')
    pose=refined
    new_d=distances(config,pose['pose'],pairs)
    for tx in range(128):
        shifts=[2*np.pi*f*(new_d[i]-d[i])/c for i,(t,rx) in enumerate(pairs) if t==tx and np.isfinite(fine[i])]
        if shifts:errors[tx]=float(circular_residual(errors[tx]+np.mean(shifts)))
    # Geometry compensated amplitude factor is an analysis weight, not analog drive control.
    txp,rxp=positions(config,pose['pose']);path_gain=np.zeros((128,4))
    from scipy.spatial.transform import Rotation
    upper_normal=Rotation.from_euler('xyz',pose['pose'][3:],degrees=True).apply([0,0,-1])
    for tx,rx in pairs:
        v=rxp[rx]-txp[tx];length=np.linalg.norm(v);co=max(0,float(v@(upper_normal if tx<64 else np.array([0,0,1]))/length))
        path_gain[tx,rx%4]=(.1/length)*co**2
    with warnings.catch_warnings():
        warnings.simplefilter('ignore',RuntimeWarning);relative=np.nanmedian(amplitudes[:,fi,:]/path_gain,axis=1)
    relative/=np.nanmedian(relative)
    channels=[]
    for tx in range(128):
        res=resonance(frequencies,response[tx]);a=relative[tx]
        status='INVALID' if not np.isfinite(a) or not np.isfinite(errors[tx]) else ('WEAK' if a<config['health']['weak_fraction'] else ('OUTLIER' if a>config['health']['outlier_fraction'] else 'GOOD'))
        channels.append({'channel':tx,'channel_id':('UPPER' if tx<64 else 'LOWER')+f'_TX_{tx%64:02d}',**res,
                         'relative_amplitude':float(a) if np.isfinite(a) else None,'phase_error_rad':float(errors[tx]) if np.isfinite(errors[tx]) else None,
                         'receiver_agreement':float(agreement[tx]),'status':status,'recommended_mask':status=='GOOD',
                         'active_mask':status=='GOOD' if config['health']['apply_recommended_mask'] else True})
    record={'schema_version':1,'project_version':'v2',**metadata,'environment':env,'sound_speed':c,'adc_sample_rate':fs,
            'burst_configuration':{k:config[k] for k in ['burst_cycles','pretrigger_samples','main_samples','ringdown_samples']},
            'measured_pose':pose,'coarse_pose':coarse_pose,
            'refinement_status':'CONDITIONAL_ON_FITTED_CHAIN_PHASE; envelope fixes absolute gauge',
            'f_work':f,'channels':channels,'source_raw_data':raw_sources,'common_frequency':common,
            'rx_phase_rad':rx_errors.tolist(),'phase_reference':'EXPLICIT_RX_ANCHORS' if anchors is not None else 'RELATIVE_PER_BANK_ONLY',
            'phase_reference_provenance':config['phase_reference']['reference_provenance'],
            'manual_gap_comparison_mm':None if metadata.get('manual_face_gap_mm') is None else pose['pose'][2]*1000-metadata['manual_face_gap_mm']}
    diagnostics={'pairs':pairs,'coarse_distances_m':coarse,'fine_distances_m':fine,'tof':tof_reports,'quality':quality,'amplitude_response':response,'phase_response':phases}
    return record,diagnostics


def phase_lut(config,record,target=(0,0,0),geometry_mode='CALIBRATED',field_mode='FOCUS'):
    if record['phase_reference']!='EXPLICIT_RX_ANCHORS':
        raise ValueError('A whole-array LUT requires an explicit cross-bank RX phase reference')
    if any(c['active_mask'] and c['phase_error_rad'] is None for c in record['channels']):
        raise ValueError('Active channel lacks valid calibration; explicitly approve a mask before generating a LUT')
    if geometry_mode not in ('NOMINAL','CALIBRATED'):raise ValueError('Explicit geometry mode required')
    if field_mode not in ('FOCUS','STANDING_WAVE'):raise ValueError('Unknown field mode')
    tx,_=positions(config,record['measured_pose']['pose'] if geometry_mode=='CALIBRATED' else None,centered=True)
    phase=-2*np.pi*record['f_work']*np.linalg.norm(tx-np.asarray(target),axis=1)/record['sound_speed']
    if field_mode=='STANDING_WAVE':phase[64:]+=np.pi
    # RTL phase code is a temporal lag. cos(+wt+error) requires positive lag correction = error.
    correction=np.array([c['phase_error_rad'] or 0 for c in record['channels']])
    req=quantize_phase(phase,config['phase_bits']);cal=quantize_phase(correction,config['phase_bits'])
    return [{'channel':i,'channel_id':record['channels'][i]['channel_id'],'requested_phase':int(req[i]),
             'calibration_phase':int(cal[i]),'effective_phase':int((req[i]+cal[i])%256),
             'enabled':int(record['channels'][i]['active_mask'])} for i in range(128)]
