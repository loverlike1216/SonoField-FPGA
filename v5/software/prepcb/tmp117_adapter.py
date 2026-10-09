"""Bounded I2C callback adapter: identity, readiness, ACK/length and timestamp.

No TMP117 temperature CRC exists; EEPROM is never unlocked or programmed.
Callback transaction timeouts belong to the actual bus implementation.
"""
import math,time
from .temperature import Reading,ADDRESSES,tmp117_decode

class TMP117Adapter:
 def __init__(self,read,clock=time.monotonic):self.read=read;self.clock=clock
 def word(self,location,address,register):
  value=self.read(location,address,register,2)
  if not isinstance(value,(bytes,bytearray)) or len(value)!=2:raise ValueError('SHORT_READ')
  return int.from_bytes(value,'big')
 def poll(self,provenance):
  if provenance not in ('REAL_SENSOR','HOST_FIXTURE','SYNTHETIC_REFERENCE'):raise ValueError('Explicit provenance required')
  result=[]
  for location,address in ADDRESSES.items():
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
