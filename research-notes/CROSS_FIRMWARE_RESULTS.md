# Cross-firmware results

Gigabyte Z590 UD F2 demonstrates that a related Intel integration can populate
four policy fields, including High, but its record is `0x100/type2` and its MRC
contract differs. Dell Aurora R12 1.0.1 shares a Low/Mid-only construction
pattern but scores 23/100 with seven O5F hard failures. Lenovo ThinkStation P350
shares some identifiers but fails the strict raw Stage-1 filter.

No external candidate matched the full policy/provider/record/callback/clamp/
sink contract. These references are explanatory negative controls, never patch
sources.

