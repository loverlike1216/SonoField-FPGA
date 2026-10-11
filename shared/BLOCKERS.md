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
