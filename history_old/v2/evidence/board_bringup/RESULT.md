# CODEX_RESULT — v2 board-only identification

PROJECT_ID: SONOFIELD_FPGA; project_name: SonoField-FPGA.
Repository: https://github.com/loverlike1216/SonoField-FPGA.git; branch main.
Workspace: E:\Codex_project\AMD-SonoField-FPGA; active version v2.
Stage: BOARD_ONLY_IDENTIFICATION_AND_TRANSPORT_PREFLIGHT.
Starting commit: 1784d7bc0481c3dd8b9b4b639918d43667cb1749.
Ending source/evidence commit: the Git commit containing this report; final remote checkpoint is reported in delivery.

## Observed results

| Item | Actual evidence and boundary |
|---|---|
| Windows USB | 24 present USB/FTDIBUS records. Relevant composite device VID 0403 / PID 6010, A=MI_00, B=MI_01, all Status OK. Raw instance/parent/serial/location/driver properties retained locally. |
| FT2232 | Confirmed as FT2232H by D2XX device type 6, status 0 for both interfaces. Descriptors JTAG+Serial A/B. Signed FTDI driver 2.12.28.0; D2XX DLL 3.02.14. |
| JTAG | Vivado 2025.2 directly opens the observed A target. Two complete scans agree: arm_dap_0 + xc7z020_1. |
| IDCODE | ARM DAP 0x4BA00477, FPGA 0x23727093. Vivado PART=xc7z020; Zynq-7000/Z-7020 silicon confirmed. |
| Full ordering code | UNKNOWN. JTAG PART is silicon identity, not package/speed/temperature ordering code. No guessed clg400-1 or other target is selected. |
| Descriptor conflict | Vivado cable descriptor says MiniZed V1; this is adapter metadata, not evidence that the user's Robei board is a MiniZed. Actual silicon remains xc7z020. |
| UART | COM4 exists on B/MI_01 (PnP parent linkage and .NET agree). Win32_SerialPort returns no rows. Port NOT opened, no baud selected, no DTR/RTS/data writes; PS wiring/console/protocol unverified. |
| Ethernet | PC Realtek PCIe GbE is Disconnected/0 bps. No board USB-network device observed. Existing annotated board image shows USB2.0/USB3320, not a proven Ethernet PHY/RJ45 path. Do not equate PC NIC presence with Zynq Ethernet availability. |
| USB PS data | FTDI bridge is visible; native PS USB gadget/network firmware is not identified or tested. |
| Alternative | Robei bundles openFPGALoader 0.13.1 and lists ft2232 cable support. --scan-usb fails to open 0403:6010 with error -5. No FPGA detect/program command run. OpenOCD not found in PATH or Robei; not an exhaustive disk-wide absence claim. |

FTDI type interpretation: [FTDI D2XX Programmer Guide v1.6, Appendix A](https://ftdichip.com/wp-content/uploads/2025/06/D2XX_Programmers_Guide.pdf).
OpenOCD is a possible future FTDI route only with a verified adapter configuration and driver access;
its [official adapter documentation](https://openocd.org/doc/html/Debug-Adapter-Configuration.html)
requires adapter-specific setup. Since Vivado already connects, installing it or changing FTDI drivers is unnecessary.
openFPGALoader's error alone does not establish the underlying cause or board failure.

## B01 / B03 and code changes

- B01 **PARTIALLY RESOLVED, STILL BLOCKING**: previously unverified silicon is now xc7z020.
  Full ordering code/package/speed and physical clock remain unverified. hardware.const still
  documents N18/33 MHz; JTAG TCK 15 MHz is the adapter scan setting, NOT the PL clock.
- B03 **OPEN**: bank VCCO/IO standards, complete connector mapping, duplicate J4 Pin6
  (D18/E18), missing V16/J6 pin number and PS UART routing are not resolved by JTAG.
- v2/config/board_identity.json records observed identity and transport evidence separately from the historical board_facts.json baseline; exact_part
  stays null, pins_verified stays false. The 132 MHz simulated core clock is not promoted to measured hardware.
- v2/scripts/create_project.tcl now rejects family-only names, wildcard parts, different
  silicon and non-exact resolution before creating any project. Seven offline tests and four Vivado 2025.2 negative-gate cases pass.
  Synthetic complete part in those tests is a fixture, not an asserted board part.
- No RTL/clock/pin changes, board project, synthesis, implementation, bitstream or firmware download.
  Existing BoardTransport continues to refuse hardware execution until integration prerequisites exist.

## Recommended next work (not executed)

Use **FTDI A + Vivado JTAG** for development/debug; prefer **FTDI B / COM4 UART** as the
first low-rate PC↔PS control candidate after confirming board UART wiring and firmware.
Do not select Ethernet as the baseline without evidence of the board PHY/connector and PS pin configuration.
Do not assume UART can sustain the full acquisition stream: calculate payload/rate budgets first.

1. Obtain legible physical chip marking or revision-matched manufacturer documents for complete part,
   PS DDR/MIO/clock/reset, UART wiring, VCCO and connector corrections. No switch changes needed for this report.
2. Define BoardTransport packet framing, version/capability handshake, sequence/CRC, timeout,
   atomic-map acknowledgement and safe STOP/reconnect semantics. Keep simulation transport distinct.
3. Implement PS UART service + reviewed PS↔PL register-bus/AXI adapter; verify clock/reset/CDC,
   register readback, full-map commit and buffering offline first. Port enumeration alone is not transport validation.
4. With verified part/pins/clock and a separately authorized hardware phase, build PS/PL integration,
   inspect synthesis/timing and prepare an output-disabled board smoke test. No such test/download ran here.

## Evidence, validation and reproduction

Raw local-only: local_raw/{usb_devices,ftdi_properties,ftdi_drivers,serial_port_names,
network_adapters,network_addresses,d2xx}.json and both Vivado logs. Raw manifest hashes retained.
Public repository: filtered JSON and Vivado logs with USB serial replaced; no host IP/MAC/unique USB instance IDs.
Scripts: collect_windows.ps1 (pwsh 7), list_ftdi.py (D2XX enumeration only),
discover_vivado.tcl (targets only), identify_vivado.tcl (exact observed target argument required),
publish_evidence.py (offline extraction/assertions/redaction).

From this folder, run collect_windows.ps1 and Python list_ftdi.py. Run Vivado 2025.2 batch
with -source discover_vivado.tcl; pass the exact observed target URL to identify_vivado.tcl
using -tclargs. Do not paste another machine's USB serial. Keep raw logs local.
From v2, run Python -m unittest tests.test_board_project_gate -v for offline guard regression.
Validation/working-tree evidence: validation.json, project_gate_tests.txt, vivado_gate_tests.log and repository_audit.json. Frozen v1: 212/212 hashes unchanged. First audit failure and correction are preserved in audit_first_attempt.json; no test weakened.

Scope self-check: ACCEPT WITH LIMITATIONS; independent Chat review PENDING.
Whole-platform acceptance remains REVISE due to B01/B03/B04/B05/B06/B07.
Hardware identification only; no functional PS↔PL transport, acoustic output or levitation validated.
No driver/EEPROM/boot/jumper/PCB change; no reset/program/download command. JTAG targets closed and
hw_server connections disconnected after each scan. NOT RELEASED, NOT DEPLOYED.
DOCUMENTATION_UPDATE_REQUIRED for Work-owned narrative files and interaction memory; Work OFF.
