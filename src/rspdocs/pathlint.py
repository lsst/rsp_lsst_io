"""Lint git-tracked doc paths for lowercase, hyphen-separated names."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import PurePosixPath

__all__ = ["find_violations", "main"]

#: Content file extensions whose paths are linted (images plus source pages).
LINTED_SUFFIXES = frozenset(
    {".rst", ".md", ".png", ".gif", ".jpg", ".jpeg", ".svg"}
)

#: A conforming path component: lowercase letters, digits, hyphens, and dots.
#: Dots let multi-suffix names such as ``foo.in.rst`` and
#: ``foo.primary.in.rst`` pass; hyphens are the only word separator.
_COMPONENT_RE = re.compile(r"^[a-z0-9][a-z0-9.-]*$")


def _tracked_files() -> list[str]:
    """Return every git-tracked path in the repository (POSIX-style).

    Paths are relative to the repository root regardless of the current
    working directory: the ``:/`` pathspec scans the whole tree and
    ``--full-name`` reports root-relative paths, so running the linter from
    a subdirectory can't silently pass on an unscanned subtree.
    """
    result = subprocess.run(
        ["git", "ls-files", "-z", "--full-name", "--", ":/"],
        capture_output=True,
        check=True,
        text=True,
    )
    return [path for path in result.stdout.split("\0") if path]


def _bad_component(path: PurePosixPath) -> str | None:
    """Return the first non-conforming path component, or ``None`` if clean."""
    for component in path.parts:
        if not _COMPONENT_RE.match(component):
            return component
    return None


def find_violations(paths: list[str]) -> list[tuple[str, str]]:
    """Find naming violations among ``paths``.

    Parameters
    ----------
    paths
        Repository-relative paths (POSIX ``/`` separators).

    Returns
    -------
    list[tuple[str, str]]
        One ``(path, reason)`` pair per violation, in the input order.
    """
    violations: list[tuple[str, str]] = []
    for raw in paths:
        path = PurePosixPath(raw)
        if path.name == ".DS_Store":
            violations.append((raw, "tracked .DS_Store file"))
            continue
        if raw.startswith("docs/") and path.suffix.lower() in LINTED_SUFFIXES:
            bad = _bad_component(path)
            if bad is not None:
                violations.append(
                    (
                        raw,
                        f"path component {bad!r} is not lowercase, "
                        "hyphen-separated ([a-z0-9.-], no uppercase, "
                        "underscores, or spaces)",
                    )
                )
    return violations


def main() -> int:
    """Lint git-tracked doc paths, reporting each violation to stderr.

    Returns
    -------
    int
        ``0`` if every tracked path conforms, ``1`` otherwise. Wrapped by the
        ``rspdocs-lint-paths`` console script as the process exit code.
    """
    violations = find_violations(_tracked_files())
    if violations:
        print("Non-conforming tracked paths:", file=sys.stderr)
        for path, reason in violations:
            print(f"  {path}: {reason}", file=sys.stderr)
        return 1
    print("All tracked doc paths conform.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
