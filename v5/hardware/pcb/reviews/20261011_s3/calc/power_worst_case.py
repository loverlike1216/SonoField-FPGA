"""Reproducible S3 electrical arithmetic; never simulates physical hardware.

The upstream current-limit envelope is separate from the conditional load model.
No typical converter efficiency or missing resonant load is promoted to a guarantee.
"""
from pathlib import Path
import json, math, csv
R = Path(__file__).resolve().parents[1]
ROOT = R.parents[4]
E = ROOT / 'v5/evidence/pcb_s3_20261011'

def calculate(x):
    ilim_lo=x['ilim_table9_min_a']/(1+x['rilim_tolerance'])
    ilim_hi=x['ilim_table9_max_a']/(1-x['rilim_tolerance'])
    array_i=ilim_hi+x['upstream_allowance_a']
    central_i=array_i+x['central_bootstrap_allowance_a']
    c=x['c0_f']*(1+x['c0_tolerance']);v=x['array_v_max'];n=x['tx_count_per_array']
    rr=x['tx_series_ohm']*(1-x['resistor_tolerance'])
    # Full short duty=1 is intentionally included; software duty is not a hard limit.
    short_peak=n*v/rr
    result=dict(ilim_min_a=ilim_lo,ilim_max_a=ilim_hi,
        array_steady_input_max_a=array_i,array_steady_input_max_w=v*array_i,
        central_steady_input_max_a=central_i,central_steady_input_max_w=x['usb_v_max']*central_i,
        adapter_current_margin_a=x['adapter_a']-array_i,
        array_normal_c0_only_w=n*c*v*v*x['switching_hz'],
        tx_all_edges_peak_a=short_peak,
        tx_one_short_continuous_w=v*v/rr,
        tx_all_shorts_unlimited_w=n*v*v/rr,
        tx_edge_charge_c=n*c*v,
        tx_edge_bulk_droop_v=n*c*v/x['tx_bulk_min_f'],
        tx_edge_energy_j=.5*n*c*v*v,
        tx_stored_energy_max_j=.5*x['tx_cap_max_total_f']*v*v,
        tx_bleed_time_to_1v_s=x['tx_bleeder_ohm']*1.01*x['tx_cap_max_total_f']*math.log(v),
        tx_c0_pole_hz=1/(2*math.pi*x['tx_series_ohm']*c),
        tx_c0_40k_gain=1/math.sqrt(1+(2*math.pi*x['switching_hz']*x['tx_series_ohm']*c)**2),
        shunt_at_limit_mv=ilim_hi*.020*1.01*1000,
        shunt_heat_w=ilim_hi**2*.020*1.01,
        efuse_one_heat_w=ilim_hi**2*.045,
        kill_en_undefined_vcc_max_v=1.65*1.01/(.99+1.01)+.0000001*50500,
        kill_en_normal_min_v=(3.15-.2)*.99/(1.01+.99)-.0000001*50500,
        central_boost_min_v=.8*.99*(1+68.7*.999/(10*1.001))-.0000001*68700-.020,
        central_boost_max_v=.8*1.01*(1+68.7*1.001/(10*.999))+.0000001*68700+.020,
        adc_avcc_min_v=5*.982,adc_avcc_max_v=5*1.018,
        heartbeat_valid=x['heartbeat_fall_min_s']>x['watchdog_lower_max_s'] and x['heartbeat_fall_max_s']<x['watchdog_upper_min_s'],
        conclusion='STEADY_LIMIT_ENVELOPE_ONLY; FAST_FAULT_AND_C0_MODEL_NOT_GUARANTEED')
    assert result['shunt_at_limit_mv']<81.92
    assert result['kill_en_undefined_vcc_max_v']<1.076
    assert result['kill_en_normal_min_v']>1.223
    assert result['central_boost_min_v']>5*1.018+1
    assert result['heartbeat_valid'] and array_i<3 and central_i<3
    return result

def main():
    x=json.loads((R/'calc/inputs.json').read_text(encoding='utf-8')); out=calculate(x)
    E.mkdir(parents=True,exist_ok=True)
    (E/'POWER_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
