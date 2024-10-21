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

**Opening Multiple Notebooks:**
You can have multiple notebooks and terminals open in your viewer at a time.
This is very handy, but you can also arrange both notebooks and terminals next to or on top of each other by dragging the notebook or terminal around by the top bar.
Arranging the windows can be convenient when working in both a terminal and notebook at the same time, or when using another notebook as a reference.

**JupyterLab Autosaves Notebooks:**
Note that JupyterLab autosaves your notebooks at a default interval of 2 minutes
unless you are working in the directory "notebooks/tutorial-notebooks/", which is read-only (see next section).


.. toctree::
   :maxdepth: 2
   :titlesonly:

   starting-and-stopping/index
   Using the Science Pipelines <science-pipelines/index>
   configuration/index
   tutorial-notebooks/index
   jupyterlab-terminal/index
   faq/index
