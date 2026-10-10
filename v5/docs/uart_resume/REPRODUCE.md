# Reproduce the v5 UART continuation candidate

Use PowerShell 7 from the current repository root. These commands perform no
serial open, board connection, programming or ps7_init execution. Keep physical
bring-up separate and gated. Choose fresh output paths; do not overwrite evidence.

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r v5/requirements-uart-lock.txt
.venv/Scripts/python.exe -m pip check
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
$env:CC='D:/DevC++/Dev-Cpp/TDM-GCC-64/bin/gcc.exe' # verify the actual host compiler
New-Item -ItemType Directory -Path v5/build/uart_manual/unit_scratch
$env:TEMP=(Resolve-Path v5/build/uart_manual/unit_scratch).Path
$env:TMP=$env:TEMP
Push-Location v5
../.venv/Scripts/python.exe -m unittest discover -s tests -v
Pop-Location
```

Expected: 203 tests, OK. Missing imports indicate the wrong working directory;
missing host compiler or temporary files outside v5/build are environment errors.
Preserve failure logs, fix the invocation and rerun; never weaken tests.

Download the official portable Arm GNU archive referenced by
`evidence/uart_resume/20261010_01/toolchain_receipt.json` into v5/build. Verify
SHA256 `51d933f00578aa28016c5e3c84f94403274ea7915539f8e56c13e2196437d18f`
before extraction. Preserve its license files. No system installer is needed.

```powershell
.venv/Scripts/python.exe v5/scripts/build_uart_ocm_candidate.py `
  --vivado-root D:/Vivado/2025.2/2025.2/Vivado `
  --arm-bin v5/build/uart_manual/arm_gnu/arm-gnu-toolchain-13.2.Rel1-mingw-w64-i686-arm-none-eabi/bin `
  --output v5/build/uart_manual/ocm
```

Expected: native interpreter version 2025.2; all eleven subprocesses exit0;
candidate_result.json status PASS; three real BSP static libraries; one linked
ELF32 ARM executable; entry within an executable LOAD segment; all LOAD ranges
inside XSA-declared OCM and DDR segment count0. Actual ELF/map/readelf/symbol/size
reports stay under the fresh output. Artifact checks are required even if a
vendor launcher exits0. Keep the observed RWX linker warning and physical HOLD.
The binary is safe/status protocol scope, not the complete deployed system.

The XSA SHA is pinned by the builder to
`e3648112eb1bea363eb6b63eb9724c0d31c5bbcce6003107e8be8f4f1777a430`.
UART1 0xE0001000, PL 0x40000000 and OCM regions are checked against generated BSP
parameters. These are candidate contracts, not permission to use those addresses
on the unknown live image. Never download or run this candidate as part of reproduction.

For independent reproduction, use a new `git clone --no-hardlinks --no-checkout`,
core.autocrlf=false, and explicit sparse checkout of v5/current governance only.
Do not materialize Historical project. Before byte auditing, run
`v5/scripts/prepare_nextstage_checkout.py` in a clean tracked tree, then
`check_nextstage_preservation.py`. This restores original expected EOL bytes from
that clone's own Git objects; it does not copy source from the original sandbox.
Create a new venv, extract the same pinned toolchain inside this clone's build,
and repeat unit tests and the complete BSP/application build. Record raw ELF
hashes separately. Application object .text hashes match in this run; complete
debug ELF/BSP bytes differ with build paths and are not declared bit-exact.

Previous complete digital/EDA reproduction remains documented in
`../next_stage/REPRODUCE.md`. This round adds no RTL change and keeps all previous
sealed hashes intact. Publication and physical operations are separate gates.
