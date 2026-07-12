# Matched capture intake

```yaml
capture_id: ""
raw_file_sha256: ""
capture_mechanism: ""
authorized_read_only: true
model_type: ""
board_fru_revision: ""
bios_revision_and_hash: ""
cpu_sku_stepping_cpuid: ""
dimm_slots_parts_ranks_spd_hashes: ""
boot_mode: ""
saved_mrc_state: "cold/no-saved | valid-saved | unknown"
ordered_values:
  policy_guid_type_size_and_plus_0x32: ""
  mrc_plus_0x5514_after_cold_conversion: ""
  provider_guid_record_guid_size_and_plus_0x1f_before_copy: ""
  d0f0_fc_dword_and_mrc_plus_0x5534_5555_55d5: ""
  frequency_and_mrc_plus_0x61be_before_clamp: ""
  mc_bios_req_and_mc_bios_data_after_completion: ""
stage_identifiers: ""
review_status: "unreviewed"
```

Reject missing raw hashes, exact stages, board/DIMM identity, or capture
authorization. Do not infer gate values from a final Gear report.

