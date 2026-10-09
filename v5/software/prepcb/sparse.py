"""Sparse directed geometry calibration; RX0/RX4 delay gauges fixed explicitly.

Single-frequency phase is refined only with independently bounded coarse ToF.
Unmeasured TX response is never promoted to full-channel calibration.
"""
import numpy as np
from scipy.optimize import least_squares
from ..calibration.geometry import positions, distances

DIAGONALS = sorted({8*r+c for r in range(8) for c in (r, 7-r)})
SUGGESTED_EXTRA = [1, 6, 8, 15, 48, 55, 57, 62]


def scan_plan(extra=()):
    if any(type(x) is not int or not 0 <= x < 64 for x in extra):
        raise ValueError('Supplemental TX must be explicit local IDs 0..63')
    ids = sorted(set(DIAGONALS) | set(extra))
    return [(tx+bank*64, rx) for bank in (0, 1) for tx in ids
            for rx in (range(4, 8) if bank == 0 else range(4))]


def refine_tof(coarse_s, phase_rad, frequency, uncertainty_s):
    values = np.array([coarse_s, phase_rad, frequency, uncertainty_s], dtype=float)
    if not np.all(np.isfinite(values)) or not 38500 <= frequency <= 41500:
        raise ValueError('Invalid ToF observation')
    if not 0 < uncertainty_s < .45/frequency:
        raise ValueError('AMBIGUOUS_CARRIER_CYCLE: independent coarse bound required')
    fraction = (phase_rad/(2*np.pi)) % 1
    cycles = int(np.rint(coarse_s*frequency-fraction))
    fine = (cycles+fraction)/frequency
    if fine <= 0 or abs(fine-coarse_s) > uncertainty_s:
        raise ValueError('Coarse/phase disagreement')
    return fine, cycles


def solve(config, observations, environment, starts=5):
    if starts < 5:
        raise ValueError('At least five initial guesses required')
    pairs, measured, valid_ids = [], [], []
    rejected = []
    for i, o in enumerate(observations):
        try:
            tx, rx = o['tx_id'], o['rx_id']
            if not 0 <= tx < 128 or not 0 <= rx < 8 or (tx < 64) == (rx < 4):
                raise ValueError('Not an opposite-board path')
            if o['SNR'] < 35 or o['quality_flags'] or o['provenance'] not in ('SYNTHETIC_REFERENCE', 'RAW_ADC'):
                raise ValueError('Quality/provenance rejected')
            tau, ambiguity = refine_tof(o['TOF_candidate'], o['phase'],
                                        o['carrier_frequency'], o['coarse_uncertainty_s'])
            pairs.append((tx, rx)); measured.append(tau); valid_ids.append(i)
        except (KeyError, ValueError, TypeError) as exc:
            rejected.append({'index': i, 'reason': str(exc)})
    if len(pairs) < 24 or len(set(pairs)) != len(pairs) or {r for _, r in pairs} != set(range(8)):
        raise ValueError('CALIBRATION_BLOCKED_BY_OBSERVABILITY: missing/duplicate paths; extra TX '+str(SUGGESTED_EXTRA))
    pairs = np.asarray(pairs); measured = np.asarray(measured)
    def predicted(x):
        tx, rx = positions(config, x[:6], centered=True)
        delays = np.r_[0., x[6:9], 0., x[9:12]]*1e-6
        return np.array([environment.travel_time(tx[t], rx[r], nodes=8)+delays[r] for t, r in pairs])
    # Angle scaled to degrees; RX delays use microseconds for readable conditioning.
    lower = [-.005, -.005, .09, -3, -3, -3]+[-10]*6
    upper = [.005, .005, .115, 3, 3, 3]+[10]*6
    candidates = []
    for j in range(starts):
        initial = np.r_[0., 0., config['nominal_gap_m']+(j-(starts-1)/2)*.0004,
                        .1*np.sin(j), .1*np.cos(j), 0., np.zeros(6)]
        fit = least_squares(lambda x: (predicted(x)-measured)/5e-8, initial,
                            bounds=(lower, upper), loss='soft_l1',
                            x_scale=[.001, .001, .1, 1, 1, 1]+[1]*6, max_nfev=160,
                            ftol=1e-10, xtol=1e-10, gtol=1e-10)
        candidates.append(fit)
    fit = min(candidates, key=lambda f: f.cost)
    residual = predicted(fit.x)-measured
    accepted = abs(residual) < 3e-7
    if np.count_nonzero(accepted) < 24:
        raise ValueError('CALIBRATION_BLOCKED_BY_RESIDUAL')
    if not np.all(accepted):
        fit = least_squares(lambda x: ((predicted(x)-measured)/5e-8)[accepted], fit.x,
                            bounds=(lower, upper), x_scale='jac', max_nfev=200)
        residual = predicted(fit.x)-measured
    # Normalize columns for identifiability; do not let units masquerade as rank.
    scaled = fit.jac / np.maximum(np.linalg.norm(fit.jac, axis=0), 1e-30)
    singular = np.linalg.svd(scaled, compute_uv=False)
    rank = int(np.sum(singular > singular[0]*1e-6))
    condition = float(singular[0]/max(singular[-1], 1e-30))
    if not fit.success or rank != 12 or condition > 1e5:
        raise ValueError('CALIBRATION_BLOCKED_BY_OBSERVABILITY: suggest '+str(SUGGESTED_EXTRA))
    sigma2 = float(np.sum(residual[accepted]**2)/max(1, int(accepted.sum())-12))
    covariance = np.linalg.pinv(fit.jac.T@fit.jac)*sigma2/(5e-8)**2
    rejected += [{'index': valid_ids[i], 'reason': 'ROBUST_RESIDUAL_OUTLIER'}
                 for i in np.flatnonzero(~accepted)]
    return dict(classification='ALTERNATIVE_VALIDATION' if any(o.get('provenance') != 'RAW_ADC' for o in observations) else 'MEASUREMENT_FIT_NOT_HARDWARE_ACCEPTANCE',
                grade='GEOMETRY_SPARSITY_CALIBRATED', pose=fit.x[:6].tolist(),
                receiver_delay_us=np.r_[0., fit.x[6:9], 0., fit.x[9:12]].tolist(),
                gauges={'RX0_delay_us': 0, 'RX4_delay_us': 0, 'basis': 'EXPLICIT_FIXED_REFERENCE_ASSUMPTION_REQUIRES_MEASURED_ALIGNMENT'},
                covariance=covariance.tolist(), rank=rank, singular_values=singular.tolist(),
                condition=condition, rms_s=float(np.sqrt(np.mean(residual[accepted]**2))),
                accepted=int(accepted.sum()), rejected=rejected, initial_guesses=starts,
                channels=[dict(channel=i, phase_offset=None, gain=None, status='UNMEASURED') for i in range(128)],
                temperature=environment.metadata(), actual_levitation_bounds=None,
                suggested_extra_tx=SUGGESTED_EXTRA, rx_coordinate_provenance='NOMINAL_MECHANICAL_NOT_MEASURED')
