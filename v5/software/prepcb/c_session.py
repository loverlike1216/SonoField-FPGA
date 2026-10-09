"""Actual compiled C service over explicit in-process HOST_FIXTURE byte transport."""
import ctypes, os, subprocess, secrets, threading
from pathlib import Path
from ..board.protocol import encode, decode, ProtocolError
from .protocol import Client
ROOT=Path(__file__).resolve().parents[2]


def build(output):
    output=Path(output).resolve();output.mkdir(parents=True,exist_ok=True)
    suffix='.dll' if os.name=='nt' else '.so'
    library=output/('prepcb_service'+suffix)
    cmd=[os.environ.get('CC','gcc'),'-std=c11','-O2','-Wall','-Wextra','-Werror','-shared',
         '-DSF_PREPCB_EXTENSION','-I',str(ROOT/'firmware/ps_service'),
         str(ROOT/'firmware/ps_service/service.c'),str(ROOT/'firmware/ps_service/prepcb_service.c'),
         str(ROOT/'tests/prepcb_fixture.c'),'-lm','-o',str(library)]
    if os.name!='nt':cmd.insert(1,'-fPIC')
    proc=subprocess.run(cmd,capture_output=True,text=True)
    (output/'compile.log').write_text(proc.stdout+proc.stderr,encoding='utf-8')
    if proc.returncode:raise RuntimeError(proc.stderr)
    return library


class Session:
    classification='HOST_FIXTURE_NOT_PHYSICAL_UART_PS_OR_TEMPERATURE'
    def __init__(self,library,temperatures=(25,26,24),flags=7):
        self.lib=ctypes.CDLL(str(library));self.sequence=0;self.trace=[];self.now=0;self.lock=threading.RLock()
        self.lib.fixture_init.argtypes=[ctypes.c_int16]*3+[ctypes.c_uint]
        self.lib.fixture_feed.argtypes=[ctypes.c_void_p,ctypes.c_uint]
        self.lib.fixture_read.argtypes=[ctypes.c_void_p,ctypes.c_uint]
        self.lib.fixture_map.argtypes=[ctypes.c_uint,ctypes.POINTER(ctypes.c_uint32)]
        self.lib.fixture_pose.argtypes=[ctypes.POINTER(ctypes.c_double)]
        self.lib.fixture_init(*[round(t*128) for t in temperatures],flags)
        nonce=secrets.token_bytes(8)
        if self.request(1,nonce)!=nonce:raise ProtocolError('C handshake failed')
        self.client=Client(self.request);self.client.negotiate()

    def request(self,command,payload=b''):
        with self.lock:return self._request(command,payload)

    def _request(self,command,payload=b''):
        self.sequence+=1;data=encode(command,self.sequence,payload)
        self.lib.fixture_feed(data,len(data))
        buffer=ctypes.create_string_buffer(4096);n=self.lib.fixture_read(buffer,4096)
        cmd,seq,body=decode(buffer.raw[:n])
        self.trace.append(dict(command=command,sequence=seq,status=body[0] if body else None,logical_ms=self.now))
        if cmd!=command|128 or seq!=self.sequence or not body or body[0]:
            raise ProtocolError('C service rejected request: '+str((cmd,seq,body.hex())))
        return body[1:]

    def tick(self,ms=20,heartbeat=True):
        with self.lock:
            if heartbeat:self.request(1,b'heartbeat')
            self.now+=ms;self.lib.fixture_tick(ms)

    def maps(self):
        result=[]
        for i in range(self.lib.fixture_cursor()):
            buffer=(ctypes.c_uint32*128)()
            if self.lib.fixture_map(i,buffer)!=128:raise RuntimeError('Missing submitted frame')
            result.append(list(buffer))
        return result

    def set_reference_pose(self,pose):
        values=(ctypes.c_double*6)(*pose)
        if self.lib.fixture_pose(values):raise ValueError('Invalid/busy geometry update')
