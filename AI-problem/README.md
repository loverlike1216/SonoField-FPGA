# Engineering problem / decision protocol

Problems contain repository evidence and questions for the external reviewer. Decisions are created only
from real attributed replies; none has been received. Do not synthesize answers as ChatGPT decisions.

Problem hashes use SHA256 of the UTF-8 body after the closing YAML frontmatter delimiter, normalized
LF, including final newline. The problem_hash field is excluded to avoid self-reference. A decision must
match this hash, problem_id and active_version before execution. Changed bodies invalidate old decisions.
User approval remains necessary for new versions, scope, spending, publishing and irreversible changes.

| Problem | Scope | Status |
|---|---|---|
| [P-20260919-001](problem/P-20260919-001__board-facts.md) | Full board identity / voltage / pin conflicts | OPEN |
| [P-20260919-002](problem/P-20260919-002__serializer-interface.md) | Serializer physical timing and interface | OPEN |
| [P-20260919-003](problem/P-20260919-003__transducer-qualification.md) | New 10 mm part and physical qualification | OPEN |

Delivery to external ChatGPT is BLOCKED by unavailable reader/sender integration. Repository records
are ready for manual review; no claim of submission, response or approval is made.
