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
