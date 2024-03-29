###############################################
Setting up pre-commit hooks to format notebooks
###############################################

Pre-commit hooks are a great way to ensure that your notebooks are formatted consistently, and are therefore easier for your team to collaborate on.
Pre-commit hooks are also great for stripping outputs from notebooks, which makes them smaller in a GitHub repository.

Adding a Pre-commit configuration file
======================================

To set up Pre-commit, you need to add a :file:`.pre-commit-config.yaml` file to the root of your repository. This file contains the configuration for the pre-commit hooks that run whenever a contributor makes a Git commit in the repository.

This file is a good starting point:

.. code-block:: yaml
   :caption: .pre-commit-config.yaml

   repos:
     - repo: https://github.com/kynan/nbstripout
       rev: 0.6.1
       hooks:
         - id: nbstripout

The nbstripout_ hook removes the outputs from Jupyter notebooks, which can make the diffs for the notebooks much easier to review and reduces the storage size of the repository.

More hooks to consider
----------------------

- black_nbconvert_ will reformat your notebooks with `black`_.

Document how to install Pre-commit
==================================

To help make sure your contributors use Pre-commit, you should add a section to your README.md files that explains how to install pre-commit:

.. code-block:: markdown
   :caption: README.md

   ## Development

   This repository uses Pre-commit to keep notebooks formatted and clean. Install Pre-commit by running:

   ```bash
   pip install pre-commit
   pre-commit install
   ```

Another common approach is to add a Makefile to the repository that includes a target to initialize a repository:

.. code-block:: makefile
   :caption: Makefile

   .PHONY: init
   init:
       pip install pre-commit
       pre-commit install

Then mention this Makefile target in the README:

.. code-block:: markdown
   :caption: README.md

   ## Development

   This repository uses Pre-commit to keep notebooks formatted and clean. Install Pre-commit by running:

   ```bash
   make init
   ```

Run Pre-commit in a GitHub Actions workflow
===========================================

Sometimes a contributor will forget to install Pre-commit.
To catch this, you can run Pre-commit in a GitHub Actions workflow:

.. code-block:: yaml
   :caption: .github/workflows/ci.yaml

   name: CI

   "on":
     merge_group: {}
     pull_request: {}
     push: {}

   jobs:
     lint:
       runs-on: ubuntu-latest
       timeout-minutes: 5

       steps:
         - uses: actions/checkout@v4

         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: "3.12"

         - name: Run pre-commit
           uses: pre-commit/action@v3.0.0

Save this file to the :file:`.github/workflows` directory in your repository.

Another option is to the the `Pre-commit.com CI service <https://pre-commit.com>`__ to run pre-commit hooks on pull requests.

Require Pre-commit to pass
==========================

You can require that pre-commit, either through a GitHub Actions workflow or through pre-commit.com, passes before a pull request can merge.
This is done by adding the status check to the default branch's protection settings.
See :doc:`branch-protections-howto` for more information.
