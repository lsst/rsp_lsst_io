#######################################
Introduction to the RSP Notebook Aspect
#######################################

The Notebook aspect enables you to do scientific analysis in your web browser by running Jupyter Notebooks and shell scripts.
The Notebook aspect is powered by JupyterLab_.

Most RSP users will find Jupyter Notebooks to be the most efficient and powerful way to interact with the LSST data sets.

**Always save and shutdown all notebooks and log out of JupyterLab when you are done with your day's work.**
This is important to preserve resources for other users and to ensure you re-enter the RSP in a known state every time.
To help users avoid issues with stale instances, sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.

This page focuses on the basic instructions for using the RSP Notebook Aspect, and a few FAQs and Troubleshooting Tips.
The full documentation for the RSP Notebook Aspect is available at `nb.lsst.io <https://nb.lsst.io/>`_.

.. _NB-Intro-Login:

How to log in, navigate, and log out of JupyterLab
==================================================

From the RSP landing page at `data.lsst.cloud <https://data.lsst.cloud/>`_ click on the central panel for Notebooks.

**Software Version and Server Size:**
The first page offers a choice of software environment version (left) and server size (right), as shown in the next figure.
Most users will choose the recommended software version and a medium server size.

   .. image:: images/RSP_NB_select_a_server.png
       :alt: This image is a screenshot of the Server Options page that users encounter first when they log into the Notebook Aspect. At left, users can select the version of the LSST Science Pipelines that they want to use, with the recommended version pre-selected as the default. At right, users can select a server size of small, medium, or large. Small is pre-selected as the default. Two additional options to enable debug logs or clear the user’s dot-local directory also appear at right. Neither of these options are pre-selected. At the bottom is a button marked start.
       :width: 400
       :name: RSP_NB_select_a_server

A screenshot of the server options available to RSP users, with the default options selected as indicated by the blue filled circles. Users should choose the recommended software version and a medium size.

The term "image" atop the left box refers to a "Docker image" that defines the software packages and their versions which will be automatically loaded in the server environment.
The "recommended" image will be updated on a regular (monthly) basis to encourage users to adapt to using software that is in active development, and to benefit from the bug fixes and updates made by Rubin Observatory staff.
Older images will remain accessible to users.

RSP users who are doing a lot of image processing might need to select a large server, and those who are working with small subsets of catalog data can use a small server.

**Start the Server:**
Pressing the orange "Start" button to start the server returns this page with a blue progress bar:

   .. image:: images/RSP_NB_progress_bar.png
       :alt: This image is a screenshot of the progress bar that displays for a minute or two while a user’s server is starting up in the Notebook Aspect. At the top there is text that says “Your server is starting up” and “You will be redirected automatically when it’s ready for you.” Below that is a progress bar. Underneath the bar, the date and time is shown. This page is not interactive and is replaced by the main work area of the Notebook Aspect once the server has started.
       :width: 400
       :name: RSP_NB_progress_bar

A screenshot of the progress bar that will show while the server is starting up. Be patient. Sometimes it takes a couple of minutes to start a server.

**Navigating the JupyterLab Interface:**
The JupyterLab landing page in the figure below is the launch pad for all JupyterLab functionality (e.g., Notebook, Terminal, Python console).
Return to this launch pad at any time by clicking the plus symbol at upper-left.

  .. image:: images/RSP_NB_launcher_options.png
      :alt: This image is a screenshot of the main work area of the Notebook Aspect, as it appears when a user starts a new server. Across the top is the main menu, with options such as file, edit, view, run, kernel, rubin, tabs, settings, and help. The left sidebar offers options to browse the file system, open files, and upload data. At right, in the main work area, one tab is open. It is the launcher tab, which offers options to open a new notebook, coding console, terminal, text file, markdown file, python file, or help file.
      :width: 400
      :name: RSP_NB_launcher_options

The JupyterLab landing page from which several tools can be launched and the file system can be browsed (left sidebar).

