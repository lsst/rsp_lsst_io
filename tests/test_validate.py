"""Tests for the bundled-config validation command."""

from __future__ import annotations

from rspdocs.validate import main, validate


def test_bundled_config_validates() -> None:
    """The real shipped config must pass every bundled-config validator."""
    validate()  # must not raise against the real shipped config


def test_main_returns_zero() -> None:
    """``main`` exits 0 when the bundled config is valid."""
    assert main() == 0
