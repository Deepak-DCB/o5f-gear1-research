# High-Gear control audit

The HII storage field at `SaSetup+0x1AD` is not a proven active Gear control.
The only decoded indexed copy uses a two-iteration loop and reaches Low/Mid
only. `FSPM_UPD+0x679` was also ruled out: it belongs to a separate policy
record rather than the active Rocket Lake High policy.

No public document in this repository should treat a hidden menu, a raw setup
value, or a field named “High Gear” as a safe way to attempt 3200 Gear 1.

