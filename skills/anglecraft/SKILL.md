---
name: anglecraft
description: "Content angle generator that turns dry expert topics into high-engagement infotainment. Applies 7 core angles (Myth vs Reality, Paradox, Level Error, Price of Solution, Conditions, Hidden Driver, Contrary Thesis) plus 3 foundational lenses (Historical, Future, News Hook) = 10 angles total. Use for blog posts, video scripts, social content, newsletters, landing pages, and ad hooks in any niche: B2B, B2C, services, products, personal brand. Do NOT use for SEO briefs (RankWise), persuasion/copy audits (MindFluence), or rewriting AI text (human-ai)."
license: MIT
compatibility: Plain Markdown. No external dependencies.
metadata:
  author: Yevhen Leonidov
  version: "2.2.0"
  angles: "7+3"
  languages: "any"
  modes: 2
  repository: "https://github.com/MADEVAL/AngleCraft"
---

# AngleCraft - Content Perspective Engine

> **Tagline:** Same topic, different lens. Turn what you know into what they want to consume.
> **Version:** 2.2.0 · **Angles:** 7 core + 3 lenses · **Modes:** Quick (default), Deep (on request) · **Language:** any

---

## Core Idea

Most experts produce useful but dull content. They explain *what* and forget *how to make it interesting*. The difference between 200 views and 200,000 is rarely the topic - it is the **angle**: the perspective from which you enter the topic.

A topic is a building. You can photograph the facade, the rooftop, the reflection in a puddle, or the view from a helicopter. Same building, completely different photographs. Same topic, completely different content.

Interest is the entry gate: people must notice, finish, and trust before they buy. This skill generates the angle and the hook. It does not write the full piece.

---

## When Not to Use

This skill stops at the angle + hook + outline layer. Hand off when the request is really about something else:

| Request | Use instead |
|---|---|
| SEO brief, keyword map, meta tags, ranking audit | RankWise |
| Persuasion audit, cognitive-bias optimization, tone tuning of existing copy | MindFluence |
| Rewriting AI text so it sounds human | human-ai |
| Full article, script, or landing page after the angle is chosen | Write it directly; do not stretch this skill past hooks and outlines |
| Fact-checking or original research | A research/browsing tool; this skill never invents sources |

If a handoff request arrives inside an angle request, deliver the angles first, then state the handoff in one line.

---

## The 7+3 Taxonomy

### Core angles (7)

| # | Angle | Pattern | Use when |
|---|---|---|---|
| 1 | **Myth vs Reality** | "Everyone says X. In reality, Y." | A prevalent belief is false or outdated and you can correct it. |
| 2 | **Paradox** | "The more X, the worse Y." | Two variables genuinely move in opposite directions. |
| 3 | **Level Error** | "You think the problem is X. It is actually Y." | The stated problem is a symptom of a cause on another level. |
| 4 | **Price of Solution** | "Yes, X works. Here is what it really costs." | A solution carries hidden trade-offs nobody mentions. |
| 5 | **Conditions** | "If A, do X. If B, do Y." | The right answer depends on the reader's situation. |
| 6 | **Hidden Driver** | "X happens because of Y." | An expert-only mechanism explains a visible effect. |
| 7 | **Contrary Thesis** | "Do not do X. Do the opposite." | Mainstream advice is calcified; the contrarian case is honestly held. |

`Conditions` is a decision structure, not a perspective. Use it when segmentation itself is the insight; do not force it onto topics without real branches.

### Foundation lenses (3)

| # | Lens | Pattern | Use when |
|---|---|---|---|
| 8 | **Historical Lens** | "How did we get here?" | History or origin explains the present. |
| 9 | **Future Lens** | "Where is this going in 5-10 years?" | Trajectory, change, or urgency is the point. |
| 10 | **News Hook** | Real event or fact → bridge to the topic | A current story genuinely connects to the lesson. |

Each pattern has a "why it works", three examples, and close-angle discrimination rules in `references/angles.md`. Read it when two angles look similar or when the niche is unfamiliar.

---

## Selection Matrix

### By goal

| Goal | Prioritize |
|---|---|
| Quick trust / credibility | Price of Solution, Hidden Driver |
| Virality / sharing / reach | Myth vs Reality, Paradox, Contrary Thesis |
| Self-identification ("is this me?") | Conditions |
| Intellectual depth / authority | Level Error, Historical Lens, Future Lens |
| Immediate relevance | News Hook |

### By platform

| Platform | Prioritize |
|---|---|
| Short-form (TikTok, Reels, Shorts) | Paradox, Myth vs Reality |
| Long-form (YouTube, blog, newsletter) | Level Error, Hidden Driver, Historical Lens |
| Ad / landing page | Price of Solution, Conditions |
| LinkedIn / B2B | Contrary Thesis, Level Error, Hidden Driver |

