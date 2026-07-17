"""Unit tests for the sphinxext service registry and condition resolver."""

from __future__ import annotations

from collections.abc import Callable

from rspdocs.discovery.models import PhalanxEnv
from rspdocs.sphinxext.services import (
    SERVICE_PAGE_EXCLUDES,
    excluded_page_patterns,
    is_available,
    is_known_dataset_service,
    is_known_service,
    resolve_condition,
    resolve_dataset_docs_url,
    resolve_dataset_url,
    resolve_url,
    split_dataset_target,
    split_service_path,
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


def test_split_service_path() -> None:
    """A target splits at the first slash into (service, path)."""
    assert split_service_path("rsp") == ("rsp", "")
    assert split_service_path("rsp/settings") == ("rsp", "settings")
    assert split_service_path("rsp//settings") == ("rsp", "/settings")
    assert split_service_path("portal/onlinehelp/") == (
        "portal",
        "onlinehelp/",
    )
    assert split_service_path("times-square") == ("times-square", "")


def test_resolve_url_with_path(make_env: MakeEnv) -> None:
    """An appended path joins relative to the service URL, slash-normalized."""
    env = make_env("idfprod", hidden_services=["times-square"])
    expected = "https://data.lsst.cloud/settings/quotas"
    assert resolve_url(env, "rsp", path="settings/quotas") == expected
    # A leading slash on the path is normalized away, not host-root-resolved.
    assert resolve_url(env, "rsp", path="/settings/quotas") == expected
    # The join is against the service's full URL, including its own path, and
    # the trailing slash of the result follows the path as written.
    assert resolve_url(env, "portal", path="onlinehelp/") == (
        "https://data.lsst.cloud/portal/app/onlinehelp/"
    )
    # An empty path returns the service URL untouched.
    assert resolve_url(env, "rsp", path="") == "https://data.lsst.cloud/"
    # An absent service stays None regardless of path.
    assert resolve_url(make_env("base"), "tap", path="x") is None


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


def test_is_known_dataset_service() -> None:
    """Dataset service tokens are recognized; plain services aren't."""
    assert is_known_dataset_service("tap")
    assert is_known_dataset_service("sia")
    assert is_known_dataset_service("hips")
    assert not is_known_dataset_service("gms")  # not user-facing
    assert not is_known_dataset_service("portal")  # a UI service
    assert not is_known_dataset_service("bogus")


def test_split_dataset_target() -> None:
    """A dataset target splits into (service, dataset, path)."""
    assert split_dataset_target("tap dp1") == ("tap", "dp1", "")
    assert split_dataset_target("tap dp1/tables") == ("tap", "dp1", "tables")
    # Any amount of whitespace may separate the two tokens.
    assert split_dataset_target("sia   dp02") == ("sia", "dp02", "")
    # A single token yields no dataset (malformed).
    assert split_dataset_target("tap") == ("tap", "", "")
    assert split_dataset_target("") == ("", "", "")
    # More than two tokens is malformed too, not silently truncated.
    assert split_dataset_target("tap dp1 tables") == ("tap", "", "")


def test_resolve_dataset_url_present(make_env: MakeEnv) -> None:
    """A dataset's service resolves to its exact URL, with optional path."""
    env = make_env("idfprod", hidden_services=["times-square"])
    assert (
        resolve_dataset_url(env, "tap", "dp1")
        == "https://data.lsst.cloud/api/tap"
    )
    assert resolve_dataset_url(env, "tap", "dp1", path="tables") == (
        "https://data.lsst.cloud/api/tap/tables"
    )
    # A leading slash on the path is normalized, not host-root-resolved.
    assert resolve_dataset_url(env, "tap", "dp1", path="/tables") == (
        "https://data.lsst.cloud/api/tap/tables"
    )


def test_resolve_dataset_url_absent(make_env: MakeEnv) -> None:
    """Absent datasets, absent services, and unknown datasets are None."""
    env = make_env("idfprod", hidden_services=["times-square"])
    # dp03 exposes only TAP, so SIA is absent.
    assert resolve_dataset_url(env, "sia", "dp03") is None
    # An unknown dataset name resolves to None.
    assert resolve_dataset_url(env, "tap", "nope") is None
    # An environment without datasets has nothing to resolve.
    assert resolve_dataset_url(make_env("base"), "tap", "dp1") is None


def test_resolve_dataset_docs_url(make_env: MakeEnv) -> None:
    """A dataset's docs_url resolves, or None when absent/unset."""
    env = make_env("idfprod", hidden_services=["times-square"])
    assert resolve_dataset_docs_url(env, "dp1") == "https://dp1.lsst.io/"
    # The prompt dataset has no docs_url in discovery.
    assert resolve_dataset_docs_url(env, "prompt") is None
    # An unknown dataset resolves to None.
    assert resolve_dataset_docs_url(env, "nope") is None


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
