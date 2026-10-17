"""Production-profile bus fixtures. No physical sensor/PS execution is claimed."""
import unittest
from software.prepcb.tmp117_adapter import MultiplexedTMP117Adapter

class MuxProfile(unittest.TestCase):
 def fixture(self):
  self.now=0.;self.mask=0;self.calls=[];self.config={k:0x0220 for k in ('center','upper','lower')}
  def select(mask):
   self.assertIn(mask,(0,1,2,4));self.mask=mask;self.calls.append(('select',mask))
  def read(location,address,register,count):
   self.assertEqual(address,0x48);self.assertEqual(count,2)
   self.assertEqual(self.mask,1<<{'center':0,'upper':1,'lower':2}[location])
   value={15:0x117,1:self.config[location]|0x2000,0:25*128}[register]
   return value.to_bytes(2,'big')
  def write(location,address,register,data):
   self.assertEqual((address,register,data),(0x48,1,b'\x00\x00'))
   self.config[location]=int.from_bytes(data,'big');self.calls.append(('write',location,register))
  return MultiplexedTMP117Adapter(read,write,select,clock=lambda:self.now)
 def test_volatile_fast_mode_and_all_three_locations(self):
  a=self.fixture();a.configure();self.now=.05;r=a.poll('HOST_FIXTURE')
  self.assertEqual([x.location for x in r],['center','upper','lower'])
  self.assertTrue(all(x.status=='OK' and x.reading_C==25 for x in r));self.assertEqual(self.mask,0)
  self.assertEqual([x for x in self.calls if x[0]=='write'],[('write',k,1)for k in a.channels])
 def test_no_poll_before_conversion_settles(self):
  a=self.fixture()
  with self.assertRaises(ValueError):a.poll('HOST_FIXTURE')
  a.configure();self.now=.01
  with self.assertRaises(ValueError):a.poll('HOST_FIXTURE')
 def test_nack_deselects_mux_and_returns_invalid_readings(self):
  a=self.fixture();a.configure();self.now=.05
  def broken(*args):raise OSError('NACK')
  a.read=broken;r=a.poll('HOST_FIXTURE');self.assertTrue(all(x.status!='OK' for x in r));self.assertEqual(self.mask,0)
 def test_bad_configuration_cannot_be_adopted(self):
  a=self.fixture();a.write=lambda *args:None
  with self.assertRaises(ValueError):a.configure()
  self.assertIsNone(a.configured_at);self.assertEqual(self.mask,0)
