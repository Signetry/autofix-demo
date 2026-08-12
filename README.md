# umbra-autofix-demo

> **Copyright (c) 2026 Binay Dalai. All rights reserved.**
> This repository is strictly for viewing and contributing to the original project. You may not use, copy, modify, distribute, or commercialize this code for your own personal or commercial projects without explicit written permission. Only the original author retains the right to use and monetize this project.


A **deliberately vulnerable** demo target for [Umbra](https://github.com/Signetry/core)'s
governed auto-fix. It exists so you can watch the full loop run end-to-end:

```
umbra scan  →  agent drafts a bounded fix  →  admission pipeline  →
independent verifier  →  earned authority (L2)  →  Ed25519-signed receipt  →
branch-only PR (Umbra never merges)
```

> ⚠️ **Intentionally insecure. Do not deploy.** `app.py` contains a real SQL
> injection so the auto-fix has something genuine to remediate.

## Run the governed auto-fix

1. Add your executor key as an Actions secret (bring-your-own-key — it never leaves
   this repo, never reaches the diff/receipt, and is never used to merge):
   - `OPENAI_API_KEY` for `--fix-agent codex-cli`, **or**
   - `ANTHROPIC_API_KEY` (API-tier `sk-ant-…`) for `--fix-agent claude-code`.
2. Settings → Actions → General → Workflow permissions → **Read and write** +
   **Allow GitHub Actions to create and approve pull requests**.
3. Actions → **Umbra auto-fix** → **Run workflow** (pick the agent).

Umbra scans, has the agent draft a parameterized-query fix, runs it through the
admission pipeline, and — if it earns **L2 (branch-PR)** — opens a **branch-only**
PR with the signed receipt committed as `.umbra-receipt.json`. A human merges.

The change contract in [`.umbra/admission.yaml`](.umbra/admission.yaml) allows edits
to `app.py` only, so a correct in-scope fix can earn L2.

Setup details: [umbra-core/docs/AUTOFIX_SETUP.md](https://github.com/Signetry/core/blob/main/docs/AUTOFIX_SETUP.md).
