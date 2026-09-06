# Release Process

This document defines the maintainer release checklist for the public framework.

## Before release

1. Confirm the intended version and compatibility impact.
2. Review open issues and pull requests related to the release.
3. Verify `VERSION` matches the intended release.
4. Update `CHANGELOG.md`.
5. Update `docs/specification-v1.md` only when required and preserve backward compatibility within v1.
6. Run repository validation.
7. Check all public files for accidental private or sensitive information.
8. Confirm `LICENSE`, `TRADEMARKS.md`, `SECURITY.md`, and `SUPPORT.md` remain accurate.

## Release evidence

Record:

- version;
- date;
- compatibility impact;
- notable changes;
- validation results;
- known limitations.

## Publish

When GitHub release/tag tooling is available to the maintainer:

1. create a tag matching the version, for example `v1.0.0`;
2. publish release notes based on `CHANGELOG.md`;
3. verify the tag points to the intended commit;
4. confirm the canonical bootstrap and documentation remain reachable.

## After release

- close completed roadmap issues;
- open follow-up issues for known gaps;
- update public examples if necessary;
- avoid silently changing mandatory requirements under an existing released major/minor version.