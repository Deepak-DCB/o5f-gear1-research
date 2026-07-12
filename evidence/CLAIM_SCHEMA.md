# Evidence-ledger schema

| Column | Meaning |
|---|---|
| `claim_id` | stable public identifier |
| `claim` | concise falsifiable statement |
| `evidence_class` | one of the public evidence classes |
| `firmware_build` | exact build or comparison set |
| `module` | module or bounded framework owner |
| `address_or_offset` | virtual address, raw offset, or bounded identifier |
| `source` / `destination` | dataflow endpoints when known |
| `condition` | predicate or scope |
| phase columns | first and latest validated research phase |
| `notes` | uncertainty, correction, or limitation |

Rows marked `INVALIDATED` are retained to prevent old interpretations from
re-entering the project as active evidence.

