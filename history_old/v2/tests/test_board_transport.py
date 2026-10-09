import ctypes
import json
import os
from pathlib import Path
import struct
import subprocess
import unittest
from software.board import generated as g
from software.board.protocol import encode,decode,Parser,ProtocolError
from software.board.serial_transport import SerialBoardTransport

ROOT=Path(__file__).resolve().parents[1]
BUILD=ROOT/'build/board_transport'
GCC=os.environ.get('CC','D:/DevC++/Dev-Cpp/TDM-GCC-64/bin/gcc.exe')

class ServiceLink:
    """Byte stream into actual compiled PS protocol C, with modeled MMIO only."""
    def __init__(self,lib,**kwargs):self.lib=lib;self.dtr=True;self.rts=True;self.is_open=False;self.drop=False
    def open(self):
        assert self.dtr is False and self.rts is False
        self.is_open=True
    def close(self):self.is_open=False
    def reset_input_buffer(self):
        while self.read(4096):pass
    def write(self,data):
        if not self.drop:self.lib.fixture_feed(bytes(data),len(data))
        return len(data)
    def read(self,n):
        out=ctypes.create_string_buffer(n);size=self.lib.fixture_read(out,n);return out.raw[:size]

class BoardTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BUILD.mkdir(parents=True,exist_ok=True)
        library=BUILD/('service.dll' if os.name=='nt' else 'service.so')
        command=[GCC,'-std=c99','-Wall','-Wextra','-Werror','-shared','-O2',
                 '-I',str(ROOT/'firmware/ps_service'),str(ROOT/'firmware/ps_service/service.c'),
                 str(ROOT/'tests/ps_service_harness.c'),'-o',str(library)]
        if os.name!='nt':command.insert(1,'-fPIC')
        result=subprocess.run(command,capture_output=True,text=True)
        (BUILD/'c_compile.log').write_text(result.stdout+result.stderr)
        if result.returncode:raise RuntimeError(result.stderr)
        cls.lib=ctypes.CDLL(str(library))
        cls.lib.fixture_feed.argtypes=[ctypes.c_char_p,ctypes.c_uint]
        cls.lib.fixture_read.argtypes=[ctypes.c_void_p,ctypes.c_uint]
    def setUp(self):self.lib.fixture_init();self.link=ServiceLink(self.lib)
    def exchange(self,cmd,seq,payload=b''):
        self.link.write(encode(cmd,seq,payload));return decode(self.link.read(4096))[2]
    def hello(self):self.assertEqual(self.exchange(g.CMD_PING,1,b'nonce001'),b'\0nonce001')
    def profile(self):
        return dict(status='VERIFIED',port='TEST_MODEL',baudrate=115200,uart_route_verified=True,
            exact_part='xc7z020clg400-1',ps_pl_smoke_verified=True,safe_disable_verified=True,
            evidence=['SYNTHETIC_TEST_FIXTURE_NOT_BOARD'],motion_authorized=False)
    def backend(self):return SerialBoardTransport(self.profile(),serial_factory=lambda **kw:self.link,timeout_s=.02)
    def test_real_profile_stays_blocked_without_port_open(self):
        with self.assertRaisesRegex(RuntimeError,'BLOCKED'):SerialBoardTransport().connect()
    def test_crc_known_vector_and_golden_c_interop(self):
        self.hello();self.assertEqual(self.exchange(g.CMD_GET_VERSION,2),b'\0'+struct.pack('<I',1))
        self.assertEqual(self.exchange(g.CMD_GET_STATUS,3),b'\0'+struct.pack('<I',128))
    def test_fragmented_requests_and_responses(self):
        request=encode(g.CMD_PING,1,b'abcdefgh')
        for b in request:self.link.write(bytes([b]))
        parser=Parser();frames=[]
        for b in self.link.read(4096):frames+=parser.feed(bytes([b]))
        self.assertEqual(frames,[(g.CMD_PING|128,1,b'\0abcdefgh')])
    def test_corruption_every_byte_never_writes(self):
        for index in range(24):
            self.lib.fixture_init();self.hello()
            frame=bytearray(encode(g.CMD_WRITE_REGISTER,2,struct.pack('<II',0,1)));frame[index]^=0x40
            self.link.write(frame)
            self.assertEqual(self.lib.fixture_writes(),0)
            # Corrupted length can describe an incomplete frame, detectable only
            # at the bounded frame watchdog, not before the missing bytes arrive.
            self.lib.fixture_tick(g.WATCHDOG_MS)
            self.assertEqual(self.lib.fixture_connected(),0)
    def test_bad_magic_version_length_and_crc(self):
        for index in (0,4,10,-1):
            self.lib.fixture_init();self.hello();frame=bytearray(encode(g.CMD_GET_STATUS,2));frame[index]^=0xff
            self.link.write(frame);self.lib.fixture_tick(g.WATCHDOG_MS);self.assertEqual(self.lib.fixture_connected(),0)
            with self.assertRaises(ProtocolError):decode(frame)
    def test_duplicate_sequence_is_not_reexecuted(self):
        self.hello();self.assertEqual(self.exchange(g.CMD_WRITE_REGISTER,2,struct.pack('<II',0,4)),b'\0')
        self.assertEqual(self.exchange(g.CMD_WRITE_REGISTER,2,struct.pack('<II',0,4)),bytes([g.ERR_BAD_SEQUENCE]))
        self.assertEqual(self.lib.fixture_writes(),1);self.assertFalse(self.lib.fixture_connected())
    def test_watchdog_partial_frame_and_session(self):
        self.hello();self.lib.fixture_tick(g.WATCHDOG_MS);self.assertFalse(self.lib.fixture_connected())
        self.lib.fixture_init();self.link.write(b'SFP');self.lib.fixture_tick(g.WATCHDOG_MS)
        self.assertGreaterEqual(self.lib.fixture_disabled(),2)
    def test_dangerous_writes_and_invalid_addresses_denied(self):
        for addr,value in ((0,1),(8,1),(96,1),(3,0),(256,0)):
            self.lib.fixture_init();self.hello()
            self.assertEqual(self.exchange(g.CMD_WRITE_REGISTER,2,struct.pack('<II',addr,value)),bytes([g.ERR_DENIED]))
            self.assertEqual(self.lib.fixture_writes(),0)
        self.lib.fixture_init();self.hello()
        self.assertEqual(self.exchange(g.CMD_READ_REGISTER,2,struct.pack('<I',0x100)),bytes([g.ERR_DENIED]))
    def test_unknown_and_later_map_commands_rejected(self):
        for command in (0x7e,g.CMD_BEGIN_MAP,g.CMD_MAP_CHUNK,g.CMD_COMMIT_MAP,g.CMD_GET_MAP_STATUS):
            self.lib.fixture_init();self.hello();self.assertEqual(self.exchange(command,2),bytes([g.ERR_UNSUPPORTED]))
    def test_bus_error_fails_closed(self):
        self.hello();self.lib.fixture_bus_fail(1)
        self.assertEqual(self.exchange(g.CMD_GET_STATUS,2),bytes([g.ERR_BUS_ERROR]))
        self.assertFalse(self.lib.fixture_connected())
    def test_backend_handshake_read_stop_reconnect(self):
        backend=self.backend().connect();self.assertEqual(backend.state,'SAFE_DISABLED')
        self.assertTrue(backend.remote_disable_confirmed);self.assertEqual(backend.read32(4),128)
        self.assertEqual(backend.ping(),b'SF');backend.write32(0,4)
        with self.assertRaises(PermissionError):backend.write32(0,1)
        with self.assertRaises(PermissionError):backend.send_phase_map([0]*128)
        backend.stop();self.assertFalse(self.link.is_open)
        backend.connect();self.assertTrue(backend.connected);backend.disconnect()
    def test_timeout_does_not_claim_remote_disable(self):
        backend=self.backend().connect();self.link.drop=True
        with self.assertRaises(TimeoutError):backend.ping()
        self.assertFalse(backend.connected);self.assertFalse(backend.remote_disable_confirmed)
        self.lib.fixture_tick(1000);self.assertFalse(self.lib.fixture_connected())
    def test_protocol_parser_bounds(self):
        with self.assertRaises(ProtocolError):encode(1,1,b'a'*257)
        with self.assertRaises(ProtocolError):encode(1,0)
        with self.assertRaises(ProtocolError):Parser().feed(b'noise')
    def test_valid_crc_malformed_reply_fails_closed(self):
        backend=self.backend().connect();original=self.link.read
        def malformed(n):
            data=original(n)
            if data:
                cmd,seq,_=decode(data);return encode(cmd,seq,b'\0')
            return data
        self.link.read=malformed
        with self.assertRaises(ProtocolError):backend.get_status()
        self.assertFalse(backend.connected);self.assertFalse(backend.remote_disable_confirmed)
    def test_duplicate_handshake_rejected(self):
        self.hello()
        self.assertEqual(self.exchange(g.CMD_PING,1,b'nonce001'),bytes([g.ERR_BAD_SEQUENCE]))
        self.assertFalse(self.lib.fixture_connected())

if __name__=='__main__':unittest.main()
