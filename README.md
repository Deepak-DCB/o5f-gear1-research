# Lenovo O5F Gear 1 Research

This is a public, read-only firmware-research project about an open question:
can the Lenovo Legion T7-34IMZ5 running O5F firmware and an Intel Core
i7-11700K safely train DDR4-3200 in Gear 1?

The project began with a practical observation: the system runs DDR4-3200 in
Gear 2 even though the firmware contains hidden Gear-related setup fields. The
work has since grown into a careful reconstruction of the policy, memory
reference-code, and hardware-state decisions involved. Its purpose is to make
the evidence legible and reusable for people with firmware, UEFI/PI, Intel
memory-init, platform-security, or hardware-validation experience.

## Research status

The question remains open, but the current evidence does **not** justify an
experiment on the target machine. Two independent eligibility gates select
Gear 2 above DDR4-2933, and their ordinary-boot sources have not been fully
recovered. The available O5F code also does not yet prove a bounded recovery
path if pre-memory training fails.

That is a safety boundary, not a claim that Gear 1 at DDR4-3200 is impossible
on this CPU. A sound continuation should reduce the remaining unknowns with
new evidence, rather than bypassing policy or forcing hardware state.

## The question in plain language

Intel Rocket Lake memory controllers can run their internal memory-controller
clock at different ratios to DRAM clock. At DDR4-3200, Gear 1 would normally
mean the controller runs at roughly 1600 MHz; Gear 2 means roughly 800 MHz.
The target system has been observed in the latter state.

The study asks four connected questions:

1. Which firmware input actually requests the High Gear setting?
2. What decides whether a DDR4-3200 Gear 1 request is eligible?
3. Does the target CPU/platform naturally satisfy those conditions?
4. If training fails, is there a proven recovery route that avoids a persistent
   pre-memory boot failure?

## What has been established

- The firmware holds Gear-related setup metadata, but the visible High-Gear
  setup byte is **not** a proven active control for the target path.
- An active Rocket Lake policy record is constructed with its High-Gear policy
  byte set to Gear 2. The surviving conversion from that policy to the MRC
  request lies behind an unresolved Intel-framework boundary.
- The MRC code initially honors its incoming High-Gear request, then applies
  two independent restrictions for Gear 1 above DDR4-2933:

  ```text
  (MrcData+0x55D5 & 0x800) == 0
  MrcData+0x5534 == 0
  ```

- One restriction is influenced by a read of host-bridge PCI D0:F0 offset
  `0xFC`, but the register's semantic meaning and the target's value remain
  unproven.
- The ordinary-boot producer of the provider-record field that reaches
  `MrcData+0x5534` is outside the recovered O5F corpus.
- The final hardware-facing outcome is documented: `MC_BIOS_REQ` and
  `MC_BIOS_DATA` are at MCHBAR `+0x5E00` and `+0x5E04`; bit 16 reports Gear 1
  when clear and Gear 2 when set.

The compact, source-linked record is the
[final evidence ledger](evidence/FINAL_EVIDENCE_LEDGER.csv). The complete
static model is in [the execution model](docs/FINAL_EXECUTION_MODEL.md).

## What remains to be solved

The most useful next evidence would resolve one or more of these boundaries:

- the external/generated marshaller that converts active Rocket Lake policy
  into `MrcData+0x5514`;
- the constructor or default table for provider record
  `5c696093-...`, especially offset `+0x1F`;
- the architectural meaning and target value of host-bridge D0:F0 offset
  `0xFC`;
- the outer consumer of MRC training failure and its retry, fallback, or
  recovery behavior;
- a matched, read-only O5F capture from both i7-11700K and i9-11900K systems;
- an official or independently validated recovery mechanism for this Lenovo
  model.

The exact reopening standard is documented in
[Reopening conditions](docs/REOPENING_CONDITIONS.md).

## How experienced contributors can help

Contributions are especially welcome from people who can provide lawful,
reproducible evidence in one of these areas:

- Intel FSP/MRC or PEI framework analysis, particularly generated policy
  marshalling and PPI/provider lifecycles;
- Rocket Lake host-bridge register documentation or trusted platform traces;
- a comparable, authorized firmware build with the same framework structures;
- Lenovo T7-34IMZ5 service/recovery documentation or validated observations;
- matched, read-only captures from O5F systems with i7-11700K and i9-11900K
  processors; or
- review of the public claim chain for an error, missing alternative, or
  stronger interpretation.

Please begin with [CONTRIBUTING.md](CONTRIBUTING.md), use the intake templates
under `templates/`, and label evidence as **PROVEN**, **STRONG INFERENCE**, or
**HYPOTHESIS**. A concrete counterexample is as valuable as confirming data.

## Safety and scope

This repository deliberately does not provide a modification recipe. It does
not endorse setup-variable edits, NVRAM changes, firmware patches, FSP/MRC
changes, branch overrides, PCI/MSR/MCHBAR writes, OC-mailbox actions, or
runtime MRC injection.

These are not arbitrary exclusions: the current evidence does not show that
they would cause a genuine Gear 1 training attempt, pass both eligibility
gates, or recover safely if training fails. See [Safety boundaries](docs/SAFETY_BOUNDARIES.md)
and [the GO/NO-GO matrix](docs/GO_NO_GO_MATRIX.md).

Vendor firmware, extracted modules, disassembly listings, vendor executables,
and write-capable tools are intentionally absent. The repository contains
original prose, hashes, compact evidence records, templates, and small
offline/read-only source tools only.

## Repository guide

- `docs/` — the model, methodology, safety constraints, limitations, and
  source references.
- `evidence/` — claims, provenance, module hashes, and the analysis contract.
- `research-notes/` — focused explanations of the policy, gates, and QCLK
  sink.
- `tools/` — small source-only offline helpers; no drivers or write paths.
- `templates/` — structured ways to submit candidate firmware or matched
  capture evidence.

For the project history, including corrected assumptions, see
[Invalidated findings](docs/INVALIDATED_FINDINGS.md). For reproduction without
redistributing vendor material, see [References and reproducibility](docs/REFERENCES.md).

## Target and observation

- Lenovo Legion T7-34IMZ5, Type 90Q8
- Lenovo O5F firmware
- Intel Core i7-11700K
- Lenovo Z490/Rocket Lake board
- 2 x 16 GB DDR4-3200 Kingston OEM DIMMs
- Observed: DDR4-3200 Gear 2, command rate 1T, MCLK approximately 1596 MHz,
  UCLK approximately 798 MHz

Primary memory timings and DIMM ranks were not captured. This repository does
not claim a benchmarked performance or latency outcome for a hypothetical Gear
change.

## License and independence

Original scripts are MIT-licensed; original prose and diagrams are CC BY 4.0.
Third-party firmware and documentation are neither included nor relicensed.
Lenovo, Intel, AMI, Dell, Gigabyte, and other marks belong to their respective
owners. This independent research is not endorsed by any vendor.
