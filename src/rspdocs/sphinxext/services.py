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
from ..discovery.models import DATASET_SERVICES, PhalanxEnv

__all__ = [
    "SERVICE_ATTRS",
    "SERVICE_PAGE_EXCLUDES",
    "DATASET_SERVICE_LABELS",
    "KNOWN_ENVS",
    "is_known_service",
    "is_known_dataset_service",
    "split_service_path",
    "split_dataset_target",
    "resolve_url",
    "resolve_dataset_url",
    "resolve_dataset_docs_url",
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

DATASET_SERVICE_LABELS: dict[str, str] = {
    "tap": "TAP",
    "sia": "SIA",
    "cutout": "Cutout (SODA)",
    "datalink": "DataLink",
    "hips": "HiPS",
}
"""Dataset service token -> display label for author-facing tables.

Its keys are exactly ``DATASET_SERVICES`` (order-preserving); a guard in
`~rspdocs.sphinxext.setup` asserts the two stay in sync.
"""


def is_known_dataset_service(name: str) -> bool:
    """Return whether ``name`` is a recognized per-dataset service token."""
    return name in DATASET_SERVICES


def split_dataset_target(target: str) -> tuple[str, str, str]:
    """Split a ``:rsp-data-url:`` target into service, dataset, and path.

    The target syntax is ``service dataset[/path]``: exactly two
    whitespace-separated tokens — a service token and a dataset name — where
    the dataset name may carry an appended ``/path`` joined onto the dataset's
    service URL exactly as `split_service_path` does for plain services. The
    two tokens may be separated by any amount of whitespace, but a target with
    more (or fewer) than two tokens is malformed.

    Returns a ``(service, dataset, path)`` tuple. A malformed target yields an
    empty dataset (and empty path), which callers report as a malformed
    reference.
    """
    parts = target.split()
    service = parts[0] if parts else ""
    if len(parts) != 2:
        return service, "", ""
    dataset, path = split_service_path(parts[1])
    return service, dataset, path


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


def split_service_path(target: str) -> tuple[str, str]:
    """Split a role target into its service token and appended path.

    The service token runs up to the first ``/``; everything after it is a
    path for `resolve_url` to append to the service's URL. A target without a
    ``/`` is a bare service token with an empty path. Service tokens must
    therefore never contain a ``/``.
    """
    service, _, path = target.partition("/")
    return service, path


def resolve_url(env: PhalanxEnv, name: str, path: str = "") -> str | None:
    """Return the URL for service ``name`` in ``env``, or ``None``.

    ``None`` is returned both for an unknown service token and for a known
    service that is not deployed in this environment. Callers that need to
    distinguish the two should check `is_known_service` first.

    A non-empty ``path`` is appended to the service's URL. The join always
    treats ``path`` as relative to the full service URL (which may itself
    carry a path, like the portal's ``/portal/app/``): slashes at the seam are
    normalized away, so ``settings`` and ``/settings`` are equivalent. This is
    deliberately not `~urllib.parse.urljoin`, whose RFC 3986 rules would
    resolve a leading-slash path against the host root and drop the last
    segment of a slashless base. The trailing slash of the result follows
    ``path`` exactly as written.
    """
    attr = SERVICE_ATTRS.get(name)
    url = getattr(env, attr) if attr else None
    if url is None:
        return None
    base = str(url)
    if not path:
        return base
    return f"{base.rstrip('/')}/{path.lstrip('/')}"


def resolve_dataset_url(
    env: PhalanxEnv, service: str, dataset: str, path: str = ""
) -> str | None:
    """Return the URL for ``service`` on ``dataset`` in ``env``, or ``None``.

    ``None`` is returned when the dataset is absent from this environment or
    when it does not expose that service; callers that need to tell an unknown
    service token apart from an absent dataset/service should check
    `is_known_dataset_service` first. A non-empty ``path`` is appended to the
    dataset's service URL with the same slash-normalizing join as
    `resolve_url`.
    """
    dataset_info = env.datasets.get(dataset)
    if dataset_info is None:
        return None
    url = dataset_info.service_url(service)
    if url is None:
        return None
    base = str(url)
    if not path:
        return base
    return f"{base.rstrip('/')}/{path.lstrip('/')}"


def resolve_dataset_docs_url(env: PhalanxEnv, dataset: str) -> str | None:
    """Return the documentation URL for ``dataset`` in ``env``, or ``None``.

    ``None`` is returned when the dataset is absent from this environment or
    when discovery reports no ``docs_url`` for it.
    """
    dataset_info = env.datasets.get(dataset)
    if dataset_info is None or dataset_info.docs_url is None:
        return None
    return str(dataset_info.docs_url)


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
