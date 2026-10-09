# SonoField-FPGA v5 pre-PCB candidate handoff

Goal: samev5 threePCB fullsystem offline preparation; user instruction and two
sketches actually read, originalcore preserved. Currentbranch is stacked on
unmergedmigrationPR1, not a new version or repository.

Changes: new hardwarecontract/pinmap/BOM, three-temperatureintegral, sparse
geometry/gauges, optionalC/UARTprotocol, dynamicGUI, failclosedPLsupervisor and
completeBRAM-to-core wrapper, real2025.2 platform scripts and regressions.

Evidence: v5/docs/pre_pcb/PRE_PCB_COMPLETE_REPORT.md and
v5/evidence/pre_pcb_20261009/FINAL_VERIFICATION.json. 171tests, twoindependent
clones full3696×4, final375GUIframes/20480channelwords/10fits/newtop37×2 pass;
PS6windows/5IRQs;132MHz PL OOC WNS+.081/WHS+.096ns. Original112protectedassets
audited. Rawfailures and corrected gates qualified separately.

Failures/limitations: earlier automaticBDaddress warnings and queueSTOP
integration fixed and rerun. Vitis OSexit0 includes targetblockedtraceback;
no actual ARMtarget/BSP/UART, sensors/ADC, boardtiming/power/cutoff or acoustics.
DRC22reportedwarnings includes20entrycap, not boardacceptance. NativeERC_NOT_RUN.

Candidate ACCEPT WITH LIMITATIONS; wholeplatform REVISE, PCBNOT_RELEASED.
13opengateitems and twoOPEN Problems retained. No fakeChatGPTreview; records
PARTIAL and chathistoryBLOCKED. CurrentCP006 contains corrected stateconflict.
Publish normaldevelopmentbranch, verify remote/CI receipt, stop for review.
Rollback beforemerge uses retainedmigrationbranchd7f; afterapprovedmerge normal
revert+regression, neverforce/historyrewrite. Oldphysicalcopy remains intact.
