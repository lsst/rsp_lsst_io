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


def test_rsp_url_with_path(make_env: MakeEnv, app_factory: AppFactory) -> None:
    """``:rsp-url:`service/path``` appends the path to the service URL."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-url:`rsp/settings/quotas`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "https://data.lsst.cloud/settings/quotas"
    assert app.warning.getvalue() == ""


def test_rsp_link_with_path(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A titled link target may carry a path; extra slashes are normalized."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-link:`Account <rsp//settings>`")
    ref = doctree.next_node(nodes.reference)
    assert isinstance(ref, nodes.reference)
    assert ref.astext() == "Account"
    assert ref["refuri"] == "https://data.lsst.cloud/settings"
    assert app.warning.getvalue() == ""


def test_rsp_link_path_joins_service_url_path(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """The join is against the service's full URL, not the host root."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-link:`Firefly <portal/onlinehelp/>`")
    ref = doctree.next_node(nodes.reference)
    assert isinstance(ref, nodes.reference)
    assert ref["refuri"].endswith("/portal/app/onlinehelp/")
    assert app.warning.getvalue() == ""


def test_rsp_url_unknown_service_with_path_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """An unknown service with a path warns and echoes the whole target."""
    app = app_factory(make_env("base"))
    doctree = parse(app, ":rsp-url:`bogus/settings`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "bogus/settings"
    assert "unknown-service" in app.warning.getvalue()


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


# -- Dataset-aware roles --------------------------------------------------


def test_rsp_data_url_emits_literal(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """``:rsp-data-url:`tap dp1``` renders the dataset TAP URL as a literal."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-data-url:`tap dp1`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "https://data.lsst.cloud/api/tap"
    assert app.warning.getvalue() == ""


def test_rsp_data_url_with_path(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A path after the dataset joins onto the dataset service URL."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-data-url:`tap dp1/tables`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "https://data.lsst.cloud/api/tap/tables"
    assert app.warning.getvalue() == ""


def test_rsp_data_link_default_and_titled(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """The link twin defaults to the URL and honors an explicit title."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-data-link:`sia dp1`")
    ref = doctree.next_node(nodes.reference)
    assert isinstance(ref, nodes.reference)
    assert ref["refuri"] == "https://data.lsst.cloud/api/sia/dp1"
    assert ref.astext() == "https://data.lsst.cloud/api/sia/dp1"
    assert ref.get("internal") is False

    titled = parse(app, ":rsp-data-link:`DP1 images <sia dp1>`")
    ref2 = titled.next_node(nodes.reference)
    assert isinstance(ref2, nodes.reference)
    assert ref2.astext() == "DP1 images"
    assert app.warning.getvalue() == ""


def test_rsp_data_url_malformed_target_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A target missing the dataset half warns and echoes the raw text."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-data-url:`tap`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "tap"
    assert "malformed-dataset-target" in app.warning.getvalue()


def test_rsp_data_url_extra_tokens_warn(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A target with more than two tokens is malformed, not truncated."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-data-url:`tap dp1 tables`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "tap dp1 tables"
    assert "malformed-dataset-target" in app.warning.getvalue()


def test_rsp_data_url_unknown_service_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A non-dataset service token warns as unknown-dataset-service."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-data-url:`gms dp1`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "gms dp1"
    assert "unknown-dataset-service" in app.warning.getvalue()


def test_rsp_data_url_unavailable_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A dataset that doesn't expose the service warns (fatal under -W)."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    # dp03 exposes only TAP, so SIA is unavailable.
    doctree = parse(app, ":rsp-data-url:`sia dp03`")
    literal = doctree.next_node(nodes.literal)
    assert isinstance(literal, nodes.literal)
    assert literal.astext() == "sia dp03"
    assert "unavailable-dataset" in app.warning.getvalue()


def test_rsp_data_link_absent_dataset_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A dataset absent from the environment warns and emits no link."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-data-link:`tap nope`")
    assert doctree.next_node(nodes.reference) is None
    assert "unavailable-dataset" in app.warning.getvalue()


def test_rsp_dataset_docs_resolves(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """``:rsp-dataset-docs:`dp1``` links to the dataset's docs_url."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-dataset-docs:`dp1`")
    ref = doctree.next_node(nodes.reference)
    assert isinstance(ref, nodes.reference)
    assert ref["refuri"] == "https://dp1.lsst.io/"

    titled = parse(app, ":rsp-dataset-docs:`Data Preview 1 <dp1>`")
    ref2 = titled.next_node(nodes.reference)
    assert isinstance(ref2, nodes.reference)
    assert ref2.astext() == "Data Preview 1"
    assert app.warning.getvalue() == ""


def test_rsp_dataset_docs_missing_url_warns(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """A dataset without a docs_url warns and falls back to the title.

    The warning is the dedicated docs subtype with an accurate message, not
    the generic unavailable-dataset one (which would misleadingly call
    ``docs`` a service the dataset fails to expose).
    """
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, ":rsp-dataset-docs:`Prompt <prompt>`")
    assert doctree.next_node(nodes.reference) is None
    assert doctree.astext().strip() == "Prompt"
    warnings = app.warning.getvalue()
    assert "unavailable-dataset-docs" in warnings
    assert "no documentation URL for dataset 'prompt'" in warnings
