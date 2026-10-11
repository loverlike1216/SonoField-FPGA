# Current v5 PCB-S3 plan

PCB-S3 user-authorized candidate delivered on feat/v5-pcb-design / PR6,base23f8d4c;soleactivev5. Central5V3A USB-C,candidate12.343Wsteadyinput envelope;upper/lower each12V3A36W GST36E12,candidate29.360Wsteadyinput envelope. Theseare limitdefined conditionaldesignbounds,not measuredload/allfaultguarantees. TPS3851one/array,two total;additionalwindow/thermal/latch/cutoff. Strict2126component/6390pin candidate,1541RCL,128TXmapping/8RX/64ADCpins. Fresh243tests,45staticchecks,256booleanstates,485cachedformulas/252numericcrosschecksPASS;S2fullframes inherited,not rerun. NativeNOT_CREATED/ERCNOT_RUN/hardwareNOT_VERIFIED. G1native/independent,G2powerfaultthermal,G3AFEandpoweroff,G4digitalintegration,VCCO,STA,BRAM,G5mechanical/SKUs. Manufacturing/procurement/boardwrite/main HOLD. ExternalChatGPT BLOCKED. See CP-20261011-003 and review11.

Next: complete normalDraftPR6publication and verifyCI/remote;then independentreview/nativeCAD/electricalqualification/actualdigitaltaskhandoff. Do not reopenadapternominal choice or rerun low-value simulation without new digitalchanges. No version upgrade.

## Earlier stages — provenance only

# Current v5 hardware plan

Gate0 reconciliation/sourceaudit COMPLETE; Gate1 formal direction/geometry COMPLETE;
Gate2 powermodel/fail-off requirements COMPLETE_CANDIDATE_CONTINUOUSPOWER_HOLD;
Gate3 IOmanual/nativepackage COMPLETE_PROPOSED_WRAPPER_EXTERNALTIMING_HOLD;
Gate4 BOM/criticalpin/connections COMPLETE_REVIEW_CONTRACT_NOT_NATIVE_NETLIST;
Gate5 nativeCAD NOT_CREATED/ERC NOT_RUN; realEasyEDA0windows;
Gate6 full current digital243/3696x4/C16/temp/sparse/GUI PASS; clean243/12bytes/package PASS;
Gate7 evidence/state/checkpoint ready, normalGitHub sync authorized. ManufacturingHOLD.

Current source6ba6314, basePR4 618b6f1; no versionupgrade. Same branch/repository.
After publication verify receipt/remoteCI and deliver. Do not restart low-value
optimization. Next meaningful work requires actual nativeCAD/electrical inputs,
complete63GPIO wrapper/safety circuits and BRAM reset review, then qualified hardware.
See v5/docs/hardware/MISSING_FACTS_AND_NEXT_MEASUREMENTS.md and RISKS.md.
Main remains unpromoted due engineering gaps; routine publication needs no new approval.

Publication: DraftPR5 https://github.com/loverlike1216/SonoField-FPGA/pull/5; evidence commit 09201d34d15b21c4956f2d2377cc4daea33b1f71; push+PR CI success;417remote SHA256 checked;main unchanged. Receipt:shared/hardware_design/PUBLICATION_RECEIPT.json.


## PCB-S2 candidate workstream (current on feat/v5-pcb-design)

S2-A evidence/reconciliation DELIVERED. S2-B power/driver/safety proposal REVISE. S2-C fullRCL freeze BLOCKED. Fresh243/full digital gates PASS. Retain parent hardware stage above as provenance; no main promotion. Next: main-chat independent review of P-20261011-001; approve concrete safety/progress/regulation scope and supply electrical facts; then native circuit review, S2-C and future BOM candidate. See CP-20261011-002 and v5/hardware/pcb/PCB_PROJECT_STATE.json.
