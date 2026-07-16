"""Unit tests for the sphinxext service registry and condition resolver."""

from __future__ import annotations

from collections.abc import Callable

from rspdocs.discovery.models import PhalanxEnv
from rspdocs.sphinxext.services import (
    SERVICE_PAGE_EXCLUDES,
    excluded_page_patterns,
    is_available,
    is_known_service,
    resolve_condition,
    resolve_url,
)

MakeEnv = Callable[..., PhalanxEnv]


def test_is_known_service() -> None:
    """Service tokens (and their aliases) are recognized; env names aren't."""
    assert is_known_service("rsp")
    assert is_known_service("squareone")
    assert is_known_service("times-square")
    assert not is_known_service("bogus")
    assert not is_known_service("idfprod")  # an env name, not a service
    assert not is_known_service("primary")  # a condition keyword


def test_resolve_url_present(make_env: MakeEnv) -> None:
    """A deployed service resolves to its exact URL string."""
    env = make_env("idfprod", hidden_services=["times-square"])
    assert resolve_url(env, "rsp") == "https://data.lsst.cloud/"
    assert resolve_url(env, "tap") == "https://data.lsst.cloud/api/tap/"
    # Aliases resolve to the same attribute.
    assert resolve_url(env, "squareone") == resolve_url(env, "rsp")
    assert resolve_url(env, "nb") == resolve_url(env, "nublado")


def test_resolve_url_absent(make_env: MakeEnv) -> None:
    """Unknown, undeployed, and hidden services all resolve to None."""
    base = make_env("base")
    assert resolve_url(base, "tap") is None  # base has no datasets
    assert resolve_url(base, "bogus") is None  # unknown service token
    idfprod = make_env("idfprod", hidden_services=["times-square"])
    assert resolve_url(idfprod, "times-square") is None  # hidden in shim


def test_is_available(make_env: MakeEnv) -> None:
    """Availability tracks the presence of a resolved URL."""
    idfprod = make_env("idfprod", hidden_services=["times-square"])
    base = make_env("base")
    idfint = make_env("idfint")
    assert is_available(idfprod, "tap")
    assert not is_available(base, "tap")
    assert not is_available(idfprod, "times-square")  # hidden
    assert is_available(idfint, "times-square")  # staff env shows it


def test_resolve_condition_primary(make_env: MakeEnv) -> None:
    """The ``primary`` keyword resolves via PhalanxEnv.is_primary."""
    idfprod = make_env("idfprod", hidden_services=["times-square"])
    assert resolve_condition(idfprod, "primary") is True
    assert resolve_condition(make_env("base"), "primary") is False


def test_resolve_condition_env_name(make_env: MakeEnv) -> None:
    """An environment-name token matches only that environment."""
    base = make_env("base")
    assert resolve_condition(base, "base") is True
    assert resolve_condition(base, "idfprod") is False


def test_resolve_condition_service(make_env: MakeEnv) -> None:
    """A service token resolves to that service's availability."""
    idfprod = make_env("idfprod", hidden_services=["times-square"])
    base = make_env("base")
    assert resolve_condition(idfprod, "tap") is True
    assert resolve_condition(base, "tap") is False


def test_resolve_condition_unknown(make_env: MakeEnv) -> None:
    """A token that is neither service, env, nor ``primary`` returns None."""
    assert resolve_condition(make_env("base"), "bogus") is None


def test_service_page_excludes_loaded_from_yaml() -> None:
    """The exclude map loads from YAML with only known-service keys."""
    assert SERVICE_PAGE_EXCLUDES  # non-empty
    for service, globs in SERVICE_PAGE_EXCLUDES.items():
        assert is_known_service(service), service
        assert globs and all(isinstance(g, str) for g in globs)


def test_excluded_page_patterns_absent_services(make_env: MakeEnv) -> None:
    """An env missing TAP and Times Square excludes their pages only.

    ``base`` has no datasets (no TAP) and no Times Square, but keeps portal and
    notebook guides.
    """
    patterns = excluded_page_patterns(make_env("base"))
    assert patterns == [
        "guides/auth/using-topcat-outside-rsp.rst",
        "guides/times-square/*.rst",
        "guides/times-square/**/*.rst",
    ]
    # Portal and notebook guides stay because those services are present.
    assert "guides/portal/**/*.rst" not in patterns
    assert "guides/nb/**/*.rst" not in patterns


def test_excluded_page_patterns_full_env(make_env: MakeEnv) -> None:
    """A fully-featured env (idfint) excludes nothing."""
    assert excluded_page_patterns(make_env("idfint")) == []


def test_excluded_page_patterns_hidden_service(make_env: MakeEnv) -> None:
    """A ``hidden_services`` entry makes the service absent for exclusions.

    idfprod deploys Times Square but hides it, so its pages are still excluded
    even though discovery reports the service.
    """
    patterns = excluded_page_patterns(
        make_env("idfprod", hidden_services=["times-square"])
    )
    assert patterns == [
        "guides/times-square/*.rst",
        "guides/times-square/**/*.rst",
    ]
