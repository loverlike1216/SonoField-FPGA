# Candidate quality gate

Conclusion: **ACCEPT WITH LIMITATIONS — CANDIDATE ONLY**. The whole physical platform remains **REVISE**, manufacturing **HOLD**. User approval for main merge/post-merge fresh remote clone/permanent workspace promotion is pending. No version upgrade.

| Gate | Status | Evidence / scope |
|---|---|---|
|MIG-01|PASS|Same repo/currentv5/fixedBASE/independent new clone|
|MIG-02|PASS|3907original paths,97559165bytes,mode/blob/rawSHA256 zero mismatch;2frozen metadata|
|MIG-03|PASS|101394unique original/ignored-target/Git files rehashed;35untracked kept;public scan required before push|
|MIG-04|PASS|Default121source paths allv5;18own-source OOC;independent importedsoftware andvenv|
|MIG-05|PASS|Single currentv5 state/AX7020 facts;historical clock candidate unused;no oldboardphysicalconstraints|
|MIG-06|PASS|115tests and3696frames×4 each of3fresh environments|
|MIG-07|PASS|3Icarus+1XSim canonical hashes equal originalBASE and eachother|
|MIG-08|PASS|Full inheritedC/AXI/UARToffline/calibration/queue/safety/atomic/serializer/golden gates|
|MIG-09|PASS|RealVivado2025.2 rebuild/reopen18sources in3environments;OOC only|
|MIG-10|PASS|SecondindependentGit/lockednewvenv/fullavailableofflinegates;samehost limitation|
|MIG-11|PASS|Currentrecovery/acceptance/blockers/hardwareboundary/runbook/packageboundary;linkcheckbeforecommit|
|MIG-12|PASS|Zero device operations;no board/hardware proof invented|

See [full regression](PORTABILITY_AND_REGRESSION.md) and [machine gate](QUALITY_GATE.json) for actual tools, canonical hashes, failures, evidence and limits. Online CI and candidate remote receipts are recorded separately only after observed completion. Model self-review does not constitute independent final acceptance.

Actual publication: [Draft PR#1](https://github.com/loverlike1216/SonoField-FPGA/pull/1), exact remote tree verified at `f014214fb8db554fb3df9ac971ac759d683447a5`, push and PR Ubuntu structural/frozen-metadata checks both success. See [publication receipt](PUBLICATION_RECEIPT.md). Main merge and post-merge fresh remote-main clone remain pending user approval.
