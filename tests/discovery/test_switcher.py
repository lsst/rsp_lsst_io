"""Unit tests for the version-switcher data builder."""

from __future__ import annotations

from rspdocs.discovery.metadata import EnvironmentsMetadata, EnvMeta
from rspdocs.discovery.switcher import build_switcher_entries


def _metadata() -> EnvironmentsMetadata:
    """A metadata shim mixing the primary env with non-primary ones."""
    return EnvironmentsMetadata(
        build_roster=["idfprod", "summit", "base"],
        environments={
            "idfprod": EnvMeta(title="data.lsst.cloud"),
            "summit": EnvMeta(title="Rubin Summit"),
            "base": EnvMeta(title="Rubin Base Data Facility"),
            # An env absent from the roster is ignored.
            "usdfprod": EnvMeta(title="Rubin USDF"),
        },
    )


def test_build_switcher_entries_order_and_urls() -> None:
    """One entry per roster env, in roster order, with edition URLs."""
    entries = build_switcher_entries(_metadata())

    assert entries == [
        {
            "name": "data.lsst.cloud",
            "version": "idfprod",
            "url": "https://rsp.lsst.io/",
        },
        {
            "name": "Rubin Summit",
            "version": "summit",
            "url": "https://rsp.lsst.io/v/summit/",
        },
        {
            "name": "Rubin Base Data Facility",
            "version": "base",
            "url": "https://rsp.lsst.io/v/base/",
        },
    ]


def test_build_switcher_entries_name_and_version() -> None:
    """``name`` is the display title and ``version`` is the env name."""
    entries = build_switcher_entries(_metadata())
    by_version = {e["version"]: e for e in entries}

    assert by_version["summit"]["name"] == "Rubin Summit"
    # The primary edition is served at the site root; others under /v/.
    assert by_version["idfprod"]["url"] == "https://rsp.lsst.io/"
    assert by_version["base"]["url"].endswith("/v/base/")
