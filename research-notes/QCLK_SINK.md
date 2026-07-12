# QCLK sink

The final MRC Gear byte is `MrcData+0x61BE`. O5F moves it into
`MC_BIOS_REQ.bit16` and writes the request at `MCHBAR+0x5E00`; it subsequently
reads `MC_BIOS_DATA` at `MCHBAR+0x5E04`.

Intel documents bit 16 as Gear type: zero is Gear 1 and one is Gear 2. This is
the strongest final-state definition recovered by the project, but a safe public
target-side reader for that exact register was not found.

