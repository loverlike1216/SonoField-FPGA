# AX7020 v5 safe organization contract — 2026-10-08

Source: direct user attachment e8213cac-ae60-4eee-bb3e-6461d16eaf66. User explicitly authorizes v5 AX7020; no artificial v4. Project SONOFIELD_FPGA, same repository/main/workspace. Current model record GPT-6.1 Sol High, user-declared.

Goal: independently runnable v5 digital/tool baseline before any historical archival, preserving original versions, protocols, algorithms, acceptance and evidence.

Scope: read-only audit, copy selected current v2 functional source/tests/tools/reference, adapt only v5 paths/version metadata/board gates, execute available Python/Icarus/XSim/offline C/AXI and Vivado2025.2 validation; freeze prior state with original hashes; low-risk archive copies/indexes; reconcile current state, checkpoints and GitHub.

Non-goals: hardware programming, DDR/PS initialization, serial/GPIO/driver/boot changes, new PCB design, physical levitation, final electrical acceptance, executing manufacturer downloaded code or copying unlicensed implementations. Hardware facts require manufacturer provenance and revision match; old Robei facts cannot become AX7020 facts.

Invariants:128channels/8bit,common timing,requested/calibration separation,atomic maps,packet/register/channel formats,safety,motion cadence;10mm/12mm pitch/100mm radiating-face gap adjustable90..115mm/origin at center. No threshold relaxation,skipped inherited tests,false-path waivers or fabricated PASS. Stable module names unchanged.

Inputs: current source HEAD, previous validated v2 core source/evidence, user-created empty v5, actual installed tools and public ALINX AX7020 documentation/reference. Generic or mismatched board preset is prohibited.

Validation: all inherited115Python tests plus complete waveform/calibration/motion and independent safety/AXI checks under Icarus/XSim; fresh v5-only sandbox with no old versions; native Vivado project/elaboration/OOC synthesis for a documented part; physical constraints/full-board timing/PS/bitstream separately blocked if revision/config missing. Compare source/canonical behavior hashes and exact test counts before/after archival.

Rollback: prior Git/source state and byte-hash inventories; copy before modifications, never overwrite untracked user files; historical directories remain in place. No reset--hard,clean-fdx,force push or important deletion. archive is frozen indexed history, excluded from default build/search.

Done when: v5's available gates pass independently, archive does not cause regression, histories unchanged, state/search scope clear, local/remote commit verified, limits explicit. If key baseline fails, stop archival, preserve failure and report exact blocker. No sub-agent delegation requested.
