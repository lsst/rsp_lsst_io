"""Test rspdocs.phalanx.service."""

from __future__ import annotations

from pathlib import Path

from src.rspdocs.phalanx.service import PhalanxEnvService


def test_parse_cache() -> None:
    """Test `PhalanxEnvService.load_from_cache_file."""
    path = Path(__file__).parent.joinpath("../data/phalanxenvs.json")
    env_service = PhalanxEnvService.load_from_cache_file(path)
    assert len(env_service.envs) > 0
