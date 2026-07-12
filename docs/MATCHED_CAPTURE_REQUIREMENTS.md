# Matched capture requirements

The useful comparison is O5F+i7-11700K versus O5F+i9-11900K with the same board
revision, BIOS build, DIMM topology, and boot mode. Capture the policy record
identity/type/size and `+0x32`; `MrcData+0x5514`; final provider `+0x1F`;
`+0x5534`, `+0x5555`, `+0x55D5`, and `+0x61BE`; full D0:F0 `0xFC`; and final
`MC_BIOS_REQ/DATA` values.

The values must be labeled by exact execution stage. A post-boot Gear value is
useful final-state evidence but cannot reconstruct the two pre-clamp gate inputs.
Use `templates/MATCHED_CAPTURE_INTAKE_TEMPLATE.md`.

