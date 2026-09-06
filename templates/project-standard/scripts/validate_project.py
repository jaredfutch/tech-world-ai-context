#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "PROJECT.md",
    "DECISIONS.md",
    "CORRECTIONS.md",
    "HANDOFF.md",
    "CHANGELOG.md",
    "docs/DEPLOYMENT.md",
    "docs/BACKUP-ROLLBACK.md",
    "docs/DATA-IDENTITY.md",
    "database/migrations/README.md",
    "tests/README.md",
    "releases/README.md",
    "releases/RELEASE.template.md",
]

STATUS_CHAIN = "Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SUSPICIOUS_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "aws access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".json", ".py", ".sh", ".sql"}


def iter_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"VERSION", "LICENSE"}:
            yield path


def check_required(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required project-control file: {rel}")


def check_status_model(errors: list[str]) -> None:
    agents = ROOT / "AGENTS.md"
    if agents.is_file() and STATUS_CHAIN not in agents.read_text(encoding="utf-8", errors="replace"):
        errors.append("AGENTS.md does not contain the canonical status chain")


def check_links(errors: list[str]) -> None:
    for path in iter_text_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in LINK_RE.findall(text):
            target = raw.strip().split("#", 1)[0]
            if not target or target.startswith("#"):
                continue
            parsed = urlparse(target)
            if parsed.scheme or target.startswith("mailto:"):
                continue
            candidate = (ROOT / target.lstrip("/")) if target.startswith("/") else (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {raw}")
                continue
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link: {raw}")


def check_sensitive_patterns(errors: list[str]) -> None:
    for path in iter_text_files():
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in SUSPICIOUS_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: suspicious {label} pattern")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_status_model(errors)
    check_links(errors)
    check_sensitive_patterns(errors)

    if errors:
        print("Project Standard validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Project Standard validation passed.")
    print(f"Checked {sum(1 for _ in iter_text_files())} text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
