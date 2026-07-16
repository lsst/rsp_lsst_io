"""The ``rsp-only`` directive: include content only in matching environments.

Arguments are bare tokens that mix service names, environment names, and the
``primary`` keyword (the token name-spaces are kept disjoint by a guard in
`~rspdocs.sphinxext.setup`). By default all tokens must hold (AND); ``:any:``
switches to OR and ``:not:`` negates the result. Excluded content is never
parsed into the doctree, so it cannot leak into the table of contents, the
index, or search.
"""

from __future__ import annotations

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

from .logging import warn_unknown_condition
from .services import resolve_condition

__all__ = ["RspOnly"]


class RspOnly(SphinxDirective):
    """Emit the directive body only when its condition matches the env."""

    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {"any": directives.flag, "not": directives.flag}
    has_content = True

    def run(self) -> list[nodes.Node]:
        # required_arguments=1 + optional_arguments=1 + final_argument_
        # whitespace captures every space-separated token across (at most) two
        # arguments; rejoin and re-split to recover the full token list.
        tokens = " ".join(self.arguments).split()
        env = self.config.rsp_env
        results: list[bool] = []
        for token in tokens:
            result = resolve_condition(env, token)
            if result is None:
                warn_unknown_condition(token, location=self.get_location())
                result = False
            results.append(result)
        match = any(results) if "any" in self.options else all(results)
        if "not" in self.options:
            match = not match
        if not match:
            return []
        return self.parse_content_to_nodes(allow_section_headings=True)
