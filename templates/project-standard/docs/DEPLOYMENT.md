# Deployment

> Replace placeholders with the project's actual deployment procedure. Never guess commands or targets.

## Environments

| Environment | Target | Branch/ref | Data source | Deployment authority |
| --- | --- | --- | --- | --- |
| Development |  |  |  |  |
| Staging |  |  |  |  |
| Production |  |  |  |  |

## Pre-deploy gate

Confirm as applicable:

- target environment and authorization are resolved;
- intended commit/artifact is identified;
- working tree/release artifact is reproducible;
- required code checks passed;
- migration status is known;
- backup/restore requirements are satisfied;
- secrets/config exist in the target without being copied into source or logs;
- known failures are disclosed;
- previous known-good release is identified.

## Deployment procedure

Record exact project-specific commands and ordering here.

1. 
2. 
3. 

## Database migrations

- Migration status command:
- Apply command:
- Expected migration(s):
- Destructive/high-risk steps:
- Rollback/restore boundary:

## Post-deploy verification

Record the exact smoke/runtime checks required for this product.

- [ ] application starts/responds;
- [ ] authentication works as applicable;
- [ ] authorization/tenant boundaries checked as applicable;
- [ ] primary changed workflow exercised;
- [ ] critical integrations checked;
- [ ] errors/logs reviewed;
- [ ] migration state confirmed;
- [ ] release evidence written to `releases/`.

## Status semantics

Deployment advances the project to **Deployed** only when the intended change is actually present in the target and post-deploy evidence supports that claim. It does not imply **User-Accepted**.
