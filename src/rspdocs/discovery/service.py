"""Coordinate Phalanx environment metadata from Repertoire discovery data."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import httpx
from rubin.repertoire import Discovery

from .metadata import load_environments_metadata
from .models import EnvironmentDict, PhalanxEnv

__all__ = ["PhalanxEnvService"]

DEFAULT_BASE_URL = "https://phalanx.lsst.io/discovery/environments"
"""Base URL for the static per-environment Repertoire discovery JSON files."""


class PhalanxEnvService:
    """A service for obtaining and providing access to Phalanx metadata.

    Parameters
    ----------
    env_data
        Data about the environments. Typically you should use a class method to
        load this data from the internet or from a local cache.
    """

    def __init__(self, env_data: EnvironmentDict) -> None:
        self._envs = env_data

    @classmethod
    def load(
        cls,
        *,
        cache_dir: Path,
        base_url: str = DEFAULT_BASE_URL,
        env_names: Sequence[str] | None = None,
    ) -> PhalanxEnvService:
        """Create a `PhalanxEnvService` from freshly-fetched Repertoire
        discovery data, falling back to a local cache when offline.

        For each requested environment, the per-environment discovery
        JSON is fetched from ``{base_url}/{env}.json`` and cached to
        ``cache_dir/{env}.json``. If the fetch fails (no network, an HTTP
        error, etc.), the previously-cached copy is used instead and a loud
        banner is printed to the build output. If neither the network nor a
        cache is available for an environment, an exception is raised.

        Parameters
        ----------
        cache_dir
            Directory for caching discovery JSON. Written on a successful
            fetch and read from when a fetch fails.
        base_url
            Base URL for the static per-environment discovery JSON files.
        env_names
            The environments to fetch. When `None` (the default), every
            environment in the build roster is fetched. When provided, only
            those environments are fetched; each must be present in the build
            roster's environment metadata, or a `KeyError` is raised.

        Returns
        -------
        PhalanxEnvService
            The environment service built from discovery data.
        """
        metadata = load_environments_metadata()
        cache_dir = Path(cache_dir)
        cache_dir.mkdir(parents=True, exist_ok=True)

        if env_names is None:
            names = list(metadata.build_roster)
        else:
            requested = set(env_names)
            missing = requested - set(metadata.environments)
            if missing:
                raise KeyError(
                    "Unknown environment(s) requested: "
                    f"{sorted(missing)}. Known environments: "
                    f"{sorted(metadata.environments)}."
                )
            # Preserve the roster ordering for the requested subset.
            names = [n for n in metadata.build_roster if n in requested]

        envs = EnvironmentDict()
        for name in names:
            meta = metadata.environments[name]
            discovery = cls._load_discovery(
                name=name,
                base_url=base_url,
                cache_path=cache_dir / f"{name}.json",
            )
            envs[name] = PhalanxEnv.from_discovery(
                discovery, name=name, meta=meta
            )
        return cls(envs)

    @staticmethod
    def _load_discovery(
        *, name: str, base_url: str, cache_path: Path
    ) -> Discovery:
        """Fetch discovery data for one environment, caching on success and
        falling back to the cache on failure.
        """
        url = f"{base_url}/{name}.json"
        try:
            response = httpx.get(url, timeout=30.0, follow_redirects=True)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            return PhalanxEnvService._load_from_cache(
                name=name, url=url, cache_path=cache_path, error=exc
            )
        discovery = Discovery.model_validate(response.json())
        cache_path.write_text(response.text)
        return discovery

    @staticmethod
    def _load_from_cache(
        *, name: str, url: str, cache_path: Path, error: Exception
    ) -> Discovery:
        """Load cached discovery data for one environment, announcing the
        fallback loudly.
        """
        if not cache_path.exists():
            raise RuntimeError(
                f"Could not fetch discovery data for {name!r} from {url} "
                f"({error}), and no cached copy exists at {cache_path}."
            ) from error
        # Use print() rather than the Sphinx logger: sphinx-build -n -W turns
        # warnings into errors, so a logged warning would fail the build. The
        # offline fallback must stay green.
        banner = "=" * 70
        print(
            f"\n{banner}\n"
            f"WARNING: could not fetch discovery data for {name!r}.\n"
            f"  URL:   {url}\n"
            f"  Error: {error}\n"
            f"Falling back to the cached copy at {cache_path}.\n"
            f"The build output for {name!r} may be stale.\n"
            f"{banner}\n"
        )
        return Discovery.model_validate_json(cache_path.read_text())

    @property
    def envs(self) -> EnvironmentDict:
        """The environments."""
        return self._envs
