# CLG400 pin audit

Vivado 2025.2: 400 package balls, PL user IO {'35': 50, '34': 50, '13': 25} (125 total).
AMD UG865 v1.9 page 22 independently states bank 33 absent, bank 13 partial, PS banks fully bonded.
Source: https://docs.amd.com/v/u/en-US/ug865-Zynq-7000-Pkg-Pinout
No bank 33 PL pin exists in this package database. Bank 13 provides 25 PL user IO, banks 34/35 each 50.
PS banks 500/501/502 are present. This proves bonding, not board routing or voltage.

Audited 101 primary .const claims and 346 total source claims including secondary images.
Each JSON row records signal, connector/number where known, ball, bank, availability, source and confidence.
No generated XDC is accepted. All board-route and VCCO evidence remains unverified.

Critical finding: hardware.const HDMI CEC J5 is PS_DDR_BA2_502, not a PL IO.
Secondary J15 is a legal bank35 PL IO, but this does NOT establish board routing or authorize replacement.
J3/J4/J5/J6 numbering differences, J4 Pin1 H15 versus F19, duplicated J4 Pin6 D18/E18,
missing V16/J6 number and image Y16/V16 disagreement are all retained in constraint_conflicts.json.
User-selected .const precedence resolves source priority only; it cannot make an illegal pin legal.
N18 is IO_L13P_T2_MRCC_34, clock-capable; documented 33 MHz is not a measurement.
Bank33/CLG484 assumptions are prohibited; bank13 cannot be budgeted as 50 pins.
Unnumbered layout positions are intentionally not converted to connector pin numbers.
