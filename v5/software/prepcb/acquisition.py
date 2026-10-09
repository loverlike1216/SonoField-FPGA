"""Sparse single-TX acquisition using the preserved Controller API.

No default phase reference or coarse uncertainty is safe enough to unwrap a
physical carrier. Frontend references must be supplied and qualified externally.
"""
from pathlib import Path
import hashlib,json
import numpy as np
from ..calibration.signal import estimate_tof,fit_carrier,capture_quality
from .sparse import scan_plan,refine_tof

def acquire(controller,config,environment,frontend,output,source_commit,provenance,extra=()):
    if provenance not in ('RAW_ADC','SYNTHETIC_REFERENCE') or not source_commit:
        raise ValueError('Actual source/provenance required')
    if len(frontend)!=8 or any(not r.get('source') for r in frontend):
        raise ValueError('Eight explicit frontend references required')
    frequency=config['carrier_hz'];clock=config['clock_hz'];fs=config['adc']['sample_rate_hz']
    for r in frontend:
        if (not np.isfinite([r['phase_rad'],r['delay_s'],r['coarse_uncertainty_s']]).all()
                or not 0<r['coarse_uncertainty_s']<.45/frequency):
            raise ValueError('Independent frontend/coarse bound is unqualified')
        if provenance=='RAW_ADC' and r.get('status')!='MEASURED_QUALIFIED':
            raise ValueError('Physical capture needs measured frontend qualification')
    output=Path(output);output.mkdir(parents=True,exist_ok=True);results=[]
    plan=scan_plan(extra)
    try:
        for tx in sorted({t for t,_ in plan}):
            controller.configure(config,frequency=frequency,first_tx=tx,count=1)
            controller.start();raw,meta=controller.read_capture()
            if meta['tx']!=tx or raw.shape!=(meta['frame_count'],8) or raw.dtype!=np.dtype('<i2'):
                raise ValueError('Signed capture/channel/timestamp mismatch')
            if meta['sample_period_ticks']!=clock//fs or meta['frequency_hz']!=frequency:
                raise ValueError('Capture clock metadata mismatch')
            name=f'tx_{tx:03d}.bin';payload=raw.astype('<i2').tobytes();(output/name).write_bytes(payload)
            relative=(meta['first_sample_tick']-meta['tx_enable_tick'])/clock
            for _,rx in (p for p in plan if p[0]==tx):
                y=raw[:,rx];reference=frontend[rx];quality=capture_quality(y)
                coarse=estimate_tof(y,fs,frequency,config['burst_cycles'],config['ring_up_s'],config['ring_down_s'])
                start=max(0,int(np.ceil((coarse['tof_s']+3*config['ring_up_s'])*fs)))
                stop=min(len(y),int((coarse['tof_s']+config['burst_cycles']/frequency)*fs))
                fit=fit_carrier(y,fs,frequency,np.arange(start,stop))
                # Fit cos(+wt): measured phase = frontend + w*t0 - w*TOF.
                phase=(reference['phase_rad']+2*np.pi*frequency*relative-fit['phase_rad'])%(2*np.pi)
                tof=coarse['tof_s']+relative-reference['delay_s']
                flags=[]
                if quality['clipping_count']:flags.append('SATURATED')
                if fit['snr_db']<35:flags.append('LOW_SNR')
                try:refine_tof(tof,phase,frequency,reference['coarse_uncertainty_s'])
                except ValueError:flags.append('AMBIGUOUS_OR_INCONSISTENT_TOF')
                results.append(dict(tx_id=tx,rx_id=rx,board='upper' if tx<64 else 'lower',
                    cmd_start_tick=meta['burst_tick'],actual_tx_onset_tick=meta['tx_enable_tick'],
                    convst_first_tick=meta['first_sample_tick'],sample_period=meta['sample_period_ticks'],
                    raw_ref=name,raw_sha256=hashlib.sha256(payload).hexdigest(),carrier_frequency=frequency,
                    temperature_vector=environment.metadata(),humidity=environment.humidity,
                    quality_flags=flags,SNR=fit['snr_db'],amplitude=fit['amplitude'],phase=float(phase),
                    TOF_candidate=float(tof),coarse_uncertainty_s=reference['coarse_uncertainty_s'],
                    coarse_ambiguity='EXTERNAL_FRONTEND_QUALIFICATION_REQUIRED',frontend_delay=reference,
                    source_commit=source_commit,provenance=provenance))
            # Persist actual metadata/raw before allowing the capture buffer to advance.
            (output/f'tx_{tx:03d}_metadata.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
            controller.acknowledge()
    finally:controller.abort()
    (output/'observations.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    return results
