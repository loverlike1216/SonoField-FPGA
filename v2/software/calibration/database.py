import hashlib
import json
from pathlib import Path
import numpy as np


def canonical(data):
    return json.dumps(data,sort_keys=True,indent=2,allow_nan=False)+'\n'


def save(root, record):
    required=['schema_version','project_version','git_commit','board_revision','upper_board_id','lower_board_id',
              'tx_batch','rx_batch','timestamp','environment','sound_speed','adc_sample_rate','burst_configuration',
              'measured_pose','f_work','channels','source_raw_data','classification']
    if any(k not in record for k in required):raise ValueError('Incomplete calibration provenance')
    if len(record['channels'])!=128 or record['project_version']!='v2':raise ValueError('Invalid calibration identity')
    text=canonical(record);digest=hashlib.sha256(text.encode()).hexdigest();root=Path(root)
    archive=root/'archive'/f'{digest}.json';archive.parent.mkdir(parents=True,exist_ok=True)
    if archive.exists() and archive.read_text(encoding='utf-8')!=text:raise ValueError('Archive collision')
    archive.write_text(text,encoding='utf-8',newline='\n')
    latest=root/'latest';latest.mkdir(exist_ok=True);temporary=latest/'calibration.json.tmp'
    temporary.write_text(text,encoding='utf-8',newline='\n');temporary.replace(latest/'calibration.json')
    return digest


def decode_frames(raw):
    if len(raw)%16:raise ValueError('Truncated 8-channel frame')
    return np.frombuffer(raw,dtype='<i2').reshape(-1,8).copy()
