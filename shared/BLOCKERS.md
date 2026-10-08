# Current v2 blockers — 2026-10-03

Current model: GPT-6.1 Sol High. B01 RESOLVED: XC7Z020-1CLG400C user-confirmed. Internal CORE_TIMING RESOLVED in strategy3: routed132MHz WNS+0.082,TNS0,WHS+0.072,THS0,zero routing errors. B02 current source priority superseded by explicit N18/33.333MHz fallback; measurement is not required to proceed with that documented fallback.

| Gate | Current status | Required next evidence |
|---|---|---|
| B03 | DOCUMENT_MAPPING_RESOLVED; ELECTRICAL_ROUTE_OPEN | Bank34/35 VCCO,actual connector orientation/continuity,matched IO standard and translator voltage |
| PS/UART | BLOCKED | FTDI-B TX/RX/DTR/RTS to UART instance/MIO; PS reference clock/reset; reviewed preset/XSA/BSP/ARM build |
| Real transport | NOT_RUN |100/1000 packets,safe MMIO,atomic map/ACK generation,real GUI/ILA after verified platform |
| B04 | OPEN | Off-chip min/max timing,loading,watchdog,power and ADC/driver qualification; review retained DRC/methodology warnings |
| B05/B06/B07 | OPEN_PHYSICAL | Actual10mm batch load/polarity/phase/amplitude,receiver/ADC reference and measured levitation |
| Independent Review | PENDING | External review of actual source,warning scope and hardware evidence; no fabricated ChatGPT approval |

Detailed acquisition list: v2/evidence/pre_pcb_board_ready/MISSING_PHYSICAL_FACTS.md. No unknown-pin XDC,driver replacement,boot change,serial opening,bitstream download or PCB operation occurred. External ChatGPT history is BLOCKED and observable Codex transcript PARTIAL; these do not prevent sourced digital work.

---

The following historical blocker narratives retain original provenance; current status is above.

# Blocking facts and decisions

## B01 — Exact part/package/speed grade
Zynq-7020 family identified. Board photos do not establish a reliably readable complete ordering code.
No schematic, BOM, manual or reference Vivado project is supplied. Do not select a guessed part.
Blocks target synthesis, implementation and bitstream. Need legible chip marking or manufacturer BOM.

## B02 — Clock source precedence RESOLVED by user
hardware.const and EDA screenshot label N18 `33MHZ`; 3.png and the full peripheral table label
N18 `33.333MHz`. User explicitly directed that constrain files prevail. Adopt N18 / 33,000,000 Hz
as the documented input clock. Physical oscillator tolerance/frequency remains unmeasured.
High-rate serializer clock still requires a justified clock-generation design and timing validation.

## B03 — GPIO/voltage conflict (DECISION_CONFLICT)
Problem: physical connector numbering conflicts. Evidence: gpio.const J3 pin1=T20 while 1.png
pin1=U14; J4 pin1=H15 versus F19. J4 Pin6 occurs twice in .const (D18,E18).
J6 V16 has no pin number in .const; 2.png lists V16 twice (16 and 20), whereas layout image
shows Y16 on the earlier row. HDMI CEC is J5 in hardware.const and J15 in tables.
Existing decision: user explicitly selected constrain files over screenshots.
Conflict: cross-source differences resolved by this precedence; duplicate/missing entries within .const remain unresolved.
Options: obtain revision-matched schematic, or manufacturer-confirmed pinout plus unpowered continuity test.
Recommendation: resolve against manufacturer schematic before any board XDC or PCB connector assignment.
Connector 5V supply labels do NOT establish FPGA bank VCCO or 5V-tolerant GPIO.

## B04 — Serializer electrical architecture
128 arbitrary 8-bit phases require 10.24 MHz simultaneous state refresh; serial bandwidth is 1.31072 Gbit/s.
16 lanes x 8 bits need at least 81.92 MHz bit rate before latch/setup overhead. Logic simulation of a
fast interface is not evidence that a 74AHC595 board supports it. Candidate must pass worst-case
datasheet timing, loading, fanout, voltage and routed timing review before PCB-A is frozen.
v1 implements and simulates a 32-lane/four-used-output alternative at 132 MHz core, 66 MHz shift
clock. AHCT at 5 V is the conditional component candidate. Board PLL, IO voltage and electrical
timing/clock distribution remain unverified; no PCB freeze is authorized by a digital PASS.

