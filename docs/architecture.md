# Architecture

```
loftia_trainer/
├── bootstrap.py         # wire services + adapters
├── core/                # memory layer
│   ├── memory_reader.py
│   ├── patch_engine.py
│   └── patterns.py
├── services/            # business logic
│   ├── player_service.py
│   ├── inventory_service.py
│   └── teleport_service.py
├── handlers/            # thin controllers
│   ├── command_router.py
│   └── hotkey_handler.py
├── adapters/            # platform glue
│   ├── process_adapter.py
│   └── overlay_adapter.py
├── models/              # dataclasses
├── config/              # toml + loader
└── utils/               # helpers
```

Handlers never touch memory directly; they call into `services/`. Services use `core/` primitives (`MemoryReader`, `PatchEngine`) and never know about the overlay. Adapters are the only place Windows-specific code lives.