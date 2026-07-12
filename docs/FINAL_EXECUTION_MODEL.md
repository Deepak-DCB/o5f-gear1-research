# Final execution model

```text
SiInitPreMemFsp
  -> construct 30d12ad5 policy record (0x7C/type 3)
  -> policy+0x32 = 1 (Gear 2)
  -> visible patchers update Low/Mid only
  -> unresolved later Intel scheduler/generated conversion
  -> MrcData+0x5514
  -> eligibility construction
  -> MrcData+0x61BE
  -> MC_BIOS_REQ.bit16 at MCHBAR+0x5E00
  -> MC_BIOS_DATA.bit16 at MCHBAR+0x5E04
```

The visible setup loop does not reach `SaSetup+0x1AD`. `FSPM_UPD+0x679` belongs
to a different policy record. On a no-saved boot, RklComp clears the working
range that includes `MrcData+0x5514` after the earlier `0xDD00` callback.
Therefore the live cold High conversion must be later than that clear and is
not recovered in the decoded closure.

The independent eligibility gates are:

```text
(MrcData+0x55D5 & 0x800) == 0
MrcData+0x5534 == 0
```

`D0:F0+0xFC.low8 == 4` can influence the first restriction through
`MrcData+0x5555.bit6`; it does not clear `+0x5534`. The provider record
`5c696093-...+0x1F` supplies ordinary `+0x5534`, but its producer remains
external.

If an above-2933 gate fails, O5F silently selects Gear 2 before any proven
Gear 1 training attempt. A separate path can downshift 3200 to 2933 while
selecting Gear 1; this is not 3200 Gear 1.

