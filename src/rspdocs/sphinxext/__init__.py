"""In-repo Sphinx extension exposing author-facing roles and a conditional
directive backed by Repertoire discovery data.

The extension provides:

* ``:rsp-url:`service``` -- a code literal of a service's URL (optionally
  with an appended path, as in ``:rsp-url:`rsp/settings```),
* ``:rsp-link:`service``` -- an external hyperlink to a service (same
  optional path syntax), and
* ``.. rsp-only::`` -- content included only in matching environments.

All three resolve against the `~rspdocs.discovery.models.PhalanxEnv` for the
environment being built, supplied through the ``rsp_env`` config value (see
:file:`conf.py`).
"""

from __future__ import annotations

from importlib.metadata import version
from typing import Any

from sphinx.application import Sphinx
from sphinx.errors import ConfigError

from ..discovery.models import PhalanxEnv
from .directives import RspOnly
from .roles import RspLinkRole, RspUrlRole
from .services import KNOWN_ENVS, SERVICE_ATTRS

__all__ = ["setup"]


def _check_token_namespaces_disjoint() -> None:
    """Assert the condition token name-spaces do not collide.

    ``rsp-only`` accepts bare tokens that may be a service name, an environment
    name, or ``primary``. Those three sets must stay pairwise disjoint or a
    token would be ambiguous; a future naming collision should fail the build
    loudly rather than resolve silently to the wrong meaning.
    """
    services = set(SERVICE_ATTRS)
    envs = set(KNOWN_ENVS)
    primary = {"primary"}
    collisions = {
        "service names and environment names": services & envs,
        "service names and 'primary'": services & primary,
        "environment names and 'primary'": envs & primary,
    }
    reported = {
        label: sorted(overlap)
        for label, overlap in collisions.items()
        if overlap
    }
    if reported:
        raise ConfigError(
            "rspdocs.sphinxext condition token name-spaces must be disjoint, "
            f"but these overlap: {reported}"
        )


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the rspdocs roles, directive, and config values."""
    _check_token_namespaces_disjoint()

    # Data channels for the current build. These are excluded from the ``env``
    # rebuild filter (rebuild="") so their pickled comparison never triggers a
    # rebuild; ``rsp_discovery_hash`` below is the single rebuild trigger.
    app.add_config_value(
        "rsp_env", None, rebuild="", types=(PhalanxEnv, type(None))
    )
    app.add_config_value("rsp_all_envs", None, rebuild="")

    # The only rebuild trigger: when discovery data changes its hash changes,
    # so Sphinx marks all docs for reparse and the roles re-bake fresh URLs
    # into the doctrees (roles resolve at read time, hence this is required for
    # incremental-build correctness).
    app.add_config_value("rsp_discovery_hash", "", rebuild="env", types=(str,))

    app.add_role("rsp-url", RspUrlRole())
    app.add_role("rsp-link", RspLinkRole())
    app.add_directive("rsp-only", RspOnly)

    return {
        "version": version("rspdocs"),
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
