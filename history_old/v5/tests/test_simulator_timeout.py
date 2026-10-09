import sys
import tempfile
from pathlib import Path
import unittest
from software.motion.transport import SimulationTransport


class SimulatorTimeoutTests(unittest.TestCase):
    def test_environment_timeout_preserves_output_and_is_not_rtl_cycle_timeout(self):
        with tempfile.TemporaryDirectory() as name:
            transport=SimulationTransport(name)
            with self.assertRaisesRegex(TimeoutError,'SIMULATOR_PROCESS_TIMEOUT'):
                transport._run('bounded_test',[sys.executable,'-u','-c',
                    'import time; print("observable child output",flush=True); time.sleep(2)'],timeout=.5)
            self.assertIn('observable child output',(Path(name)/'bounded_test.log').read_text())
            self.assertIsNotNone(transport.process.poll())
