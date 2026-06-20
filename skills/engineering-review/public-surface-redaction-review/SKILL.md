---
name: public-surface-redaction-review
description: Review a repo, package, docs set, generated artifact, skill, screenshot, demo, SDK, example, or template before public sharing. Use when making something public or shareable and it must not leak secrets, personal paths, customer data, private org names, internal process, implementation details, or live-looking credentials.
---

# Public Surface Redaction Review

Use this before publishing anything that came from a private working context.

## Workflow

1. Define the surface.
   - What is being shared: repo, folder, package, docs, site, SDK, skill, screenshot, video, dataset, prompt, or template.
   - Where it goes: public GitHub, marketplace, customer docs, partner handoff, package registry, or share link.
   - Which files are generated and what source owns them.

2. Scan content and metadata.
   - Inspect names, frontmatter, comments, README, catalog, package metadata, examples, scripts, images, and CI/deploy files.
   - Search for org names, personal paths, usernames, emails, customer names, codenames, tunnel URLs, internal hosts, account IDs, tokens, keys, cookies, webhooks, env values, and live-looking credentials.
   - Inspect screenshots/media for account switchers, profile data, notifications, billing, paths, keys, customer data, or unreleased names.

3. Make it public-useful.
   - Replace private examples with generic examples that still teach the workflow.
   - Remove assumptions that only make sense inside one company or deployment.
   - Keep implementation details only when a public user needs them.

4. Handle real leaks correctly.
   - If a real secret was exposed remotely, report it and recommend rotation. Redaction alone is not enough.
   - Rewrite history only with explicit owner approval.
   - Fix source files, then regenerate generated output.

## Useful Checks

```bash
rg -n -i "(secret|token|api[_-]?key|password|cookie|bearer|private key|webhook|localhost|ngrok|customer|internal|do not share)" .
rg -n "/Users|/home|C:\\\\Users|@[A-Za-z0-9._%+-]+\\.[A-Za-z]{2,}" .
git status --short
git diff --stat
```

## Redaction Rules

- Use `example.com`, `acme`, `org_123`, and `user_123` for placeholders.
- Do not publish masked secrets if surrounding context reveals the real account or service.
- Do not publish private roadmap, revenue, legal, security, customer, or internal process details without owner approval.
- Check binary assets manually.

## Final Shape

```text
Public readiness: safe | blocked | safe with gaps
Scope: <paths/artifacts>
Changed: <redactions/genericization>
Checks: <commands/manual review>
Residual risk: <history, binaries, external links, screenshots, unrun checks>
Next: <publish, rotate, regenerate, or owner decision>
```
