# CP-20261011-001 — v5 hardware design recovery

Current identity: SONOFIELD_FPGA, same official SonoField-FPGA repository and
E:\Codex_project\AMD_Sonofield, codex/v5-hardware-design-20261011, v5 ACTIVE.
Base618b6f1; validated source6ba6314; containing checkpoint commit resolves with
`git log -1 --format=%H -- shared/CONTEXT_CHECKPOINT.json`. No circular SHA invented.

Goal: manufacturing-preparation candidate for one central/two symmetric arrays;
whole physical system is REVISE, scoped offline candidate ACCEPT WITH LIMITATIONS.
Architecture:128TX8RX, C16,3TMP117; independentUSB-C central/independent12V arrays,
AX7020headerpowerNC, fixedgeometry, sharedI2C63GPIO candidate. ADR042 supersedes
older centralheaderpower/50mg active-target wording, retaining original artifacts.

Completed:243current+243clean tests,3696frames x3Icarus+1XSim full digital gate,
C16/temp/sparse/GUI/C/AXI/safety/equivalence;68nativepackage/80manual pins,
404BOMformula rows and12byteequal generated files. No current boardprogram or
hardware acceptance. Previous OOC/ARMlinked safe-status evidence retains its scope.

Plan position:Gate0-7 offline artifacts and available checks complete; nativeCAD,
electrical/physical gates remain HOLD. Next verify publication receipt and CI,
connect real EasyEDA/libraries, complete63GPIO runtime wrapper and independent
safety circuit, resolve BRAM Problem, measure power/AFE/ADC/sensors and qualified
board platform/SDrecovery before real control/acoustic tests.

Active decisions:ADR035-041 in scope and current actual-user ADR042. Open Problems
P-20261008-001/P-20261009-001/P-20261010-001; do not invent ChatGPT Decision or
automatically cross hardware assumptions. Critical design gaps and PC-B01..13
current meanings are in BLOCKERS and v5/docs/hardware/RISKS.md.

Latest validation: v5/evidence/hardware_design_20261011/FINAL_VERIFICATION.json,
digital_full_retry2/summary.json, clean_clone/REPRODUCTION.json,
CONTRACT_VALIDATION_portable.json, PRESERVATION_final.json and FILE_HASHES.json.
This round clean clone reran243unit/contract/generation/package, not full digital;
current clone reran full digital. Same Windows/EDA, not independent hardware.

Do not change:originalRTL/firmware/tests/goldens/35dB/oldBOM/evidence; solev5;
no historybody/oldworkspace reads, forcepush, unknownimage writes or productionXDC.
Invariants:commonclock/atomiccomplete maps/separate8bitrequestedcal/signedcaptureACK,
32lanesx4/50Hz/12mm/90-115gap/origin and fail-off/manualrearm requirements.

Delta:four-source direction andEPS2-5mm target adopted, new101typeBOM/newmodels40tests,
new80contact review/nativepackageDB, realEasyEDA0window result and retained failures.
Conflicts:V2filename/internalREV1.0 vsV3 usercompatibility; UARTGM vspriorOSN;
SDbackup intention has no image/hash. Keep unknowns explicit. User sync permission
is granted; unresolved technical gates prevent main promotion/manufacturing.

Resume:read current shared state/plan/decisions/acceptance and hardware docs/evidence;
verify liveGit remote/PR chain before action. Never fall back to frozen source.
Provenance:actual user instructionSHA8b1fdbfe...; source manifests, native tool logs,
unit/simulation reports, independent clean clone, before/after hashes and Git metadata.

See hardware FINAL_REPORT, FAILURE_REGISTER and publication receipt.
