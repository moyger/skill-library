"""Link the library into the user's local Codex and Claude Code skill folders."""

import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", action="store_true", help="List pending links without writing.")
    args = parser.parse_args()
    library = Path(__file__).resolve().parents[1] / "skills"
    skills = sorted(entry.parent for entry in library.glob("*/*/SKILL.md"))
    if not skills or len({skill.name for skill in skills}) != len(skills):
        parser.exit(1, "Expected at least one skill and unique skill folder names.\n")

    home = Path.home()
    pending = []
    conflicts = []
    for skill in skills:
        for folder in (home / ".agents/skills", home / ".claude/skills"):
            link = folder / skill.name
            if link.is_symlink() and link.resolve() == skill:
                continue
            if link.exists() or link.is_symlink():
                conflicts.append(link)
            else:
                pending.append((link, skill))

    if conflicts:
        for link in conflicts:
            print(f"Name already in use: {link}", file=sys.stderr)
        parser.exit(1, "Existing entries were preserved.\n")

    for link, skill in pending:
        if args.preview:
            print(f"Would link {link} to {skill}")
        else:
            link.parent.mkdir(parents=True, exist_ok=True)
            link.symlink_to(skill, target_is_directory=True)
    action = "pending" if args.preview else "created"
    print(f"{len(skills)} skills, {len(pending)} links {action}.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError) as error:
        sys.exit(f"Could not finish linking skills: {error}")
