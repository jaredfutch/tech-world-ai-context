# Database Migrations

Store ordered structural database changes here using the migration mechanism native to the actual project.

## Required properties

Each migration should have:

- a unique ordered identifier;
- a concise purpose;
- deterministic forward behavior;
- explicit destructive/high-risk notes when applicable;
- a rollback/down strategy when safe and supported;
- compatibility notes when application code and schema must be deployed in a specific order.

## Rules

- Do not replace versioned migrations with undocumented manual production SQL.
- Never assume production schema state from source code alone.
- Record applied migrations in the database or deployment system.
- Back up before destructive/high-risk migrations.
- Prefer expand/migrate/contract patterns when zero-downtime compatibility matters.
- Do not edit an already-applied migration in a way that changes its historical meaning; create a new migration instead unless the project's migration tool and policy explicitly require otherwise.

## Naming example

```text
20260906_001_add_canonical_opportunity_id.sql
20260906_002_create_source_mapping_table.sql
```

Use the naming convention required by the project's real migration tool when one exists.
