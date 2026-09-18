import unittest
from dataclasses import replace
import numpy as np
from software.acoustic_model.array_geometry import opposing_arrays, SHAPES
from software.acoustic_model.field_solver import pressure
from software.acoustic_model.phase_solver import focus_phases, quantize_phase
from software.acoustic_model.standing_wave import standing_wave_phases
from software.acoustic_model.phase_lut_generator import phase_map
from software.acoustic_model.particle_model import Particle, scenarios


class AcousticTests(unittest.TestCase):
    def test_all_geometries_and_ids(self):
        for n in SHAPES:
            for shape in ("planar","concave"):
                a=opposing_arrays(n,shape=shape)
                self.assertEqual(len(a),n)
                self.assertEqual(len({e.channel_id for e in a}),n)
                self.assertEqual(a[n//2].rtl_channel,64)
                np.testing.assert_allclose([np.linalg.norm(e.normal) for e in a],1)

    def test_two_source_analytic_pressure(self):
        a=opposing_arrays(2,gap=.1)
        p=pressure(a,[[0,0,0]],focus_phases(a))[0]
        self.assertAlmostEqual(abs(p),40,places=10)

    def test_central_node_and_antinode_separation(self):
        a=opposing_arrays(2,gap=.16)
        phases=standing_wave_phases(a)
        wavelength=343/40000
        p=pressure(a,[[0,0,0],[0,0,wavelength/4]],phases)
        self.assertLess(abs(p[0]),1e-10)
        self.assertGreater(abs(p[1]),20)

    def test_focus_matches_triangle_bound(self):
        a=opposing_arrays(72)
        p=abs(pressure(a,[[0,0,0]],focus_phases(a))[0])
        bound=sum(abs(pressure([e],[[0,0,0]],[0])[0]) for e in a)
        self.assertAlmostEqual(p,bound,places=8)

    def test_rear_radiation_suppressed(self):
        a=opposing_arrays(2)
        self.assertEqual(abs(pressure([a[0]],[[0,0,.2]],[0])[0]),0)

    def test_calibration_cancels_intrinsic_phase(self):
        a=opposing_arrays(8)
        corrected=[replace(e,intrinsic_phase=.7,calibration_phase=-.7) for e in a]
        np.testing.assert_allclose(pressure(a,[[0,0,0]],focus_phases(a)),
                                   pressure(corrected,[[0,0,0]],focus_phases(a)),atol=1e-10)

    def test_quantization_wrap_and_error(self):
        self.assertEqual(quantize_phase([2*np.pi])[0],0)
        phase=np.linspace(-20,20,1000)
        q=quantize_phase(phase)*2*np.pi/256
        error=np.angle(np.exp(1j*(q-phase)))
        self.assertLessEqual(np.max(abs(error)),np.pi/256+1e-12)

    def test_export_keeps_lower_ids_and_disables_absent(self):
        rows=phase_map(opposing_arrays(2))
        self.assertEqual(len(rows),128)
        self.assertEqual([r["rtl_channel"] for r in rows if r["enabled"]],[0,64])
        self.assertEqual(rows[64]["CHANNEL_ID"],"LOWER_TX_00")
        self.assertEqual(rows[64]["effective_phase"],(rows[64]["requested_phase"]+rows[64]["calibration_phase"])%256)

    def test_environment_changes_phase(self):
        a=opposing_arrays(32)
        self.assertFalse(np.allclose(focus_phases(a,sound_speed=330),focus_phases(a,sound_speed=350)))

    def test_invalid_inputs_rejected(self):
        for kw in ({"pitch":.01},{"shape":"invalid"},{"total":6},{"shape":"concave","radius":.01}):
            with self.assertRaises(ValueError): opposing_arrays(**kw)
        with self.assertRaises(ValueError): pressure(opposing_arrays(2),[[0,0,.08]],[0,0])
        with self.assertRaises(ValueError): focus_phases(opposing_arrays(2),sound_speed=0)
        with self.assertRaises(ValueError): phase_map(opposing_arrays(2),mode="TRAJECTORY")

    def test_particle_units_and_no_guarantee(self):
        p=Particle(50,10)
        self.assertAlmostEqual(p.weight_newton,.0004903325)
        self.assertAlmostEqual(p.density_kg_m3,95.4929658551)
        self.assertFalse(p.assessment()["levitation_guaranteed"])
        self.assertFalse(scenarios()[-1].assessment()["rayleigh_small_particle_assumption"])


if __name__ == "__main__": unittest.main()
