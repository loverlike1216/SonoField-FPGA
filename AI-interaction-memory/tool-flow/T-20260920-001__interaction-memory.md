# T-20260920-001 — observable interaction capture

## Context / trigger
Project SONOFIELD_FPGA; v1; stage INTERACTION_MEMORY. Codex thread
01a0b538-9430-7561-9ba4-623f57501f43. User requested local/GitHub persistence of Codex interactions,
then said continue. Original wording is in the canonical [transcript](../codex/01a0b538-9430-7561-9ba4-623f57501f43.md).
This report is a curated observable execution summary, not a verbatim transcript or hidden reasoning.

## Actual tool sequence and outputs
1. Git status/remote/log/fetch: clean main at 4ff3c38, remote divergence 0/0.
2. Read AGENTS, README, shared state/version/plan/decisions/acceptance/blockers and AI-chat-memory index.
3. Inspect enabled tools: no external ChatGPT conversation reader. Locate exact local Codex source by
   thread ID, verify session_meta cwd equals this workspace. Source contains compaction; no full-history claim.
4. First terminal preview appeared garbled. Explicit Unicode codepoint inspection and zero replacement
   character count showed the source Chinese was intact. Codex corrected its earlier commentary publicly.
5. Implement role/channel allowlist, sanitized transcript, source-ID hashes, partial tool-call register,
   explicit source matching and checkpoint commands. No raw tool payloads or reasoning are published.
6. First 8-test run: 7 passed, one fixture read failed with Windows default GBK decoding; corrected the test
   reader to explicit UTF-8. A subsequent real export check exposed CRLF/LF digest mismatch. Canonical-LF
   file hashing fixed this without changing source messages; mixed-newline fixtures retained.
7. Final 8 tests PASS; exporter --check PASS; existing repository audit PASS. Commands/exit codes are in
   [validation evidence](../../v1/evidence/interaction_memory/validation.json).

## Commands / actions
- .venv/Scripts/python.exe -m unittest discover -s AI-interaction-memory/tools -p test_sync_codex.py -v
- .venv/Scripts/python.exe AI-interaction-memory/tools/sync_codex.py --source <verified-local-rollout.jsonl>
- .venv/Scripts/python.exe AI-interaction-memory/tools/sync_codex.py --check
- .venv/Scripts/python.exe v1/scripts/check_repository.py
- Normal git add/commit/push origin main; no release, force push or version upgrade.

## Files / evidence / decision impact
Writes AI-interaction-memory plus project rules/shared/README/CHANGELOG and scoped validation logs.
Existing v1 functional source and previous validation evidence remain unchanged. No FPGA synthesis or
hardware test is claimed. Tool calls are indexed in the [source register](01a0b538-9430-7561-9ba4-623f57501f43.md).
ADRs: shared/DECISIONS.md ADR-028. No external decision or cross-agent consultation occurred here.
Git commit containing this flow is discoverable with git log -- this file; do not invent a self-referential hash.
