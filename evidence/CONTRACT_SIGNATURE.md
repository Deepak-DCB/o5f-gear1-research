# O5F contract signature

The contract filter prevents shared GUIDs from being mistaken for compatible
MRC behavior. A candidate is not considered useful unless it satisfies every
hard requirement below.

## Mandatory fields

- IA32 TE pre-memory modules.
- Policy GUID `30d12ad5-a3c6-49c7-a2fd-355ccb61cbcf` with size `0x7C`, type 3.
- Provider GUID `eb7fb39c-da93-badd-2b1e-8fd3b321d143`.
- Final record GUID `5c696093-b3d4-c920-28e9-f4085f0fd446`.
- O5F record-copy, High-honor, above-2933 clamp, final-sink, and callback ABI
  anchors.
- Decisive field-reference profile for `+0x5514`, `+0x5534`, `+0x5555`,
  `+0x55B0`, `+0x55D5`, `+0x61A5`, and `+0x61BE`.

The published scorer uses an exact O5FKT14A-17A RklComp reference hash:

```text
f8f55d0f8fe6bb829576d2cb1ef004ce9f2ea1c74e1848c4deb59745310da6c2
```

Score interpretation:

| Result | Meaning |
|---|---|
| hard failure | reject O5F equivalence |
| 95-100 without hard failure | contract match requiring manual semantic audit |
| 80-94 without hard failure | near match, manual audit only |
| lower score | reject for this research purpose |

A pass is an admission condition for analysis, not permission to transfer code,
offsets, fields, defaults, or hardware policy.

