"""Locates and attaches to the Loftia.exe process."""
from __future__ import annotations

import subprocess
from dataclasses import dataclass


@dataclass
class ProcessAdapter:
    name: str
    pid: int | None = None

    def attach(self) -> bool:
        try:
            out = subprocess.check_output(
                ["tasklist", "/FI", f"IMAGENAME eq {self.name}", "/FO", "CSV", "/NH"],
                text=True,
            )
        except subprocess.CalledProcessError:
            return False
        for line in out.splitlines():
            cols = [c.strip('"') for c in line.split('","')]
            if len(cols) >= 2 and cols[0].lower() == self.name.lower():
                self.pid = int(cols[1])
                return True
        return False

    def detach(self) -> None:
        self.pid = None