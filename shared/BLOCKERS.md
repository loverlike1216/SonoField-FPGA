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
