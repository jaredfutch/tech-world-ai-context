# Continuity Model

## Continuity is controlled, not automatic

Previous conversations, files, repositories, memories, and summaries are potential context—not unquestionable truth. They must be reconciled against newer decisions and current evidence.

## Current truth and historical truth are separate

A continuing project should preserve both:

- **Current state** — the best supported statement of what is true now.
- **Historical events** — what happened previously, including superseded states, corrections, deployments, failures, and decisions.

Updating current state must not erase older events. Append a new event and use an explicit supersession relationship when a prior state is replaced.

## Timestamp semantics

Keep these separate:

- `last_activity_at` — most recent known project activity.
- `last_changed_at` — most recent confirmed material state change.
- `last_verified_at` — most recent time the recorded state was checked against authoritative evidence.

Activity does not imply verification. A recent conversation does not automatically refresh an old deployment fact.

## Correction retention

When a user corrects a fact, design, price, schedule, dimension, ownership claim, architecture choice, or wording:

1. Identify exactly what changed.
2. Preserve previously approved work that is unaffected.
3. Mark the rejected information as superseded.
4. Recheck downstream dependencies affected by the correction.
5. Avoid reintroducing the rejected approach unless new evidence materially changes the situation.

A useful private correction record contains:

```text
previous value / approach
→ replacement
→ reason/source
→ affected downstream items
→ verification needed
```

## Source-of-truth labels

Use explicit evidence labels when useful:

- **Confirmed** — directly supplied or approved by the user or current authoritative artifact.
- **Observed** — directly seen in repository state, logs, UI, API output, files, or connected systems.
- **Calculated** — derived from known inputs; show important math.
- **Estimate** — reasoned range with stated assumptions.
- **Inference** — supported but not directly established.
- **Unknown** — materially unavailable.

## Status semantics

For substantial software work:

```text
Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted
```

These are evidence states, not writing style. Do not upgrade status merely because work was requested or discussed.

## Conflict handling

When two sources disagree, do not silently average or merge them. Identify which is newer, closer to the real system, explicitly approved, or more authoritative.

Examples:

- A current repository schema outranks an old architecture summary.
- A user's explicit correction outranks an earlier assumption.
- A current signed contract outranks an informal pricing note.
- Current official API documentation outranks remembered platform behavior.

## Project identity

Use one permanent canonical ID per real continuing project. A rename becomes an alias. A feature, deployment, task, or defect remains under its parent project unless it develops a genuinely independent lifecycle and architecture.

## Project separation

Continuity does not mean cross-contamination. Keep separate projects, clients, owners, money, schedules, credentials, data sets, and commitments isolated unless a real relationship is established.

See [`live-context-protocol.md`](live-context-protocol.md) for the private current-state and append-only history model.
