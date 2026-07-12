# Eligibility gates

O5F allows Gear 1 above 2933 only when both conditions hold:

```text
(MrcData+0x55D5 & 0x800) == 0
MrcData+0x5534 == 0
```

The D0:F0 offset `0xFC` behavior can influence the first restriction, but the
register's semantic origin is unknown. The second gate comes from final provider
record `5c696093+0x1F`; its normal producer is outside the decoded closure.

These are independent gates. Clearing or explaining one does not settle the
other.