### By funnel tier

- **Reach** (broad appeal, sharing): Myth vs Reality, Paradox, Contrary Thesis, News Hook
- **Trust** (depth, credibility): Level Error, Hidden Driver, Price of Solution, Historical Lens
- **Conversion** (objection handling, self-selection, urgency): Conditions, Future Lens

Tiers describe the funnel role of a piece; the goal matrix describes the user's immediate intent. They can overlap (Future Lens is both depth and a conversion/urgency play).

---

## Operating Modes

### Quick Mode (default)

**Trigger:** the user provides a topic, product, or content idea and asks for angles.

**Always default to Quick Mode unless at least one Deep Mode trigger is present.**

**Procedure:**

1. Identify the core topic and niche.
2. Note the audience, platform, and emotional charge already present in the message.
3. Generate 3-5 angle variants across different types from the taxonomy.
4. For each: angle type, hook line, and a 1-2 sentence direction.
5. Output using the Quick Mode table in the Output Contract.

**No clarifying questions in Quick Mode.** Produce angles immediately. If the topic is too broad ("marketing", "health"), pick the most commercially specific sub-topic, state the assumption in one line ("Assuming you mean B2B SaaS content marketing"), and offer to redo it for a narrower topic. Never stall waiting for a refinement.

### Deep Mode

**Trigger (at least one must be present):**

- The user explicitly requests "strategy", "audit", "roadmap", "content plan", or a "deep" analysis.
- The user provides multi-paragraph business context (niche + audience + past attempts + goals) **and** asks for a plan, roadmap, or diagnosis.
- The user provides existing content and asks "why isn't this working" or "how can this be better".
- The user asks to map angles across a content calendar or multiple topics at once.

**If none of these triggers are met, stay in Quick Mode.** Business context alone is not a trigger: if the user just describes their business and asks for angles, produce Quick Mode and optionally close with: "If you'd like a full Deep Mode roadmap across tiers and platforms, flag it."

**Procedure:**

1. Check what is missing: audience, niche, platform, goal, prior attempts. Ask 1-3 questions **only** for missing information. If enough is supplied, state assumptions in one line and proceed.
2. Identify niche sacred cows - beliefs everyone repeats but nobody questions. Ask: "What does every [niche] expert say that might be outdated or incomplete?"
3. Map the 7+3 taxonomy against each topic. Test every angle; discard any with no genuine entry point.
4. Recommend a mix across Reach / Trust / Conversion with a one-line rationale.
5. Deliver the Deep Mode roadmap from the Output Contract.

A full worked Deep Mode example is in `references/examples.md`; ready-made niche outputs are in `examples/`; input-to-mode routing is in `scenarios/`.

---

## Output Contract

### Quick Mode output

| # | Angle | Hook | Direction |
|---|-------|------|-----------|

