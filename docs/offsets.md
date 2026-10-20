# Loftia Client Offsets

Current target build: **2026.03**

| Signature        | Purpose                    | Notes                              |
|------------------|----------------------------|------------------------------------|
| `PLAYER_HEALTH`  | Health float               | God-mode patch at `+0x??`          |
| `PLAYER_STAMINA` | Stamina float              | Sprint stamina                     |
| `INVENTORY_BASE` | Inventory slot array       | 60 slots × 0x10 stride             |
| `TELEPORT_HOOK`  | Position write hook        | x/y/z packed as 3 floats           |
| `GOLD_POINTER`   | Gold counter (i32)         | Patched after each transaction     |

If the game updates, run `python scripts/dump_signatures.py` and diff the hexdump against the previous build. Update `loftia_trainer/core/patterns.py` and bump the build tag with `python scripts/update_offsets.py 2026.04`.