# Scenario: Handoff to a Sibling Skill

**Input:** "Write an SEO-optimized article with keyword density and meta tags, and make it sound human."

**Mode:** Handoff

**Expected behavior:**

1. Recognize that the request is mostly outside AngleCraft's layer.
2. Offer one angle if it helps the article, then hand off.
3. State the pipeline in one line.

**Example response:**

> I can pick the angle and hook, but this request is mostly SEO and humanization.
> Angle: Level Error - "The keyword is not the problem. The search intent is."
> Handoff: RankWise for the brief/meta, HumanAI for the voice.

**Routing table:**

| Request | Skill |
|---|---|
| SEO brief, keywords, meta, ranking audit | RankWise |
| Persuasion audit, bias optimization, tone of existing copy | MindFluence |
| Humanizing AI text | HumanAI |
| Angle, hook, outline | AngleCraft |

**Do not:**

- Pretend to run an SEO audit.
- Claim keyword-density expertise.
- Rewrite the whole article when the user asked for a pipeline.
