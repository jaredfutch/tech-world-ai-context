# Public / Private Boundary

## Principle

Public context should explain **how the assistant should work**. Private context should contain **facts that do not need to be public to perform the work**.

## Appropriate for public context

- general operating principles;
- context precedence rules;
- verification standards;
- generic `AGENTS.md` templates;
- safe example project structures;
- sanitized workflow examples;
- release/checklist conventions;
- public product documentation links;
- public company/project descriptions already intended for disclosure.

## Keep private

Do not publish:

- passwords, API keys, tokens, cookies, SSH keys, or recovery material;
- customer PII or private contact records;
- private email/text/thread contents;
- live lead lists or campaign recipient data;
- confidential contracts, NDAs, pricing terms, or financial records;
- bank/payment account details;
- employee/subcontractor sensitive records;
- private schedules or location patterns;
- production database exports;
- proprietary source code that is not intended to be open source;
- security findings that would materially increase exploitation risk;
- private project notes simply because they are useful to an AI assistant.

## Public bootstrap rule

Treat the bootstrap as an index/router, not a data warehouse. It should remain safe to fetch in any context where its URL is known.

## Repository examples

Sanitize examples before publishing. Replace real organizations, contacts, IDs, amounts, domains, addresses, credentials, and project facts with placeholders unless those details are intentionally public.

## Connected tools

A public document can instruct an assistant to consult authorized private sources when relevant, but it must not imply that the assistant automatically has access. Access depends on the current product, workspace, connector permissions, repository permissions, and user authorization.

## Secret discovery

If a secret or sensitive record is found in a public repository:

1. Do not repeat the value unnecessarily.
2. Remove it from the active source as appropriate.
3. Rotate/revoke exposed credentials when applicable.
4. Consider repository history and caches, not only the current file.
5. Record the incident in an appropriate private security process.

## Test before publishing

Before making context public, ask:

- Does this reveal a customer or person's private information?
- Does it expose where money, credentials, or production systems live?
- Does it disclose a contractual or operational commitment that was not intended to be public?
- Would a malicious reader gain meaningful access or targeting information?
- Can this be converted into a generic template without losing the method?

If yes, keep it private or sanitize it.