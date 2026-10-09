# CODEX_RESULT — v2 board transport / PS-PL preflight

PROJECT_ID: SONOFIELD_FPGA  
project_name: SonoField-FPGA  
Repository: https://github.com/loverlike1216/SonoField-FPGA.git  
Workspace: E:\Codex_project\AMD-SonoField-FPGA  
Version/branch: v2 / main  
Stage: BOARD_TRANSPORT_AND_PS_PL_INTEGRATION_PREFLIGHT  
Starting HEAD: d25e1d857334c061493459ce49a24debba222432  
Ending engineering source HEAD: b7f285896f78334d66091328f46aa4f657504430. Final evidence-only checkpoint follows this source commit; the containing Git commit identifies the delivered report.

This is a Codex engineering self-check. Independent Chat/user acceptance is PENDING. Work remains OFF.

## Implemented

- Physically confirmed XC7Z020/CLG400 persisted in chip_marking_fact.json and board_identity.json. ABX22 is not treated as speed grade. Speed/temperature/full ordering code remain UNKNOWN; canonical exact_part=null.
- Existing real JTAG evidence retained: xc7z020 IDCODE 0x23727093, ARM DAP 0x4BA00477, direct Vivado 2025.2 connection; FT2232H 0403:6010 A/MI00 and B/MI01. This run did not repeat JTAG or program the board.
- Complete CLG400 legality audit: 400 package balls, 125 PL IO (Bank13=25, Bank34=50, Bank35=50), Bank33 absent. 101 primary constraint entries and 346 total source claims audited. Package bonding does not prove board routing or VCCO.
- CEC=J5 is PS_DDR_BA2_502, not PL. J15 in a secondary picture is not automatically substituted. J3/J4 numbering, J4 pin1, duplicate pin6 D18/E18, J6 V16 and Y16/V16 conflicts remain explicit in constraint_conflicts.json. No XDC accepted.
- SerialBoardTransport has real pyserial I/O, mandatory VERIFIED profile, nonce handshake, version/capability/status, safe-disable, reads and restricted writes. Current profile remains UNVERIFIED and no real COM4 was opened.
- Binary SFP2 protocol implements command/sequence/length/CRC, duplicate rejection, timeout and reconnect behavior. Initial capability BASIC only; map/motion client methods are gated and PS rejects later-stage commands as UNSUPPORTED.
- PS service C core implements parser/dispatch/MMIO callbacks/watchdog. Actual host C is tested through Python packets. Zynq UART/MMIO entry source exists, but verified BSP/XSA, ARM linking, bus-fault handling and target deployment remain NOT_VERIFIED.
- AXI4-Lite bridge buffers channels independently, handles backpressure/errors/timeouts/reset/IRQ, and connects to the existing native register bus without changing its map. Real sono_axi_system wrapper is tested with external outputs disabled.
- Calibration capture RAM write moved to an equivalent synchronous process to fix Vivado BRAM inference. No motion/phase algorithm rewrite, PCB change or frozen v1 edit.

## Real tool evidence / validated

- PowerShell7.6.5, Python3.10.11, GCC9.2.0, Icarus12 development build, Vivado2025.2 build6299465; tool_environment.json.
- 112 Python tests PASS, including15 protocol/backend tests against compiled C (-Wall -Wextra -Werror). Not a physical UART test.
- AXI24 checks plus real wrapper test PASS in both Icarus and XSim: independent AW/W, read/write, backpressure, partial/zero strobes, illegal address, delayed error, timeout, reset, motion ownership, IRQ and safe outputs.
- Full3696-frame GUI/RTL motion path PASS in three Icarus runs plus XSim; exact trajectory/map/trap/ACK hashes match. Production cadence and fault injection pass both tools.
- Inherited phase/waveform/model-map/serializer and self-calibration gates PASS, including exact1024x8 ADC roundtrip and128 short RTL captures. Synthetic noise robustness retains failures outside fixed baseline limits; no physical calibration claim.
- Frozen v1 integrity PASS (212 files). Source manifests use canonical LF UTF-8. Fresh sparse clone (v1 worktree absent) and fresh venv PASS:112 Python tests, complete GUI/XSim path with exact baseline hashes, repository audit and both AXI simulator tests. The source manifest, including C firmware, matches the clone.
- Candidate-only OOC synthesis completes for xc7z020clg400-1/-2/-3: each8681 LUT,17996 registers,4 BRAM. This is not TARGET_SYNTHESIS_PASS.
- 132 MHz core setup WNS: -8.128/-4.995/-3.609 ns: FAIL. No place/route, external timing closure or bitstream. Worst -1 path runs from carrier_acc_reg[7] to serializer bit_index_reg[0]/CE. P-20260927-001 requests a decision before architectural timing changes.
- Diagnostic 33 MHz -> MMCM792 MHz VCO ->132/66 MHz reports exist. Explicit jitter assumptions and reset/CDC limits are in CLOCK_ARCHITECTURE.md. Clock-only PS7 DRC warning and missing external delay/skew constraints remain disclosed.
- Original failed attempts and the raw resource-summary zero-count reporting defect are preserved. Corrected resource summary is parsed from actual utilization.rpt, not invented replacement values; see FAILURES_AND_CORRECTIONS.md.

