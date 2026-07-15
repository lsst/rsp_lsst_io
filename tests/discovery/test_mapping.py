"""Test `PhalanxEnv.from_discovery` mapping from discovery data."""

from __future__ import annotations

from pathlib import Path

from rubin.repertoire import Discovery

from rspdocs.discovery.metadata import EnvMeta
from rspdocs.discovery.models import PhalanxEnv


def _load(name: str, discovery_data_dir: Path) -> Discovery:
    text = (discovery_data_dir / f"{name}.json").read_text()
    return Discovery.model_validate_json(text)


def test_public_env_mapping(discovery_data_dir: Path) -> None:
    """A public environment with datasets maps all service URLs."""
    discovery = _load("idfprod", discovery_data_dir)
    meta = EnvMeta(title="data.lsst.cloud", title_full="data.lsst.cloud")

    env = PhalanxEnv.from_discovery(discovery, name="idfprod", meta=meta)

    assert env.name == "idfprod"
    assert env.title == "data.lsst.cloud"
    assert env.domain == "data.lsst.cloud"
    assert str(env.squareone_url) == "https://data.lsst.cloud/"
    # UI service URLs come straight from discovery.
    assert str(env.portal_url) == str(discovery.services.ui["portal"].url)
    assert str(env.nb_url) == str(discovery.services.ui["nublado"].url)
    assert str(env.api_webdav_url) == str(discovery.services.ui["webdav"].url)
    # Derived VO API URLs (datasets are present for idfprod).
    assert str(env.api_url) == "https://data.lsst.cloud/api/"
    assert str(env.api_tap_url) == "https://data.lsst.cloud/api/tap/"
    # Derived auth and Phalanx-docs URLs.
    assert str(env.gafaelfawr_tokens_url) == (
        "https://data.lsst.cloud/auth/tokens/"
    )
    assert str(env.phalanx_docs_url) == (
        "https://phalanx.lsst.io/environments/idfprod/"
    )


def test_times_square_present(discovery_data_dir: Path) -> None:
    """Times Square is derived when discovery reports it and it is not
    hidden.
    """
    discovery = _load("idfdev", discovery_data_dir)
    assert "times-square" in discovery.services.internal
    meta = EnvMeta(title="Rubin IDF (Dev)")

    env = PhalanxEnv.from_discovery(discovery, name="idfdev", meta=meta)

    assert str(env.times_square_url) == (
        "https://data-dev.lsst.cloud/times-square/"
    )
    assert env.has_apps is True


def test_hidden_times_square(discovery_data_dir: Path) -> None:
    """A service in ``hidden_services`` is treated as absent."""
    discovery = _load("idfprod", discovery_data_dir)
    # Discovery *does* report times-square for idfprod...
    assert "times-square" in discovery.services.internal
    meta = EnvMeta(
        title="data.lsst.cloud",
        title_full="data.lsst.cloud",
        hidden_services=["times-square"],
    )

    env = PhalanxEnv.from_discovery(discovery, name="idfprod", meta=meta)

    # ...but the override hides it, keeping parity with today's public site.
    assert env.times_square_url is None
    assert env.has_apps is False


def test_staff_env_without_datasets(discovery_data_dir: Path) -> None:
    """An environment without datasets has no VO API URLs, but still exposes
    WebDAV now that discovery reports it.
    """
    discovery = _load("base", discovery_data_dir)
    assert discovery.datasets == {}
    meta = EnvMeta(title="Rubin Base Data Facility")

    env = PhalanxEnv.from_discovery(discovery, name="base", meta=meta)

    assert env.api_url is None
    assert env.api_tap_url is None
    assert env.times_square_url is None
    assert env.has_apps is False
    # WebDAV is now reported by discovery for all environments.
    assert str(env.api_webdav_url) == str(discovery.services.ui["webdav"].url)
    assert env.is_primary is False


def test_primary_env_flag(discovery_data_dir: Path) -> None:
    """The primary environment (idfprod) sets ``is_primary``."""
    discovery = _load("idfprod", discovery_data_dir)
    meta = EnvMeta(title="data.lsst.cloud", title_full="data.lsst.cloud")

    env = PhalanxEnv.from_discovery(discovery, name="idfprod", meta=meta)

    assert env.is_primary is True
    assert env.ltd_url_prefix == "https://rsp.lsst.io/"
