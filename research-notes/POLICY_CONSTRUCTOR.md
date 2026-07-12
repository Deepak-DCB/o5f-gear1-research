# Policy constructor

`SiInitPreMemFsp` constructs the Rocket Lake policy record
`30d12ad5-a3c6-49c7-a2fd-355ccb61cbcf` as a `0x7C`, type-3 record. Its Rocket
Lake initializer writes High policy `+0x32 = 1`, where `1` is Gear 2.

Visible Lenovo and FSP patchers update only Low/Mid `+0x30/+0x31`. The later
conversion from this policy object to `MrcData+0x5514` is not present in the
decoded closure and must not be assumed to be a direct copy.

