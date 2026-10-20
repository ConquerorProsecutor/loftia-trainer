"""Console/overlay adapter — replace with ImGui overlay in production."""
from __future__ import annotations

import logging
from dataclasses import dataclass

from loftia_trainer.config.settings import OverlaySettings

log = logging.getLogger("loftia.overlay")


@dataclass
class OverlayAdapter:
    settings: OverlaySettings
    _router: object | None = None

    def bind(self, router) -> None:
        self._router = router

    def loop(self) -> None:
        log.info("overlay up (%s)", self.settings.theme)
        while True:
            try:
                line = input("loftia> ")
            except (EOFError, KeyboardInterrupt):
                break
            if self._router is not None:
                out = self._router.dispatch(line)
                if out:
                    print(out)