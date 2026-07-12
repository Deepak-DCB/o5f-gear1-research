# Lenovo O5F Rocket Lake Gear 1 Firmware Research

This repository is a read-only reverse-engineering study of memory Gear policy
in Lenovo Legion T7-34IMZ5 O5F firmware. It documents reproducible reasoning,
hashes, offsets, and safe evidence requirements without redistributing vendor
firmware or providing a modification procedure.

## Final result: NO-GO

No safe or supported procedure was found to make the target system train
DDR4-3200 in Gear 1.

This does **not** prove an i7-11700K is electrically incapable of DDR4-3200
Gear 1. It proves that the analyzed O5F integration leaves essential policy and
eligibility inputs unresolved, offers no proven normal High-Gear control path,
and has no proven bounded recovery from failed pre-memory experimentation.

The project does not recommend setup-variable edits, NVRAM changes, firmware
patching, FSP/MRC modification, branch overrides, PCI/MSR/MCHBAR writes, OC
mailbox actions, or runtime MRC injection.

## Target and observed configuration

- Lenovo Legion T7-34IMZ5, Type 90Q8
- Intel Core i7-11700K
- Lenovo Z490/Rocket Lake board
- 2 × 16 GB DDR4-3200 Kingston OEM DIMMs
- Observed state: DDR4-3200 Gear 2, command rate 1T, MCLK approximately
  1596 MHz, UCLK approximately 798 MHz

Primary memory timings and DIMM ranks were not captured, so this repository
does not claim a benchmarked latency delta for a hypothetical Gear change.

## Canonical model

```text
SiInitPreMemFsp
  -> construct policy record 30d12ad5-...
  -> policy+0x32 = 1 (Gear 2)
  -> unresolved Intel scheduler/generated conversion
  -> MrcData+0x5514 (High request)
  -> independent eligibility gates
  -> MrcData+0x61BE (final Gear)
  -> MC_BIOS_REQ.bit16
  -> MC_BIOS_DATA.bit16
```

Gear 1 above DDR4-2933 requires both proven predicates to be clear:

```text
(MrcData+0x55D5 & 0x800) == 0
MrcData+0x5534 == 0
```

The physical sink is documented by Intel and proven in O5F dataflow:

```text
MC_BIOS_REQ  = MCHBAR + 0x5E00
MC_BIOS_DATA = MCHBAR + 0x5E04
bit 16: 0 = Gear 1, 1 = Gear 2
```

The visible High-Gear HII field has no proven active consumer. O5F initializes
the active High policy byte to Gear 2; the later cold conversion and provider
record producer are missing Intel framework boundaries. See
[the final execution model](docs/FINAL_EXECUTION_MODEL.md) and
[the evidence ledger](evidence/FINAL_EVIDENCE_LEDGER.csv).

## Major corrections

- `SaSetup+0x1AD` is storage metadata, not a proven active High-Gear control.
- `FSPM_UPD+0x679` targets a different policy record and is not the Rocket Lake
  High-Gear input.
- The `(MrcData, 0xDD00)` callback precedes a cold clear through `+0x5514`; it
  is not established as the surviving cold High producer.
- D0:F0 offset `0xFC` affects only one eligibility restriction. It is not a
  proven CPU-SKU identifier or a complete Gear unlock.
- The 3200-to-2933 Gear 1 branch is a downshift, not a 3200 Gear 1 path.

## Project history in brief

The investigation began with hidden HII Gear fields and visible policy records.
It then traced the active request, recovered the two independent above-2933
gates, ruled out a generic HOB constructor, and tested carefully constrained
cross-firmware references. The final stages corrected earlier off-by-one and
callback-provenance assumptions, established the physical QCLK sink, and closed
the public static route at partial references only.

## Method and scope

The work uses official firmware provenance, local extraction by the researcher,
short essential pseudocode, module GUIDs, addresses, hashes, and offline scripts.
Vendor binaries, extracted modules, disassemblies, large machine-code listings,
and write-capable utilities are intentionally absent. Details are in
[Evidence method](docs/EVIDENCE_METHOD.md), [Safety boundaries](docs/SAFETY_BOUNDARIES.md),
and [Third-party content](THIRD_PARTY_CONTENT.md).

## Repository contents

- `docs/`: public-safe model, methods, limits, safety, and references.
- `evidence/`: concise claims, hashes, provenance, and contract definition.
- `tools/`: offline source-only read-only analysis tools.
- `templates/`: contribution and matched-capture intake forms.
- `research-notes/`: focused explanatory summaries of the major boundaries.

Publication checks are recorded in [the safety audit](docs/PUBLICATION_SAFETY_AUDIT.md),
[privacy audit](docs/PRIVACY_AUDIT.md), and
[copyright audit](docs/COPYRIGHT_AUDIT.md). The current publication recommendation
is [private manual review first](docs/PUBLICATION_DECISION.md).

## Reproducing public-safe results

Download firmware only from the cited official sources, verify the published
hashes, extract locally, and run the offline scripts against files you lawfully
obtained. Do not upload firmware or extracts to this repository. The process is
documented in [References and reproducibility](docs/REFERENCES.md).

## Contributing evidence

Useful contributions are authenticated firmware metadata, hashes, contract
results, exact module identities, authorized matched O5F observations, and
model-specific recovery documentation. Use the templates under `templates/` and
read [CONTRIBUTING.md](CONTRIBUTING.md) first.

The project can reopen only under the evidence gates in
[Reopening conditions](docs/REOPENING_CONDITIONS.md). A screenshot, an
unmatched board, or a proposed patch does not meet that bar.

## Practical recommendation

Keep a stable DDR4-3200 Gear 2 configuration. Consider DDR4-2933 Gear 1 only
if Lenovo exposes it through a normal supported firmware path. This repository
does not endorse an unsupported 3200 Gear 1 experiment on O5F.

## License and vendor relationship

Original scripts are MIT-licensed; original prose and diagrams are CC BY 4.0.
Third-party firmware and documentation are not included or relicensed. Lenovo,
Intel, AMI, Dell, Gigabyte, and other marks belong to their respective owners.
This work is independent and not endorsed by any vendor.
