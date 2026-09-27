"""Little-endian framed requests/responses, CRC32/ISO-HDLC over header+payload."""
import struct
import zlib
from . import generated as g

HEADER=struct.Struct('<4sBBIH')

class ProtocolError(ValueError):
    pass

def encode(command, sequence, payload=b''):
    if not 0<=command<=255 or not 1<=sequence<=0xffffffff or len(payload)>g.MAX_PAYLOAD:
        raise ProtocolError('Invalid frame bounds')
    data=HEADER.pack(g.MAGIC,g.VERSION,command,sequence,len(payload))+payload
    return data+struct.pack('<I',zlib.crc32(data))

def decode(data):
    if len(data)<HEADER.size+4:raise ProtocolError('Truncated frame')
    magic,version,command,sequence,length=HEADER.unpack_from(data)
    if magic!=g.MAGIC or version!=g.VERSION or sequence==0:raise ProtocolError('Bad header')
    if length>g.MAX_PAYLOAD or len(data)!=HEADER.size+length+4:raise ProtocolError('Bad length')
    if zlib.crc32(data[:-4])!=struct.unpack_from('<I',data,len(data)-4)[0]:raise ProtocolError('Bad CRC')
    return command,sequence,data[HEADER.size:-4]

class Parser:
    """Bounded incremental parser. Errors fail closed; caller must reconnect."""
    def __init__(self):self.buffer=bytearray()
    def feed(self,data):
        frames=[]
        for byte in data:
            self.buffer.append(byte)
            if len(self.buffer)<=4 and self.buffer!=g.MAGIC[:len(self.buffer)]:
                self.buffer.clear();raise ProtocolError('Bad magic')
            if len(self.buffer)>=HEADER.size:
                _,version,_,sequence,length=HEADER.unpack_from(self.buffer)
                if version!=g.VERSION or sequence==0 or length>g.MAX_PAYLOAD:
                    self.buffer.clear();raise ProtocolError('Bad header')
                if len(self.buffer)==HEADER.size+length+4:
                    value=bytes(self.buffer);self.buffer.clear();frames.append(decode(value))
        return frames
