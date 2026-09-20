# v1 execution contract — observable AI interaction memory

## Goal / user authorization
Apply the new personalized rules: persist user/Codex messages and key observable tool flows locally and
on the existing GitHub main branch. Keep v1; no hardware/RTL/model changes or new version.

## Inputs / baseline
Clean main 4ff3c38 equals origin/main. Repository audit PASS; existing digital evidence is unchanged.
ChatGPT source remains SonoField-FPGA and BLOCKED. Local Codex JSONL exists for thread
01a0b538-9430-7561-9ba4-623f57501f43 and its session metadata matches this exact workspace.

## Scope / architecture
AI-interaction-memory: index, session metadata, canonical Codex transcript, partial tool-call register and curated tool-flow reports,
and a reusable allowlist exporter/checker. Register actual participation only; no made-up Work/Agent messages.
Update project AGENTS, README, shared state/handoff/decision/changelog. Store a public-safe filtered copy.

## Constraints / non-goals
Never export analysis, reasoning, summaries, system/developer prompts or runtime metadata payloads.
Only user-supplied instructions and visible assistant commentary/final answers are message sources.
Do not reintroduce obsolete version trees; historical words in quoted user instructions remain verbatim.
No global memory writes, no background service or fictitious automatic capture after turn completion.
No source log edits. No full ChatGPT-history claim; no guessed earlier messages.

## Validation / evidence
Test role/channel allowlist, secret redaction, source-workspace match, deterministic exports, integrity
hash tampering, and explicit partial-history handling. Run existing repository audit to confirm no stale
functional source hashes. Check text/links/JSON, scan public records for credentials and sensitive paths,
commit/push and verify matching remote SHA. No RTL rerun needed for unchanged functional source.

## Rollback / done when
Normal Git revert of scoped changes. Canonical transcript/index and source boundary are inspectable,
sync command rerunnable, privacy checks pass, local/remote match, limitations documented.

## Execution result
Real transcript and partial call register exported; eight tests, integrity/secret check and repository audit PASS.
No functional engineering source changes; no new version. GitHub checkpoint sync follows reviewed capture.
