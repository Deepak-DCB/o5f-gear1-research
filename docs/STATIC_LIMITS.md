# Static limits

The completed public static search found no external firmware that matches the
full O5F contract. Gigabyte Z590 UD F2, Dell Aurora R12 1.0.1, and Lenovo
ThinkStation P350 each supplied limited structural evidence but failed mandatory
ABI, record, or behavior requirements.

The unresolved boundary is specific, not open-ended:

- policy `30d12ad5+0x32 -> MrcData+0x5514` after cold clear;
- provider `eb7fb39c` construction and final `5c696093+0x1F` producer; and
- target/matched-SKU runtime values for both gates.

Further broad BIOS acquisition is closed. Reopen only for qualifying evidence.

