# Publication safety audit

Audit date: 2026-07-12. The authoritative source repository was audited only to
create this separate, clean public tree. It was not altered.

| Source-artifact class | Classification | Public treatment |
|---|---|---|
| Lenovo installers, BIOS images, capsules, firmware volumes, and dump trees | PRIVATE ONLY | excluded; hashes and official URLs only |
| Intel FSP/MRC and extracted PEI/DXE/TE/PE32 modules | PRIVATE ONLY | excluded; module GUIDs/hashes/roles only |
| Dell, Gigabyte, and P350 packages/extracts | PRIVATE ONLY | excluded; provenance and contract result only |
| flash utilities, drivers, and write-capable hardware tools | SECURITY-SENSITIVE | excluded |
| full disassemblies, large code listings, binary prefixes, proprietary tables | COPYRIGHT/REDISTRIBUTION UNCLEAR | excluded; original concise prose and minimal pseudocode only |
| private repository recovery snapshots and local extraction reports | PRIVATE ONLY | excluded |
| original closure summaries, ledgers, templates, and source-only offline tools | PUBLIC-SAFE AFTER REDACTION | rewritten in this repository with no local paths or vendor binaries |
| earlier superseded models | OBSOLETE OR INVALIDATED | retained only as explicit corrections |
| tool caches and bytecode | GENERATED AND UNNECESSARY | excluded through `.gitignore` |

The public tree intentionally has new history. It is not a visibility change or
history rewrite of the authoritative source repository.

