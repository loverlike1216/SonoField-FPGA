# Schematic execution contract — 2026-09-25

Project SONOFIELD_FPGA, active project v2, schematic revision V1, main.
Starting commit bad4f665889b12f8b75245d9513ae3919fa0cca3.
Authority: user instruction `AI-interaction-memory/codex/instructions/v2_schematic_revision_V1.md`.

Goal: produce an editable JLCEDA Pro schematic and auditable electrical design for
128 TX, 8 RX and AD7606B acquisition. Native capture, library pin audit, ERC and
save/reopen are separate gates; documents alone do not pass native capture.

Allowed changes: PCB/V1/{project,log,device}, v2 hardware documentation and
support scripts, shared state, sanitized interaction records, commit/push main.
This is the user-authorized exception to the normal v2-only engineering layout.
No PCB layout, fabrication files, purchases, new project version or v1 changes.
No guessed FPGA pin/package/VCCO, supplier identifiers or physical results.

Inputs: existing v2 RTL/interface contract, user BOM, Zynq7020 constrain precedence,
new instruction and primary manufacturer documents. External ChatGPT is inaccessible.
Required independent checks: generated connectivity against RTL/channel mappings,
datasheet pins against actual library pins, native ERC, exported connectivity,
power/safety/AFE/timing review and native save/reopen. Mark every unrun gate.

Rollback: retain existing Git history and starting commit; remove only newly created
project-specific working artifacts if necessary. Never delete unrelated EDA projects.
Done when the instruction's native schematic and evidence gates pass, or a concrete
blocker prevents dependent work and the maximum honest design package is saved.
