#!/usr/bin/env python3
"""Structural validator for AngleCraft.

Stdlib only. Run from the repository root or from any directory:

    python tests/validate_skill.py

Exits 1 if any hard check fails.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "anglecraft"
SKILL = SKILL_DIR / "SKILL.md"
README = ROOT / "README.md"
README_RU = ROOT / "README.ru.md"
CHANGELOG = ROOT / "CHANGELOG.md"

ANGLES = [
    "Myth vs Reality",
    "Paradox",
    "Level Error",
    "Price of Solution",
    "Conditions",
    "Hidden Driver",
    "Contrary Thesis",
    "Historical Lens",
    "Future Lens",
    "News Hook",
]

REQUIRED_SECTIONS = [
    "Core Idea",
    "When Not to Use",
    "The 7+3 Taxonomy",
    "Selection Matrix",
    "Operating Modes",
    "Output Contract",
    "Quality Gate",
    "Anti-Patterns",
    "Language & Culture",
    "Ethics & Refusal",
    "References",
]

FORBIDDEN = [
    "7+2",
    "7%2B2",
    "cortisol",
    "cardio",
    "$3,000",
    "40 hours",
    "TODO",
    "FIXME",
]

errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        fail("SKILL.md must start with YAML frontmatter")
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("unterminated YAML frontmatter")
        return {}, text
    raw, body = parts[1], parts[2]
    data: dict[str, str] = {}
    parent = ""
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  ") and ":" in line and parent:
            key, value = line.strip().split(":", 1)
            data[f"{parent}.{key.strip()}"] = value.strip().strip('"').strip("'")
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            data[key] = value
            parent = key if not value else ""
    return data, body


def relative_links(text: str) -> list[str]:
    targets = re.findall(r"\]\(([^)]+)\)", text)
    result = []
    for target in targets:
        target = target.strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        result.append(target.split("#", 1)[0])
    return [t for t in result if t]


def main() -> int:
    skill_text = read(SKILL)
    readme_text = read(README)
    readme_ru_text = read(README_RU)
    changelog_text = read(CHANGELOG)

    meta, body = parse_frontmatter(skill_text)

    # Frontmatter
    if meta.get("name") != "anglecraft":
        fail(f"frontmatter name must be 'anglecraft', got {meta.get('name')!r}")
    description = meta.get("description", "")
    if not 80 <= len(description) <= 1024:
        fail(f"description length must be 80..1024, got {len(description)}")
    if "Do NOT use" not in description:
        fail("description must include negative triggers ('Do NOT use')")
    if "10 angles total" not in description:
        fail("description must state '10 angles total'")
    version = meta.get("metadata.version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"metadata.version must be semver, got {version!r}")
    if meta.get("metadata.angles") != "7+3":
        fail("metadata.angles must be '7+3'")
    if meta.get("license") != "MIT":
        fail("frontmatter license must be MIT")
    if meta.get("compatibility") != "Plain Markdown. No external dependencies.":
        fail("frontmatter compatibility must describe a plain-Markdown environment")

    # Required sections
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in body:
            fail(f"missing section: ## {section}")

    # Taxonomy rows
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*\*\*(.+?)\*\*", body, flags=re.MULTILINE)
    numbers = [int(n) for n, _ in rows]
    if numbers != list(range(1, 11)):
        fail(f"taxonomy must have rows 1..10 in order, got {numbers}")
    row_names = [name.strip() for _, name in rows]
    if row_names != ANGLES:
        fail(f"taxonomy angle names/order mismatch: {row_names}")

    # Angle names and stale counts
    for angle in ANGLES:
        if angle not in skill_text:
            fail(f"SKILL.md missing angle: {angle}")
        if angle not in readme_text:
            fail(f"README.md missing angle: {angle}")

    # Cross-file version consistency
    for path, text in [
        (README, readme_text),
        (README_RU, readme_ru_text),
        (CHANGELOG, changelog_text),
    ]:
        if version and version not in text:
            fail(f"{path.name} does not mention version {version}")

    # Forbidden strings across markdown. The changelog may quote removed strings
    # for historical accuracy, so only check TODO/FIXME there.
    md_files = sorted(ROOT.rglob("*.md"))
    for path in md_files:
        if ".git" in path.parts:
            continue
        text = read(path)
        needles = ["TODO", "FIXME"] if path.name == "CHANGELOG.md" else FORBIDDEN
        for needle in needles:
            if needle in text:
                fail(f"{path.relative_to(ROOT)} contains forbidden string: {needle!r}")

    # Size budget
    size = SKILL.stat().st_size if SKILL.exists() else 0
    if size > 16000:
        fail(f"SKILL.md is {size} bytes; budget is 16000")
    elif size > 15500:
        warn(f"SKILL.md is {size} bytes; close to the 16000 budget")

    # References and assets
    required = [
        "skills/anglecraft/references/angles.md",
        "skills/anglecraft/references/examples.md",
        "evals/topics.jsonl",
        "evals/rubric.md",
        ".github/workflows/ci.yml",
        ".gitignore",
        ".gitattributes",
        "LICENSE",
        "CHANGELOG.md",
        "README.ru.md",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(f"missing required asset: {rel}")

    for rel in ["references/angles.md", "references/examples.md"]:
        if rel not in skill_text:
            fail(f"SKILL.md must link to {rel}")

    examples = sorted((SKILL_DIR / "examples").glob("*.md")) if (SKILL_DIR / "examples").exists() else []
    scenarios = sorted((SKILL_DIR / "scenarios").glob("*.md")) if (SKILL_DIR / "scenarios").exists() else []
    if len(examples) < 5:
        fail(f"examples/ must contain at least 5 files, found {len(examples)}")
    if len(scenarios) < 5:
        fail(f"scenarios/ must contain at least 5 files, found {len(scenarios)}")

    for path in examples:
        text = read(path)
        for marker in ["**Input:**", "**Mode:**"]:
            if marker not in text:
                fail(f"{path.relative_to(ROOT)} missing marker: {marker}")
        quick = "| # | Angle | Hook | Direction |" in text
        deep = "| Topic | Angle | Hook | Tier | Platform |" in text
        if not (quick or deep):
            fail(f"{path.relative_to(ROOT)} missing a Quick or Deep output table")
    for path in scenarios:
        text = read(path)
        for marker in ["**Input:**", "**Mode:**"]:
            if marker not in text:
                fail(f"{path.relative_to(ROOT)} missing marker: {marker}")

    # Relative links across all markdown files
    if "]()" in readme_text:
        fail("README.md contains an empty badge link ']()'")
    for path in md_files:
        if ".git" in path.parts:
            continue
        for target in relative_links(read(path)):
            if not (path.parent / target).exists():
                fail(f"{path.relative_to(ROOT)} links to missing path: {target}")

    # Key content checks
    checks = {
        "Fact discipline": "Fact discipline" in skill_text,
        "Fabricated specificity anti-pattern": "Fabricated specificity" in skill_text,
        "Localized refusal": "Не могу сгенерировать углы" in skill_text,
        "Sensitive-topic rule": "Sensitive-topic rule" in skill_text,
        "Output failure behavior": "Failure:" in skill_text,
        "Deep trigger guard": "Business context alone is not a trigger" in skill_text,
        "Quick no-questions rule": "No clarifying questions in Quick Mode" in skill_text,
        "Handoff table": "RankWise" in skill_text and "MindFluence" in skill_text and "human-ai" in skill_text,
    }
    for label, ok in checks.items():
        if not ok:
            fail(f"content check failed: {label}")

    # Report
    print(f"AngleCraft validator (version {version or '?'})")
    print(f"  SKILL.md: {size} bytes")
    print(f"  angles: {len(row_names)}; examples: {len(examples)}; scenarios: {len(scenarios)}")
    if warnings:
        print("\nWarnings:")
        for message in warnings:
            print(f"  - {message}")
    if errors:
        print("\nErrors:")
        for message in errors:
            print(f"  - {message}")
        print(f"\nFAILED: {len(errors)} error(s)")
        return 1
    print("\nOK: all structural checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
