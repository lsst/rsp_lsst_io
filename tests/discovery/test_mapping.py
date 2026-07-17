"""Test `PhalanxEnv.from_discovery` mapping from discovery data."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
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
    # WebDAV is normalized to a trailing slash (discovery gives .../files).
    assert str(env.api_webdav_url) == "https://data.lsst.cloud/files/"
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


def test_webdav_url_has_trailing_slash(discovery_data_dir: Path) -> None:
    """The WebDAV URL ends in a slash so the documented server address
    ``<url>(your_username)`` renders correctly.
    """
    discovery = _load("idfprod", discovery_data_dir)
    meta = EnvMeta(title="data.lsst.cloud", title_full="data.lsst.cloud")

    env = PhalanxEnv.from_discovery(discovery, name="idfprod", meta=meta)

    assert str(env.api_webdav_url).endswith("/")
    assert (
        f"{env.api_webdav_url}(your_username)"
        == "https://data.lsst.cloud/files/(your_username)"
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
    # WebDAV is now reported by discovery for all environments, normalized to
    # a trailing slash (discovery gives .../files).
    assert str(env.api_webdav_url) == "https://base-lsp.lsst.codes/files/"
    assert env.is_primary is False


def test_missing_squareone_raises(discovery_data_dir: Path) -> None:
    """A discovery payload without a squareone UI service raises a clear
    error naming the environment.
    """
    data = json.loads((discovery_data_dir / "idfprod.json").read_text())
    del data["services"]["ui"]["squareone"]
    discovery = Discovery.model_validate(data)
    meta = EnvMeta(title="data.lsst.cloud", title_full="data.lsst.cloud")

    with pytest.raises(ValueError, match="idfprod"):
        PhalanxEnv.from_discovery(discovery, name="idfprod", meta=meta)


def test_api_and_times_square_host_follow_discovery(
    discovery_data_dir: Path,
) -> None:
    """The API and Times Square URLs take their host from the discovered
    service, not from squareone, so a service on a subdomain is honored.
    """
    data = json.loads((discovery_data_dir / "idfprod.json").read_text())
    # Move the TAP service and internal Times Square onto a subdomain of the
    # squareone host, leaving squareone itself on the parent domain.
    for dataset in data["datasets"].values():
        tap = dataset.get("services", {}).get("tap")
        if tap is not None:
            tap["url"] = tap["url"].replace(
                "data.lsst.cloud", "api.data.lsst.cloud"
            )
    times_square = data["services"]["internal"]["times-square"]
    times_square["url"] = times_square["url"].replace(
        "data.lsst.cloud", "api.data.lsst.cloud"
    )
    discovery = Discovery.model_validate(data)
    # squareone stays on the parent host, proving the derivation follows the
    # service rather than squareone.
    assert discovery.services.ui["squareone"].url.host == "data.lsst.cloud"
    meta = EnvMeta(title="data.lsst.cloud", title_full="data.lsst.cloud")

    env = PhalanxEnv.from_discovery(discovery, name="idfprod", meta=meta)

    assert str(env.api_url) == "https://api.data.lsst.cloud/api/"
    assert str(env.api_tap_url) == "https://api.data.lsst.cloud/api/tap/"
    assert str(env.times_square_url) == (
        "https://api.data.lsst.cloud/times-square/"
    )


def test_primary_env_flag(discovery_data_dir: Path) -> None:
    """The primary environment (idfprod) sets ``is_primary``."""
    discovery = _load("idfprod", discovery_data_dir)
    meta = EnvMeta(title="data.lsst.cloud", title_full="data.lsst.cloud")

    env = PhalanxEnv.from_discovery(discovery, name="idfprod", meta=meta)

    assert env.is_primary is True
    assert env.ltd_url_prefix == "https://rsp.lsst.io/"


def test_non_primary_env_ltd_url(discovery_data_dir: Path) -> None:
    """A non-primary environment is served under the ``/v/{env}/`` edition."""
    discovery = _load("summit", discovery_data_dir)
    meta = EnvMeta(title="Rubin Summit")

    env = PhalanxEnv.from_discovery(discovery, name="summit", meta=meta)

    assert env.is_primary is False
    assert env.ltd_url_prefix == "https://rsp.lsst.io/v/summit/"


def test_datasets_mapped(discovery_data_dir: Path) -> None:
    """Datasets and their user-facing service URLs map from discovery.

    Discovery order is preserved, and only the user-facing data-access service
    tokens (TAP, SIA, cutout, datalink, HiPS) are retained -- the per-dataset
    ``gms`` and ``alerts`` services are dropped.
    """
    discovery = _load("idfprod", discovery_data_dir)
    meta = EnvMeta(title="data.lsst.cloud")

    env = PhalanxEnv.from_discovery(discovery, name="idfprod", meta=meta)

    assert list(env.datasets) == ["dp02", "dp03", "dp1", "prompt"]
    dp1 = env.datasets["dp1"]
    assert dp1.name == "dp1"
    assert dp1.description is not None
    assert str(dp1.docs_url) == "https://dp1.lsst.io/"
    # The user-facing data-access services, and nothing else (no gms).
    assert set(dp1.services) == {"tap", "sia", "cutout", "datalink", "hips"}
    assert str(dp1.service_url("tap")) == "https://data.lsst.cloud/api/tap"
    assert dp1.has_service("sia")
    # dp03 exposes only TAP (per discovery), so SIA is absent.
    dp03 = env.datasets["dp03"]
    assert set(dp03.services) == {"tap"}
    assert not dp03.has_service("sia")
    assert dp03.service_url("sia") is None
    # The prompt dataset exposes only non-user-facing services (gms/alerts),
    # so it maps to an empty service set but keeps its metadata.
    assert env.datasets["prompt"].services == {}


def test_datasets_absent_without_data(discovery_data_dir: Path) -> None:
    """An environment serving no datasets has an empty ``datasets`` map."""
    discovery = _load("base", discovery_data_dir)
    meta = EnvMeta(title="Rubin Base Data Facility")

    env = PhalanxEnv.from_discovery(discovery, name="base", meta=meta)

    assert env.datasets == {}


def test_dataset_services_differ_across_envs(
    discovery_data_dir: Path,
) -> None:
    """A dataset can expose different services in different environments.

    dp1 exposes SIA and cutout on idfprod but not on usdfprod, so the roles
    and tables must resolve against the environment being built.
    """
    idfprod = PhalanxEnv.from_discovery(
        _load("idfprod", discovery_data_dir),
        name="idfprod",
        meta=EnvMeta(title="idfprod"),
    )
    usdfprod = PhalanxEnv.from_discovery(
        _load("usdfprod", discovery_data_dir),
        name="usdfprod",
        meta=EnvMeta(title="usdfprod"),
    )

    assert idfprod.datasets["dp1"].has_service("sia")
    assert not usdfprod.datasets["dp1"].has_service("sia")
