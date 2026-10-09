# Rollback plan

This candidate is unmerged. Close its PR or leave its branch unmerged to leave main `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570` untouched. The old physical sandbox, private/untracked assets and prior PR branches remain intact. Do not delete history or reset/clean user workspaces.

To inspect the exact complete pre-migration v5 tree, create a separate clone and check out `7dda49f00983c57d06ac639ad70bdaff9696e900` detached. The original pre-workspace root can be restored from `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570` in another clone; it contains the old relative structure. Recovery reads of historical data require explicit user authorization. Fixed refs and all file identities are in v5/evidence/repository_cleanup/20261009/protected_refs.json and tracked_manifest_before.csv; active relocation map gives every old→new path. No protection tag was created/pushed.

After an approved normal merge, revert the specific merge with `git revert -m 1 <approved-merge-sha>` on a new review branch, or revert this migration's logical commits in reverse order if a fast-forward strategy was explicitly chosen. Determine the actual merge commit/parents first; do not run placeholder commands blindly. Run the same integrity/hash/full baseline/native OOC checks and review the revert PR before merging. No force push or history rewrite. Revert only the historical-isolation commits if the earlier complete v5 candidates should remain.

This PR includes prior unmerged PR1/PR2 ancestry. Review those dependencies before approving the full main diff; closing this candidate does not merge or close prior PRs. Reconcile any new main commits before acceptance. Gate7 post-merge verification has not been authorized or executed.