- 3-5 rows. If the user asks for more, deliver up to 7 per batch and offer another batch; never repeat a hook.
- Hook: one sentence, 30 words maximum, in the publication language (fall back to the user's language).
- Direction: 1-2 sentences on how the piece unfolds; do not write the full piece.
- Add one `Assumption:` line only when you had to narrow an ambiguous topic.
- Add one `Replace bracketed placeholders with verified data before publishing.` line only when placeholders are used.

### Deep Mode output

| Topic | Angle | Hook | Tier | Platform |
|---|---|---|---|---|

- 5-10 rows covering at least two different funnel tiers.
- Add an `Assumptions:` line when audience, platform, or goal was inferred.
- Add a `Data to verify:` line listing every placeholder used.

### Cross-mode rules

- **Canonical angle names stay in English** so they map to the taxonomy. When responding in another language, translate the surrounding text and keep the angle name, e.g. `Myth vs Reality` or `Myth vs Reality / Миф против реальности` on first use.
- **Language:** respond in the user's language; hooks follow the publication language. If the publication language is unknown, write hooks in the user's language.
- **Scope:** this skill produces angles and hooks, not full articles. If the user asks for a full draft, output a short outline (hook + 3-5 beats) first and ask whether to expand.
- **No padding:** no preamble, no restating the request, no "here are some ideas" filler.
- **Mode marker:** optional plain-text line such as `AngleCraft - Quick Mode` or `AngleCraft - Deep Mode`. Skip it inside an ongoing conversation or when the user prefers terse output.
- **Failure:** if no angle passes the Quality Gate, say which criteria failed and what input would unlock a usable angle. Do not output generic filler.

---

## Quality Gate

Before outputting, score every hook:

1. **Surprise** - does it contradict a common assumption or reveal non-obvious information?
2. **Specificity** - is it anchored in a concrete mechanism, trade-off, or decision rule? (Specificity is not permission to invent numbers.)
3. **Curiosity gap** - does the reader need to know what comes next?

A hook must pass all three criteria to ship. If it fails any one, revise it or try another angle type. Cap retries at two per angle; if the topic still cannot pass, return the best hook plus a note about what data would make it stronger.

### Fact discipline

- Never invent statistics, prices, dates, study results, client outcomes, quotes, or expert mechanisms.
- If a hook needs a number the user did not provide, write a placeholder: `[N]`, `[$N]`, `[timeframe]`, `[source]`.
- Canonical placeholder vocabulary across the skill set: `[N]` and `[$N]` for missing numbers, `[timeframe]`, `[source]`, `[VERIFY: ...]` for a claim to check, `[DATA NEEDED: ...]` for a missing block of input, `[illustrative]` for hypothetical examples.
- When placeholders are used, add one line: "Replace bracketed placeholders with verified data before publishing."
- Label hypothetical examples as hypothetical. Never present a made-up case study, testimonial, or benchmark as real.
- If a claim is central to the angle and cannot be verified or safely generalized, choose a different angle.

---

## Anti-Patterns

- **Contrarian for shock value** - Contrary Thesis must be honestly held, not manufactured for engagement.
- **Strawman myth** - Myth vs Reality fails if the "myth" is something nobody actually believes. Attack real, prevalent beliefs.
- **Fake paradox** - Paradox only works when the contradiction is genuine, not a forced rhetorical trick.
- **Vague conditions** - Conditions fails if the branches are generic ("if you want results, work hard"). Branches must be concrete and actionable.
- **Misaligned platform** - A Historical Lens hook that needs two minutes of setup fails on TikTok. Match angle to format.
- **Generic AI voice** - Replace "unlock your potential", "in today's fast-paced world", and "game-changer" with niche-specific language. Every hook needs a detail an expert in *this* niche would recognize - a mechanism, trade-off, or decision rule. If none exists, use a placeholder instead of inventing one.
- **Fabricated specificity** - Invented numbers, fake case studies, and made-up quotes are worse than vagueness. Use `[N]` placeholders and flag them.
- **Angle stuffing** - Do not force all ten angles onto one topic. Three strong, distinct angles beat seven overlapping ones.

---

## Language & Culture

1. **Respond in the user's language.** Match their language for framing, explanations, and surrounding text.
2. **Hooks follow the publication language.** If the content will be published in English, write hooks in English; if in the user's language, translate them. When in doubt, offer both.
3. **Angle logic is language-independent.** Surprise, paradox, and curiosity gaps work across languages; the wording must not be a literal translation of an English template.
4. **Localize references.** A Versailles analogy means nothing to a Korean audience. Use local history, media, and examples when the target market is known.
5. **Do not stereotype by country.** Base cultural choices on the specific audience and evidence, not nationality defaults. When uncertain, prefer universal mechanisms (Paradox, Level Error) or decision framing (Conditions).
6. **Localize everything the user sees** - refusals, disclaimers, placeholder notes, and the mode marker. Only canonical angle names stay in English.

Detailed cultural notes are in `references/angles.md`.

---

## Ethics & Refusal

Do **not** generate angles for:

- Pseudoscience presented as fact (you may use Myth vs Reality only to debunk it).
- Hate speech, discrimination, or content targeting vulnerable groups.
- Get-rich-quick, gambling, or predatory financial schemes.
- Unproven medical, legal, or financial claims presented as professional advice.

**Sensitive-topic rule:** angles are framing devices, not professional advice. For health, legal, financial, or safety topics, never imply a diagnosis, treatment, guaranteed return, or legal outcome. Keep hooks to general education, add a clear "not professional advice" disclaimer to the final content, and prefer behavioral or decision-framing angles over outcome promises.

**Refusal message:** reply in the user's language.

- English: "I can't generate angles for this topic - it falls outside ethical content boundaries. If you have a related legitimate topic, I'm happy to help."
- Russian: "Не могу сгенерировать углы для этой темы - она выходит за этические границы контента. Если есть смежная легитимная тема, помогу."
- Other languages: translate the English template.

---

## References

Read only when needed; the core skill is self-contained.

| File | Read when |
|---|---|
| `references/angles.md` | You need full "why it works", more examples, close-angle discrimination, or cultural notes. |
| `references/examples.md` | You need a complete worked Quick or Deep Mode output. |
| `examples/` | You want a ready output for a specific niche. |
| `scenarios/` | The request is ambiguous and you need mode/handoff routing. |
| `../../evals/` | You are testing or changing the skill (repository root, dev only). |
