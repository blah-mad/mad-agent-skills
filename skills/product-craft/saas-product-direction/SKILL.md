---
name: saas-product-direction
description: Define product direction and execution guidance for SaaS products. Use when deciding what to build next, setting roadmap strategy, prioritizing initiatives, writing product briefs, aligning teams, choosing success metrics, or evaluating product tradeoffs for B2B, B2B2C, prosumer, or product-led SaaS.
---

# SaaS Product Direction

Use this to turn product ambiguity into a sharp thesis, a few bets, and an executable first slice. Avoid long roadmaps that hide the real decision.

## Workflow

1. Snapshot context.
   - Stage, users, buyers, admins, current objective, baseline metrics.
   - Evidence: calls, tickets, usage, churn, win/loss, sales objections, design partners.
   - Constraints: capacity, deadline, tech debt, migration risk, trust, compliance, runway, commitments.

2. Frame the problem.
   - Who is struggling?
   - What are they trying to do?
   - What fails today?
   - How often and how costly is it?
   - Why now?
   - Separate symptoms from root cause before accepting a feature request.

3. Write the thesis.
   - Objective: one measurable outcome.
   - Bets: one to three, each tied to evidence.
   - Mechanism: why the bets should move the objective.
   - Non-goals: attractive work to avoid now.
   - Guardrails: trust, privacy, reliability, performance, support, platform.

4. Prioritize.
   - Score by pain/frequency, business impact, strategic leverage, confidence, time to learn, complexity, operational burden, and trust risk.
   - Prefer fewer sharper bets.
   - State what will not ship because this does.

5. Plan the first slice.
   - Now / Next / Later tied to outcomes, not feature inventory.
   - For each Now item: behavior change, success metric, failure threshold, validation method, dependency, owner, review cadence.

6. Write the brief when implementation is likely.
   - Problem, objective, users, scenarios, requirements, non-requirements, UX/API shape, edge cases, metrics, rollout, docs, open decisions.

## Quality Gate

- One primary objective.
- Bets tied to evidence.
- First slice small enough to learn from.
- Metrics measurable.
- Tradeoffs and non-goals explicit.
- Trust, privacy, reliability, and support risks visible.

## Output Shape

```text
Recommendation: <product move>
Thesis: <problem/objective/bets/mechanism/non-goals>
Priorities: <ranked rationale>
Roadmap: <Now / Next / Later>
First slice: <brief and validation>
Metrics: <success/failure/review cadence>
Risks: <assumptions and decisions>
```
