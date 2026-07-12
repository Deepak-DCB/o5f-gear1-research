# References and reproducibility

## Primary sources

- Lenovo O5F package page for Legion T7-34IMZ5:
  <https://support.lenovo.com/us/en/downloads/ds545238-bios-for-windows-10-64-bit-legion-t7-34imz5-desktop>
- Lenovo platform specification reference:
  <https://psref.lenovo.com/syspool/Sys/PDF/Legion/Lenovo_Legion_T7_34IMZ5/Lenovo_Legion_T7_34IMZ5_Spec.PDF>
- Intel Gear 1/Gear 2 explanation and SKU guidance:
  <https://www.intel.com/content/www/us/en/support/articles/000058859/processors/intel-core-processors.html>
- Intel 11th-generation processor datasheet catalog:
  <https://www.intel.com/content/www/us/en/content-details/631122/11th-generation-intel-coretm-processors-datasheet-volume-2-of-2.html>

Additional vendor package links and hashes are in
[`evidence/FIRMWARE_PROVENANCE.csv`](../evidence/FIRMWARE_PROVENANCE.csv).

## Reproduce public-safe checks

1. Download a cited firmware package directly from the vendor.
2. Verify its SHA-256 against `FIRMWARE_PROVENANCE.csv`.
3. Extract it locally with a tool you lawfully obtained. Do not commit or upload
   the package, image, modules, or disassembly.
4. Install the Python dependency needed by the public scripts in an isolated
   environment: `python -m pip install capstone`.
5. Run `tools/score_o5f_contract.py` only against locally obtained files. Use
   repository-relative placeholder paths in your own notes.
6. Compare resulting hashes, GUID counts, scores, and hard failures with the
   published ledgers.

No command in this repository flashes a device, runs a vendor updater, writes a
firmware variable, or accesses target hardware state.