## B05 — Purchased transducer and physical validation
No batch measurements, driver prototype, calibrated pressure, object mass or levitation evidence supplied.
PH0 onward remain unvalidated. Absolute force and 50 mg support cannot be inferred from normalized pressure.

## B06 — New 10 mm part electrical/mechanical qualification
User selected the pictured nominal 10 mm transmitter and a 128-channel planar geometry. This resolves
geometry choice, not exact part identity. Capacitance, active aperture, drive rating, actual dimensions,
mounting standoff and acoustic polarity remain unknown. Do not reuse the old 16 mm ratings.
Nominal radiating-center coordinates are ready to implement; PCB/drill dimensions and power-stage freeze
require batch measurements. Source: v2/hardware/transducers/10mm_supplier_reference.md.

## CHAT_MEMORY_ACCESS_BLOCKED — external history
User designated SonoField-FPGA. No exposed tool can read its external ChatGPT history.
AI-chat-memory records BLOCKED with zero imported messages. This blocks automatic history/decision
sync, not v2 bootstrap organization or available digital tests. See AI-chat-memory/CHAT_MEMORY_IMPORT_REQUIRED.md.

Open consultation records: AI-problem/problem/P-20260919-001 (B01/B03), 002 (B04), 003 (B05/B06).


## v2 bootstrap revalidation (2026-09-21)
New BOM selects the part baseline but does not close B01/B03 board facts, B04 physical timing,
or B05/B06 batch qualification. The original three v1 Problem records retain original version/body
hashes; they are historical consultations, not executable v2 decisions. No external decision was imported.
The new formal user instruction authorizes architecture requirements directly. Full v2 calibration/ADC
runtime remains future work; this is not a bootstrap implementation defect.
BOM review: v2/hardware/bom/BOM_LOCK.md. Imported old version metadata is superseded by user approval.


## Current software/digital stage update (2026-09-21)

The bootstrap-only future-work statement above is historical. v2 now implements and simulates
ADC acquisition and self-calibration; see current report/evidence. Board-target synthesis,
implementation, CDC/timing closure and all physical tests remain blocked by B01/B03/B04/B05/B06.
B04's old AHCT candidate is superseded for v2 by the user BOM SN74LVC595APWR / SN74AXC8T245PWR /
SN74LVC244APWR contract. Its 66 MHz physical timing concern remains open.

## B07 — real RX/TX timing and phase references (hardware gate)

Opposite-bank measurements form two phase graphs with independent gauges. Simulated RX anchors
are not physical calibration. Before using a full calibrated hardware LUT, measure reference phase
in each bank, receiver group delay and TX onset/ringup relative to captured clocks. Synthetic
35 dB performance cannot substitute for that reference. Also validate the source-synchronous ADC
return timing through actual translator/cable and provide the PS transport wrapper. Software rejects
a real record paired with simulated reference provenance. This blocks physical deployment, not
the explicitly authorized synthetic/digital stage.

## Schematic V1 findings — 2026-09-26
P-20260925-001 documents the B04 clock-only buffer hold risk and missing independent watchdog/power qualification. No external ChatGPT decision is available. Native ERC has2single-pin logical endpoints (HARDWARE_ENABLE,RST_N) and43supplier-attribute warning groups; do not suppress them. Generic templates are not final procurement parts.
B06 baseline is now user-supplied TCT40-10T/R1 design input; manufacturer provenance and purchased-batch qualification remain open. No 16 mm ratings are transferred.
Read PCB/V1/log/review/electrical_findings.md and ERC_DISPOSITION.md. Native capture is complete as a draft; electrical release is not accepted.

## Current engineering update — 2026-10-03

Recording model: GPT-6.1 Sol High; previous sections retain their historical scope. Real earlier JTAG identified XC7Z020, IDCODE0x23727093; user chip photograph established CLG400. B01 is PARTIALLY_RESOLVED: physical speed/temperature/full ordering code still UNKNOWN. Explicit conservative -1 engineering authorization permits bounded timing analysis; it does not identify the physical grade.

CORE_TIMING: two real route rounds failed. Latest WNS -4.515 ns,TNS -6007.936 ns; required throughput minimum116.864MHz excludes the only tested fixed-route positive-slack profile82.5MHz. P-20260929-001 records the selector/enable/reset RCA and next decision.

