# Observable interaction memory

This directory records public-safe, observable project interactions. It never captures hidden reasoning,
analysis, compaction summaries, system/developer prompts or unknown previous conversations.
Canonical external ChatGPT history stays in ../AI-chat-memory; it is currently BLOCKED.

## Sources and coverage
Local Codex rollout metadata identifies the project workspace and thread. Export requires an explicit source
file and rejects another workspace. Canonical transcript is codex/<thread>.md. Session manifests provide
source filename, UTC cutoff, source lines, available message IDs, message count and file hashes.
Status is PARTIAL: the current session is open, compaction exists, images are not copied, and the tool register
intentionally contains only name/ID/source-line/output-presence. No summary masquerades as verbatim speech.
Only sanitized original text appears inside the fenced message blocks. Historical version names in original
user instructions remain quotations; they do not recreate an old version layout.

## Synchronization
From the repository root, in PowerShell:

```powershell
$sourceLog = Join-Path $env:USERPROFILE '.codex/sessions/2026/09/18/rollout-2026-09-18T23-52-59-01a0b538-9430-7561-9ba4-623f57501f43.jsonl'
.\.venv\Scripts\python.exe AI-interaction-memory/tools/sync_codex.py --source $sourceLog
.\.venv\Scripts\python.exe AI-interaction-memory/tools/sync_codex.py --check
.\.venv\Scripts\python.exe -m unittest discover -s AI-interaction-memory/tools -p test_sync_codex.py -v
```

For a new thread, find its actual matching source log and pass that explicit path; do not assume this old
thread covers it. Source data stays read-only. Existing message ID/digest comparisons reject missing/changed
history; repeated unchanged snapshots do not duplicate messages. File hashes use UTF-8 canonical LF;
per-message hashes describe sanitized source text. No source-wide hash of private excluded payloads is exported.

This is a checkpoint command plus project AGENTS policy, not an installed background service or native
end-of-turn hook. At task start capture the previous final response; before commit capture messages already
persisted. A final response emitted after the last capture enters the next checkpoint. Do not claim otherwise.
If the local rollout is missing, mark BLOCKED/NOT_SUPPORTED and preserve earlier records; no reconstruction.

## Privacy and review
Known credential patterns, home-directory names and email addresses are redacted. Binary attachments are
omitted. No generic detector guarantees discovery of every secret: review diffs before GitHub publication.
Raw tool payloads are not blindly copied because source-log inspection outputs can echo excluded private
content. Curated tool-flow reports record meaningful commands/results and link existing evidence instead.
User-supplied instruction history is retained; internal model/provider instructions are excluded by allowlist.

## Other sources
work/, other-ai/, cross-agent/ currently contain no captured sessions. Add real records only when those tools
actually participate; never manufacture consultations or replies. INDEX is the recovery entry point.
