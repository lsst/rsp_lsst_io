"""Doctree tests for the ``rsp-only`` directive."""

from __future__ import annotations

from collections.abc import Callable

from docutils import nodes
from sphinx.testing.restructuredtext import parse
from sphinx.testing.util import SphinxTestApp

from rspdocs.discovery.models import PhalanxEnv

MakeEnv = Callable[..., PhalanxEnv]
AppFactory = Callable[..., SphinxTestApp]

MARKER = "CONDITIONAL-BODY"
"""Sentinel text used to detect whether the directive body was emitted."""


def _snippet(*tokens: str, option: str = "") -> str:
    """Build an ``rsp-only`` snippet whose body contains ``MARKER``."""
    lines = [".. rsp-only:: " + " ".join(tokens)]
    if option:
        lines.append(f"   {option}")
    lines += ["", f"   {MARKER}", ""]
    return "\n".join(lines)


def _emitted(doctree: nodes.document) -> bool:
    return MARKER in doctree.astext()


def test_included_for_primary(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """``primary`` includes the body in the primary environment."""
    app = app_factory(make_env("idfprod", hidden_services=["times-square"]))
    doctree = parse(app, _snippet("primary"))
    assert _emitted(doctree)
    assert app.warning.getvalue() == ""


def test_excluded_for_nonprimary(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """Excluded content never enters the doctree."""
    app = app_factory(make_env("base"))
    doctree = parse(app, _snippet("primary"))
    assert not _emitted(doctree)


def test_env_name_token(make_env: MakeEnv, app_factory: AppFactory) -> None:
    """An environment-name token matches only that environment."""
    app = app_factory(make_env("base"))
    assert _emitted(parse(app, _snippet("base")))
    assert not _emitted(parse(app, _snippet("idfprod")))


def test_service_token(make_env: MakeEnv, app_factory: AppFactory) -> None:
    """A service token includes content only where the service exists."""
    idfprod = app_factory(
        make_env("idfprod", hidden_services=["times-square"])
    )
    assert _emitted(parse(idfprod, _snippet("tap")))
    base = app_factory(make_env("base"))
    assert not _emitted(parse(base, _snippet("tap")))


def test_default_conjunction_is_and(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """Multiple tokens default to AND: base has portal but not tap."""
    app = app_factory(make_env("base"))
    assert not _emitted(parse(app, _snippet("portal", "tap")))


def test_any_option_is_or(make_env: MakeEnv, app_factory: AppFactory) -> None:
    """``:any:`` switches to OR: base has portal, so the body is emitted."""
    app = app_factory(make_env("base"))
    assert _emitted(parse(app, _snippet("portal", "tap", option=":any:")))


def test_not_option_negates(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """``:not:`` negates the match."""
    base = app_factory(make_env("base"))
    assert _emitted(parse(base, _snippet("primary", option=":not:")))
    idfprod = app_factory(
        make_env("idfprod", hidden_services=["times-square"])
    )
    assert not _emitted(parse(idfprod, _snippet("primary", option=":not:")))


def test_unknown_token_warns_and_excludes(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """An unknown token warns and resolves to False (excluding the body)."""
    app = app_factory(make_env("base"))
    doctree = parse(app, _snippet("bogus"))
    assert not _emitted(doctree)
    assert "unknown-condition" in app.warning.getvalue()


def test_unknown_token_warning_is_suppressible(
    make_env: MakeEnv, app_factory: AppFactory
) -> None:
    """suppress_warnings silences the unknown-condition warning."""
    app = app_factory(
        make_env("base"),
        confoverrides={"suppress_warnings": ["rspdocs.unknown-condition"]},
    )
    parse(app, _snippet("bogus"))
    assert app.warning.getvalue() == ""
