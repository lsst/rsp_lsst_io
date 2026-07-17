---
name: new-page
description: Scaffold a new documentation page for rsp.lsst.io — file placement, reStructuredText skeleton, heading style, and toctree registration. Use when adding a new page or section to the docs.
---

# Scaffold a new documentation page

Use this playbook to add a new page to rsp.lsst.io.
The docs are Sphinx reStructuredText under `docs/`, built once per RSP environment with `-W` (warnings are fatal).
Full editorial rules live in `docs/contributing/style-guide.rst` — this skill is the quick procedure, not a replacement for it.

## 1. Choose the location and file name

Pick the section under `docs/` that fits the content:

- `docs/guides/` — the bulk of user documentation (getting-started, notebooks, portal, API, auth, WebDAV, Times Square, recovery, life-of-an-account). New user-facing content almost always belongs here.
- `docs/contributing/` — how to write and build the docs.
- `docs/support/` — how users get help.
- `docs/updates/` — release/update notes.

File-name rules:

- Lowercase, with hyphens between words. Never underscores or spaces (e.g. `starting-and-stopping`, not `starting_and_stopping`).
- A page **with images** (or that heads a subsection) lives in its own directory as `index.rst`, with images in a sibling `images/` directory — e.g. `docs/guides/notebooks/starting-and-stopping/index.rst` and `docs/guides/notebooks/starting-and-stopping/images/`.
- A simple single-file page can live directly in the section — e.g. `docs/guides/life/quotas.rst`.

Inspect the neighboring pages in the section you chose and match their layout.

## 2. Write the reStructuredText skeleton

Match the heading-underline convention used across this repo (inspect a neighbor to confirm):

- Top-level page title: `#` characters as an **overline and underline**, both at least as long as the title.
- Section headings: `=` underline.
- Subsection headings: `-` underline.

Use **sentence case** for the title and all headings (capitalize only the first word and proper nouns).
Use **semantic line breaks**: one sentence (or clause) per source line — never hard-wrap to a fixed column.

Skeleton to adapt:

```rst
#########################
Start and stop a server
#########################

From the RSP landing page, click on the central panel for Notebooks.
This paragraph uses one sentence per source line.

Select a server size
====================

Text for the first section.

A narrower detail
-----------------

Text for a subsection.
```

Try not to exceed two levels of heading hierarchy below the title (see the style guide).

## 3. Register the page in the parent toctree

**A page that no `toctree` links to fails the `-W` build** with `document isn't included in any toctree` (an "orphan").
After creating the page, add its name (without the `.rst` extension, or the directory name for an `index.rst` page) to the `toctree` of the parent `index.rst`.

For example, `docs/guides/getting-started/index.rst` registers pages like this:

```rst
.. toctree::
   :caption: Account set up
   :titlesonly:

   get-an-account
   linking-more-ids
```

Add your new page's stem on its own line inside the appropriate `toctree`.
For a page in its own directory, register the directory-relative path to its index, e.g. `starting-and-stopping/index`.

## 4. Style reminders

- Address the reader as **"you"**, never **"we"** (name "Rubin Observatory" if that's what's meant).
- **Never use "here" as link text** — make the relevant noun or phrase the link.
- Write in the active voice and present tense; short sentences and paragraphs.

These are the essentials only. Read `docs/contributing/style-guide.rst` for the full guidance before writing substantial prose.

## 5. Environment-specific content

If the page's content varies across RSP environments — it mentions an RSP service URL, differs by environment, or should be dropped from some environments — **use the `env-specific-content` skill**.
Never hard-code an environment hostname; the env-specific machinery (roles, substitutions, `rsp-only`, includes, page excludes) resolves it per environment.

## 6. Verify

Build the primary environment and read the output for warnings, not just the exit status:

```bash
tox -e sphinx-idfprod
```

(If `tox` is not on `PATH`, use `uvx tox -e sphinx-idfprod`.)
The build must be green — a fatal warning here usually means an unregistered page (step 3) or a broken cross-reference.
If the page has environment-varying content, also build a non-primary environment (see the `env-specific-content` skill).
