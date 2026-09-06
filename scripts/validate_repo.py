#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "TRADEMARKS.md",
    "SECURITY.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "CONTRIBUTING.md",
    "VERSION",
    "CHANGELOG.md",
    "bootstrap.md",
    "AGENTS.md",
    "docs/specification-v1.md",
    "docs/compatibility.md",
    "docs/versioning.md",
    "docs/release-process.md",
    "templates/AGENTS.template.md",
    "templates/custom-instructions.example.md",
    "templates/project-register.template.md",
]

TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".json", ".py"}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SUSPICIOUS_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "aws access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}


def iter_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.name in {"LICENSE", "VERSION"} or path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def check_required(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")


def check_version(errors: list[str]) -> None:
    path = ROOT / "VERSION"
    if not path.exists():
        return
    value = path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", value):
        errors.append(f"VERSION is not semantic version format: {value!r}")


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
            if target.startswith("/"):
                candidate = ROOT / target.lstrip("/")
            else:
                candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {raw}")
                continue
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link: {raw}")


def check_sensitive_patterns(errors: list[str]) -> None:
    for path in iter_text_files():
        if path.name == Path(__file__).name:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in SUSPICIOUS_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: suspicious {label} pattern")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_version(errors)
    check_links(errors)
    check_sensitive_patterns(errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    print(f"Checked {sum(1 for _ in iter_text_files())} text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
