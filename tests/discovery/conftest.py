"""Shared fixtures for the discovery test suite."""

from __future__ import annotations

from pathlib import Path

import pytest

ENV_NAMES = [
    "base",
    "idfdev",
    "idfint",
    "idfprod",
    "summit",
    "tucson-teststand",
    "usdfdev",
    "usdfprod",
]
"""The environments captured as discovery fixtures."""


@pytest.fixture
def discovery_data_dir() -> Path:
    """Directory holding the captured per-environment discovery JSON."""
    return Path(__file__).parent.parent / "data" / "discovery"


@pytest.fixture
def discovery_texts(discovery_data_dir: Path) -> dict[str, str]:
    """The raw discovery JSON text for each environment, keyed by name."""
    return {
        name: (discovery_data_dir / f"{name}.json").read_text()
        for name in ENV_NAMES
    }
