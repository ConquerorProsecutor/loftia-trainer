"""Utility to dump candidate AOB signatures from a running Loftia.exe."""
from __future__ import annotations

import argparse

from loftia_trainer.adapters.process_adapter import ProcessAdapter
from loftia_trainer.core.memory_reader import MemoryReader
from loftia_trainer.utils.logger import setup


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--module", default="Loftia.exe")
    ap.add_argument("--len", type=int, default=64)
    args = ap.parse_args()

    log = setup("DEBUG")
    proc = ProcessAdapter("Loftia.exe")
    if not proc.attach():
        log.error("Loftia.exe not running")
        return
    mem = MemoryReader(proc)
    mem.bind()
    base = mem.module_base(args.module)
    log.info("module base: 0x%X", base)
    head = mem._pm.read_bytes(base, args.len)
    from loftia_trainer.utils.address import hexdump
    print(hexdump(head))


if __name__ == "__main__":
    main()