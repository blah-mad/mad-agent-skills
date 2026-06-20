---
name: interface-system-design
description: Design, build, or review useful product interfaces for SaaS apps, dashboards, admin tools, and workflow software. Use when a screen needs product judgment, information hierarchy, real states, implementation fit, responsive behavior, accessibility, and rendered browser proof rather than decorative UI ideas.
---

# Practical Product Interface Design

Use this to make the actual product surface better. The taste is quiet, sharp, work-focused, and proven in the browser.

## Workflow

1. Read the product.
   - Inspect the existing app patterns before inventing new ones.
   - Identify the user, primary job, top action, scope, data objects, frequency, and failure cost.
   - Keep the change as small as the job allows.

2. Design for the work.
   - Make it obvious where the user is, what they are editing, and what the action will affect.
   - Put controls near the data or object they operate on.
   - Prefer dense, scannable layouts for SaaS, admin, and operational tools.
   - Do not turn app screens into landing pages, hero sections, or decorative card stacks.

3. Cover real states.
   - Include loading, empty, error, permission, disabled, unsaved, partial-success, and destructive-action states.
   - For tables/lists: sort, filter, pagination or virtualization, selection, bulk action, no-results.
   - For forms: validation timing, required/optional clarity, defaults, destructive confirmation, recovery.

4. Apply taste.
   - Use type, spacing, borders, and restrained color to create hierarchy.
   - Use icons where they clarify actions.
   - Keep dimensions stable under long labels, IDs, counts, translated strings, and dynamic data.
   - Avoid generic AI UI: purple gradients, glass panels, random bento grids, vague marketing copy, and cards inside cards.

5. Implement like an owner.
   - Follow the existing design system and component library.
   - Use real data shapes or realistic mocks.
   - Add new primitives only when they remove real complexity.
   - Make responsive behavior explicit.

6. Prove it.
   - Run the app when code changes.
   - Inspect desktop and mobile.
   - Check console/network errors where relevant.
   - Use screenshots or concrete rendered observations as proof.

## Review Gate

- Can a busy user find the primary action in a few seconds?
- Are scope, permissions, and destructive effects visible before action?
- Do the empty/error/loading states feel designed, not patched on?
- Does text fit without overlap or layout shift?
- Is the interface useful before it is pretty?
- Was the rendered UI actually inspected?

## Output Shape

```text
Decision: <design/build/review recommendation>
Surface: <user/job/scope/failure cost>
Changes: <structure, states, visual system, interaction>
Implementation: <code or plan>
Proof: <browser checks, screenshots, or remaining risk>
```
