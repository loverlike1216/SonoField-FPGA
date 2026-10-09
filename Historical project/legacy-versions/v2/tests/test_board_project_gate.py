"""Exercise the actual Tcl pre-project gate offline; never connect hardware.

Part names below are synthetic validation inputs, not board ordering-code claims.
Vivado commands are isolated at the project-creation boundary.
"""
from pathlib import Path
import tempfile
import tkinter
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/create_project.tcl'


class BoardProjectGateTests(unittest.TestCase):
    def invoke(self, part, resolved=None, source='fixture', version='2025.2'):
        interp = tkinter.Tcl()
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / 'board.tcl'
            config.write_text('set PART {' + part + '}\nset PART_SOURCE {' + source +
                              '}\nset CORE_CLOCK_HZ 132000000\nset CLOCK_SOURCE {fixture}\n')
            interp.setvar('argv', (str(config),))
            interp.setvar('test_version', version)
            interp.setvar('test_resolved', part if resolved is None else resolved)
            interp.eval('proc version {args} {return $::test_version}')
            interp.eval('proc get_parts {args} {return $::test_resolved}')
            interp.eval('proc create_project {args} {error REACHED_PROJECT_BOUNDARY}')
            with self.assertRaises(tkinter.TclError) as caught:
                interp.call('source', str(SCRIPT))
            return str(caught.exception)

    def test_family_only_rejected(self):
        self.assertIn('full documented', self.invoke('xc7z020'))

    def test_wrong_silicon_rejected(self):
        self.assertIn('full documented', self.invoke('xc7z010clg400-1'))

    def test_wildcard_rejected_even_single_resolution(self):
        self.assertIn('full documented', self.invoke('xc7z020clg400-*', 'xc7z020clg400-1'))

    def test_missing_provenance_rejected(self):
        self.assertIn('missing PART_SOURCE', self.invoke('xc7z020clg400-1', source=''))

    def test_unknown_or_mismatched_part_rejected(self):
        for resolved in ('', 'xc7z020clg484-1', 'xc7z020clg400-1 xc7z020clg400-2'):
            with self.subTest(resolved=resolved):
                self.assertIn('non-exact', self.invoke('xc7z020clg400-1', resolved))

    def test_wrong_tool_rejected(self):
        self.assertIn('2025.2', self.invoke('xc7z020clg400-1', version='2024.2'))

    def test_complete_fixture_reaches_boundary_only(self):
        self.assertEqual('REACHED_PROJECT_BOUNDARY', self.invoke('xc7z020clg400-1'))


if __name__ == '__main__':
    unittest.main()
