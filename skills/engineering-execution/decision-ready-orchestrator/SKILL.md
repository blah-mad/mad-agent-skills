---
name: decision-ready-orchestrator
description: Orchestrate multi-step agent work into decision-ready outputs. Use when coordinating subagents, parallel reviews, research tasks, implementation queues, issue triage, or any workflow where the owner needs clear options and evidence instead of raw agent chatter.
---

# Decision-Ready Orchestrator

Use this when several threads, agents, tools, repos, or research paths need to converge into one recommendation. The job is not to summarize everything; it is to remove ambiguity until the next action is obvious.

## Workflow

1. Frame the decision.
   - State the objective in one sentence.
   - Name the decision, if any: ship, fix first, choose option, pause, publish, rollback, or reject.
   - Define what evidence would make that decision credible.

2. Split by perspective.
   - Assign narrow scopes: implementation, tests, security, public surface, docs, UX, performance, migration, customer workflow.
   - Give exact repo/path, branch, files, URLs, commands, and edit permissions.
   - Review-only agents do not edit.

3. Classify work.
   - `Autonomous`: safe to do now.
   - `Needs owner`: product, brand, legal, budget, public-action, or security call.
   - `Unsafe`: risks data, money, production state, permissions, public reputation, or git history.
   - `Blocked`: missing access, environment, dependency, secret, or user input.

4. Verify claims.
   - Require file/line refs, command results, screenshots, logs, metrics, or reproduction steps.
   - Treat agent reports as hypotheses until checked.
   - Collapse duplicates and reject stale-branch, wrong-repo, or preference-only findings.

5. Turn it into action.
   - Patch verified safe items.
   - Escalate only decisions the agent cannot responsibly make.
   - Keep unrelated refactors out.

## Delegation Prompt

```text
Task: <narrow objective>
Checkout/URL: <target>
Mode: review-only | implementation | research | verification
Scope: <files, surfaces, commands>
Do not: <boundaries>
Return: evidence, confidence, and next action
```

## Decision Brief

```text
Recommendation: <action>
Why: <evidence-backed reason>
Done: <completed work>
Verified: <checks/proof>
Risks: <remaining risk>
Owner decision: <only if needed>
Next: <single concrete step>
```

## Bar

- Do not forward unverified claims.
- Do not ask the owner questions you can answer by inspecting, testing, or researching.
- Do not let parallel agents overlap edits without ownership.
