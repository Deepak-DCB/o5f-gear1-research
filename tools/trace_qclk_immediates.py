#!/usr/bin/env python3
"""Read-only census of user-supplied IA32 RklComp bytes for QCLK MMIO offsets."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from capstone import CS_ARCH_X86, CS_MODE_32, Cs
from capstone.x86 import X86_OP_IMM, X86_OP_MEM


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rkl", required=True, type=Path, help="local RklComp TE body")
    parser.add_argument("--base", required=True, type=lambda value: int(value, 0), help="TE virtual base")
    parser.add_argument("--offset", action="append", type=lambda value: int(value, 0),
                        default=[0x5E00, 0x5E04], help="MMIO offset to report; repeatable")
    args = parser.parse_args()
    data = args.rkl.read_bytes()
    targets = set(args.offset)
    decoder = Cs(CS_ARCH_X86, CS_MODE_32)
    decoder.detail = True
    decoder.skipdata = True
    hits = []
    for insn in decoder.disasm(data, args.base):
        if not insn.id:
            continue
        values = []
        for operand in insn.operands:
            if operand.type == X86_OP_IMM and operand.imm in targets:
                values.append(operand.imm)
            if operand.type == X86_OP_MEM and operand.mem.disp in targets:
                values.append(operand.mem.disp)
        if values:
            hits.append({"address": f"0x{insn.address:X}", "targets": [f"0x{x:X}" for x in values],
                         "mnemonic": insn.mnemonic, "operands": insn.op_str})
    print(json.dumps({"schema": 1, "targets": [f"0x{x:X}" for x in sorted(targets)], "hits": hits}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

