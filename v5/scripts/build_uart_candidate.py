"""Attempt the Vitis 2025.2 platform BSP flow. Never connects to hardware.

Run: vitis -s v5/scripts/build_uart_candidate.py
SF_CANDIDATE_WORKSPACE selects a fresh directory under v5/build.
The XSA is a logical candidate: DDR disabled; physical Rev3 facts unqualified.
This diagnostic does not build an application. The installed platform flow is
blocked by missing Zynq QEMU resources; build_uart_ocm_candidate.py supplies a
separate real 2025.2 SDT/BSP/application flow without that platform resource.
"""
import hashlib
import json
import os
from pathlib import Path
import traceback
import faulthandler

root = Path(__file__).resolve().parents[1]
work = Path(os.environ.get("SF_CANDIDATE_WORKSPACE", root / "build/uart_resume_candidate_01")).resolve()
if not work.is_relative_to((root / "build").resolve()) or work.exists():
    raise RuntimeError("Select a fresh build directory inside v5/build")
xsa = root / "evidence/next_stage/20261010/clean_reproduction/nextstage_platform_clean/prepcb_logical_candidate.xsa"
result = {
    "classification": "OFFLINE_LOGICAL_CANDIDATE_NOT_DEPLOYABLE",
    "xsa": xsa.relative_to(root).as_posix(),
    "xsa_sha256": hashlib.sha256(xsa.read_bytes()).hexdigest(),
    "hardware_access": False,
    "ddr_enabled": False,
    "physical_board_qualified": False,
    "bsp": "NOT_RUN", "application": "NOT_RUN",
}
work.mkdir(parents=True)
client = None
try:
    print("IMPORTING_VITIS_2025_2", flush=True)
    faulthandler.dump_traceback_later(90, exit=True)
    import vitis
    print("STARTING_OFFLINE_VITIS_SERVER", flush=True)
    # Optional port is an explicitly owned, offline Vitis server, not hw_server.
    port = os.environ.get("SF_CANDIDATE_VITIS_PORT")
    client = vitis.create_client(port=int(port) if port else None, workspace=str(work))
    faulthandler.cancel_dump_traceback_later()
    client.set_workspace(str(work))
    platform = client.create_platform_component(
        name="sonofield_ocm_candidate", hw_design=str(xsa),
        os="standalone", cpu="ps7_cortexa9_0", domain_name="standalone_a9",
        no_boot_bsp=True, generate_dtb=False,
    )
    platform.report()
    platform.build()
    result["bsp"] = "BUILD_RETURNED_REQUIRE_ARTIFACT_AUDIT"
    platform_path = client.find_platform_in_repos("sonofield_ocm_candidate")
    result["platform"] = str(platform_path)
    print("CANDIDATE_PLATFORM_BUILD_RETURNED", flush=True)
except Exception:
    result["exception"] = traceback.format_exc()
    result["bsp"] = "FAILED"
    raise
finally:
    (work / "candidate_result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if client is not None:
        vitis.dispose()
