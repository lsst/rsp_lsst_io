##############################################
Making a notebook compatible with Times Square
##############################################

Times Square uses Jupyter Notebooks (``ipynb`` files) that you'll be familiar with if you use the :doc:`Notebook Aspect <../../notebooks/index>` of the Rubin Science Platform.
There are some caveats and requirements to keep in mind, however, for your notebook to run successfully with Times Square.

.. _ts-reqs-parameters-cell:

Reserve the first code cell for setting parameter defaults
==========================================================

Reserve the first **code** cell in your notebook for setting parameter defaults.
When Times Square runs your notebook, it replaces that first code cell with new code that assigns parameter variables to values set by the user.

As an author, the variable assignments in the first code cell are what you use when interactively editing the notebook.
It often makes sense for these values to match the defaults you set in the :doc:`notebook's YAML sidecar file <sidecar-schema>`.

Even if you don't have any parameters in your notebook, you must still reserve the first code cell for this purpose.
You might include a comment in the cell to explain that it's reserved for parameter defaults.

.. _ts-reqs-git-repo-referencing:

Notebooks can't reference data or code in the Git repository
============================================================

Times Square notebooks are maintained in GitHub repositories.
Don't include any data files or Python modules in the repository that are needed for the notebook to run.
When Times Square runs a notebook, only the ``ipynb`` file is sent to the JupyterLab server.
Any relative imports of Python modules or reads of Git repository data files will fail.

If you want to import Python modules, functions or classes into your notebook, you'll need to do so from a package that's installed on the Rubin Science Platform.
If that code isn't available in an installed package yet, you might need to temporarily vendor (copy) it into your notebook.

If you need to read data into your notebook, you'll normally use Science Platform APIs or the Butler to do so.
If the data is very small, you might even embed it into the notebook itself.
Another option is to save the data file to a shared directory on the file storage.
Any user on the Science Platform must be able to read the file, so make sure the file permissions are set appropriately (notebooks are executed from "bot" accounts, not your own user account).

.. _ts-reqs-user-home-referencing:

Notebooks can't reference files or code installed in a specific user's home directory
=====================================================================================

When Times Square runs a notebook, it's executed from a "bot" account, not a specific user account (or your own user account).
Any Python modules that the notebook imports must be pre-installed for all users on the Science Platform.
Similarly, any data files must be accessible from shared file storage accessible to any user on the Science Platform.

.. _ts-reqs-external-side-effects:

Avoid external side-effects when a notebook runs
================================================

Times Square notebooks shouldn't make changes to external systems when they run.
Examples of things to avoid:

- Sending emails or Slack messages
- Writing to a database
- Triggering another computation
- Commanding a telescope

.. _ts-reqs-idempotent:

Notebooks should be idempotent
==============================

Times Square notebooks can be executed multiple times, with different parameter values, and at different times.
For best results, notebooks should be idempotent: they should produce the same output every time they're run, even if they're run multiple times.
This follows the advice that notebooks should avoid external side-effects.

An exception to this rule is a notebook that runs against an incomplete dataset (for example, a night observing report that's generated at midnight).
Times Square will provide ways to cache-bust incomplete notebooks so that they can be re-run when the data are available.
