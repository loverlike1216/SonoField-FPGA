import numpy as np
from .phase_solver import focus_phases

MODES = {0: "STANDING_WAVE", 1: "FOCUS", 2: "TRANSLATE_Z", 3: "TRANSLATE_XY",
         4: "TRAJECTORY", 5: "CALIBRATION"}


def standing_wave_phases(elements, target=(0,0,0), sound_speed=343.0, lower_offset=np.pi):
    """Opposed focused waves with a central pressure node when lower_offset=pi.

    Node existence alone does not prove a stable 3D particle trap.
    """
    phase = focus_phases(elements, target, sound_speed)
    return (phase + np.array([lower_offset if e.channel_id.startswith("LOWER") else 0
                              for e in elements])) % (2*np.pi)
