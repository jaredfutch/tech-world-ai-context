# PROJECT.md

> Canonical project manifest. Populate from current repository/runtime evidence. Keep private if populated values are sensitive.

## Identity

- Project ID:
- Project name:
- Owner:
- Operating role: internal product / client project / collaboration / other
- Repository:
- Default branch:
- Current version/release:
- Current commit/artifact:
- Last known-good release:
- Current status: Requested / Implemented / Code-Verified / Runtime-Tested / Deployed / User-Accepted
- Current priority:
- Next action:

## Environments

| Environment | Purpose | Source/ref | Deployment target | Data boundary | Status |
| --- | --- | --- | --- | --- | --- |
| Development |  |  |  |  |  |
| Staging |  |  |  |  |  |
| Production |  |  |  |  |  |

## Architecture

- Runtime/framework:
- Entry point(s):
- Package/dependency manifests:
- Database/storage:
- Authentication:
- Authorization/roles:
- Tenant/isolation model:
- File/object storage:
- Background jobs/cron/queues:
- External integrations:
- Observability/logging:
- Hosting/deployment model:

## Repository commands

Record exact commands discovered in this repository.

- Install:
- Development run:
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

## Protected behavior

List working features, APIs, data contracts, security boundaries, user journeys, integrations, and branding that changes must preserve unless explicitly superseded.

- 

## Core data identities

| Entity | Stable ID | Canonical record rule | External/source mapping | Duplicate prevention |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

See `docs/DATA-IDENTITY.md`.

## Migration state

- Migration system/tool:
- Migration ledger/table:
- Latest migration expected by current code:
- Latest migration confirmed in production:
- Destructive migration precautions:

## Backup and rollback

- Backup system:
- Backup scope:
- Backup retention:
- Restore procedure:
- Known-good code rollback:
- Data/schema rollback boundary:

See `docs/BACKUP-ROLLBACK.md`.

## Deployment

- Deployment authority:
- Deployment procedure:
- Required pre-deploy checks:
- Required post-deploy checks:
- Release evidence location: `releases/`

See `docs/DEPLOYMENT.md`.

## Known risks / open decisions

| ID | Risk or decision | Impact | Owner | Next action |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Acceptance criteria

- 