B03 remains OPEN: FT2232H B/COM4 was enumerated historically, but no verified bridge-to-PS UART MIO route, VCCO/connector facts or reviewed PS preset/XSA/BSP. Target ARM firmware compilation and real UART transmission are blocked. B04 remains OPEN: serializer physical clock/data/latch timing and watchdog/power qualification are unmeasured. B05/B06/B07 retain physical batch/calibration/levitation limitations.

STATE_CONFLICT_DETECTED: prior shared narratives and machine-state evidence pointers describe older stages; current real evidence and recovery summary prevail. Previous GUI retry FAIL is retained separately from the earlier PASS and the new recovery run. No hardware result is promoted by the model switch. Work OFF; CURRENT_PLAN/HANDOFF/general narrative refresh remains DOCUMENTATION_UPDATE_REQUIRED.


Current validation update — 2026-10-03, GPT-6.1 Sol High: fixed-source recovery PASS,114Python tests,3696TRAP_VALID frames,threeIcarus/oneVivadoXSim matching canonical hashes,calibration/ADC and frozen-parent gates. Saved-preview defect fixed and failure retained. Routed Gate A remains FAIL; physical PS/PL and acoustic operation NOT_RUN. Acceptance thresholds unchanged.

## DDR detection continuation — 2026-10-04

Model: GPT-6.1 Sol High. Active v2 and existing Stage unchanged. Current read-only native Vivado2025.2 scan confirms XC7Z020 IDCODE0x23727093; Micron public decoder identifies D9PSK as MT41K128M16JT-125 IT:K. Photo shows two2Gb x16 devices, but512MiB/32bit remain CANDIDATE. XSDB/AP0 reads DDRC_CTRL0x00000200 andCTRL_REG1 0x0000003E, both documented reset values; controller reset not released, so32bit default field is not board topology proof. No CPU halt/reset/init,DDR memory access,download,COM,GPIO orPCB operation. Original Vivado GUI preserved. Report: parameter_detection/20261004_ddr/RESULT.md; candidate: v2/config/ddr_candidate.json. Existing core115tests/132MHz timing retain their2026-10-03 source/date; not rerun today.

B01 remains resolved by prior user full-part confirmation and JTAG family; B03 remains PARTIALLY_RESOLVED, with actual PS/DDR configuration, PS clock/reset/UART and VCCO unknown. Missing manufacturer/reference configuration is BOARD_MATCHED_PS_DDR_CONFIGURATION_OR_MANUFACTURER_TOPOLOGY_MISSING. Observed reset-only state is DDR_CONTROLLER_OBSERVED_IN_RESET_NO_EFFECTIVE_CONFIGURATION. Neither means defective DDR. Generic ZedBoard/ZC702 presets and guessed capacity cannot close these gates.


## Current AX7020 v5 blockers — 2026-10-08

Prior B01/B03 etc above retain Robei/v2 historical scope; they are not reopened or closed as AX7020 facts. Current blockers:

- V5-B01: Physical AX7020 board/revision/order code/VCCO and documented-pin match not verified
- V5-B03: Revision-matched PS DDR/clock/preset, XSA/BSP and real host transport/PS-PL runtime absent
- V5-B04: Production IO/XDC/external timing, actual serializer/driver/ADC/safety qualification not completed
- V5-B05: 10mm emitter batch, RX phase reference, physical trap and measured particle milestones not tested
- CHAT_MEMORY_ACCESS_BLOCKED: No supported tool to read external ChatGPT SonoField-FPGA history/review

No organization/source-path blocker remains after real gates. These blockers prevent physical/full-platform acceptance, not continuation of current digital development. No board access/programming was performed this iteration.

## Current v5 BOM review — 2026-10-08

V5-BOM_REVIEW: REVISE / electrical release HOLD. Source and findings:v5/hardware/bom/submissions/2026-10-08/submission.json. ADP7118 wrong package; TVS/eFuse surge coordination; AD7606B40kHz bandwidth(P-20261008-001 OPEN); exactTX/RX specifications; external timing/pin map/powered-off safety and passive-net qualification. No new hardware/PCB test. Earlier v2 blockers above retain historical board scope.