## Board status and blockers

B01: PARTIALLY_RESOLVED_STILL_BLOCKING; silicon/package confirmed, speed/temperature/ordering code unknown.  
B03: OPEN; connector contradictions, VCCO, IO standards, actual clock and PS UART routing unverified.  
B04: OPEN; physical66 MHz serializer path and independent watchdog/power qualification unverified.  
CORE_TIMING: OPEN; all three candidate core timing reports fail at132 MHz.  
B05/B06/B07: transducer/levitation/analog reference and acquisition hardware remain unverified.

Windows PnP recheck at19:35 +08:00 still shows FTDI A/B and COM4 OK, VID/PID0403/6010. COM4 existence does not prove PS MIO routing. PC Ethernet is disconnected; no board network transport identified. Preferred future route is verified FTDI B UART if schematic/continuity establishes the connection. JTAG currently proves identification/debug access only.

No serial bytes transmitted, no driver/EEPROM/boot switch changes, no PS register writes, no program download, no unknown GPIO and no external array/ADC/AFE/ultrasonic operation. No physical levitation or motion is claimed. NOT_RELEASED; NOT_DEPLOYED.

## Reproduction / remaining work

Run from v2 using pwsh and installed tools:

```powershell
../.venv/Scripts/python.exe scripts/board_transport_gate.py
../.venv/Scripts/python.exe scripts/motion_gate.py --output build/board_transport_regression
../.venv/Scripts/python.exe scripts/motion_reproduce.py --target build/board_transport_standalone --output v2/evidence/board_transport/standalone
```

The fresh-clone command requires a committed source and a new destination. Install requirements-lock.txt plus requirements-board.txt into a fresh venv. Candidate diagnostics use scripts/audit_clg400_parts.tcl and candidate_board_synthesis.tcl; never promote a candidate into verified_board.tcl.

Before a physical smoke test: obtain independent speed/temperature/ordering and UART MIO/control-line evidence; resolve pin/VCCO/clock conflicts; review PS reset/DDR/clocks/XSA/BSP/address map; decide the timing-closure approach; build a minimal top with acoustic outputs disabled/unconnected; pass correctly targeted synthesis/implementation/timing and review the board-only test scope. No hardware stage starts automatically.

General plans/README/decisions/interaction memory remain historical and are marked DOCUMENTATION_UPDATE_REQUIRED / STATE_CONFLICT_DETECTED in canonical engineering state. Current instruction explicitly authorizes this stage's technical evidence; Work did not run. Existing untracked schematic backup is preserved, not committed.

Stage evidence: summary.json, protocol_tests.json, axi_bridge_tests.json, source_manifest.json, regression_complete/summary.json, candidate_synthesis/summary.json and source reports. Preflight/tests and fresh-source reproduction are complete. Code/RTL are unchanged since the source commit above; the remaining commit records evidence/state only. Remote equality is checked after the final push and reported in the final Codex response; no remote result is inferred from this file.

## Session checkpoint / result

CODEX_CHECKPOINT: OFFLINE_INTEGRATION_PASS; REAL_TRANSPORT_BLOCKED_BY_BOARD_FACT.
Next owner: Chat/user independent review. Work OFF. No formal architecture decision or final platform acceptance is fabricated.
Tracked engineering tree is checkpointed; the preexisting untracked schematic backup remains preserved.
Scope: this offline preflight/software integration stage only; target synthesis/timing, PS deployment, UART hardware and acoustic operation remain blocked.

ACCEPT WITH LIMITATIONS
