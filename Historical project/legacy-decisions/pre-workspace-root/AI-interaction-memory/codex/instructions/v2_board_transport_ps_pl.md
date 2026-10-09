# SonoField-FPGA v2
# Stage: BOARD_TRANSPORT_AND_PS_PL_INTEGRATION_PREFLIGHT

## 0. PROJECT

PROJECT_ID: SONOFIELD_FPGA

project_name:
SonoField-FPGA

repository:
https://github.com/loverlike1216/SonoField-FPGA.git

workspace:
E:\Codex_project\AMD-SonoField-FPGA

branch:
main

active_version:
v2

primary tool:
AMD Vivado 2025.2

physical board:
Robei Octagonal Board / Zynq-7020

Current verified GitHub checkpoint:

d25e1d857334c061493459ce49a24debba222432

Continue CURRENT v2.

DO NOT create v3.

v1 remains frozen.

---

# 1. NEW PHYSICAL EVIDENCE FROM USER

The user has now supplied a clear physical photograph of the main Zynq package.

Readable package markings:

XC7Z020

CLG400ABX22

TAIWAN

Treat the following as newly supplied physical evidence:

DEVICE:
XC7Z020

PACKAGE:
CLG400

The text:

ABX22

must NOT be interpreted as speed grade unless an authoritative AMD marking reference explicitly proves that interpretation.

Current speed grade:

UNKNOWN

Current temperature grade:

UNKNOWN

Therefore:

B01 is NOT fully closed.

Update its meaning from:

"device/package/speed unknown"

to:

"device and CLG400 package physically confirmed;
speed/temperature/full ordering code still unresolved."

Do not set:

xc7z020clg400-1

xc7z020clg400-2

or any other exact Vivado part as the canonical physical target without independent evidence.

---

# 2. CURRENT VERIFIED BOARD FACTS

Retain the previous real hardware evidence:

FTDI:
FT2232H

VID:
0x0403

PID:
0x6010

interfaces:
A / MI_00
B / MI_01

JTAG:
VERIFIED

Vivado 2025.2:
DIRECT JTAG CONNECTION VERIFIED

detected FPGA:
xc7z020

FPGA IDCODE:
0x23727093

ARM DAP:
0x4BA00477

FT2232 B:
COM4 exists

COM4 PS UART path:
NOT YET VERIFIED

documented PL clock precedence:
N18 / 33 MHz

No bitstream has been downloaded.

No external GPIO has been driven.

No external SonoField PCB is connected.

---

# 3. IMPORTANT CLG400 PACKAGE AUDIT

The newly confirmed package is CLG400.

Before any board-target XDC is accepted:

perform a complete CLG400 package legality audit.

Use:

AMD/Xilinx official Zynq-7000 package documentation
+
Vivado 2025.2 installed device database
+
repository board constraints.

Important package facts to verify and record:

- XC7Z020 CLG400 is the actual package family;
- PL Bank 33 is not bonded in CLG400;
- Bank 13 is only partially bonded;
- PS banks are bonded.

Do NOT assume a pin available in CLG484 is available in CLG400.

---

# 4. AUDIT EXISTING BOARD CONSTRAINTS

Inspect:

E:\Codex_project\AMD-SonoField-FPGA\Zynq7020

especially:

constrain/hardware.const

and all other pin/reference files.

For every claimed FPGA pin record:

logical signal
connector
connector pin
FPGA package pin
bank
package availability
source file
confidence.

Create:

v2/evidence/board_transport/clg400_pin_audit.json

and:

v2/evidence/board_transport/CLG400_PIN_AUDIT.md

Specifically re-check existing B03 problems:

- J3 numbering discrepancy;
- J4 Pin1 discrepancy;
- duplicated J4 Pin6 D18/E18;
- missing/ambiguous V16/J6 mapping;
- Y16/V16 inconsistencies;
- HDMI/CEC naming differences;
- any pin belonging to non-bonded Bank 33;
- any partially bonded Bank 13 assumption.

Do NOT "resolve" duplicate constraint entries by choosing one arbitrarily.

---

# 5. VIVADO PART-CANDIDATE MATRIX

Because speed grade is unresolved, do NOT weaken:

v2/scripts/create_project.tcl

and do NOT install a guessed default exact part.

Instead create a separate diagnostic script, for example:

v2/scripts/audit_clg400_parts.tcl

Its purpose is diagnostic only.

Use Vivado:

get_parts

