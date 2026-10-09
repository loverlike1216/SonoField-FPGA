import json,tempfile,unittest,struct
from pathlib import Path
from software.prepcb.c_session import Session,build
from software.prepcb.acquisition import acquire
from software.prepcb.protocol import Client

class TransferTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lib=build(Path(__file__).resolve().parents[1]/'build/prepcb_transfer_tests')
    def test_actual_c_raw_framing(self):
        s=Session(self.lib,flags=15);raw=s.client.download_raw()
        self.assertEqual(raw,bytes(range(256))*64)
        self.assertEqual(sum(r['command']==43 for r in s.trace),69)
    def test_no_implicit_raw_capability(self):
        with self.assertRaises(ValueError):Session(self.lib).client.download_raw()
    def test_raw_offset_corruption_rejected(self):
        c=Client(lambda cmd,p:struct.pack('<III',0x7f,512,50) if cmd==32 else bytes(248));c.negotiate()
        with self.assertRaises(ValueError):c.download_raw()
    def test_raw_timeout_bounded_retry(self):
        calls=[]
        def request(cmd,p):
            if cmd==32:return struct.pack('<III',0x7f,512,50)
            calls.append(p)
            if len(calls)==1:raise TimeoutError()
            offset,n=struct.unpack('<II',p);return p+bytes(range(offset,offset+n))
        c=Client(request);c.negotiate();self.assertEqual(c.download_raw(16),bytes(range(16)))
        self.assertEqual(len(calls),2)
    def test_acquisition_requires_physical_references(self):
        with self.assertRaises(ValueError):acquire(None,{},None,[],'.','abc','RAW_ADC')

if __name__=='__main__':unittest.main()
