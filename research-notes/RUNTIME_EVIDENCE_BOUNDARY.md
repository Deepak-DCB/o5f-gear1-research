# Runtime evidence boundary

The missing facts require ordered observation before and during memory
initialization. A qualifying pair captures matching O5F 11700K and 11900K
systems with policy `+0x32`, `MrcData+0x5514`, final provider `+0x1F`, both gates,
D0:F0 `0xFC`, final Gear, and controller request/data fields.

Post-MRC state can support final-Gear confirmation but cannot reconstruct the
first values of the two gates. Firmware instrumentation or enabling a debug
path on a production machine is outside this project.

