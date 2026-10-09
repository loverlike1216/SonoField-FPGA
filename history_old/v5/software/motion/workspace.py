"""One authoritative profile; finite, inclusive limits with no silent clipping."""
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def load_profile(path=None, *, hardware=False, engineering=False):
    base = ROOT / 'config/motion_profile.json'
    qualified = ROOT / 'config/hardware_motion_profile.json'
    profile = json.loads(Path(path or (qualified if hardware and qualified.exists() else base)).read_text())
    if hardware and profile['classification'] != 'HARDWARE_VERIFIED':
        raise ValueError('HARDWARE_PROFILE_NOT_VERIFIED')
    if profile['update_rate_hz'] not in (50, 100):
        raise ValueError('Unsupported update rate')
    if profile['update_rate_hz'] == 100 and not profile.get('rate_validation_evidence'):
        raise ValueError('100 Hz requires validation evidence')
    for key in ('workspace_mm', 'model_workspace_mm'):
        a = np.asarray(profile[key], dtype=float)
        if a.shape != (3,) or not np.all(np.isfinite(a) & (a > 0)):
            raise ValueError('Invalid workspace profile')
    if np.any(np.array(profile['workspace_mm']) > profile['model_workspace_mm']):
        raise ValueError('Workspace exceeds modeled envelope')
    for key in ('horizontal_speed_mm_s', 'vertical_speed_mm_s'):
        a = np.asarray(profile[key], dtype=float)
        if a.shape != (3,) or not np.all(np.isfinite(a)) or not 0 < a[0] <= a[1] <= a[2]:
            raise ValueError('Invalid speed profile')
    for key in ('horizontal_acceleration_mm_s2', 'vertical_acceleration_mm_s2',
                'corner_radius_mm', 'max_duration_s', 'trap_neighborhood_mm', 'trap_max_error_mm'):
        if not np.isfinite(profile[key]) or profile[key] <= 0:
            raise ValueError('Invalid positive profile limit: ' + key)
    for key in ('max_waypoints', 'max_frames', 'max_repeats', 'buffer_capacity'):
        if not isinstance(profile[key], int) or profile[key] < 2:
            raise ValueError('Invalid bounded capacity')
    if engineering:
        if hardware:
            raise ValueError('Engineering envelope is simulation-only')
        profile['workspace_mm'] = profile['model_workspace_mm'][:]
        profile['profile_id'] += '_ENGINEERING_SIMULATION'
    return profile


def point(value):
    a = np.asarray(value, dtype=float)
    if a.shape != (3,) or not np.all(np.isfinite(a)):
        raise ValueError('Position must contain three finite coordinates')
    return a


def validate_target(value, profile):
    a = point(value)
    if np.any(np.abs(a) > np.asarray(profile['workspace_mm']) + 1e-10):
        raise ValueError('TARGET_OUT_OF_WORKSPACE')
    return a


def mm_to_m(value):
    return point(value) * 0.001


def m_to_mm(value):
    return point(value) * 1000


def validate_speed(speed, profile, *, vertical=False, hold=False):
    if not np.isfinite(speed) or speed < 0 or (speed == 0 and not hold):
        raise ValueError('INVALID_SPEED')
    if speed == 0 and hold:
        return 0.0
    low, _, high = profile['vertical_speed_mm_s' if vertical else 'horizontal_speed_mm_s']
    if not low <= speed <= high:
        raise ValueError('SPEED_OUT_OF_RANGE')
    return float(speed)
