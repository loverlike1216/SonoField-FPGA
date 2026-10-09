"""Single source for system geometry, ADC mapping and capture parameters."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(path=None):
    c = json.loads(Path(path or ROOT/'config/system_baseline.json').read_text(encoding='utf-8'))
    if c['tx_count'] != 128 or c['rx_count'] != 8 or c['adc']['channels'] != 8:
        raise ValueError('Configuration identity mismatch')
    if not 2*max(c['sweep_hz']) < c['adc']['sample_rate_hz'] <= 800000:
        raise ValueError('ADC sample rate outside Nyquist/device limits')
    adc=c['adc']
    if (adc['bits'],adc['lanes'],adc['range_v'],adc['oversampling'],adc['crc'],adc['status_header'])!=(16,4,5.0,1,False,False):
        raise ValueError('Unsupported ADC wire profile; update and revalidate RTL before changing it')
    if adc['lane_channels']!=[[0,1],[2,3],[4,5],[6,7]]:raise ValueError('AD7606B four-DOUT ordering is fixed')
    if c['clock_hz']%adc['sample_rate_hz']:raise ValueError('Sample rate must have an exact integer system-clock period')
    if c['pretrigger_samples'] + c['main_samples'] + c['ringdown_samples'] > c['buffer_depth']:
        raise ValueError('Capture exceeds bounded buffer')
    return c
