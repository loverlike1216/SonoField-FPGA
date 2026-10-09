"""Run with Vitis 2025.2: vitis -s ps_platform_preflight.py. No device access."""
import importlib.util,json,os,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=json.loads((root/'config/board_smoke_profile.json').read_text(encoding='utf-8'))
result={'scope':'Installed target-build capability and required platform facts; no board access',
 'vitis_python_available':importlib.util.find_spec('vitis') is not None,
 'arm_gcc_on_path':shutil.which('arm-none-eabi-gcc'),'xsa':p['ps_platform_xsa'],'bsp':p['target_bsp'],
 'uart_route':p['uart_route'],'target_compile':'NOT_RUN_MISSING_VERIFIED_PLATFORM',
 'host_c':'Verified independently by board_transport_gate.py against real GCC DLL'}
print(json.dumps(result,indent=2))
if not p['ps_platform_xsa'] or not p['target_bsp']:
 raise RuntimeError('PS_TARGET_BUILD_BLOCKED: no reviewed XSA/BSP; do not substitute a guessed board preset')
