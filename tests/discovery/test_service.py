"""Test `PhalanxEnvService.load` with mocked discovery endpoints."""

from __future__ import annotations

from pathlib import Path

import httpx
import respx

from rspdocs.discovery.service import DEFAULT_BASE_URL, PhalanxEnvService

from .conftest import ENV_NAMES


@respx.mock
def test_load_from_network(
    tmp_path: Path, discovery_texts: dict[str, str]
) -> None:
    """`load` fetches every roster environment and caches the raw JSON."""
    for name, text in discovery_texts.items():
        respx.get(f"{DEFAULT_BASE_URL}/{name}.json").mock(
            return_value=httpx.Response(200, text=text)
        )

    service = PhalanxEnvService.load(cache_dir=tmp_path)

    assert set(service.envs.env_names) == set(ENV_NAMES)
    # The primary environment is accessible and is idfprod.
    assert service.envs.primary.name == "idfprod"
    # Times Square is hidden on idfprod via the in-repo shim.
    assert service.envs["idfprod"].times_square_url is None
    assert service.envs["idfprod"].has_apps is False
    # ...but idfint (a staff env) follows discovery and shows it.
    assert service.envs["idfint"].times_square_url is not None
    # WebDAV is present on base now that discovery reports it.
    assert service.envs["base"].api_webdav_url is not None

    # The raw discovery JSON is written to the cache for each environment.
    for name, text in discovery_texts.items():
        cache_file = tmp_path / f"{name}.json"
        assert cache_file.exists()
        assert cache_file.read_text() == text


@respx.mock
def test_load_with_custom_base_url(
    tmp_path: Path, discovery_texts: dict[str, str]
) -> None:
    """`load` honors a custom base URL."""
    base_url = "https://example.test/discovery/environments"
    for name, text in discovery_texts.items():
        respx.get(f"{base_url}/{name}.json").mock(
            return_value=httpx.Response(200, text=text)
        )

    service = PhalanxEnvService.load(cache_dir=tmp_path, base_url=base_url)

    assert len(service.envs) == len(ENV_NAMES)
