import numpy as np


def focus_phases(elements, target=(0, 0, 0), sound_speed=343.0):
    if sound_speed <= 0:
        raise ValueError("Sound speed must be positive")
    distance = np.linalg.norm(np.array([e.position for e in elements])-np.asarray(target), axis=1)
    return (-2*np.pi*distance*np.array([e.frequency for e in elements])/sound_speed) % (2*np.pi)


def quantize_phase(radians, bits=8):
    if bits < 1 or bits > 12:
        raise ValueError("Phase bits must be 1..12")
    return (np.floor((np.asarray(radians) % (2*np.pi))/(2*np.pi)*(1 << bits)+0.5).astype(int)
            % (1 << bits))


def dequantize_phase(codes, bits=8):
    return np.asarray(codes)*2*np.pi/(1 << bits)
