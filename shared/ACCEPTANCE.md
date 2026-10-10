# UART continuation amendment — 2026-10-10

Current result: offline ACCEPT WITH LIMITATIONS; real-board/whole-platform REVISE.
COM3 now Code0 with driver11.6.0.420; pyserial3.5 locked. New read-only SLCR check
kept both CPUs Running, originalVivado retained; no UARTopen/TX/boardwrite.
Actual2025.2nativeSDT/BSP+ArmGNU13.2 linked safe/status ARMELF and OCM audit PASS
in current/newcleanclone;203+203tests PASS. FullELF is not claimed bit-exact;
application .text matches. Vitis platformAPI missingQEMU failure and RWX warning
remain. Prior1160sealedfiles and original criteria preserved.
User correction: recovery files are remote references only, no local verified
backup. Rev3 DTR/RTS A0 and image/platform/recovery/isolation/permission A2 gates
remain open. PC-B08 logicalbuild subgate closed; physical13PC-B scopes/BRAMProblem
and independentreview stay open. Samev5/mainunmerged/Draft4 update authorized.
See v5/docs/uart_resume/RESULT.md, v5/evidence/uart_resume/20261010_01/FINAL_VERIFICATION.json,
CP-20261010-002 and shared/uart_resume/PUBLICATION_RECEIPT.json. Prior snapshots
below retain provenance; this amendment supersedes only their stale current facts.

---

# 2026-10-10 current next-stage acceptance amendment

Actual user approval supersedes older B-formal/pending-C16 wording below: formal direction AD7606C-16; electrical/ordering/analog gates remain HOLD. No other inherited criterion is lowered. Required original171+new32=203, original3696frames×3Icarus+1XSim and canonicalhash equality, allC/AXI/safety/calibration/equivalence; newC16two-tool signed/timing/readback/fault/full1024capture/ACK/actualtop; temperature160maps20480words,10sparsefits5seeds5starts384holdouts,5dynamicGUIcases375frames; native2025.2 source/BD/XSA/reopen/STA/DRC/CDC; actualARMtargetarchitecture; history-absentclone/freshlockedvenv/rawS0/filehash audit. Current and clean203PASS; fullafterinitialdiscovery199 plus four later contract tests separately executed. Exact source/report/functional hashes and EOL policy are recorded, not assumed.

Preserve35dBtranslation<.1mm/angle<.1deg/f0RMSE<80Hz/phaseRMSE<2deg, all tests/goldens/thresholds, signedcapture/commonclock/atomicmaps/ownership/safety/protocol. No skip/mock-hardware/waiver to obtainPASS. DRC346REQP-1839+1ZPS7-1 and161in/148outmissingdelays block board release. CortexA9object is not linked BSPapplication. RealUART100/1000, ADC/AFE/TMP117/powercutoff/acoustics/particle/nativeERC remain NOT_RUN or BLOCKED.

Scoped candidate **ACCEPT WITH LIMITATIONS**; real-board and whole-platform **REVISE**. No final independent/hardware certification. Open13PC-Bgates+P-20261010-001; externalChatGPTBLOCKED. Main merge/production release requires actual user review/approval. Evidence: v5/evidence/next_stage/20261010/FINAL_VERIFICATION.json and docs/next_stage/FINAL_REPORT.md. Prior candidate records below are provenance; their old ADCdirection and stage statements are superseded only by this actual current amendment.

---

# Current v5 acceptance

Migration scope preserves all inherited technical criteria. Required: MIG01–12 exact archive blob/mode/rawSHA256; private original protection; v5-only load/search; current facts;171/171Python (original115 + new56) and3696frames×3Icarus+1XSim; canonical trajectory/map/trap/ACK equality; all protocol/C/AXI/calibration/safety/serializer/golden gates; native Vivado2025.2 OOC/reopen/loaded source proof; second clean clone with new locked venv and full offline gates; consistent current docs and hardware no-operation boundary. Results: shared/migration/PORTABILITY_AND_REGRESSION.md.

Keep calibration35dB thresholds: translation norm<0.1mm, angle norm<0.1deg, f0RMSE<80Hz, phaseRMSE<2deg. Keep lower-SNR failed/rejected records; never weaken thresholds. Signed1024×8 capture, two-bank reference constraints, full-map atomic commit/ACK/no overwrite, safety/timeout/error behavior and protocol/registers remain fixed. Canonical functional hashes ignore only explicitly nonfunctional timestamps/absolute-report headers. Formal ADC remains AD7606BBSTZ-RL; candidates require separate decision/approval.

Candidate-only scope may be ACCEPT WITH LIMITATIONS after all executable migration gates. Formal migration requires user-approved merge and post-merge fresh remote clone; before that no claim main is migrated. Physical whole-platform remains REVISE: no full-board routed timing/XDC/PS platform/ARM BSP/realUART+AXI/ADC+driver/AFE/safety/electrical/thermal/trap/particle evidence. Historical read-only identification and OOC do not close physical gates. Native v5 schematic NOT_CREATED/ERC_NOT_RUN; electrical/manufacturing HOLD. Independent review remains pending.

Current pre-PCB S0–S7 additive gate: every original115 test remains byte-identical
and executed; new56 bring171 total. Re-run3696frames×3Icarus+1XSim with original
canonical hashes, originalC/AXI/safety/calibration/equivalence. New supervisor/
mailbox fault tests require bothsimulators. Sparse≥5seeds/10fits/5starts,
translationnorm<.1mm/anglenorm<.1°, rank12/condition<1e5, independent holdout and
bad-data rejection. Python/C temperature maps must match bit-for-bit with
calibration bytes preserved. Five actual runtimeGUI inputs require savedSHA,
modeltrap/motion checks, actualCpacket/50Hztick and bothsimulators'ACK equality.
Centralpower/Rev3/IOtiming/ARMbuild remain explicitHOLD rather than guessed.
Freshindependentclone+lockedvenv must reproduce executable gates before S7
candidate delivery. Independentreview and user's main approval remain pending.


## 2026-10-09 final pre-PCB candidate evidence

All feasible offline gates PASS at the sources qualified by FINAL_VERIFICATION.
171tests; two-clone3696frames×4 with matchingcanonical hashes; new safety/top
two-tool PASS; five runtimeGUIcases375frames;160temperaturemaps/20480words;
ten sparsefits, rank12 and384holdouts each. Actual PS6windows/5IRQs, real2025.2
PL OOC WNS+.081/WHS+.096ns. No originaltest/golden/threshold changes.
Candidate conclusion ACCEPT WITH LIMITATIONS FOR REVIEW; wholeplatform REVISE.
13open gates, no physicalhardwareacceptance, no finalindependentreview claimed.
PCB/productionXDC/ARMtarget/electrical/manufacturing NOT_RELEASED or BLOCKED.


Current Historical project migration (ADR039): all6670sourcefiles unique disposition;3911rawSHA256/blob/mode-identical moves and2759kept; current171tests and allprePCB gates required. Actualsource lists/cleanhistory-absent clone required, not grep-only. Gate7 is a separate post-user-approval action. See current cleanup evidence, do not rewrite older result sections.


Historical-isolationcandidateGates0–5PASS: fresh171before/after,3696×4exactcanonicalhashes,fullprePCBextra,three nativeOOC/reopens andhistory-absentnewvenv. CandidateACCEPTWITHLIMITATIONS;Gate6receiptpending;Gate7userapprovalrequired;wholeplatformREVISE.
