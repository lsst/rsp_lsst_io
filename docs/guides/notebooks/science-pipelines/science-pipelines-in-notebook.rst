Using the LSST Science Pipelines in notebooks (LSST kernel)
###########################################################

The LSST Jupyter kernel includes the `LSST Science Pipelines`_, making it a convenient way to work with LSST’s software.
The version of the LSST Science Pipelines that’s preinstalled corresponds to the image you selected at log in .

This page describes how to :ref:`use the LSST kernel <lsst-kernel-create>` and configure EUPS package set ups and environment variables with the :ref:`~/notebooks/.user_setups <lsst-kernel-user-setups>` configuration file.

.. seealso::

   :doc:`science-pipelines-in-terminal`.

.. _lsst-kernel-create:

Create a new notebook with the LSST kernel
==========================================

1. From the `file browser`_, click the **+** button (or type :kbd:`command`\ -\ :kbd:`shift`\ -\ :kbd:`L`) to open the launcher.
2. Under the **Notebook** heading, click on the **LSST** icon.

Now the LSST Science Pipelines are available for you to import and use.
For example, in a notebook cell, import ``lsst.afw`` and check the version:

.. code-block:: python

   from lsst import afw

   afw.version.__version__

With the LSST kernel you don’t run the ``setup lsst_distrib`` command that is needed for command-line usage. The LSST kernel does this for you. You can still customize how packages are set up, see :ref:`lsst-kernel-user-setups`.

.. seealso::

   The `JupyterLab Notebooks documentation`_ has more information on creating and using notebooks.

.. _lsst-kernel-switch:

Switch an opened notebook to the LSST kernel
============================================

You can open existing notebooks by double clicking on their icons in the JupyterLab `file browser`_.
JupyterLab automatically opens notebooks in the same kernel that they were created with.
If you’re opening a notebook that wasn’t created in the Notebook Aspect, you may need to switch the kernel to LSST:

1. Look for the kernel name in the notebook’s upper right menu bar. It should read **LSST**. If it is **Python 3** (the default kernel) you’ll need to switch it.
2. Click on the kernel name and select **LSST** from the menu.

.. _lsst-kernel-user-setups:

Customizing the EUPS package setup (~/notebooks/.user_setups)
=============================================================

When the LSST kernel starts up, it activates the LSST environment and sets up ``lsst_distrib`` (the top-level EUPS package of the `LSST Science Pipelines`_).
You can customize what packages are set up by creating and editing a :file:`~/notebooks/.user_setups` file (see :doc:`../configuration/notebook-user-setups`).

The main use for :file:`~/notebooks/.user_setups` is setting up a package that you’ve locally cloned and built.
For example, if your package is the ``~/notebooks/my_package`` directory, add this line to ``~/notebooks/.user_setups``:

.. code-block:: bash

   setup -k -r ~/notebooks/my_package

.. note::

   You need to compile an LSST Science Pipelines package first with :command:`scons` before using it.
   See: :doc:`science-pipelines-development`.

For more information about working with the :file:`~/notebooks/.user-setups` file, see :doc:`../configuration/notebook-user-setups`.

.. _`LSST Science Pipelines`: https://pipelines.lsst.io
.. _`file browser`: https://jupyterlab.readthedocs.io/en/latest/user/files.html
.. _`terminal`: https://jupyterlab.readthedocs.io/en/latest/user/terminal.html
.. _`JupyterLab Notebooks documentation`: https://jupyterlab.readthedocs.io/en/latest/user/notebook.html
