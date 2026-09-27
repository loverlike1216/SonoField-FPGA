"""D2XX enumeration only: never open a device or change its mode/EEPROM."""
import ctypes as c
import json
from pathlib import Path

dll = c.WinDLL('ftd2xx.dll')
count = c.c_ulong()
rc = dll.FT_CreateDeviceInfoList(c.byref(count))
result = {'create_status': rc, 'count': count.value, 'devices': []}
if rc == 0:
    for index in range(count.value):
        flags, kind, ident, location = (c.c_ulong() for _ in range(4))
        serial, desc = c.create_string_buffer(16), c.create_string_buffer(64)
        handle = c.c_void_p()
        rc = dll.FT_GetDeviceInfoDetail(index, c.byref(flags), c.byref(kind), c.byref(ident),
                                      c.byref(location), serial, desc, c.byref(handle))
        result['devices'].append(dict(index=index, status=rc, flags=flags.value,
            type=kind.value, id=hex(ident.value), location=location.value,
            serial=serial.value.decode(), description=desc.value.decode(),
            handle_is_null=handle.value is None))
Path(__file__).with_name('local_raw').joinpath('d2xx.json').write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
