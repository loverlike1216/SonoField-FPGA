"""Publish filtered read-only evidence; never operate the board or vendor init code.

Run from any directory with Python 3.10+. Private inputs are in local_raw/.
Original board photos and full USB/JTAG identities deliberately stay private.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys

V = Path(__file__).resolve().parents[1]
R = V.parent
E = V / 'evidence/board_bringup/20261009'
RAW = E / 'local_raw'
C = V / 'hardware/integration_candidates/20261009'
sys.path.insert(0, str(C))
from verify_candidates import xlsx


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inventory = json.loads((RAW / 'windows_inventory.json').read_text(encoding='utf-8-sig'))
    devices = []
    serials = set()
    for device in inventory['usb']:
        device_id = device['PNPDeviceID']
        if 'VID_0403&PID_6014' not in device_id:
            continue
        serials.add(device_id.rsplit('\\', 1)[-1])
        devices.append({k: device[k] for k in ('Name', 'Service', 'Manufacturer', 'Status', 'ConfigManagerErrorCode')})
        devices[-1].update(vid='0403', pid='6014', interface=re.search(r'MI_(\w+)', device_id).group(1) if 'MI_' in device_id else None,
                          com=None, serial='[REDACTED_DEVICE_SERIAL]')
    driver = inventory['drivers']
    dump(E / 'windows_public.json', dict(observed_at=inventory['observed_at'], pwsh=inventory['pwsh'], relevant_usb=devices,
        driver={k: driver[k] for k in ('DriverVersion', 'DriverProviderName', 'IsSigned')},
        com_devices=inventory.get('serial') or [], ft2232_confirmed=False,
        interpretation='FTDI USB Converter VID0403/PID6014; Vivado identifies Digilent JTAG-HS1. No UART COM present; no driver failure proven.'))
    logs = []
    for name in ('vivado_readonly.log', 'xsdb_readonly.log', 'package_review.log', 'package_review_retry.log'):
        text = (RAW / name).read_text(encoding='utf-8', errors='replace')
        text = '\n'.join(line for line in text.splitlines() if not re.search(r'EFUSE|DNA', line, re.I)) + '\n'
        for serial in serials:
            text = text.replace(serial, '[REDACTED_DEVICE_SERIAL]')
        (E / name).write_text(text, encoding='utf-8')
        logs.append(dict(file=name, raw_sha256=digest(RAW / name), public_sha256=digest(E / name),
                         redaction='Device serials and entire DNA/EFUSE property lines removed'))
    dump(E / 'log_provenance.json', dict(logs=logs, originals='PRIVATE_LOCAL_RAW'))
    photos = []
    for source, title in [
        (Path('C:/Users/LOVERL~1/AppData/Local/Temp/codex-clipboard-f1d97adb-0c09-43e7-9362-7b82d66bb4d9.jpg'), 'ax7020_front.jpg'),
        (Path('C:/Users/LOVERL~1/AppData/Local/Temp/codex-clipboard-4c3d2c2b-ec27-4ad1-8f8c-4e27103e2bf0.jpg'), 'ax7020_back.jpg')]:
        target = RAW / title
        if source.exists() and not target.exists():
            shutil.copy2(source, target)
        assert target.exists(), f'Missing actual uploaded photo: {title}'
        photos.append(dict(file=title, sha256=digest(target), size_bytes=target.stat().st_size,
                           storage='PRIVATE_LOCAL_RAW', source='USER_UPLOADED_REAL_BOARD_PHOTO'))
    dump(E / 'photo_provenance.json', dict(photos=photos, observations={
        'front': ['AX7020 product label', 'XC7Z020 and CLG400 FPGA marking', 'SD card inserted', 'SD boot jumper visible'],
        'back': ['AX701020.3.0 PCB silkscreen'],
        'not_established': ['full FPGA speed/temperature ordering code', 'DDR chip identity/capacity', 'measured VCCO', 'actual connector continuity']},
        privacy='Originals contain QR/serial labels and remain local. No unsupported inference from obstructed markings.'))
    refs = []
    urls = {
        'hello.xsa': 'https://raw.githubusercontent.com/alinxalinx/AX7020_2023.1/fcf1e4a239b0f47e8ee95dfde7c2eedc5685c327/course_s2_vitis/01_ps_hello/Vitis/design_1_wrapper.xsa',
        'ad7606c-16.pdf': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf',
        'adp7118.pdf': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf'}
    for file in sorted(RAW.glob('*.pdf')) + [RAW / 'hello.xsa']:
        refs.append(dict(file=file.name, url=urls.get(file.name, 'https://www.ti.com/lit/ds/symlink/' + file.name),
                         size_bytes=file.stat().st_size, sha256=digest(file), scope='READ_ONLY_REFERENCE_NOT_EXECUTED'))
    dump(E / 'reference_sources.json', dict(sources=refs, earlier_board_docs='v5/hardware/ax7020/sources.json',
        initial_failures='Initial ADI downloads were truncated with IncompleteRead. Complete PDFs were downloaded in a later retry; actual retained byte hashes above prevail.'))
    dump(E / 'execution_failures.json', dict(status='RECOVERED_OFFLINE_FAILURES_RETAINED', failures=[
        dict(tool='Vivado package review', error='No open design', evidence='package_review.log', recovery='Read minimal combinational stub and synth_design -rtl', result='package_review_retry.log PASS'),
        dict(tool='ADI reference download', error='IncompleteRead on initial requests', recovery='Retry complete official source; validate actual PDF and byte hash', result='reference_sources.json'),
        dict(tool='XSim candidate wrapper', error='Expected a switch but found E (drive-qualified testplusarg path)', recovery='Run same self-checking TB with local vector filename; no assertions removed', result='adc_candidate_xsim.log PASS', failure_log='SOURCE_TOOL_OUTPUT_ONLY_NO_LOG_FILE'),
        dict(tool='New integrity helper', error='Initially compared raw CRLF bytes against LF-normalized baseline hashes', recovery='Use the exact read_text UTF-8 hash scope of run_baseline.py; no source or acceptance change', result='final_integrity.json PASS', failure_log='SOURCE_TOOL_OUTPUT_ONLY_NO_LOG_FILE')]))
    # Archive fresh equivalence logs, then restore the prior tracked baseline byte-for-byte.
    for name in ('tb_burst_equivalence_xsim.log', 'tb_phase_equivalence_xsim.log'):
        old = V / 'evidence/core_timing_real_loop/timing_refactor' / name
        fresh = V / 'evidence/baseline/board_integration_20261009/equivalence' / name
        fresh.parent.mkdir(parents=True, exist_ok=True)
        if not fresh.exists():
            shutil.copy2(old, fresh)
            original = subprocess.check_output(['git', 'show', 'HEAD:' + old.relative_to(R).as_posix()], cwd=R)
            old.write_bytes(original)
    working = V / 'hardware/bom/working/2026-10-09/BOM_AX7020_NU40C10T_WORKING_2026-10-09.xlsx'
    bom = xlsx(working)[1]
    def cell(c, row):
        return bom.get(f'{c}{row}', {}).get('value') or ''
    # Only source/package combinations actually inspected are promoted here.
    checked = {
        8: ('TSSOP-16 / PW', 'https://www.ti.com/lit/ds/symlink/sn74lvc595a.pdf'),
        9: ('TSSOP-24 / PW', 'https://www.ti.com/lit/ds/symlink/sn74axc8t245.pdf'),
        14: ('TSSOP-16 / PW', 'https://www.ti.com/lit/ds/symlink/tmux1574.pdf'),
        15: ('TSSOP-14 / PW', 'https://www.ti.com/product/OPA4192/part-details/OPA4192IPWR'),
        18: ('LQFP-64 / ST-64', 'https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606c-16.pdf'),
        24: ('VQFN-10 / RPW', 'https://www.ti.com/lit/ds/symlink/tps25947.pdf'),
        25: ('VSSOP-10 / DGS', 'https://www.ti.com/lit/ds/symlink/ina226.pdf'),
        33: ('LFCSP-6 / CP-6-3', 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7118.pdf'),
        36: ('WSON-6 / DRV', 'https://www.ti.com/lit/gpn/TMP117')}
    audit = []
    for row in range(5, 77):
        status = 'PACKAGE_TEXT_SOURCE_MATCH' if row in checked else 'EXACT_VENDOR_MPN_PACKAGE_REVIEW_REQUIRED'
        if row in (19, 20): status = 'COMPOSITE_NON_PROCUREMENT'
        if 50 <= row <= 72 or row == 26: status = 'PASSIVE_GENERIC_MPN_RATING_TOLERANCE_REQUIRED'
        if 37 <= row <= 49 or row in (22, 23, 73, 74, 75, 76): status = 'CONNECTOR_EQUIPMENT_MECHANICAL_SELECTION_REQUIRED'
        if row in (5, 6): status = 'TRANSDUCER_VENDOR_DRAWING_REQUIRED'
        audit.append(dict(source_row=row, item_id=cell('A', row), description=cell('D', row), working_mpn=cell('E', row),
            bom_package=cell('G', row), source_package=checked.get(row, ('UNKNOWN', 'UNKNOWN'))[0],
            source=checked.get(row, ('UNKNOWN', 'UNKNOWN'))[1], status=status,
            native_symbol_footprint_pin1_ep='NOT_VERIFIED', release='HOLD'))
    with (C / 'package_procurement_audit.csv').open('w', newline='', encoding='utf-8-sig') as out:
        writer = csv.DictWriter(out, fieldnames=audit[0].keys())
        writer.writeheader()
        writer.writerows(audit)
    facts_path = V / 'config/board_facts.json'
    facts = json.loads(facts_path.read_text(encoding='utf-8'))
    facts.update(classification='MIXED_EVIDENCE_EACH_FIELD_SCOPED', physical_board_revision='AX701020.3.0 / PCB Revision 3.0',
        revision_evidence='USER_DECLARATION_AND_BACK_PHOTO', physical_package='CLG400_PHOTO',
        observed_family='Zynq-7000 / XC7Z020', observed_jtag_idcode='0x23727093', observed_arm_dap_idcode='0x4BA00477',
        observed_jtag_adapter='Digilent JTAG-HS1 / FTDI VID0403 PID6014', ft2232_confirmed=False,
        observed_pl_done=True, observed_cpu_state='BOTH_CORTEX_A9_RUNNING', observed_boot_mode='0x5_SD',
        observed_ddrc_ctrl='0x00000081', observed_ddrc_ctrl_reg1='0x0000003E', observed_controller_bus_width_bits=32,
        actual_ddr_capacity_bytes=None, physical_part=None, actual_speed_temperature_grade=None,
        hardware_access_authorized_this_task=True, hardware_scope='READ_ONLY_NO_INITIALIZATION_DOWNLOAD_OR_RAM_ACCESS',
        reference_revision_match='NOT_VERIFIED_V2_SCHEMATIC_VS_REV3_PHOTO',
        reference_ddr_part_conflict='Manual H5TQ4G63AFR-PBC vs hello XSA MT41J256M16 RE-125; actual topology not matched',
        sysmon_measurement_valid=False, uart_com=None, evidence='v5/evidence/board_bringup/20261009/RESULT.md')
    dump(facts_path, facts)
    dump(C / 'current_hardware_scope.json', dict(status='WORKING_CANDIDATES_NOT_ELECTRICAL_RELEASE', transmitter='NU40C10T_VENDOR_BATCH_UNQUALIFIED',
        receiver='EXACT_10MM_RX_MPN_UNKNOWN', formal_adc='AD7606BBSTZ-RL', recommended_adc='AD7606C-16BSTZ-RL_PENDING_APPROVAL',
        inherited_config='config/hardware_parts.json remains an unchanged digital fixture; not AX7020 procurement authority',
        revised_bom=working.relative_to(R).as_posix()))
    print(json.dumps(dict(status='CURATED', photos=len(photos), audit_rows=len(audit), private_identity='EXCLUDED')))


if __name__ == '__main__':
    main()
