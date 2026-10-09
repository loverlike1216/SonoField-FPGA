"""Optional extension commands keep the original SFP2 frame/CRC/version intact."""
import struct
from ..board.protocol import encode, decode, Parser, ProtocolError

COMMANDS = dict(GET_BOARD_CAPS=32, GET_TEMP=33, CAL_START=34, CAL_PROGRESS=35,
                CAL_RESULT=36, CAL_ABORT=37, TRAJECTORY_UPLOAD=38, MOTION_START=39,
                MOTION_PAUSE=40, MOTION_RESUME=41, MOTION_STOP=42, RAW_CHUNK=43)


class Client:
    def __init__(self, request):
        self.request = request
        self.capabilities = None

    def negotiate(self):
        data = self.request(COMMANDS['GET_BOARD_CAPS'], b'')
        if len(data) != 12:
            raise ProtocolError('Unsupported pre-PCB capabilities')
        caps, capacity, rate = struct.unpack('<III', data)
        if caps & 0x47 != 0x47 or rate != 50 or not 0 < capacity <= 12000:
            raise ProtocolError('Incompatible task queue')
        self.capabilities = dict(flags=caps, capacity=capacity, motion_hz=rate)
        return self.capabilities

    def upload(self, frames):
        if not self.capabilities or not 0 < len(frames) <= self.capabilities['capacity']:
            raise ProtocolError('Negotiate capacity; task must fit before start')
        for index in range(0, len(frames), 20):
            group = frames[index:index+20]
            payload = struct.pack('<II', len(frames), index)+b''.join(struct.pack('<iii',
                *[round(f[k]*1000000) for k in ('x_mm', 'y_mm', 'z_mm')]) for f in group)
            reply = self.request(COMMANDS['TRAJECTORY_UPLOAD'], payload)
            if reply != struct.pack('<I', index+len(group)):
                raise ProtocolError('Upload ACK index mismatch')

    def command(self, name):
        if not self.capabilities:
            raise ProtocolError('Capability negotiation required')
        return self.request(COMMANDS[name], b'')

    def download_raw(self,length=16384,chunk=240,retries=2):
        if not self.capabilities or not self.capabilities['flags'] & 8:
            raise ProtocolError('Raw transfer not advertised')
        if type(length) is not int or not 0<length<=16384 or not 1<=chunk<=240 or not 0<=retries<=2:
            raise ValueError('Invalid bounded raw transfer')
        result=bytearray()
        for offset in range(0,length,chunk):
            size=min(chunk,length-offset)
            for attempt in range(retries+1):
                try:
                    reply=self.request(COMMANDS['RAW_CHUNK'],struct.pack('<II',offset,size))
                    break
                except TimeoutError:
                    if attempt==retries:raise
            if len(reply)!=size+8 or reply[:8]!=struct.pack('<II',offset,size):
                raise ProtocolError('Raw chunk offset/length mismatch')
            result.extend(reply[8:])
        return bytes(result)


def discover_ports():
    """Enumerate without opening/toggling any device. Optional pyserial dependency."""
    try:
        from serial.tools import list_ports
        return [dict(device=p.device, description=p.description, vid=p.vid, pid=p.pid)
                for p in list_ports.comports()]
    except ImportError:
        return []
