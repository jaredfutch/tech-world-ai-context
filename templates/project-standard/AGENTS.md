# AGENTS.md

## Project identity

- Project: see `PROJECT.md`
- Owner: see `PROJECT.md`
- Current source/version: inspect repository and `PROJECT.md`
- Current priority: see `HANDOFF.md`

## Start-of-work protocol

Before substantive edits:

1. read `PROJECT.md`, `DECISIONS.md`, `CORRECTIONS.md`, and `HANDOFF.md`;
2. inspect the actual repository, manifests, lockfiles, configuration, schema, migrations, tests, and deployment files relevant to the task;
3. establish the real current implementation and affected layers;
4. identify protected behavior and data;
5. reproduce or otherwise verify the reported issue when possible.

Do not invent missing project facts.

## Source precedence

1. newest explicit authorized correction/decision;
2. actual repository and observed live state;
3. this `AGENTS.md` and current private project records;
4. public operating guidance;
5. earlier confirmed conversation context;
6. assumptions or inference.

## Change rules

- Fix root causes rather than layering cosmetic patches over broken behavior.
- Preserve unrelated working features, APIs, data, permissions, integrations, and accepted decisions.
- Implement every affected layer, not only the visible UI.
- Use stable IDs and canonical records; do not create duplicate storage merely to support another view or routing lane.
- Use migrations for structural database changes.
- Back up before destructive/high-risk production or data operations.
- Maintain a defined rollback path for releases that can materially affect production.
- Keep secrets out of source, logs, prompts, examples, screenshots, and release notes.
- Do not perform production, financial, public, destructive, or person-directed actions unless explicitly authorized and the target is resolved.

## Repository-specific commands

Fill from inspection. Never guess.

- Install:
- Build:
- Lint:
- Typecheck:
- Unit tests:
- Integration tests:
- Smoke tests:
- Migration status:
- Migration apply:
- Backup:
- Deploy:
- Rollback:

## Verification

Verify affected functionality as applicable:

- syntax/imports/dependencies;
- build/lint/typecheck;
- routes/APIs/schema/migrations;
- authentication/authorization/tenant isolation;
- validation and invalid-input handling;
- success, denial, failure, retry, duplicate, cancellation, and recovery paths;
- external integrations;
- payments/messaging/consent when present;
- responsive behavior and accessibility;
- runtime/browser/device behavior;
- target-environment configuration without exposing secret values.

Report what passed, failed, or could not be run.

## Status model

`Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted`

Never advance a state without evidence.

## End-of-work protocol

Before handoff:

1. update affected project documentation;
2. update `DECISIONS.md` or `CORRECTIONS.md` when a durable decision/state change occurred;
3. update `HANDOFF.md` with current state, evidence, risks, and next action;
4. record release evidence when deployed;
5. state what remains unverified or unaccepted.
