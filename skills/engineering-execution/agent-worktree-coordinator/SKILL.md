---
name: agent-worktree-coordinator
description: Coordinate coding agents across branches, worktrees, shared checkouts, and generated artifacts. Use before editing when multiple sessions may touch the same repo, when starting an implementation thread, when claiming files, when running generators, or when handing off work safely.
---

# Agent Worktree Coordinator

Use this before editing in a repo that a human or another agent may also touch. The goal is simple: know where you are, claim what you will touch, avoid generated-output collisions, and hand off cleanly.

## Workflow

1. Orient.
   - Read local instructions such as `AGENTS.md`, `CONTRIBUTING.md`, or repo coordination notes.
   - Run `pwd`, `git branch --show-current`, and `git status --short`.
   - Identify whether this is a shared checkout, isolated worktree, throwaway clone, or protected release branch.

2. Claim scope.
   - If a board, lock, issue, or thread note exists, claim the exact files, surfaces, or generated artifacts.
   - Keep claims short: task, paths, generator ownership, and what others should avoid.
   - If no board exists, state the scope in your user update or branch name.

3. Pick isolation.
   - Use a branch/worktree for broad work, risky changes, reviews, long tests, or generators.
   - Stay in place only for tiny, obvious edits or when the user requested the current checkout.
   - Never reset, stash, switch, merge, rebase, or delete work you did not create without explicit approval.

4. Protect shared outputs.
   - Edit source-of-truth files, then run the official generator.
   - Treat route trees, registries, SDK output, API specs, snapshots, lockfiles, and compiled assets as one-owner-at-a-time.
   - If another active session owns the output, coordinate instead of producing churn.

5. Finish cleanly.
   - Run the narrowest meaningful checks.
   - Review `git status --short` and `git diff --stat`.
   - Mark the claim done or leave a clear handoff.

## Handoff Shape

```text
Done: <what changed>
Touched: <paths/surfaces>
Generated: <yes/no and command>
Checks: <commands and result>
Remaining: <next step or none>
Avoid: <still-owned files, if any>
```

## Hard Rules

- Preserve unrelated dirty files.
- Do not hand-edit generated output when a generator exists.
- Do not leave servers, commands, or review agents running at final.
- Do not publish, push, or merge until the target branch and public/private surface are clear.
