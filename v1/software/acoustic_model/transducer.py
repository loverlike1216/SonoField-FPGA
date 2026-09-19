from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Transducer:
    channel_id: str
    rtl_channel: int
    position: tuple[float, float, float]
    normal: tuple[float, float, float]
    diameter: float = 0.010  # acoustic piston approximation; actual active aperture is unmeasured
    frequency: float = 40000.0
    relative_amplitude: float = 1.0
    calibration_phase: float = 0.0  # radians, electronic correction, kept separate
    intrinsic_phase: float = 0.0    # measured acoustic lag/offset, not the correction

    def __post_init__(self):
        if self.diameter <= 0 or self.frequency <= 0 or self.relative_amplitude < 0:
            raise ValueError("Invalid transducer parameters")
        if not np.isclose(np.linalg.norm(self.normal), 1.0):
            raise ValueError("Normal must be a unit vector")
        if not (0 <= self.rtl_channel < 128):
            raise ValueError("Invalid channel")
