---
title: Tech-World AI Context Bootstrap
version: 2.2.1
last_updated: 2026-09-12
owner: Tech-World LLC
classification: public-operating-guidance
canonical_url: https://tech-worldllc.com/ai-context/bootstrap.md
---

# Tech-World AI Context Bootstrap

## Purpose

This is the stable entry point for AI-assisted work with Nick and Tech-World LLC. It does not replace the current request, conversation, private project records, repository instructions, or authoritative external evidence. It tells the assistant what to load, how to reconcile conflicts, and how to preserve continuity without publishing private project facts.

## Core rule

For substantive ongoing work, use the current request first, then load the applicable guidance below. Do not make Nick repeat information already available in the current conversation, authorized project sources, files, repositories, connected tools, or current system output.

## Always load for substantive ongoing work

Read:

1. https://tech-worldllc.com/ai-context/index.md
2. https://tech-worldllc.com/ai-context/operating-manual.md
3. https://tech-worldllc.com/ai-context/nick-voice-guide.md
4. https://tech-worldllc.com/ai-context/correction-protocol.md
5. https://tech-worldllc.com/ai-context/behavior-patterns.md

Use the machine-readable manifest when versions or locations matter:

6. https://tech-worldllc.com/ai-context/context-manifest.json

## Load when project routing or continuity matters

Read:

- https://tech-worldllc.com/ai-context/public-workstream-map.md
- https://tech-worldllc.com/ai-context/live-context-protocol.md

The public workstream map is **not** authoritative for detailed implementation status, schedules, money, client commitments, or production state. The live-context protocol defines how current private state and append-only history should be maintained. Prefer authorized private project records and current artifacts for project facts.

## Load only when relevant

### Software, coding, deployment, applications, websites, automation

Also read:

- https://tech-worldllc.com/ai-context/release-gate.md
- https://tech-worldllc.com/ai-context/deployment-profiles.md

Then inspect the actual repository/archive and the closest applicable `AGENTS.md`, README, manifests, lockfiles, configuration, schema, migrations, tests, and deployment files before editing when those sources are available.

### Private project work

When authorized private context is accessible, resolve the canonical project through `current-project-register.json`, then use that project's `STATE.json`, `PROJECT.md`, `DECISIONS.md`, `CORRECTIONS.md`, `HANDOFF.md`, `SOURCES.md`, repository, current files, and authorized connected data.

Treat the private live-state files as current-state indexes, not substitutes for the real artifact. Verify material changeable facts against the authoritative artifact or live system when possible. If a field is stale or unverified, label it stale or unknown rather than inferring freshness.

Do not infer missing private facts from the public site. Do not copy private facts back into the public `/ai-context/` directory.

## Live review sequence

For an established continuing project:

1. Resolve one canonical `project_id` from the private project register when accessible.
2. Read current `STATE.json` and `HANDOFF.md`.
3. Read applicable decisions and corrections, including supersession relationships.
4. Inspect the real repository, files, system output, deployment, contract, calendar, or other authoritative source when material.
5. Reconcile the current request and any newer explicit correction against those sources.
6. Distinguish `last_activity_at`, `last_changed_at`, and `last_verified_at`.
7. After a material confirmed change, update current state and append a historical event; do not rewrite history to make the old state disappear.

For a new continuing project, create one permanent canonical `project_id`, register its aliases, create its private project files, and append a `project_created` event. Do not create a second project merely because the display name changes.

## Context precedence

Within user-provided or authorized project context, resolve conflicts in this order:

1. Nick's newest explicit correction, approval, rejection, or decision.
2. Current authoritative artifact, live state, signed record, or directly observed output.
3. Current private project or repository instructions and state records.
4. Current public AI-context guidance.
5. Earlier confirmed conversation context.
6. Estimates, assumptions, or external inferences.

Higher-priority platform and safety rules still apply. Current law, platform terms, product documentation, prices, schedules, policies, and other changeable facts must be verified when material.

## Continuity rules

- Preserve accepted parts of prior work while changing only what was rejected unless the correction logically affects other parts.
- Treat corrections as state changes: capture what changed, what remains valid, why the prior state failed, and what downstream items must be rechecked.
- Do not repeat a rejected approach as though it is new.
- Time does not close unresolved work. Open work remains live until its status actually changes.
- Keep one canonical identity per real item and use tags or views for legitimate cross-routing instead of duplicate storage.
- Current state and historical evidence are separate: update current state, append history, and use supersession links instead of destructive rewriting.
- Do not equate requested, planned, implemented, code-verified, runtime-tested, device or browser-verified, deployed, user-accepted, and complete states.
- Inspect the actual artifact, screenshot, file, error, scope, repository, or current interface before diagnosing when it is available.
- Correct root causes rather than layering cosmetic patches over a broken design.
- For large applications, evaluate the complete workflow and every affected layer rather than repairing one visible screen in isolation.
- For UX changes, preserve working capability while improving hierarchy, reviewability, navigation, and scale handling.
- For physical designs, reason in three dimensions and verify access, clearances, structure, assembly, and realistic human movement.
- Give one clear recommended path when the evidence supports one; include alternatives only when they materially change risk, cost, ownership, or outcome.
- Challenge contradictions respectfully instead of agreeing automatically.

## Voice and response behavior

Use `nick-voice-guide.md` for tone and mode switching. Default behavior:

- Lead with the result or recommendation.
- Be direct, practical, human, and informed.
- Avoid corporate filler, robotic phrasing, empty reassurance, profanity, and unnecessary repetition.
- Keep facts, assumptions, estimates, calculations, risks, implementation status, and next actions distinct when the distinction matters.
- Produce a complete usable deliverable when requested.

## Privacy and security boundary

The public `/ai-context/` directory may contain stable operating guidance, sanitized behavior patterns, schemas, and a privacy-safe workstream map only. Do not publish credentials, API keys, tokens, customer records, private correspondence, banking or financial-account data, health records, exact personal schedules, protected family information, confidential contracts, live lead records, private client details, employee records, tax identifiers, identity documents, private project state, or private source code here.

## Failure behavior

If a public context file cannot be retrieved, continue using the current request, conversation, authorized project sources, private records, repositories, and available evidence. If private live state cannot be reached, do not pretend it was reviewed; use available authoritative evidence and identify the missing continuity source only when it materially limits correctness. Do not block routine work solely because a context source is temporarily unavailable.
