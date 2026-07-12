# Offline tools

Both scripts are source-only, offline, and read-only. They require Python 3 and
the `capstone` package. They do not include firmware and do not execute,
repackage, flash, or modify any input.

- `score_o5f_contract.py` compares locally obtained candidate modules against
  the published O5F contract. It is intentionally false-negative-biased.
- `trace_qclk_immediates.py` reports only instructions in a locally obtained
  IA32 RklComp body that reference supplied MMIO offsets such as `0x5E00` and
  `0x5E04`.

Example placeholders:

```text
python tools/score_o5f_contract.py --label candidate --image path/to/image.bin \
  --rkl path/to/RklComp.bin --si path/to/Si.bin --fsp path/to/Fsp.bin \
  --platform path/to/Platform.bin --reference-rkl path/to/verified-O5F-RklComp.bin

python tools/trace_qclk_immediates.py --rkl path/to/RklComp.bin --base 0xFFC0FFD4
```

Do not commit the referenced local input files.

