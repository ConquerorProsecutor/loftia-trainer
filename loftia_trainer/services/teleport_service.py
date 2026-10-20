"""Waypoint teleport via the position hook signature."""
from __future__ import annotations

from dataclasses import dataclass

from loftia_trainer.core.patterns import TELEPORT_HOOK


@dataclass
class Waypoint:
    name: str
    x: float
    y: float
    z: float


class TeleportService:
    def __init__(self, mem, player) -> None:
        self.mem = mem
        self.player = player
        self.waypoints: dict[str, Waypoint] = {
            "spawn": Waypoint("spawn", 0.0, 1.5, 0.0),
            "market": Waypoint("market", 128.4, 1.5, -64.2),
            "farm": Waypoint("farm", -310.7, 1.5, 220.1),
            "dungeon": Waypoint("dungeon", 512.0, -8.0, 512.0),
        }

    def _hook_addr(self) -> int:
        return self.mem.module_base() + TELEPORT_HOOK.offset

    def teleport(self, wp_name: str) -> bool:
        wp = self.waypoints.get(wp_name)
        if wp is None:
            return False
        base = self._hook_addr()
        self.mem.write_f32(base + 0x00, wp.x)
        self.mem.write_f32(base + 0x04, wp.y)
        self.mem.write_f32(base + 0x08, wp.z)
        return True

    def save_position(self, name: str) -> Waypoint:
        base = self._hook_addr()
        wp = Waypoint(name, self.mem.read_f32(base), self.mem.read_f32(base + 4), self.mem.read_f32(base + 8))
        self.waypoints[name] = wp
        return wp