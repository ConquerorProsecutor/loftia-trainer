"""Thin command router — maps overlay commands to services."""
from __future__ import annotations

from loftia_trainer.services.player_service import PlayerService
from loftia_trainer.services.inventory_service import InventoryService
from loftia_trainer.services.teleport_service import TeleportService


class CommandRouter:
    def __init__(self, player: PlayerService, inventory: InventoryService, teleport: TeleportService) -> None:
        self.player = player
        self.inventory = inventory
        self.teleport = teleport
        self._handlers = {
            "god": self._cmd_god,
            "heal": self._cmd_heal,
            "stamina": self._cmd_stamina,
            "gold": self._cmd_gold,
            "unlock": self._cmd_unlock,
            "dupe": self._cmd_dupe,
            "tp": self._cmd_tp,
            "savepos": self._cmd_savepos,
        }

    def dispatch(self, line: str) -> str:
        parts = line.strip().split()
        if not parts:
            return ""
        cmd, *args = parts
        handler = self._handlers.get(cmd)
        if handler is None:
            return f"unknown command: {cmd}"
        try:
            return handler(*args)
        except Exception as exc:  # noqa: BLE001
            return f"error: {exc}"

    def _cmd_god(self) -> str:
        return f"godmode={'on' if self.player.toggle_godmode() else 'off'}"

    def _cmd_heal(self) -> str:
        self.player.set_health(100.0)
        return "health=100"

    def _cmd_stamina(self) -> str:
        self.player.set_stamina(100.0)
        return "stamina=100"

    def _cmd_gold(self, amount: str) -> str:
        self.player.set_gold(int(amount))
        return f"gold={amount}"

    def _cmd_unlock(self) -> str:
        self.inventory.unlock_all_slots()
        return "slots=unlocked"

    def _cmd_dupe(self, slot: str) -> str:
        self.inventory.duplicate_item(int(slot))
        return f"duped slot={slot}"

    def _cmd_tp(self, name: str) -> str:
        return f"tp={name}:{'ok' if self.teleport.teleport(name) else 'fail'}"

    def _cmd_savepos(self, name: str) -> str:
        wp = self.teleport.save_position(name)
        return f"saved {wp.name} ({wp.x:.1f},{wp.y:.1f},{wp.z:.1f})"