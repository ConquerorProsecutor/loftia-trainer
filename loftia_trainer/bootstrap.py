"""Application bootstrap: wires services, adapters and the overlay together."""
from __future__ import annotations

import logging
import sys

from loftia_trainer.core.memory_reader import MemoryReader
from loftia_trainer.core.patch_engine import PatchEngine
from loftia_trainer.services.player_service import PlayerService
from loftia_trainer.services.inventory_service import InventoryService
from loftia_trainer.services.teleport_service import TeleportService
from loftia_trainer.handlers.command_router import CommandRouter
from loftia_trainer.adapters.process_adapter import ProcessAdapter
from loftia_trainer.adapters.overlay_adapter import OverlayAdapter
from loftia_trainer.config.settings import load_settings


log = logging.getLogger("loftia.trainer")


class TrainerApp:
    def __init__(self, config_path: str = "config/trainer.toml") -> None:
        self.settings = load_settings(config_path)
        self.proc = ProcessAdapter(self.settings.process_name)
        self.mem = MemoryReader(self.proc)
        self.patches = PatchEngine(self.mem)

        self.player = PlayerService(self.mem, self.patches)
        self.inventory = InventoryService(self.mem, self.patches)
        self.teleport = TeleportService(self.mem, self.player)

        self.overlay = OverlayAdapter(self.settings.overlay)
        self.router = CommandRouter(self.player, self.inventory, self.teleport)

    def run(self) -> int:
        if not self.proc.attach():
            log.error("could not attach to %s", self.settings.process_name)
            return 1
        self.overlay.bind(self.router)
        log.info("loftia-trainer attached pid=%s", self.proc.pid)
        try:
            self.overlay.loop()
        finally:
            self.proc.detach()
        return 0


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    sys.exit(TrainerApp().run())