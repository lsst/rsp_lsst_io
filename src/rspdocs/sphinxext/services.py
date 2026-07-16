"""Single source of truth mapping service names and conditions to discovery
data.

This module is deliberately free of any Sphinx dependency so it can be unit
tested against `~rspdocs.discovery.models.PhalanxEnv` objects directly.

A *service token* names a user-facing RSP service; it resolves to an attribute
on `PhalanxEnv`. A service is *available* in an environment iff that attribute
resolves to a non-``None`` URL. A *condition token* (used by the ``rsp-only``
directive) is a service token, an environment name, or the special keyword
``primary``.

The service -> whole-page-exclude globs mapping is author-facing build config,
so it lives in the sibling :file:`page_excludes.yaml` and is loaded here rather
than hard-coded.
"""

from __future__ import annotations

from importlib.resources import files

import yaml

from ..discovery.metadata import load_environments_metadata
from ..discovery.models import PhalanxEnv

__all__ = [
    "SERVICE_ATTRS",
    "SERVICE_PAGE_EXCLUDES",
    "KNOWN_ENVS",
    "is_known_service",
    "resolve_url",
    "is_available",
    "resolve_condition",
    "excluded_page_patterns",
]

SERVICE_ATTRS: dict[str, str] = {
    "rsp": "squareone_url",
    "squareone": "squareone_url",
    "portal": "portal_url",
    "nublado": "nb_url",
    "nb": "nb_url",
    "api": "api_url",
    "tap": "api_tap_url",
    "webdav": "api_webdav_url",
    "times-square": "times_square_url",
    "tokens": "gafaelfawr_tokens_url",
    "phalanx-docs": "phalanx_docs_url",
}
"""Canonical service token -> `PhalanxEnv` attribute holding its URL."""


def _load_service_page_excludes() -> dict[str, list[str]]:
    """Load the service -> page-exclude globs mapping from the bundled YAML.

    Validates that every key is a known service token and every value is a list
    of glob strings, so a typo in :file:`page_excludes.yaml` fails the build
    loudly instead of silently excluding nothing.
    """
    text = (
        files("rspdocs.sphinxext").joinpath("page_excludes.yaml").read_text()
    )
    data = yaml.safe_load(text) or {}
    if not isinstance(data, dict):
        raise TypeError(
            "page_excludes.yaml must be a mapping of service -> glob list"
        )
    result: dict[str, list[str]] = {}
    for service, globs in data.items():
        if service not in SERVICE_ATTRS:
            raise ValueError(
                f"page_excludes.yaml references unknown service {service!r}"
            )
        if not isinstance(globs, list) or not all(
            isinstance(g, str) for g in globs
        ):
            raise TypeError(
                f"page_excludes.yaml globs for {service!r} must be a list of "
                "strings"
            )
        result[service] = globs
    return result


SERVICE_PAGE_EXCLUDES: dict[str, list[str]] = _load_service_page_excludes()
"""Service token -> source-file glob patterns to exclude when that service is
absent from an environment. Loaded from :file:`page_excludes.yaml`.
"""

KNOWN_ENVS: frozenset[str] = frozenset(
    load_environments_metadata().build_roster
)
"""Every environment name in the build roster (all environments, not just the
subset fetched for a given build).
"""


def is_known_service(name: str) -> bool:
    """Return whether ``name`` is a recognized service token."""
    return name in SERVICE_ATTRS


def resolve_url(env: PhalanxEnv, name: str) -> str | None:
    """Return the URL for service ``name`` in ``env``, or ``None``.

    ``None`` is returned both for an unknown service token and for a known
    service that is not deployed in this environment. Callers that need to
    distinguish the two should check `is_known_service` first.
    """
    attr = SERVICE_ATTRS.get(name)
    url = getattr(env, attr) if attr else None
    return str(url) if url is not None else None


def is_available(env: PhalanxEnv, name: str) -> bool:
    """Return whether service ``name`` has a URL in ``env``."""
    return resolve_url(env, name) is not None


def excluded_page_patterns(env: PhalanxEnv) -> list[str]:
    """Return source patterns to exclude for services absent in ``env``."""
    patterns: list[str] = []
    for service, globs in SERVICE_PAGE_EXCLUDES.items():
        if not is_available(env, service):
            patterns.extend(globs)
    return patterns


def resolve_condition(env: PhalanxEnv, token: str) -> bool | None:
    """Evaluate an ``rsp-only`` condition token against ``env``.

    Returns ``True``/``False`` for a recognized token, or ``None`` when the
    token is neither a known service, a known environment name, nor
    ``primary``.
    """
    if token == "primary":
        return env.is_primary
    if token in KNOWN_ENVS:
        return env.name == token
    if is_known_service(token):
        return is_available(env, token)
    return None
