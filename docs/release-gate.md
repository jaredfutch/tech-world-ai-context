# Release Gate

Use a release gate to prevent “implemented” from being confused with “ready for production.” Adapt the checks to the real repository and product.

## Gate 1 — Scope confirmed

- Requested behavior is clear.
- Exact target environment and ownership are known.
- Protected behavior and exclusions are identified.
- Relevant current repository/project guidance has been read.

## Gate 2 — Implementation complete

- Every affected layer has been changed: UI, API, data, permissions, integrations, configuration, etc. as applicable.
- Root cause is addressed rather than hidden behind an overlay.
- Unrelated behavior and data are preserved.
- Data migrations/backups/rollback are prepared where needed.

Status may now be **Implemented**.

## Gate 3 — Code verification

Run only commands actually provided/discovered by the repository. Typical checks may include:

- syntax/compile;
- lint;
- typecheck;
- unit/integration tests;
- build;
- migration validation;
- static security checks.

Record exact pass/fail/could-not-run results.

Status may now be **Code-Verified** if the required static checks pass.

## Gate 4 — Runtime verification

Exercise the actual changed behavior in an appropriate runtime.

Include relevant paths such as:

- normal success;
- invalid input;
- permission denial;
- missing/expired state;
- cancellation;
- duplicate submission;
- retry/recovery;
- external-service failure;
- responsive/device behavior;
- payment/messaging flows when applicable.

Status may now be **Runtime-Tested** when runtime evidence supports it.

## Gate 5 — Deployment authorization

Before deployment:

- deployment was explicitly requested/authorized;
- environment is resolved;
- production secrets/config are available without exposing them;
- backup/migration/rollback needs are satisfied;
- known failures are disclosed.

After the change is actually applied and verified in the target environment, status may be **Deployed**.

## Gate 6 — Acceptance

User/stakeholder acceptance is separate from technical deployment. Record acceptance only after the authorized stakeholder has reviewed or otherwise accepted the result.

Status may then be **User-Accepted**.

## Release report

A concise handoff should state:

```text
Status:
Implemented:
Code checks passed:
Runtime checks passed:
Deployment:
Known limitations:
Rollback/recovery:
User acceptance:
Next action:
```

Never manufacture missing evidence simply to advance a status.