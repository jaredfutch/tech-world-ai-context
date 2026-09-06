# Setup: ChatGPT

## Goal

Use a short persistent instruction as a router to a stable public bootstrap URL rather than storing every operating rule and project detail in one prompt.

## 1. Host the bootstrap

Publish `bootstrap.md` at a stable URL you control, for example:

```text
https://example.com/ai-context/bootstrap.md
```

Keep the path stable. Update the linked public guidance as your operating method evolves.

## 2. Add the persistent pointer

Start from [`../templates/custom-instructions.example.md`](../templates/custom-instructions.example.md) and replace the example URL.

The pointer should tell ChatGPT:

- when to retrieve the bootstrap;
- that the bootstrap is supplemental user guidance;
- to reconcile it with the current conversation, files, repositories, and authorized private records;
- to prefer the newest explicit correction over rejected older context;
- to inspect actual repositories and `AGENTS.md` files before coding when available;
- to continue safely from available context if the bootstrap cannot be retrieved.

## 3. Keep task-specific data out of the public pointer

Do not put customer records, credentials, live project status, financial account data, private schedules, or confidential correspondence into the public bootstrap merely to make them persistent.

Use the appropriate private project/file/connector/repository source instead.

## 4. Treat retrieval as selective

A substantive task may require the bootstrap, one relevant operating document, one project record, and the actual artifact being changed. It usually does not require loading every document for every project.

## 5. Verify current facts

Persistent context is useful for continuity but can become stale. For changeable facts—platform behavior, APIs, pricing, laws, schedules, policies, current people/roles, or deployment state—verify against current authoritative evidence when the fact matters.

## 6. Preserve action boundaries

A prompt that says “research,” “review,” “diagnose,” or “draft” should not be treated as authorization to send messages, publish changes, deploy code, purchase items, delete data, or otherwise mutate an external system.

## 7. New projects

The bootstrap can apply before a project-specific record exists. For a new project, use the public operating rules, inspect/create the actual repository, establish its real architecture, then add a project-specific `AGENTS.md` and private record as needed.

## Practical test

To verify your setup, start a fresh conversation and ask a substantive project question without pasting the bootstrap URL. Then check whether the assistant retrieves the public operating context and still inspects the real project evidence before making claims.