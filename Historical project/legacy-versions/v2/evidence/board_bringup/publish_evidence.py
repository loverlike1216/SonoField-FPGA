"""Derive a privacy-filtered evidence bundle from local tool output, offline."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / 'local_raw'


def read(name):
    return json.loads((RAW / name).read_text(encoding='utf-8-sig'))


def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def main():
    d2xx = read('d2xx.json')
    assert d2xx['create_status'] == 0
    assert all(d['status'] == 0 for d in d2xx['devices'])
    serials = [d['serial'] for d in d2xx['devices']]
    secrets = serials + [s[:-1] for s in serials]
    for name in ('vivado_identify.log', 'vivado_identify_repeat.log'):
        text = (RAW / name).read_text(encoding='utf-8-sig')
        assert 'IDENTIFICATION_DEVICE_COUNT=2' in text
        assert re.findall(r'^IDCODE_HEX\s+string\s+true\s+(\w+)', text, re.M) == ['4BA00477', '23727093']
        assert 'Exiting Vivado' in text
        for secret in sorted(set(secrets), key=len, reverse=True):
            text = re.sub(re.escape(secret), '[REDACTED_DEVICE_SERIAL]', text, flags=re.I)
        (HERE / name).write_text(text, encoding='utf-8')
    save('d2xx_public.json', dict(create_status=d2xx['create_status'], count=d2xx['count'],
        devices=[{k: v for k, v in d.items() if k not in ('serial', 'location')} for d in d2xx['devices']]))
    usb = read('usb_devices.json')
    inventory = []
    for d in usb:
        ident = d['InstanceId']
        vid = re.search(r'VID_([0-9A-F]{4})', ident, re.I)
        pid = re.search(r'PID_([0-9A-F]{4})', ident, re.I)
        interface = re.search(r'MI_([0-9A-F]{2})', ident, re.I)
        inventory.append(dict(status=d['Status'], device_class=d['Class'],
            vid=vid[1] if vid else None, pid=pid[1] if pid else None,
            interface=interface[1] if interface else None,
            name=d['FriendlyName'] if vid and vid[1]=='0403' else '[UNRELATED_DEVICE_NAME_REDACTED]'))
    save('usb_inventory_public.json', inventory)
    save('drivers_public.json', [{k:v for k,v in d.items() if k!='DeviceID'} for d in read('ftdi_drivers.json')])
    save('serial_public.json', dict(dotnet_port_names=read('serial_port_names.json'),
        win32_serialport=read('serial_ports.json'),
        explanation='Win32_SerialPort returned no rows; PnP + .NET independently enumerate COM4. Port was NOT opened.'))
    save('network_public.json', [{k:d[k] for k in ('InterfaceDescription','Status','LinkSpeed','HardwareInterface','Virtual')}
        for d in read('network_adapters.json')])
    save('board_reference_hashes.json', [dict(file=d['Path'].split('Zynq7020\\')[-1], sha256=d['Hash'])
        for d in read('board_reference_hashes.json')])
    for name in ('openfpgaloader_version.txt', 'openfpgaloader_usb.txt', 'openfpgaloader_cables.txt'):
        text = (RAW / name).read_text(encoding='utf-8-sig')
        (HERE / name).write_text('\n'.join(line.rstrip() for line in text.splitlines()).rstrip()+'\n', encoding='utf-8')
    save('raw_evidence_manifest.json', [dict(file=p.name, bytes=p.stat().st_size,
        sha256=hashlib.sha256(p.read_bytes()).hexdigest(), published_raw=False)
        for p in sorted(RAW.iterdir()) if p.is_file()])
    save('summary.json', dict(project_id='SONOFIELD_FPGA', version='v2',
        stage='BOARD_ONLY_IDENTIFICATION_AND_TRANSPORT_PREFLIGHT',
        evidence_date='2026-09-27', base_commit='1784d7bc0481c3dd8b9b4b639918d43667cb1749',
        usb_device_records=len(usb), ftdi=dict(vid='0403',pid='6010',interfaces=['MI_00/A','MI_01/B'],
        chip='FT2232H',confirmation='D2XX type=6; FTDI Programmer Guide 1.6 Appendix A', driver='2.12.28.0'),
        jtag=dict(status='IDENTIFIED',tool='Vivado 2025.2',repeated_scans=2,
        devices=[dict(name='arm_dap_0',idcode='0x4BA00477'),dict(name='xc7z020_1',idcode='0x23727093')],
        family='Zynq-7000',silicon='xc7z020',exact_part=None,package=None,speed_grade=None),
        uart=dict(port='COM4',interface='B / MI_01',opened=False,ps_wiring='NOT_VERIFIED',data_exchange='NOT_RUN'),
        ethernet=dict(pc_controller='Realtek PCIe GbE Family Controller',pc_link='Disconnected',
        board_usb_network_interface='NOT_OBSERVED',board_phy_connector='NOT_VERIFIED'),
        b01='PARTIALLY_RESOLVED_STILL_BLOCKING: silicon confirmed; package/speed/full ordering code missing',
        b03='OPEN: VCCO/connector errors/IO standards/PS UART wiring remain unverified',
        recommended_transport='Candidate: FTDI B UART for initial PS control, A JTAG for debug; no runtime link verified',
        alternative=dict(openfpgaloader='0.13.1 --scan-usb error -5; no detect/program command executed',
        openocd='NOT_FOUND in PATH or Robei installation; no install/driver change attempted'),
        programmed=False,driver_modified=False,external_pcb_touched=False,
        target_synthesis='BLOCKED_BY_BOARD_FACT',system_hardware_verified=False))


if __name__ == '__main__':
    main()
