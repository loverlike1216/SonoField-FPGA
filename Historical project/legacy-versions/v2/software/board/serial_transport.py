"""Real serial backend with explicit verification gate and no automatic motion arm.

pyserial is optional until a verified physical profile exists. Tests inject a byte
stream connected to the compiled C service, not canned PONGs.
"""
import json
import re
import secrets
import struct
import time
from pathlib import Path
from . import generated as g
from .protocol import encode,Parser,ProtocolError
from ..control import registers as r

DEFAULT_PROFILE=Path(__file__).resolve().parents[2]/'config/board_transport_profile.json'

class SerialBoardTransport:
    def __init__(self,profile=None,*,serial_factory=None,timeout_s=0.5):
        self.profile=json.loads(DEFAULT_PROFILE.read_text()) if profile is None else dict(profile)
        self.factory=serial_factory;self.timeout_s=timeout_s
        if not 0<timeout_s<g.WATCHDOG_MS/1000:raise ValueError('Timeout must be below service watchdog')
        self.port=None;self.sequence=0;self.connected=False;self.capabilities=0
        self.state='SAFE_DISABLED';self.remote_disable_confirmed=False

    def _verify(self):
        p=self.profile
        if (p.get('status')!='VERIFIED' or not all(p.get(k) is True for k in
            ('uart_route_verified','ps_pl_smoke_verified','safe_disable_verified')) or
            not re.fullmatch(r'xc7z020clg400-[123]',p.get('exact_part') or '') or
            not p.get('evidence') or not isinstance(p.get('baudrate'),int) or p['baudrate']<=0):
            raise RuntimeError('BOARD_TRANSPORT_BLOCKED: verified route/part/PS-PL/safety profile required')

    def connect(self):
        self._verify()
        if self.port is not None:raise RuntimeError('Already connected')
        if self.factory is None:
            import serial
            factory=serial.Serial
        else:factory=self.factory
        # Set control-line intent BEFORE opening. Some drivers may still glitch;
        # physical DTR/RTS routing must be included in the verified profile.
        self.port=factory(port=None,baudrate=self.profile['baudrate'],timeout=min(.05,self.timeout_s),
                          write_timeout=self.timeout_s,rtscts=False,dsrdtr=False)
        self.port.dtr=False;self.port.rts=False;self.port.port=self.profile['port']
        try:
            self.port.open();self.port.reset_input_buffer();self.sequence=0
            nonce=secrets.token_bytes(8)
            if self._request(g.CMD_PING,nonce)!=nonce:raise ProtocolError('Bad PONG')
            if self.get_version()!=g.VERSION:raise ProtocolError('Version mismatch')
            self.capabilities=struct.unpack('<I',self._request(g.CMD_GET_CAPABILITIES))[0]
            if not self.capabilities&g.CAP_BASIC:raise ProtocolError('Missing basic capability')
            self.safe_disable();self.get_status();self.connected=True
        except Exception:
            self._close();raise
        return self

    def _close(self):
        self.state='SAFE_DISABLED';self.connected=False;self.capabilities=0
        if self.port is not None:
            try:self.port.close()
            finally:self.port=None

    def _request(self,command,payload=b''):
        if self.port is None:raise RuntimeError('Disconnected')
        self.sequence+=1;parser=Parser();deadline=time.monotonic()+self.timeout_s
        try:
            frame=encode(command,self.sequence,payload)
            if self.port.write(frame)!=len(frame):raise IOError('Short serial write')
            while time.monotonic()<deadline:
                frames=parser.feed(self.port.read(272))
                if frames:
                    if len(frames)!=1 or parser.buffer:raise ProtocolError('Unexpected extra response')
                    cmd,seq,body=frames[0]
                    if cmd!=(command|0x80) or seq!=self.sequence or not body:raise ProtocolError('Mismatched response')
                    if body[0]!=g.ERR_OK:raise ProtocolError('Remote error '+str(body[0]))
                    expected={g.CMD_GET_VERSION:4,g.CMD_GET_CAPABILITIES:4,g.CMD_GET_STATUS:4,
                        g.CMD_READ_REGISTER:4,g.CMD_SAFE_DISABLE:0,g.CMD_WRITE_REGISTER:0,
                        g.CMD_BEGIN_MAP:0,g.CMD_MAP_CHUNK:0,g.CMD_COMMIT_MAP:0,g.CMD_GET_MAP_STATUS:4}
                    if command in expected and len(body)-1!=expected[command]:raise ProtocolError('Malformed response payload')
                    if command==g.CMD_PING and body[1:]!=payload:raise ProtocolError('Mismatched PONG')
                    return body[1:]
            raise TimeoutError('Transport timeout; remote watchdog required')
        except Exception:
            self.remote_disable_confirmed=False;self._close();raise

    def ping(self):return self._request(g.CMD_PING,b'SF')
    def get_version(self):return struct.unpack('<I',self._request(g.CMD_GET_VERSION))[0]
    def get_status(self):return struct.unpack('<I',self._request(g.CMD_GET_STATUS))[0]
    def safe_disable(self):
        self._request(g.CMD_SAFE_DISABLE);self.state='SAFE_DISABLED';self.remote_disable_confirmed=True
    def read_register(self,address):return struct.unpack('<I',self._request(g.CMD_READ_REGISTER,struct.pack('<I',address)))[0]
    def write_register(self,address,value):
        # Initial transport never enables a mode, capture, serializer or waveform.
        if (address,value) not in ((r.CONTROL,4),(r.MODE,0)):
            raise PermissionError('Read/status stage: only explicit safe-disable writes permitted')
        self._request(g.CMD_WRITE_REGISTER,struct.pack('<II',address,value))
    read32=read_register
    write32=write_register

    def _map_gate(self):
        if not self.connected or not self.profile.get('motion_authorized') or not self.capabilities&g.CAP_MAP:
            raise PermissionError('Map capability is disabled in the first transport stage')
    def send_phase_map(self,words):
        self._map_gate()
        if len(words)!=128 or any(type(w)is not int or not 0<=w<2**17 for w in words):raise ValueError('Complete 128-channel map required')
        self._request(g.CMD_BEGIN_MAP)
        for start in range(0,128,32):
            self._request(g.CMD_MAP_CHUNK,struct.pack('<H32I',start,*words[start:start+32]))
    def commit_map(self):self._map_gate();return self._request(g.CMD_COMMIT_MAP)
    def wait_ack(self):
        self._map_gate();deadline=time.monotonic()+self.timeout_s
        while time.monotonic()<deadline:
            status=struct.unpack('<I',self._request(g.CMD_GET_MAP_STATUS))[0]
            if status&1:return status
        self.stop();raise TimeoutError('Map ACK timeout')
    def stop(self):
        try:
            if self.port is not None:self.safe_disable()
        finally:self._close()
    disconnect=stop
