"""In-repo Sphinx extension exposing author-facing roles and a conditional
directive backed by Repertoire discovery data.

The extension provides:

* ``:rsp-url:`service``` -- a code literal of a service's URL (optionally
  with an appended path, as in ``:rsp-url:`rsp/settings```),
* ``:rsp-link:`service``` -- an external hyperlink to a service (same
  optional path syntax),
* ``:rsp-data-url:`service dataset``` / ``:rsp-data-link:`service dataset``` --
  a code literal / hyperlink of a per-dataset data-access service URL (TAP,
  SIA, cutout, datalink, HiPS), as in ``:rsp-data-url:`tap dp1```,
* ``:rsp-dataset-docs:`dataset``` -- a link to a dataset's documentation,
* ``.. rsp-data-table::`` -- a dataset/service availability matrix rendered
  from discovery data, and
* ``.. rsp-only::`` -- content included only in matching environments.

These resolve against the `~rspdocs.discovery.models.PhalanxEnv` for the
environment being built, supplied through the ``rsp_env`` config value, and --
for the cross-environment table -- against every roster environment supplied
through ``rsp_all_envs`` (see :file:`conf.py`).
"""

from __future__ import annotations

from importlib.metadata import version
from typing import Any

from sphinx.application import Sphinx
from sphinx.errors import ConfigError

from ..discovery.models import DATASET_SERVICES, PhalanxEnv
from .directives import RspOnly
from .roles import (
    RspDataLinkRole,
    RspDatasetDocsRole,
    RspDataUrlRole,
    RspLinkRole,
    RspUrlRole,
)
from .services import DATASET_SERVICE_LABELS, KNOWN_ENVS, SERVICE_ATTRS
from .tables import RspDataTable

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


def _check_dataset_service_labels() -> None:
    """Assert the dataset-service label map covers exactly the known tokens.

    ``DATASET_SERVICE_LABELS`` supplies a display label for every per-dataset
    service token; a token added to ``DATASET_SERVICES`` without a label (or a
    stale label for a removed token) should fail the build loudly rather than
    render a table with a missing or dangling column heading.
    """
    labelled = set(DATASET_SERVICE_LABELS)
    known = set(DATASET_SERVICES)
    if labelled != known:
        raise ConfigError(
            "rspdocs.sphinxext DATASET_SERVICE_LABELS must label exactly the "
            f"DATASET_SERVICES tokens; missing {sorted(known - labelled)}, "
            f"extra {sorted(labelled - known)}"
        )


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the rspdocs roles, directive, and config values."""
    _check_token_namespaces_disjoint()
    _check_dataset_service_labels()

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
    app.add_role("rsp-data-url", RspDataUrlRole())
    app.add_role("rsp-data-link", RspDataLinkRole())
    app.add_role("rsp-dataset-docs", RspDatasetDocsRole())
    app.add_directive("rsp-only", RspOnly)
    app.add_directive("rsp-data-table", RspDataTable)

    return {
        "version": version("rspdocs"),
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
