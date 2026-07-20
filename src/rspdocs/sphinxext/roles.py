"""Author-facing roles that resolve service URLs from discovery data.

``:rsp-url:`service``` emits a code literal of the service's URL for the
environment being built; ``:rsp-link:`service``` (or
``:rsp-link:`Title <service>```) emits a real external hyperlink. A target may
append a path to the service's URL, as in ``:rsp-url:`rsp/settings/quotas```
or ``:rsp-link:`Firefly <portal/onlinehelp/>``` (see
`~rspdocs.sphinxext.services.resolve_url` for the join rules). Because both
roles resolve at parse time, URLs can appear in code literals, tables,
admonitions, and lists, and ``:rsp-link:`` references are crawled by
``linkcheck``.
"""

from __future__ import annotations

from docutils import nodes
from sphinx.util.docutils import ReferenceRole, SphinxRole

from .logging import (
    warn_malformed_dataset_target,
    warn_unavailable_dataset,
    warn_unavailable_dataset_docs,
    warn_unavailable_service,
    warn_unknown_dataset_service,
    warn_unknown_service,
)
from .services import (
    is_known_dataset_service,
    is_known_service,
    resolve_dataset_docs_url,
    resolve_dataset_url,
    resolve_url,
    split_dataset_target,
    split_service_path,
)

__all__ = [
    "RspDataLinkRole",
    "RspDataUrlRole",
    "RspDatasetDocsRole",
    "RspLinkRole",
    "RspUrlRole",
]


class RspUrlRole(SphinxRole):
    """``:rsp-url:`service[/path]``` -> a code literal of the URL."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        service, path = split_service_path(self.text)
        if not is_known_service(service):
            warn_unknown_service(service, location=self.get_location())
            return [nodes.literal("", self.text)], []
        env = self.config.rsp_env
        url = resolve_url(env, service, path=path)
        if url is None:
            warn_unavailable_service(
                service, env.name, location=self.get_location()
            )
            return [nodes.literal("", self.text)], []
        return [nodes.literal("", url)], []


class RspLinkRole(ReferenceRole):
    """``:rsp-link:`service[/path]``` -> an external hyperlink.

    With no explicit title the link text is the URL itself (matching the prior
    ``|rsp-url|``/``|nb-url|`` substitutions);
    ``:rsp-link:`Title <service[/path]>``` uses ``Title`` as the link text.
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        service, path = split_service_path(self.target)
        if not is_known_service(service):
            warn_unknown_service(service, location=self.get_location())
            return [nodes.Text(self.title)], []
        env = self.config.rsp_env
        url = resolve_url(env, service, path=path)
        if url is None:
            warn_unavailable_service(
                service, env.name, location=self.get_location()
            )
            return [nodes.Text(self.title)], []
        display = self.title if self.has_explicit_title else url
        node = nodes.reference("", display, refuri=url, internal=False)
        return [node], []


class RspDataUrlRole(SphinxRole):
    """``:rsp-data-url:`service dataset[/path]``` -> a code literal.

    Resolves a per-dataset data-access service URL (TAP, SIA, cutout,
    datalink, HiPS) for the environment being built, as in
    ``:rsp-data-url:`tap dp1```. An optional path may be appended to the
    dataset name (``tap dp1/tables``), joined onto the service URL like
    `~rspdocs.sphinxext.roles.RspUrlRole`. A malformed target, an unknown
    service token, or a dataset/service absent from the environment warns
    (fatal under ``-W``) and echoes the raw target.
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        service, dataset, path = split_dataset_target(self.text)
        if not dataset:
            warn_malformed_dataset_target(
                self.text, location=self.get_location()
            )
            return [nodes.literal("", self.text)], []
        if not is_known_dataset_service(service):
            warn_unknown_dataset_service(service, location=self.get_location())
            return [nodes.literal("", self.text)], []
        env = self.config.rsp_env
        url = resolve_dataset_url(env, service, dataset, path=path)
        if url is None:
            warn_unavailable_dataset(
                service, dataset, env.name, location=self.get_location()
            )
            return [nodes.literal("", self.text)], []
        return [nodes.literal("", url)], []


class RspDataLinkRole(ReferenceRole):
    """``:rsp-data-link:`service dataset[/path]``` -> an external hyperlink.

    The hyperlink twin of ``:rsp-data-url:``. With no explicit title the link
    text is the URL; ``:rsp-data-link:`Title <service dataset[/path]>``` uses
    ``Title``.
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        service, dataset, path = split_dataset_target(self.target)
        if not dataset:
            warn_malformed_dataset_target(
                self.target, location=self.get_location()
            )
            return [nodes.Text(self.title)], []
        if not is_known_dataset_service(service):
            warn_unknown_dataset_service(service, location=self.get_location())
            return [nodes.Text(self.title)], []
        env = self.config.rsp_env
        url = resolve_dataset_url(env, service, dataset, path=path)
        if url is None:
            warn_unavailable_dataset(
                service, dataset, env.name, location=self.get_location()
            )
            return [nodes.Text(self.title)], []
        display = self.title if self.has_explicit_title else url
        node = nodes.reference("", display, refuri=url, internal=False)
        return [node], []


class RspDatasetDocsRole(ReferenceRole):
    """``:rsp-dataset-docs:`dataset``` -> a link to the dataset's docs.

    Resolves a dataset's ``docs_url`` from discovery for the environment being
    built, as in ``:rsp-dataset-docs:`dp1```. With no explicit title the link
    text is the URL; ``:rsp-dataset-docs:`Title <dataset>``` uses ``Title``. A
    dataset absent from the environment, or one whose discovery data carries no
    ``docs_url``, warns (fatal under ``-W``) and falls back to the title text.
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        dataset = self.target.strip()
        env = self.config.rsp_env
        url = resolve_dataset_docs_url(env, dataset)
        if url is None:
            warn_unavailable_dataset_docs(
                dataset, env.name, location=self.get_location()
            )
            return [nodes.Text(self.title)], []
        display = self.title if self.has_explicit_title else url
        node = nodes.reference("", display, refuri=url, internal=False)
        return [node], []
