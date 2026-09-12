# Private Project Register Template

> Keep populated project records private. Never publish credentials, customer data, private schedules, contracts, financial-account data, confidential correspondence, health records, or production secrets in a public framework repository.

For machine-readable implementations, use the public schemas in `schemas/` and keep the populated JSON in an access-controlled private store.

## Canonical project identity

- Project ID: permanent lowercase stable ID
- Canonical name:
- Aliases:
- Parent project ID, if any:
- Owner:
- Tech-World role:
- Repository/source:
- Status: active / paused / blocked / completed / canceled / archived
- Stage:
- Current version/commit/archive:
- Next action:

A rename should update the canonical display name or aliases; it should not create a duplicate project ID.

## State timestamps

- Created at:
- Last activity at:
- Last changed at:
- Last verified at:

Do not treat these timestamps as interchangeable.

## Scope

- Included:
- Excluded:
- Dependencies:
- Acceptance criteria:

## Confirmed decisions

| Date | Decision | Source/evidence | Supersedes |
| --- | --- | --- | --- |
| YYYY-MM-DD |  |  |  |

## Corrections

| Date | What was wrong | Replacement | Downstream items to recheck |
| --- | --- | --- | --- |
| YYYY-MM-DD |  |  |  |

## Risks and open work

- Risk:
- Impact:
- Mitigation:
- Owner:

- Open work:
- Next verification:

## Verification state

- Requested:
- Implemented:
- Code-Verified:
- Runtime-Tested:
- Deployed:
- User-Accepted:

## Evidence and provenance

Reference authorized repositories, current files, tests, screenshots, logs, contracts, dashboards, or connected records. Store source references and verification timestamps; do not copy secrets merely for convenience.

## Historical events

Keep material project history append-only. When current state changes, update the current state record and append a new event rather than rewriting older events to match the new reality.
