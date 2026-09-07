# Tech-World AI Context Framework

**Controlled continuity for ChatGPT, Codex, and AI coding agents.**

[![Version](https://img.shields.io/badge/version-1.1.0-blue)](VERSION)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A layered, versioned, open-source framework for keeping long-running AI-assisted work grounded in current project truth instead of relying on conversational memory alone.

> **Conversation history tells us what the project is supposed to be.**  
> **Current artifacts tell us what the project actually is.**  
> **Verification tells us what actually works.**

**Current framework version: 1.1.0**

Created and maintained by **Tech-World LLC**.

## Why this exists

AI assistants can be excellent inside one conversation. Real projects are harder: they accumulate decisions, corrections, repositories, database changes, deployment state, integrations, private records, and changing external facts.

The failure mode is subtle: an assistant may correctly remember the *intent* of a project while being wrong about the *current implementation*.

The Tech-World AI Context Framework separates those layers and defines how to reconcile them.

```text
Current request
    ↓
Persistent instructions / stable bootstrap
    ↓
Repository AGENTS.md
    ↓
Private project records
    ↓
Current source + schema + configuration
    ↓
Implementation
    ↓
Verification evidence
    ↓
Deployment state
    ↓
User acceptance
```

The goal is not unlimited memory. The goal is **controlled continuity**.

## See it in one minute

Read the [one-minute demo](docs/one-minute-demo.md) for a concrete before/after example of how stale conversational context can create duplicate or incorrect repairs—and how the framework changes the workflow.

For substantial software projects, see the [Project Standard](docs/project-standard.md), which adds project manifests, decisions, corrections, handoffs, stable IDs, migrations, tests, deployment evidence, backups, and rollback guidance.

## The key operating rule

When history and reality differ, do not silently blend them.

A practical precedence model is:

1. Newest explicit user correction, approval, rejection, or decision.
2. Current authoritative artifact or directly observed live state.
3. Current private project/repository instructions.
4. Current public operating guidance.
5. Earlier confirmed conversation context.
6. Estimates, assumptions, or external inferences.

Platform, safety, legal, privacy, and access-control requirements still apply.

## Status is evidence, not optimism

Substantial software work uses this progression:

```text
Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted
```

A code edit is not a deployment. A deployment is not acceptance. Missing evidence remains missing rather than being upgraded to “done.”

## What is included

- `bootstrap.md` — sanitized stable public entry point.
- `AGENTS.md` — repository-level instructions for this framework itself.
- `VERSION` and `CHANGELOG.md` — framework version and release history.
- `GOVERNANCE.md` — canonical-upstream and maintainer decision rules.
- `CONTRIBUTING.md` — contribution expectations.
- `SUPPORT.md` — community and commercial-support boundaries.
- `templates/AGENTS.template.md` — reusable project-specific agent instructions.
- `templates/custom-instructions.example.md` — compact persistent pointer for ChatGPT-style custom instructions.
- `templates/project-register.template.md` — private project-register starter.
- `templates/project-standard/` — ready-to-copy project control plane for substantial software.
- `docs/project-standard.md` — version control, manifests, IDs, migrations, tests, deployment evidence, backups, rollback, and handoff guidance.
- `docs/one-minute-demo.md` — concrete explanation of the framework in practice.
- `docs/launch-kit.md` — public promotion and discussion starter copy.
- `docs/specification-v1.md` — mandatory v1 compatibility requirements.
- `docs/compatibility.md` — permitted compatibility language.
- `docs/versioning.md` and `docs/release-process.md` — semantic versioning and release governance.
- `docs/architecture.md` — context layers, precedence, and lifecycle.
- `docs/setup-chatgpt.md` — using a bootstrap URL with persistent custom instructions.
- `docs/setup-codex.md` — pairing the bootstrap with repository guidance.
- `docs/public-private-boundary.md` — what belongs in public context vs private records.
- `docs/continuity-model.md` — correction retention, source-of-truth control, and status semantics.
- `docs/release-gate.md` — verification model for software changes.
- `examples/sample-project/AGENTS.md` — sanitized project example.
- `.github/workflows/validate.yml` — automated repository integrity checks.
- `.github/workflows/release.yml` — automated GitHub release publication from `VERSION`.

## Quick start

### 1. Host a stable bootstrap

Publish a small Markdown file at a URL you control. Keep the URL stable even as linked operating documents evolve.

```text
https://example.com/ai-context/bootstrap.md
```

### 2. Point persistent instructions to it

Keep the persistent prompt compact. Tell the assistant when to retrieve the bootstrap, how to treat it, and what to do if it is unavailable.

See [`templates/custom-instructions.example.md`](templates/custom-instructions.example.md).

### 3. Put repository rules next to the code

Each substantial repository should document its real stack, protected behavior, build/test commands, deployment boundary, known risks, and project-specific verification requirements in `AGENTS.md`.

See [`templates/AGENTS.template.md`](templates/AGENTS.template.md).

### 4. Adopt the Project Standard when the project is substantial

Copy [`templates/project-standard/`](templates/project-standard/README.md) into the project repository and populate it from current evidence rather than guesses.

### 5. Keep private project state private

Customer data, credentials, contracts, schedules, internal financial data, private correspondence, and proprietary project facts should not be placed in a public bootstrap tree. Store them only in authorized private project files, repositories, connected systems, or other access-controlled sources.

## Reference implementation

Tech-World LLC maintains a live public bootstrap implementing this pattern:

**https://tech-worldllc.com/ai-context/bootstrap.md**

The live implementation intentionally contains only public operating guidance. This repository does **not** publish Tech-World private project records, customer records, credentials, live lead data, financial account data, confidential contracts, or other sensitive operational data.

## Official upstream and specification

This repository is the canonical public upstream for the **Tech-World AI Context Framework**.

The formal v1 compatibility requirements are in [`docs/specification-v1.md`](docs/specification-v1.md).

Third-party implementations that satisfy those mandatory requirements may accurately state:

> Compatible with Tech-World AI Context Framework v1

Compatibility does **not** imply endorsement, sponsorship, certification, affiliation, or official Tech-World status. See [`docs/compatibility.md`](docs/compatibility.md), [`GOVERNANCE.md`](GOVERNANCE.md), and [`TRADEMARKS.md`](TRADEMARKS.md).

## Validation

Run the zero-dependency repository validator locally:

```bash
python scripts/validate_repo.py
```

After copying the Project Standard into a project, run:

```bash
python scripts/validate_project.py
```

GitHub Actions runs framework validation on pushes and pull requests. Project-specific build, lint, test, migration, and smoke commands must still come from the real project repository rather than being invented by the generic framework.

Automated checks are defense-in-depth. They do not replace the requirement to keep private data out of public repositories.

## New-project lifecycle

```text
Request
  → load bootstrap guidance
  → inspect/create repository
  → establish architecture and boundaries
  → create project AGENTS.md / Project Standard controls
  → implement
  → verify
  → deploy only when authorized
  → record decisions/corrections
  → record release evidence
  → update project status
```

## Contributions and support

Issues and pull requests are welcome. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

Use the GitHub issue forms for reproducible bugs, backward-compatible feature ideas, or formal specification-change proposals. Support boundaries are documented in [`SUPPORT.md`](SUPPORT.md).

Open-source availability does not create an SLA or a promise of individual implementation support. Tech-World LLC may separately offer commercial implementation, migration, integration, or private-deployment services.

## Promotion and discussion

If you want to discuss or share the framework, [`docs/launch-kit.md`](docs/launch-kit.md) contains concise descriptions, discussion prompts, and launch-post starters. The strongest introduction is the [one-minute demo](docs/one-minute-demo.md), not just the repository root.

## Releases and compatibility

The framework uses Semantic Versioning. See [`docs/versioning.md`](docs/versioning.md) and [`CHANGELOG.md`](CHANGELOG.md).

A release workflow validates the repository and publishes the matching GitHub release when `VERSION` advances on `main`. Breaking changes to mandatory compatibility behavior require a new major version.

## Security model

Public context should describe **how to work**, not reveal private facts needed only for a specific engagement. See [`docs/public-private-boundary.md`](docs/public-private-boundary.md).

If you discover a security issue, do not post credentials, tokens, customer data, or exploit details in a public issue. See [`SECURITY.md`](SECURITY.md).

## License and use

The framework, templates, documentation, and examples are licensed under the **MIT License**. You may use them personally or commercially, modify them, fork them, redistribute them, and build products or services from them, subject to the MIT License terms. See [`LICENSE`](LICENSE).

The MIT License does **not** grant permission to present a third-party or modified implementation as an official Tech-World product or to imply Tech-World sponsorship, endorsement, certification, or affiliation. Tech-World names, logos, and branding remain separate from the open-source license. See [`TRADEMARKS.md`](TRADEMARKS.md).

In short: **use the framework freely; use your own branding; do not impersonate Tech-World or imply endorsement.**

---

This project is an operational pattern, not a mechanism for bypassing platform instructions, repository permissions, privacy controls, or security boundaries.
