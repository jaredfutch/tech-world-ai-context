# Setup: Codex and Repository Agents

## Goal

Combine organization-level operating guidance with repository-local instructions so an agent understands both **how to work** and **how this specific codebase actually works**.

## 1. Keep the global layer small

Use your persistent/global instructions to point to a stable public bootstrap and define high-level behavior: continuity, correction precedence, verification, privacy boundaries, and authorization.

## 2. Put repository facts in `AGENTS.md`

Add an `AGENTS.md` at the repository root or other appropriate scope. Start from [`../templates/AGENTS.template.md`](../templates/AGENTS.template.md).

Populate it by inspecting the repository. Do not invent:

- stack/framework;
- entry points;
- database/migration method;
- auth/role model;
- build/test commands;
- deployment target;
- rollback process.

## 3. Keep instructions close to the work

More specific project instructions should live closer to the relevant code. Large monolithic instruction files are harder to maintain and more likely to mix unrelated concerns.

## 4. Inspect before editing

For an existing repository:

1. Read applicable `AGENTS.md` files and repository documentation.
2. Inspect manifests, configuration, routes, schema, integrations, tests, and deployment files.
3. Establish actual commands from the codebase.
4. Trace the defect or requested behavior through every affected layer.
5. Preserve unrelated working behavior and data.
6. Implement.
7. Run the repository's real verification commands.
8. Runtime-test when the environment permits.
9. Deploy only when explicitly authorized.

## 5. Keep production facts separate from public examples

Repository instructions may be private when the repository is private. Do not copy secrets into `AGENTS.md`. Reference environment-variable names or secret-management locations without exposing values.

## 6. New repositories

When starting from scratch:

1. Load operating guidance.
2. Resolve project requirements and boundaries.
3. Establish an initial architecture.
4. Create the repository.
5. Add `AGENTS.md` reflecting the chosen architecture.
6. Implement and verify.
7. Update `AGENTS.md` if architecture or commands materially change.

The repository instructions should evolve with the real repository rather than becoming a stale design document.

## 7. Completion language

Use evidence-based stages:

`Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted`

A successful code edit does not prove deployment, runtime behavior, or user acceptance.