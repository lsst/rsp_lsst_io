####################################################
Configure the shell environment for notebook kernels
####################################################

While the terminal_ in the Notebook Aspect sources :file:`~/.bashrc`, Jupyter Notebook kernels do not.
Instead, you can configure the environment for Jupyter notebooks with the :file:`~/notebooks/.user_setups` file.
With this file, you can set up environment variables and even set up LSST Science Pipelines packages, for your Jupyter notebooks.

.. _user-setups-envvars:

Export environment variables for notebooks
==========================================

The :file:`~/notebooks/.user_setups` file is sourced by bash.
This means you can include any valid bash syntax.

For example, you can define environment variables that are accessible from notebooks:

.. code-block:: bash

   export MYVAR="My env var"

.. note::

   Environment variables exported from :doc:`~/.bashrc <shell-configuration>` **are not** accessible from notebooks.
   You need to export those variables from :file:`~/notebooks/.user_setups` instead.

Customizing the EUPS package set up
===================================

The main use for :file:`~/notebooks/.user_setups` is setting up a package that you’ve locally cloned and built.
See :ref:`lsst-kernel-user-setups` for an example.

.. _user-setups-restart:

Updating ~/notebooks/.user_setups for a running notebook kernel
===============================================================

If you need to change package setups or environment variables for an already-opened notebook, follow these steps:

1. Edit and save the :file:`~/notebooks/.user_setups` file.

2. Return to your notebook's tab and restart the kernel (**Kernel** → **Restart Kernel**).

You'll need to rerun your notebook's cells after restarting the kernel.

.. _verify-user-setups:

Tip: source ~/notebooks/.user_setups to verify it
=================================================

Since :file:`~/notebooks/.user_setups` is a bash script, it's sensitive to syntax errors.
You won't be alerted to syntax errors when you start a new notebook kernel, though.

The best way to check that your :file:`~/notebooks/.user_setups` file is correct is by sourcing it from a `terminal`_:

.. code-block:: bash

   source ~/notebooks/.user_setups

.. note::

   If :file:`~/notebooks/.user_setups` includes a :command:`setup` command, ensure that you have :doc:`set up the LSST environment <../science-pipelines/science-pipelines-in-terminal>` in the terminal first.
