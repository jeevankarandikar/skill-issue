#!/usr/bin/env python3
"""Install everything in this repository for Claude Code, Cursor and Codex.

    python3 install.py            every agent whose config folder exists
    python3 install.py --cursor   only the ones named (--claude, --cursor, --codex)
    python3 install.py --remove   take it all out again

It links the design skill into each agent's skills folder, wires the writing
guard into each agent's hooks, and sets up the usage gauge for Cursor and Codex. Both point at this clone, so `git pull` updates
them. Running it twice changes nothing.
"""
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HOME = Path.home()
SKILL = "design-jeev"
# agent: (config folder, skills folder)
AGENTS = {
    "claude": (Path(os.environ.get("CLAUDE_CONFIG_DIR") or HOME / ".claude"), None),
    "cursor": (HOME / ".cursor", None),
    "codex": (Path(os.environ.get("CODEX_HOME") or HOME / ".codex"), HOME / ".agents" / "skills"),
}


def link(agent: str, remove: bool) -> str:
    root, skills = AGENTS[agent]
    target = (skills or root / "skills") / SKILL
    if target.is_symlink():
        if target.resolve() == HERE / SKILL and not remove:
            return f"no change: {target}"
        target.unlink()
    elif target.exists():
        return f"{target} is a real folder, left alone. Move it away and run this again."
    if remove:
        return f"unlinked {target}"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.symlink_to(HERE / SKILL, target_is_directory=True)
    return f"linked {target}"


def main() -> None:
    remove = "--remove" in sys.argv
    named = [a for a in AGENTS if f"--{a}" in sys.argv]
    chosen = named or [a for a in AGENTS if AGENTS[a][0].is_dir()]
    if not chosen:
        raise SystemExit("no Claude Code, Cursor or Codex config folder found; name one, for example --claude")
    for agent in chosen:
        print(f"{agent}: {link(agent, remove)}")
    flags = [f"--{a}" for a in chosen] + (["--remove"] if remove else [])
    subprocess.run([sys.executable, str(HERE / "writing-guard" / "install.py"), *flags], check=True)
    rest = [f"--{a}" for a in chosen if a != "claude"]
    if rest:
        gauge = HERE / "fleet-gauge" / "other-agents" / "install.py"
        subprocess.run([sys.executable, str(gauge), *rest, *flags[len(chosen):]], check=True)


if __name__ == "__main__":
    main()
