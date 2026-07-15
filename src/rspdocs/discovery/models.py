"""Pydantic models representing Phalanx attributes about RSP environments."""

from __future__ import annotations

from collections import UserDict

from pydantic import BaseModel, Field, HttpUrl
from rubin.repertoire import Discovery

from ..constants import DOCS_ROOT_URL, PRIMARY_ENV
from .metadata import EnvMeta

__all__ = ["PhalanxEnv", "EnvironmentDict"]


class PhalanxEnv(BaseModel):
    """A Pydantic model of a Phalanx environment."""

    name: str = Field(
        description="The environment's name in Phalanx.", examples=["idfprod"]
    )

    title: str = Field(
        description="The short title of the environment, usually an acronym.",
        examples=["IDF"],
    )

    title_full: str | None = Field(
        None,
        description="Full title, that expands acronyms",
        examples=["Rubin Interim Data Facility"],
    )

    domain: str = Field(
        description="Domain name of the environment.",
        examples=["data.lsst.cloud"],
    )

    squareone_url: HttpUrl = Field(
        description="Root URL of the RSP homepage.",
        examples=["https://data.lsst.cloud/"],
    )

    portal_url: HttpUrl | None = Field(
        None,
        description="Root URL for the portal.",
        examples=["https://data.lsst.cloud/portal/app"],
    )

    nb_url: HttpUrl | None = Field(
        None,
        description="URL for the Nublado spawner page.",
        examples=["https://data.lsst.cloud/nb/"],
    )

    api_url: HttpUrl | None = Field(
        None,
        description="Root URL for VO APIs.",
        examples=["https://data.lsst.cloud/api/"],
    )

    api_tap_url: HttpUrl | None = Field(
        None,
        description="Root URL for the TAP service.",
        examples=["https://data.lsst.cloud/api/tap/"],
    )

    api_webdav_url: HttpUrl | None = Field(
        None,
        description="Root URL for the WebDAV service.",
        examples=["https://data.lsst.cloud/files/"],
    )

    gafaelfawr_tokens_url: HttpUrl = Field(
        description="URL for the Gafaelfawr user tokens page.",
        examples=["https://data.lsst.cloud/auth/tokens/"],
    )

    phalanx_docs_url: HttpUrl = Field(
        description=(
            "URL for the environment's homepage in the Phalanx docs. "
            "Don't show this URL for public RSPs, but it may be appropriate "
            "for staff (internal) RSPs."
        ),
        examples=["https://phalanx.lsst.io/environments/base/index.html"],
    )

    times_square_url: HttpUrl | None = Field(
        None,
        description="URL for root Times Square page (if deployed).",
        examples=["https://data.lsst.cloud/times-square/"],
    )

    @classmethod
    def from_discovery(
        cls, discovery: Discovery, *, name: str, meta: EnvMeta
    ) -> PhalanxEnv:
        """Build a `PhalanxEnv` from Repertoire discovery data and the
        in-repo metadata shim.

        Parameters
        ----------
        discovery
            The Repertoire discovery payload for the environment.
        name
            The environment's name (the roster key).
        meta
            Supplementary metadata (titles and hidden-service overrides) for
            the environment.

        Returns
        -------
        PhalanxEnv
            The environment model derived from discovery data.

        Notes
        -----
        A service named in ``meta.hidden_services`` is treated as absent, even
        if discovery reports it. This is used to hide services that are
        deployed but not visible to normal users (for example, a service
        behind an admin-scoped ingress).
        """
        hidden = set(meta.hidden_services)
        ui = discovery.services.ui
        internal = discovery.services.internal

        def ui_url(key: str) -> HttpUrl | None:
            if key in hidden:
                return None
            service = ui.get(key)
            return service.url if service is not None else None

        # squareone is the RSP homepage and the base for all derived URLs.
        squareone_service = ui.get("squareone")
        if squareone_service is None:
            raise ValueError(
                f"discovery for {name!r} has no 'squareone' UI service"
            )
        squareone = squareone_service.url
        squareone_str = str(squareone)
        base = (
            squareone_str
            if squareone_str.endswith("/")
            else f"{squareone_str}/"
        )
        host = squareone.host
        if host is None:  # pragma: no cover - HttpUrl always has a host
            raise ValueError(f"squareone URL for {name} has no host")

        # VO APIs only exist where the environment serves datasets.
        has_datasets = len(discovery.datasets) > 0
        api_url = HttpUrl(f"{base}api/") if has_datasets else None
        api_tap_url = HttpUrl(f"{base}api/tap/") if has_datasets else None

        # Times Square, in its user-facing UI form (not the /api internal URL).
        has_times_square = (
            "times-square" in internal and "times-square" not in hidden
        )
        times_square_url = (
            HttpUrl(f"{base}times-square/") if has_times_square else None
        )

        return cls(
            name=name,
            title=meta.title,
            title_full=meta.title_full,
            domain=host,
            squareone_url=HttpUrl(base),
            portal_url=ui_url("portal"),
            nb_url=ui_url("nublado"),
            api_url=api_url,
            api_tap_url=api_tap_url,
            api_webdav_url=ui_url("webdav"),
            gafaelfawr_tokens_url=HttpUrl(f"{base}auth/tokens/"),
            phalanx_docs_url=HttpUrl(
                f"https://phalanx.lsst.io/environments/{name}/"
            ),
            times_square_url=times_square_url,
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
