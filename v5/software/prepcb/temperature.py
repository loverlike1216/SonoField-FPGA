"""Three measured locations, piecewise-linear T(z), straight-ray propagation.

Dry-air approximation is deliberately explicit. RH is diagnostic until a sourced
humid-air implementation is qualified; pressure is assumed, never measured.
"""
from dataclasses import dataclass, asdict
from functools import lru_cache
import math
import numpy as np
from scipy.integrate import quad

ADDRESSES = {'center': 0x48, 'upper': 0x49, 'lower': 0x4b}

@lru_cache(maxsize=8)
def quadrature(nodes):
    return np.polynomial.legendre.leggauss(nodes)


@dataclass(frozen=True)
class Reading:
    sensor_id: str
    location: str
    timestamp: float
    reading_C: float
    uncertainty: float = .15
    status: str = 'OK'
    staleness_ms: float = 0
    calibration_offset: float = 0
    provenance: str = 'UNKNOWN'


def tmp117_decode(data):
    if len(data) != 2:
        raise ValueError('TMP117 short read')
    return int.from_bytes(data, 'big', signed=True) / 128


def sht_crc(data):
    crc = 0xff
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = ((crc << 1) ^ (0x31 if crc & 0x80 else 0)) & 255
    return crc


def sht45_decode(data):
    if len(data) != 6 or any(sht_crc(data[i:i+2]) != data[i+2] for i in (0, 3)):
        raise ValueError('SHT45 CRC/length error')
    return (-45 + 175 * int.from_bytes(data[:2], 'big') / 65535,
            max(0, min(100, -6 + 125 * int.from_bytes(data[3:5], 'big') / 65535)))


class Sensors:
    """Inject an actual I2C read callback; exceptions/short reads never become OK.

    read(segment, address, register, count) must complete with its own bounded
    hardware timeout. No implicit scan or default sensor reading is performed.
    """
    def __init__(self, read):
        self.read = read

    def poll(self, now, provenance):
        values = []
        for location, address in ADDRESSES.items():
            try:
                value = tmp117_decode(self.read(location, address, 0, 2))
                status = 'OK'
            except (OSError, ValueError, TimeoutError):
                value, status = math.nan, 'READ_FAILED'
            values.append(Reading('TMP117_'+location.upper(), location, now,
                                  value, status=status, provenance=provenance))
        return values


