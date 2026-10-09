"""Bounded command envelope shared by GUI and the PS-side execution model."""
import json
import struct
import zlib

HEADER=struct.Struct('<4sBIIH')
COMMANDS=('CONNECT','GET_STATUS','SET_TARGET','RUN_LINE','RUN_TRAJECTORY','RUN_VERTICAL',
          'RETURN_CENTER','HOLD','STOP','LOAD_CALIBRATION','APPLY_CENTER','BALL_AT_CENTER_CONFIRMED','RUN_DEMO')
MAX_PAYLOAD=16384


def encode(sequence, command, payload=None):
    if type(sequence) is not int or not 0<=sequence<2**32: raise ValueError('Invalid sequence')
    data=json.dumps(payload or {},allow_nan=False,separators=(',',':')).encode()
    if len(data)>MAX_PAYLOAD: raise ValueError('COMMAND_TOO_LARGE')
    head=HEADER.pack(b'SONO',1,sequence,len(data),COMMANDS.index(command))
    packet=head+data
    return packet+struct.pack('<I',zlib.crc32(packet))


def decode(packet):
    if not isinstance(packet,bytes) or len(packet)<HEADER.size+4: raise ValueError('TRUNCATED_COMMAND')
    magic,version,seq,size,cmd=HEADER.unpack_from(packet)
    if magic!=b'SONO' or version!=1 or cmd>=len(COMMANDS) or size>MAX_PAYLOAD or len(packet)!=HEADER.size+size+4:
        raise ValueError('INVALID_COMMAND_HEADER')
    if zlib.crc32(packet[:-4])!=struct.unpack('<I',packet[-4:])[0]: raise ValueError('COMMAND_CRC')
    payload=json.loads(packet[HEADER.size:-4])
    if not isinstance(payload,dict): raise ValueError('Invalid command payload')
    return seq,COMMANDS[cmd],payload