to enumerate installed parts matching:

DEVICE = xc7z020
PACKAGE = clg400

Record all valid Vivado part names.

For each candidate record:

part
package
speed grade
availability in Vivado 2025.2.

Candidate enumeration is NOT physical identification.

Do not promote any candidate into:

verified_board.tcl

until speed-grade evidence exists.

---

# 6. OPTIONAL CANDIDATE SYNTHESIS

To avoid blocking engineering progress, candidate-only out-of-context synthesis MAY be run against every valid XC7Z020/CLG400 speed-grade candidate.

Purpose:

- confirm RTL elaborates for CLG400;
- compare utilization;
- inspect speed-grade sensitivity;
- detect package-related incompatibilities;
- identify whether 132 MHz internal architecture has timing margin.

Classification must be:

CANDIDATE_ANALYSIS_ONLY

not:

TARGET_SYNTHESIS_PASS.

Do not generate a production bitstream from a guessed candidate.

Do not alter canonical B01 status.

---

# 7. CLOCK ARCHITECTURE REVIEW

Current physical PL input clock source remains:

N18 / 33 MHz

according to repository precedence.

The current motion/self-calibration simulation uses internal rates such as:

132 MHz core
66 MHz serializer shift clock.

Create a real clock-generation design review:

33 MHz input
→ MMCM/PLL
→ required internal clocks.

Check:

- legal MMCM/PLL multiplication/division;
- clock jitter assumptions;
- 132 MHz generation;
- 66 MHz serializer generation;
- ADC clock requirements;
- reset sequencing;
- clock-domain crossings.

Do not claim physical timing closure.

Store:

CLOCK_ARCHITECTURE.md

and candidate Vivado clock reports.

---

# 8. UART / COM4 PATH VERIFICATION

The next preferred PC transport candidate remains:

FT2232 B / COM4

but it is still only a candidate.

Goal:

determine whether COM4 is physically connected to Zynq PS UART/MIO.

Use evidence in this priority:

1. revision-matched board schematic/BOM;
2. manufacturer board documentation;
3. verified PCB routing/reference;
4. non-destructive continuity evidence supplied by user;
5. read-only PS/JTAG observations where useful.

Do NOT infer:

COM4 exists
therefore
COM4 = PS UART

without evidence.

---

# 9. SAFE READ-ONLY UART INVESTIGATION

If useful and safe:

inspect COM4 properties and FTDI B descriptors.

Do not transmit arbitrary bytes.

Do not change FTDI EEPROM.

Do not replace drivers.

Do not use Zadig.

Do not toggle unknown board control signals intentionally.

If opening COM4 might assert:

DTR
RTS

ensure they remain inactive where the API allows.

No user data writes are authorized until UART routing is established.

---

# 10. OPTIONAL PS READ-ONLY JTAG INSPECTION

Because ARM DAP is verified, Codex MAY use a documented Xilinx debug route to inspect PS state if this can be done read-only and without modifying the running board.

Possible useful observations:

- current PS reset state;
- MIO configuration;
- UART-related PS configuration;
- clock state.

Any such observation proves only:

current PS configuration

not:

physical FT2232-to-MIO routing.

Do not write PS registers in this preflight unless separately justified and authorized.

---

# 11. BOARD TRANSPORT ARCHITECTURE

Current repository already contains:

PC GUI
MotionController
TrapSolver
Phase LUT generation
SimulationTransport
RegisterTranscriptTransport

and PL contains:

sono_motion_system
motion_queue
existing synchronous register bus
128-channel atomic map update.

Do NOT rewrite these systems.

Implement the missing bridge architecture:

Windows PC
    ↓
BoardTransport
    ↓
FT2232 B / COM4 candidate
    ↓
Zynq PS communication service
    ↓
AXI4-Lite
    ↓
AXI-to-existing-register-bus bridge
    ↓
sono_motion_system
    ↓
existing phase engine.

---

# 12. BOARDTRANSPORT IMPLEMENTATION

Replace the current intentionally blocked architecture only by adding a real backend.

Do not remove the safety gate.

Suggested structure:

Transport
├── SimulationTransport
├── RegisterTranscriptTransport
└── SerialBoardTransport

SerialBoardTransport must remain unusable unless:

transport profile = VERIFIED.

Implement:

connect()
disconnect()
ping()
get_version()
get_status()
safe_disable()
read_register()
write_register()
send_phase_map()
commit_map()
wait_ack()
stop()

