################################################
Using the LSST Science Pipelines in the terminal
################################################

The Notebook Aspect includes the `LSST Science Pipelines`_, making it a convenient way to work with LSST’s software.
The version of the LSST Science Pipelines that’s preinstalled corresponds to the image you selected when launching a notebook session.

This page describes how to use the LSST Science Pipelines from the `JupyterLab terminal`_.
If you're working from a Jupyter notebook, see also :doc:`science-pipelines-in-notebook`.

Setting up the LSST Science Pipelines
=====================================

1. Open a `terminal`_.
   Click the :guilabel:`+` button in the `file browser`_ (or type :kbd:`command`\ -\ :kbd:`shift`\ -\ :kbd:`L`) and then click the :guilabel:`Terminal` icon.

2. Set up LSST Science Pipelines packages:

   .. code-block:: bash

      setup lsst_distrib

Now you can run LSST Science Pipelines commands.
For example:

.. code-block:: bash

   pipetask -h

See `Setting up installed LSST Science Pipelines`_ in the LSST Science Pipelines documentation for more information about EUPS and the :command:`setup` command.

.. _`Setting up installed LSST Science Pipelines`: https://pipelines.lsst.io/install/setup.html
