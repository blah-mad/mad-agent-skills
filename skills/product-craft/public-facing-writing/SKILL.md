---
name: public-facing-writing
description: Write or review public-facing copy without exposing internal agent reasoning, process notes, private context, or implementation chatter. Use for READMEs, docs, website copy, product pages, marketplace listings, release notes, brand voice work, support copy, onboarding copy, and any text meant for users, customers, developers, candidates, partners, or the public.
---

# Public-Facing Writing

Use this when the output should read like finished copy, not an explanation of how the agent thought about the copy.

## Workflow

1. Identify the reader.
   - Who is reading: user, customer, developer, buyer, partner, contributor, candidate, teammate, or public audience.
   - What should they understand or do next?
   - What does this surface need to earn: trust, clarity, action, confidence, or orientation?

2. Separate reasoning from copy.
   - Think through structure privately.
   - Write the final artifact directly.
   - Do not include internal analysis, prompt interpretation, implementation notes, review commentary, or "I changed this because..." unless the user explicitly asked for a changelog or explanation.

3. Write for the surface.
   - README/docs: what it is, who it is for, what is included, how to use it.
   - Website/product copy: problem, promise, proof, next action.
   - UI/help/support copy: what happened, what the user can do, what changes next.
   - Release notes/changelogs: what changed, why it matters, migration or action needed.

4. Remove internal tells.
   - No "the goal is", "this repo intentionally", "we should", "maybe", "I think", "as an AI", or process narration unless it belongs to the surface.
   - No private org details, local paths, secret names, customer data, roadmap leaks, or implementation details that readers do not need.
   - No vague hype, filler, or over-explaining.

5. Final scan.
   - Is it written for the reader, not the writer?
   - Are links and examples useful?
   - Is the next action clear?
   - Could this be published as-is?

## Output Shape

For writing tasks, provide the finished copy first.

For review tasks:

```text
Verdict: <publishable | needs edits>
Issues: <reader-facing problems>
Rewrite: <improved copy or key sections>
Notes: <only if needed>
```
