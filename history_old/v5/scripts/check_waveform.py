"""Independent Python oracle: analytic time/edge calculation, no RTL-derived expected trace."""
import argparse
import hashlib
import json
from pathlib import Path


def expected_map(channel, generation):
    if generation == 0:
        return 0
    if generation == 1:
        requested = (0,0,64,128,255)[channel] if channel < 5 else (channel*37+11)%256
        calibration = 0 if channel < 4 else (1 if channel == 4 else (channel*7+13)%256)
    else:
        requested, calibration = (channel*19+203)%256, (channel*7+26)%256
    return (requested+calibration)%256


def check(path, channels):
    rows=Path(path).read_text().splitlines()
    acknowledgements=[]
    for index,row in enumerate(rows,1):
        c,p,g,ack,w,e=row.split(",")
        cycle,phase,generation,ack=int(c),int(p),int(g),int(ack)
        if cycle != index or phase != (cycle*10240000//33000000)%256:
            raise AssertionError(f"Analytic timebase mismatch at {cycle}")
        expected_word=0; expected_effective=0
        for channel in range(channels):
            offset=expected_map(channel,generation)
            expected_effective |= offset << (8*channel)
            enabled=generation != 0 and (generation == 1 or channel%3 != 0)
            # Interval membership gives edge positions independently of an RTL MSB expression.
            high=((phase-offset)%256) in range(128)
            expected_word |= int(enabled and high) << channel
        if int(w,16)!=expected_word or int(e,16)!=expected_effective:
            raise AssertionError(f"TB14 waveform/map mismatch at {cycle}")
        if ack:
            if cycle%825:
                raise AssertionError("Non-boundary commit")
            acknowledgements.append(cycle)
    if len(rows)<7000 or len(acknowledgements)!=2:
        raise AssertionError("Incomplete simulation trace")
    return {"test":"TB14", "status":"PASS", "channels":channels, "cycles":len(rows),
            "channel_cycle_comparisons":len(rows)*channels,"commit_cycles":acknowledgements,
            "sha256":hashlib.sha256(Path(path).read_bytes()).hexdigest()}


if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("trace"); p.add_argument("--channels",type=int,default=128)
    a=p.parse_args(); print(json.dumps(check(a.trace,a.channels),indent=2))
