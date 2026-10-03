# SonoField-FPGA v2 — current pre-PCB result

PROJECT_ID: SONOFIELD_FPGA
project_name: SonoField-FPGA
repository: https://github.com/loverlike1216/SonoField-FPGA.git
workspace_path: E:\Codex_project\AMD-SonoField-FPGA
branch: main
active_version: v2
stage: TIMING_CLOSURE_REAL_BOARD_INTEGRATION_AND_PRE_PCB_INTERFACE_FREEZE
current_model: GPT-6.1 Sol High (user-declared; exact runtime variant not exposed)
starting_HEAD: bd9e79f622ee58ea970870071702eb24596cd753
validated_source: 9936a737c45bf61f1908863a94f6374c6b5c828c
remote_verified_checkpoint: dea455f3f0e1c9e10d28b26559d01ba3f484e252
ending_HEAD: see repository `git rev-parse HEAD`; later sync-record commit follows the already verified checkpoint

## Implemented / tested

New personalized rules reviewed before work. Current-version/decision/evidence continuity preserved. Complete part user-confirmed. Bounded queue pointer/channel/timer/watchdog/occupancy and balanced17-bit selection, plus a measured scheduler CE repair, preserve observable cycle behavior. Original/new comparisons cover depths2/4/5 and64,096scheduler cycles, successful captures, rejected commands and faults. The inherited serializer is restored unchanged; the first strict-guard failure remains archived.

115Python tests; complete inherited waveform/calibration/ADC regression;3696-frame motion demonstration in three Icarus runs and one Vivado XSim run; exact map/trajectory/trap/ACK hashes; current-source offline AXI/host-C protocol checks PASS. Separate upper/lower array-disable adapter is implemented and tested in both simulators, with shared clocks and fresh-frame release; it is not integrated into a physical wrapper.

## Real tool evidence

Vivado2025.2 strategy3 fully routed21,475nets,zero routing errors. Internal132MHz OOC WNS+0.082ns,TNS0,WHS+0.072ns,THS0; internal unconstrained endpoints0 and no_clock0. Both normal synchronous and asynchronous recovery/removal paths remain analyzed; no false/multicycle exceptions were added. Strategy2 remains archived with WNS-0.284ns and84failed setup endpoints. Strategy1 was interrupted after measured prolonged congestion; it has no final post-route result.

Current serializer accepted100consecutive starts spaced11cycles in each simulator. Minimum core frequency at41.5kHz×256 is116.864MHz;132MHz meets digital throughput. N18/33.333MHz is the latest approved document fallback. A vendor-synthesized MMCM candidate gives131.998680MHz (10ppm below nominal132MHz); it is not integrated or selected as a final board clock.

Windows USB descriptors VID0403/PID6010/REV0700 identify a reported FT2232H variant, interfaces MI00/MI01 and COM4. Managed COM enumeration sees COM4 even though Win32_SerialPort returned no rows. Official FTDI descriptor basis: [FT2232H datasheet](https://www.ftdichip.cn/Support/Documents/DataSheets/ICs/DS_FT2232H.pdf). Vivado directly discovered ARM DAP0x4BA00477 and XC7Z0200x23727093. No driver replacement was needed. Cable descriptor naming is not a board-model proof.

## Board facts / connector references

XC7Z020-1CLG400C is USER_CONFIRMED_PHYSICAL_FACT; JTAG independently confirms family only. The new Excel/image supersede legacy pin/clock-document precedence. All64connector signal pins are legal and unique in the confirmed part database. J3/J6 bank34, J4 bank35, J5 spans34/35; N18 is bank34 MRCC. Document mapping is verified, actual continuity/voltages are not. B01 resolved. B03 partially resolved: document conflicts resolved, electrical and physical routing gates remain OPEN.

J3upper/J4lower each16lanes for64TX. J5/J6 control budgets retain ONE central8RX AD7606B, not two ADC buses.5V connector pins are AUX/UNUSED and do not specify VCCO. Candidate config/docs are provided; no fabricated XDC or electrical freeze. ADC SCLK is core/4≈33MHz, distinct from TX shift core/2≈66MHz. [AD7606B Rev B](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7606b.pdf) supports a frequency check, but off-chip min/max delay/loading still need qualification.

## Not validated / blocking

Bank34/35VCCO and IO standards; physical connector orientation/continuity; FTDI-B TX/RX↔PS UART/MIO and DTR/RTS routing; actual PS reference clock/reset/preset; reviewed XSA/BSP and linked Cortex-A9 firmware; real100/1000PING/PONG; PC↔PS↔AXI↔PL readback; real128-channel map/ACK generation; real GUI transport; ILA; external timing and fail-safe driver/ADC qualification. The current PS service advertises BASIC only and rejects reserved map commands; future implementation must distinguish fresh map completion from raw write_ready or an old active_valid. See PS_PLATFORM_AND_TRANSPORT_REMAINING.md.

Routed DRC retains RAMB36async-control,missing-PS7 and rule-limit warnings. Methodology retains LUT-derived-reset and missing external-delay warnings. These are not waived by internal timing PASS. Final board/PS integration must re-run implementation and review reset/BRAM behavior. An exact manual acquisition list is MISSING_PHYSICAL_FACTS.md; N18frequency measurement and unreadable part digits are not reintroduced as blockers because the user supplied explicit fallback/identity authorization.

## TCT40 and next physical hardware

10mm body,12mm radiating-center pitch,opposed8×8arrays,100mm face gap adjustable90..115mm,origin at geometric center remain the approved geometry. Vendor image claims are not batch electrical measurements. Keep independent requested/calibration, polarity/load/phase characterization and conservative10→12→16→~20Vpp qualification. No emitter, externalPCB, ADC board or levitation test was performed.50mg remains a staged final target, not a guarantee; measured5/10/25/50mg milestones follow basic particle bring-up.

## Integrity / synchronization / next stage

Frozenv1 and historical tool/model records remain unchanged; native PCB files unchanged. Uploaded active-project instructions, pin workbook/image and available references are classified with original hashes. GPS-bearing original board photograph and raw USB/cable/network identifiers are local-only; public records are sanitized. External ChatGPT history remains BLOCKED; actual observable current Codex transcript is PARTIAL. No ChatGPT decision or review is fabricated.

Next: obtain exact physical facts, construct verified PS/clock/reset/AXI platform and gated bare-board firmware; validate real transport/map/GUI; freeze bank voltages/IO/external budgets and independent disables; only then connect arrays/ADC and enter measured characterization. No program was downloaded, COM was not opened, drivers/boot/GPIO/externalPCB were not changed.

PRE_PCB_BOARD_READY = NO

REVISE

Fresh source checkout:115tests,212frozenfile coverage and queue/scheduler/serializer/array safety both-simulator checks PASS. Same machine/pinnedvenv, not a second machine. Source and checkpoint pushed and verified as recorded in delivery_sync.json.
