from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Particle:
    mass_mg: float
    diameter_mm: float
    geometry: str = "sphere"
    measured: bool = False

    def __post_init__(self):
        if self.mass_mg <= 0 or self.diameter_mm <= 0 or self.geometry != "sphere":
            raise ValueError("Positive mass/diameter and spherical geometry required")

    @property
    def density_kg_m3(self):
        return self.mass_mg*1e-6 / (math.pi/6*(self.diameter_mm*1e-3)**3)

    @property
    def weight_newton(self):
        return self.mass_mg*1e-6*9.80665

    def assessment(self, sound_speed=343.0, frequency=40000.0):
        ka = 2*math.pi*frequency/sound_speed*(self.diameter_mm*1e-3/2)
        return {"mass_mg": self.mass_mg, "diameter_mm": self.diameter_mm,
                "density_kg_m3": self.density_kg_m3, "geometry": self.geometry,
                "weight_newton": self.weight_newton, "ka": ka, "measured": self.measured,
                "classification": "SIMULATION_ESTIMATE", "levitation_guaranteed": False,
                "rayleigh_small_particle_assumption": ka < 0.3}


def scenarios(density=20.0):
    """Illustrative density, not purchased EPS measurements."""
    if density <= 0:
        raise ValueError("Density must be positive")
    return [Particle(m, (6*m*1e-6/(math.pi*density))**(1/3)*1000)
            for m in (1, 5, 10, 25, 50)]
