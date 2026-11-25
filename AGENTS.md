# Repository Guidelines

## Project Structure

This repository holds portable instructions for AI agents. `START-HERE.md` explains how to try the library and its roadmap. Each skill lives in its own folder under `skills/`, with a `SKILL.md` entry point and optional supporting files such as `references/pilot-cases.md`. Keep examples and notes beside the skill they support. Use fictional names, sample data and shareable artwork in examples. Keep private briefs, screenshots and internal file paths outside the library.

## Adding or Updating a Skill

Use a short, lowercase, hyphen-separated folder name, such as `moodboard-to-direction`. Give each `SKILL.md` valid YAML frontmatter with a `name` and a clear `description`. Write steps an agent can follow, state what inputs it needs, and say what the output should contain. Link to supporting files with relative paths. Keep the editable master in this repository; install or copy it into client-specific skill folders rather than editing multiple copies.

## Development and Checks

There is no build command or automated test suite in the current project. To review the library, list the files with `find skills -type f`, read the changed `SKILL.md`, and check that every linked reference exists. Try meaningful instruction changes on a real task and record what was checked and what remains unverified. Do not claim a check passed unless you performed it.

## Writing Style

Use Markdown headings, short paragraphs, and numbered steps for workflows. Keep instructions specific to the task. Separate things visible in a reference from suggestions or assumptions. Prefer the project's existing design tokens and components when a skill discusses UI. Tell the agent when to ask a focused question, when to stop, and what actions need the user's request.

## Changes and Reviews

Use a short action-oriented commit title when committing. In a pull request, explain the user problem, list changed skills, describe a real example or check, and note unverified behavior. Remove client screenshots and private material unless they are cleared for sharing. Document the source and keep its licence notices with any copied or adapted material.
