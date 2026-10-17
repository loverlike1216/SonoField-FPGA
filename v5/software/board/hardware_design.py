"""Pre-manufacture calculations and fail-off contracts, never hardware access.

All allocation/derating inputs are engineering hypotheses. None is a measured
load, a guaranteed thermal limit or a substitute for component qualification.
"""
from dataclasses import dataclass
import math


def _positive(*values):
    if any(not math.isfinite(x) or x <= 0 for x in values):
        raise ValueError('Finite positive parameters required')


def capacitive_power(capacitance_nf=2.64, swing_v=12., frequency_hz=40000., channels=64, active_fraction=1.):
    _positive(capacitance_nf, swing_v, frequency_hz, channels)
    if not math.isfinite(active_fraction) or not 0 <= active_fraction <= 1:
        raise ValueError('active_fraction must be in [0,1]')
    return capacitance_nf * 1e-9 * swing_v**2 * frequency_hz * channels * active_fraction


def source_limit(rated_w, headroom=.30, derating=1.):
    _positive(rated_w, derating)
    if not math.isfinite(headroom) or headroom < 0 or derating > 1:
        raise ValueError('Invalid margin/derating')
    return rated_w * derating / (1 + headroom)


def array_power(*, motional_w=None, driver_extra_w=None, auxiliary_w=None,
                capacitance_nf=2.64, swing_v=12., frequency_hz=40000.,
                cable_loop_ohm=None, efficiency=None):
    """Unknown contributors stay unknown; CV2f is only one contribution.

    driver_extra_w must exclude CV2f energy already counted; efficiency covers
    auxiliary conversion only, since the TX rail is not buck converted here.
    Supply draw solves P_source = P_load + (P_source / V)^2 R on the
    lower-current stable branch. R must describe the complete power loop.
    """
    cap = capacitive_power(capacitance_nf, swing_v, frequency_hz)
    unknown = [k for k, v in locals().copy().items()
               if k in ('motional_w', 'driver_extra_w', 'auxiliary_w', 'cable_loop_ohm', 'efficiency') and v is None]
    if unknown:
        return dict(capacitive_w=cap, total_w=None, status='HOLD', unknown=unknown)
    for val in (motional_w, driver_extra_w, auxiliary_w, cable_loop_ohm):
        if not math.isfinite(val) or val < 0:
            raise ValueError('Nonnegative load/resistance required')
    _positive(efficiency)
    if efficiency > 1:
        raise ValueError('Efficiency >1')
    load = cap + motional_w + driver_extra_w + auxiliary_w / efficiency
    k = cable_loop_ohm / swing_v**2
    discriminant = 1 - 4*k*load
    if discriminant <= 0:
        return dict(capacitive_w=cap, total_w=None, status='INVALID_VOLTAGE_COLLAPSE', unknown=[])
    total = 2*load/(1+math.sqrt(discriminant))
    return dict(capacitive_w=cap, load_w=load, total_w=total,
                cable_loss_w=total-load, status='PARAMETERIZED_NOT_MEASURED', unknown=[])


def usb_avcc(vbus_min, current_a, loop_ohm, switch_drop_v, avcc_min=4.75):
    _positive(vbus_min, avcc_min)
    if any(not math.isfinite(x) or x < 0 for x in (current_a, loop_ohm, switch_drop_v)):
        raise ValueError('Invalid loss')
    delivered = vbus_min - current_a*loop_ohm - switch_drop_v
    return dict(delivered_v=delivered, direct_path_valid=delivered >= avcc_min,
                avcc_min_v=avcc_min, regulator='DIRECT_PATH' if delivered >= avcc_min else 'BUCK_BOOST_REVIEW_REQUIRED')


def i2c_pullup_bounds(capacitance_pf, rise_time_ns=1000., vdd=3.3, vol_max=.4, sink_ma=3.):
    _positive(capacitance_pf, rise_time_ns, vdd, sink_ma)
    if not 0 <= vol_max < vdd:
        raise ValueError('Invalid VOL')
    r_min=(vdd-vol_max)/(sink_ma*1e-3)
    r_max=rise_time_ns*1e-9/(.8473*capacitance_pf*1e-12)
    return dict(r_min_ohm=r_min, r_max_ohm=r_max, feasible=r_min <= r_max)


def adc_serial_budget(sample_hz=800000., sclk_hz=33000000., busy_max_ns=900., overhead_ns=80.):
    _positive(sample_hz, sclk_hz, busy_max_ns)
    if not math.isfinite(overhead_ns) or overhead_ns < 0:
        raise ValueError('Invalid overhead')
    shift_ns=32/sclk_hz*1e9
    available=1e9/sample_hz
    # No read-during-conversion/pipeline assumption permitted without proof.
    return dict(data_only_min_sclk_hz=32*sample_hz, shift_ns=shift_ns,
                serial_total_ns=busy_max_ns+shift_ns+overhead_ns, period_ns=available,
                sequential_feasible=busy_max_ns+shift_ns+overhead_ns <= available,
                status='TIMING_HYPOTHESIS_REQUIRES_DATASHEET_AND_RTL_PROOF')


@dataclass
class InterlockModel:
    """Requirements model for a proposed hardware latch, not circuit proof."""
    latched: bool = True
    armed: bool = False

    def step(self, *, central_ok=True, local_ok=True, estop_closed=True,
             temperature_ok=True, watchdog_ok=True, efuse_ok=True,
             cable_ok=True, pl_request=False, manual_rearm_edge=False):
        healthy=all((central_ok,local_ok,estop_closed,temperature_ok,
                     watchdog_ok,efuse_ok,cable_ok))
        if not healthy:
            self.latched=True
            self.armed=False
        elif manual_rearm_edge and not pl_request:
            self.latched=False
            self.armed=True
        return healthy and self.armed and not self.latched and pl_request


class MuxPolicy:
    """One-hot channel policy; a stuck bus needs independent hardware RESET."""
    def __init__(self):
        self.mask=0
        self.fault=False

    def select(self, channel, *, powered=True):
        if channel not in (0,1,2):
            raise ValueError('Only qualified central/upper/lower domains')
        if self.fault or not powered:
            self.mask=0
            raise RuntimeError('Bus reset or powered segment required')
        self.mask=1 << channel
        return self.mask

    def bus_timeout(self):
        self.mask=0
        self.fault=True
        return 'ASSERT_INDEPENDENT_MUX_RESET_REQUIRED'

    def reset_observed(self):
        self.mask=0
        self.fault=False
