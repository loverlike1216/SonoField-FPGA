"""Bounded I2C callback adapter: identity, readiness, ACK/length and timestamp.

No TMP117 temperature CRC exists; EEPROM is never unlocked or programmed.
Callback transaction timeouts belong to the actual bus implementation.
"""
import math,time
from .temperature import Reading,ADDRESSES,tmp117_decode

class TMP117Adapter:
 def __init__(self,read,clock=time.monotonic,addresses=None):
  self.read=read;self.clock=clock;self.addresses=dict(ADDRESSES if addresses is None else addresses)
 def word(self,location,address,register):
  value=self.read(location,address,register,2)
  if not isinstance(value,(bytes,bytearray)) or len(value)!=2:raise ValueError('SHORT_READ')
  return int.from_bytes(value,'big')
 def poll(self,provenance):
  if provenance not in ('REAL_SENSOR','HOST_FIXTURE','SYNTHETIC_REFERENCE'):raise ValueError('Explicit provenance required')
  result=[]
  for location,address in self.addresses.items():
   start=self.clock();status='OK';value=math.nan
   try:
    if self.word(location,address,15)&0x0fff!=0x0117:raise ValueError('DEVICE_ID')
    config=self.word(location,address,1)
    if config&0x1000:raise ValueError('EEPROM_BUSY_POWERUP')
    if not config&0x2000:raise ValueError('CONVERSION_NOT_READY')
    raw=self.word(location,address,0)
    if raw==0x8000:raise ValueError('POWERUP_SENTINEL')
    value=tmp117_decode(raw.to_bytes(2,'big'))
    if not 0<=value<=50:raise ValueError('OPERATING_INTERVAL')
   except (OSError,ValueError,TimeoutError) as exc:status='TEMP_'+str(exc);value=math.nan
   end=self.clock()
   if not math.isfinite(end-start) or not 0<=end-start<=.1:status='TEMP_TRANSACTION_TIME';value=math.nan
   result.append(Reading('TMP117_'+location.upper(),location,end,value,status=status,staleness_ms=(end-start)*1000,provenance=provenance))
  return result

class MultiplexedTMP117Adapter(TMP117Adapter):
 """Physical v5 profile: TCA9548A 0x70 channels0/1/2; all TMP117 at0x48.

 select(mask), read(location,address,register,count) and write(...,bytes) are
 bounded bus callbacks. Only volatile configuration01 is written, never EEPROM.
 Call configure while disarmed, wait20ms, then poll every50ms. Poll failure must
 prevent the PS freshness toggle, not reuse a previous successful temperature.
 """
 channels={'center':0,'upper':1,'lower':2}
 def __init__(self,read,write,select,clock=time.monotonic):
  super().__init__(read,clock,{k:0x48 for k in self.channels})
  self.write=write;self.select=select;self.configured_at=None
 def word(self,location,address,register):
  try:
   self.select(1<<self.channels[location])
   return super().word(location,address,register)
  finally:self.select(0)
 def configure(self):
  self.configured_at=None
  for location,address in self.addresses.items():
   if self.word(location,address,15)&0x0fff!=0x0117:raise ValueError('DEVICE_ID')
   try:
    self.select(1<<self.channels[location]);self.write(location,address,1,b'\x00\x00')
   finally:self.select(0)
   if self.word(location,address,1)&0x0ffc:raise ValueError('VOLATILE_CONFIG_READBACK')
  self.configured_at=self.clock()
 def poll(self,provenance):
  if self.configured_at is None or self.clock()-self.configured_at<.020:
   raise ValueError('FAST_CONVERSION_NOT_CONFIGURED_OR_SETTLED')
  return super().poll(provenance)
