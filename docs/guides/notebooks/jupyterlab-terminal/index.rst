#############################
Using the JupyterLab Terminal
#############################

.. _NB-Intro-Use-A-JL-terminal:

How to use the JupyterLab terminal
==================================

Launching a JupyterLab terminal window is an option within the Notebook Aspect's Launcher window:

  .. figure:: images/RSP_NB_launcher_options.png
      :alt: This image is a screenshot of the main work area of the Notebook Aspect, as it appears when a user starts a new server. Across the top is the main menu, with options such as file, edit, view, run, kernel, rubin, tabs, settings, and help. The left sidebar offers options to browse the file system, open files, and upload data. At right, in the main work area, one tab is open. It is the launcher tab, which offers options to open a new notebook, coding console, terminal, text file, markdown file, python file, or help file.
      :width: 400
      :name: RSP_NB_launcher_options

      The JupyterLab Launcher page from which the JupyterLab terminal can be selected (black square icon labeled "Terminal" under "Other").

Click the black square icon labeled "Terminal" to launch a new JupyterLab terminal window.

The Rubin/LSST data products and the `LSST Science Pipelines`_ tools can both be accessed from the command line of a JupyterLab terminal tab.
A terminal session can be started by clicking on the terminal icon in the Jupyterlab launch pad.
As described in the default message that appears in all newly-launched terminals, to create a Rubin Observatory environment in a JupyterLab terminal session and set up the full set of packages, users must first execute:

.. code-block:: bash

   setup lsst_distrib

For example, once the above command has been executed, `Butler command-line tools <https://pipelines.lsst.io/modules/lsst.daf.butler/scripts/butler.html>`_ to query data sets will be available.
Type ``butler --help`` in any terminal to see a list of available Butler command-line functionality.
