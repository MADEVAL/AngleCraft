# AngleCraft - Content Perspective Engine

[![Version](https://img.shields.io/badge/version-2.1.0-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Angles](https://img.shields.io/badge/angles-7%2B3-orange)](#the-73-angle-taxonomy)
[![Compatibility](https://img.shields.io/badge/compatibility-any%20LLM-purple)](#compatibility)
[![CI](https://github.com/MADEVAL/AngleCraft/actions/workflows/ci.yml/badge.svg)](https://github.com/MADEVAL/AngleCraft/actions/workflows/ci.yml)

> **Same topic, different lens. Turn what you know into what they want to watch.**

AngleCraft is an AI skill that turns dry expert topics into high-engagement content by applying 7 core angles and 3 foundational lenses (10 angles total). Give it a topic - it returns hooks built to earn attention, with placeholders instead of invented facts.

**Source of truth:** [`SKILL.md`](SKILL.md). This README is the human-facing summary; the skill file is what an agent loads.

---

## The Problem

Most experts produce useful but dull content. They explain *what* and forget *how to make it interesting*. The difference between 200 views and 200,000 is rarely the topic. It is the **angle**: the perspective from which you enter the topic.

## The Solution

A topic is a building. You can photograph the facade, the rooftop, the reflection in a puddle, or the view from a helicopter. Same building, completely different photographs. Same topic, completely different content experiences.

AngleCraft systematizes that choice, then writes the hook. It stops at the angle layer - no padded 1,000-word drafts.

---

## The 7+3 Angle Taxonomy

### Core angles (7)

| # | Angle | Pattern | Best for |
|---|-------|---------|----------|
| 1 | **Myth vs Reality** | "Everyone says X. In reality, Y." | Virality, debate, challenging dogma |
| 2 | **Paradox** | "The more X, the worse Y." | Cognitive hooks, pattern violation |
| 3 | **Level Error** | "You think the problem is X. The real cause is Y." | Reframing, intellectual depth |
| 4 | **Price of Solution** | "Yes, X works. But here is what you really pay." | Trust, credibility, objection handling |
| 5 | **Conditions** | "If A, do X. If B, do Y." | Self-identification, lead screening |
| 6 | **Hidden Driver** | "The real reason X happens is Y." | Insider insight, "aha" moments |
| 7 | **Contrary Thesis** | "Do not do X. Do the opposite." | Debate, contrarian trust |

`Conditions` is a decision structure, not a perspective. It only works when there are real branches.

### Foundation lenses (3)

| # | Lens | Pattern | Best for |
|---|------|---------|----------|
| 8 | **Historical Lens** | How did we get here? | Origin stories, authority |
| 9 | **Future Lens** | Where is this going in 5-10 years? | Urgency, vision |
| 10 | **News Hook** | Real event → bridge to the lesson | Immediate relevance |

Full patterns, examples, and close-angle discrimination: [`references/angles.md`](references/angles.md).

---

## Selection Matrix

### By goal

| Goal | Prioritize |
|------|------------|
| Quick trust / credibility | Price of Solution, Hidden Driver |
| Virality / sharing / reach | Myth vs Reality, Paradox, Contrary Thesis |
| Self-identification | Conditions |
| Intellectual depth / authority | Level Error, Historical Lens, Future Lens |
| Immediate relevance | News Hook |

### By platform

| Platform | Prioritize |
|----------|------------|
| Short-form (TikTok, Reels, Shorts) | Paradox, Myth vs Reality |
| Long-form (YouTube, blog, newsletter) | Level Error, Hidden Driver, Historical Lens |
| Ads / landing pages | Price of Solution, Conditions |
| LinkedIn / B2B | Contrary Thesis, Level Error, Hidden Driver |

### By funnel tier

- **Reach:** Myth vs Reality, Paradox, Contrary Thesis, News Hook
- **Trust:** Level Error, Hidden Driver, Price of Solution, Historical Lens
- **Conversion:** Conditions, Future Lens

---

## Quick Start

### Install (global, OpenCode-compatible)

```bash
git clone https://github.com/MADEVAL/AngleCraft.git ~/.agents/skills/anglecraft
```

`~/.agents/skills` is read by OpenCode and by agents that follow the `.agents` convention. Other supported locations:

| Scope | Path |
|---|---|
| OpenCode global | `~/.config/opencode/skills/anglecraft/` |
| OpenCode project | `.opencode/skills/anglecraft/` |
| Claude Code global | `~/.claude/skills/anglecraft/` |
| Claude Code project | `.claude/skills/anglecraft/` |
| Generic `.agents` | `~/.agents/skills/anglecraft/` or `.agents/skills/anglecraft/` |

Create the directory if needed and copy the repository contents into it. The folder name becomes the skill ID, so keep it lowercase: `anglecraft`.

### Use

```
Give me content angles for: I sell handmade ceramic mugs.
```

Quick Mode answers without clarifying questions. If the topic is broad, it states one assumption and proceeds.

For a full strategy, ask explicitly: `Need a content strategy for my B2B SaaS.` That triggers Deep Mode.

See [`references/examples.md`](references/examples.md) for complete Quick and Deep outputs.

---

## Output Contract

**Quick Mode:** 3-5 rows, columns `# | Angle | Hook | Direction`. Hook is one sentence, 30 words max. Direction is 1-2 sentences, not the full piece.

**Deep Mode:** 5-10 rows, columns `Topic | Angle | Hook | Tier | Platform`, covering at least two funnel tiers.

Both modes add an `Assumption:` line when the topic was narrowed or the audience inferred, and a placeholder note when data is missing.

---

## Quality Control

Every hook is scored on three criteria:

1. **Surprise** - does it contradict a common assumption or reveal non-obvious information?
2. **Specificity** - is it anchored in a concrete mechanism, trade-off, or decision rule?
3. **Curiosity gap** - does the reader need to know what comes next?

Specificity never means inventing facts. If a hook needs a number that was not supplied, AngleCraft writes a `[X]` placeholder and tells you to replace it with verified data before publishing. No fake statistics, case studies, or testimonials.

---

## When Not to Use

AngleCraft works at the idea layer: angles, hooks, and outlines. It is not a full copy engine and not a research tool.

| Request | Use instead |
|---|---|
| SEO briefs, keyword maps, ranking audits | [RankWise](https://github.com/MADEVAL/RankWise) |
| Persuasion audits and cognitive-bias copy optimization | [MindFluence](https://github.com/MADEVAL/MindFluence) |
| Rewriting AI text to sound human | [HumanAI](https://github.com/MADEVAL/HumanAI) |
| Full article or script after the angle is chosen | Write it directly |
| Fact-checking or source research | A research/browsing tool - AngleCraft never invents sources |

---

## Compatibility

- Works with any LLM that can load a Markdown skill.
- Tested paths: OpenCode, Claude Code, and the generic `.agents/skills` convention.
- The runtime skill is a single `SKILL.md` plus optional reference files; no scripts or API keys are required.
- Supporting files (`references/`, `examples/`, `scenarios/`) are read on demand, not loaded automatically.

---

## Repository Layout

```
AngleCraft/
├── SKILL.md                 # runtime skill (source of truth)
├── references/
│   ├── angles.md            # full taxonomy, examples, discrimination
│   └── examples.md          # worked Quick and Deep outputs
├── examples/                # ready outputs by niche
├── scenarios/               # input -> mode/handoff routing
├── evals/                   # 20 test topics + rubric
├── tests/                   # structure validator + dataset checker
├── run_tests.ps1            # Windows test runner
├── CHANGELOG.md
├── README.md
├── README.ru.md
├── LICENSE
└── .github/workflows/ci.yml
```

---

## Testing

```bash
python tests/validate_skill.py
python tests/eval_dataset.py
```

Windows PowerShell: `.\run_tests.ps1`

`validate_skill.py` checks frontmatter, counts, references, README consistency, relative links, and forbidden strings. `eval_dataset.py` checks that every eval topic maps to valid angles and includes safety cases.

For manual output scoring, use [`evals/rubric.md`](evals/rubric.md).

---

## Ethical Boundaries

AngleCraft refuses to generate content for:

- Pseudoscience presented as fact
- Hate speech, discrimination, or targeting of vulnerable groups
- Get-rich-quick, gambling, or predatory financial schemes
- Unproven medical, legal, or financial claims presented as professional advice

For sensitive topics (health, legal, finance, safety), AngleCraft produces educational framing only - never diagnosis, treatment, guaranteed returns, or legal outcomes - and expects a "not professional advice" disclaimer in the final content.

---

## License

MIT - free to use, modify, and distribute. See [`LICENSE`](LICENSE).

---

## Related Skills

- **[RankWise](https://github.com/MADEVAL/RankWise)** - SEO content engine with 49 ranking factors
- **[MindFluence](https://github.com/MADEVAL/MindFluence)** - Marketing copy using 20 cognitive biases
- **[HumanAI](https://github.com/MADEVAL/HumanAI)** - Rewriting AI text to sound human-written (9 languages)

Pipeline: **AngleCraft** picks the angle and hook → **MindFluence** shapes the persuasive copy → **HumanAI** removes the AI voice → **RankWise** handles search visibility.
