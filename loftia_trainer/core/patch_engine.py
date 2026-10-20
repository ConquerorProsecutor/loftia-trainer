"""Byte patcher with reversible patch records."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class PatchRecord:
    address: int
    original: bytes
    patched: bytes
    label: str = ""


@dataclass
class PatchEngine:
    mem: object
    applied: Dict[int, PatchRecord] = field(default_factory=dict)

    def apply(self, address: int, original: bytes, patched: bytes, label: str = "") -> None:
        if address in self.applied:
            return
        self.mem._pm.write_bytes(address, patched, len(patched))
        self.applied[address] = PatchRecord(address, original, patched, label)

    def revert(self, address: int) -> bool:
        rec = self.applied.pop(address, None)
        if rec is None:
            return False
        self.mem._pm.write_bytes(rec.address, rec.original, len(rec.original))
        return True

    def revert_all(self) -> int:
        count = 0
        for addr in list(self.applied.keys()):
            if self.revert(addr):
                count += 1
        return count