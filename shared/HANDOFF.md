# v1 interaction-memory handoff

## Goal / inputs
Apply user's added observable AI-interaction rules and persist real Codex messages locally/GitHub.
Preflight: 4ff3c38 main matched origin, v1 ACTIVE; shared/AI source/blockers and source session checked.

## Changes made
AI-interaction-memory now has a canonical sanitized Codex transcript, source-ID/time/hash manifest,
index, partial tool-call register, curated tool flow, reusable sync/check command and eight privacy/provenance tests.
AGENTS, README, state, governance review and ADR-028 updated. Other AI directories contain policies only.
No invented external ChatGPT/Work/Agent conversations. Original Codex source logs remain read-only.

## Tests / evidence
Eight exporter tests PASS. Capture integrity/secret-pattern check PASS. Existing repository audit PASS;
no functional source hashes changed, so previous RTL/model evidence remains applicable. No new EDA run claimed.
Evidence: v1/evidence/interaction_memory/validation.json. Tool-flow report retains observed initial UTF-8
fixture and CRLF digest failures and their fixes. Source Chinese is intact (earlier terminal display issue corrected).

## Limits / next action
Codex coverage PARTIAL: compaction/open turn, omitted images and raw tool payloads. Only allowlisted visible
messages are exported, never private reasoning/provider instructions. Run capture at next task start to include
this task's final response after it exists in the source log. No background recorder or native hook installed.
External ChatGPT SonoField-FPGA remains BLOCKED. Existing hardware problems unchanged.
Diff/privacy review and normal main push complete this delivery; future checkpoints use documented commands.

## Scoped result
ACCEPT WITH LIMITATIONS for interaction-memory configuration. Whole-platform hardware acceptance remains external.
