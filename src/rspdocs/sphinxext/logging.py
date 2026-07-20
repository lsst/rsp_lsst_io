"""Shared Sphinx logging for the rspdocs extension.

All warnings emitted by the extension use the ``rspdocs`` warning *type* with a
descriptive *subtype*, so they are

* precise -- every call passes ``location`` for a ``file:line`` reference,
* fatal under ``sphinx-build -W`` (Sphinx counts non-suppressed warnings), and
* individually silenceable via ``suppress_warnings`` (for example
  ``suppress_warnings = ["rspdocs.unknown-service"]`` or the whole family with
  ``["rspdocs"]``).
"""

from __future__ import annotations

from typing import Any

from sphinx.util import logging

__all__ = [
    "MALFORMED_DATASET_TARGET",
    "UNAVAILABLE_DATASET",
    "UNAVAILABLE_DATASET_DOCS",
    "UNAVAILABLE_SERVICE",
    "UNKNOWN_CONDITION",
    "UNKNOWN_DATASET",
    "UNKNOWN_DATASET_SERVICE",
    "UNKNOWN_SERVICE",
    "WARNING_TYPE",
    "warn_malformed_dataset_target",
    "warn_unavailable_dataset",
    "warn_unavailable_dataset_docs",
    "warn_unavailable_service",
    "warn_unknown_condition",
    "warn_unknown_dataset",
    "warn_unknown_dataset_service",
    "warn_unknown_service",
]

logger = logging.getLogger(__name__)

WARNING_TYPE = "rspdocs"
"""The Sphinx warning ``type`` for every warning this extension emits."""

UNKNOWN_SERVICE = "unknown-service"
"""Subtype: a role targets a token that is not a known service name."""

UNAVAILABLE_SERVICE = "unavailable-service"
"""Subtype: a role targets a known service that is absent in this env."""

UNKNOWN_CONDITION = "unknown-condition"
"""Subtype: an ``rsp-only`` token that isn't a service/env/``primary``."""

UNKNOWN_DATASET_SERVICE = "unknown-dataset-service"
"""Subtype: a dataset role targets an unknown per-dataset service token."""

UNKNOWN_DATASET = "unknown-dataset"
"""Subtype: an ``rsp-data-table`` ``:datasets:`` name that is not served."""

UNAVAILABLE_DATASET = "unavailable-dataset"
"""Subtype: a dataset role targets a dataset/service absent in this env."""

UNAVAILABLE_DATASET_DOCS = "unavailable-dataset-docs"
"""Subtype: a dataset-docs role targets a dataset with no docs URL here."""

MALFORMED_DATASET_TARGET = "malformed-dataset-target"
"""Subtype: a dataset role target isn't the ``service dataset`` form."""


def warn_unknown_service(name: str, *, location: Any) -> None:
    """Warn that ``name`` is not a recognized RSP service token."""
    logger.warning(
        "unknown RSP service %r; expected one of the documented service "
        "tokens (see docs/contributing/env-specific-docs.rst)",
        name,
        location=location,
        type=WARNING_TYPE,
        subtype=UNKNOWN_SERVICE,
    )


def warn_unavailable_service(
    name: str, env_name: str, *, location: Any
) -> None:
    """Warn that service ``name`` is not available in ``env_name``.

    This usually means the reference should be wrapped in a matching
    ``.. rsp-only::`` block so it is only emitted where the service exists.
    """
    logger.warning(
        "RSP service %r is not available in the %r environment; wrap the "
        "reference in a matching '.. rsp-only::' block",
        name,
        env_name,
        location=location,
        type=WARNING_TYPE,
        subtype=UNAVAILABLE_SERVICE,
    )


def warn_unknown_condition(token: str, *, location: Any) -> None:
    """Warn that ``token`` is not a valid ``rsp-only`` condition."""
    logger.warning(
        "unknown rsp-only condition %r; expected a service name, an "
        "environment name, or 'primary'",
        token,
        location=location,
        type=WARNING_TYPE,
        subtype=UNKNOWN_CONDITION,
    )


def warn_unknown_dataset_service(name: str, *, location: Any) -> None:
    """Warn that ``name`` is not a recognized per-dataset service token."""
    logger.warning(
        "unknown dataset service %r; expected one of the documented "
        "per-dataset service tokens (see "
        "docs/contributing/env-specific-docs.rst)",
        name,
        location=location,
        type=WARNING_TYPE,
        subtype=UNKNOWN_DATASET_SERVICE,
    )


def warn_unknown_dataset(name: str, where: str, *, location: Any) -> None:
    """Warn that dataset ``name`` is not served in ``where``.

    ``where`` is a human-readable scope, such as ``"the 'idfprod'
    environment"`` or ``"any environment"``.
    """
    logger.warning(
        "unknown dataset %r; it is not served in %s",
        name,
        where,
        location=location,
        type=WARNING_TYPE,
        subtype=UNKNOWN_DATASET,
    )


def warn_unavailable_dataset(
    service: str, dataset: str, env_name: str, *, location: Any
) -> None:
    """Warn that ``service`` on ``dataset`` is absent in ``env_name``.

    This usually means the reference should be wrapped in a matching
    ``.. rsp-only::`` block (gated on ``api``, ``tap``, or environment names;
    the per-dataset service tokens are not ``rsp-only`` conditions) so it is
    only emitted where the dataset and service exist.
    """
    logger.warning(
        "dataset %r does not expose the %r service in the %r environment; "
        "wrap the reference in a matching '.. rsp-only::' block",
        dataset,
        service,
        env_name,
        location=location,
        type=WARNING_TYPE,
        subtype=UNAVAILABLE_DATASET,
    )


def warn_unavailable_dataset_docs(
    dataset: str, env_name: str, *, location: Any
) -> None:
    """Warn that no documentation URL exists for ``dataset`` in ``env_name``.

    This covers both a dataset absent from the environment and one that is
    served but whose discovery data carries no ``docs_url``.
    """
    logger.warning(
        "no documentation URL for dataset %r in the %r environment (the "
        "dataset is absent, or discovery reports no docs_url for it); wrap "
        "the reference in a matching '.. rsp-only::' block",
        dataset,
        env_name,
        location=location,
        type=WARNING_TYPE,
        subtype=UNAVAILABLE_DATASET_DOCS,
    )


def warn_malformed_dataset_target(target: str, *, location: Any) -> None:
    """Warn that ``target`` is not the ``service dataset`` form."""
    logger.warning(
        "malformed dataset reference %r; expected 'service dataset' (for "
        "example 'tap dp1')",
        target,
        location=location,
        type=WARNING_TYPE,
        subtype=MALFORMED_DATASET_TARGET,
    )
