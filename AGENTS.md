# SonoField-FPGA execution rules

Scope: SONOFIELD_FPGA, VN1, repository loverlike1216/SonoField-FPGA,
workspace E:\Codex-project\AMD-SonoField-FPGA, branch main.

Read README and shared state/plan/decisions/acceptance/blockers before changes.
Preserve the user's supplied Zynq7020 directory. It is authoritative board evidence,
not a verified schematic, and contains conflicting pin and clock information.
Do not guess a part, board clock, package pin, bank voltage or IO standard.
No board implementation/bitstream until these facts are resolved.
Use Vivado 2025.2 as authoritative EDA; distinguish simulation from synthesis and hardware.
No direct FPGA-to-transducer drive. No physical levitation claim without measurements.
Keep requested phase and calibration distinct; complete maps commit atomically.
Update plan before major work; baseline, test, save raw evidence, update state/handoff.
Never weaken tests to get PASS. Preserve user files and historical evidence.
Use meaningful VN1 commits. Inspect secrets/license/personal data before push.
No release, deployment or visibility changes without explicit user authorization.
Final independent acceptance remains external; internal state is READY_FOR_REVIEW,
BLOCKED or REVISE_REQUIRED. Follow the user's full project brief and global rules.
