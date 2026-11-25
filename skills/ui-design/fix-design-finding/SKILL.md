---
name: fix-design-finding
description: Apply a requested correction to an existing interface and check the rendered result against the original. Use for a specific design finding in a Figma frame, component or working page.
---

# Fix a Design Finding

Start with the reported problem, the editable target and what the user wants changed. A screenshot can document the issue. If it is the only input and the user expects a source edit, ask for the design file or implementation and give the exact proposed correction in the meantime.

1. Locate the element in context. Inspect it at the width, state and content where the problem occurred. Capture a before view or record the relevant measurements. If it already looks correct, report what you saw and seek the missing condition before changing it.
2. Define what success would look like. For cropped artwork, the whole intended mark must fit at its original proportions. For a proposal about reading order, specify what to compare. When the user requests an exploration, make a variant they can compare with the original.
3. Find the cause. Check the containing frame, constraints, shared component or style before editing. Apply the smallest change that solves the requested problem. For a problem specific to one placement, use the local instance or container. A shared change calls for checking another affected use.
4. Inspect the rendered result under the original conditions. Check the nearest label, control or layout edge for unwanted movement. If the finding involved interaction, repeat the affected action. If verification is blocked, distinguish the edit you made from the result that still needs checking.

Deliver the edited location and a short before-and-after account. Name the check performed and its outcome. For a design experiment, describe the visible difference and what still needs user feedback.

**Example.** A footer has a 48 × 84 px slot for a 60.48 × 105.84 px logo. Both shapes have the same proportions. Fit the artwork to 48 × 84 px within the slot. Check all four edges and the wordmark beside the neighbouring footer text at normal size.
