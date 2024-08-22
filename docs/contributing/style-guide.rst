#########################
Documentation style guide
#########################

This documentation is written primarily in reStructuredText.
The `Rubin reStructuredText style guide <https://developer.lsst.io/restructuredtext/style.html>`__ can help you create effective reStructuredText.

Style and voice
===============

This is user documentation, which is different from academic writing.
Here are some tips:

- Make sure that all of your writing is in the service of users.

- Write with the active voice and in the present tense as much as possible.

- Address the user directly (“you can…”).
  Never use “we” since that’s ambiguous.
  If “we” means “Rubin Observatory,” then name “Rubin Observatory.”
  If “we” means the user, then say “you.”
  Even in tutorials, don’t use “we” to refer to an imaginary writer assisting the user.

- Write simply, with short sentences and short paragraphs.
  Chunk information with headers.

- Write confidently and precisely, yet also casually.
  Contractions are good.

For further discussion about specific style issues, refer to the `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_.

File names
==========

Always use hyphens to separate words in file names.
Don’t use underscores or spaces.

Prose formatting in plain text
==============================

DM's user documentation is written with soft wrapping, meaning that lines are as long as they need to be in the plain text file and the text editor is expected to handle wrapping.
Never hard wrap to an arbitrary line length.
Soft wrapping makes editing more approachable for more people (particularly those using the GitHub editor) and makes pull request line comments more useful.

More specifically, use `semantic line formatting <https://rhodesmill.org/brandon/2012/one-sentence-per-line/>`__.
Generally this means that each sentence should be its own line in the text file.

Titles and headings
===================

Use sentence case for headings (don’t use title case).
Capitalize proper nouns as usual.

Try not to use more than two levels of heading hierarchy.
Using more than two levels of hierarchy might suggest an information architecture issue.

Also keep in mind DM’s `reStructuredText heading styles <https://developer.lsst.io/restructuredtext/style.html#sections>`__.

Links
=====

Never use "here" as link text.
Instead, make the relevant noun or phrase the link.

Environment-specific documentation
==================================

If the content is specific to an RSP environment, or is different across RSP environments, use the project's tools to write environment-specific content.
See :doc:`env-specific-docs`.
