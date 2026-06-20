# Mad Agent Skills

A compact, public-safe skill library for Codex and other AI agents.

These skills capture repeatable workflows an agent can load and follow: review risky code, coordinate worktrees, verify UI in a real browser, write public-facing copy, create a brand voice, and turn product or GTM ambiguity into a decision.

They are intentionally small. No giant manuals. No private company context. Just practical instructions that help agents work with better judgment, clearer evidence, and cleaner output.

## Quick Start

Clone the repo:

```bash
git clone https://github.com/blah-mad/mad-agent-skills.git
cd mad-agent-skills
```

Install one skill into a Codex-style local skills folder:

```bash
cp -R skills/engineering-review/devils-advocate-review "$HOME/.codex/skills/"
```

Then ask your agent to use it:

```text
Use the devils-advocate-review skill on the current branch before I push.
```

For other agent runtimes, use `catalog.json` as the index and load the relevant `SKILL.md` file as the instruction source.

## Skill Catalog

Click any skill name to open the exact `SKILL.md` file.

| Category | Skill | Use it for |
| --- | --- | --- |
| Engineering review | [`devils-advocate-review`](skills/engineering-review/devils-advocate-review/SKILL.md) | Engineering-only release review for code changes, PRs, diffs, CI, deploy readiness, regressions, generated artifacts, and launch risk. |
| Engineering review | [`public-surface-redaction-review`](skills/engineering-review/public-surface-redaction-review/SKILL.md) | Public-readiness checks for repos, packages, docs, examples, screenshots, templates, and skills before sharing. |
| Engineering execution | [`agent-worktree-coordinator`](skills/engineering-execution/agent-worktree-coordinator/SKILL.md) | Branch, worktree, generated-file, file-claim, and handoff coordination across agents or sessions. |
| Engineering execution | [`decision-ready-orchestrator`](skills/engineering-execution/decision-ready-orchestrator/SKILL.md) | Turning multi-agent research, reviews, and workstreams into one evidence-backed recommendation. |
| Browser UI | [`live-browser-proof`](skills/browser-ui/live-browser-proof/SKILL.md) | Real browser verification for UI flows, logged-in sessions, visual QA, screenshots, rendered states, and external-action boundaries. |
| Product craft | [`public-facing-writing`](skills/product-craft/public-facing-writing/SKILL.md) | READMEs, docs, websites, product copy, and brand voice work that should read like final copy, not internal reasoning. |
| Product craft | [`interface-system-design`](skills/product-craft/interface-system-design/SKILL.md) | Practical product interface design for SaaS, dashboards, admin tools, real states, existing app patterns, and browser-proven UI. |
| Product craft | [`saas-product-direction`](skills/product-craft/saas-product-direction/SKILL.md) | SaaS product thesis, prioritization, roadmap, first slice, metrics, risks, and product briefs. |
| Product craft | [`saas-gtm-strategy`](skills/product-craft/saas-gtm-strategy/SKILL.md) | SaaS ICP, positioning, offer, pricing logic, channels, funnel targets, and 90-day execution. |
| Product craft | [`create-brand-voice`](skills/product-craft/create-brand-voice/SKILL.md) | Creating a local brand voice skill from URLs, audience, tone, examples, and forbidden phrases. |

## What Is A Skill?

A skill is a small folder that teaches an agent how to handle a recurring workflow.

```text
skills/<category>/<skill-name>/SKILL.md
```

Some skills also include supporting scripts or references. For example, `create-brand-voice` includes a generator script that creates a local product-specific brand voice skill.

## Create A Brand Voice Skill

Use the brand voice generator when you want reusable writing guidance for a product, company, founder, or project:

```bash
python3 skills/product-craft/create-brand-voice/scripts/create_brand_voice_skill.py \
  --name "Example Product" \
  --website-url "https://example.com" \
  --audience "Operations teams at mid-market companies" \
  --category "Workflow automation software" \
  --tone "clear, direct, concrete, calm" \
  --avoid "hype, vague AI claims, exclamation marks" \
  --surfaces "website, docs, dashboard UI, emails"
```

Generated brand voice skills include a public-facing writing rule by default: final copy should not expose internal reasoning, process notes, private context, or implementation chatter.

## Public-Safe By Design

This repository is meant to be shared. The skills avoid:

- private company workflows,
- secrets or credentials,
- customer data,
- personal local paths,
- private roadmap or revenue details,
- tool or vendor lock-in unless a skill is intentionally scoped.

Product-specific or organization-specific variants should stay local or live in private repositories unless they are intentionally public.

## Principles

- Compact beats exhaustive.
- Evidence beats confidence.
- Verify before reporting success.
- Write for the reader, not the agent's internal process.
- Keep public artifacts free of private context.
- Prefer reusable workflows over one-off prompts.
- Keep product and GTM guidance concrete enough to act on.

## Contributing

Good additions are small, reusable workflows that help agents behave more reliably. A skill should be easy to read, easy to copy, and useful in a real session.

Avoid adding private company assumptions, secrets, customer data, personal paths, or large reference dumps.
