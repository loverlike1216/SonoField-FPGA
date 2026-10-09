# Execution contract — v5 next stage

Goal: preserve verified digital behavior while formally adopting approved AD7606C-16; implement and validate current offline ADC, sensor, calibration, GUI, PS and three-board candidates; inspect present hardware nonintrusively.

Scope: new codex/v5-ad7606c16-nextstage-20261010 branch on PR3. No version upgrade, historical-body read, old sandbox access, board write or main merge. Protected source hashes are S0_PROTECTED_HASHES.json. Legacy B tests/goldens/thresholds and all prior evidence/submitted BOM remain immutable. Only explicit parameter plumbing, new C16 source/config, current documentation/governance and standalone new tests may change existing files; any such change receives before/after hashes and exact user-authority scope. Original test expectations never change.

Architecture/invariants:128TX/8RX, requested/calibration8bit separation, common clock, complete atomicmap/ACK,32×4 serializer,50Hz local motion,40kHz local carrier,12mm pitch/100mm nominal90–115mm gap, geometric-center origin; sparse geometry is not perTX calibration or physical particle tracking. One central8channel ADC, independent12V perarray and centralAX7020-only protected power. ThreeTMP117; humidity diagnostic only. Board XDC/Rev3/PS/DDR/ownership/physicalpower remain qualified separately.

Validation: fresh full pretest171+3696×4 and existing C/AXI/safety/equivalence; additive199-or-more tests; old full regressions; C16 independent two-tool negative/timing/mapping tests; Python/C temperature160maps/20480words, sparse10fits/5seeds/5starts/384holdouts, five realGUIcallback cases375frames; native2025.2 BD/XSA/source/reopen/STA/DRC/CDC; real compiler architecture inspection; history-absent freshclone/freshlockedvenv; privacy scan and defaulthistoryread exclusion; exact source/evidence/oldBOM preservation.

Evidence: actual exit codes/logs and hashes; failures retained, scope boundaries explicit. OS USB enumeration is not JTAG ID or real UART. Simulation is not cutoff/ADC/acoustic measurement. Missing native CAD means machine-readable contract and ERC_NOT_RUN.

Rollback: leave new stacked DraftPR unmerged; PR3 and main remain unchanged. Separate reviewed revert for accepted current branch changes, full regression; no reset-hard, clean, historyrewrite or forcepush. If future board test approved, its own image ownership/recovery and isolated-output proof are required before first write.

Done when all executable gates have real results, remaining physical/approval gates have bounded STOP records, docs/BOM/contracts/states/checkpoint match real facts, normalpush and stackedDraftPR verified. Candidate Quality Gate reported separately from realboard/wholeplatform.
