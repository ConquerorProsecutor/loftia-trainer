"""TOML-based settings loader."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class OverlaySettings:
    theme: str = "dark"
    opacity: float = 0.85
    font_size: int = 14


@dataclass
class Settings:
    process_name: str = "Loftia.exe"
    overlay: OverlaySettings = field(default_factory=OverlaySettings)
    hotkeys_enabled: bool = True
    log_level: str = "INFO"


def load_settings(path: str) -> Settings:
    p = Path(path)
    if not p.exists():
        return Settings()
    data = tomllib.loads(p.read_text(encoding="utf-8"))
    overlay = OverlaySettings(**data.get("overlay", {}))
    return Settings(
        process_name=data.get("process_name", "Loftia.exe"),
        overlay=overlay,
        hotkeys_enabled=data.get("hotkeys_enabled", True),
        log_level=data.get("log_level", "INFO"),
    )