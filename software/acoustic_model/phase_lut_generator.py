import argparse
import csv
import json
from pathlib import Path
import numpy as np
from .array_geometry import opposing_arrays, planar_profile
from .phase_solver import focus_phases, quantize_phase
from .standing_wave import standing_wave_phases


def phase_map(elements, mode="STANDING_WAVE", target=(0,0,0), sound_speed=343.0):
    if mode not in ("STANDING_WAVE", "FOCUS"):
        raise ValueError("VN1 only implements STANDING_WAVE and FOCUS map generation")
    phases = (standing_wave_phases if mode == "STANDING_WAVE" else focus_phases)(elements, target, sound_speed)
    requested = quantize_phase(phases)
    calibration = quantize_phase([e.calibration_phase for e in elements])
    present = {e.rtl_channel: (e,int(p),int(c)) for e,p,c in zip(elements,requested,calibration)}
    rows = []
    for channel in range(128):
        side, local = ("UPPER",channel) if channel < 64 else ("LOWER",channel-64)
        e,p,c = present.get(channel,(None,0,0))
        rows.append({"CHANNEL_ID": f"{side}_TX_{local:02d}", "rtl_channel": channel,
                     "requested_phase": p, "calibration_phase": c, "enabled": int(e is not None),
                     "effective_phase": (p+c)%256})
    return rows


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",default="config/acoustic_baseline.json")
    parser.add_argument("--output",default="build/phase_map.csv")
    parser.add_argument("--gap-mm",type=float,help="Face-to-face gap, constrained to the configured mechanical range")
    args=parser.parse_args()
    config=json.loads(Path(args.config).read_text(encoding="utf-8"))
    elements=planar_profile(config,None if args.gap_mm is None else args.gap_mm/1000)
    rows=phase_map(elements,config["mode"],config["target_m"],config["sound_speed_m_s"])
    output=Path(args.output); output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=rows[0].keys()); writer.writeheader(); writer.writerows(rows)
    print(f"Wrote {len(rows)} complete map entries to {output}; issue one COMMIT after all writes")


if __name__ == "__main__":
    main()
