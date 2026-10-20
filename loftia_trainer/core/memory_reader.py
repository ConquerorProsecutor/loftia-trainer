"""Thin wrapper around pymem for reading/writing Loftia client memory."""
from __future__ import annotations

import struct
from typing import Optional

import pymem


class MemoryReader:
    def __init__(self, process_adapter) -> None:
        self._proc = process_adapter
        self._pm: Optional[pymem.Pymem] = None

    def bind(self) -> None:
        self._pm = pymem.Pymem(self._proc.name)
        self._proc.pid = self._pm.process_id

    def module_base(self, module: str = "Loftia.exe") -> int:
        assert self._pm is not None
        return pymem.process.module_from_name(self._pm.process_handle, module).lpBaseOfDll

    def read_i32(self, address: int) -> int:
        assert self._pm is not None
        return self._pm.read_int(address)

    def read_f32(self, address: int) -> float:
        assert self._pm is not None
        return self._pm.read_float(address)

    def read_vec3(self, address: int) -> tuple[float, float, float]:
        assert self._pm is not None
        raw = self._pm.read_bytes(address, 12)
        return struct.unpack("<fff", raw)

    def write_i32(self, address: int, value: int) -> None:
        assert self._pm is not None
        self._pm.write_int(address, value)

    def write_f32(self, address: int, value: float) -> None:
        assert self._pm is not None
        self._pm.write_float(address, value)