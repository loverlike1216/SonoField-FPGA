"""Schematic-only TX draft, derived from the v2 four-bit serializer contract.

Library templates for passives/transducers are not procurement selections.
The manifest describes intended connectivity; native export is the independent check.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'PCB/V1'


def build():
    sheets, channels = [], []
    for bank_index, bank in enumerate(('UPPER', 'LOWER')):
        for group in range(16):
            parts = []
            prefix = f'{bank}_{group:02d}'
            short = bank[0]
            ground, power = f'PGND_{short}', f'VDRV_{short}'

            def part(key, ref, value, x, y, nets, generic=False, dnp=False):
                parts.append(dict(key=key, ref=ref, value=value, x=x, y=y,
                                  nets={str(k): v for k, v in nets.items()},
                                  generic=generic, dnp=dnp))

            def passive(key, ref, value, x, y, a, b, dnp=False):
                part(key, ref, value, x, y, {1: a, 2: b}, True, dnp)

            for pair in range(2):
                first = 4 * group + 2 * pair
                suffix = f'{short}{first:02d}'
                y = 640 - 260 * pair
                logic = [f'{short}_TX{first+i:02d}_IN' for i in range(2)]
                output = [f'{short}_TX{first+i:02d}_DRV' for i in range(2)]
                part('TC4427AEOA', f'U_DRV_{suffix}', 'TC4427AEOA713', 240, y,
                     {1: None, 2: logic[0], 3: ground, 4: logic[1],
                      5: output[1], 6: power, 7: output[0], 8: None})
                passive('C', f'C_HF_{suffix}', '100nF 50V X7R', 470, y+65, power, ground)
                passive('C', f'C_LOCAL_{suffix}', '1uF 25V X7R', 770, y+65, power, ground)
                for i in range(2):
                    local = first+i
                    cid = f'{bank}_TX_{local:02d}'
                    row = y-70*i
                    tag = f'{short}{local:02d}'
                    face = f'{short}_TX{local:02d}_FACE'
                    passive('R', f'R_PD_{tag}', '100k', 180, row-75, logic[i], ground)
                    passive('R', f'R_OUT_{tag}', '0R / TUNE', 470, row, output[i], face)
                    part('TX', cid, 'TCT40-10T / MPN_TBD', 920, row,
                         {1: ground, 2: face}, True)
                    passive('R', f'R_DAMP_{tag}', '1.2k DNP', 750, row-35, face, ground, True)
                    part('TP', f'TP_IN_{tag}', 'LOGIC', 300, row-115, {1: logic[i]}, True)
                    part('TP', f'TP_OUT_{tag}', 'DRIVER', 520, row-35, {1: output[i]}, True)
                    part('TP', f'TP_TX_{tag}', 'TRANSDUCER', 1040, row-35, {1: face}, True)
                    channels.append(dict(channel_id=cid, rtl_channel=64*bank_index+local,
                                         serial_lane=16*bank_index+group, output=('QA','QB','QC','QD')[local%4],
                                         x_mm=-42+12*(local%8), y_mm=-42+12*(local//8),
                                         z_mm=50 if bank_index==0 else -50,
                                         coordinate_reference='RADIATING_SURFACE_CENTER',
                                         polarity='UNMEASURED', logic_net=logic[i], drive_net=output[i],
                                         face_net=face, sheet=f'TX_{prefix}'))
            if group % 2 == 0:
                passive('C', f'C_BULK_{prefix}', '22uF 25V X7R', 230, 120, power, ground)
            sheets.append(dict(name=f'TX_{prefix}', parts=parts, notes=[
                f'{bank} TX {4*group:02d}-{4*group+3:02d} | 12 V initial electrical qualification',
                'DRAFT: batch qualification, power safety and upstream timing gates OPEN.',
                'R/C/TX symbols are templates; MPN/footprint TBD. TX polarity must be measured.',
                'DAMP is DNP. No snubber values selected without load measurements.',
                'Return TX current via PGND; never through RX analog return.']))
    return {'status': 'DRAFT_NOT_FOR_FABRICATION', 'sheets': sheets, 'channels': channels}


if __name__ == '__main__':
    design = build()
    assert len(design['channels']) == 128
    assert len({p['ref'] for s in design['sheets'] for p in s['parts']}) == sum(len(s['parts']) for s in design['sheets'])
    (OUT/'project/tx_design.json').write_text(json.dumps(design, indent=2)+'\n', encoding='utf-8')
    print(f"Generated {len(design['sheets'])} TX sheets; 128 mapped TX; 64 dual drivers")
