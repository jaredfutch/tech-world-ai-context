# Tests

Tests should reflect the project's actual stack and business risk. Record exact commands in `AGENTS.md` and `PROJECT.md` after inspection.

## Suggested layers

### Unit

Pure business logic, normalization, calculations, validation, and isolated components.

### Integration

Database behavior, migrations, APIs, authentication/authorization, tenant boundaries, queues, and external-service adapters.

### Smoke/runtime

Critical user journeys and deploy-sensitive paths in an appropriate runtime.

## Minimum risk-oriented coverage

As applicable, verify:

- primary success path;
- invalid input;
- permission denial;
- missing/expired state;
- duplicate submission/idempotency;
- retry/recovery;
- external-service failure;
- cancellation/partial completion;
- data isolation;
- payment/messaging consent boundaries;
- responsive/accessibility behavior;
- production-critical smoke paths.

A missing automated test should be recorded as a limitation rather than represented as passing evidence.
