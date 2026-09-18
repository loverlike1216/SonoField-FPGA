# PREFLIGHT and baseline

- User explicitly activated SONOFIELD_FPGA / VN1 with repository, main and exact workspace.
- `gh repo view`: existing public loverlike1216/SonoField-FPGA, default main. No repository was created by Codex.
- Initially no local .git; workspace contained only user-owned Zynq7020 (12 files).
- `git init -b main`, add specified origin, fetch main, checkout origin/main; baseline c72b670 Initial commit.
- Initial README contained only the project title. No previous RTL, tests, architecture, shared state,
  synthesis, implementation, changelog or acceptance evidence existed. No tracked user edits were overwritten.
- All supplied files inspected before RTL or constraints; user resolved source precedence to constrain/.
- Baseline build/test: NOT AVAILABLE (empty source repository), not PASS.
- Windows PowerShell, Python 3.10.11; global Python lacked numpy/Pillow. Created workspace .venv and pinned dependencies.
- Icarus 12.0 development build found at C:/iverilog/bin. Vivado 2025.2 found and identified under D:/Vivado/2025.2/2025.2/Vivado/bin.
- Exact part/VCCO still absent. No guessed device was selected to manufacture a synthesis success.
- Raw pin extraction has 101 records, not 101 free FPGA outputs. Functions include peripheral pins and malformed GPIO records.

The first simulator launcher failure is retained separately; later successful logs do not replace it.
