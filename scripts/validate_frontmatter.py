#!/usr/bin/env python3
"""Validate frontmatter and required body sections for skills and agents.

Walks `skills/<name>/SKILL.md` and `agents/<name>.md`. For each file:
  1. Parses the YAML frontmatter.
  2. Checks required keys against the schema for its type.
  3. Checks the body contains the required headings and bold field markers.
  4. Reports every error with the file path; exits non-zero on any failure.

Run from the repository root:
    python scripts/validate_frontmatter.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
AGENTS_DIR = ROOT / "agents"

SEMVER_RE = r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$"
KEBAB_RE = r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$"

COMMON_FRONTMATTER_PROPERTIES = {
    "name": {"type": "string", "pattern": KEBAB_RE},
    "description": {"type": "string", "minLength": 60},
    "version": {"type": "string", "pattern": SEMVER_RE},
    "author": {"type": "string", "minLength": 2},
    "license": {"type": "string", "minLength": 2},
    "language": {"type": "string", "enum": ["fr", "en"]},
    "book": {
        "type": "object",
        "required": ["title", "annex"],
        "properties": {
            "title": {"type": "string", "minLength": 2},
            "annex": {"type": "string", "minLength": 1},
        },
    },
    "tags": {
        "type": "array",
        "minItems": 1,
        "items": {"type": "string"},
    },
    "status": {
        "type": "string",
        "enum": ["active", "experimental", "deprecated"],
    },
    "replaced_by": {"type": "string"},
    "contributors": {"type": "array", "items": {"type": "string"}},
}

SKILL_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["name", "description", "version", "author", "license", "language", "book", "tags"],
    "properties": COMMON_FRONTMATTER_PROPERTIES,
    "additionalProperties": True,
}

AGENT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["name", "description", "version", "author", "license", "language", "book", "tags"],
    "properties": {
        **COMMON_FRONTMATTER_PROPERTIES,
        "tools": {"type": "array", "items": {"type": "string"}},
    },
    "additionalProperties": True,
}

SKILL_REQUIRED_BODY = [
    r"^##\s+Fiche éditoriale\s*$",
    r"\*\*Objectif\.\*\*",
    r"\*\*Entrées\.\*\*",
    r"\*\*Sorties\.\*\*",
    r"\*\*Cadence d'usage\.\*\*",
    r"^##\s+Mode opératoire\s*$",
]

AGENT_REQUIRED_BODY = [
    r"^##\s+Fiche éditoriale\s*$",
    r"\*\*Mission\.\*\*",
    r"\*\*Périmètre\.\*\*",
    r"\*\*Déclencheurs\.\*\*",
    r"\*\*Boucle de contrôle\.\*\*",
    r"\*\*Garde-fous\.\*\*",
    r"^##\s+Mode opératoire\s*$",
]


def split_frontmatter(text: str) -> tuple[dict | None, str]:
    """Return (frontmatter_dict, body) or (None, body) if no frontmatter."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    raw = text[4:end]
    body = text[end + 5:]
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML frontmatter: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data, body


def check_body(body: str, patterns: list[str]) -> list[str]:
    errors: list[str] = []
    for pat in patterns:
        if not re.search(pat, body, flags=re.MULTILINE):
            errors.append(f"missing required body element: {pat!r}")
    return errors


def check_file(path: Path, schema: dict, body_patterns: list[str], expected_name: str) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    try:
        frontmatter, body = split_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]
    if frontmatter is None:
        return ["missing YAML frontmatter delimited by '---' lines"]

    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(frontmatter), key=lambda e: list(e.absolute_path)):
        location = "/".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"frontmatter {location}: {err.message}")

    name = frontmatter.get("name")
    if name and name != expected_name:
        errors.append(f"frontmatter name {name!r} does not match folder/file name {expected_name!r}")

    errors.extend(check_body(body, body_patterns))
    return errors


def main() -> int:
    failures: dict[Path, list[str]] = {}

    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()) if SKILLS_DIR.exists() else []:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            failures[skill_file] = ["expected SKILL.md not found"]
            continue
        errs = check_file(skill_file, SKILL_SCHEMA, SKILL_REQUIRED_BODY, expected_name=skill_dir.name)
        if errs:
            failures[skill_file] = errs

    for agent_file in sorted(AGENTS_DIR.glob("*.md")) if AGENTS_DIR.exists() else []:
        errs = check_file(agent_file, AGENT_SCHEMA, AGENT_REQUIRED_BODY, expected_name=agent_file.stem)
        if errs:
            failures[agent_file] = errs

    if failures:
        for path, errs in failures.items():
            print(f"\n{path.relative_to(ROOT)}")
            for e in errs:
                print(f"  - {e}")
        print(f"\n{len(failures)} file(s) failed validation.", file=sys.stderr)
        return 1

    print("All skills and agents pass frontmatter and required-section checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
