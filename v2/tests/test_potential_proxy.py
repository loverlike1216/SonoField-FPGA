import unittest
import numpy as np
from software.acoustic_model.array_geometry import opposing_arrays
from software.acoustic_model.standing_wave import standing_wave_phases
from software.acoustic_model.visualize_field import potential_proxy


class PotentialProxyTests(unittest.TestCase):
    def test_symmetry_and_gradient_step_convergence(self):
        a=opposing_arrays(32)
        phase=standing_wave_phases(a)
        points=np.array([[.001,0,.001],[-.001,0,-.001],[0,0,0]])
        fine=potential_proxy(a,points,phase,343,h=.000025)
        coarse=potential_proxy(a,points,phase,343,h=.00005)
        self.assertAlmostEqual(fine[0],fine[1],places=7)
        np.testing.assert_allclose(coarse,fine,rtol=.002)


if __name__=="__main__":unittest.main()
