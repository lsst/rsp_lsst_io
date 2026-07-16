"""Validate the bundled, hand-edited rspdocs config files without a build."""

from __future__ import annotations

import sys

from pydantic import ValidationError
from sphinx.errors import ConfigError

__all__ = ["main", "validate"]


def validate() -> None:
    """Run every bundled-config validator; raise on the first failure."""
    # Importing services validates page_excludes.yaml at import time and
    # re-loads the roster (KNOWN_ENVS).
    import rspdocs.sphinxext.services  # noqa: F401

    from .discovery.metadata import load_environments_metadata
    from .sphinxext import _check_token_namespaces_disjoint

    load_environments_metadata()  # build_roster subset of environments
    _check_token_namespaces_disjoint()  # token name-spaces disjoint


def main() -> int:
    """Run the validators, reporting the first failure to stderr.

    Returns
    -------
    int
        ``0`` if the bundled config is valid, ``1`` otherwise. Wrapped by the
        ``rspdocs-validate-config`` console script as the process exit code.
    """
    try:
        validate()
    except (ValidationError, ValueError, TypeError, ConfigError) as exc:
        print(f"Bundled rspdocs config is invalid:\n  {exc}", file=sys.stderr)
        return 1
    print("Bundled rspdocs config is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
