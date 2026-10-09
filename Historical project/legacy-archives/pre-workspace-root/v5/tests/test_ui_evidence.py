"""Verify evidence provenance when UI preview changes after command execution."""
import json
from pathlib import Path
import tempfile
import unittest
from software.motion.trap_solver import digest
from software.ui.app import App


class UIEvidenceTests(unittest.TestCase):
    def test_saved_path_is_executed_snapshot_not_new_preview(self):
        executed=[{'sequence_id':0,'validity':'TRAP_VALID','phase_map_reference':'measured-map-digest','trap_score':0.5}]
        with tempfile.TemporaryDirectory() as temp:
            app=App.__new__(App);app.output=Path(temp);app.results=[]
            app.preview_path=[{'validity':'NOT_EVALUATED','phase_map_reference':None}]
            app.record_execution('RUN_DEMO',{'trajectory_sha256':digest(executed)},executed)
            saved=json.loads((app.output/'trajectory_00.json').read_text())
            self.assertEqual(saved,executed)
            self.assertEqual(digest(saved),app.results[0]['trajectory_sha256'])

    def test_mismatched_path_is_rejected_before_recording_success(self):
        with tempfile.TemporaryDirectory() as temp:
            app=App.__new__(App);app.output=Path(temp);app.results=[]
            with self.assertRaisesRegex(RuntimeError,'EXECUTED_TRAJECTORY_HASH_MISMATCH'):
                app.record_execution('RUN_DEMO',{'trajectory_sha256':digest([{'validity':'TRAP_VALID'}])},
                                     [{'validity':'NOT_EVALUATED'}])
            self.assertEqual(app.results,[])
            self.assertFalse((app.output/'trajectory_00.json').exists())


if __name__=='__main__':unittest.main()
