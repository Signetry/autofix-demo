# Contributing

`signetry-autofix-demo` is **[Apache-2.0](LICENSE)**. Use it, fork it, run it in your
own CI, build a paid product on top of it — no permission needed, no strings.

This repo is part of Signetry's
[open-core model](https://github.com/Signetry/signetry/blob/main/LICENSING.md): the
integration surface is Apache-2.0, while the engine
([`Signetry/core`](https://github.com/Signetry/core)) is source-available under
BUSL-1.1 and converts to Apache-2.0 on 2030-08-31.

## What this repo is (read this before you open a PR)

It is a **deliberately vulnerable demo target**, not a library. `app.py` contains a
real SQL injection so Signetry's governed auto-fix has something genuine to remediate.

> ⚠️ **Please do not "fix" the SQL injection in `app.py`.** Removing it removes the
> point of the repo. A PR that patches it will be closed.

The moving parts:

| Path | What it is |
| --- | --- |
| `app.py` | The vulnerable Flask endpoint the demo scans and fixes |
| `.signetry/admission.yaml` | The change contract: what an agent is allowed to touch |
| `.github/workflows/signetry-autofix.yml` | The end-to-end demo (scan → fix → branch-only PR + receipt) |
| `.github/workflows/cla.yml` | The CLA gate |

## Getting started

There is no test suite, linter, or dependency manifest in this repo — deliberately, so
the demo stays a single readable file. The only real check is the workflow itself:

1. **Fork** this repo (the workflow needs to push a branch and open a PR).
2. Add an executor secret in your fork — `OPENAI_API_KEY` (for `--fix-agent
   codex-cli`) or `ANTHROPIC_API_KEY` (for `--fix-agent claude-code`).
3. Settings → Actions → General → Workflow permissions → **Read and write** +
   **Allow GitHub Actions to create and approve pull requests**.
4. Actions → **Signetry auto-fix** → **Run workflow**.

Full setup notes:
[signetry-core/docs/AUTOFIX_SETUP.md](https://github.com/Signetry/core/blob/main/docs/AUTOFIX_SETUP.md).

If you change `app.py`, keep it valid on **Python 3.12** — that is the version the
workflow's `actions/setup-python` step installs.

If you change `.signetry/admission.yaml`, say in the PR description what the demo now
proves. Today it allows edits to `app.py` only, forbids `.github/**` and `.signetry/**`,
and caps a fix at 5 files / 80 diff lines; widening any of those changes the claim the
demo is making about bounded authority.

Good contributions here look like: a second realistic vulnerability class to remediate,
clearer setup docs, or a workflow fix for a runner behaviour that has changed.

## Signing the CLA (required before merge)

This is enforced by a bot. When you open a pull request, the **CLA Assistant** check
will ask you to sign the [Contributor License Agreement](CLA.md). Reply on the PR
with exactly:

```
I have read the CLA Document and I hereby sign the CLA
```

Your acceptance is recorded in `signatures/cla.json`. A PR **cannot be merged** until
the CLA is signed.

**Why an Apache-2.0 project still asks for a CLA.** Signetry is open core, and the line
between the Apache-2.0 integration surface and the BUSL-1.1 engine is not permanent — a
well-built adapter that starts life here may later belong inside
[`Signetry/core`](https://github.com/Signetry/core). The CLA gives the maintainer the
rights to move code across that line, and to relicense it (including to Apache-2.0 when
the engine converts in 2030), without having to track down every past contributor for
permission. It is a relicensing tool, not a claim on what you may do with the code:
your contribution ships under Apache-2.0 like everything else here, so you keep every
right the licence gives anyone, commercial use included.

## Credit

Contributors are **acknowledged** in [CONTRIBUTORS.md](CONTRIBUTORS.md), the Git
history, and release notes. Attribution is separate from trademark: you may freely say
you contributed, but please don't use the Signetry name or the maintainer's name to
endorse or promote your own product. See the "Recognition of Contributors" clause in
[CLA.md](CLA.md).

## Conduct and security

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).

Do **not** open a public issue for a security vulnerability in Signetry itself — see
[SECURITY.md](SECURITY.md). (The SQL injection in `app.py` is not a vulnerability
report; it is the fixture.)
