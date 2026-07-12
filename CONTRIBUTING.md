# Contributing evidence

This project values provenance and reproducibility over volume. Read the safety
policy before opening an issue or pull request.

## Welcome contributions

- official firmware metadata, source URLs, and SHA-256 values;
- contract-scoring results from lawfully obtained local firmware;
- exact FFS/module identities and independently reproducible offsets;
- matched O5F i7-11700K/i9-11900K observations with authorized pre-memory
  capture provenance;
- model-specific recovery documentation with primary-source support; and
- corrections backed by instruction-level dataflow or an exact table/map.

Use `templates/FIRMWARE_CANDIDATE_INTAKE.md`,
`templates/MATCHED_CAPTURE_INTAKE_TEMPLATE.md`, or
`templates/CLAIM_SUBMISSION_TEMPLATE.md`.

## Do not submit through ordinary pull requests

- firmware packages, BIOS images, capsules, FSP/MRC blobs, or extracted modules;
- private Intel or OEM documentation;
- credentials, tokens, personal logs, telemetry captures, serials, or MAC data;
- write-capable unlock scripts, setup editors, flash tools, or patch recipes;
- unverifiable screenshots; or
- claims that a patch is safe without the evidence required by this repository.

Every accepted evidence contribution needs provenance, hardware/BIOS identity,
capture stage, raw output hash, reproduction procedure, proposed evidence class,
and a statement that the contributor may publish the submitted material.

Security-sensitive findings and write-capable techniques must be reported
privately under `SECURITY.md`, not published in an issue first.

