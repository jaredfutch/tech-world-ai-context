# AGENTS.md — Sample Project

## Identity

- Owner: Example Organization
- Product type: Multi-user web application
- Current source/version: inspect the repository before work
- Current priority: preserve existing behavior while implementing explicitly requested changes

## Protected behavior

- Existing authentication and role boundaries must continue working.
- Tenant data must remain isolated.
- Existing API contracts must not be changed casually.
- Production data must not be modified during tests.
- External email, payment, and destructive actions must remain disabled in test environments unless specifically configured for safe test targets.

## Repository facts

Fill these after inspection:

- Framework: UNKNOWN
- Database: UNKNOWN
- Auth provider: UNKNOWN
- Build command: UNKNOWN
- Test command: UNKNOWN
- Deployment target: UNKNOWN

Do not guess these values from previous projects.

## Implementation workflow

1. Inspect manifests, routes, schema, auth/roles, integrations, tests, and deployment configuration.
2. Identify the exact affected layers.
3. Trace the root cause or requested behavior through those layers.
4. Preserve unrelated features and data.
5. Implement the smallest coherent fix/change.
6. Run discovered repository checks.
7. Exercise relevant runtime success/failure/permission/retry paths.
8. Record exact status and limitations.

## Required verification

- Verify authorized user succeeds.
- Verify unauthorized user is denied.
- Verify one tenant cannot access another tenant's records.
- Verify invalid and duplicate submissions fail safely.
- Verify retries do not duplicate side effects.
- Verify external messages/payments are routed only to approved test destinations during testing.
- Verify responsive UI for affected screens.

## Status

Use:

`Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted`

Do not report later stages without evidence.