#!/usr/bin/env python3
"""Validate the AngleCraft evaluation dataset.

Stdlib only. Run:

    python tests/eval_dataset.py

Checks schema, angle coverage, safety coverage, and refusal cases.
Exits 1 on failure.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "evals" / "topics.jsonl"

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
PLATFORMS = {"short", "long", "ads", "linkedin", "any"}
SAFETY = {"none", "health", "finance", "legal"}
BEHAVIORS = {"angles", "refusal", "handoff"}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def main() -> int:
    if not DATASET.exists():
        print(f"FAILED: missing {DATASET.relative_to(ROOT)}")
        return 1

    topics = []
    for line_number, line in enumerate(DATASET.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"line {line_number}: invalid JSON ({exc})")
            continue
        if not isinstance(item, dict):
            fail(f"line {line_number}: expected a JSON object")
            continue
        item["_line"] = line_number
        topics.append(item)

    if len(topics) != 20:
        fail(f"expected exactly 20 topics, found {len(topics)}")

    ids = [item.get("id") for item in topics]
    if len(set(ids)) != len(ids):
        fail(f"duplicate ids: {[k for k, v in Counter(ids).items() if v > 1]}")
    if ids != [f"t{i:02d}" for i in range(1, 21)]:
        fail(f"ids must be t01..t20 in order, got {ids}")

    angle_coverage: Counter[str] = Counter()
    niche_set = set()
    safety_set = Counter()
    behavior_set = Counter()

    for item in topics:
        label = item.get("id", f"line {item['_line']}")
        required = {
            "id",
            "niche",
            "platform",
            "topic",
            "mode",
            "expected_behavior",
            "safety",
            "acceptable_angles",
            "notes",
        }
        missing = required - set(item)
        if missing:
            fail(f"{label}: missing keys {sorted(missing)}")
            continue

        if item["mode"] not in {"quick", "deep"}:
            fail(f"{label}: invalid mode {item['mode']!r}")
        if item["expected_behavior"] not in BEHAVIORS:
            fail(f"{label}: invalid expected_behavior {item['expected_behavior']!r}")
        if item["safety"] not in SAFETY:
            fail(f"{label}: invalid safety {item['safety']!r}")
        if item["platform"] not in PLATFORMS:
            fail(f"{label}: invalid platform {item['platform']!r}")
        if not str(item["topic"]).strip():
            fail(f"{label}: empty topic")
        if not str(item["notes"]).strip():
            fail(f"{label}: empty notes")

        angles = item["acceptable_angles"]
        if not isinstance(angles, list):
            fail(f"{label}: acceptable_angles must be a list")
            continue
        if len(angles) != len(set(angles)):
            fail(f"{label}: duplicate angles in acceptable_angles")
        unknown = [a for a in angles if a not in ANGLES]
        if unknown:
            fail(f"{label}: unknown angles {unknown}")

        if item["expected_behavior"] == "refusal":
            if angles:
                fail(f"{label}: refusal topics must not list acceptable angles")
        else:
            if len(angles) < 3:
                fail(f"{label}: expected at least 3 acceptable angles, got {len(angles)}")
            if item["mode"] == "deep" and len(angles) < 5:
                fail(f"{label}: deep topics need at least 5 acceptable angles, got {len(angles)}")

        angle_coverage.update(angles)
        niche_set.add(item["niche"])
        safety_set[item["safety"]] += 1
        behavior_set[item["expected_behavior"]] += 1

    if len(niche_set) < 6:
        fail(f"need at least 6 distinct niches, found {len(niche_set)}")
    if behavior_set["refusal"] < 1:
        fail("dataset must include at least one refusal case")
    if safety_set["health"] < 2:
        fail("dataset must include at least two health-adjacent cases")
    if safety_set["finance"] < 2:
        fail("dataset must include at least two finance cases")
    if safety_set["legal"] < 1:
        fail("dataset must include at least one legal case")
    missing_angles = [a for a in ANGLES if angle_coverage[a] == 0]
    if missing_angles:
        fail(f"angles never covered by the dataset: {missing_angles}")

    print("AngleCraft eval dataset")
    print(f"  topics: {len(topics)}; niches: {len(niche_set)}")
    print(f"  behaviors: {dict(behavior_set)}")
    print(f"  safety: {dict(safety_set)}")
    print(f"  angle coverage: {len([a for a in ANGLES if angle_coverage[a]])}/{len(ANGLES)}")
    if errors:
        print("\nErrors:")
        for message in errors:
            print(f"  - {message}")
        print(f"\nFAILED: {len(errors)} error(s)")
        return 1
    print("\nOK: dataset is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
