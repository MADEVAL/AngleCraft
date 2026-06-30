# AngleCraft — Content Perspective Engine

[![Version](https://img.shields.io/badge/version-2.0-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Angles](https://img.shields.io/badge/angles-7%2B2-orange)]()
[![Compatibility](https://img.shields.io/badge/compatibility-any%20LLM-purple)]()

> **Same topic, different lens. Turn what you know into what they want to watch.**

AngleCraft is an AI skill that transforms dry expert topics into high-engagement content by applying 7+2 journalistic angle types. Give it a topic - it returns hooks people actually click.

---

## The Problem

Most experts produce useful but dull content. They tell you *what* - but not *how* to make it interesting. The difference between 200 views and 200,000 is rarely the topic. It's the **angle**: the perspective from which you enter the topic.

## The Solution

AngleCraft systematizes angle selection. Think of a topic as a building. You can photograph it from the main facade - or from the rooftop, reflected in a puddle, from a helicopter. Same building, completely different photographs. Same topic, completely different content experiences.

---

## The 7+2 Angle Taxonomy

### Main Angles

| # | Angle | Pattern | Best For |
|---|-------|---------|----------|
| 1 | **Myth vs Reality** | "Everyone says X. In reality, Y works." | Virality, debate, challenging dogma |
| 2 | **Paradox** | "The more X, the worse Y." | Cognitive hooks, pattern violation |
| 3 | **Level Error** | "You think the problem is X. The real cause is Y." | Reframing, intellectual depth |
| 4 | **Price of Solution** | "Yes, X works. But here's what you're really paying." | Trust, credibility, objection handling |
| 5 | **Conditions** | "If A → do X. If B → do Y." | Self-identification, lead screening |
| 6 | **Hidden Driver** | "The real reason X happens is Y - and you'd never guess it." | Insider insight, "aha!" moments |
| 7 | **Contrary Thesis** | "Don't do X. Do the opposite. Here's why." | Debate, algorithmic fuel, contrarian trust |

### Foundation Angles (Use Anytime)

- **Historical Lens** - How was it in the past?
- **Future Lens** - Where is it going in 5–10 years?
- **News Hook / Story Bridge** - Fascinating fact → bridge to your topic

---

## Selection Matrix

### By Goal

| Goal | Best Angles |
|------|-------------|
| Quick trust / credibility | Price of Solution, Hidden Driver |
| Virality / sharing / reach | Myth vs Reality, Paradox, Contrary Thesis |
| Self-identification | Conditions |
| Intellectual depth / authority | Level Error, Historical Lens, Future Lens |
| Immediate relevance | News Hook |

### By Platform

| Platform | Best Angles |
|----------|-------------|
| Short-form (TikTok, Reels, Shorts) | Paradox, Myth vs Reality |
| Long-form (YouTube, blog, newsletter) | Level Error, Hidden Driver, Historical Lens |
| Ads / landing pages | Price of Solution, Conditions |
| LinkedIn / B2B | Contrary Thesis, Level Error, Hidden Driver |

---

## Quick Start

### Installation

Copy `SKILL.md` into your agent's skills directory:

```
~/.agents/skills/anglecraft/SKILL.md
```

Load the skill in your agent session - AngleCraft activates automatically when you describe a topic and ask for content angles.

### Usage

**Quick Mode** (default - no questions asked):

```
> User: I sell handmade ceramic mugs. Give me content angles.

AngleCraft — Quick Mode

| # | Angle Type    | Hook                                                                 | Direction                                          |
|---|---------------|----------------------------------------------------------------------|----------------------------------------------------|
| 1 | Myth vs Reality | "Everyone says handmade mugs are overpriced. Here's what 40 hours of craft actually looks like." | Break down the production process to justify value |
| 2 | Historical Lens | "This 400-year-old Japanese firing technique still can't be replicated by machines." | Story of a specific craft tradition |
| 3 | Paradox         | "The more 'perfect' a handmade mug looks, the less it's worth."      | Premium value of visible human imperfection         |
| 4 | Hidden Driver   | "Cheap mugs break because of a design flaw you've never noticed."    | Expert material science insight                     |
| 5 | Contrary Thesis | "Stop buying matching mug sets. Mismatched is the real luxury."      | Reframe uniformity → curated individuality          |
```

**Deep Mode** (triggered by complex context or explicit strategy request):

```
> User: I run a SaaS for automated invoice processing. Our content is all feature comparisons - boring. Need a content strategy.

AngleCraft — Deep Mode (identifying niche sacred cows and mapping the angle stack)

| Topic | Angle | Hook | Tier | Platform |
|---|---|---|---|---|
| Why invoices are still manual | Level Error | "It's not a software problem. It's a trust problem." | Trust | Blog, LinkedIn |
| AI taking accounting jobs | Myth vs Reality | "AI won't replace accountants. It'll replace accountants who only type numbers." | Reach | Twitter, LinkedIn |
| Hidden cost of cheap AP tools | Price of Solution | "Your $29/month tool costs $3,000/month in errors. Here's the math." | Conversion | Blog, Newsletter |
| Automate vs manual | Conditions | "If under $500 → automate. If enterprise → one wrong digit costs the deal." | Conversion | Landing page |
| Finance teams resist change | Hidden Driver | "They're not lazy. Their bonus depends on zero errors." | Trust | LinkedIn, Video |
```

---

## Quality Control

Every generated hook must pass three criteria:

1. **Surprise** - Does it contradict a common assumption or reveal non-obvious information?
2. **Specificity** - Is it anchored in a concrete detail, or vague and generic?
3. **Curiosity gap** - Does the reader *need* to know what comes next?

---

## Content Niches

Works for any niche: B2B, B2C, services, products, personal brands. Use cases include:

- Blog posts and newsletters
- Video scripts (YouTube, TikTok, Reels, Shorts)
- Social media content (LinkedIn, Twitter/X, Instagram)
- Landing pages and ad copy
- Webinar and podcast hooks
- Product launch campaigns

---

## Ethical Boundaries

AngleCraft refuses to generate content for:

- Pseudoscience presented as fact
- Hate speech, discrimination, or targeting of vulnerable groups
- Get-rich-quick, gambling, or predatory financial schemes
- Unproven medical claims as treatment advice

---

## License

MIT - free to use, modify, and distribute.

---

## Related Skills

- **[RankWise](https://github.com/MADEVAL/RankWise)** - SEO content engine with 49 ranking factors
- **[MindFluence](https://github.com/MADEVAL/MindFluence)** - Marketing copy using 20 cognitive biases
- **[HumanAI](https://github.com/MADEVAL/HumanAI)** - Rewriting AI text to sound human-written (9 languages)
