import json
from pathlib import Path
import unittest
import numpy as np
from software.acoustic_model.array_geometry import planar_profile, coordinate_rows
from software.acoustic_model.export_geometry import geometry_summary
from software.acoustic_model.phase_lut_generator import phase_map
from software.acoustic_model.field_solver import pressure
from software.acoustic_model.standing_wave import standing_wave_phases

CONFIG=Path(__file__).resolve().parents[1]/"config/acoustic_baseline.json"


class RadiatingGeometryTests(unittest.TestCase):
    def setUp(self):
        self.config=json.loads(CONFIG.read_text(encoding="utf-8"))

    def test_nominal_exact_grid_and_global_origin(self):
        a=planar_profile(self.config)
        self.assertEqual(len(a),128)
        levels=np.array([-42,-30,-18,-6,6,18,30,42])/1000
        for row in range(8):
            for col in range(8):
                n=row*8+col
                np.testing.assert_allclose(a[n].position,(levels[col],levels[row],.05),atol=1e-15)
                np.testing.assert_allclose(a[64+n].position,(levels[col],levels[row],-.05),atol=1e-15)
                self.assertEqual(a[n].normal,(0,0,-1))
                self.assertEqual(a[64+n].normal,(0,0,1))
        np.testing.assert_allclose(np.mean([e.position for e in a],axis=0),0,atol=1e-15)

    def test_gap_sweep_keeps_xy_and_reflects_z(self):
        reference=coordinate_rows(planar_profile(self.config))
        for gap in np.linspace(.09,.115,26):
            a=planar_profile(self.config,float(gap))
            for n in range(64):
                np.testing.assert_allclose(a[n].position[:2],a[64+n].position[:2],atol=1e-15)
                self.assertAlmostEqual(a[n].position[2]-a[n+64].position[2],gap)
                self.assertAlmostEqual(a[n].position[2]+a[n+64].position[2],0)
            for new,old in zip(coordinate_rows(a),reference):
                self.assertEqual((new["CHANNEL_ID"],new["rtl_channel"],new["x_mm"],new["y_mm"]),
                                 (old["CHANNEL_ID"],old["rtl_channel"],old["x_mm"],old["y_mm"]))

    def test_gap_outside_limits_rejected(self):
        for gap in (.089999,.115001,float("nan"),float("inf")):
            with self.assertRaises(ValueError):planar_profile(self.config,gap)

    def test_envelope_and_travel_are_not_pcb_dimensions(self):
        s=geometry_summary(self.config)
        np.testing.assert_allclose(s["center_span_xy_mm"],[84,84])
        np.testing.assert_allclose(s["nominal_body_envelope_xy_mm"],[94,94])
        self.assertAlmostEqual(s["nominal_neighbor_clearance_mm"],2)
        self.assertAlmostEqual(s["total_gap_travel_mm"],25)
        self.assertAlmostEqual(s["symmetric_travel_per_plane_mm"],12.5)
        self.assertIsNone(s["pcb_plane_z_mm"])
        self.assertIsNone(s["pcb_gap_mm"])

    def test_corner_channel_mapping(self):
        rows=coordinate_rows(planar_profile(self.config))
        for n,xy in {0:(-42,-42),7:(42,-42),56:(-42,42),63:(42,42)}.items():
            for base,side in ((0,"UPPER"),(64,"LOWER")):
                r=rows[base+n]
                self.assertEqual(r["CHANNEL_ID"],f"{side}_TX_{n:02d}")
                self.assertEqual(r["rtl_channel"],base+n)
                self.assertEqual((r["x_mm"],r["y_mm"]),xy)

    def test_gap_dependent_relative_phase_requires_new_map(self):
        maps=[phase_map(planar_profile(self.config,g),"FOCUS") for g in (.09,.1,.115)]
        relative=[[(r["requested_phase"]-m[0]["requested_phase"])%256 for r in m] for m in maps]
        self.assertNotEqual(relative[0],relative[1]);self.assertNotEqual(relative[1],relative[2])
        self.assertTrue(all(r["enabled"] for m in maps for r in m))

    def test_center_node_for_every_gap(self):
        for gap in self.config["gap_sweep_m"]:
            a=planar_profile(self.config,gap)
            phase=standing_wave_phases(a,sound_speed=self.config["sound_speed_m_s"])
            self.assertLess(abs(pressure(a,[[0,0,0]],phase,self.config["sound_speed_m_s"])[0]),1e-9)


if __name__=="__main__":unittest.main()
