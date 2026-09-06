# Governance

## Canonical upstream

The canonical upstream repository for the Tech-World AI Context Framework is:

`https://github.com/jaredfutch/tech-world-ai-context`

Tech-World LLC maintains the official public specification, reference implementation guidance, release history, and compatibility language in this repository.

Forks and derivative projects are allowed under the MIT License, but they are independent unless Tech-World LLC explicitly states otherwise.

## Maintainer authority

The repository owner and designated maintainers may:

- accept, modify, or reject proposed changes;
- define specification requirements and compatibility language;
- publish releases and changelog entries;
- deprecate unsafe or obsolete guidance;
- maintain the public/private boundary;
- protect Tech-World branding from misleading use;
- close issues or pull requests that are out of scope, duplicative, unsafe, or unsupported by evidence.

Open source does not mean every proposal must be merged.

## Decision priorities

Framework decisions should prioritize:

1. safety and privacy;
2. continuity without invented state;
3. clear source-of-truth and correction precedence;
4. real repository and runtime evidence;
5. portability across AI tools and development environments;
6. low adoption friction;
7. backward compatibility within a major version;
8. maintainability and clarity.

## Specification changes

Changes that alter mandatory compatibility behavior require:

- a documented issue or pull request;
- explanation of the problem and expected effect;
- consideration of backward compatibility;
- versioning under `docs/versioning.md`;
- changelog entry when released.

Breaking changes require a new major specification version.

## Community contributions

Contributors may propose improvements, examples, documentation, tests, interoperability ideas, and specification changes. Contributions are reviewed on technical merit and alignment with the framework principles.

No contributor receives trademark, endorsement, certification, or governance rights merely by contributing code or documentation.

## Official status

Only this canonical upstream and other resources explicitly designated by Tech-World LLC may call themselves the official Tech-World AI Context Framework or official reference implementation.

Third-party implementations may use factual compatibility language as allowed by `TRADEMARKS.md` and `docs/compatibility.md`.