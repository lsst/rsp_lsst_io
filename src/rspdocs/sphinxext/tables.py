"""The ``rsp-data-table`` directive: dataset/service availability matrices.

The directive renders a table from Repertoire discovery data at build time, so
authors don't hand-maintain which datasets expose which data-access services.
It has two shapes, chosen by the ``:scope:`` option:

* ``:scope: env`` (the default) -- one row per dataset served in the
  environment being built (omitting datasets that expose none of the
  data-access services), one column per data-access service (TAP, SIA, cutout,
  datalink, HiPS), each cell a check-mark linking to that dataset's service
  URL. This answers "which services can I use for each dataset here?".
* ``:scope: environments`` -- one row per dataset, one column per roster
  environment *that serves datasets* (dataset-less environments get no
  column), each cell marking whether a chosen ``:service:`` (default ``tap``)
  is available for that dataset in that environment. This answers "where is
  this dataset's TAP service deployed?" and needs discovery data for every
  roster environment, supplied through the ``rsp_all_envs`` config value.

A ``:services:`` option narrows the ``env`` scope to a subset of service
columns; a ``:datasets:`` option narrows either scope to a subset of dataset
rows. Unknown tokens or dataset names warn (fatal under ``-W``). When no
dataset rows remain -- notably in an environment that serves no datasets --
the directive emits nothing rather than a header-only table.
"""

from __future__ import annotations

from collections.abc import Sequence

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

from ..discovery.models import DATASET_SERVICES, PhalanxEnv
from .logging import warn_unknown_dataset, warn_unknown_dataset_service
from .services import DATASET_SERVICE_LABELS, resolve_dataset_url

__all__ = ["RspDataTable"]

_CHECK = "✓"  # check mark for an available service
_DASH = "—"  # em dash for an absent one


def _tokens(raw: str | None) -> list[str]:
    """Split a comma/whitespace option value into a list of tokens."""
    if not raw:
        return []
    return raw.replace(",", " ").split()


