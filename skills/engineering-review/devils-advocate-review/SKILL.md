---
name: devils-advocate-review
description: Skeptical, release-grade engineering review workflow for coding work. Use when reviewing code changes, PRs, unstaged diffs, generated artifacts, tests, docs tied to code, CI, deploy readiness, regressions, auth boundaries, data isolation, public API/SDK surfaces, or any engineering change that must be checked before commit, push, merge, deploy, or launch.
---

# Devil's Advocate Review

Use this for engineering work only. The goal is not to collect objections; it is to find real release risk, reject false alarms, fix verified gaps, and leave clean evidence.

## Workflow

1. Pin the target.
   - Confirm repo, worktree, branch, commit range, PR, or diff.
   - Run `pwd`, `git branch --show-current`, `git status --short`, and `git diff --stat` when local.
   - If multiple checkouts exist, make sure implementation and review point at the same one.

2. Build the risk map.
   - Identify touched surfaces: API contract, auth, data model, migrations, generated output, SDK/docs, UI, deploy path, runtime, tests.
   - Name the invariants that must hold: no cross-user leakage, backward compatibility, correct permissions, generated files match source, safe deploy order.
   - Pick only the review lenses that match the risk.

3. Review independently.
   - Use subagents only when authorized and useful; otherwise run named passes yourself.
   - Reviewers inspect, cite file/line evidence, and do not edit unless assigned.
   - Ask for high-confidence or release-blocking findings. Mark speculation as likely false alarm.

4. Verify before changing.
   - Treat every finding as a hypothesis.
   - Reproduce, inspect the cited path, or prove the code path.
   - Reject findings from stale branches, wrong checkouts, unrelated dirty files, missing local setup, preference-only arguments, or accepted tradeoffs.

5. Patch real gaps.
   - Keep fixes scoped.
   - Preserve unrelated user or agent changes.
   - Use generators for generated files.
   - Add a regression test when the issue is behavioral, security-sensitive, user-visible, or likely to recur.

6. Recheck and report.
   - Run focused tests first; broaden only to match blast radius.
   - Do not commit while reviewers, tests, or long-running commands are still pending.
   - Lead with outcome: blockers found, fixes made, false alarms rejected, checks run, residual risk.

## Review Lenses

Choose the smallest useful set:

- Correctness and edge cases.
- Auth, permissions, tenancy, secrets, and data isolation.
- State lifecycle, retries, cleanup, migrations, and backward compatibility.
- Public/generated surfaces: API specs, SDKs, docs, schemas, catalogs.
- Runtime, deploy order, CI, logs, rollback, and operational diagnosis.
- UI behavior, accessibility, responsive layout, and actual rendered proof.
- Test coverage and observability.

## Delegation Prompt

```text
Review-only task. Work in exactly this checkout: <path> on branch <branch>.
Do not edit files. Run pwd, git branch --show-current, and git status --short.
Inspect <diff/PR/commit> for <risk lens>.
Return only high-confidence engineering findings with file/line refs, proof, and likely false alarms.
```

## Final Shape

```text
Outcome: <safe | fixed blockers | blocked>
Real issues: <verified findings and fixes>
False alarms: <rejected findings>
Checks: <commands and results>
Residual risk: <unrun checks or remaining decisions>
```
