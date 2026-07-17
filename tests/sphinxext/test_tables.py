"""Doctree tests for the ``rsp-data-table`` directive."""

from __future__ import annotations

from collections.abc import Callable

from docutils import nodes
from sphinx.testing.restructuredtext import parse
from sphinx.testing.util import SphinxTestApp

from rspdocs.discovery.models import PhalanxEnv

MakeEnv = Callable[..., PhalanxEnv]
AppFactory = Callable[..., SphinxTestApp]


def _table(doctree: nodes.document) -> nodes.table:
    return next(iter(doctree.findall(nodes.table)))


def _headers(table: nodes.table) -> list[str]:
    thead = next(iter(table.findall(nodes.thead)))
    row = next(iter(thead.findall(nodes.row)))
    return [entry.astext() for entry in row.findall(nodes.entry)]


def _body_rows(table: nodes.table) -> list[list[str]]:
    tbody = next(iter(table.findall(nodes.tbody)))
    return [
        [entry.astext() for entry in row.findall(nodes.entry)]
        for row in tbody.findall(nodes.row)
    ]


def test_env_scope_columns_are_services(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """The default scope has one column per data-access service."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    table = _table(parse(app, ".. rsp-data-table::"))
    assert _headers(table) == [
        "Dataset",
        "TAP",
        "SIA",
        "Cutout (SODA)",
        "DataLink",
        "HiPS",
    ]
    rows = _body_rows(table)
    # One row per dataset served in idfprod, in discovery order. ``prompt``
    # exposes none of the data-access services, so it is omitted by default.
    assert [row[0] for row in rows] == ["dp02", "dp03", "dp1"]
    # dp1 exposes every service (a check mark in each cell).
    dp1 = next(row for row in rows if row[0] == "dp1")
    assert dp1[1:] == ["✓", "✓", "✓", "✓", "✓"]
    # dp03 exposes only TAP; the rest are em dashes.
    dp03 = next(row for row in rows if row[0] == "dp03")
    assert dp03[1:] == ["✓", "—", "—", "—", "—"]
    assert app.warning.getvalue() == ""


def test_env_scope_links_to_service_urls(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """Each available cell links to that dataset's service URL."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    table = _table(parse(app, ".. rsp-data-table::"))
    refs = [r["refuri"] for r in table.findall(nodes.reference)]
    assert "https://data.lsst.cloud/api/tap" in refs
    assert "https://data.lsst.cloud/api/sia/dp1" in refs


def test_env_scope_services_option_narrows_columns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """The ``:services:`` option restricts the service columns."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    table = _table(parse(app, ".. rsp-data-table::\n   :services: tap, sia\n"))
    assert _headers(table) == ["Dataset", "TAP", "SIA"]
    assert app.warning.getvalue() == ""


def test_env_scope_datasets_option_narrows_rows(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """The ``:datasets:`` option restricts the dataset rows."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    table = _table(parse(app, ".. rsp-data-table::\n   :datasets: dp1\n"))
    assert [row[0] for row in _body_rows(table)] == ["dp1"]


def test_env_scope_explicit_dataset_without_services(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """An explicitly requested dataset is kept even with no services.

    ``prompt`` is omitted from the default rows (it exposes none of the
    data-access services), but naming it in ``:datasets:`` includes it as an
    all-dash row without warning.
    """
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    table = _table(parse(app, ".. rsp-data-table::\n   :datasets: prompt\n"))
    rows = _body_rows(table)
    assert [row[0] for row in rows] == ["prompt"]
    assert rows[0][1:] == ["—", "—", "—", "—", "—"]
    assert app.warning.getvalue() == ""


def test_env_scope_no_datasets_emits_nothing(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """An environment serving no datasets renders no table at all."""
    app = app_factory(make_env("base"))
    doctree = parse(app, ".. rsp-data-table::")
    assert next(iter(doctree.findall(nodes.table)), None) is None
    assert app.warning.getvalue() == ""


def test_env_scope_unknown_dataset_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A ``:datasets:`` name not served in this environment warns."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    table = _table(
        parse(app, ".. rsp-data-table::\n   :datasets: dp1 bogus\n")
    )
    assert [row[0] for row in _body_rows(table)] == ["dp1"]
    assert "unknown-dataset" in app.warning.getvalue()


def test_unknown_service_column_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """An unknown ``:services:`` token warns and is dropped from the table."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    table = _table(
        parse(app, ".. rsp-data-table::\n   :services: tap bogus\n")
    )
    assert _headers(table) == ["Dataset", "TAP"]
    assert "unknown-dataset-service" in app.warning.getvalue()


def test_environments_scope_matrix(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """The ``environments`` scope makes columns of dataset-serving envs."""
    envs = {
        name: make_env(name, hidden_services=["times-square"])
        for name in ("idfprod", "usdfprod", "base")
    }
    app = app_factory(envs["idfprod"], all_envs=envs)
    table = _table(
        parse(app, ".. rsp-data-table::\n   :scope: environments\n")
    )
    headers = _headers(table)
    # base serves no datasets, so it is not a column; idfprod/usdfprod are.
    # Columns are labelled with env.title (the make_env fixture titles each
    # environment with its name).
    assert headers == ["Dataset", "idfprod", "usdfprod"]
    rows = _body_rows(table)
    # dp1 has TAP in both idfprod and usdfprod.
    dp1 = next(row for row in rows if row[0] == "dp1")
    assert dp1 == ["dp1", "✓", "✓"]
    assert app.warning.getvalue() == ""


def test_environments_scope_service_option(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """The ``:service:`` option chooses which service the matrix shows.

    dp1 exposes SIA on idfprod but not on usdfprod, so the SIA matrix differs
    across the two environment columns.
    """
    envs = {
        name: make_env(name, hidden_services=["times-square"])
        for name in ("idfprod", "usdfprod")
    }
    app = app_factory(envs["idfprod"], all_envs=envs)
    table = _table(
        parse(
            app,
            ".. rsp-data-table::\n   :scope: environments\n   :service: sia\n",
        )
    )
    rows = _body_rows(table)
    dp1 = next(row for row in rows if row[0] == "dp1")
    # SIA present on idfprod, absent on usdfprod.
    assert dp1 == ["dp1", "✓", "—"]
    assert app.warning.getvalue() == ""


def test_environments_scope_unknown_dataset_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A ``:datasets:`` name served in no environment warns and is dropped."""
    envs = {
        name: make_env(name, hidden_services=["times-square"])
        for name in ("idfprod", "usdfprod")
    }
    app = app_factory(envs["idfprod"], all_envs=envs)
    table = _table(
        parse(
            app,
            ".. rsp-data-table::\n"
            "   :scope: environments\n"
            "   :datasets: dp1 bogus\n",
        )
    )
    assert [row[0] for row in _body_rows(table)] == ["dp1"]
    warnings = app.warning.getvalue()
    assert "unknown-dataset" in warnings
    assert "any environment" in warnings


def test_environments_scope_column_titles(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """Environment columns are labelled with env.title, not env.name."""
    env = make_env("idfprod", hidden_services=["times-square"])
    env = env.model_copy(update={"title": "data.lsst.cloud"})
    app = app_factory(env, all_envs={"idfprod": env})
    table = _table(
        parse(app, ".. rsp-data-table::\n   :scope: environments\n")
    )
    assert _headers(table) == ["Dataset", "data.lsst.cloud"]
    assert app.warning.getvalue() == ""
