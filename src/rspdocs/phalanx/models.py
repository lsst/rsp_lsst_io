"""Pydantic models representing Phalanx attributes about RSP environments."""

from __future__ import annotations

from collections import UserDict
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl

from ..constants import DOCS_ROOT_URL, PRIMARY_ENV

__all__ = ["PhalanxEnv", "EnvironmentDict"]


class PhalanxEnv(BaseModel):
    """A Pydantic model of a Phalanx environment."""

    name: str = Field(
        description="The environment's name in Phalanx.", example="idfprod"
    )

    title: str = Field(
        description="The short title of the environment, usually an acronym.",
        example="IDF",
    )

    title_full: Optional[str] = Field(
        None,
        description="Full title, that expands acronyms",
        example="Rubin Interim Data Facility",
    )

    domain: str = Field(
        description="Domain name of the environment.",
        example="data.lsst.cloud",
    )

    squareone_url: HttpUrl = Field(
        description="Root URL of the RSP homepage.",
        example="https://data.lsst.cloud/",
    )

    portal_url: Optional[HttpUrl] = Field(
        None,
        description="Root URL for the portal.",
        example="https://data.lsst.cloud/portal/app",
    )

    nb_url: Optional[HttpUrl] = Field(
        None,
        description="URL for the Nublado spawner page.",
        example="https://data.lsst.cloud/nb/",
    )

    webdav_url: Optional[HttpUrl] = Field(
        None,
        description="URL for the WebDAV spawner page.",
        example="https://data.lsst.cloud/files/",
    )

    api_url: Optional[HttpUrl] = Field(
        None,
        description="Root URL for VO APIs.",
        example="https://data.lsst.cloud/api/",
    )

    api_tap_url: Optional[HttpUrl] = Field(
        None,
        description="Root URL for the TAP service.",
        example="https://data.lsst.cloud/api/tap/",
    )

    gafaelfawr_tokens_url: HttpUrl = Field(
        description="URL for the Gafaelfawr user tokens page.",
        example="https://data.lsst.cloud/auth/tokens/",
    )

    phalanx_docs_url: HttpUrl = Field(
        description=(
            "URL for the environment's homepage in the Phalanx docs. "
            "Don't show this URL for public RSPs, but it may be appropriate "
            "for staff (internal) RSPs."
        ),
        example="https://phalanx.lsst.io/environments/base/index.html",
    )

    times_square_url: Optional[HttpUrl] = Field(
        None,
        description="URL for root Times Square page (if deployed).",
        example="https://data.lsst.cloud/times-square/",
    )

    @property
    def ltd_url_prefix(self) -> str:
        """The root URL of the environment's documentation site."""
        if self.name == PRIMARY_ENV:
            return DOCS_ROOT_URL
        else:
            return f"{DOCS_ROOT_URL}{self.name}/"

    @property
    def is_primary(self) -> bool:
        """Flag for whether the environment is the primary environment (i.e.
        corresponding to the default documentation edition.
        """
        return self.name == PRIMARY_ENV

    @property
    def has_apps(self) -> bool:
        """Flag for whether the environment has apps beyond the three
        main aspects.
        """
        # Expand this test as we add more apps
        return self.times_square_url is not None


class EnvironmentDict(UserDict[str, PhalanxEnv]):
    """Collection of `PhalanxEnv`, keyed by the environment name"""

    @property
    def primary(self) -> PhalanxEnv:
        """Quick access to the primary environment."""
        return self[PRIMARY_ENV]

    @property
    def env_names(self) -> list[str]:
        """The names of available environments."""
        return list(self.keys())
