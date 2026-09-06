# Security Policy

This repository is public operating guidance and sanitized examples. It should never contain real credentials, private customer data, confidential correspondence, live production records, or other sensitive operational material.

## Reporting a problem

If you find exposed credentials, sensitive customer information, or another issue that would materially increase exploitation risk, do **not** post the secret or exploit details in a public issue.

Instead, contact Tech-World LLC through an appropriate private channel and provide only the minimum information needed to locate the problem.

## If sensitive data is committed

1. Remove the sensitive value from the active source.
2. Rotate or revoke affected credentials when applicable.
3. Review repository history, forks, caches, logs, and CI artifacts as appropriate.
4. Determine whether customer/person notification or other response obligations apply.
5. Record the remediation in a private security process.

Deleting a value from the newest commit alone does not guarantee it is no longer exposed.