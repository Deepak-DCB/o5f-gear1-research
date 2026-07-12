# Invalidated findings

| Earlier idea | Corrected conclusion |
|---|---|
| `SaSetup+0x1AD` directly populates policy `+0x32` | Low/Mid loop has two iterations; High is not copied |
| `FSPM_UPD+0x679` is High Gear | it belongs to another record |
| `0xDD00` callback supplies surviving cold High state | cold clear through `+0x5514` follows it |
| D0:F0 `0xFC` is an i9 or complete unlock condition | it affects only one gate and its semantics are unknown |
| 3200-to-2933 fallback proves 3200 Gear 1 | it explicitly lowers frequency to 2933 |
| generic GUID HOB constructor creates decisive provider record | it creates HOBs, not the provider record |