class Environment:
    model_version = 'dry_linear_Tz_v1'

    def __init__(self, readings, now, gap_m=.1, humidity=None):
        if len(readings) != 3 or {r.location for r in readings} != set(ADDRESSES):
            raise ValueError('Three unique TMP117 locations required')
        if len({r.sensor_id for r in readings}) != 3 or not .09 <= gap_m <= .115:
            raise ValueError('Sensor identity/gap conflict')
        for r in readings:
            age = max(r.staleness_ms, (now-r.timestamp)*1000)
            if (r.timestamp > now or r.status != 'OK' or not math.isfinite(r.reading_C+r.calibration_offset)
                    or not 0 <= age <= 2000 or not 0 < r.uncertainty <= 1
                    or not 0 <= r.reading_C+r.calibration_offset <= 50
                    or r.provenance == 'UNKNOWN'):
                raise ValueError('TEMP_UNSAFE_OR_STALE: '+r.sensor_id)
        self.readings = tuple(readings)
        by_location = {r.location: r.reading_C+r.calibration_offset for r in readings}
        self.temperatures = np.array([by_location[k] for k in ('lower', 'center', 'upper')])
        self.z = np.array([-gap_m/2, 0, gap_m/2])
        self.humidity = humidity
        if humidity is not None and (not math.isfinite(humidity) or not 0 <= humidity <= 100):
            raise ValueError('Humidity out of range')

    def speed(self, z):
        return 331.3 + .606*np.interp(z, self.z, self.temperatures)

    def travel_time(self, a, b, nodes=32):
        a, b = np.asarray(a), np.asarray(b)
        # Gauss quadrature split at T(z)'s kink, independent of ray direction.
        d = b-a
        split = [0., 1.]
        if abs(d[2]) > 1e-15:
            split += [float((z-a[2])/d[2]) for z in self.z if 0 < (z-a[2])/d[2] < 1]
            split.sort()
        x, w = quadrature(nodes)
        integral = sum((hi-lo)/2 * np.sum(w/self.speed(a[2]+d[2]*(lo+(x+1)*(hi-lo)/2)))
                       for lo, hi in zip(split, split[1:]))
        return float(np.linalg.norm(d)*integral)

    def reference_time(self, a, b):
        a, b = np.asarray(a), np.asarray(b)
        # Adaptive scipy integrator provides an independent numerical algorithm.
        return float(np.linalg.norm(b-a)*quad(
            lambda t: 1/float(self.speed(a[2]+t*(b[2]-a[2]))), 0, 1,
            points=[float((z-a[2])/(b[2]-a[2])) for z in self.z
                    if abs(b[2]-a[2])>1e-15 and 0<(z-a[2])/(b[2]-a[2])<1],
            epsabs=1e-13, epsrel=1e-11)[0])

    def travel_times(self, a, b, nodes=16):
        a,b=np.broadcast_arrays(np.asarray(a),np.asarray(b))
        delta=b-a;x,w=quadrature(nodes)
        cuts=[np.zeros(a.shape[:-1]),np.ones(a.shape[:-1])]
        for knot in self.z:
            crossing=np.zeros(a.shape[:-1])
            np.divide(knot-a[...,2],delta[...,2],out=crossing,where=abs(delta[...,2])>1e-15)
            cuts.append(np.where((crossing>0)&(crossing<1),crossing,1.))
        cuts=np.sort(np.stack(cuts),axis=0)
        integral=np.zeros(a.shape[:-1])
        for lo,hi in zip(cuts,cuts[1:]):
            t=lo[...,None]+(x+1)*(hi-lo)[...,None]/2
            z=a[...,2,None]+delta[...,2,None]*t
            integral+=(hi-lo)/2*np.sum(w/self.speed(z),axis=-1)
        return np.linalg.norm(delta,axis=-1)*integral

    def metadata(self):
        return dict(model=self.model_version, pressure_assumed=True,
                    humidity_percent=self.humidity, humidity_applied=False,
                    uncertainty='sensor accuracy plus unmeasured air/board bias',
                    temperature_confidence='THREE_LOCAL_POINTS_NOT_3D_THERMOMETRY',
                    readings=[asdict(r) for r in self.readings])


def compensate(rows, tx, target, frequency, old_speed, environment):
    """Complete new map only. Calibration bytes remain independent and unchanged."""
    if len(rows) != 128 or len(tx) != 128:
        raise ValueError('Complete 128-channel map required')
    result = []
    for row, source in zip(rows, tx):
        code = int(np.rint(-frequency*environment.travel_time(source, target)*256))
        code = (code+(128 if row['channel'] >= 64 else 0)) % 256
        result.append({**row, 'requested_phase': code,
                       'effective_phase': (code+row['calibration_phase']) % 256})
    return result


def transition(previous, wanted, max_step=2, hold_delta=32):
    if not 1 <= max_step <= hold_delta < 128 or len(previous) != 128 or len(wanted) != 128:
        raise ValueError('Invalid phase transition')
    delta = np.array([(b['requested_phase']-a['requested_phase']+128) % 256-128
                      for a, b in zip(previous, wanted)])
    if any(a['calibration_phase'] != b['calibration_phase'] for a, b in zip(previous, wanted)):
        raise ValueError('Calibration update requires safe re-arm')
    if np.max(abs(delta)) > hold_delta:
        return 'HOLD_REARM_REQUIRED', previous
    result = [{**a, 'requested_phase': int(a['requested_phase']+np.clip(d, -max_step, max_step)) % 256}
              for a, d in zip(previous, delta)]
    return 'ATOMIC_MAP_REQUIRED', result
