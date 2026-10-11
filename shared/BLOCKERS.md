# Current v5 blockers — 2026-10-11

PC-B01 revision/platform:V3manual and oldinternalREV1.0schematic hash-reviewed,
user compatibility retained, actual VCCO/grade/DDR/UARTbridge still unqualified.
PC-B02 power:central independentUSB-C5V now official; headerpowerNC. CC3A,
minimumVBUS/AVCC, current/thermal/protection/load budget remain HOLD.
PC-B03 transducers:exactRX/continuousrating/impedance/motionalpower unknown.
PC-B04 AFE:8channelprotection/gain/filter/blank/phase/noise NOT_VERIFIED.
PC-B05 C16:formal direction approved; pin contract/digital PASS; analog/reference HOLD.
PC-B06 safety:powercutoff/NCestop/windowwatchdog/overtemp/rearm physical circuit HOLD.
PC-B07 timing/reset:346BRAMwarnings and P-20261010-001 OPEN; externalSTA/VCCO/63IO
runtimewrapper/RESET/SYNC/I2C/FAULT mapping unclosed. Review-onlyXDC cannot deploy.
PC-B08 application:native linkedsafe-statusBSP priorPASS; matchedfullPSruntime NOT_VERIFIED.
PC-B09 sensors:temperature/sparse synthetic PASS; actual3TMP117/ADC acquisition NOT_RUN.
PC-B10 acoustics:full128TX/calibration/field andEPS2-5mm NOT_RUN.
PC-B11 nativeCAD:realEasyEDA0connectedwindows; nativeNOT_CREATED/ERCNOT_RUN.
PC-B12 publication/review:userautonomousGitHubsyncAUTHORIZED; independentreview
pending and main qualitygate unmet, not a missing routine-push permission.
PC-B13 externalChat:readerBLOCKED, no fabricated source/Decision.

SDbackup:user intends backup but no localverifiedimage/hash/recoverytest. Board existing
image UNKNOWN. No boardreset/program/serialopen or realultrasound performed thisstage.
Detailed priorities/minimal closure: v5/docs/hardware/RISKS.md and
MISSING_FACTS_AND_NEXT_MEASUREMENTS.md. Current offline tests have no unresolved
failures; physical/integration gates remain. Do not weaken acceptance or read history.


## PCB-S2 P0 additions

S2-P01 window/progress coverage; S2-P02 cold-start/失电/锁存/physical cutoff/discharge; S2-P03 actual load and eFuse/TVS/source/jack/shunt coordination; S2-P04 centralAVCC/RX/AFE; S2-P05 fullIO/VCCO/externalSTA/BRAM. See v5/hardware/pcb/reviews/20261011_s2/08_RISK_BLOCKERS_AND_DECISION_REQUESTS.md. S2-C/BOM/manufacturing HOLD. These are current candidate facts, not main-merged implementation.

## PCB-S3 current five release gates

PCB-S3 user-authorized candidate delivered on feat/v5-pcb-design / PR6,base23f8d4c;soleactivev5. Central5V3A USB-C,candidate12.343Wsteadyinput envelope;upper/lower each12V3A36W GST36E12,candidate29.360Wsteadyinput envelope. Theseare limitdefined conditionaldesignbounds,not measuredload/allfaultguarantees. TPS3851one/array,two total;additionalwindow/thermal/latch/cutoff. Strict2126component/6390pin candidate,1541RCL,128TXmapping/8RX/64ADCpins. Fresh243tests,45staticchecks,256booleanstates,485cachedformulas/252numericcrosschecksPASS;S2fullframes inherited,not rerun. NativeNOT_CREATED/ERCNOT_RUN/hardwareNOT_VERIFIED. G1native/independent,G2powerfaultthermal,G3AFEandpoweroff,G4digitalintegration,VCCO,STA,BRAM,G5mechanical/SKUs. Manufacturing/procurement/boardwrite/main HOLD. ExternalChatGPT BLOCKED. See CP-20261011-003 and review11.

S2design-scope decision is now authorized by realuser;electrical/safety/implementation portions remainopen underS3G1-G5. See review11 forownersandclosureactions.
