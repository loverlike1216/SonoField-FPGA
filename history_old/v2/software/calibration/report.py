"""Complete user-facing calibration report and per-path quality CSV from actual estimators."""
import argparse,csv,json
from pathlib import Path
import numpy as np
from .experiment import run
from .database import canonical


def write_report(record,diagnostics,metrics,output):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    counts={s:sum(c['status']==s for c in record['channels']) for s in ['GOOD','WEAK','OUTLIER','INVALID']}
    rows=[]
    for i,(tx,rx) in enumerate(diagnostics['pairs']):
        tof=diagnostics['tof'][i] or {}
        rows.append({'tx':tx,'rx':rx,**diagnostics['quality'][i],
                     'tof_s':tof.get('tof_s'),'integer_delay':tof.get('integer_delay'),
                     'fractional_delay':tof.get('sample_delay'),'peak_ratio':tof.get('peak_ratio'),
                     'fit_rms':tof.get('fit_rms'),'coarse_distance_m':diagnostics['coarse_distances_m'][i],
                     'refined_distance_m':diagnostics['fine_distances_m'][i],
                     'pose_accepted':record['measured_pose']['accepted'][i],
                     'pose_residual_m':record['measured_pose']['residual_m'][i]})
    with (output/'path_quality.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    q={'classification':record['classification'],'counts':counts,
       'valid_tx_count':128-counts['INVALID'],'weak_tx_count':counts['WEAK'],'invalid_tx_count':counts['INVALID'],
       'paths':len(rows),'paths_with_clipping':sum(x['clipping_count']>0 for x in rows),
       'median_tof_peak_ratio':float(np.median([x['peak_ratio'] for x in rows if x['peak_ratio'] is not None])),
       'mean_circular_phase_agreement':float(np.mean([x['receiver_agreement'] for x in record['channels']])),
       'manual_gap_comparison_mm':record['manual_gap_comparison_mm'],
       'recommended_disabled_channels':[c['channel'] for c in record['channels'] if not c['recommended_mask']],
       'active_disabled_channels':[c['channel'] for c in record['channels'] if not c['active_mask']]}
    (output/'quality_summary.json').write_text(canonical(q),encoding='utf-8')
    sections={'System metadata':{k:record[k] for k in ['project_version','git_commit','board_revision','upper_board_id','lower_board_id','tx_batch','rx_batch','timestamp','classification']},
              'Environment':record['environment'],'Measured pose':record['measured_pose']['pose'],
              'Quality and masks':q,'Metrics':metrics}
    body='# Calibration run report\n\nSIMULATION_ESTIMATE. No physical calibration or levitation claim.\n'
    for title,values in sections.items():body+='\n## '+title+'\n\n```json\n'+canonical(values)+'```\n'
    body+='\nPer-path TOF/ADC/pose quality: path_quality.csv. Per-channel phase/f0/amplitude/health: channel_health.csv.\n'
    body+='Phase references: '+record['phase_reference_provenance']+'\n'
    (output/'report.md').write_text(body,encoding='utf-8')
    return q


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='build/calibration_report');a=p.parse_args()
    record,diag,metrics=run(a.output);write_report(record,diag,metrics,a.output)
