# One-Minute Demo

## The problem

Long-running AI work breaks down when conversation history is treated as project state.

A typical failure pattern looks like this:

```text
User: "Fix the project again."

AI reconstructs from memory
  → assumes an older architecture
  → misses a prior correction
  → duplicates an existing workflow
  → edits the visible symptom
  → calls the change "done" before deployment
```

The result may be plausible in the conversation while being wrong for the actual repository.

## The Tech-World approach

The Tech-World AI Context Framework separates **intent** from **operational truth**.

```text
Current request
    ↓
Persistent pointer / bootstrap
    ↓
Repository AGENTS.md
    ↓
PROJECT.md + DECISIONS.md + CORRECTIONS.md + HANDOFF.md
    ↓
Current repository + schema + migrations + configuration
    ↓
Implementation
    ↓
Tests / build / runtime evidence
    ↓
Deployment evidence
    ↓
User acceptance
```

### Example

Suppose a user says:

> "The AI assistant stopped routing local opportunities into the right lead categories. Fix it without losing what already works."

Without controlled continuity, an agent may create another routing layer because it remembers the goal but not the current implementation.

With the framework, the agent first establishes:

- what the user previously approved;
- what corrections superseded older decisions;
- which version is currently deployed;
- how the existing lead router works;
- which database records and IDs are canonical;
- which migrations already ran;
- which tests define protected behavior;
- what the last known-good release was.

Only then does it calculate the delta and make a change.

## The key distinction

```text
Conversation history tells us what the project is supposed to be.
Current artifacts tell us what the project actually is.
Verification tells us what actually works.
```

Those three layers should not be collapsed into one.

## Status is evidence, not optimism

The framework uses a precise progression:

```text
Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted
```

A code edit is not a deployment. A deployment is not user acceptance. Missing evidence is reported as missing rather than guessed.

## Why this matters

The framework is designed for teams and individuals using ChatGPT, Codex, and other AI coding agents across real projects that accumulate:

- months of conversation history;
- source repositories;
- database changes;
- corrections and rejected ideas;
- deployment state;
- client or business constraints;
- external integrations;
- test and runtime evidence.

The goal is not infinite memory. The goal is **controlled continuity**.

## Start here

1. Read the repository README.
2. Use the compact bootstrap pattern.
3. Add project-specific `AGENTS.md` guidance.
4. For substantial software projects, adopt the Project Standard templates.
5. Keep private operational state in authorized private storage rather than the public framework repository.
