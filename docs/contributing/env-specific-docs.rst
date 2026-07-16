##########################################
Writing environment-specific documentation
##########################################

There are multiple science platforms deployed in different locations for different purposes.
Each science platform instance is a separate `Phalanx environment <https://phalanx.lsst.io/environments/index.html>`__.
A separate version of this documentation is built for each science platform environment and deployed using LSST the Docs's editions feature.
The documentation corresponding to the primary, public-facing science platform is always deployed as the main edition at the root URL (https://rsp.lsst.io).
Other editions are available from https://rsp.lsst.io/v and the Science Platform homepages of each environment also link directly to these editions.

Information about the RSP environments is fetched at build time from the per-environment `Repertoire <https://repertoire.lsst.io/>`__ service-discovery data that Phalanx publishes at ``https://phalanx.lsst.io/discovery/environments/{env}.json``.
A small supplementary shim in the `documentation repository <https://github.com/lsst/rsp_lsst_io>`_ (:file:`src/rspdocs/discovery/environments.json`) provides the handful of things discovery doesn't cover, such as human-readable environment titles and the roster of environments to build.
When the network is unavailable, the build falls back to a local cache (in :file:`_build/discovery/`) and announces the fallback in the build output.

This page describes the supported approaches for writing documentation that differs between environments.
Reach for them in this order, from the most targeted to the most general:

- :ref:`envdocs-roles` for inline URLs and links to RSP services.
- :ref:`envdocs-substitutions` for env-specific words and short phrases that a role can't produce.
- :ref:`envdocs-conditional` to include or exclude whole blocks of content per environment.
- :ref:`envdocs-jinja` when a branch's text must be *computed* from environment data (interpolation, loops, or expressions).
- :ref:`envdocs-jinja-includes` to swap large included files.

The roles and the ``rsp-only`` directive are provided by the in-repo :file:`src/rspdocs/sphinxext` Sphinx extension.
The homepage (:file:`docs/index.rst`) and log-in (:file:`docs/guides/getting-started/get-an-account.rst`) pages demonstrate these techniques.

.. _envdocs-roles:

Linking to RSP services with roles
==================================

For an inline link or URL to an RSP service, use one of these two roles.
Each takes a service name — listed in the table below — and resolves it to that service's URL for the environment being built.

``rsp-url``
    ``:rsp-url:`service``` renders the service's URL as a code literal.
    For example, ``:rsp-url:`rsp``` renders as :rsp-url:`rsp`.

``rsp-link``
    ``:rsp-link:`service``` renders a hyperlink to the service whose link text is the URL itself.
    For example, ``:rsp-link:`rsp``` renders as :rsp-link:`rsp`.

    Give an explicit link title with the familiar ``title <target>`` syntax: ``:rsp-link:`Rubin Science Platform <rsp>``` renders as :rsp-link:`Rubin Science Platform <rsp>`.

Some services aren't deployed in every environment; targeting a service that is absent in the environment being built raises a warning (fatal under ``-W``), which usually means the reference should be wrapped in a matching :ref:`rsp-only <envdocs-conditional>` block.

.. list-table:: Service names
   :header-rows: 1

   * - Name
     - Service
     - In every environment?
   * - ``rsp``, ``squareone``
     - RSP homepage
     - yes
   * - ``portal``
     - Portal Aspect
     - no
   * - ``nublado``, ``nb``
     - Notebook Aspect
     - no
   * - ``api``
     - VO API root
     - no
   * - ``tap``
     - TAP service
     - no
   * - ``webdav``
     - WebDAV service
     - no
   * - ``times-square``
     - Times Square
     - no
   * - ``tokens``
     - Access-token page
     - yes
   * - ``phalanx-docs``
     - Phalanx environment docs
     - yes

.. _envdocs-substitutions:

Using reStructuredText substitutions
====================================

For env-specific *prose* — a word, a name, or a derived path that a role can't produce — use `reStructuredText substitutions <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#substitutions>`__.
These substitutions are defined in :file:`rst_epilog.rst.jinja`, which is itself templated with Jinja so the replacement text can vary by environment.

.. list-table:: Available substitutions
   :header-rows: 1

   * - Syntax
     - Example
   * - ``|rsp-at|``
     - |rsp-at|
   * - ``|rsp-env|``
     - |rsp-env|
   * - ``|rsp-env-link|``
     - |rsp-env-link|
   * - ``|rsp-quotas-url|``
     - |rsp-quotas-url|
   * - ``|rsp-quotas-page|``
     - |rsp-quotas-page|
   * - ``|webdav-server|``
     - |webdav-server|

Prefer a :ref:`role <envdocs-roles>` whenever you only need a service's URL or a link to it — the roles replaced the per-service URL and link substitutions the docs used to define.

.. _envdocs-conditional:

Conditional content with the ``rsp-only`` directive
===================================================

To include a block of content only in certain environments, wrap it in the ``rsp-only`` directive:

.. code-block:: rst

   .. rsp-only:: primary

      This content appears only in the primary (public) build.

The directive takes one or more bare *condition tokens*, which may be:

- a **service name** (from the table above) — true where that service is deployed;
- an **environment name** (``base``, ``idfdev``, ``idfint``, ``idfprod``, ``summit``, ``tucson-teststand``, ``usdfdev``, ``usdfprod``) — true only in that environment; or
- the keyword ``primary`` — synonymous with ``idfprod``, the primary environment, whose documentation is the default edition.

By default every token must hold (logical AND):

.. code-block:: rst

   .. rsp-only:: portal nublado

      This content appears only where both the Portal and Notebook aspects exist.

Use the ``:any:`` option for a logical OR, and the ``:not:`` option to negate the result:

.. code-block:: rst

   .. rsp-only:: summit base
      :any:

      This content appears in the summit or base environments.

   .. rsp-only:: primary
      :not:

      This content appears in every environment except the primary one.

For an "AND of an OR" condition, nest ``rsp-only`` directives.

Unlike Sphinx's built-in `only <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-only>`__ directive, ``rsp-only`` excludes non-matching content at parse time: excluded content never enters the doctree, so it can't leak into the table of contents, the index, or search results.
This is safe here because each environment is built separately (one ``sphinx-build`` per environment), so ``rsp-only`` is the right tool for conditional content — there's no need to avoid it the way you would avoid ``only``.

.. _envdocs-jinja:

Using Jinja templating
======================

The ``rsp-only`` directive only *includes or excludes* static reStructuredText.
Reach for the ``jinja`` directive — available through sphinx-jinja_ — when a branch's text has to be *computed* rather than merely shown or hidden: interpolating an expression like ``{{ env.title }}``, running a loop, or testing an ``env`` attribute that isn't a service name, an environment name, or ``primary``.

The deciding question is not how many branches you have, but whether the prose inside a branch depends on a value — and one that no ``rsp-url``/``rsp-link`` role or substitution already provides.
If every branch is self-contained rST, prefer stacking :ref:`rsp-only <envdocs-conditional>` blocks; use ``jinja`` only when a branch needs to *say something* built from the environment's data.

For example, a three-way switch whose branches are worded differently *and* each interpolates an environment value that has no substitution of its own (here the short title ``env.title`` and the ``env.domain`` host):

.. code-block:: rst

   .. jinja:: rsp

      {% if env.is_primary %}
      The public Science Platform is served at {{ env.domain }}.

      {% elif env.name in ("idfint", "idfdev") %}
      {{ env.title }} is a staff integration environment.

      {% else %}
      {{ env.title }} runs at {{ env.domain }} for internal use.
      {% endif %}

The argument to the ``jinja`` directive is always ``rsp``.
Inside it, ``env`` is the environment being built (an instance of ``rspdocs.discovery.models.PhalanxEnv``, so any of its attributes are available), and ``all_envs`` maps environment names to their ``PhalanxEnv``.
As with any Sphinx directive, indent the content consistently with respect to the directive's scope, as shown above.

Two things to keep in mind:

- For a simple two-way include/exclude, prefer :ref:`envdocs-conditional`: it reads more clearly and keeps excluded content out of search and the table of contents.
- Each build fetches only the target environment and the primary environment (for speed), so ``all_envs`` holds just those one or two entries — a ``{% for %}`` loop over it will **not** enumerate all eight environments.

.. _envdocs-jinja-includes:

Using source file includes (\*.in.rst) with rsp-only and jinja
==============================================================

Both the ``rsp-only`` and ``jinja`` approaches work well for tailoring specific paragraphs for different environments, but writing a large amount of content inside a directive is inconvenient.
To customize large portions of text, you can combine the ``rsp-only`` directive (or a ``jinja`` directive for multi-way switches) with the ``include`` directive:

.. code-block:: rst

   .. rsp-only:: primary

      .. include:: the-page.primary.in.rst

   .. rsp-only:: primary
      :not:

      .. include:: the-page.notprimary.in.rst

This inserts content from the included source files, either ``the-page.primary.in.rst`` or ``the-page.notprimary.in.rst``.
Those included files are in the familiar reStructuredText syntax (you shouldn't need further Jinja syntax within them, though you can certainly use :ref:`roles <envdocs-roles>` and :ref:`substitutions <envdocs-substitutions>`).

The included files **must** have a ``.in.rst`` suffix so that the Sphinx build won't incorporate those files as separate pages.
Our further convention is to prefix the name with the root name of the page, followed by a description of the environment or context where the content applies.
