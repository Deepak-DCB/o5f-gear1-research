#!/usr/bin/env python3
"""Read-only, false-negative-biased O5F contract scorer.

This script accepts only local files supplied by the user. It never writes to
them and does not download, flash, or execute firmware.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import uuid
from collections import Counter
from pathlib import Path

from capstone import CS_ARCH_X86, CS_MODE_32, Cs
from capstone.x86 import X86_OP_MEM


GUIDS = {
    "policy": uuid.UUID("30d12ad5-a3c6-49c7-a2fd-355ccb61cbcf"),
    "source_provider": uuid.UUID("c133fe57-17c7-4b09-8b3c-97c189d0ab8d"),
    "source_record": uuid.UUID("26cf084c-c9db-41bb-92c6-d197b8a1e4bf"),
    "mrc_provider": uuid.UUID("eb7fb39c-da93-badd-2b1e-8fd3b321d143"),
    "final_record": uuid.UUID("5c696093-b3d4-c920-28e9-f4085f0fd446"),
}

O5F_REFERENCE_HASH = "f8f55d0f8fe6bb829576d2cb1ef004ce9f2ea1c74e1848c4deb59745310da6c2"
FIELDS = {0x5514, 0x5534, 0x5555, 0x55B0, 0x55D5, 0x61A5, 0x61BE}
WINDOWS = {
    "record_copy": (0x4B65, 32),
    "d0f0_fc": (0x4DB3, 32),
    "reconstruct_55d5": (0x61AF, 32),
    "above_2933_clamp": (0x743A, 32),
    "fallback_2933": (0x74DD, 32),
    "high_honor": (0x8593, 32),
    "dd00_call": (0x53E8, 32),
    "d5_call": (0x5A49, 32),
    "final_sink": (0x21B14, 32),
}
INITIALIZER_PATTERNS = [bytes.fromhex(value) for value in ("8d4128", "c6400a01", "83ee0175d7", "33c066894130")]
FSP_TWO_FIELD = bytes.fromhex("8a840e2501000088014183eb0175f1")
PLATFORM_SOURCE = bytes.fromhex("8a840cad010000")
PLATFORM_LOOP_END = bytes.fromhex("83f90272")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def te_base(data: bytes) -> int:
    if data[:2] != b"VZ" or struct.unpack_from("<H", data, 2)[0] != 0x14C:
        raise ValueError("expected IA32 TE image")
    return struct.unpack_from("<Q", data, 0x10)[0] + struct.unpack_from("<H", data, 6)[0] - 0x28


def field_profile(data: bytes) -> dict[str, int]:
    base = te_base(data)
    decoder = Cs(CS_ARCH_X86, CS_MODE_32)
    decoder.detail = True
    decoder.skipdata = True
    counts: Counter[int] = Counter()
    for insn in decoder.disasm(data, base):
        if not insn.id:
            continue
        for operand in insn.operands:
            if operand.type == X86_OP_MEM and operand.mem.disp in FIELDS:
                counts[operand.mem.disp] += 1
    return {f"0x{field:X}": counts[field] for field in sorted(FIELDS)}


def policy_descriptors(si: bytes) -> list[dict[str, int]]:
    base = te_base(si)
    policy_offset = si.find(GUIDS["policy"].bytes_le)
    if policy_offset < 0:
        return []
    pointer = struct.pack("<I", base + policy_offset)
    hits: list[dict[str, int]] = []
    start = 0
    while True:
        offset = si.find(pointer, start)
        if offset < 0:
            return hits
        if offset + 12 <= len(si):
            size, record_type, callback = struct.unpack_from("<HHI", si, offset + 4)
            if 0x10 <= size <= 0x1000 and record_type <= 8:
                hits.append({"offset": offset, "size": size, "type": record_type, "callback": callback})
        start = offset + 1


def platform_two_field_loop(data: bytes) -> bool:
    start = data.find(PLATFORM_SOURCE)
    while start >= 0:
        if PLATFORM_LOOP_END in data[start:start + 48]:
            return True
        start = data.find(PLATFORM_SOURCE, start + 1)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True)
    parser.add_argument("--image", type=Path, required=True)
    parser.add_argument("--rkl", type=Path, required=True)
    parser.add_argument("--si", type=Path, required=True)
    parser.add_argument("--fsp", type=Path, required=True)
    parser.add_argument("--platform", type=Path, required=True)
    parser.add_argument("--reference-rkl", type=Path, required=True,
                        help="verified local O5FKT14A-17A RklComp body")
    args = parser.parse_args()

    image, rkl, si, fsp, platform, reference = [
        path.read_bytes() for path in (args.image, args.rkl, args.si, args.fsp, args.platform, args.reference_rkl)
    ]
    if sha256(reference) != O5F_REFERENCE_HASH:
        raise ValueError("reference RklComp hash does not match verified O5FKT14A-17A")

    try:
        for body in (rkl, si, fsp, platform):
            te_base(body)
        ia32_te = True
    except ValueError:
        ia32_te = False

    descriptors = policy_descriptors(si) if ia32_te else []
    windows = {}
    for name, (offset, length) in WINDOWS.items():
        anchor = reference[offset:offset + length]
        windows[name] = {"reference_offset": offset, "match": anchor in rkl}

    counts = {name: image.count(value.bytes_le) for name, value in GUIDS.items()}
    rkl_counts = {name: rkl.count(value.bytes_le) for name, value in GUIDS.items()}
    profile_ok = ia32_te and field_profile(rkl) == field_profile(reference)
    descriptor_ok = any(item["size"] == 0x7C and item["type"] == 3 for item in descriptors)
    initializer_ok = all(pattern in si for pattern in INITIALIZER_PATTERNS)
    population_ok = FSP_TWO_FIELD in fsp and platform_two_field_loop(platform)
    callback_ok = windows["dd00_call"]["match"] and windows["d5_call"]["match"]
    hard = {
        "not_ia32_te": ia32_te,
        "policy_descriptor_not_0x7c_type3": descriptor_ok,
        "missing_provider_or_final_record": rkl_counts["mrc_provider"] > 0 and rkl_counts["final_record"] > 0,
        "missing_record_copy": windows["record_copy"]["match"],
        "missing_field_profile": profile_ok,
        "missing_high_honor": windows["high_honor"]["match"],
        "missing_clamp": windows["above_2933_clamp"]["match"],
        "missing_final_sink": windows["final_sink"]["match"],
        "callback_abi_mismatch": callback_ok,
    }
    hard_failures = [name for name, passed in hard.items() if not passed]
    scores = {
        "policy_guids": 4 if counts["policy"] and counts["source_provider"] and counts["source_record"] else 0,
        "policy_descriptor": 6 if descriptor_ok else 0,
        "policy_initializer": 6 if initializer_ok else 0,
        "two_field_population": 4 if population_ok else 0,
        "provider_guids": 6 if hard["missing_provider_or_final_record"] else 0,
        "field_profile": 6 if profile_ok else 0,
        "record_copy": 8 if windows["record_copy"]["match"] else 0,
        "d0f0_fc": 6 if windows["d0f0_fc"]["match"] else 0,
        "reconstruct": 5 if windows["reconstruct_55d5"]["match"] else 0,
        "clamp": 8 if windows["above_2933_clamp"]["match"] else 0,
        "fallback": 6 if windows["fallback_2933"]["match"] else 0,
        "honor": 7 if windows["high_honor"]["match"] else 0,
        "sink": 5 if windows["final_sink"]["match"] else 0,
        "callback": 5 if callback_ok else 0,
        "exact_rkl": 18 if sha256(rkl) == O5F_REFERENCE_HASH else 0,
    }
    score = sum(scores.values())
    classification = "REJECT_O5F_EQUIVALENCE"
    if not hard_failures and score >= 95:
        classification = "O5F_CONTRACT_MATCH"
    elif not hard_failures and score >= 80:
        classification = "NEAR_MATCH_MANUAL_AUDIT_REQUIRED"
    print(json.dumps({
        "schema": 1, "label": args.label, "classification": classification,
        "score": score, "score_max": 100, "hard_failures": hard_failures,
        "score_parts": scores, "guid_counts": counts, "rkl_guid_counts": rkl_counts,
        "policy_descriptors": descriptors, "field_profile_match": profile_ok,
        "window_results": windows,
        "hashes": {"image": sha256(image), "rkl": sha256(rkl), "reference_rkl": sha256(reference)},
        "safety_note": "A match is not permission to transfer offsets, policy, or firmware behavior."
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
