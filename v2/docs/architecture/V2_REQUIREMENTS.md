# Approved v2 roadmap, not implemented capabilities

Authoritative full instruction is archived in root AI-interaction-memory/codex/instructions.
This stage implements only bootstrap and inherited baseline. Future scope:

- Two planar boards, each 64 TCT40-10T and four TCT40-10R; RX corners proposed at (+/-54,+/-54) mm.
- TX radiating-face centers unchanged at 12 mm pitch; nominal faces z=+/-50 mm, gap 90..115 mm.
- 512 directed opposite-board TX/RX paths; receiver paths stay separate.
- PL deterministic burst/blank/capture, AD7606B acquisition, timestamps and safety.
- PS/host coarse TOF plus carrier phase, ambiguity/confidence checks, robust relative 6DoF fitting,
  environmental sound speed using remote SHT45, resonance sweep and one common f_work.
- Per-channel requested and calibration phase remain distinct; amplitude is health/weight/mask
  unless real hardware amplitude control is later designed and validated.
- Two 130x130 mm proposed array PCBs, central ADC PCB, remote sensor PCB, star 15 V supply.
  TC4427A directly drives TX loads. No additional MOSFET stage is assumed by this v2 baseline.
- Per array: 16 595 lanes with Q0..Q3 used, buffered SRCLK/RCLK; physical timing unverified.
- Formal hardware stages: PH0 prototype concept, PH1 single TX/RX, PH2 4/16 TX, PH3 one board,
  PH4 dual-board pose independently measured, PH5 calibration, PH6 staged-mass levitation.

ADC/calibration software and RTL are NOT_IMPLEMENTED. No empty modules stand in for them.
Existing simulator safety coverage does not prove power-on/brownout/cable-loss/clock-loss safety.
Next stage requires bootstrap review. Full v2 acceptance is not this migration's acceptance.
