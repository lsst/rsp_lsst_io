"""Doctree tests for the :rsp-url: and :rsp-link: roles."""

from __future__ import annotations

from collections.abc import Callable

from docutils import nodes
from sphinx.testing.restructuredtext import parse
from sphinx.testing.util import SphinxTestApp

from rspdocs.discovery.models import PhalanxEnv

MakeEnv = Callable[..., PhalanxEnv]
AppFactory = Callable[..., SphinxTestApp]


def test_rsp_url_emits_literal(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """``:rsp-url:`service``` renders the URL as a code literal."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-url:`tap`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "https://data.lsst.cloud/api/tap/"
    assert app.warning.getvalue() == ""


def test_rsp_link_default_text_is_url(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """With no explicit title, the link text is the URL itself."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-link:`rsp`")
    ref = doctree.next_node(nodes.reference)
    assert isinstance(ref, nodes.reference)
    assert ref["refuri"] == "https://data.lsst.cloud/"
    assert ref.astext() == "https://data.lsst.cloud/"
    assert ref.get("internal") is False
    assert app.warning.getvalue() == ""


def test_rsp_link_explicit_title(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """``:rsp-link:`Title <service>``` uses Title as the link text."""
    app = app_factory(make_env("idfint"))  # times-square deployed here
    doctree = parse(app, ":rsp-link:`Times Square <times-square>`")
    ref = doctree.next_node(nodes.reference)
    assert isinstance(ref, nodes.reference)
    assert ref.astext() == "Times Square"
    assert ref["refuri"].endswith("/times-square/")
    assert app.warning.getvalue() == ""


def test_rsp_url_unknown_service_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """An unknown service token warns and falls back to a literal token."""
    app = app_factory(make_env("base"))
    doctree = parse(app, ":rsp-url:`bogus`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "bogus"
    assert "unknown-service" in app.warning.getvalue()


def test_rsp_link_unavailable_service_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A known-but-absent service warns and emits no broken empty link."""
    app = app_factory(make_env("base"))  # base has no tap
    doctree = parse(app, ":rsp-link:`tap`")
    assert doctree.next_node(nodes.reference) is None
    assert "unavailable-service" in app.warning.getvalue()


def test_role_warning_is_suppressible(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """suppress_warnings silences the rspdocs warning family."""
    app = app_factory(
        make_env("base"),
        confoverrides={"suppress_warnings": ["rspdocs.unavailable-service"]},
    )
    parse(app, ":rsp-link:`tap`")
    assert app.warning.getvalue() == ""
