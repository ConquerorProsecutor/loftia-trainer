# Contributing to loftia-trainer

Thanks for helping improve the Loftia Trainer.

## Ground rules

- This is a hobbyist, educational modding project. Do not use it to grief other players or to violate Loftia's Terms of Service.
- Every PR that touches `loftia_trainer/core/patterns.py` must include updated AOB signatures for the current Loftia client build.
- New services go in `loftia_trainer/services/`; keep handlers in `loftia_trainer/handlers/` thin.
- Do not commit memory dumps or crash logs — they are gitignored for a reason.

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m loftia_trainer
```

## Testing

```bash
pytest -q
```

## Style

- Python 3.11+, type hints on public APIs.
- Prefer dataclasses over plain dicts for models.
- Keep `loftia_trainer/adapters/` platform-specific — Windows only for now.