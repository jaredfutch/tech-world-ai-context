# Tech-World Project Standard

The Project Standard turns the framework's continuity principles into a repeatable repository operating model for real software projects.

It is intentionally stack-neutral. A template must not guess whether a project uses PHP, Python, Node, MySQL, Postgres, Docker, cPanel, AWS, or another stack. Each repository records its actual commands, environments, integrations, risks, and deployment method after inspection.

## Relationship to the framework

The AI Context Framework controls how context is loaded and reconciled. The Project Standard controls how a repository records its current state and how changes move from request to accepted release.

Use the following precedence for project work:

1. newest explicit user or authorized stakeholder correction/decision;
2. current authoritative artifact or observed live state;
3. repository `AGENTS.md` and current private project records;
4. public framework guidance;
5. earlier confirmed conversation context;
6. estimates, assumptions, or external inference.

## Canonical project control files

A substantial project SHOULD maintain:

- `AGENTS.md` — repository-specific operating and verification instructions;
- `PROJECT.md` — canonical project manifest and current architecture facts;
- `DECISIONS.md` — durable approved decisions;
- `CORRECTIONS.md` — rejected/superseded behavior and downstream effects;
- `HANDOFF.md` — current work state and next action;
- `CHANGELOG.md` — release-facing change history;
- `docs/DEPLOYMENT.md` — actual environment, deploy, verification, and release procedure;
- `docs/BACKUP-ROLLBACK.md` — backup scope, restore procedure, and rollback boundary;
- `docs/DATA-IDENTITY.md` — stable-ID, canonical-record, idempotency, and deduplication rules;
- `database/migrations/` — append-only structural data changes;
- `tests/` — project-specific test organization and required checks;
- `releases/` — deployment/release evidence;
- `scripts/validate_project.py` — control-plane integrity check;
- `.github/workflows/verify-project.yml` — CI execution of the project validator.

The ready-to-copy starter is in [`../templates/project-standard/`](../templates/project-standard/README.md).

## Project lifecycle

Use the status chain:

`Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted`

These states are evidence claims, not optimistic labels.

### Requested

The desired change, target project, ownership, and material constraints are understood.

### Implemented

Every affected layer has been changed and the root cause has been addressed. This does not mean tests passed.

### Code-Verified

Applicable static checks, builds, migrations, unit/integration tests, or other repository-defined verification passed.

### Runtime-Tested

The changed behavior was exercised in an appropriate runtime, including important success, failure, denial, retry, duplicate, and recovery paths.

### Deployed

The authorized target environment actually received the intended version, required migrations completed, and post-deploy verification produced evidence.

### User-Accepted

The authorized stakeholder reviewed or otherwise accepted the deployed result. Deployment alone is not acceptance.

## Git and version control

Every meaningful change SHOULD be traceable to a commit. Production releases SHOULD identify the exact commit or immutable release artifact deployed.

Prefer feature/fix branches and reviewable pull requests for substantial changes. Avoid editing production as the only copy of a change. If emergency production edits are unavoidable, reconcile them back into version control immediately and record the divergence.

A repository SHOULD be able to answer:

- what changed;
- why it changed;
- who/what authorized it;
- which commit contains it;
- which database migrations belong to it;
- which checks passed;
- where it was deployed;
- what release was previously known-good;
- how to roll back safely.

## Database migrations

Structural database changes SHOULD be represented by ordered migration files rather than undocumented manual SQL.

Migrations SHOULD be:

- uniquely identified;
- ordered;
- reviewable;
- idempotent where the migration system supports it;
- reversible when practical;
- backed up before destructive or high-risk operations;
- recorded as applied in the target environment.

Never assume a migration ran merely because the code expects the new schema.

## Stable IDs and canonical records

Names, titles, email text, URLs, timestamps, or display labels are not reliable primary identity.

Persist a stable internal identifier for every real entity that must survive edits, imports, retries, merges, or cross-routing. When several sources refer to one real-world item, preserve one canonical record and attach source mappings/tags rather than storing independent duplicates.

Use idempotency keys or equivalent safeguards for actions where retrying could create duplicate invoices, messages, payments, jobs, leads, imports, or webhooks.

See the starter's `docs/DATA-IDENTITY.md`.

## Automated tests

Automated verification SHOULD reflect the real risk of the project rather than a generic checklist alone.

As applicable, cover:

- syntax/build/type checks;
- authentication and authorization;
- tenant/data isolation;
- schema and migrations;
- core create/read/update/delete flows;
- critical business rules;
- invalid input and denial paths;
- duplicates and idempotency;
- external-service failures and retries;
- payments/messaging/consent;
- responsive/accessibility behavior;
- smoke tests of deploy-critical paths.

The exact commands belong in `AGENTS.md` and `PROJECT.md` after repository inspection.

## Deployment logs and release evidence

Each production release SHOULD record at minimum:

- release/version identifier;
- commit or artifact identifier;
- target environment;
- timestamp;
- operator or automation identity;
- backup evidence;
- migrations applied;
- code checks;
- runtime/smoke checks;
- known limitations;
- previous known-good release;
- rollback path;
- user acceptance state.

A release log is evidence of what happened, not proof that unrecorded testing occurred.

## Backups and rollback

Before risky production or data changes, define what must be backed up and how restoration is performed. Code rollback and data rollback are different operations and must not be conflated.

A rollback plan SHOULD state:

- what code version is known-good;
- whether schema rollback is safe;
- which data must be restored instead of migrated backward;
- how uploads/object storage/configuration are handled;
- who is authorized to trigger rollback;
- how the restored runtime will be verified.

## Private/public boundary

The templates in this public repository are sanitized. Populated project files may contain private architecture, customers, schedules, internal URLs, costs, contractual obligations, or other protected details and may therefore belong only in a private repository or other authorized storage.

Never publish credentials, API keys, tokens, customer records, private correspondence, banking data, identity records, live lead data, or confidential source code merely because a template contains a field for project information.

## Adopting the standard

For an existing project:

1. inspect the actual repository and runtime first;
2. copy the starter files into the project;
3. populate architecture and command fields from evidence, not memory;
4. record the current known-good release and deployment method;
5. inventory existing migrations, tests, backups, and rollback capability;
6. add missing controls without breaking working functionality;
7. run the project validator;
8. establish CI;
9. use the release evidence template for the next change;
10. migrate older ad-hoc notes into decisions/corrections only when their status can be verified.

Do not manufacture historical certainty. Unknown historical state should be recorded as unknown until evidence resolves it.
