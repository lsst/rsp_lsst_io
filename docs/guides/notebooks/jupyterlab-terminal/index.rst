#############################
Using the JupyterLab Terminal
#############################

.. _NB-Intro-Use-A-JL-terminal:

How to use the JupyterLab terminal
==================================

The `DP0.2 Data Products Definition Document (DPDD) <https://dp0-2.lsst.io/data-products-dp0-2/index.html#dp0-2-data-products-dpdd>`_ and the `LSST Science Pipelines`_ tools can both be accessed from the command line of a JupyterLab terminal tab.
A terminal session can be started by clicking on the terminal icon in the Jupyterlab launch pad.
As described in the default message that appears in all newly-launched terminals, to create a Rubin Observatory environment in a JupyterLab terminal session and set up the full set of packages, users must first execute:

.. code-block:: bash

   setup lsst_distrib

For example, to query and retrieve data sets using the Butler (see `What is the Butler, and when do I use it? <https://dp0-2.lsst.io/data-access-analysis-tools/nb-intro.html#nb-intro-use-a-nb-faq-butler>`_, below), command-line tools are available as `documented here <https://pipelines.lsst.io/v/weekly/modules/lsst.daf.butler/scripts/butler.html>`_.
Type ``butler --help`` in any terminal to see a list of available butler functionality.
