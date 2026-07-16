"""Author-facing roles that resolve service URLs from discovery data.

``:rsp-url:`service``` emits a code literal of the service's URL for the
environment being built; ``:rsp-link:`service``` (or
``:rsp-link:`Title <service>```) emits a real external hyperlink. Because both
resolve at parse time, URLs can appear in code literals, tables, admonitions,
and lists, and ``:rsp-link:`` references are crawled by ``linkcheck``.
"""

from __future__ import annotations

from docutils import nodes
from sphinx.util.docutils import ReferenceRole, SphinxRole

from .logging import warn_unavailable_service, warn_unknown_service
from .services import is_known_service, resolve_url

__all__ = ["RspUrlRole", "RspLinkRole"]


class RspUrlRole(SphinxRole):
    """``:rsp-url:`service``` -> a code literal of the service's URL."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        service = self.text
        if not is_known_service(service):
            warn_unknown_service(service, location=self.get_location())
            return [nodes.literal("", service)], []
        env = self.config.rsp_env
        url = resolve_url(env, service)
        if url is None:
            warn_unavailable_service(
                service, env.name, location=self.get_location()
            )
            return [nodes.literal("", service)], []
        return [nodes.literal("", url)], []


class RspLinkRole(ReferenceRole):
    """``:rsp-link:`service``` -> an external hyperlink to the service.

    With no explicit title the link text is the URL itself (matching the prior
    ``|rsp-url|``/``|nb-url|`` substitutions); ``:rsp-link:`Title <service>```
    uses ``Title`` as the link text.
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        service = self.target
        if not is_known_service(service):
            warn_unknown_service(service, location=self.get_location())
            return [nodes.Text(self.title)], []
        env = self.config.rsp_env
        url = resolve_url(env, service)
        if url is None:
            warn_unavailable_service(
                service, env.name, location=self.get_location()
            )
            return [nodes.Text(self.title)], []
        display = self.title if self.has_explicit_title else url
        node = nodes.reference("", display, refuri=url, internal=False)
        return [node], []
