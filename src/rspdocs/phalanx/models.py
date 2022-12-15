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
        descrption="The environment's name in Phalanx.", example="idfprod"
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

    portal_url: HttpUrl = Field(
        description="Root URL for the portal.",
        example="https://data.lsst.cloud/portal/app",
    )

    nb_url: HttpUrl = Field(
        description="URL for the Nublado spawner page.",
        example="https://data.lsst.cloud/nb/",
    )

    api_url: HttpUrl = Field(
        description="Root URL for VO APIs.",
        example="https://data.lsst.cloud/api/",
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
    def api_tap_url(self) -> Optional[str]:
        """The root URL for the TAP service, or ``None`` if the TAP server is
        not available.
        """
        # FIXME change this to return None if TAP isn't available on this RSP.
        return f"{self.api_url}tap"


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
