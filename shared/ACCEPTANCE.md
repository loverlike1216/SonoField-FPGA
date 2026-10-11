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


## PCB-S2 review boundary

Review artifact/calculation/baseline checks PASS in their stated scope. Circuit decision REVISE; S2-C BLOCKED; native schematic NOT_CREATED/ERC NOT_RUN/hardware NOT_VERIFIED. Neither1203arithmetic nor offline digitalPASS releases BOM/manufacturing. No acceptance threshold,35dB/test/golden/protocol was changed. External review remains required.

## PCB-S3 candidate acceptance

PCB-S3 user-authorized candidate delivered on feat/v5-pcb-design / PR6,base23f8d4c;soleactivev5. Central5V3A USB-C,candidate12.343Wsteadyinput envelope;upper/lower each12V3A36W GST36E12,candidate29.360Wsteadyinput envelope. Theseare limitdefined conditionaldesignbounds,not measuredload/allfaultguarantees. TPS3851one/array,two total;additionalwindow/thermal/latch/cutoff. Strict2126component/6390pin candidate,1541RCL,128TXmapping/8RX/64ADCpins. Fresh243tests,45staticchecks,256booleanstates,485cachedformulas/252numericcrosschecksPASS;S2fullframes inherited,not rerun. NativeNOT_CREATED/ERCNOT_RUN/hardwareNOT_VERIFIED. G1native/independent,G2powerfaultthermal,G3AFEandpoweroff,G4digitalintegration,VCCO,STA,BRAM,G5mechanical/SKUs. Manufacturing/procurement/boardwrite/main HOLD. ExternalChatGPT BLOCKED. See CP-20261011-003 and review11.

Artifactdelivery ACCEPT WITH LIMITATIONS;wholeplatform REVISE. Staticnetlistchecks areALTERNATIVE_VALIDATION,notnativeERC orfinalQualityGate. No thresholds orgoldens relaxed.
