---
problem_id: P-20260925-001
project_id: SONOFIELD_FPGA
active_version: v2
current_stage: SCHEMATIC_DESIGN_JLCEDA_PRO
status: OPEN
created_at: 2026-09-25
created_by: Codex
chat_source_name: SonoField-FPGA
problem_hash: SEE_ADJACENT_SHA256_FILE
---

# Serializer hold margin and independent shutdown decision

## Decision needed
Select a physical clock/data distribution solution that closes worst-case hold
timing, and define the independent watchdog/power qualification boundary. No RTL
frequency, output interface or safety architecture change has been authorized here.

## Goal and repository facts
128 coherent channels, 32 serial lanes, four used 595 outputs per lane; 132 MHz
core / 66 MHz shift clock. Current RTL changes serial data on the falling half
cycle. Candidate board uses AXC8T245 translation and clock-only LVC244 buffering.
Source baseline: bad4f665889b12f8b75245d9513ae3919fa0cca3.
See v2/rtl/output/serializer.sv and v2/docs/hardware/PCB_SOFTWARE_INTERFACE.md.

## Evidence
PCB/V1/log/review/electrical_findings.md and primary-source metadata under
PCB/V1/log/datasheet. TI LVC244A worst-case delay at 3.3 V +/-0.3 V is 5.9 ns
(-40..85 C), 7.2 ns (-40..125 C). LVC595A hold requirement is 1.5 ns.
Ideal half-core interval is 1000/132 = 7.575758 ns.
Residual before translator, FPGA IO and cable skew: 0.175758 ns or -1.124242 ns.
This fails a robust worst-case closure argument; it is not measured hardware failure.
VCCA/VCCO and physical interconnect delays remain unknown (B03).

## What Codex tried
Read RTL edges, manufacturer timing tables and candidate pin maps. Preserved the
existing RTL and recorded conditional limits. No frequency reduction, replacement
logic family, fabricated board pins or physical timing claim was made.

## Candidate directions
1. Match data/clock paths with a characterized topology. Preserves bandwidth;
   requires board-level skew analysis and may change buffer count/BOM.
2. Re-time or phase-shift serializer data relative to its external clock. Requires
   a reviewed clocking/interface change and independent RTL/timing verification.
3. Reduce serial rate only if 10.24 MHz state-refresh throughput and latch overhead
   remain satisfied. A nominally slower part is not a solution without arithmetic.

## Independent shutdown
OE pulls cover reset/disconnection but do not establish shutdown on a stopped,
configured FPGA that retains enable. Decide a watchdog/heartbeat and power-good
qualification circuit, including startup and brownout behavior. Do not treat the
eFuse AUXOFF pin alone as a complete multi-rail supervisor.

## Constraints and acceptance impact
Keep user-controlled version v2 and schematic-only V1. No PCB layout or fabrication.
Full timing/safety review cannot pass until the chosen direction is verified over
voltage, temperature, load, skew and loss-of-clock/reset/power cases.

## Preliminary assessment (Codex, not ChatGPT decision)
Do not freeze the current clock-only buffer chain. Continue independent capture and
pin/net audits while withholding physical timing and system safety acceptance.

## Questions for ChatGPT / user
1. Which timing remedy and operating temperature range should be adopted?
2. What maximum watchdog shutdown latency and heartbeat semantics are required?
3. What independent simulations/measurements constitute closure of B04 and safety?

## User approval boundary
Any change to serializer interface, clock plan or hardware safety architecture needs
an explicit adopted decision. No external ChatGPT history or decision is accessible;
no Decision record has been invented.
