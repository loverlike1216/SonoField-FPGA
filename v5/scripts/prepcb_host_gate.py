"""Real compiled C request -> temperature phase map -> inherited RTL ACK chain."""
from pathlib import Path
import os, sys, subprocess, struct, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from software.board.protocol import encode, Parser
from software.prepcb.protocol import Client
from software.motion.transport import SimulationTransport, RegisterTranscriptTransport


def compile_host(output):
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    exe = output/'prepcb_host.exe'
    cmd = [os.environ.get('CC', 'gcc'), '-std=c11', '-O2', '-Wall', '-Wextra', '-Werror',
           '-DSF_PREPCB_EXTENSION', '-I', str(ROOT/'firmware/ps_service'),
           str(ROOT/'firmware/ps_service/service.c'), str(ROOT/'firmware/ps_service/prepcb_service.c'),
           str(ROOT/'tests/prepcb_host.c'), '-lm', '-o', str(exe)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    (output/'c_compile.log').write_text(proc.stdout+proc.stderr, encoding='utf-8')
    if proc.returncode:
        raise RuntimeError('C compile failed: '+proc.stderr)
    return exe


def run_host(exe, frames, output, temperatures=(25, 26, 24), flags=7, commands=None):
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    # Request stream produced by the actual Python extension client. Returned
    # upload indexes here are request-construction acknowledgements only; the
    # actual C responses are parsed and checked independently below.
    requests = [encode(1, 1, b'PCFIXT01')]
    def request(command, payload):
        requests.append(encode(command, len(requests)+1, payload))
        if command == 32:
            return struct.pack('<III', 0x7f, 512, 50)
        if command == 38:
            return struct.pack('<I', struct.unpack_from('<I', payload, 4)[0]+(len(payload)-8)//12)
        return b''
    client = Client(request)
    client.negotiate()
    client.command('GET_TEMP')
    client.upload(frames)
    for name in commands or ['MOTION_START']:
        client.command(name)
    # Native size_t framing exists only in this HOST_FIXTURE file, not UART.
    (output/'requests.bin').write_bytes(b''.join(struct.pack('P', len(r))+r for r in requests))
    (output/'sensor_input.bin').write_bytes(struct.pack('<hhhB', *[round(t*128) for t in temperatures], flags))
    args = [exe, output/'requests.bin', output/'sensor_input.bin', output/'responses.bin', output/'maps.bin', output/'host_trace.json']
    subprocess.run(list(map(str,args)), check=True, timeout=30)
    parser = Parser()
    replies = parser.feed((output/'responses.bin').read_bytes())
    if parser.buffer or len(replies) != len(requests):
        raise RuntimeError('C response count/truncation')
    for i, (command, seq, body) in enumerate(replies):
        if seq != i+1 or command != (requests[i][5] | 0x80) or not body or body[0] != 0:
            raise RuntimeError('C rejected request: '+str((command, seq, body.hex())))
        if requests[i][5] == 38:
            expected = struct.unpack_from('<I', requests[i], 16)[0]+(len(requests[i])-24)//12
            if body[1:] != struct.pack('<I', expected):
                raise RuntimeError('Actual C upload ACK differs')
    raw = (output/'maps.bin').read_bytes()
    transcript = RegisterTranscriptTransport()
    for i in range(0, len(raw), 520):
        seq, last, *words = struct.unpack('<II128I', raw[i:i+520])
        if seq != len(transcript.frames)+1:
            raise RuntimeError('PS map sequence gap')
        transcript.frames.append(words)
        transcript.write_count += 385
    trace = json.loads((output/'host_trace.json').read_text())
    return transcript, dict(trace=trace, response_count=len(replies), mode='HOST_FIXTURE_NOT_PS_HARDWARE')


def rtl_chain(transcript, output, simulator):
    return SimulationTransport(output, simulator=simulator).execute(transcript, 40000)
