# Privacy audit

The public tree was scanned before its initial commit for absolute local paths,
user names, machine names, email addresses, API keys, tokens, cookies,
credentials, authenticated remotes, serial numbers, MAC addresses, Windows SIDs,
browser-download locations, telemetry files, and crash dumps.

Result: no secret or machine-specific value is intentionally included. Local
input paths in examples are repository-relative placeholders. Vendor hashes,
module GUIDs, and public model identifiers are retained because they are needed
for reproducibility and are not personal identifiers.

If a contributor finds a privacy issue, report it privately under `SECURITY.md`.

