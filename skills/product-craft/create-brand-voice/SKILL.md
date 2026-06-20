---
name: create-brand-voice
description: Create a local product-specific brand voice skill from user answers, URLs, existing copy, audience context, tone preferences, and forbidden phrases. Use when a user wants reusable writing guidance for a brand, product, founder voice, docs, UI copy, website copy, social posts, emails, support replies, or GTM messaging.
---

# Create Brand Voice

Use this to create a private local brand voice skill for a specific product, company, project, or person.

## Workflow

1. Collect only useful inputs.
   - Name of brand/product/person.
   - URLs to inspect: website, docs, app, pricing, blog, changelog, social, competitors.
   - Audience, category, alternatives, differentiation.
   - Surfaces: website, docs, UI, onboarding, email, sales, social, support, errors, releases, ads.
   - Copy the user likes/dislikes, forbidden words, claims, and habits.

2. Turn vague tone into rules.
   - Convert adjectives into sentence length, vocabulary, proof level, humor level, directness, and technical depth.
   - Add a public-facing writing rule: final copy should not expose internal reasoning, process notes, prompt interpretation, private context, or implementation chatter.
   - Browse provided URLs when current public facts matter.
   - Do not copy long passages.
   - Do not include secrets, customer data, private roadmap, credentials, personal paths, or private implementation details.

3. Generate the local skill.
   - Run `scripts/create_brand_voice_skill.py`.
   - Default output: `$AGENT_SKILLS_HOME`, then `$CODEX_HOME/skills`, then `~/.codex/skills`.
   - Default name: `<brand-slug>-brand-voice`.
   - Store durable facts in `references/brand-voice.md`.

4. Tighten it.
   - Make it specific enough to shape copy.
   - Keep it safe enough for future agents.
   - Add before/after examples only if supplied examples are safe.
   - Validate the generated skill when a validator exists.

## Questions

Ask the smallest useful set:

- What brand/product/person is this for?
- Which URLs should I inspect?
- Who is the audience?
- What category and alternatives define the market?
- What should it sound like, and never sound like?
- Which surfaces should it cover?
- Any safe examples of copy you like or dislike?

If the user wants speed, create a first version with TODOs.

## Usage

```bash
python3 scripts/create_brand_voice_skill.py \
  --name "Example Product" \
  --website-url "https://example.com" \
  --audience "Operations teams at mid-market companies" \
  --category "Workflow automation software" \
  --tone "clear, direct, concrete, calm" \
  --avoid "hype, vague AI claims, exclamation marks" \
  --surfaces "website, docs, dashboard UI, emails"
```

## Final Shape

```text
Created: <skill path>
Skill: <name>
Inputs: <answers/URLs/examples>
Validation: <result>
TODOs: <missing facts>
```
