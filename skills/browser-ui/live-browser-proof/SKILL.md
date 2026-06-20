---
name: live-browser-proof
description: Verify UI behavior, logged-in workflows, visual rendering, and external web surfaces in a real browser. Use when code inspection is not enough, when existing browser state matters, when screenshots or rendered proof are needed, or before claiming a UI flow works.
---

# Live Browser Proof

Use this when the answer depends on what actually renders or what a logged-in browser can do.

## Workflow

1. Pick the browser.
   - Use the user's existing browser for cookies, extensions, logged-in accounts, or already-open apps.
   - Use an isolated/local browser for localhost, repeatable QA, and public pages.
   - Do not extract cookies, tokens, local storage, or profile data unless explicitly required and approved.

2. Set the action boundary.
   - Classify actions: read-only, local-only, draft, externally visible, paid, destructive, irreversible.
   - Stop before final send/delete/purchase/publish/permission changes unless the user approved that exact action.
   - Hand control back for MFA, CAPTCHA, passwords, or sensitive account approval.

3. Inspect and act.
   - Record URL, viewport, visible account/workspace context, and starting state.
   - Prefer roles, labels, text, and selectors over coordinates.
   - Use coordinates only when needed, then verify immediately.

4. Prove it.
   - Test desktop/mobile viewports when relevant.
   - Check loading, empty, error, disabled, success, and partial states.
   - For visual work, capture screenshots or report concrete rendered evidence.
   - For canvas/3D/animation, verify nonblank pixels, framing, and motion/interaction.

## Proof Checklist

- Correct URL/environment/account.
- Primary action reaches expected result or confirmation boundary.
- No blocking console/network errors for local app work.
- Text fits; controls are clickable; important UI does not overlap.
- Error and empty states look intentional.

## Final Shape

```text
Browser: <existing | isolated | local>
Surface: <URL/environment>
Verified: <actions>
Evidence: <screenshots/visible state/logs>
Not done: <final external actions avoided>
Issues: <bugs or none>
```
