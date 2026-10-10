# Current v5 acceptance — 2026-10-11

Scoped offline hardware candidate ACCEPT WITH LIMITATIONS; wholeplatform REVISE.
Manufacturing/procurementHOLD. Formal actual-user ADR042 changes only power/I2C/
candidateIO andEPS2-5mm target; all core protocols/goldens/thresholds including35dB,
commonclock/atomicmaps/signedACK/50Hz/12mm/90-115geometry remain protected.

Required original203 plus40new tests=243; current243 and clean243PASS. Complete3696
frames x3Icarus+1XSim/C/AXI/safety/calibration/equivalence andC16 actualdigitaltop,
temperature160maps/20480words,10sparsefits384holdouts,5GUIcases375frames PASS.
80contacts/68nativepackage/63used5sparecandidate/8negativecases and404BOMformula
rows independently checked;12generatedassets byteequal in fresh clone.

Real safety circuit/63GPIO wrapper/Rev3VCCO/continuouspower/AFE/ADC/TMP117/PSruntime/
externalSTA/nativeCAD/ERC/independentreview/particle remain NOT_VERIFIED or HOLD.
346BRAM asynchronous warnings still OPEN; no waiver. Previous nativeBSPsafe-status
ELF exists but does not implement full motion/sensor runtime. No current UART/boardwrite.
Final evidence v5/evidence/hardware_design_20261011/FINAL_VERIFICATION.json.
