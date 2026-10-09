"""Cross-check native connectivity against geometry and the four-bit RTL contract."""
import csv,hashlib,json
from pathlib import Path
from tx_design import ROOT,OUT

def main():
    wrapper=json.loads((OUT/'log/review/single_native_netlist.json').read_text(encoding='utf-8'))
    native=json.loads(wrapper['text']);parts={v['props']['Designator']:v for v in native['components'].values() if v['props'].get('Designator')}
    errors=[];checks=0
    def pin(ref,p,net):
        nonlocal checks
        checks+=1
        got=parts.get(ref,{}).get('pinInfoMap',{}).get(str(p),{}).get('net')
        if got!=net:errors.append({'ref':ref,'pin':p,'expected':net,'found':got})
    coords=list(csv.DictReader((ROOT/'v2/hardware/mechanical/geometry_10mm/coordinates_nominal.csv').open(encoding='utf-8')))
    lines=['# Schematic channel map — v2 / schematic V1','','Native net names are uppercase. RTL identifiers remain case-sensitive. Logical mapping only; physical FPGA/connector pins and VCCO remain BLOCKED.','','| Channel | RTL index | Lane / 595 output | Driver / pins in,out | x,y,z mm | Face net |','|---|---|---|---|---|---|']
    assert len(coords)==128
    for row in coords:
        cid=row['CHANNEL_ID'];n=int(row['rtl_channel']);local=n%64;b='U' if n<64 else 'L';lane=n//4;bit=n%4
        expectedxyz=(-42+12*(local%8),-42+12*(local//8),50 if n<64 else -50)
        assert tuple(float(row[k]) for k in ('x_mm','y_mm','z_mm'))==expectedxyz
        assert cid==('UPPER' if n<64 else 'LOWER')+f'_TX_{local:02d}'
        inp=f'{b}_TX{local:02d}_IN';drv=f'{b}_TX{local:02d}_DRV';face=f'{b}_TX{local:02d}_FACE'
        driver=f'U_DRV_{b}{local//2*2:02d}';pi,po=(2,7) if local%2==0 else (4,5)
        pin(f'U_SER{lane:02d}',[15,1,2,3][bit],inp);pin(driver,pi,inp);pin(driver,po,drv)
        pin(f'R_OUT_{b}{local:02d}',1,drv);pin(f'R_OUT_{b}{local:02d}',2,face);pin(cid,2,face);pin(cid,1,f'PGND_{b}')
        group=(local//4)//8;ai=(local//4)%8
        pin(f'U_LEVEL_{b}{group}',3+ai,f'SERIAL_DATA[{lane}]');pin(f'U_LEVEL_{b}{group}',21-ai,f'{b}_SER{local//4:02d}')
        pin(f'U_SER{lane:02d}',14,f'{b}_SER{local//4:02d}')
        lines.append(f'| {cid} | {n} | {lane} / Q{"ABCD"[bit]} | {driver} / {pi},{po} | {expectedxyz} | {face} |')
    for b,base in [('U',0),('L',4)]:
        for c,muxpin in enumerate([4,7,9,12]):
            pin(f'U_BLANK_{b}',muxpin,f'{b}_RX{c}_MUX');pin(f'R_ADC_{b}{c}',1,f'{b}_RX{c}_MUX');pin(f'R_ADC_{b}{c}',2,f'ADC_IN{base+c}');pin('U_ADC',49+2*(base+c),f'ADC_IN{base+c}');pin('U_ADC',50+2*(base+c),'AGND_A')
    for b in ['U','L','A']:
        for kind in ['A','D']:
            pin(f'R_GROUND_{kind}_{b}',1,f'{kind}GND_{b}');pin(f'R_GROUND_{kind}_{b}',2,f'PGND_{b}')
        pin(f'R_SYSTEM_GND_{b}',1,f'PGND_{b}');pin(f'R_SYSTEM_GND_{b}',2,'SYSTEM_GND')
    lines+=['','## Interface case mapping','','| RTL / logical identifier | Native electrical net |','|---|---|']
    m=json.loads((OUT/'project/power_design.json').read_text(encoding='utf-8'))['rtl_to_native_net']
    lines += [f'| `{a}` | `{b}` |' for a,b in m.items()]
    lines+=['','## RX and serial order','','UPPER_RX0–3 map to ADC V1–V4 (software 0–3); LOWER_RX0–3 map to V5–V8 (4–7). Each lane shifts bit3 first and bit0 last, so QA/QB/QC/QD hold channels 4L+0/1/2/3. QH-prime is not cascaded. The audit proves named connectivity, not propagation delay, ADC settling or independent safety.','']
    (ROOT/'v2/docs/hardware/SCHEMATIC_CHANNEL_MAP.md').write_text('\n'.join(lines),encoding='utf-8')
    freeze=json.loads((ROOT/'shared/versions/v1_freeze.json').read_text());changed=[p for p,h in freeze['sha256'].items() if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
    result={'status':'PASS' if not errors and not changed else 'FAIL','tx_channels':128,'rx_channels':8,'native_pin_checks':checks,'errors':errors,'frozen_v1_files_checked':len(freeze['sha256']),'frozen_v1_changed':changed,'scope':'Independent geometry/RTL pin-order and return-link checks, not circuit simulation or hardware qualification'}
    (OUT/'log/review/channel_mapping_audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2));assert result['status']=='PASS'
if __name__=='__main__':main()
