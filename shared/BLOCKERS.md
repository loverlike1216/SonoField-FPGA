# Current v5 blocker authority — 2026-10-10

This current table supersedes prior shared B-approval/state text; old Git snapshots remain provenance. Offline candidate gates have no unclosed test failures; physical release has the unresolved risks below. No hardware/main/manufacturing acceptance is claimed.

# Current unresolved gates and minimal closure

Device-direction approval is CLOSED: user approved C-16. Its analog/electrical qualification remains OPEN. Original PC-B01..13 IDs persist for continuity; current meaning below supersedes the old pre-PCB B-direction condition.

| Gate | Priority / owner | Minimum closure evidence | Current status |
|---|---|---|---|
| NS-UART / JTAG | P1 user + system/board operator | Official CP2102N driver restored, COM enumerated; actual JTAG adapter and existing safe server visible; then read-only identification | JTAG current read-only identification PASS; UART Code28/0COM remains BLOCKED; no install/write authorized |
| PC-B01 Rev3 | P0 user/vendor | Exact revision schematic/full part/VCCO/PSclock/UART/DDR and current image ownership | BLOCKED; generic2023.1 candidate only |
| PC-B02 central power | P0 electrical reviewer | Per-rail max/startup/fault budget and header capacity with single protected source/no backfeed | CENTRAL_POWER_BUDGET_BLOCKED |
| PC-B03 transducers | P1 supplier/bench operator | Exact T/R ordering codes, rated continuous/burst excitation, batch dimensions, impedance/current/thermal sweep | Images transcribed; bench NOT_RUN |
| PC-B04 RXAFE | P0 electrical/bench reviewer | Exact RX, AFE/protection/blank/gain/filter/noise/group-delay/40kHz measurements | HOLD |
| PC-B05 C-16 analog | P0 electrical/bench reviewer | Reference/supply/brownout/straps/highBW/anti-alias/phase/SNR and independent review | USER_DIRECTION_APPROVED; ELECTRICAL_HOLD |
| PC-B06 protection | P0 electrical reviewer | TVS/eFuse/fuse/wire/inrush/thermal coordination; NC estop/localwatchdog/coldrearm real cutoff injections | PROPOSED / SIMULATED_ONLY |
| PC-B07 BRAM/external timing | P0 independent RTL/electrical reviewer | Real decision for P-20261010-001; reset-at-capture proof; complete DRC/CDC; production pins/66MHzIOminmax/SI |346 inherited REQP-1839 plus1OOC PS warning; board timing HOLD |
| PC-B08 target application | P1 platform owner | Qualified XSA/BSP/linker/OCM/UART/I2C/IRQ and linked ARM ELF with logged success | Portable Cortex-A9 object PASS; BSP application BLOCKED |
| PC-B09 temperature/acquisition | P1 bench operator | Three timestamped actual sensor readings, ADC waveforms, coarseTOF/phase gauges and air bias | Digital synthetic / host fixture PASS; real NOT_RUN |
| PC-B10 acoustic/fullTX | P1 bench operator |128TX response/polarity/frequency/temperature, field maps and physical particle tests | UNMEASURED |
| PC-B11 nativeCAD/ERC | P1 CAD/electrical reviewer | Connected native EasyEDA project, every symbol/net/passive pin allocated, actual ERC warnings resolved | Network contract only; ERC_NOT_RUN; MANUFACTURING_HOLD |
| PC-B12 review/merge | P1 user + independent reviewer | Review concrete new stacked Draft PR and dependencies; explicit merge approval | PENDING; main untouched |
| PC-B13 externalChat | P2 user/tool environment | Real exported history or supported reader; genuine independent decisions | BLOCKED; no fabricated transcript/decision |

S5 real UART->PS->AXI->PL volatile test is NOT_RUN. A2's board facts, safe isolated outputs, known image/recovery and explicit reset/download/RAM-write approval must all be present before any write. No missing physical gate blocks safe offline implementation, regression, reports or Draft publication.

Rollback before merge: retain the new candidate branch and switch a separate clean checkout to PR3 baseb08ccf58. Never reset/clean the original sandbox. Revert C-16 adaptation only through a reviewed normal revert/decision; it must not silently withdraw the user's formal device choice. Current evidence and all failed logs remain preserved. No board state restoration action was needed because no hardware state was changed. If the user later approves an affected hardware test, its reviewed image must include a separate restore plan. Main merge and postmerge fresh-main regression remain deferred.


Current JTAG update after actual user reseat: After the actual user reseated JTAG, dedicated localhost3122 XSDB/Vivado2025.2 read-only identification PASS: xc7z020 ID0x23727093; both Cortex-A9 Running before/after; BOOT_MODE0x05, DDRC0x81/0x3e; PL DONE/EOS1, existing image identity UNKNOWN. Sysmon zero/-273.1 values INVALID, no voltage/temperature claim. Original Vivado GUI retained; owned server disconnected/stopped. CP2102N remains Code28/0COM. No halt/reset/init/download/memory/DDR-RAM/GPIO/driver/serial write. Real UART->PS->AXI->PL and A2 write gate remain STOP. Evidence: v5/evidence/next_stage/20261010/jtag_reseated/summary.json.
