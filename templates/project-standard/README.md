# Project Standard Starter

This directory is a stack-neutral starter for a substantial software repository using the Tech-World AI Context Framework.

## How to use it

Copy the contents of this directory into the root of the target repository, then populate each file from current evidence.

Do not fill architecture, commands, deployment targets, credentials, versions, or runtime status from memory when the repository or environment can be inspected.

Recommended first pass:

1. inspect repository instructions and current source;
2. fill `PROJECT.md` and `AGENTS.md`;
3. identify protected behavior and current known-good state;
4. populate existing decisions/corrections that can be verified;
5. document real migration, test, deployment, backup, and rollback procedures;
6. run `python scripts/validate_project.py`;
7. enable `.github/workflows/verify-project.yml`;
8. use `releases/RELEASE.template.md` for future releases.

## Privacy

This public starter contains placeholders only. A populated project copy may be private. Never publish secrets, credentials, customer data, private schedules, financial-account data, confidential contracts, live lead records, or proprietary implementation details merely because a template includes a place to record project facts.
