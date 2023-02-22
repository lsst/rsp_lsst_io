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

# Add environment switcher
version = rsp_env.title  # noqa: F405
html_theme_options["switcher"] = {  # noqa: F405
    "json_url": (
        "https://gist.githubusercontent.com/jonathansick/bbe902507790911d40173"
        "f11a4a1a256/raw/547a1ada8db54aac2540ca8291f5aa0b79923251/"
        "rsp-versions.json"
    ),
    "version_match": rsp_env.title,
}
html_theme_options["navbar_center"] = [  # noqa: F405
    "version-switcher",
    "navbar-nav",
]
html_theme_options["navbar_align"] = "left"  # noqa: F405

# Update doc_path for the "Edit on GitHub" link. The DocumenteerGuide preset
# doesn't work here because docs/ doesn't contain the Sphinx conf.py.
html_context["doc_path"] = "docs"  # noqa: F405

html_static_path.append("docs/_static/versions.json")  # noqa: F405

# Delete any objects that needn't be pickled with the Sphinx configuration
del _config_template_loader
del _jinja_env
