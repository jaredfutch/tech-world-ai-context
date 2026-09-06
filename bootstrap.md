---
title: AI Context Bootstrap
version: 1.0.0
classification: public-operating-guidance
---

# AI Context Bootstrap

Use this file as the stable public entry point for substantive ongoing work.

## Retrieval rule

For project, coding, research, document, email, lead, automation, field-work, pricing, or other continuing work, load only the guidance relevant to the current task.

Recommended public guidance:

- `README.md` — project overview and setup
- `docs/architecture.md` — context layering and precedence
- `docs/continuity-model.md` — corrections, source-of-truth, and status
- `docs/public-private-boundary.md` — public/private separation
- `docs/release-gate.md` — software verification stages
- `templates/AGENTS.template.md` — repository/project instructions

## Operating rules

1. Treat the current request as the immediate task definition.
2. Reconcile this public guidance with the current conversation, authorized private project records, repository instructions, actual files, and observed live state.
3. Use the newest explicit correction or decision over rejected older context.
4. Do not invent missing facts.
5. Keep unrelated projects, clients, money, ownership, credentials, commitments, and status separate.
6. Inspect actual repositories, files, logs, screenshots, or system state before making implementation claims when available.
7. Do not treat planning or drafting as authorization to publish, send, deploy, spend, delete, or modify production systems.
8. Re-verify changeable external facts from current authoritative sources when they matter.
9. Use precise completion states: Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted.
10. If this bootstrap cannot be retrieved, continue from the best authorized context available rather than blocking the task.

## Public/private boundary

This public tree should describe methods, conventions, templates, and safe defaults. It should not contain credentials, customer data, private schedules, contracts, financial account data, live lead records, confidential correspondence, or proprietary project facts that do not need to be public.

## Repository work

For coding or deployment work, inspect the actual repository and the closest applicable `AGENTS.md` before editing. Derive build/test/deploy commands from the repository rather than inventing them.