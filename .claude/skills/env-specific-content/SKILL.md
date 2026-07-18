---
name: env-specific-content
description: Write rsp.lsst.io content that differs across RSP environments — rsp-url/rsp-link roles, the rsp-only directive, substitutions, .in.rst includes, and page excludes. Use whenever content mentions an environment URL or varies per environment.
---

# Environment-specific content

rsp.lsst.io is built once per RSP environment (`base`, `idfdev`, `idfint`, `idfprod`, `summit`, `tucson-teststand`, `usdfdev`, `usdfprod`) from a single source tree, with `-W` so warnings are fatal.
`idfprod` is the primary, public edition.
Content that varies across environments must use the project's machinery — **never hard-code an environment hostname or URL**.

This skill is a summary and decision guide.
`docs/contributing/env-specific-docs.rst` is the full treatment (including the complete service-name table, code-sample substitutions, and the `jinja` directive) — **read it for anything beyond what's below.**

## 1. Which mechanism to use

Reach from the most targeted to the most general:

| Situation | Mechanism |
| --- | --- |
| A URL or link to an RSP service | `rsp-url` / `rsp-link` role |
| A URL or link to a **specific dataset's** service (e.g. `dp1`'s TAP endpoint) | `rsp-data-url` / `rsp-data-link` role |
| A link to a dataset's own documentation site | `rsp-dataset-docs` role |
| A table of which datasets expose which data-access services | `rsp-data-table` directive |
| An env-specific word, name, or phrase a role can't produce | substitution (`\|rsp-env\|`, `\|rsp-at\|`, …) |
| A paragraph or section shown only in some environments | `rsp-only` directive |
| A large block of divergent content | `rsp-only` (or `jinja`) + an `*.in.rst` include |
| A whole page absent from some environments | conditionalize the `toctree` entry **and** add the source to `page_excludes.yaml` |

## 2. Usage examples (real patterns from this repo)

### rsp-url / rsp-link roles

Each role takes a service name (e.g. `rsp`, `portal`, `nublado`, `tap`, `webdav`, `times-square`) and resolves it for the environment being built.
`rsp-url` renders the URL as a code literal; `rsp-link` renders a hyperlink.
A path can be appended after the service name.

From `docs/guides/portal/starting-and-stopping/index.rst`:

```rst
From the RSP landing page at :rsp-link:`rsp` click on the left panel for the Portal.
```

From `docs/guides/life/quotas.rst` (explicit link title, and a URL with an appended path):

```rst
Always consult your :rsp-link:`Quotas page <rsp/settings/quotas>` (found under your account settings or directly at :rsp-url:`rsp/settings/quotas`) for limits being currently applied.
```

Targeting a service absent from the environment being built raises a fatal warning — wrap such references in a matching `rsp-only` block (below).

### Dataset-aware roles and the availability table

Discovery describes services *per dataset* too. Three roles and a directive expose that dimension; all resolve against the environment being built.

- `:rsp-data-url:`service dataset`` — a code literal of a dataset's data-access service URL. Service is one of `tap`, `sia`, `cutout`, `datalink`, `hips`; dataset is a name like `dp1`, `dp02`, `dp03`. Example: `:rsp-data-url:`tap dp1``. A path may follow the dataset (`tap dp1/tables`).
- `:rsp-data-link:`service dataset`` — the hyperlink twin, with the usual `title <service dataset>` form.
- `:rsp-dataset-docs:`dataset`` — a link to a dataset's own docs site (discovery's `docs_url`), with a `title <dataset>` form.
- `.. rsp-data-table::` — a table of datasets × data-access services for the current environment, each available cell linking to the endpoint (datasets exposing none of these services are omitted; no datasets at all → no output). Options: `:services:` / `:datasets:` to narrow rows/columns, `:scope: environments` (+ `:service:`) for a datasets × dataset-serving-environments matrix, `:title:` for a caption.

A dataset/service absent in the environment being built (or a dataset with no `docs_url`) raises a fatal warning, so wrap dataset references in an `rsp-only` block. Careful: the per-dataset service names (`sia`, `cutout`, `datalink`, `hips`) are NOT valid `rsp-only` conditions — only `tap` and `api` double as both. Gate on `api` (true wherever the environment serves datasets), `tap`, or environment names, and build the affected environments to confirm the guarded content resolves everywhere the condition holds. The `rsp-data-table` belongs inside `.. rsp-only:: api` so its lead-in prose is dropped where the environment serves no datasets. See `docs/guides/api/api.primary.in.rst` for a real use.

