import glob
import hashlib
import json
import os
from pathlib import Path
from typing import Optional

from documenteer.conf.guide import *  # noqa: F401 F403
from jinja2 import Environment, FileSystemLoader, select_autoescape

from rspdocs.constants import PRIMARY_ENV
from rspdocs.discovery import load_environments_metadata
from rspdocs.discovery.models import PhalanxEnv
from rspdocs.discovery.service import PhalanxEnvService
from rspdocs.discovery.switcher import build_switcher_entries
from rspdocs.sphinxext.services import excluded_page_patterns

# Select the environment to build given the sphinx tag (-t on sphinx-build
# CLI), defaulting to the primary env if no tag matches. Each sphinx-build
# renders a single environment, so we only fetch that one -- plus the primary
# env, which the docs always reference via ``all_envs.primary`` regardless of
# which environment is being built.
_metadata = load_environments_metadata()
target_env = PRIMARY_ENV
for env_name in _metadata.build_roster:
    if env_name in tags:  # noqa: F405 F821
        target_env = env_name
        break
_fetch_envs = list(dict.fromkeys([target_env, PRIMARY_ENV]))

env_service = PhalanxEnvService.load(
    cache_dir=Path(__file__).parent / "_build" / "discovery",
    env_names=_fetch_envs,
)

rsp_env: Optional[PhalanxEnv] = env_service.envs[target_env]

# Enable the in-repo Sphinx extension providing the :rsp-url:/:rsp-link: roles
# and the .. rsp-only:: directive. ``extensions`` is exported by
# ``documenteer.conf.guide``. The extension's own setup() runs because it is in
# ``extensions``; don't also invoke it from the setup() below.
extensions.append("rspdocs.sphinxext")  # noqa: F405

# Enable |substitutions| inside code-block/literalinclude directives that carry
# the :substitutions: option, so code samples can embed environment URLs (e.g.
# the TAP URL in the notebooks FAQ). The substitutions themselves are defined
# in rst_prolog below.
extensions.append("sphinx_substitution_extensions")  # noqa: F405

# Data channels the extension resolves roles/conditions against.
rsp_all_envs = env_service.envs

# Hash of the discovery JSON that was just loaded. Registered with
# rebuild="env", this is the sole incremental-rebuild trigger: when discovery
# data changes its hash changes, so Sphinx reparses every doc and the roles
# re-bake fresh URLs into the doctrees.
_discovery_hash = hashlib.sha256()
for _name in _fetch_envs:
    _discovery_hash.update(
        (
            Path(__file__).parent / "_build" / "discovery" / f"{_name}.json"
        ).read_bytes()
    )
rsp_discovery_hash = _discovery_hash.hexdigest()

_config_template_loader = FileSystemLoader(".")
_jinja_env = Environment(
    loader=_config_template_loader, autoescape=select_autoescape()
)
# The substitutions and link targets are rendered into rst_prolog rather than
# rst_epilog because sphinx-substitution-extensions resolves |substitutions|
# inside code blocks at parse time: the definitions must already have been
# parsed when the directive runs, so they have to precede the page content.
rst_prolog = _jinja_env.get_template("rst_prolog.rst.jinja").render(
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

# Ignore source files whose service is absent in this environment. The
# service-token -> paths map and its is_available() logic live in the
# Sphinx-free services module, shared with the roles and the rsp-only
# directive.
exclude_patterns.extend(excluded_page_patterns(rsp_env))

# Add environment switcher
version = rsp_env.title  # noqa: F405

# Generate the version-switcher data from the build roster into the gitignored
# _build/ dir and register it as a static asset (copied to
# <edition>/_static/versions.json). The switcher points at THIS edition's own
# copy, which is freshly written on every build and complete because it lists
# every roster environment. This keeps each edition self-consistent and fresh
# even when other editions are rebuilt independently.
_switcher_path = Path(__file__).parent / "_build" / "versions.json"
_switcher_path.parent.mkdir(parents=True, exist_ok=True)
_switcher_path.write_text(
    json.dumps(build_switcher_entries(_metadata), indent=2) + "\n"
)
html_static_path.append(str(_switcher_path))  # noqa: F405

html_theme_options["switcher"] = {  # noqa: F405
    "json_url": f"{rsp_env.ltd_url_prefix}_static/versions.json",
    "version_match": rsp_env.name,
}
html_theme_options["navbar_center"] = [  # noqa: F405
    "version-switcher",
    "navbar-nav",
]
html_theme_options["navbar_align"] = "left"  # noqa: F405

# Update doc_path for the "Edit on GitHub" link. The DocumenteerGuide preset
# doesn't work here because docs/ doesn't contain the Sphinx conf.py.
html_context["doc_path"] = "docs"  # noqa: F405

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
