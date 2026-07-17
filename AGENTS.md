# Agent briefing for rsp_lsst_io

This repo builds **rsp.lsst.io**, the Rubin Science Platform (RSP) user documentation.
It is a Sphinx project (built with [documenteer](https://documenteer.lsst.io/)) plus a small in-repo Python package, `rspdocs`, that supplies custom Sphinx machinery.

The site is **built once per RSP environment** — `base`, `idfdev`, `idfint`, `idfprod`, `summit`, `tucson-teststand`, `usdfdev`, `usdfprod` — from a single source tree.
`idfprod` is the primary, public-facing edition served at the root URL; the others are published as separate editions.
Because content can differ across environments, authoring often uses the environment-specific machinery described below.

## Repository layout

- `docs/` — the reStructuredText source for the site. Sections:
  - `docs/guides/` — the bulk of the user documentation.
    Subsections include getting-started, notebooks, portal, API and auth,
    WebDAV, Times Square, recovery, and life-of-an-account material.
    New user-facing content almost always belongs somewhere under here.
  - `docs/contributing/` — how to write and build these docs.
    **Read the relevant page here before writing or restructuring content** (see below).
  - `docs/support/` — how users get help.
  - `docs/updates/` — release/update notes.
  - `docs/roadmap.rst`, `docs/index.rst` — roadmap and homepage.
- `src/rspdocs/` — the in-repo Python package that powers the custom build:
  - `sphinxext/` — the Sphinx extension providing the `rsp-url`/`rsp-link` roles,
    the `rsp-only` directive, and page-exclude logic (`page_excludes.yaml`).
  - `discovery/` — fetches per-environment service-discovery data at build time
    and supplies the environment roster and titles (`environments.json`).
  - `validate.py` — the `rspdocs-validate-config` command that checks the
    hand-edited config files (`page_excludes.yaml`, `environments.json`).
    It runs automatically under pre-commit and the test suite.
- `tests/` — the pytest suite for `rspdocs` (discovery, sphinxext, config validation).
- Sphinx configuration lives at the repo root: `conf.py`, `documenteer.toml`, and `rst_prolog.rst.jinja` (the Jinja-templated substitution prolog).

## Commands

`tox` drives everything; you don't invoke Sphinx or pytest directly.

- `make init` — first-time setup: installs `tox` + `pre-commit` and the editable package. Skip it if the environment is already set up.
- `tox -e sphinx-idfprod` — build the docs for the primary environment.
  Substitute any other environment for a different edition: `tox -e sphinx-base`, `tox -e sphinx-summit`, `tox -e sphinx-usdfdev`, etc. (one `sphinx-{env}` env per environment listed above). Bare `tox` builds lint plus all environments.
- `tox -e py` — run the pytest suite.
- `tox -e typing` — run mypy over `src/rspdocs` and `tests`.
- `tox -e lint` — run all pre-commit hooks over the tree.
- `tox -e vale` — run the [Vale](https://vale.sh) editorial linter (Google + RSP styles) over `docs/`. Findings are **advisory**: they never fail CI (a non-zero exit just means Vale had something to report), there is no pre-commit hook, and on pull requests the CI annotations are non-blocking. See `docs/contributing/vale.rst`. Accept legitimate terms in `styles/config/vocabularies/RSP/accept.txt`; fix real typos in the source.
- `tox -e linkcheck-idfprod` — check external links for that environment (a `linkcheck-{env}` exists per environment).

**Builds run under `-W`, so every Sphinx warning is fatal.**
A change that "renders fine" but emits a warning — a broken cross-reference,
an orphaned page, or a role targeting a service that isn't in the environment
being built — will **fail CI**.
Always run a build before concluding a docs change is done, and read the build
output for warnings, not just the final exit status.
When in doubt, build more than one environment (for example `idfprod` plus one
non-primary environment), since environment-specific mistakes often only show
up in the environment they affect.

## Top style rules

Full editorial guidance is in `docs/contributing/style-guide.rst`; it defers to the [Google Developer Documentation Style Guide](https://developers.google.com/style/) for anything it doesn't cover. The essentials:

- **Semantic line breaks** — one sentence (or clause) per source line; never hard-wrap to a fixed column.
- **Sentence case** for headings, not title case.
- **Lowercase, hyphen-separated file names** — no underscores or spaces. File and directory names under `docs/` are enforced by `rspdocs-lint-paths` (runs in pre-commit / `tox -e lint`), which also blocks committed `.DS_Store` files.
- Address the reader as **"you"**, never **"we"** (name "Rubin Observatory" if that's what's meant).
- **Never use "here" as link text** — make the relevant noun or phrase the link.

## Environment-specific authoring

Content that differs across RSP environments must use the project's machinery rather than hard-coded values.
`docs/contributing/env-specific-docs.rst` is the full treatment; **read it before writing environment-varying content.** In brief, reaching from most targeted to most general:

- **`rsp-url` / `rsp-link` roles** — resolve a named RSP service (e.g. `rsp`,
  `portal`, `nublado`, `tap`) to its URL (or a hyperlink) for the environment
  being built, optionally with a path appended. Use these for any RSP service URL.
- **Substitutions** (e.g. `|rsp-env|`, `|rsp-at|`) — env-specific words/phrases, defined in `rst_prolog.rst.jinja`. Code samples need the `:substitutions:` option to expand them.
- **`rsp-only` directive** — include/exclude a block of content by environment or by service presence.
- **`jinja` directive** — when a branch's text must be *computed* from environment data, not just shown or hidden.
- **`*.in.rst` / `*.primary.in.rst` includes** — swap large included fragments per environment; the `.in.rst` suffix keeps Sphinx from building them as standalone pages.
- **`page_excludes.yaml`** (`src/rspdocs/sphinxext/`) — leave a whole page out of environments where its service is absent.

Biggest gotchas:

- **Don't hard-code an environment URL.** Use an `rsp-url`/`rsp-link` role (or a substitution in code samples) so it resolves correctly per environment.
- **Referencing a service absent from the environment raises a warning** — fatal under `-W`. Wrap such content in a matching `rsp-only` block.
- **Dropping a page from an environment is a two-part change**: conditionalize its `toctree` entry *and* register the source in `page_excludes.yaml`. Miss the second and Sphinx flags an orphan (fatal under `-W`).

## Before you write

Read the relevant page(s) under `docs/contributing/` before writing or restructuring content — `style-guide.rst` for conventions, `env-specific-docs.rst` for anything that varies by environment, and `building-the-docs.rst` for the build workflow. These are the source of truth; this file only points at them.

## Repo skills

This repo ships agent skills — step-by-step playbooks for common tasks — under `.claude/skills/` (mirrored at `.agents/skills` for non-Claude harnesses). Load the matching skill when you start one of these tasks:

- **`new-page`** — scaffolding a new documentation page: file placement, the reStructuredText skeleton, heading style, and toctree registration. Use when adding a new page or section.
- **`env-specific-content`** — writing content that differs across RSP environments: the `rsp-url`/`rsp-link` roles, the `rsp-only` directive, substitutions, `*.in.rst` includes, and page excludes. Use whenever content mentions an environment URL or varies per environment.

## Branch convention

Work on a branch named `tickets/DM-XXXXX`, using the Jira ticket key for the work.
For small-scale work with no Jira ticket, use `u/<github-username>/<description>` instead.
