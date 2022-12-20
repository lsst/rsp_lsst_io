from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Optional

from documenteer.conf.guide import *  # noqa: F401 F403

from rspdocs.phalanx.service import PhalanxEnvService
from rspdocs.phalanx.models import PhalanxEnv

env_cache_path = Path(__file__).parent.joinpath(".phalanxenvs.json")
env_service = PhalanxEnvService.load_from_cache_file(env_cache_path)

# Select the environment given the sphinx tag (-t on sphinx-build CLI)
# Default to the primary env if a tag is not set.
env_names = env_service.envs.env_names
rsp_env: Optional[PhalanxEnv] = None
for env_name in env_names:
    if env_name in tags:  # noqa: F405 F821
        rsp_env = env_service.envs[env_name]
        break
if rsp_env is None:
    rsp_env = env_service.envs.primary

_config_template_loader = FileSystemLoader(".")
_jinja_env = Environment(
    loader=_config_template_loader, autoescape=select_autoescape()
)
rst_epilog = _jinja_env.get_template("rst_epilog.rst.jinja").render(
    env=rsp_env
)

# Configure Jinja Sphinx extension
jinja_contexts = {"rsp": {"env": rsp_env, "all_envs": env_service.envs}}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    "**/*.in.rst",  # rst files meant to be used for include directives
    "**/*.rst.jinja",  # Jinja templates for sphinx-jinja
]

# Ignore specific files that are ignored because the relevant services
# aren't available in that environment.
if not rsp_env.portal_url:
    exclude_patterns.append("guides/portal/**/*.rst")
    exclude_patterns.append("guides/getting-started/portal-first-steps.rst")
if not rsp_env.nb_url:
    exclude_patterns.append("guides/nb/**/*.rst")
    exclude_patterns.append("guides/getting-started/notebook-first-steps.rst")
if not rsp_env.api_tap_url:
    exclude_patterns.append("guides/auth/using-topcat-outside-rsp.rst")

# Delete any objects that needen't be picked with the Sphinx configuration
del _config_template_loader
del _jinja_env