Do not allow motion immediately after connect.

---

# 13. PC ↔ PS PROTOCOL

Define a binary framed protocol.

At minimum:

MAGIC
PROTOCOL_VERSION
COMMAND
SEQUENCE
PAYLOAD_LENGTH
PAYLOAD
CRC

Commands for first hardware phase:

PING
GET_VERSION
GET_CAPABILITIES
GET_STATUS
SAFE_DISABLE
READ_REGISTER
WRITE_REGISTER

Later:

BEGIN_MAP
MAP_CHUNK / MAP_WRITE
COMMIT_MAP
GET_MAP_STATUS

Motion commands shall not be enabled until the basic transport passes.

---

# 14. PROTOCOL SAFETY

Required behavior:

bad MAGIC:
reject

bad version:
reject

bad CRC:
reject

duplicate sequence:
detect

timeout:
fail safely

disconnect:
SAFE_DISABLED

reconnect:
requires fresh handshake

protocol mismatch:
motion disabled

unexpected command:
error response

Never interpret corrupted data as register writes.

---

# 15. PS COMMUNICATION SERVICE

Create a small Zynq PS-side service architecture.

Preferred responsibilities:

UART receive
frame parser
CRC verification
sequence handling
command dispatch
AXI register access
response framing
watchdog / timeout
SAFE_DISABLE on communication loss.

Do not place acoustic mathematics in this first PS transport stage.

The existing PC software remains the motion/calibration reference implementation for now.

---

# 16. PS ↔ PL BRIDGE

Current PL exposes:

bus_valid
bus_write
bus_address
bus_wdata
bus_rdata
bus_ready
bus_error
irq.

Implement:

AXI4-Lite Slave
→ existing register-bus adapter.

Do NOT redesign the native register map.

Keep:

v2/config/register_map.json

as the canonical functional register definition.

Generate constants from one source where possible.

---

# 17. AXI BRIDGE VERIFICATION

Before any real-board programming:

build a self-checking RTL test for:

AXI write
→ native bus write

AXI read
→ native bus read

backpressure
invalid address
bus error
reset
simultaneous motion ownership
IRQ.

Run with:

Icarus
and
Vivado 2025.2 XSim.

No real board is required for this step.

---

# 18. REGISTER SAFETY

First real PS/PL access must be limited to harmless read/status operations.

Initial real-board sequence SHALL be:

PS/PC handshake
→ GET_VERSION
→ GET_STATUS
→ READ known read-only register.

Do NOT begin with:

MAP_COMMIT
NORMAL_FIELD
hardware_enable
serializer output
ADC capture
or ultrasonic control.

---

# 19. REAL BOARD TEST GATE

A real firmware/bitstream download remains forbidden until all of the following are true:

1. exact XC7Z020 package is confirmed — CURRENTLY YES: CLG400;
2. speed grade is independently verified — CURRENTLY NO;
3. selected Vivado PART exactly matches evidence;
4. N18/33 MHz XDC is reviewed;
5. PS reset/clock/DDR assumptions are reviewed;
6. UART route is verified if UART is used;
7. no unresolved output pin is driven;
8. top-level design keeps external acoustic outputs disabled;
9. synthesis passes;
10. implementation/timing review passes;
11. bitstream scope is explicitly a BOARD_SMOKE_TEST.

If speed grade remains unknown:

DO NOT download.

Stop at offline integration.

---

# 20. FIRST HARDWARE SMOKE TEST

Only after the previous gate is satisfied:

Program a minimal board image with:

all external SonoField outputs disabled.

First acceptance:

PC:
PING

PS:
PONG

Second:

GET_VERSION.

Third:

GET_STATUS.

Fourth:

read PL STATUS register through:

PC
→ UART
→ PS
→ AXI
→ PL
→ PS
→ UART
→ PC.

No external SonoField PCB shall be connected.

---

# 21. DO NOT TEST ACOUSTIC OUTPUT YET

This stage explicitly excludes:

TC4427
TCT40
ADC board
AFE
serializer physical output
external array GPIO
levitation
motion.

Even if the PL contains those modules, the physical smoke-test top must keep them disabled/unconnected.

---

# 22. CLG400-SPECIFIC PCB CONSEQUENCE

Because the physical package is now CLG400:

review all future PCB/FPGA interface assumptions against CLG400 bonding.

Create:

v2/docs/hardware/CLG400_BOARD_IMPACT.md

