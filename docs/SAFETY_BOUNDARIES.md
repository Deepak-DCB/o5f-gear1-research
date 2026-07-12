# Safety boundaries

| Activity | Project status | Notes |
|---|---|---|
| offline static analysis of lawfully obtained files | in scope | no firmware execution or modification |
| ordinary hardware observation through documented normal tools | context only | do not infer Gear from a clock display alone |
| authorized debugger or privileged read access | conditional | only as a qualifying evidence source; no enablement or state changes |
| firmware instrumentation | outside recommended boundary | signature, Boot Guard, and no-POST risk |
| firmware modification or repack | prohibited | not a supported experiment |
| direct PCI/MSR/MCHBAR/mailbox/MRC writes | prohibited | bypasses the research safety boundary |
| setup/NVRAM changes intended to influence Gear | prohibited | active path and recovery are unproven |

Pre-memory failure can remove normal operating-system access. The existence of
hidden setup questions or a write-capable utility is not evidence of a safe
recovery route. The project remains read-only unless the reopening gates are met.

