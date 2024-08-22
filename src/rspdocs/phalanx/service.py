"""Coordinate Phalanx metadata."""

from __future__ import annotations

import json
from pathlib import Path

from .models import EnvironmentDict, PhalanxEnv

__all__ = ["PhalanxEnvService"]


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
    def load_from_cache_file(cls, cache_path: Path) -> PhalanxEnvService:
        """Create a `PhalanxEnvService` from a locally cached environments data
        file.

        Parameters
        ----------
        cache_path
            Local path for the environments cache (a JSON file).

        Returns
        -------
        PhalanxEnvService
            The environment service created from cached data.
        """
        cache_data = json.loads(cache_path.read_text())
        envs = EnvironmentDict()
        for env_name, env_data in cache_data["environments"].items():
            envs[env_name] = PhalanxEnv.model_validate(env_data)
        return PhalanxEnvService(envs)

    @property
    def envs(self) -> EnvironmentDict:
        """The environments."""
        return self._envs
