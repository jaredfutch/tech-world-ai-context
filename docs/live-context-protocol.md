# Live Context Protocol

## Purpose

The framework separates **what is true now** from **what happened before** so a newer summary does not erase historical truth and an old conversation does not masquerade as current state.

## Three layers

### Public operating guidance

The public framework describes methods, precedence, schemas, privacy boundaries, and verification rules. It must not contain populated private project state.

### Private canonical live state

Each continuing project keeps one permanent canonical `project_id` and, when useful:

- `PROJECT.md` — durable scope, ownership, architecture references, environments, and boundaries.
- `STATE.json` — concise current machine-readable state.
- `DECISIONS.md` — confirmed decisions and supersession history.
- `CORRECTIONS.md` — rejected or replaced facts and downstream effects.
- `HANDOFF.md` — compact continuation snapshot.
- `SOURCES.md` — authoritative repositories, files, systems, contracts, dashboards, and provenance.

A cross-project `current-project-register.json` resolves aliases to permanent project IDs.

### Append-only history

`history/project-events.ndjson` stores material events one JSON object per line. Existing events are not rewritten merely because current state changed.

## Canonical identity

- Create one permanent ID for each real continuing project.
- A rename becomes an alias or display-name change, not a second project.
- A feature, defect, client deployment, or one-time task remains under the parent project unless it develops an independent lifecycle and architecture.
- Keep unrelated projects, ownership, money, commitments, schedules, credentials, and data separated.

## Timestamp semantics

Keep three timestamps distinct:

- `last_activity_at` — most recent known project activity.
- `last_changed_at` — most recent confirmed material change to project state.
- `last_verified_at` — most recent check of recorded state against authoritative evidence.

Recent activity does not automatically mean the underlying deployment, contract, price, configuration, or implementation was re-verified.

## Provenance

A state record should identify the source type and source reference for material facts. When a fact cannot be verified, mark it stale, unknown, or unverified rather than silently refreshing it.

Private state is an index, not a substitute for the real artifact. Current repositories, live systems, signed records, official platform documentation, files, logs, and directly observed output remain authoritative when material.

## Continuing-project review sequence

1. Resolve the canonical project ID.
2. Read current `STATE.json` and `HANDOFF.md`.
3. Apply current decisions and corrections.
4. Inspect the real repository, system, contract, file, dashboard, or other authoritative source when the task depends on it.
5. Reconcile the current request and any newer explicit correction.
6. Distinguish activity, change, and verification timestamps.
7. After a material confirmed change, update current state and append a historical event.

## Corrections and supersession

A correction should record:

- what was wrong or superseded;
- the replacement;
- source or reason;
- affected downstream items;
- verification that remains necessary.

Do not delete historical evidence merely to make the timeline look consistent.

## New projects

When new work becomes a continuing project:

1. Assign one permanent canonical project ID.
2. Register canonical name and aliases.
3. Create private project records from current evidence, not guesses.
4. Append a `project_created` event.
5. Leave unknown fields null or explicitly unverified until authoritative evidence is available.

## Privacy boundary

The public repository may contain this protocol and the schemas that define private records. Populated private records belong only in an authorized access-controlled store.

Never copy credentials, API keys, authentication tokens, customer records, private schedules, contracts, financial-account data, health information, confidential correspondence, private source code, or other secrets into public framework files.

## Failure behavior

If private context is unavailable, do not claim it was reviewed. Continue from the best authorized evidence available and identify the missing continuity source only when it materially limits correctness.
