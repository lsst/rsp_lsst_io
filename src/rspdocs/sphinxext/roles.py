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

from .logging import warn_unavailable_service, warn_unknown_service
from .services import is_known_service, resolve_url, split_service_path

__all__ = ["RspUrlRole", "RspLinkRole"]


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
