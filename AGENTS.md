# AGENTS.md

## Repository purpose

This repository documents the public Tech-World AI Context Framework. It is intentionally sanitized and must not become a storage location for private Tech-World operational data.

## Protected rules

- Keep examples generic and reusable.
- Never add real credentials, secrets, customer records, contracts, private financial data, live lead lists, private schedules, or confidential correspondence.
- Preserve the distinction between public operating guidance and private project records.
- Keep the status model precise: Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted.
- Treat current explicit corrections as superseding rejected older guidance.
- Do not claim a workflow is tested across a product or platform unless it was actually tested.

## Editing guidance

- Prefer concise Markdown with concrete examples.
- Keep the bootstrap stable and lightweight.
- Put reusable instructions in `docs/` and `templates/` rather than bloating `bootstrap.md`.
- When adding a new integration example, document its trust boundary and what information must remain private.
- Keep relative links valid.

## Verification

Before calling a documentation change complete:

1. Check all repository-relative links.
2. Check example paths and filenames for consistency.
3. Confirm no private or identifying operational data was introduced.
4. Confirm examples do not imply permissions or capabilities that an AI agent may not actually have.
5. Confirm any product-specific claims that may change are either sourced or phrased as examples rather than guarantees.