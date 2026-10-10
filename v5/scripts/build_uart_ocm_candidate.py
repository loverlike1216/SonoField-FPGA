"""Build the existing safe/status service with real 2025.2 SDT/BSP tools.

All artifacts stay in a fresh v5/build directory. No hardware connection,
programming, init execution, serial open, or download is performed.
The XSA and UART/AXI values are logical candidates, not Rev3 qualification.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess

V5 = Path(__file__).resolve().parents[1]
XSA = V5 / "evidence/next_stage/20261010/clean_reproduction/nextstage_platform_clean/prepcb_logical_candidate.xsa"
XSA_HASH = "e3648112eb1bea363eb6b63eb9724c0d31c5bbcce6003107e8be8f4f1777a430"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_elf(path):
    data = path.read_bytes()
    if data[:6] != b"\x7fELF\x01\x01":
        raise RuntimeError("Expected little-endian ELF32")
    header = struct.unpack_from("<16sHHIIIIIHHHHHH", data)
    if header[1:3] != (2, 40):
        raise RuntimeError("Expected linked ARM executable")
    regions = [(0, 0x30000), (0xFFFF0000, 0xFFFFFE00)]
    segments = []
    for n in range(header[10]):
        p = struct.unpack_from("<IIIIIIII", data, header[5] + n * header[9])
        if p[0] != 1:
            continue
        _, offset, virtual, physical, file_size, memory_size, flags, align = p
        if file_size > memory_size or offset + file_size > len(data):
            raise RuntimeError("Invalid load segment sizes")
        if virtual != physical or not any(lo <= physical and physical + memory_size <= hi for lo, hi in regions):
            raise RuntimeError("Load segment outside candidate OCM")
        segments.append(dict(address=hex(physical), file_bytes=file_size, memory_bytes=memory_size, flags=flags, alignment=align))
    if not segments or not any(int(p["address"], 16) <= header[4] < int(p["address"], 16) + p["memory_bytes"] and p["flags"] & 1 for p in segments):
        raise RuntimeError("No executable load segment contains entry")
    return dict(status="PASS", elf_type="ELF32_ARM_EXECUTABLE", entry=hex(header[4]), load_segments=segments,
                load_segments_ocm_only=True, ddr_load_segments=0, physical_ram_ownership="UNKNOWN_NOT_AUTHORIZED")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--vivado-root", type=Path, required=True)
    p.add_argument("--arm-bin", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    work = args.output.resolve()
    if work.exists() or not work.is_relative_to((V5 / "build").resolve()):
        raise ValueError("Fresh v5/build output directory required")
    if sha(XSA) != XSA_HASH:
        raise RuntimeError("Logical candidate XSA hash mismatch")
    vivado, arm = args.vivado_root.resolve(), args.arm_bin.resolve()
    empyro, sdtgen = vivado / "bin/empyro.bat", vivado / "bin/sdtgen.bat"
    repo = vivado.parent / "data/embeddedsw"
    for path in (empyro, sdtgen, repo / "cmake/toolchainfiles/cortexa9_toolchain.cmake", arm / "arm-none-eabi-gcc.exe"):
        if not path.exists():
            raise FileNotFoundError(path)
    work.mkdir(parents=True)
    env = os.environ.copy()
    env["CUSTOM_TOOLCHAIN_PATH"] = str(arm)
    env["PATH"] = str(arm) + os.pathsep + env["PATH"]
    commands = []
    result = dict(classification="OFFLINE_LOGICAL_CANDIDATE_NOT_DEPLOYABLE", hardware_access=False,
                  serial_opened=False, physical_board_qualified=False, xsa_sha256=XSA_HASH,
                  commands=commands, status="RUNNING")

    def run(name, command):
        # sdtgen passes arguments through Tcl: native backslashes become Tcl
        # escapes even when Windows process argument quoting is otherwise valid.
        command = [x.as_posix() if isinstance(x, Path) else str(x) for x in command]
        with (work / (name + ".log")).open("w", encoding="utf-8") as log:
            r = subprocess.run(command, cwd=work, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=300)
        commands.append(dict(name=name, argv=list(map(str, command)), exit_code=r.returncode))
        print(name, r.returncode, flush=True)
        if r.returncode:
            raise RuntimeError(name + " failed; logs retained")

    try:
        version_check = work / "version_check.tcl"
        version_check.write_text('puts "SF_TOOL_VERSION=[version -short]"\nexit\n', encoding="utf-8")
        run("vivado_version", [vivado / "bin/vivado.bat", "-mode", "batch", "-nolog", "-nojournal", "-source", version_check])
        if not re.search(r"SF_TOOL_VERSION=2025\.2\b", (work / "vivado_version.log").read_text()):
            raise RuntimeError("Vivado 2025.2 required")
        run("compiler", [arm / "arm-none-eabi-gcc.exe", "--version"])
        run("sdt", [sdtgen, "-xsa", XSA, "-dir", work / "sdt"])
        if not (work / "sdt/system-top.dts").is_file():
            raise RuntimeError("sdtgen returned without required device-tree artifact")
        run("repo", [empyro, "repo", "-st", repo])
        # A9 is intrinsically 32-bit; empyro's -m 32-bit option applies to A53.
        run("create_bsp", [empyro, "create_bsp", "-w", "bsp", "-s", work / "sdt/system-top.dts", "-p", "ps7_cortexa9_0", "-o", "standalone", "-t", "empty_application", "-v"])
        run("build_bsp", [empyro, "build_bsp", "-d", "bsp", "-v"])
        params = (work / "bsp/include/xparameters.h").read_text()
        for macro, value in (("XPAR_UART1_BASEADDR", 0xE0001000), ("XPAR_PL_CORE_BASEADDR", 0x40000000), ("XPAR_PS7_RAM_0_BASEADDRESS", 0), ("XPAR_PS7_RAM_0_HIGHADDRESS", 0x2FFFF), ("XPAR_PS7_RAM_1_BASEADDRESS", 0xFFFF0000), ("XPAR_PS7_RAM_1_HIGHADDRESS", 0xFFFFFDFF)):
            found = re.search(r"^#define\s+" + macro + r"\s+(0x[0-9a-fA-F]+)\s*$", params, re.M)
            if not found or int(found[1], 16) != value:
                raise RuntimeError("Candidate BSP contract mismatch: " + macro)
        run("create_app", [empyro, "create_app", "-d", "bsp", "-t", "empty_application", "-w", "app", "-v"])
        src = work / "app/src"
        originals = V5 / "firmware/ps_service"
        result["application_sources"] = {}
        for name in ("service.c", "service.h", "generated.h", "zynq_service_main.c"):
            shutil.copyfile(originals / name, src / name)
            result["application_sources"][name] = sha(originals / name)
        shutil.copyfile(originals / "sdt_2025_2/xtime_l.h", src / "xtime_l.h")
        config = src / "UserConfig.cmake"
        text = config.read_text()
        text = text.replace('set(USER_COMPILE_DEFINITIONS\n""\n)', 'set(USER_COMPILE_DEFINITIONS\n"SF_UART_DEVICE_ID=0xE0001000U"\n"SF_UART_BAUD=115200U"\n"SF_PL_BASE=0x40000000U"\n)')
        text = text.replace("set(USER_COMPILE_WARNINGS_AS_ERRORS )", "set(USER_COMPILE_WARNINGS_AS_ERRORS -Werror)")
        text = text.replace("set(USER_LINK_OTHER_FLAGS\n)", 'set(USER_LINK_OTHER_FLAGS\n"-Wl,-Map=sonofield_ocm_candidate.map"\n)')
        config.write_text(text, encoding="utf-8")
        run("build_app", [empyro, "build_app", "-w", "app", "-v"])
        elfs = list((work / "app").rglob("empty_application.elf"))
        if len(elfs) != 1:
            raise RuntimeError("Expected one linked application ELF")
        elf = elfs[0]
        result.update(elf_sha256=sha(elf), elf_bytes=elf.stat().st_size, elf_audit=audit_elf(elf),
                      bsp_libraries={name: sha(work / "bsp/lib" / name) for name in ("libxil.a", "libxilstandalone.a", "libxiltimer.a")})
        run("elf_readelf", [arm / "arm-none-eabi-readelf.exe", "-h", "-l", "-A", elf])
        run("elf_size", [arm / "arm-none-eabi-size.exe", "-A", elf])
        run("elf_symbols", [arm / "arm-none-eabi-nm.exe", "-n", elf])
        result.update(status="PASS", application_scope="SAFE_STATUS_PROTOCOL_ONLY_NO_MOTION_OR_SENSOR_RUNTIME", deployed=False)
        # Preserve the vendor linker warning; OCM placement is not W^X hardening.
        result["rwx_load_segment"] = any(s["flags"] & 7 == 7 for s in result["elf_audit"]["load_segments"])
    except Exception as exc:
        result.update(status="FAIL", error=str(exc))
        raise
    finally:
        (work / "candidate_result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
