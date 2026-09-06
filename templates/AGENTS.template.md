# AGENTS.md

## Project identity

- Owner: <owner or organization>
- Product/project: <name>
- Role: <internal product / client project / collaboration / personal project>
- Current source/version: <commit, release, archive, or UNKNOWN — inspect first>
- Current priority: <one concise statement>

## Protected behavior

List features, contracts, workflows, APIs, data boundaries, branding, permissions, and user journeys that must not be broken.

## Source of truth

1. Current explicit user decision/correction.
2. Actual repository and observed runtime state.
3. This `AGENTS.md` and project documentation.
4. Authorized private project records.
5. Public operating guidance.
6. Older summaries or assumptions.

Do not invent missing repository facts.

## Architecture facts

Fill these from inspection, not guesses:

- Runtime/framework:
- Entry point:
- Database/storage:
- Authentication:
- Authorization/roles:
- External integrations:
- Build command:
- Test command:
- Lint/typecheck command:
- Migration method:
- Deployment target:
- Rollback method:

## Change rules

- Trace defects to the root source.
- Preserve unrelated working features and data.
- Implement every affected layer, not only the visible UI.
- Use migrations/backups/rollback where data or production state can change.
- Keep secrets out of logs, prompts, examples, commits, and screenshots.
- Do not perform production, financial, public, destructive, or person-directed actions unless explicitly authorized.

## Verification

For affected functionality, verify as applicable:

- syntax/imports/dependencies;
- routes/APIs/schema/data migrations;
- authentication, authorization, and tenant boundaries;
- validation and invalid-input handling;
- success, denial, failure, retry, duplicate, cancellation, and recovery paths;
- payments/messaging/consent when present;
- responsive behavior and accessibility;
- lint/typecheck/tests/build;
- runtime/browser/device behavior;
- production configuration without exposing secret values.

Report precisely what passed, failed, or could not be run.

## Status model

Use:

`Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted`

Never skip a state merely to call the project complete.

## Known risks / open decisions

- <risk or unresolved decision>

## Current next action

- <next concrete action>