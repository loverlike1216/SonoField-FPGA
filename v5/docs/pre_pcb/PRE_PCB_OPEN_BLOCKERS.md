# Pre-PCB open blockers

Whole hardware platform: **REVISE**. Electrical/PCB/manufacturing: **NOT_RELEASED**.
No device was reset, halted, programmed or initialized in this task.

| ID | Missing fact or verification | Required closure |
|---|---|---|
| PC-B01 | Rev3 exact schematic, complete part grade, VCCO, UART/button/clock ownership | Revision-matched sources and approved nonintrusive measurements |
| PC-B02 | J10/J11 max/startup/spare power and protection/reverse current | Measured central budget with one source per rail; CENTRAL_POWER_BUDGET_BLOCKED |
| PC-B03 | NU40C10T original datasheet, C_eq(f,T,V), continuous/burst rating and actual consumption | Supplier authority plus impedance/current/thermal measurements |
| PC-B04 | Exact RX MPN, eight AFE delay/noise/gain/phase and mechanical positions | Datasheet, circuit and measured characterization |
| PC-B05 | Formal AD7606B effective analog bandwidth at ultrasonic carrier | Independent review; C-16 substitution requires actual user approval |
| PC-B06 | eFuse2A vs5A source, TVS clamp, fuse/wire, hotspot threshold, independent watchdog | Electrical review and physical fault/clock-stop/cable/unpowered tests |
| PC-B07 | Actual offchip timing, SI, CDC, inherited BRAM async reset and fullPS7 implementation | Min/max measured constraints and routed full-board DRC/CDC acceptance |
| PC-B08 | ARM compiler, Rev3 matched Vitis2025.2 BSP, linker, OCM, UART/I2C/IRQ adapter | Actual target build and independently approved bring-up |
| PC-B09 | Real ADC burst/coarseTOF bound/frontend delay/gauge and3sensor air bias | Raw measurements with timestamps/source/quality and independent calibration |
| PC-B10 | Sparse perTX amplitude/phase, acoustic side lobes, mass/trap and levitation range | Full-channel measurements and physical particle/force/temperature tests |
| PC-B11 | Native CAD/ERC, approved connector/harness and assembly constraints | Original schematic/layout/ERC/DFM review; no Gerber release now |
| PC-B12 | Independent reviewer and user final merge approval | Review concrete branch/evidence; never auto-merge main |
| PC-B13 | External ChatGPT full history reader unavailable | BLOCKED import status; do not invent ChatGPT review or decisions |

These are physical/deployment gates, not permission to skip offline regression.
No measured50mg or actual particle position, consumption, heat or calibration
result is claimed. Numerical board-temperature interpolation does not establish
true3D air temperature. Formal ADC unchanged; raw download throughput at115200
8N1 ideally11520B/s and16384B≥1.422s before framing/retry. Real carrier and50Hz
motion must be local PS/PL work after task upload; PC is not a40kHz scheduler.
