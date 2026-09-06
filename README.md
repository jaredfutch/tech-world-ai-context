# Tech-World AI Context Framework

**Current framework version: 1.1.0**

A practical, layered context architecture for long-running AI-assisted work across ChatGPT, Codex, repositories, projects, files, and connected tools.

Created and maintained by **Tech-World LLC**.

## Why this exists

AI assistants are useful in a single conversation, but substantial work rarely lives in one conversation. Real projects accumulate decisions, corrections, repositories, files, deployment rules, private records, and changing external facts. Repeating all of that context manually is slow and error-prone.

This framework uses a small stable pointer plus layered project context so an assistant can load the right guidance for the task without treating one giant prompt as the source of truth.

```text
Current request
    ↓
Custom Instructions / persistent pointer
    ↓
Public bootstrap.md
    ↓
Operating guidance
    ↓
Project / repository AGENTS.md
    ↓
Private project records and current files
    ↓
Actual implementation / live state
    ↓
Current authoritative external evidence when needed
```

The goal is not unlimited memory. The goal is **controlled continuity**: load the right context, preserve confirmed decisions, separate unrelated work, resolve conflicts consistently, and verify what actually happened.

## Official upstream and specification

This repository is the canonical public upstream for the **Tech-World AI Context Framework**.

The formal v1 compatibility requirements are in [`docs/specification-v1.md`](docs/specification-v1.md).

Third-party implementations that satisfy those mandatory requirements may accurately state:

> Compatible with Tech-World AI Context Framework v1

Compatibility does **not** imply endorsement, sponsorship, certification, affiliation, or official Tech-World status. See [`docs/compatibility.md`](docs/compatibility.md), [`GOVERNANCE.md`](GOVERNANCE.md), and [`TRADEMARKS.md`](TRADEMARKS.md).

## Core principles

- The current request comes first.
- Stable operating guidance can live behind a public bootstrap URL.
- Repository-specific instructions belong close to the code, typically in `AGENTS.md`.
- Private project records stay private.
- The newest explicit correction supersedes rejected earlier information.
- Current artifacts and observed system state outrank stale summaries.
- Proposed, implemented, tested, deployed, and accepted are different states.
- External actions require explicit authorization and resolved targets.
- Changeable facts should be re-verified from current authoritative sources.
- Root causes should be fixed instead of accumulating cosmetic patches.

## What is included

- `bootstrap.md` — sanitized example of a stable public entry point.
- `AGENTS.md` — repository-level instructions for this framework itself.
- `VERSION` and `CHANGELOG.md` — framework version and release history.
- `GOVERNANCE.md` — canonical-upstream and maintainer decision rules.
- `CONTRIBUTING.md` — contribution expectations.
- `SUPPORT.md` — community and commercial-support boundaries.
- `templates/AGENTS.template.md` — reusable project-specific agent instructions.
- `templates/custom-instructions.example.md` — compact persistent pointer for ChatGPT-style custom instructions.
- `templates/project-register.template.md` — private project-register starter.
- `templates/project-standard/` — ready-to-copy repository control plane for substantial software projects.
- `docs/project-standard.md` — Git/version control, project manifests, stable IDs, migrations, tests, deployment evidence, backups, rollback, and handoff guidance.
- `docs/specification-v1.md` — mandatory v1 compatibility requirements.
- `docs/compatibility.md` — permitted compatibility language.
- `docs/versioning.md` and `docs/release-process.md` — semantic versioning and release governance.
- `docs/architecture.md` — context layers, precedence, and lifecycle.
- `docs/setup-chatgpt.md` — how to use a bootstrap URL with persistent custom instructions.
- `docs/setup-codex.md` — how to pair the bootstrap with repository guidance.
- `docs/public-private-boundary.md` — what belongs in public context vs private records.
- `docs/continuity-model.md` — correction retention, source-of-truth control, and status semantics.
- `docs/release-gate.md` — verification model for software changes.
- `examples/sample-project/AGENTS.md` — a sanitized project example.
- `.github/workflows/validate.yml` — automated repository integrity checks.

## Quick start

### 1. Host a stable bootstrap

Publish a small Markdown file at a URL you control. Keep it stable even as the linked operating documents evolve.

Example:

```text
https://example.com/ai-context/bootstrap.md
```

### 2. Point your persistent instructions to it