Record:

- bank availability;
- package restrictions;
- affected existing constraint claims;
- implications for array connector planning;
- implications for ADC return;
- implications for serializer lanes;
- remaining VCCO facts.

Do NOT modify the PCB project in this task.

---

# 23. B01 UPDATE RULE

After photo review:

B01 status should become approximately:

PARTIALLY_RESOLVED_STILL_BLOCKING

with:

silicon:
CONFIRMED XC7Z020

package:
CONFIRMED CLG400

speed grade:
UNKNOWN

temperature grade:
UNKNOWN

full ordering code:
UNKNOWN.

Do not mark B01 fully RESOLVED.

---

# 24. B03 UPDATE RULE

B03 remains OPEN until:

- actual bank VCCO is known;
- connector pin duplication/conflicts are resolved;
- usable PL pins are validated for CLG400;
- PS UART physical route is verified where relevant.

The package confirmation may help narrow B03 but does not close it.

---

# 25. B04

Continue reviewing the physical serializer architecture separately.

Do not confuse:

RTL PASS
candidate timing PASS
real routed board timing PASS.

Current 66 MHz physical serializer path remains unverified.

No PCB freeze.

---

# 26. ALLOWED WORK

Authorized:

- inspect current repository;
- inspect connected bare Zynq board non-destructively;
- update board identity evidence;
- add CLG400 package audit;
- enumerate Vivado candidate parts;
- run candidate-only OOC synthesis;
- implement PC protocol code;
- implement SerialBoardTransport behind verification gates;
- implement PS service source;
- implement AXI4-Lite bridge;
- implement simulation tests;
- run Python/Icarus/XSim;
- update docs/evidence/shared state;
- commit/push to existing repository.

---

# 27. NOT AUTHORIZED

Do NOT:

- create v3;
- modify frozen v1;
- guess speed grade;
- guess VCCO;
- guess connector mapping;
- suppress B03 conflicts;
- change FTDI drivers;
- use Zadig;
- rewrite FTDI EEPROM;
- drive unknown FPGA pins;
- attach external array PCB;
- enable ultrasound output;
- modify PCB design;
- fabricate hardware PASS;
- force push;
- release/deploy.

---

# 28. REQUIRED EVIDENCE

Store under:

v2/evidence/board_transport/

At minimum:

chip_marking_fact.json
clg400_part_candidates.json
clg400_pin_audit.json
constraint_conflicts.json
clock_architecture.json
uart_route_evidence.json
protocol_tests.json
axi_bridge_tests.json
python_tests.log
icarus.log
xsim.log
candidate_synthesis/
RESULT.md

If real UART/board testing becomes permitted:

serial_transcript.jsonl
ping_pong.log
pl_status_readback.log
vivado_synthesis.rpt
vivado_timing.rpt

---

# 29. ACCEPTANCE FOR THIS STAGE

The preflight/software integration part may PASS when:

- XC7Z020 + CLG400 is persisted as physical evidence;
- speed grade remains explicitly unknown unless proven;
- all CLG400 pin constraints are audited;
- all B03 conflicts are listed;
- PC packet protocol is implemented and tested;
- SerialBoardTransport exists but is safely gated;
- PS communication service is implemented;
- AXI4-Lite→native-bus bridge is implemented;
- Icarus/XSim tests pass;
- current motion/self-calibration regressions still pass;
- v2 remains standalone;
- no PCB or acoustic hardware is operated.

Real transport may only PASS if:

- UART route is verified;
- exact Vivado target is verified;
- real PING/PONG succeeds;
- real PS→PL readback succeeds.

Otherwise report:

OFFLINE_INTEGRATION_PASS
REAL_TRANSPORT_BLOCKED_BY_BOARD_FACT.

---

# 30. END REPORT

Report:

PROJECT_ID
version
branch
starting HEAD
ending HEAD

## Photo-derived board facts

## JTAG-derived board facts

## CLG400 package audit

## Exact-part status

## Constraint / pin audit

## B01

## B03

## B04

## COM4 / UART evidence

## BoardTransport

## PC protocol

## PS firmware

## AXI bridge

## Python / Icarus / XSim

## Candidate synthesis

## Real hardware tests

## Not validated

## Remaining blockers

## Next recommended action

End with exactly one:

ACCEPT
ACCEPT WITH LIMITATIONS
REVISE

and scope the conclusion to this stage.

Do not start PCB or acoustic hardware work automatically.