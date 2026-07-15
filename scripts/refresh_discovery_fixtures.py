#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
#     "pydantic",
#     "rubin-repertoire>=2.0",
# ]
# ///
"""Re-capture the Repertoire discovery test fixtures.

The fixtures in :file:`tests/data/discovery/` are snapshots of the per-
environment discovery JSON that Phalanx publishes. They drift as environments
change, so this script re-fetches them from the live discovery site and writes
them back in a deterministic, lint-clean format.

This is a self-contained `uv <https://docs.astral.sh/uv/>`__ script: its
dependencies are declared inline (PEP 723) and installed on demand, so no
project environment is required. The environment roster is read directly from
the in-repo shim so it stays in sync with the build.

Usage
-----
    make refresh-fixtures
    # or, directly (uv fetches the dependencies):
    uv run scripts/refresh_discovery_fixtures.py [--base-url URL]
    ./scripts/refresh_discovery_fixtures.py [--base-url URL]

Each fetched payload is validated against the ``rubin.repertoire.Discovery``
model. Environments that cannot be fetched (network error, non-2xx response)
are reported and skipped without disturbing their existing fixture, and the
loop continues so every fixture it *could* fetch is written and revalidated.
The script exits non-zero if any environment failed to fetch or failed to
validate (validation failure being a sign that the discovery schema changed
and the model may need updating).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import httpx
from pydantic import ValidationError
from rubin.repertoire import Discovery

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURE_DIR = REPO_ROOT / "tests" / "data" / "discovery"
ROSTER_FILE = REPO_ROOT / "src" / "rspdocs" / "discovery" / "environments.json"

# Mirrors rspdocs.discovery.service.DEFAULT_BASE_URL. Duplicated here so this
# stays a standalone uv script without installing the rspdocs package.
DEFAULT_BASE_URL = "https://phalanx.lsst.io/discovery/environments"


def load_roster() -> list[str]:
    """Read the environment build roster from the in-repo shim."""
    roster = json.loads(ROSTER_FILE.read_text())["build_roster"]
    return list(roster)


def refresh(base_url: str) -> int:
    """Fetch and rewrite every fixture, returning a process exit code."""
    roster = load_roster()
    FIXTURE_DIR.mkdir(parents=True, exist_ok=True)

    fetch_failures: list[str] = []
    validation_failures: list[str] = []
    for name in roster:
        url = f"{base_url}/{name}.json"
        try:
            response = httpx.get(url, timeout=30.0, follow_redirects=True)
            response.raise_for_status()
            payload = response.json()
        except httpx.HTTPError as exc:
            # Leave this environment's existing fixture untouched and keep
            # going so a single flaky env doesn't strand the others.
            fetch_failures.append(name)
            print(f"  ! {name} could not be fetched: {exc}", file=sys.stderr)
            continue

        # Write in the same format lint expects: 2-space indent, trailing
        # newline. This matches the committed fixtures byte-for-byte.
        text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
        (FIXTURE_DIR / f"{name}.json").write_text(text)
        print(f"  wrote tests/data/discovery/{name}.json")

        try:
            Discovery.model_validate(payload)
        except ValidationError as exc:
            validation_failures.append(name)
            print(
                f"  ! {name} does not validate against Discovery:\n{exc}",
                file=sys.stderr,
            )

    if fetch_failures or validation_failures:
        if fetch_failures:
            print(
                f"\n{len(fetch_failures)} environment(s) could not be "
                f"fetched: {', '.join(fetch_failures)}.\n"
                "Their existing fixtures were left unchanged.",
                file=sys.stderr,
            )
        if validation_failures:
            print(
                f"\n{len(validation_failures)} environment(s) failed "
                f"validation: {', '.join(validation_failures)}.\n"
                "The discovery schema may have changed; check whether "
                "rspdocs.discovery.models needs updating.",
                file=sys.stderr,
            )
        return 1
    print(f"\nRefreshed {len(roster)} fixtures from {base_url}.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=(
            "Base URL for the discovery JSON files "
            f"(default: {DEFAULT_BASE_URL})."
        ),
    )
    args = parser.parse_args()
    sys.exit(refresh(args.base_url))


if __name__ == "__main__":
    main()
