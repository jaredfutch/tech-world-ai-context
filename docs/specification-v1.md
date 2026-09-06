# Tech-World AI Context Framework Specification v1

Status: **1.0.0**

This document defines the minimum requirements for claiming compatibility with the Tech-World AI Context Framework v1.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY indicate requirement strength.

## 1. Layered context

A compatible implementation MUST distinguish at least these context layers:

1. the current user request;
2. persistent or bootstrap-level operating guidance;
3. repository or project-specific guidance;
4. authorized private project records and current files when relevant;
5. actual implementation or observed live state;
6. current authoritative external evidence when the requested fact can change.

An implementation MUST NOT treat a stale summary as stronger evidence than a current authoritative artifact or directly observed state.

## 2. Stable bootstrap

The system SHOULD support a stable bootstrap document or equivalent persistent entry point that can direct an assistant to relevant operating guidance without embedding all guidance in one permanent prompt.

If the bootstrap is unavailable, the assistant MUST NOT invent its contents. It SHOULD continue from other authorized current context when safe to do so.

## 3. Project-specific repository instructions

Substantial code repositories SHOULD contain a project-specific instruction document such as `AGENTS.md` describing the actual project, protected behavior, relevant commands, verification expectations, and deployment boundaries.

Repository facts that have not been inspected MUST be marked unknown rather than invented.

## 4. Correction precedence

A compatible implementation MUST preserve explicit corrections and decisions.

When a user explicitly corrects an earlier fact, decision, ownership statement, dimension, price, schedule, architecture choice, or other material item, the newer confirmed correction MUST supersede the rejected information unless newer authoritative evidence establishes otherwise.

Unaffected approved work SHOULD remain intact.

## 5. Source-of-truth reconciliation

When sources conflict, the implementation MUST identify or resolve the conflict using the most authoritative and current applicable evidence.

A recommended precedence model is:

1. newest explicit user correction, approval, rejection, or decision;
2. current authoritative artifact or directly observed live state;
3. current project/repository guidance;
4. current operating guidance;
5. earlier confirmed conversation context;
6. estimates, assumptions, or inferences.

Higher-priority platform, safety, security, legal, and access-control requirements always remain applicable.

## 6. Public/private separation

A compatible public bootstrap architecture MUST NOT require publication of credentials, tokens, customer records, private correspondence, contracts, personal schedules, financial account data, protected health information, or other private project data.

Public guidance SHOULD describe how work is performed. Private project facts SHOULD remain in access-controlled sources.

## 7. Action authority

The framework MUST distinguish research, diagnosis, planning, drafting, implementation, testing, deployment, sending/publishing, purchasing, deletion, charging, and scheduling.

Research, inspection, planning, or drafting MUST NOT be treated as authorization for a consequential external action.

## 8. Evidence-based status

For substantial software work, implementations SHOULD use precise states such as:

`Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted`

An implementation MUST NOT claim a later state without evidence that the corresponding action occurred.

## 9. Verification

Changes SHOULD be verified using the real commands, tests, builds, runtime checks, environment, and acceptance criteria available to the project.

A compatible implementation MUST NOT invent commands or test results.

## 10. Root-cause repair

When repairing defects, implementations SHOULD correct the underlying source rather than repeatedly adding overlays, duplicated logic, or cosmetic workarounds when a clean source-level correction is possible.

## 11. Multi-project separation

Unrelated businesses, clients, repositories, finances, ownership, commitments, and project status MUST NOT be merged merely because the same user or AI assistant works with them.

## 12. Compatibility statement

A third-party implementation satisfying the mandatory requirements above MAY state:

`Compatible with Tech-World AI Context Framework v1`

That statement indicates compatibility only. It MUST NOT be used to imply endorsement, sponsorship, certification, affiliation, or official Tech-World status. See `TRADEMARKS.md` and `docs/compatibility.md`.

## 13. Extensions

Implementations MAY add additional layers, tools, memory systems, agent roles, automation, schemas, or project metadata as long as those extensions do not violate the mandatory requirements above.

## 14. Versioning

Breaking changes to these mandatory requirements require a new major specification version. See `docs/versioning.md`.