# PCB-A / PCB-B / PCB-C boundary — proposed, not fabrication-ready

## PCB-A digital expansion

Candidate 32 independent serial lanes, shared SHCP/STCP, active-high OE disable, ground returns and
external default-disable pulls. Physical connector pin numbers are **unassigned** pending board B01/B03.
Use one non-cascaded package per lane with four populated output channels. Buffer high-fanout clocks;
characterize aggregate capacitance, impedance, series termination, skew, ringing and setup/hold at the
farthest package. No random jumpers or long ribbon clock chain should be treated as timing-verified.

Nexperia [74AHC/AHCT595 datasheet, Rev.9](https://assets.nexperia.com/documents/data-sheet/74AHC_AHCT595.pdf),
tables 5–7: AHCT supply 4.5–5.5 V, VIH minimum 2.0 V. Full-temperature guaranteed clock rate is 90 MHz
at that supply; the 66 MHz candidate has nominal frequency margin. Required 5 ns clock widths and
5 ns SHCP-to-STCP setup fit 7.576 ns half-period / 15.15 ns latch spacing before PCB skew.
This calculation does not verify signal integrity. AHC at 3.0–3.6 V guarantees only 40 MHz across
-40..125 C, so that operating corner is rejected. Never infer capability from typical 170 MHz headlines.

## PCB-B modular driver

Prefer 16 acoustic channels per replaceable module, up to eight modules. Logic enters a level/gate-driver
stage, then a separately reviewed MOSFET/bridge power stage, then the TCT40. No FPGA or shift-register
output directly drives a transducer. Candidate gate driver is Microchip
[TC4427A](https://www.microchip.com/en-us/product/TC4427A), a dual non-inverting MOSFET driver.
Its [datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/APID/ProductDocuments/DataSheets/TC4426A-TC4427A-TC4428A-1.5A-Dual-High-Speed-Power-MOSFET-Drivers-20001423.pdf)
specifies a 4.5–18 V supply range and 1.5 A peak class; neither number is a transducer continuous rating.
It is not by itself a bootstrapped high-side bridge controller. Select high-side drive, dead time,
shoot-through prevention and disable topology when the power stage is designed.

Every channel has test points TP_LOGIC, TP_GATE/DRIVER and TP_TX_PLUS/TP_TX_MINUS. Differential
transducer voltage must be measured with suitable probes; do not short a bridge node with a grounded probe.
Provide module current limiting/fusing, local decoupling, thermal access, power-enable interlock and clear
signal/power return paths. Disabled state must remove AC drive and avoid sustained DC bias on the piezo.
No bridge PCB or 128-channel component values are frozen in VN1.

## PCB-C carrier

Mechanically locate and label UPPER_TX_00..63 and LOWER_TX_00..63; preserve these across calibration,
CSV maps, tests and driver connectors. Simulation pitch 18 mm is provisional. Measure body diameter,
pin separation, height, tolerance and effective polarity before designing holes or curved carriers.
`evidence/model/vn1/channel_mapping.csv` specifies logical identities, not board/header pin assignments.

## Proposed topology decision

The 32-lane scheme trades more FPGA I/O and half-used 595 packages for a feasible serial bit-rate.
It uses 35 signal nets before host/debug/control additions (32 data + shift + latch + OE).
GPIO availability is only a candidate pool until exact part, bank supply and connector facts are resolved.
P0 can bypass expansion through a reviewed two-channel interface, still using the same FPGA phase engine.
Do not fabricate PCB-A/B/C from this document; schematic review and measured load data precede fabrication.
