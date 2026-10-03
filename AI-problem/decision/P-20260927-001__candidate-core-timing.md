---
problem_id: P-20260927-001
problem_hash: 0bf40cdd79faaf5fd4aca4af6e1f7cf85eab8662128f4633ea1acb3b4ef61916
active_version: v2
revalidated_commit: b11c80ca3e7fc7745241c32f8f80d95329ca4ddf
status: USER_APPROVED
source: User attachment deb51e17-1b72-4eab-ac76-9695ca9bda77 sections 0/2/13
---

# APPROVE_LIMITED_TIMING_REFACTOR_IN_V2

User explicitly approves xc7z020clg400-1 as CONSERVATIVE_ENGINEERING_ASSUMPTION for timing and gated bare-board smoke tests. Physical XC7Z020/CLG400 is confirmed, speed/temperature/full order code remain UNKNOWN. B01 is not closed.

Retain 132 MHz core / 66 MHz shift first. At most two substantial timing refactor rounds before a quantified throughput/MMCM clock trade study. Preserve register/packet/channel/map/calibration/motion semantics; document and independently test any common pipeline latency. No faster-part guessing, unjustified exceptions, arbitrary clock reduction, test weakening, external GPIO, PCB or v3 work.

Gate A requires post-route WNS/WHS >=0 and TNS/THS=0, full functional regression. Gate B may follow only with verified PS/UART route and a safe top exposing no acoustic outputs. Missing UART routing blocks real transmission/deployment. Temporary JTAG only; no boot-media change.

The problem body hash and original source path were revalidated. This decision is persisted by Codex under the user's explicit current request, not attributed to Work or an unobserved Chat review.
