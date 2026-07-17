"""Tests for the doc-path naming linter."""

from __future__ import annotations

import pytest

from rspdocs.pathlint import find_violations, main


@pytest.mark.parametrize(
    "path",
    [
        "docs/guides/getting-started/index.rst",
        "docs/guides/life/quotas-ani.gif",
        "docs/guides/portal/images/portal-sidebar.png",
        "docs/guides/getting-started/user-step-by-step.in.rst",
        "docs/guides/api/api.primary.in.rst",
        "docs/index.md",
        "docs/guides/logo.svg",
        # Non-docs, non-image tracked files are out of scope.
        "src/rspdocs/PathLint.py",
        "README.md",
    ],
)
def test_conforming_paths_pass(path: str) -> None:
    """Conforming (and out-of-scope) paths produce no violations."""
    assert find_violations([path]) == []


@pytest.mark.parametrize(
    "path",
    [
        "docs/guides/life/quotas_ani.gif",
        "docs/guides/notebooks/images/RSP_NB_launcher_options.png",
        "docs/guides/Bad_Name.rst",
        "docs/guides/portal/Using The Portal/index.rst",
        "docs/guides/Getting-Started/index.rst",
        "docs/guides/portal/images/portal_landing.png",
    ],
)
def test_non_conforming_paths_flagged(path: str) -> None:
    """Uppercase, underscore, or space components are flagged."""
    violations = find_violations([path])
    assert len(violations) == 1
    assert violations[0][0] == path


def test_ds_store_flagged_anywhere() -> None:
    """A tracked ``.DS_Store`` is flagged regardless of its location."""
    paths = ["docs/.DS_Store", ".DS_Store", "src/rspdocs/.DS_Store"]
    violations = find_violations(paths)
    assert {v[0] for v in violations} == set(paths)
    assert all(".DS_Store" in reason for _, reason in violations)


def test_multi_dot_suffixes_allowed() -> None:
    """``.in.rst`` and ``.primary.in.rst`` names pass unflagged."""
    paths = [
        "docs/a/foo.in.rst",
        "docs/a/foo.primary.in.rst",
    ]
    assert find_violations(paths) == []


def test_real_tree_is_clean() -> None:
    """The real tracked tree must have no naming violations."""
    assert main() == 0
