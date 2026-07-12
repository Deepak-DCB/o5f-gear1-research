# Evidence method

Claims use the following classes:

| Class | Meaning |
|---|---|
| `PROVEN` | instruction-level dataflow, exact binary identity, or direct documentation |
| `STRONG_INFERENCE` | several independent static indicators support one interpretation |
| `HYPOTHESIS` | plausible but not demonstrated |
| `INVALIDATED` | an earlier active claim was disproven or corrected |
| `EXTERNAL_EVIDENCE_REQUIRED` | the necessary implementation or live value lies outside the decoded evidence |

The workflow was: authenticate package metadata; hash locally obtained images;
extract locally without execution; inspect module GUIDs, offsets, and small
necessary instruction behavior; compare only contract-compatible external
images; and reject incompatible references rather than transplant offsets.

This repository publishes the results of that method, not the vendor material
used locally. The offline tools process researcher-supplied local files and do
not modify them.

