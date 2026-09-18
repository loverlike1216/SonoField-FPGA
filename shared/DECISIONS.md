# Architecture decisions — VN1

All user-directed decisions below are retained. New implementation choices do not override hardware gates.

| ADR | Decision | Status |
|---|---|---|
| ADR-001 | Robei Zynq-7020 is the main controller | Accepted by user; exact ordering code pending |
| ADR-002 | Vivado 2025.2 is authoritative EDA | Accepted |
| ADR-003 | TCT40-16T is low-cost first-generation transmitter | Accepted; characterize purchased batch |
| ADR-004 | Nominal acoustic frequency 40 kHz | Accepted |
| ADR-005 | Digital architecture supports 128 channels | Accepted |
| ADR-006 | First physical system uses opposed standing-wave arrays | Accepted |
| ADR-007 | 6x6 + 6x6 is serious demonstration target | Accepted, after P0/P1 |
| ADR-008 | 8x8 + 8x8 only for evidence-justified expansion | Accepted |
| ADR-009 | 8-bit phase representation | Accepted |
| ADR-010 | Independent per-channel calibration | Accepted |
| ADR-011 | Complete phase maps commit atomically at carrier boundary | Accepted |
| ADR-012 | Host acoustic solver first, advanced FPGA field solver later | Accepted |
| ADR-013 | 50 mg is a staged physical target, never a simulation guarantee | Accepted |
| ADR-014 | User explicitly selected Zynq7020/constrain over screenshots | Accepted; 33 MHz/N18 documented, conflicting screenshot superseded |
| ADR-015 | Integer fractional master phase clock; parallel shadow/active register banks | Local implementation decision; all channels coherent, no partial copy window |
| ADR-016 | Requested and calibration values plus enable mask committed together | Local implementation decision; supports sparse P0/P1 arrays without remapping lower IDs |
| ADR-017 | 32 lanes, four used outputs/package, 132 MHz core/66 MHz shift clock | **Candidate only**, simulated; no physical clock/PCB freeze |
| ADR-018 | No guessed part, pin voltage, XDC or bitstream | Mandatory; blocks board-target synthesis pending exact part |
| ADR-019 | Full maps generated for STANDING_WAVE and FOCUS; other mode IDs reserved | VN1 scope; unsupported modes explicitly reject |

ADR-017 alternatives: one 128-bit chain would require >=1.31 Gbit/s; 16x8 needs >=81.92 MHz plus
overhead; 32x4 reduces bit-rate at cost of I/O/package count. The selected **simulation** candidate
does not authorize fabrication. Need confirmed IO bank voltage, clock generation, buffering and timing review.
