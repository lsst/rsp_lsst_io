"""Unit tests for the environments metadata shim."""

from __future__ import annotations

import pytest

from rspdocs.discovery.metadata import EnvironmentsMetadata, EnvMeta


def test_roster_subset_of_environments() -> None:
    """Roster envs plus an unrostered extra env construct fine."""
    metadata = EnvironmentsMetadata(
        build_roster=["idfprod", "summit"],
        environments={
            "idfprod": EnvMeta(title="data.lsst.cloud"),
            "summit": EnvMeta(title="Rubin Summit"),
            # An env absent from the roster is allowed.
            "usdfprod": EnvMeta(title="Rubin USDF"),
        },
    )

    assert metadata.build_roster == ["idfprod", "summit"]


def test_roster_missing_environment_raises() -> None:
    """A roster env with no metadata entry raises a clear error."""
    with pytest.raises(ValueError) as excinfo:
        EnvironmentsMetadata(
            build_roster=["idfprod", "summit"],
            environments={
                "idfprod": EnvMeta(title="data.lsst.cloud"),
            },
        )

    assert "summit" in str(excinfo.value)