### Substitutions

For env-specific prose a role can't produce, use substitutions defined in `rst_prolog.rst.jinja` (available on every page).
From `docs/guides/life/quotas.rst`:

```rst
As an approved user of the |rsp-at| you have access to certain individual, group, and shared resources.
```

`|rsp-env|` (plain-text display name), `|rsp-env-link|` (linked display name), and `|rsp-at|` (link to this environment's homepage) are the common ones.

Roles and ordinary substitutions don't expand inside literal blocks. For an environment URL inside a code sample, add the `:substitutions:` option and use a substitution like `|rsp-tap-url|`. From `docs/guides/notebooks/faq/index.rst`:

```rst
.. code-block:: bash
   :substitutions:

   export EXTERNAL_TAP_URL="|rsp-tap-url|"
```

### rsp-only directive

Include a block only where its condition holds. Tokens are service names, environment names, or `primary` (= `idfprod`); default is logical AND, with `:any:` for OR and `:not:` to negate.

From `docs/guides/notebooks/faq/index.rst` — a block (and its lead-in prose) shown only where TAP exists:

```rst
.. rsp-only:: tap

   As an example, we will walk through how to access the Rubin LSST TAP service locally.
```

From `docs/guides/recovery/index.rst` — the negated form for "every environment except the primary one":

```rst
.. rsp-only:: primary
   :not:

   To recover a staff account, contact one of the RSP environment's administrators or your manager.
```

### Large divergent block: `*.in.rst` include

To swap a large block per environment, combine `rsp-only` with an `include` of an `*.in.rst` fragment.
The `.in.rst` suffix keeps Sphinx from building the fragment as its own page; name it `<page-stem>.<context>.in.rst`.
From `docs/guides/recovery/index.rst`:

```rst
.. rsp-only:: primary

   .. include:: user-recovery.primary.in.rst
```

(Real fragment: `docs/guides/recovery/user-recovery.primary.in.rst`.)

### Whole page absent from some environments

This is a **two-part** change that must agree on the gating service.

First, conditionalize the `toctree` entry with a `jinja` directive on the service's URL attribute. From `docs/guides/auth/index.rst`:

```rst
.. jinja:: rsp

   .. toctree::
      :titlesonly:

      creating-user-tokens
      token-scopes
      {% if env.api_tap_url %}using-topcat-outside-rsp{% endif %}
```

Second, register the page's source under the matching service token in `src/rspdocs/sphinxext/page_excludes.yaml`, so Sphinx skips it (and doesn't flag it as an orphan) where the service is absent:

```yaml
tap:
  - guides/auth/using-topcat-outside-rsp.rst
```

When excluding an index page that heads a subtree, also exclude the subtree (a `**` glob) so its children don't become orphans.

## 3. Gotchas

- **Never hard-code an environment hostname.** Use a role (or, in code samples, a substitution) so URLs resolve per environment.
- Referencing a service that's absent from the environment being built is a fatal warning — wrap it in a matching `rsp-only` block.
- `page_excludes.yaml` (and `environments.json`) are validated by the `rspdocs-validate-config` pre-commit hook: keys must be recognized service tokens, so a typo fails at commit time.
- An excluded page must not be linked *unconditionally* from a page that builds everywhere — the two-part change (toctree gate + exclude) keeps them in sync.

## 4. Progressive disclosure

This skill covers the common cases only.
For the full service-name table, code-sample substitutions, the `jinja` directive for *computed* (not just shown/hidden) text, and the details of page excludes, **read `docs/contributing/env-specific-docs.rst`.**

## 5. Verify

Environment-specific mistakes often only show up in the environment they affect, so build at least two environments with differing behavior — the primary plus one where the relevant service is absent:

```bash
tox -e sphinx-idfprod
tox -e sphinx-base
```

(If `tox` is not on `PATH`, use `uvx tox -e …`.)
Both must be green; read the output for warnings, not just the exit status.