Keep the persistent prompt compact. It should tell the assistant when to retrieve the bootstrap, how to treat it, and what to do if it is unavailable.

See [`templates/custom-instructions.example.md`](templates/custom-instructions.example.md).

### 3. Put repository rules in `AGENTS.md`

Each substantial repository should document its real stack, protected behavior, build/test commands, deployment boundary, known risks, and project-specific verification requirements.

See [`templates/AGENTS.template.md`](templates/AGENTS.template.md).

### 4. Adopt the Project Standard for substantial software

For projects that need durable versioning, migrations, testing, deployment evidence, stable IDs, backups, rollback, decisions, corrections, and handoff state, copy the [`templates/project-standard/`](templates/project-standard/README.md) starter into the project repository and populate it from current evidence.

See [`docs/project-standard.md`](docs/project-standard.md).

### 5. Keep private project state private

Customer data, credentials, contracts, schedules, internal financial data, private correspondence, and proprietary project facts should not be placed in a public bootstrap tree. Store them in authorized private project files, repositories, connected systems, or other access-controlled sources.

### 6. Reconcile instead of blindly merging

A useful precedence model is:

1. Newest explicit user correction, approval, rejection, or decision.
2. Current authoritative artifact or directly observed live state.
3. Current private project/repository instructions.
4. Current public operating guidance.
5. Earlier confirmed conversation context.
6. Estimates, assumptions, or external inferences.

Platform, safety, legal, and access-control requirements still apply.

## Reference implementation

Tech-World LLC maintains a live public bootstrap used as an implementation of this pattern:

**https://tech-worldllc.com/ai-context/bootstrap.md**

The live implementation intentionally contains only public operating guidance. This repository does **not** publish Tech-World private project records, customer records, credentials, live lead data, financial account data, confidential contracts, or other sensitive operational data.

## Status model for substantial software work

Use precise state labels:

```text
Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted
```

Do not collapse these into “done.” A build can be implemented without being runtime-tested, and deployed without being user-accepted.

## New-project lifecycle

For a brand-new project:

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

## Validation

The repository includes a zero-dependency validator that checks required framework files, semantic version formatting, repository-relative Markdown links, and a small set of obvious accidental-secret patterns.

Run locally:

```bash
python scripts/validate_repo.py
```

The Project Standard starter also includes its own zero-dependency validator and GitHub Actions workflow. After copying the starter into a project, run:

```bash
python scripts/validate_project.py
```

GitHub Actions can run the same control-plane check on pull requests and pushes. Project-specific build, lint, test, migration, and smoke commands must still be added from the real repository rather than guessed.

This is defense-in-depth. Automated checks do not replace the requirement to keep private data out of the public repository.

## Contributions and support

Issues and pull requests are welcome. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

Use the GitHub issue forms for reproducible bugs, backward-compatible feature ideas, or formal specification-change proposals. Support boundaries are documented in [`SUPPORT.md`](SUPPORT.md).

Open-source availability does not create an SLA or a promise of individual implementation support. Tech-World LLC may separately offer commercial implementation, migration, integration, or private-deployment services.

## Releases and compatibility

The framework uses Semantic Versioning. See [`docs/versioning.md`](docs/versioning.md) and [`CHANGELOG.md`](CHANGELOG.md).

Breaking changes to mandatory compatibility requirements require a new major version. The public bootstrap URL should remain stable even as the framework evolves.

## Security model

Public context should describe **how to work**, not reveal private facts needed only for a specific engagement. See [`docs/public-private-boundary.md`](docs/public-private-boundary.md).

If you discover a security issue in this repository, do not post credentials, tokens, customer data, or exploit details in a public issue. See [`SECURITY.md`](SECURITY.md).

## License and use

The framework, templates, documentation, and examples are licensed under the **MIT License**. You may use them personally or commercially, modify them, fork them, redistribute them, and build products or services from them, subject to the MIT License terms. See [`LICENSE`](LICENSE).

The MIT License does **not** grant permission to present a third-party or modified implementation as an official Tech-World product or to imply Tech-World sponsorship, endorsement, certification, or affiliation. Tech-World names, logos, and branding remain separate from the open-source license. See [`TRADEMARKS.md`](TRADEMARKS.md).

In short: **use the framework freely; use your own branding; do not impersonate Tech-World or imply endorsement.**

---

This project is an operational pattern, not a mechanism for bypassing platform instructions, repository permissions, privacy controls, or security boundaries.