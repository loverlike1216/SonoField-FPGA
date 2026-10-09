# v2 bounded execution contract
Source: explicit user attachment deb51e17-1b72-4eab-ac76-9695ca9bda77, reinforced by latest single-board v2 priority.
Active v2; v3 paused and excluded. Work OFF. Starting commit b11c80ca3e7fc7745241c32f8f80d95329ca4ddf.
Goal: two substantive timing refactor rounds at 132/66 MHz, then quantified clock/throughput study if failing. Gate A is post-route WNS/WHS >=0 and TNS/THS=0 plus full regression.
Gate B: only after A and verified physical UART/PS facts, bare-board temporary JTAG safe transport loop. No guessed pins, external loads, permanent boot changes or PCB edits.
Allowed changes: phase/control timing implementation, verification, reproducible scripts, safe internal AXI leaf, evidence and explicitly named engineering-state/decision/blocker/acceptance/changelog files.
Stop: CORE_TIMING_REVISE with RCA if two rounds fail; otherwise complete gated real smoke or report route blocked. No secret third round.
Rollback: retain original source snapshots and prior Git history; do not erase failed reports. No physical state changed.
