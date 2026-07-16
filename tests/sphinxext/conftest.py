"""Shared fixtures for the sphinxext test suite."""

from __future__ import annotations

from collections.abc import Callable, Iterator, Mapping, Sequence
from pathlib import Path

import pytest
from rubin.repertoire import Discovery
from sphinx.testing.util import SphinxTestApp

from rspdocs.discovery.metadata import EnvMeta
from rspdocs.discovery.models import PhalanxEnv

# Re-export the discovery fixtures so tests here can build PhalanxEnv objects
# from the same captured discovery JSON used by the discovery test suite.
from tests.discovery.conftest import discovery_data_dir, discovery_texts

# ``__all__`` marks the imports above as an intentional re-export (they are
# consumed as pytest fixtures, not referenced by name in this module).
__all__ = ["discovery_data_dir", "discovery_texts"]


@pytest.fixture
def make_env(discovery_data_dir: Path) -> Callable[..., PhalanxEnv]:
    """Return a factory that builds a `PhalanxEnv` from a discovery fixture."""

    def _make(name: str, *, hidden_services: Sequence[str] = ()) -> PhalanxEnv:
        text = (discovery_data_dir / f"{name}.json").read_text()
        discovery = Discovery.model_validate_json(text)
        meta = EnvMeta(
            title=name,
            title_full=name,
            hidden_services=list(hidden_services),
        )
        return PhalanxEnv.from_discovery(discovery, name=name, meta=meta)

    return _make


@pytest.fixture
def app_factory(
    tmp_path: Path,
) -> Iterator[Callable[..., SphinxTestApp]]:
    """Return a factory that builds a `SphinxTestApp` with the extension on.

    Each call gets a fresh source directory, so a single test can exercise
    several environments. Every app created through the factory is torn down at
    the end of the test.
    """
    created: list[SphinxTestApp] = []
    count = 0

    def _make(
        env: PhalanxEnv,
        all_envs: Mapping[str, PhalanxEnv] | None = None,
        confoverrides: Mapping[str, object] | None = None,
    ) -> SphinxTestApp:
        nonlocal count
        count += 1
        srcdir = tmp_path / f"src{count}"
        srcdir.mkdir()
        (srcdir / "conf.py").write_text("extensions = ['rspdocs.sphinxext']\n")
        (srcdir / "index.rst").write_text("Index\n=====\n")
        overrides: dict[str, object] = {
            "rsp_env": env,
            "rsp_all_envs": dict(all_envs) if all_envs else {env.name: env},
            "rsp_discovery_hash": "test",
        }
        if confoverrides:
            overrides.update(confoverrides)
        app = SphinxTestApp(srcdir=srcdir, confoverrides=overrides)
        created.append(app)
        return app

    yield _make
    for app in created:
        app.cleanup()
