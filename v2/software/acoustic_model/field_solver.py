import numpy as np
from scipy.special import j1


def pressure(elements, points, requested_phases, sound_speed=343.0, attenuation_np_m=0.0):
    """Complex relative pressure in arbitrary units, exp(-j*omega*t) convention.

    Baffled circular piston far-field approximation 2*J1(ka*sin(theta))/(ka*sin(theta));
    signed sidelobes retained, rear hemisphere suppressed. No invented SPL-to-Pa calibration.
    Each emitter has amplitude 1 at 1 m on-axis absent attenuation.
    """
    if sound_speed <= 0 or attenuation_np_m < 0:
        raise ValueError("Invalid environment")
    points = np.atleast_2d(np.asarray(points, dtype=float))
    if points.shape[1] != 3 or len(requested_phases) != len(elements):
        raise ValueError("Inconsistent field dimensions")
    frequencies = {e.frequency for e in elements}
    if len(frequencies) != 1:
        raise ValueError("Coherent solver requires one frequency")
    result = np.zeros(len(points), dtype=complex)
    for e, phase in zip(elements, requested_phases):
        vector = points-np.asarray(e.position)
        distance = np.linalg.norm(vector, axis=1)
        if np.any(distance <= e.diameter/2):
            raise ValueError("Field point lies inside excluded near-source region")
        cosine = np.clip(vector @ np.asarray(e.normal)/distance, -1, 1)
        k = 2*np.pi*e.frequency/sound_speed
        argument = k*e.diameter/2*np.sqrt(1-cosine*cosine)
        directivity = np.ones_like(argument)
        np.divide(2*j1(argument), argument, out=directivity, where=np.abs(argument)>1e-12)
        directivity[cosine <= 0] = 0
        result += (e.relative_amplitude*directivity*np.exp(-attenuation_np_m*distance)/distance
                   * np.exp(1j*(k*distance+phase+e.calibration_phase+e.intrinsic_phase)))
    return result
