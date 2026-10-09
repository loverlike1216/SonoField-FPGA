# Rollback plan

Recovery SHA: `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`. Same repository, original Git history preserved. Original physical sandbox `E:\Codex_project\AMD-SonoField-FPGA` remains exactly as found, including pre-existing deletion, untracked v3/PCB/BOM/handoff and ignored raw data. Private inventories are local only.

Before merge: leave main unchanged, retain candidate branch and failure logs. To recover a clean original source copy, independently `git clone https://github.com/loverlike1216/SonoField-FPGA.git <new-empty-directory>`, then `git switch --detach ecd32e76e9b6c08806eae30a3c75a9c3be5e7570` there. Never reset/pull/clean the original sandbox.

One file can be read with `git show ecd32e76e9b6c08806eae30a3c75a9c3be5e7570:<original-path>`; restore to a new review destination, without overwriting the original. The archive manifest maps every original path to history_old/<path> and records rawSHA256/blob/mode.

After an approved merge, a regression requires a newly reviewed revert commit. For a two-parent merge: `git revert -m 1 <verified-merge-SHA>` on a new rollback branch; for squash/single-parent commits, revert the verified migration commit(s) in reverse order. Review the resulting tree/diff, rerun core gates and submit a rollback PR. These are conditional instructions, not actions executed in this migration. Scope/merge approval is required. No force push, orphan branch, reset--hard or history rewrite.

Remote main changing during preparation invalidates the frozen comparison until a fresh reconciliation; never overwrite parallel commits. Missing archived objects, mismatched hashes or failures block merge. Device/boot rollback is unnecessary because migration performs no hardware operations.
