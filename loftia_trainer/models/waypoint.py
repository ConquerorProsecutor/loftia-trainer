"""Waypoint model — mirrors teleport_service.Waypoint for persistence."""
from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class WaypointRecord:
    name: str
    x: float
    y: float
    z: float

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "WaypointRecord":
        return cls(**data)