"""Inventory item model."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Item:
    slot: int
    item_id: int
    quantity: int
    locked: bool = False

    def stackable(self) -> bool:
        return self.quantity > 1