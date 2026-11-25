---
name: review-adaptive-ui
description: Review an existing screen across widths, input methods or native platforms. Use for responsive layout checks and iOS or Android design reviews.
---

# Review an adaptive interface

Identify the main task, supported platforms, and evidence available. Record whether each finding comes from a live build, a frame at a known size or a written design. A frame can show clipping. Keyboard or back-button behaviour needs interaction evidence.

1. Follow the same task at the supplied narrow and wide sizes. Check the width where columns collapse, including just either side when resizing is possible. Look for lost actions, mismatched reading order, clipped labels and tables that lose row identity.
2. Check how each action works with the supported inputs. Inspect focus order, visible focus, tap areas and access to details normally shown on hover. Try enlarged text and long values where possible.
3. For native apps, trace a concrete route such as list → detail → dialog → return. Compare back, dismissal, system gestures, keyboard overlap, text scaling and insets with the conventions of the target OS version. Use the current official platform guidance when making a compliance claim.
4. Describe the smallest change that preserves the task. For example, when filters move into a drawer, keep the active filter count visible and preserve selections when the drawer closes.

Deliver findings in task-impact order. Give the screen, width or device, observed problem, suggested fix and a repeatable check. List interactions or platforms still awaiting inspection.

Adapted from [Designer Skills](https://github.com/Owl-Listener/designer-skills), UI Design. [Upstream licence](UPSTREAM-LICENSE.txt).
