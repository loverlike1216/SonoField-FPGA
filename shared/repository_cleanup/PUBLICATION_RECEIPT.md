# Historical isolation publication receipt

READY_FOR_USER_REVIEW. Verified 2026-10-09T16:23:22.043424+00:00. Same v5, official SonoField-FPGA repository.
Draft [PR #3](https://github.com/loverlike1216/SonoField-FPGA/pull/3) is OPEN, base main, head `939280960e6baddaf5d190b9c7f8534eb0b6fb16`. Main remains `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`; no merge. Runtime code actually tested is `3e788f4a2763c0354ca66d3836d0709dcf9f0107`; runtime source delta to the published evidence commit is zero. Archive 3,918 Git entries exactly match active payload/index identities; remote root has exact Historical project and no history_old. The history-absent clean clone fetched the official branch and confirmed the same source ancestry/metadata without checking out history.

Push CI and pull_request CI both passed at the evidence commit. [Push](https://github.com/loverlike1216/SonoField-FPGA/actions/runs/37958411424), [PR](https://github.com/loverlike1216/SonoField-FPGA/actions/runs/37958420085). They check current structure, preserved copies and frozen Git metadata with historical worktree absent; they do not claim cloud Vivado/GUI/hardware execution. Actual full before/after/newvenv/native evidence is in v5/evidence/repository_cleanup/20261009.

CP008 containing commit is `939280960e6baddaf5d190b9c7f8534eb0b6fb16`. This receipt's containing commit is resolved with Git log; it does not invent a circular self hash. This final receipt/transcript/status update changes no runtime source or archive payload. Final HEAD CI can be read directly from the PR without creating an endless receipt/CI commit loop.

Prior PR1/PR2 remain unmerged and their ancestry is included in PR3. Review those dependencies. Candidate ACCEPT WITH LIMITATIONS; whole platform REVISE,13existingphysical/ARM/PCB/reviewgatesopen. Gate7 deferred until explicit user approval of this concrete PR. No board/CAD/driver operation, version upgrade, force push or old physical workspace access.
