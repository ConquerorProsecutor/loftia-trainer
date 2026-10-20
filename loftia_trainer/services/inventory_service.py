"""Inventory manipulation: stack size, item duplication, slot unlock."""
from __future__ import annotations

from loftia_trainer.core.patterns import INVENTORY_BASE


class InventoryService:
    MAX_SLOTS = 60

    def __init__(self, mem, patches) -> None:
        self.mem = mem
        self.patches = patches

    def _base(self) -> int:
        return self.mem.module_base() + INVENTORY_BASE.offset

    def unlock_all_slots(self) -> None:
        base = self._base()
        for slot in range(self.MAX_SLOTS):
            self.mem.write_i32(base + slot * 0x10 + 0x04, 1)

    def set_stack(self, slot: int, quantity: int) -> None:
        if not 0 <= slot < self.MAX_SLOTS:
            raise ValueError(f"slot {slot} out of range")
        self.mem.write_i32(self._base() + slot * 0x10 + 0x08, quantity)

    def duplicate_item(self, slot: int) -> None:
        qty = self.mem.read_i32(self._base() + slot * 0x10 + 0x08)
        self.set_stack(slot, qty * 2)