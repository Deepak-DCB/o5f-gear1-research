# Security and safety policy

This project does not provide a Gear 1 unlock. Firmware modification can prevent
POST, and Boot Guard, signed-firmware, and pre-memory recovery constraints may
apply.

Do not use this repository as justification to write NVRAM, PCI configuration,
MSRs, MCHBAR, OC mailbox state, flash contents, or MRC memory. Do not disable
platform security controls to collect one value.

If you discover a vulnerability, a write-capable technique, a bypass, or a
security-sensitive recovery method, do not publish operational details in a
public issue. Contact the maintainers privately through the repository host's
private vulnerability-reporting mechanism when configured. Include only the
minimum reproduction detail required for triage and do not attach vendor
firmware or credentials.