class RspDataTable(SphinxDirective):
    """Render a dataset/service availability table from discovery data."""

    has_content = False
    option_spec = {
        "scope": lambda a: directives.choice(a, ("env", "environments")),
        "service": directives.unchanged,
        "services": directives.unchanged,
        "datasets": directives.unchanged,
        "title": directives.unchanged,
    }

    def run(self) -> list[nodes.Node]:
        scope = self.options.get("scope", "env")
        if scope == "environments":
            return self._run_environments()
        return self._run_env()

    # -- helpers ----------------------------------------------------------

    def _service_columns(self) -> list[str]:
        """Return the dataset-service tokens to use as columns."""
        requested = _tokens(self.options.get("services"))
        if not requested:
            return list(DATASET_SERVICES)
        columns: list[str] = []
        for token in requested:
            if token not in DATASET_SERVICES:
                warn_unknown_dataset_service(
                    token, location=self.get_location()
                )
                continue
            columns.append(token)
        return columns

    def _dataset_rows(self, env: PhalanxEnv) -> list[str]:
        """Return the dataset names to use as rows, in discovery order.

        By default, datasets that expose none of the data-access services are
        omitted (they would render an all-dash row). An explicit ``:datasets:``
        request keeps such datasets, but a requested name that is not served
        in this environment warns and is dropped.
        """
        requested = _tokens(self.options.get("datasets"))
        if not requested:
            return [
                name for name, info in env.datasets.items() if info.services
            ]
        # Preserve the requested order; warn on names not served here.
        rows: list[str] = []
        for name in requested:
            if name not in env.datasets:
                warn_unknown_dataset(
                    name,
                    f"the {env.name!r} environment",
                    location=self.get_location(),
                )
                continue
            rows.append(name)
        return rows

    def _all_dataset_names(self, envs: Sequence[PhalanxEnv]) -> list[str]:
        """Return dataset names across ``envs``, discovery order, de-duped.

        A ``:datasets:`` request preserves its own order; a requested name
        served in none of the environments warns and is dropped.
        """
        served: list[str] = []
        for env in envs:
            for name in env.datasets:
                if name not in served:
                    served.append(name)
        requested = _tokens(self.options.get("datasets"))
        if not requested:
            return served
        names: list[str] = []
        for name in requested:
            if name not in served:
                warn_unknown_dataset(
                    name, "any environment", location=self.get_location()
                )
                continue
            names.append(name)
        return names

    @staticmethod
    def _build_table(
        headers: Sequence[str],
        rows: Sequence[Sequence[nodes.Node]],
        *,
        title: str | None,
    ) -> nodes.table:
        """Assemble a docutils table node from header/row content nodes."""
        table = nodes.table()
        if title:
            table += nodes.title("", title)
        tgroup = nodes.tgroup(cols=len(headers))
        table += tgroup
        for _ in headers:
            tgroup += nodes.colspec(colwidth=1)
        thead = nodes.thead()
        tgroup += thead
        header_row = nodes.row()
        for label in headers:
            entry = nodes.entry()
            entry += nodes.paragraph("", "", nodes.Text(label))
            header_row += entry
        thead += header_row
        tbody = nodes.tbody()
        tgroup += tbody
        for row in rows:
            table_row = nodes.row()
            for cell in row:
                entry = nodes.entry()
                entry += cell
                table_row += entry
            tbody += table_row
        return table

    @staticmethod
    def _cell(content: nodes.Node) -> nodes.paragraph:
        """Wrap inline content in a paragraph for a table cell."""
        para = nodes.paragraph()
        para += content
        return para

    def _link_or_mark(self, url: str | None) -> nodes.paragraph:
        """A linked check-mark when ``url`` is set, else a plain em dash."""
        if url is None:
            return self._cell(nodes.Text(_DASH))
        ref = nodes.reference("", _CHECK, refuri=url, internal=False)
        return self._cell(ref)

    # -- scope: env -------------------------------------------------------

    def _run_env(self) -> list[nodes.Node]:
        env: PhalanxEnv = self.config.rsp_env
        columns = self._service_columns()
        datasets = self._dataset_rows(env)
        if not datasets:
            # No rows (for example, an environment serving no datasets):
            # emit nothing rather than a header-only table.
            return []
        headers = ["Dataset"] + [
            DATASET_SERVICE_LABELS[token] for token in columns
        ]
        rows: list[list[nodes.Node]] = []
        for dataset in datasets:
            cells: list[nodes.Node] = [self._cell(nodes.literal("", dataset))]
            for token in columns:
                url = resolve_dataset_url(env, token, dataset)
                cells.append(self._link_or_mark(url))
            rows.append(cells)
        title = self.options.get("title")
        return [self._build_table(headers, rows, title=title)]

    # -- scope: environments ----------------------------------------------

    def _run_environments(self) -> list[nodes.Node]:
        all_envs: dict[str, PhalanxEnv] = self.config.rsp_all_envs or {}
        # Only environments that serve at least one dataset are worth a column.
        envs = [env for env in all_envs.values() if env.datasets]
        service = self.options.get("service", "tap")
        if service not in DATASET_SERVICES:
            warn_unknown_dataset_service(service, location=self.get_location())
            service = "tap"
        datasets = self._all_dataset_names(envs)
        if not datasets:
            # No dataset rows anywhere in the fleet: emit nothing.
            return []
        # Column headings use the human-readable environment title.
        headers = ["Dataset"] + [env.title for env in envs]
        rows: list[list[nodes.Node]] = []
        for dataset in datasets:
            cells: list[nodes.Node] = [self._cell(nodes.literal("", dataset))]
            for env in envs:
                url = resolve_dataset_url(env, service, dataset)
                cells.append(self._link_or_mark(url))
            rows.append(cells)
        title = self.options.get(
            "title",
            f"{DATASET_SERVICE_LABELS[service]} service availability",
        )
        return [self._build_table(headers, rows, title=title)]
