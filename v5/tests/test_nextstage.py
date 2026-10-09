"""Additive C-16/sensor/ownership qualification; fixtures are never real devices."""
import hashlib,unittest
from software.prepcb.adc7606c16 import Profile,Snapshot
from software.prepcb.tmp117_adapter import TMP117Adapter
from software.prepcb.temperature import Environment,ADDRESSES
from software.prepcb.sparse import scan_plan

def fixture(overrides=None,exception=None,clock=None):
 calls=[];overrides=overrides or {}
 def read(segment,address,register,count):
  calls.append((segment,address,register,count))
  if exception:raise exception
  return overrides.get(register,{15:0x117,1:0x2220,0:25*128}[register]).to_bytes(2,'big')
 return TMP117Adapter(read,clock or (lambda:0)),calls

class NextStage(unittest.TestCase):
 def test_c16_full_high_bandwidth(self):self.assertEqual(Profile().registers()[7],255)
 def test_c16_per_channel_switch(self):
  for channel in range(8):self.assertEqual(Profile(1<<channel).registers()[7],1<<channel)
 def test_c16_low_bw_allowed_reference(self):self.assertEqual(Profile(0).registers()[7],0)
 def test_c16_four_dout_and_reserved(self):self.assertEqual(Profile().registers()[2],0x10)
 def test_c16_oversampling_crc_off(self):self.assertEqual([Profile().registers()[a] for a in (8,33)],[0,0])
 def test_c16_id_rejects_b(self):
  with self.assertRaises(ValueError):Profile().verify(Profile().registers(),0x13)
 def test_c16_missing_readback(self):
  with self.assertRaises(ValueError):Profile().verify({},0x23)
 def test_c16_corrupt_bw(self):
  d=Profile().registers();d[7]=254
  with self.assertRaises(ValueError):Profile().verify(d,0x23)
 def test_c16_profile_validation(self):
  for v in (-1,256,1.5,True):
   with self.assertRaises(ValueError):Profile(v).registers()
 def test_c16_initial_rate_not_upgraded(self):
  with self.assertRaises(ValueError):Profile(sample_rate=1000000).registers()
 def test_c16_timing_budget(self):self.assertGreater(Profile().timing_budget()['read_before_next_busy_margin_ns'],0)
 def test_tmp_three_addresses(self):
  a,calls=fixture();r=a.poll('HOST_FIXTURE');self.assertTrue(all(x.status=='OK' and x.reading_C==25 for x in r));self.assertEqual({x[1] for x in calls},{0x48,0x49,0x4b})
 def test_tmp_id_error(self):a,_=fixture({15:0x118});self.assertTrue(all(x.status!='OK' for x in a.poll('HOST_FIXTURE')))
 def test_tmp_not_ready(self):a,_=fixture({1:0x220});self.assertTrue(all(x.status!='OK' for x in a.poll('HOST_FIXTURE')))
 def test_tmp_eeprom_busy(self):a,_=fixture({1:0x3220});self.assertTrue(all(x.status!='OK' for x in a.poll('HOST_FIXTURE')))
 def test_tmp_powerup(self):a,_=fixture({0:0x8000});self.assertTrue(all(x.status!='OK' for x in a.poll('HOST_FIXTURE')))
 def test_tmp_nack(self):a,_=fixture(exception=OSError('NACK'));self.assertTrue(all(x.status!='OK' for x in a.poll('HOST_FIXTURE')))
 def test_tmp_bus_timeout(self):a,_=fixture(exception=TimeoutError());self.assertTrue(all(x.status!='OK' for x in a.poll('HOST_FIXTURE')))
 def test_tmp_unknown_provenance(self):
  a,_=fixture()
  with self.assertRaises(ValueError):a.poll('UNKNOWN')
 def test_tmp_bad_value(self):a,_=fixture({0:60*128});self.assertTrue(all(x.status!='OK' for x in a.poll('HOST_FIXTURE')))
 def test_tmp_environment_uses_three(self):
  a,_=fixture();e=Environment(a.poll('HOST_FIXTURE'),0);self.assertAlmostEqual(float(e.speed(0)),346.45)
 def test_tmp_failed_environment(self):
  a,_=fixture(exception=OSError('NACK'))
  with self.assertRaises(ValueError):Environment(a.poll('HOST_FIXTURE'),0)
 def test_sparse_user_coordinates(self):
  selected={t%64 for t,_ in scan_plan()}
  for row,col in ((1,1),(2,2),(3,3),(4,4),(8,1),(7,2)):self.assertIn((row-1)*8+col-1,selected)
 def test_snapshot_bounded_read_and_ack(self):
  b=Snapshot();data=bytes(range(256))*64;b.publish(1,data);self.assertEqual(b.read(1,16000,384),data[16000:]);b.acknowledge(1,hashlib.sha256(data).hexdigest());self.assertIsNone(b.data)
 def test_snapshot_no_overwrite(self):
  b=Snapshot();b.publish(1,bytes(16384))
  with self.assertRaises(ValueError):b.publish(2,bytes(16384))
 def test_snapshot_stale_ack(self):
  b=Snapshot();b.publish(1,bytes(16384))
  with self.assertRaises(ValueError):b.acknowledge(2,hashlib.sha256(bytes(16384)).hexdigest())
 def test_snapshot_bad_digest(self):
  b=Snapshot();b.publish(1,bytes(16384))
  with self.assertRaises(ValueError):b.acknowledge(1,'0'*64)
 def test_snapshot_bad_range(self):
  b=Snapshot();b.publish(1,bytes(16384))
  for offset,count in ((-1,1),(16380,10),(0,513),(0,0)):
   with self.assertRaises(ValueError):b.read(1,offset,count)

if __name__=='__main__':unittest.main()
