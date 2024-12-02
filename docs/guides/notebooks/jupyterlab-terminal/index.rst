#############################
Using the JupyterLab Terminal
#############################

.. _NB-Intro-Use-A-JL-terminal:

How to use the JupyterLab terminal
==================================

The Rubin/LSST data products and the `LSST Science Pipelines`_ tools can both be accessed from the command line of a JupyterLab terminal tab.
A terminal session can be started by clicking on the terminal icon in the Jupyterlab launch pad.
As described in the default message that appears in all newly-launched terminals, to create a Rubin Observatory environment in a JupyterLab terminal session and set up the full set of packages, users must first execute:

.. code-block:: bash

   setup lsst_distrib

For example, once the above command has been executed, `Butler command-line tools <https://pipelines.lsst.io/modules/lsst.daf.butler/scripts/butler.html>`_ to query data sets will be available.
Type ``butler --help`` in any terminal to see a list of available Butler command-line functionality.
