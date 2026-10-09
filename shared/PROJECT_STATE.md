# Current v5 pre-PCB state

SONOFIELD_FPGA / feat/v5-prepcb-full-system / base d7f7b60ae8ed9ed8bdee34c8738ce68aacd81743. Sole active version v5.
Latest user continues S0–S7; migrationPR1 remains unmerged, main unchanged.
Execution sandbox E:\Codex_project\AMD_Sonofield; old physical sandbox/archive not read or modified.

S0 facts and original112-file byte lock; S1 threePCB/pin/power/BOM contracts
prepared as NON_DEPLOYABLE. S2 PL OOC route internal132MHzWNS+.068/WHS+.070,
no internal no_clock/unconstrained endpoints; externalIO161/147 and DRC holds.
New51 C/Python tests PASS; full inherited115+51/3696×4 running. S3–S6
temperature/sparse/C protocol/runtimeGUI integration in validation.
Target ARM/BSP and all physical hardware remain NOT_VERIFIED/BLOCKED.

Current instruction and evidence are linked in PROJECT_STATE.json. CP005
records in-progress state, not acceptance. Next: finish full gates and clean
clone, persist actual interactions, reconcile remote and push reviewed branch.
No v6, no main merge, no board operations. Whole platform REVISE.
