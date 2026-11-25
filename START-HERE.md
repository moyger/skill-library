# Getting started with Skill Library

The [library overview](README.md#browse-by-category) lists available and planned categories. This guide covers the available design skills, with examples and setup instructions.

## Find a design skill by task

| I need to… | Collection | Skill |
| --- | --- | --- |
| Choose a visual direction from reference images | Design direction | [Moodboard to Direction](skills/design-direction/moodboard-to-direction/SKILL.md) |
| Turn a brief into a screen with a clear main action | UI design | [Design a screen layout](skills/ui-design/design-screen-layout/SKILL.md) |
| Help someone compare values or find a record | UI design | [Design a data view](skills/ui-design/design-data-view/SKILL.md) |
| Brief artwork for a hero image, onboarding step or empty state | UI design | [Define UI illustration](skills/ui-design/define-ui-illustration/SKILL.md) |
| Set text styles that work across several screens | Design systems | [Design UI typography](skills/design-systems/design-ui-type/SKILL.md) |
| Define colours for actions, states and themes | Design systems | [Design UI colour and dark mode](skills/design-systems/design-ui-colour/SKILL.md) |
| Find what makes an existing screen hard to follow and decide what to improve first | Design review | [Screen Critique](skills/design-review/screen-critique/SKILL.md) |
| Correct a specific problem in a design and compare the result with the original | UI design | [Fix a Design Finding](skills/ui-design/fix-design-finding/SKILL.md) |
| Find where an existing screen breaks across widths, inputs or mobile platforms | Design review | [Review an adaptive interface](skills/design-review/review-adaptive-ui/SKILL.md) |

## Try it on a project

For a service website, start with **Moodboard to Direction** if the look is still open. Attach a Figma frame or 3–5 reference images and ask for two directions that make the coverage check easy to find. Once you have a direction, use **Design a screen layout** to place the suburb field and quote action. Show a coverage result once the business has confirmed its service areas. Use **Review an adaptive interface** once there is a frame or build to inspect.

For a reporting app, start with **Design a data view** if the open question is which figures, chart or table will help someone decide. Use **Design a screen layout** when you know what data to show and need to arrange it alongside filters and actions.

For an existing page, start with **Screen Critique** to review the reading order, grouping and main action. Use **Fix a Design Finding** when you have chosen a correction. For example, if a workshop schedule clips a date, adjust the row and check both the longest date and its neighbouring booking button at the original width.

## Use the library in every local project

From this repository, run `python3 scripts/install-design-skills.py` once. It links each skill into your personal Codex and Claude Code folders on this Mac. To see the planned links first, add `--preview`. The installer checks for name conflicts before writing and keeps links that already point here.

Open a new session in any project. In Codex, type `$screen-critique` and add the frame link or screenshot. In Claude Code, type `/screen-critique` followed by the same request. For example, ask “Can a visitor find where to request a quote? Rank the findings.” Check that the skill appears in the picker before using it.

Edit skills here to update the linked versions. Run the installer again when you add a skill. Keep this library at the same path so its links keep working.

## Share one skill with a project

Open the skill from the table and copy the whole folder containing its `SKILL.md`. For example, copy `skills/ui-design/design-screen-layout/` to `.agents/skills/design-screen-layout/` in a Codex project or `.claude/skills/design-screen-layout/` in a Claude Code project. For redistribution, include the root `LICENSE` alongside the skill and retain its bundled upstream notice if present. In another chat app, attach the skill instructions, any supporting files it calls for, and the task inputs.

## Where new skills go

Readers browse by category, then by task. For example, **Design → Design review → Screen Critique** leads to `skills/design-review/screen-critique/SKILL.md`. The category groups related collections in the README. Each skill has one folder at `skills/<collection>/<skill-name>/SKILL.md`.

When the first skill in a planned category is ready, link the category to its task list in the README and give the skill a one-sentence description. Add new design skills to the design table above.

Six skills adapt the UI Design collection from [Designer Skills](https://github.com/Owl-Listener/designer-skills). Screen Critique adapts the same project's Visual Critique collection. Each adapted folder includes the original MIT notice. The [worked examples](skills/design-direction/moodboard-to-direction/references/worked-examples.md) show how to choose a direction for a fictional booking page and a library returns desk. Trials of the six adapted skills are pending.

## Roadmap

| Phase | Skills | Proof before adding more |
| --- | --- | --- |
| 1. Design | Moodboard to Direction → Design Brief → Screen Critique → UI Kit & Handoff | Try the first skill on a simple marketing page, then on a data-heavy app. Keep the same workflow; swap the brief and inputs. |
| 2. Engineering | Grill Me → buildable spec; Verifier → evidence against acceptance criteria; Code Review → findings against the spec and diff; Retro → one change to improve the next run | Use on one real change. Record what the agent actually ran or inspected, and what remains unverified. |
| 3. Software factory | Connect proven skills into a spec → small tasks → build → verify → review loop | Start with explicit human checkpoints and reproducible tests. Automate handoffs only after they are reliable manually. |

Keep strategy notes next to the skills: one problem, one decision, one way you checked it. Version the skill from what real runs teach you.

The GitHub repository is `moyger/skill-library`. Use fictional examples or material already intended for public sharing. The [MIT licence](LICENSE) covers original work. Retain upstream notices for any code or instructions you copy or adapt.

Inspiration: [Designer Skills](https://github.com/Owl-Listener/designer-skills), [AI Hero](https://www.aihero.dev/skills), and the [Agent Skills standard](https://agentskills.io/specification).
