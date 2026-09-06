# Changelog

All notable changes to the Tech-World AI Context Framework are documented here.

This project uses Semantic Versioning for the public framework specification.

## [1.1.0] - 2026-09-06

### Added

- Canonical Project Standard guidance for turning continuity rules into repository-level operating controls.
- Ready-to-copy `templates/project-standard/` starter pack with project identity, decisions, corrections, handoff, changelog, deployment, backup/rollback, data-identity, migration, testing, release-evidence, and validation files.
- Stable-ID and canonical-record guidance to reduce duplicate records and preserve identity across imports, routing, retries, and integrations.
- Database migration rules that separate schema evolution from ad-hoc production changes.
- Project-level CI validation workflow and zero-dependency validator for required control files and obvious accidental-secret patterns.
- Release-evidence template that preserves the distinction between Implemented, Code-Verified, Runtime-Tested, Deployed, and User-Accepted.

### Compatibility

This is a backward-compatible minor release. Existing v1-compatible implementations remain compatible; the Project Standard is additional recommended guidance and tooling.

## [1.0.0] - 2026-09-06

### Added

- Public `bootstrap.md` entry point.
- Layered context architecture for persistent instructions, public operating guidance, repository `AGENTS.md`, private project records, actual implementation, and current authoritative evidence.
- Reusable `AGENTS.md`, custom-instructions, and project-register templates.
- Documentation for ChatGPT, Codex, continuity, public/private boundaries, and release verification.
- MIT license, security policy, and separate Tech-World trademark/branding notice.
- Initial roadmap issues for validation, automated repository checks, additional sanitized examples, and framework versioning.
- Versioned v1 specification, governance, contribution, support, compatibility, and release process documentation.
- GitHub issue/PR intake templates and repository validation workflow.

### Compatibility

Implementations may describe themselves as `Tech-World AI Context Framework v1 compatible` when they satisfy the mandatory requirements in `docs/specification-v1.md`.

### Branding

Compatibility does not imply endorsement, certification, sponsorship, or official Tech-World status. See `TRADEMARKS.md`.
