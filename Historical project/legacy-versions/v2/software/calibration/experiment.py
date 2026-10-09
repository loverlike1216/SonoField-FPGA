"""Reproducible end-to-end experiment. Raw vectors stay in ignored build; summaries are small."""
import argparse, csv, hashlib, json, subprocess
from pathlib import Path
import numpy as np
from .config import load, ROOT
from .synthetic import truth, generate
from .pipeline import process, phase_lut
from .database import save, canonical
from .signal import circular_residual


def run(output, snr=None, save_raw=True):
    output=Path(output);output.mkdir(parents=True,exist_ok=True);cfg=load();gt=truth(cfg)
    freq=cfg['sweep_hz'];raw=np.stack([generate(cfg,gt,f,snr_db=snr,seed=cfg['synthetic']['seed']+i) for i,f in enumerate(freq)])
    sha=hashlib.sha256(raw.tobytes()).hexdigest()
    rawpath=ROOT/'build/calibration_raw'/f'{sha}.npz'
    if save_raw:
        rawpath.parent.mkdir(parents=True,exist_ok=True)
        if not rawpath.exists():np.savez_compressed(rawpath,samples=raw,frequencies=freq)
    metadata={'git_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
              'board_revision':'SYNTHETIC','upper_board_id':'SIM_UPPER','lower_board_id':'SIM_LOWER',
              'tx_batch':'SIM_SEED_7020','rx_batch':'SIM_SEED_7020','timestamp':'2000-01-01T00:00:00Z',
              'timestamp_policy':'fixed simulation epoch, not a physical measurement date',
              'classification':'SIMULATION_ESTIMATE','manual_face_gap_mm':None}
    record,diag=process(cfg,raw,freq,metadata,[{'path':str(rawpath.relative_to(ROOT)), 'raw_int16_sha256':sha,
                     'shape':list(raw.shape),'dtype':'little-endian signed int16','order':'frequency,TX,frame,ADC_channel',
                     'trigger_sample':cfg['pretrigger_samples'],'sequence':'TX64..127 then TX0..63; opposite bank four paths each'}])
    digest=save(output/'database',record)
    try:lut=phase_lut(cfg,record);lut_status='GENERATED'
    except ValueError as exc:lut=None;lut_status='BLOCKED: '+str(exc)
    tables=[('channel_health',record['channels'])]+([('phase_lut',lut)] if lut is not None else [])
    for name,rows in tables:
        with (output/f'{name}.csv').open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    (output/'calibration.json').write_text(canonical(record),encoding='utf-8')
    response=1/(1+1j*2*(record['f_work']-gt['f0'])/gt['bandwidth'])
    estimates=np.array([c['phase_error_rad'] if c['phase_error_rad'] is not None else np.nan for c in record['channels']])
    f0=np.array([c['f0_hz'] if c['f0_hz'] is not None else np.nan for c in record['channels']])
    err=np.array(record['measured_pose']['pose'])-gt['pose']
    metrics={'snr_db':cfg['synthetic']['snr_db'] if snr is None else snr,'translation_error_mm':float(np.linalg.norm(err[:3])*1000),
             'rotation_error_deg':float(np.linalg.norm(err[3:])),'pose_rms_mm':record['measured_pose']['rms_m']*1000,
             'f0_rmse_hz':float(np.sqrt(np.nanmean((f0-gt['f0'])**2))),
             'phase_rmse_deg':float(np.rad2deg(np.sqrt(np.nanmean(circular_residual(estimates,gt['tx_phase']+np.angle(response))**2)))),
             'valid_channels':int(np.isfinite(estimates).sum()),'path_count':len(diag['pairs']),
             'f_work_hz':record['f_work'],'record_sha256':digest,'raw_sha256':sha,'lut_status':lut_status}
    (output/'metrics.json').write_text(canonical(metrics),encoding='utf-8')
    (output/'report.md').write_text('# Synthetic calibration\n\nSIMULATION_ESTIMATE. No physical measurements.\n\n'+
        '\n'.join(f'- {k}: {v}' for k,v in metrics.items())+'\n\nPhase values require the declared RX phase reference; pressure is relative only.\n',encoding='utf-8')
    np.savez(output/'diagnostics.npz',frequencies=freq,response=diag['amplitude_response'],pairs=diag['pairs'],
             distances=diag['coarse_distances_m'],truth_f0=gt['f0'],truth_phase=gt['tx_phase'],truth_pose=gt['pose'])
    print(json.dumps(metrics),flush=True)
    return record,diag,metrics


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='build/calibration_run');p.add_argument('--snr',type=float)
    a=p.parse_args();run(a.output,a.snr)
