"""Player stats: health, stamina, gold, and god-mode toggle."""
from __future__ import annotations

from loftia_trainer.core.patterns import PLAYER_HEALTH, PLAYER_STAMINA, GOLD_POINTER


class PlayerService:
    def __init__(self, mem, patches) -> None:
        self.mem = mem
        self.patches = patches
        self._godmode = False

    def _resolve(self, sig) -> int:
        base = self.mem.module_base()
        return base + sig.offset

    def set_health(self, value: float) -> None:
        self.mem.write_f32(self._resolve(PLAYER_HEALTH), value)

    def set_stamina(self, value: float) -> None:
        self.mem.write_f32(self._resolve(PLAYER_STAMINA), value)

    def set_gold(self, amount: int) -> None:
        self.mem.write_i32(self._resolve(GOLD_POINTER), amount)

    def toggle_godmode(self) -> bool:
        addr = self._resolve(PLAYER_HEALTH)
        if not self._godmode:
            self.patches.apply(addr, b"\x74\x05", b"\xEB\x05", label="godmode")
            self._godmode = True
        else:
            self.patches.revert(addr)
            self._godmode = False
        return self._godmode