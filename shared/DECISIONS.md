# Current engineering decisions — v1

Project SONOFIELD_FPGA. These are user-approved requirements or identified local implementation choices,
not invented external ChatGPT decisions. Chat Source SonoField-FPGA is inaccessible; source message IDs UNKNOWN.
Prior provenance is retained in Git history. Current references below use repository-root paths.

| ID | Current decision | Source / validation consequence |
|---|---|---|
| ADR-001 | Robei Zynq-7020 controller; exact part unresolved | User project brief; B01 |
| ADR-002 | Vivado 2025.2 authoritative | User brief; simulation and synthesis distinguished |
| ADR-003 | User-selected nominal 10 mm / 40 kHz transmitter | User supplier image; exact electrical ratings unresolved |
| ADR-004 | 40 kHz common carrier | User brief; waveform reference |
| ADR-005 | 128-channel capable digital design | User brief; multi-size regression |
| ADR-006 | Opposed standing waves and geometric focusing | User brief; model estimates only |
| ADR-009 | 8-bit requested and independent calibration phase | User brief; RTL/oracle tests |
| ADR-011 | Complete-map atomic commit at period boundary | User brief; completeness and pending-write tests |
| ADR-012 | Host solver first | User brief; advanced field solver outside scope |
| ADR-013 | 50 mg is staged physical target | User brief; no simulated force guarantee |
| ADR-014 | Zynq7020/constrain prevails over conflicting screenshots | Explicit user reply; documented N18 / 33 MHz, remaining malformed entries open |
| ADR-015 | Shared fractional phase timebase, shadow/active registers | Local implementation; deterministic trace checks |
| ADR-016 | Requested/calibration/mask committed together | Local implementation; no partial-array map |
| ADR-017 | Candidate 32 serial lanes / four used outputs, 132 MHz core | Simulated candidate only; B04 electrical review required |
| ADR-018 | No guessed part, voltage, XDC or bitstream | Mandatory board evidence gate |
| ADR-019 | STANDING_WAVE and FOCUS implemented | Other modes reject; no fake results |
| ADR-021 | Opposed planar 8x8 + 8x8 at 12 mm pitch | Explicit user geometry instruction |
| ADR-022 | Coordinates at radiating-face centers, origin at pair center | Explicit user instruction; exact-grid tests |
| ADR-023 | Face gap 100 mm, adjustable 90–115 mm, z=+/-g/2 | Explicit user instruction; range and phase tests |
| ADR-024 | Regenerate phase maps for measured face gap | Geometry propagation model and cross-validation |
| ADR-025 | Single active v1 directory, root cross-version governance | Current user organization instruction; same version, no v2 |
| ADR-026 | Delete obsolete version records from current tree after integrity passes | Current user follow-up; Git history retained, fresh evidence required |
| ADR-027 | Chat source SonoField-FPGA; blocked access is explicit | Current user reply + actual tool catalog inspection |

For ADR-025/026 approval: Approved By User; source is the current Codex conversation, message ID/time UNKNOWN.
Date of engineering record: 2026-09-19. Base commit: ada1b2062756a2b852ed643a6eaa04fdc746323b.
Consequences: root/v1 path regression, full simulation and clean reproduction required. No hardware scope changes.
Open hardware questions: AI-problem/problem/P-20260919-001 through 003. No external answers received.

## ADR-028 — observable Codex interaction memory (2026-09-20, v1)
Source: user's current revised rules and explicit request, captured in AI-interaction-memory/codex/.
Adopt canonical sanitized transcript, source-ID/hash/cutoff provenance and curated tool flows at checkpoints.
Do not export hidden/private provider instructions or reconstruct unavailable history. PARTIAL stays PARTIAL.
No new version and no change to FPGA/acoustic design. Validation: exporter tests + source integrity audit.
Quoted historical instructions may retain old labels; active engineering layout remains v1 only.
External ChatGPT access remains blocked; no decision is attributed to it.

## ADR-029 — VERSION_UPGRADE_APPROVED (2026-09-21)

From v1 to v2. Approved By: User. Approval Source: AI-interaction-memory/codex/instructions/v2_formal_development.md, sections 1 and 75.
Freeze v1 unchanged at 487210d1a2b157bca52d1722c2343b50851a3578; complete reusable project copied to standalone v2.
Only bootstrap/inherited baseline in this stage. No v3, PCB fabrication or calibration implementation now.
External ChatGPT decision is not claimed. Freeze hashes: shared/versions/v1_freeze.json.

## ADR-030 — v2 bootstrap evidence boundary (2026-09-21)

Version: v2. Source: direct user formal instruction, section 75.
Complete inherited baseline verified at e353c16d35da2b430f46ba5b83a5a9a79dd749b7. Fresh clone excludes v1 directory; parent Git tree unchanged.
New BOM is PCB_PROPOSED input. Obsolete workbook version cell has no authority over explicit v2 approval.
No calibration/ADC capability or external ChatGPT decision claimed. Stop before deeper stages.


## ADR-031 — authorized v2 software/digital stage (2026-09-21)

Version v2; source direct user instruction v2_self_calibration.md, sections 70/71. This supersedes
ADR-029/030's bootstrap-only execution boundary for the new stage, not their historical results.
Implement the complete raw ADC to geometry/frequency/phase/LUT pipeline and PL acquisition. Keep
v1 frozen; no v3, PCB files, purchases, force push or physical claims. Source checkpoint begins
at 5fa046d0ad3dd7fe0c44824b74b71f974f9a09bc. No external ChatGPT decision was imported.

## ADR-032 — ADC and phase-reference contracts (2026-09-21)

Version v2; source user requirements plus AD7606B Rev B protocol and actual simulations.
Use software-mode four DOUT, 32 clocks/frame, +/-5 V for the 2.5 V biased AFE, explicit config/range
readback and no CRC/status/OS header. Configuration/source mapping is checked, not guessed.
Shared simulated 132 MHz clock; target PLL/VCCO/IO timing remains blocked. Register bus is a
board-independent transport boundary. Bounded 16 KiB BRAM-style capture, host ACK before reuse.
Keep per-bank phase gauge explicit: two simulated RX anchors enable a synthetic full map, while
real RX reference measurement remains required. Reject active invalid channels or unreferenced
whole-array LUTs. Coarse/fine refinement records its fitted-chain dependence and coarse baseline.
Evidence: v2/evidence/self_calibration_stage/validation. No hardware freeze authorized.

## ADR-033 — authorized schematic-only stage (2026-09-25)

Source: direct user instruction v2_schematic_revision_V1.md. Project stays v2;
schematic revision V1 uses root PCB/V1 as an explicit layout exception. Native
JLCEDA Pro capture and electrical review are authorized; PCB layout, manufacturing,
hardware freeze and physical acceptance are not. Prior software results stay historical.
Start: bad4f665889b12f8b75245d9513ae3919fa0cca3. B01/B03/B04/B05/B06/B07 remain open.
No external ChatGPT decision is claimed. Execute the preflight contract; preserve v1.

## ADR-034 — Single-sheet presentation and pwsh preference (2026-09-26)
Source: user's actual Codex instructions requesting a single schematic with solid named partitions and Windows PowerShell7 by default. Project remains v2; schematic remains V1. Preserve all128TX and8RX circuits; re-layout only into one native sheet. All3992 native pins unchanged after presentation adjustments. PDF/SVG are vector reading artifacts. No scope expansion to PCB or safety-gate waiver. Long-term shell preference saved separately in the authorized memory update note.
