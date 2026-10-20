"""Address math helpers."""
from __future__ import annotations


def ptr(base: int, offsets: list[int]) -> int:
    """Resolve a pointer chain (offsets applied last-to-first)."""
    addr = base
    for off in reversed(offsets):
        addr = addr + off
    return addr


def align(addr: int, size: int = 0x10) -> int:
    return (addr + size - 1) & ~(size - 1)


def hexdump(data: bytes, width: int = 16) -> str:
    lines = []
    for i in range(0, len(data), width):
        chunk = data[i:i + width]
        hexpart = " ".join(f"{b:02X}" for b in chunk)
        lines.append(f"{i:08X}  {hexpart}")
    return "\n".join(lines)