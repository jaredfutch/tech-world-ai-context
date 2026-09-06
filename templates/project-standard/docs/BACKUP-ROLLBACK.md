# Backup and Rollback

Code rollback, schema rollback, and data restoration are different operations. Document each explicitly.

## Backup policy

- Systems/data covered:
- Backup mechanism:
- Storage location/class:
- Encryption/access boundary:
- Frequency:
- Retention:
- Last restore test:
- Backup owner:

## Pre-change backup requirement

Define which changes require a fresh backup or snapshot before execution.

Examples may include destructive migrations, large imports, bulk edits, payment/data-model changes, authentication changes, or infrastructure replacement.

## Code rollback

- Previous known-good release:
- Rollback command/procedure:
- Configuration compatibility concerns:
- Verification after rollback:

## Database/schema rollback

- Migration tool:
- Are down migrations supported?:
- Which migrations are safe to reverse?:
- Which changes require forward-fix instead?:
- Which changes require restoring a snapshot?:

## Data restore

- Restore source:
- Restore procedure:
- Point-in-time capability:
- Expected data loss window, if any:
- Required authorization:
- Verification after restore:

## Rollback decision record

When rollback occurs, record:

- reason;
- affected release/commit;
- trigger time;
- authorized operator;
- code action;
- data/schema action;
- verification result;
- follow-up corrective work.
