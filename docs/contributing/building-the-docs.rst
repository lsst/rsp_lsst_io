#########################
Building the docs locally
#########################

Setting up the development environment
======================================

These are the basic steps to clone and build the docs:

.. code-block:: bash

   git clone https://github.com/lsst/rsp_lsst_io
   cd rsp_lsst_io

Next, create a Python virtual environment (with venv_, for example).

Once you’ve done that, initialize the development environment:

.. code-block:: bash

   make init

This command installs tox_ and pre-commit_ hooks.
Tox enables you to build customized documentation sites for each RSP environment from a single source repository.
A consequence of using tox is that you don't install and run Sphinx directly; instead, tox handles build dependencies through its own Python virtual environments.
If you ever need to refresh those virtual environments — perhaps because you've updated your branch and the up-stream dependencies changed — you can re-initialize the environment by running ``make init`` in your shell again.

Running a documentation build
=============================

Build documentation for all RSP environments by running tox:

.. code-block:: bash

   tox

By default, the tox command generates documentation site builds for each RSP environment in the ``_builds/html`` directory.
For example, ``_builds/html/idfprod/index.html`` is the homepage for the production IDF deployment and ``_builds/html/summit/index.html`` is the homepage for the summit deployment.

To build documentation for a limited number of environments, supply environment names to tox's ``-e`` option:

.. code-block:: bash

   tox -e sphinx-idfprod,sphinx-summit

To see a list of all available environments:

.. code-block:: bash

   tox -a

Although GitHub Actions performs link checks automatically for you, you can manually check links:

.. code-block:: bash

   tox -e linkcheck-idfprod

To force a complete rebuild of the documentation, you can clean-up the existing builds:

.. code-block:: bash

   make clean

Git commit hooks
================

To ensure that code quality is consistent, this project uses pre-commit_ hooks to lint the source repository before every commit.
These hooks are also in GitHub Actions, however, for the best development experience you will want to run these hooks during development.
By running ``make init``, these hooks are installed in your local repository clone.

If the hooks "fail," you will need to correct and re-add (``git add``) your changes before running ``git commit`` again.
Some hooks auto-correct the source, in which case you only need to re-add the changes.
