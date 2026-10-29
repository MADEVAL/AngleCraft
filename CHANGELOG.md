# Changelog

All notable changes to AngleCraft are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [2.1.0] - 2026-10-30

### Fixed

- **Angle count:** corrected `7+2` to `7+3` everywhere (7 core angles + 3 foundational lenses = 10). The old count contradicted the three listed lenses in both `SKILL.md` and `README.md`.
- **Deep Mode consistency:** business context alone no longer triggers Deep Mode; the trigger now requires an explicit plan/roadmap/diagnosis request. Clarifying questions are limited to missing information, and the worked example states assumptions instead of contradicting the procedure.
- **Funnel tiers:** all ten angles are now assigned exactly once. `Historical Lens` is no longer missing; `News Hook` moved from Conversion to Reach; `Future Lens` is documented as both depth and urgency.
- **Quick Mode contradiction:** removed the simultaneous "no questions asked" and "ask for a refinement" instruction. Broad topics now get one stated assumption and an immediate output.
- **Unsafe examples:** removed the fitness/cortisol/cardio hooks that violated the skill's own medical-claims policy. Replaced with an accounting-firm example.
- **Fabricated specificity:** removed invented numbers (`40 hours`, `$3,000/month`, `$29/month`, `$500`) and replaced them with `[X]` placeholders. Added a Fact Discipline section and a `Fabricated specificity` anti-pattern.

### Added

- **Output Contract** with exact table shapes, row limits, hook length, language rules, and failure behavior.
- **When Not to Use** section and negative triggers in the frontmatter description, with handoffs to RankWise, MindFluence, and HumanAI.
- **Localized refusal** templates (English + Russian, translation rule for other languages) and localized safety disclaimers.
- **Sensitive-topic rule** for health, legal, financial, and safety content.
- **`references/angles.md`** with full patterns, examples, close-angle discrimination, and cultural notes.
- **`references/examples.md`** with worked Quick, Deep, audit, full-draft, refusal, and localization examples.
- **`examples/`** with six niche-ready outputs.
- **`scenarios/`** with input-to-mode and handoff routing.
- **`evals/`** with 20 test topics, a scoring rubric, and a dataset checker.
- **CI** (`.github/workflows/ci.yml`) running the structure validator and dataset checker.
- **`README.ru.md`**, `.gitignore`, `.gitattributes`, `.markdownlint.json`, and `run_tests.ps1`.

### Changed

- `SKILL.md` reduced from 19.7 KB to 15.1 KB (-23%) by moving long examples and "why it works" detail into `references/`.
- README no longer duplicates full behavior details; `SKILL.md` is documented as the source of truth.
- Static badges now link to meaningful targets; added a CI badge.
- Installation instructions expanded for OpenCode, Claude Code, project-local, and generic `.agents` paths.

## [2.0.0] - 2026-06-27

### Added

- Initial public release.
- 7 core angles: Myth vs Reality, Paradox, Level Error, Price of Solution, Conditions, Hidden Driver, Contrary Thesis.
- 3 foundational lenses: Historical, Future, News Hook.
- Quick Mode (default) and Deep Mode (strategy/roadmap).
- Selection matrices by goal and platform.
- Language handling, cultural adaptation, quality checks, anti-patterns, and refusal policy.
