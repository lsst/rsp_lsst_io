"""In-repo metadata shim that supplements Repertoire discovery data.

Repertoire's per-environment discovery payloads describe the services deployed
in each RSP environment, but they don't (yet) carry a few things the docs build
needs: human-readable environment titles and a way to hide services that are
deployed but not visible to normal users (for example, a service behind an
admin-scoped ingress). This module loads that supplementary data from the
bundled :file:`environments.json` file.
"""

from __future__ import annotations

from importlib.resources import files

from pydantic import BaseModel, Field, model_validator

__all__ = ["EnvMeta", "EnvironmentsMetadata", "load_environments_metadata"]


class EnvMeta(BaseModel):
    """Supplementary metadata for a single RSP environment."""

    title: str = Field(
        description="The short title of the environment, usually an acronym.",
        examples=["IDF"],
    )

    title_full: str | None = Field(
        None,
        description="Full title, that expands acronyms.",
        examples=["Rubin Interim Data Facility"],
    )

    hidden_services: list[str] = Field(
        default_factory=list,
        description=(
            "Discovery service keys (from ``services.ui`` or "
            "``services.internal``) that are deployed but should be treated "
            "as absent when building the documentation. Use this for services "
            "that are not visible to normal users, such as those behind an "
            "admin-scoped ingress."
        ),
        examples=[["times-square"]],
    )


class EnvironmentsMetadata(BaseModel):
    """The contents of the :file:`environments.json` shim."""

    build_roster: list[str] = Field(
        description="Environment names to build documentation for, in order.",
    )

    environments: dict[str, EnvMeta] = Field(
        description="Supplementary metadata, keyed by environment name.",
    )

    @model_validator(mode="after")
    def _check_roster_has_metadata(self) -> EnvironmentsMetadata:
        """Ensure every ``build_roster`` env has a metadata entry."""
        missing = set(self.build_roster) - set(self.environments)
        if missing:
            raise ValueError(
                "environments.json build_roster references environments "
                f"with no metadata entry: {sorted(missing)}"
            )
        return self


def load_environments_metadata() -> EnvironmentsMetadata:
    """Load the bundled environments metadata shim.

    Returns
    -------
    EnvironmentsMetadata
        The parsed contents of :file:`environments.json`.
    """
    text = files("rspdocs.discovery").joinpath("environments.json").read_text()
    return EnvironmentsMetadata.model_validate_json(text)
