"""AOB signatures for Loftia client offsets (build 2026.03)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Signature:
    name: str
    pattern: str
    offset: int = 0


PLAYER_HEALTH = Signature("player_health", "48 8B 05 ?? ?? ?? ?? 48 85 C0 74 05 F3 0F 10", 3)
PLAYER_STAMINA = Signature("player_stamina", "F3 0F 10 8B ?? ?? ?? ?? F3 0F 11 4D F0", 4)
INVENTORY_BASE = Signature("inventory_base", "48 8D 0D ?? ?? ?? ?? E8 ?? ?? ?? ?? 48 8B D8", 3)
TELEPORT_HOOK = Signature("teleport_hook", "E8 ?? ?? ?? ?? 48 8B F8 48 85 C0 0F 84", 1)
GOLD_POINTER = Signature("gold_pointer", "48 8B 0D ?? ?? ?? ?? 48 85 C9 74 0C 8B 01", 3)

ALL_SIGNATURES = (PLAYER_HEALTH, PLAYER_STAMINA, INVENTORY_BASE, TELEPORT_HOOK, GOLD_POINTER)