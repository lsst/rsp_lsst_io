"""Build the pydata-theme version-switcher data from the build roster.

The switcher lets readers hop between the per-environment documentation
editions. Its data (one entry per built environment) is derived here from the
already-loaded environments metadata so it never drifts from the roster.
"""

from __future__ import annotations

from .metadata import EnvironmentsMetadata
from .models import ltd_edition_url

__all__ = ["build_switcher_entries"]


def build_switcher_entries(
    metadata: EnvironmentsMetadata,
) -> list[dict[str, str]]:
    """Return version-switcher entries, one per environment in the roster.

    Each entry has the shape the pydata-sphinx-theme switcher expects: a
    ``name`` display label, a ``version`` match key (the environment name), and
    the published edition ``url``.
    """
    return [
        {
            "name": metadata.environments[name].title,
            "version": name,
            "url": ltd_edition_url(name),
        }
        for name in metadata.build_roster
    ]
