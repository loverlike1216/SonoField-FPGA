"""C-16 register/profile reference, independent of legacy B tests."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Profile:
 bandwidth_mask:int=255
 sample_rate:int=800000
 range_code:int=1
 def registers(self):
  if type(self.bandwidth_mask) is not int or not 0<=self.bandwidth_mask<=255:raise ValueError('BANDWIDTH mask')
  if self.sample_rate!=800000 or self.range_code!=1:raise ValueError('Initial qualified digital profile only')
  return {2:0x10,3:0x11,4:0x11,5:0x11,6:0x11,7:self.bandwidth_mask,8:0,0x21:0}
 def verify(self,values,device_id):
  if device_id>>4!=2:raise ValueError('Not AD7606C-16')
  if any(values.get(k)!=v for k,v in self.registers().items()):raise ValueError('Readback mismatch; acquisition disabled')
  return True
 def timing_budget(self,clock=132000000):
  # Reading starts after max650ns BUSY plus <=4core cycles synchronization/control.
  read_ns=(32*4+3)*1e9/clock
  next_busy_min_ns=1e9/self.sample_rate+500
  margin_ns=next_busy_min_ns-(650+4e9/clock+read_ns)-25
  return dict(sclk_hz=clock/4,read_ns=read_ns,read_before_next_busy_margin_ns=margin_ns,board_timing='HOLD_MISSING_MIN_MAX_IO_PVT')

class Snapshot:
 """16KiB ownership reference. Reads do not ACK, release needs matching sequence/hash."""
 def __init__(self):self.data=None;self.sequence=None
 def publish(self,sequence,data):
  if self.data is not None or type(sequence) is not int or sequence<0 or len(data)!=16384:raise ValueError('Snapshot ownership/length')
  self.data=bytes(data);self.sequence=sequence
 def read(self,sequence,offset,count):
  if sequence!=self.sequence or self.data is None or not 0<=offset<len(self.data) or not 1<=count<=512 or offset+count>len(self.data):raise ValueError('Bounded snapshot read')
  return self.data[offset:offset+count]
 def acknowledge(self,sequence,sha256):
  import hashlib
  if self.data is None or sequence!=self.sequence or hashlib.sha256(self.data).hexdigest()!=sha256:raise ValueError('Snapshot ACK mismatch')
  self.data=None;self.sequence=None
