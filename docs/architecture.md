# Architecture

## Goal

The framework separates durable operating guidance from task-specific and private state. The assistant loads only the context needed for the current task, then reconciles it against the real artifact or system being changed.

## Layers

### 1. Current request

Defines the immediate goal, scope, constraints, and authorization.

### 2. Persistent pointer

A compact custom instruction or equivalent tells the assistant when and how to retrieve the public bootstrap.

### 3. Public bootstrap

A stable URL routes to current public operating guidance. It should remain small enough to retrieve quickly and stable enough to reference for long periods.

### 4. Public operating guidance

Reusable conventions live in separate documents: continuity, verification, public/private boundaries, release gates, and setup instructions.

### 5. Repository/project guidance

`AGENTS.md` documents rules closest to the code or project. It should describe protected behavior, known architecture facts, verification commands, deployment boundaries, and unresolved risks.

### 6. Private project records

Private records carry customer/project state, decisions, schedules, financial commitments, correspondence, and other information that should not be public.

### 7. Actual artifacts and observed state

Repositories, archives, files, logs, screenshots, database state, API responses, deployed behavior, and device behavior are evidence. They should be inspected before claiming implementation details or success.

### 8. Current external authority

Laws, regulations, platform documentation, pricing, schedules, API requirements, and other changeable facts should be checked against current authoritative sources when they materially affect the task.

## Precedence

A practical reconciliation order is:

1. Higher-priority platform/safety/access-control requirements.
2. Current explicit user request and newest correction/decision.
3. Current authoritative artifact or directly observed live state.
4. Closest applicable repository/project guidance.
5. Authorized private project record.
6. Current public operating guidance.
7. Earlier confirmed conversation context.
8. Estimates, assumptions, and external inference.

The point is not that every task needs every layer. The point is to know where to look when layers conflict.

## Retrieval strategy

Do not ingest the entire context tree by default.

A good retrieval flow is:

```text
classify task
  ↓
load bootstrap if task is substantive/ongoing
  ↓
select relevant public guidance
  ↓
select project/repository context
  ↓
inspect actual evidence
  ↓
retrieve private records only when needed and authorized
  ↓
verify changeable external facts when material
  ↓
perform the requested work
  ↓
record exact status and remaining gap
```

## Why not one giant prompt?

A monolithic prompt becomes stale, mixes unrelated projects, consumes context unnecessarily, and is difficult to audit. Layering keeps generic policy stable while allowing project-specific guidance and current evidence to remain close to their source.

## New-project bootstrap

A project does not need to be pre-registered before the framework applies. For new work:

1. Load the public operating context.
2. Inspect or create the repository/project artifact.
3. Establish the actual stack and boundaries.
4. Create a project `AGENTS.md` based on inspection.
5. Create a private project record if continuity is needed.
6. Implement and verify.
7. Update status and decisions based on evidence.

## Failure behavior

The public bootstrap is a continuity aid, not a single point of failure. If it cannot be retrieved, continue from authorized current context and state the limitation only when it materially affects confidence or completion.