In the very left-most vertical sidebar of icons, the top icon is a file folder, and that is the default view.
The left sidebar lists folders in the user's home directory (e.g., DATA, WORK, and notebooks).
Launching a terminal (the default is a linux bash terminal) and using the command "ls" will return the same list.
Navigate the file system and open files by double-clicking on folders and files in the left sidebar.

Although the file browser is a handy way to navigate your user home space, it does not allow you to navigate to, e.g., the shared data space.
One way to make other spaces available in the file browser is to create a `symbolic link <https://en.m.wikipedia.org/wiki/Symbolic_link>`_ using the Terminal to the desired space somewhere in your home directory.

Jupyter Notebooks can be identified by their file extension ".ipynb".
All users will find a set of tutorial notebooks provided in the "notebooks/tutorial-notebooks/" directory.

**Safely Log Out of JupyterLab:**
Use the "File" menu in the top menu bar.
To safely shut down a Notebook, choose "Close and Shutdown Notebook".
To safely shut down a JupyterLab server and log out of the RSP, choose "Save all, Exit, and Log Out".
It is recommended you log out every time you are finished with a session in order to both preserve resources for other users and to ensure you re-enter the RSP in a known state every time.
To help users avoid issues with stale instances, sessions will be automatically shut-down after 5 days of inactivity, or after 25 days.


.. _NB-Intro-Use-A-JL-terminal:

How to use the JupyterLab terminal
==================================

The `DP0.2 Data Products Definition Document (DPDD) <https://dp0-2.lsst.io/data-products-dp0-2/index.html#dp0-2-data-products-dpdd>`_ and the LSST Science Pipelines tools can both be accessed from the command line of a JupyterLab terminal tab.
A terminal session can be started by clicking on the terminal icon in the Jupyterlab launch pad.
As described in the default message that appears in all newly-launched terminals, to create a Rubin Observatory environment in a JupyterLab terminal session and set up the full set of packages, users must first execute:

.. code-block:: bash

   source ${LOADSTACK}
   setup lsst_distrib

For example, to query and retrieve data sets using the Butler (see `What is the Butler, and when do I use it? <https://dp0-2.lsst.io/data-access-analysis-tools/nb-intro.html#nb-intro-use-a-nb-faq-butler>`_, below), command-line tools are available as `documented here <https://pipelines.lsst.io/v/weekly/modules/lsst.daf.butler/scripts/butler.html>`_.
Type ``butler --help`` in any terminal to see a list of available butler functionality.


.. _NB-Intro-Use-A-NB:

How to use a Jupyter notebook
=============================

**Executing code in a Notebook:**
Jupyter notebooks provide "cells" within which you type either Python code or markdown language (for formatted text).
Choose the cell to execute by clicking in it with your mouse (the cursor must be in the desired cell).
Hold down the *shift* key and press either *enter* or *return* (depending on your keyboard type), or click the 'Play' button in the notebook toolbar, and the contents of the cell will be executed.
If the cell type is code, and the cell contains python code, the code will be executed.
If the cell type is markdown, then it will be rendered upon execution to yield nicely formatted text.
There is a `user guide for markdown cells in the Jupyter Notebooks documentation <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html>`_.

  .. figure:: images/notebook.png
      :name: notebook_aspect
      :alt: This image is a screenshot of tutorial notebook 01, titled introduction to DP0.2. The notebook has been scrolled down to Section 3.3, which contains both markdown text and code cells which have been executed. The last code cell has produced a greyscale image of a rich galaxy cluster. Across the top of the notebook there is a menu bar of actions for users. Actions include save notebook, set cell type, and insert, cut, copy, paste, run, or interrupt cells. 

      A screenshot from the end of tutorial notebook 01 “Introduction to DP0.2”, showing the panel of the Notebook Aspect where multiple interface tabs can be open at once. In this case, the first tab is a command-line terminal, the second is the Launcher interface, and the third (which is currently selected) is an executed version of tutorial notebook 01. Multiple notebooks can be opened in separate tabs.


.. toctree::
   :maxdepth: 2
   :titlesonly:

   starting-and-stopping/index
   Using the Science Pipelines <science-pipelines/index>
   configuration/index
