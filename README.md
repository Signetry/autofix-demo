# signetry-autofix-demo

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

A **deliberately vulnerable** demo target for [Signetry](https://github.com/Signetry/core)'s
governed auto-fix. It exists so you can watch the full loop run end-to-end:

```
signetry scan  →  agent drafts a bounded fix  →  admission pipeline  →
independent verifier  →  earned authority (L2)  →  Ed25519-signed receipt  →
branch-only PR (Signetry never merges)
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
3. Actions → **Signetry auto-fix** → **Run workflow** (pick the agent).

Signetry scans, has the agent draft a parameterized-query fix, runs it through the
admission pipeline, and — if it earns **L2 (branch-PR)** — opens a **branch-only**
PR with the signed receipt committed as `.signetry-receipt.json`. A human merges.

The change contract in [`.signetry/admission.yaml`](.signetry/admission.yaml) allows edits
to `app.py` only, so a correct in-scope fix can earn L2.

Setup details: [signetry-core/docs/AUTOFIX_SETUP.md](https://github.com/Signetry/core/blob/main/docs/AUTOFIX_SETUP.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Note that `app.py`'s SQL injection is the
point of this repo — please don't "fix" it here.

## License

[Apache-2.0](LICENSE). Use it, fork it, ship it commercially — no strings.

This repository is part of Signetry's [open-core model](https://github.com/Signetry/signetry/blob/main/LICENSING.md):
the **integration surface is Apache-2.0** so anyone can add an agent, an editor, or a
CI adapter, while the engine ([`Signetry/core`](https://github.com/Signetry/core)) is
source-available under BUSL-1.1 and converts to Apache-2.0 on 2030-08-31.

Contributions are accepted under the [CLA](CLA.md) — it lets us move a well-built
adapter into the engine later without asking every contributor for permission again.
