# GO/NO-GO matrix

| Criterion | State | Why it fails |
|---|---|---|
| normal controllable field reaches `MrcData+0x5514` | FAIL | cold conversion is unresolved |
| both eligibility gates pass on target 11700K | FAIL | target `0xFC` and provider `+0x1F` are unknown |
| normal Gear 1 training attempt occurs | FAIL | failed gate chooses Gear 2 first |
| failed training has bounded recovery | FAIL | no proven Gear/frequency retry or valid-state rollback |
| control uses ordinary Lenovo firmware services | FAIL | no active High control path is proven |
| bad state clears without external SPI | FAIL | valid bad pre-memory policy recovery is unproven |
| actual Gear is verified read-only | FAIL | final register is known; trusted narrow reader absent |
| no capability/MRC/branch/hardware patch is needed | FAIL | no complete legitimate path exists |

All criteria are conjunctive. The project stays NO-GO until every row is
proven, not merely plausible.

