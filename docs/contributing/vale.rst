###########################
Editorial linting with Vale
###########################

This project uses Vale_ to lint the prose in the documentation against the :doc:`style-guide` and the `Google Developer Documentation Style Guide`_.
Vale's feedback is *advisory*: it never fails a build or blocks a pull request.
Use it as a checklist of things to look at, not as a gate.

.. _Vale: https://vale.sh
.. _`Google Developer Documentation Style Guide`: https://developers.google.com/style/

What Vale checks
================

Vale runs three sets of rules over the ``.rst`` and ``.md`` files under ``docs/``:

- ``Vale.Spelling`` — spell-checking, using the project vocabulary (see below) for legitimate project and astronomy terms.
- **Google** — the Google Developer Documentation Style Guide package, tuned for this corpus. Some of its rules are demoted to suggestions or disabled where they produce noise; see the comments in ``.vale.ini`` for the rationale behind each adjustment.

.. vale off

- **RSP** — a small set of house rules drawn from the :doc:`style-guide`, such as addressing the reader as "you" rather than "we" and not using "here" as link text.

.. vale on

The configuration lives in ``.vale.ini`` at the repository root, and the RSP rules live in ``styles/RSP/``.

Some paths are excluded because their prose is frozen or provisional: the dated release notes under ``docs/updates/``, the rough drafts in ``docs/guides/inbox/``, and ``docs/roadmap.rst``.

Running Vale locally
====================

Run Vale over the documentation with tox:

.. code-block:: bash

   tox -e vale

This installs Vale and docutils, runs ``vale sync`` to download the Google package into ``styles/`` (which is gitignored), and lints ``docs/``.
A non-zero exit code just means Vale found something to report; it is not an error.

On a pull request, GitHub Actions runs Vale too, and posts any findings on the lines you changed as inline annotations.
That job is always green, even when Vale has findings.

Adding words to the vocabulary
==============================

When Vale flags a legitimate project term, an astronomy term, or a piece of software as a misspelling, add it to the project vocabulary rather than working around it.
The vocabulary is a plain-text file at ``styles/config/vocabularies/RSP/accept.txt``.
Each line is a case-sensitive regular expression; add the term on its own line, grouped under the appropriate comment heading.

Before you accept a word, make sure it is genuinely a term and not a typo.
The `lsst-texmf glossary <https://github.com/lsst/lsst-texmf/blob/main/etc/glossarydefs.csv>`__ is a useful reference for the canonical spelling of Rubin Observatory terms.
If a flagged word is actually a typo, fix it in the source instead of accepting it.

Suppressing false positives
===========================

Occasionally a rule fires on something that is correct in context.
When that happens, you can turn Vale off for a span of source with comments:

.. code-block:: rst

   .. vale off

   This text is not linted by Vale.

   .. vale on

Use this sparingly, and only for genuine false positives — for example, a required verbatim string that happens to trip a rule.
Prefer adding a real term to the vocabulary over switching Vale off, and never use ``.. vale off`` to silence a legitimate style issue that you should fix instead.
