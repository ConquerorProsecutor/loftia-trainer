# Security Policy

## Scope

`loftia-trainer` is an offline, client-side memory trainer for the Loftia desktop game. It performs reads/writes against the local `Loftia.exe` process only. It does not phone home, does not include network code, and does not ship any anti-cheat bypass.

## Reporting a vulnerability

If you find a security issue in the trainer itself (e.g. unsafe pointer math, arbitrary file write, privilege escalation), please open a private security advisory on GitHub instead of a public issue.

Include:
- Loftia client build number (visible in-game under Settings → About).
- Windows version.
- Steps to reproduce.

## Out of scope

- Reports about the trainer being detectable by anti-cheat — that is expected and documented.
- Reports about in-game bans — use at your own risk.
- Requests for bypasses, spoofers, or HWID changers — not accepted.