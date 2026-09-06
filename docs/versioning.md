# Versioning

The public framework uses Semantic Versioning: `MAJOR.MINOR.PATCH`.

## Patch

Increment PATCH for changes that do not alter compatibility requirements, such as:

- typo fixes;
- clearer wording;
- documentation corrections;
- non-breaking validation improvements;
- additional examples that do not change mandatory behavior.

## Minor

Increment MINOR for backward-compatible additions, such as:

- new optional guidance;
- new templates;
- new validation capabilities;
- new recommended but non-mandatory practices;
- additional compatibility metadata that does not invalidate existing v1 implementations.

## Major

Increment MAJOR when mandatory compatibility behavior changes in a way that can make an existing conforming implementation non-conforming.

Examples include:

- changing correction precedence requirements;
- changing required public/private boundaries;
- adding a new mandatory action-authority rule;
- removing or materially redefining a required context layer;
- changing compatibility language in a breaking way.

## Stable bootstrap URL

The canonical bootstrap URL SHOULD remain stable across releases. The bootstrap may point to newer versioned guidance while preserving the same entry URL.

## Release requirements

A release-worthy change SHOULD include:

- updated `VERSION`;
- `CHANGELOG.md` entry;
- updated specification/docs when applicable;
- validation passing;
- explicit note of compatibility impact.

## Detecting changes

Consumers can track:

- `VERSION` for the current framework version;
- `CHANGELOG.md` for notable changes;
- GitHub releases/tags when published;
- the canonical repository for current specification files.