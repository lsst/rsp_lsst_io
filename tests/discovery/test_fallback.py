"""Test the offline cache fallback of `PhalanxEnvService.load`."""

from __future__ import annotations

from pathlib import Path

import httpx
import pytest
import respx

from rspdocs.discovery.service import DEFAULT_BASE_URL, PhalanxEnvService

from .conftest import ENV_NAMES


@respx.mock
def test_fallback_to_cache(
    tmp_path: Path,
    discovery_texts: dict[str, str],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """When the network fails, `load` uses the cache and prints a banner."""
    # Every request fails as if there were no network.
    for name in ENV_NAMES:
        respx.get(f"{DEFAULT_BASE_URL}/{name}.json").mock(
            side_effect=httpx.ConnectError("no network")
        )
    # Pre-seed the cache with the fixtures.
    for name, text in discovery_texts.items():
        (tmp_path / f"{name}.json").write_text(text)

    service = PhalanxEnvService.load(cache_dir=tmp_path)

    assert set(service.envs.env_names) == set(ENV_NAMES)
    assert service.envs.primary.name == "idfprod"

    captured = capsys.readouterr()
    # A loud banner is printed for each fallen-back environment.
    assert "could not fetch discovery data" in captured.out
    assert "Falling back to the cached copy" in captured.out
    assert "idfprod" in captured.out


@respx.mock
def test_fallback_without_cache_raises(tmp_path: Path) -> None:
    """With no network and no cache, `load` raises."""
    for name in ENV_NAMES:
        respx.get(f"{DEFAULT_BASE_URL}/{name}.json").mock(
            side_effect=httpx.ConnectError("no network")
        )

    with pytest.raises(RuntimeError, match="no cached copy"):
        PhalanxEnvService.load(cache_dir=tmp_path / "empty")
