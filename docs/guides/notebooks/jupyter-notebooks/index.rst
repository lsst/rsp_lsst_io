#######################
Using Jupyter Notebooks
#######################

.. _NB-Intro-Use-A-NB:

How to use a Jupyter notebook
=============================

**Executing code in a Notebook:**
Jupyter notebooks provide "cells" within which is typed either Python code or markdown language (for formatted text).
Choose the cell to execute by clicking in it with the mouse (the cursor must be in the desired cell).
Hold down the *shift* key and press either *enter* or *return* (depending on keyboard type), or click the 'Play' button in the notebook toolbar, and the contents of the cell will be executed.
If the cell type is code, and the cell contains python code, the code will be executed.
If the cell type is markdown, then it will be rendered upon execution to yield nicely formatted text.
There is a `user guide for markdown cells in the Jupyter Notebooks documentation <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html>`_.

Jupyter notebook cells can be executed out of order. This provides a degree of flexibility in executing Jupyter notebooks, but could also lead to errors if, for instance, a cell is executed before prior cells that define necessary functions and/or variables. If you've executed a notebook's cells out of order and are concerned about having caused potential issues in doing so, you can restart the notebook's kernel.

  .. figure:: images/notebook.png
      :name: notebook_aspect
      :alt: This image is a screenshot of a Rubin tutorial notebook. The notebook has been scrolled down to Section 3.3, which contains both markdown text and code cells which have been executed. The last code cell has produced a greyscale sky image.

      A screenshot from an executed Rubin/LSST tutorial notebook. Multiple notebooks can be opened in separate tabs.

**Opening Multiple Notebooks:**
Multiple notebooks and terminals can be open at a time.
Notebooks and/or terminal windows can be arranged next to or on top of each other by dragging the notebook or terminal around by the top bar.
Arranging the windows can be convenient when working in both a terminal and notebook at the same time, or when using another notebook as a reference.

**JupyterLab Autosaves Notebooks:**
Note that JupyterLab autosaves notebooks at a default interval of 2 minutes
unless working in the directory "notebooks/tutorial-notebooks/", which is read-only (see :ref:`NB-Intro-Use-Tutorial-NBs`).

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: How-to guides

   tutorial-notebooks
