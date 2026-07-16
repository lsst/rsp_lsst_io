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
    "WARNING_TYPE",
    "UNKNOWN_SERVICE",
    "UNAVAILABLE_SERVICE",
    "UNKNOWN_CONDITION",
    "warn_unknown_service",
    "warn_unavailable_service",
    "warn_unknown_condition",
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
