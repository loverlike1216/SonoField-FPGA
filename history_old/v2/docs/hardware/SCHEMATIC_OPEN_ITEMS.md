# Open schematic and hardware gates

| Gate | Status / evidence |
|---|---|
| B01 exact FPGA ordering code | BLOCKED; family alone is insufficient |
| B03 connector/VCCO | BLOCKED; internal constrain-file ambiguity persists |
| B04 serializer timing | OPEN; P-20260925-001, worst-case hold margin not closed |
| B05 physical TX/load/levitation | NOT_VERIFIED; no measurement evidence |
| B06 purchased 10 mm part | MPN and batch qualification pending; no 16 mm-rating reuse |
| B07 timing/phase reference | RX recovery/ADC timing and phase reference need hardware evidence |
| Clock-loss safety | Independent watchdog/power qualification decision pending |
| TCT library | Generic symbol template; exact device and footprint NOT qualified |
| Passive BOM/library | Value/rating shown; final MPN/package standardization required |
| Native whole schematic | DRAFT_CAPTURE_VALIDATED; one sheet,1561components,3992pins and1338independent mapping checks pass |
| ERC | Actual strict check:0fatal/0error/45warnings; see PCB/V1/log/review/ERC_DISPOSITION.md |
| Independent review | External ChatGPT history inaccessible; user review pending |

Next physical items: purchased TCT40-10T/R samples with traceable supplier data,
oscilloscope and current-limited supply, receiver fixture, actual board identification
and VCCO/connector documentation. Do not manufacture the final array before these gates.
