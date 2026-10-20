"""Player state model."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PlayerState:
    health: float = 100.0
    stamina: float = 100.0
    gold: int = 0
    godmode: bool = False
    position: tuple[float, float, float] = (0.0, 0.0, 0.0)

    def is_alive(self) -> bool:
        return self.health > 0.0