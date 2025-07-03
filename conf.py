import glob
import os
from pathlib import Path
from typing import Optional

from documenteer.conf.guide import *  # noqa: F401 F403
from jinja2 import Environment, FileSystemLoader, select_autoescape

from rspdocs.phalanx.models import PhalanxEnv
from rspdocs.phalanx.service import PhalanxEnvService

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
if not rsp_env.times_square_url:
    exclude_patterns.append("guides/times-square/*.rst")
    exclude_patterns.append("guides/times-square/**/*.rst")

# Add environment switcher
version = rsp_env.title  # noqa: F405
html_theme_options["switcher"] = {  # noqa: F405
    "json_url": (
        "https://gist.githubusercontent.com/jonathansick/bbe902507790911d4017"
        "3f11a4a1a256/raw/50267ee4dc957bd817e93a12c79a1702377e6ae1"
        "/rsp-versions.json"
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

# FIXME(jonathansick): Remove TLS verification due to SSL issues with
# TOPCAT. Should be temporary.
tls_verify = False


def setup(app):
    def add_orphan_to_inbox(app, docname, source):
        # Add orphan metadata to files in guides/inbox/
        if docname.startswith("guides/inbox/"):
            import os

            # Get the file extension to determine format
            file_path = os.path.join(app.srcdir, docname + ".rst")
            if not os.path.exists(file_path):
                file_path = os.path.join(app.srcdir, docname + ".md")

            file_ext = os.path.splitext(file_path)[1].lower()

            if file_ext == ".rst":
                # RST format: use :orphan: directive
                print(f"Processing {docname} (RST) for orphan directive")
                source[0] = ":orphan:\n\n" + source[0]
            elif file_ext == ".md":
                # Markdown format: use YAML front-matter
                print(
                    f"Processing {docname} (Markdown) for orphan front-matter"
                )
                content = source[0]

                # Check if file already has YAML front-matter
                if content.startswith("---\n"):
                    # Find the end of existing front-matter
                    lines = content.split("\n")
                    end_idx = -1
                    for i, line in enumerate(lines[1:], 1):
                        if line.strip() == "---":
                            end_idx = i
                            break

                    if end_idx > 0:
                        # Insert orphan into existing front-matter
                        front_matter = lines[1:end_idx]
                        # Check if orphan already exists
                        has_orphan = any(
                            line.strip().startswith("orphan:")
                            for line in front_matter
                        )
                        if not has_orphan:
                            front_matter.append("orphan: true")

                        # Reconstruct content
                        new_lines = ["---"] + front_matter + lines[end_idx:]
                        source[0] = "\n".join(new_lines)
                    else:
                        # Malformed front-matter, add new one
                        source[0] = "---\norphan: true\n---\n\n" + content
                else:
                    # No existing front-matter, add new one
                    source[0] = "---\norphan: true\n---\n\n" + content

    def add_toctree_to_inbox_index(app, docname, source):
        # Add auto-generated toctree to guides/inbox/index.rst
        if docname == "guides/inbox/index":
            # Find all .rst and .md files in guides/inbox/ except index.rst
            inbox_dir = os.path.join(app.srcdir, "guides", "inbox")
            rst_files = glob.glob(os.path.join(inbox_dir, "*.rst"))
            md_files = glob.glob(os.path.join(inbox_dir, "*.md"))

            # Get basenames and exclude index.rst
            all_files = []
            for file_path in rst_files + md_files:
                basename = os.path.basename(file_path)
                if basename != "index.rst":
                    # Remove extension for toctree
                    name_without_ext = os.path.splitext(basename)[0]
                    all_files.append(name_without_ext)

            # Sort files alphabetically
            all_files.sort()

            if all_files:
                # Create toctree directive
                toctree_content = "\n\n.. toctree::\n   :maxdepth: 1\n\n"
                for file_name in all_files:
                    toctree_content += f"   {file_name}\n"

                # Append to the source
                source[0] = source[0] + toctree_content
                print(
                    f"Added toctree to {docname} with {len(all_files)} files"
                )

    app.connect("source-read", add_orphan_to_inbox)
    app.connect("source-read", add_toctree_to_inbox_index)
