"""Global hotkey registration via keyboard library."""
from __future__ import annotations

import logging

import keyboard

log = logging.getLogger("loftia.hotkeys")

DEFAULT_BINDS = {
    "f1": "god",
    "f2": "heal",
    "f3": "unlock",
    "f4": "tp market",
    "f5": "tp farm",
}


def install(router, binds: dict[str, str] | None = None) -> None:
    bind_map = binds or DEFAULT_BINDS
    for key, cmd in bind_map.items():
        keyboard.add_hotkey(key, lambda c=cmd: log.info(router.dispatch(c)))
        log.debug("bound %s -> %s", key, cmd)